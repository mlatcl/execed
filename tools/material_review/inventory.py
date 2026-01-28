#!/usr/bin/env python3
"""
Material review inventory (CIP-0002).

Builds a simple inventory of \\include{...} usage across:
- ExecEd lecture sources (execed/_lamd/*.md)
- Talk sources (e.g. ~/lawrennd/talks/_atomic-human/, _business/, _policy/, _economics/)

Outputs:
- JSON (full inventory + frequency tables)
- CSV (include frequency table)

Design goals:
- No third-party dependencies.
- Works even if target directories live outside this repo.
- Can be upstreamed/mirrored into lamd tooling later.
"""

from __future__ import annotations

import argparse
import csv
import dataclasses
import datetime as dt
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Iterable, Optional


INCLUDE_RE = re.compile(r"\\include\{([^}]+)\}")


SKIP_DIR_NAMES = {
    ".git",
    "_site",
    ".jekyll-cache",
    ".sass-cache",
    "vendor",
    ".venv",
    ".venv-vibesafe",
    "__pycache__",
    ".ipynb_checkpoints",
}


SKIP_FILE_SUFFIXES = (
    ".posts.html",
    ".posts.html.markdown",
    ".slides.html",
    ".slides.html.markdown",
    ".notes.ipynb.markdown",
    ".ipynb",
)


def run_git_last_change_date(repo_dir: Path, file_path: Path) -> Optional[dt.date]:
    """
    Return last-change date for file via git, or None if unavailable.
    """
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_dir), "log", "-1", "--format=%cs", "--", str(file_path)],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return None
    if not out:
        return None
    try:
        return dt.date.fromisoformat(out)
    except ValueError:
        return None


def find_repo_root(start: Path) -> Optional[Path]:
    cur = start.resolve()
    if cur.is_file():
        cur = cur.parent
    for p in [cur] + list(cur.parents):
        if (p / ".git").exists():
            return p
    return None


def iter_source_files(root: Path) -> Iterable[Path]:
    """
    Yield .md and .gpp.markdown files under root, skipping generated artifacts.
    """
    root = root.resolve()
    if not root.exists():
        return
    for dirpath, dirnames, filenames in os.walk(root):
        # prune
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_NAMES]
        for name in filenames:
            p = Path(dirpath) / name
            if name.endswith(SKIP_FILE_SUFFIXES):
                continue
            if name.endswith(".md") or name.endswith(".gpp.markdown"):
                yield p


def iter_lecture_files_from_csv(lamd_dir: Path) -> Iterable[Path]:
    """
    Yield lecture source files based on lamd_dir/lectures.csv.

    This avoids accidentally indexing talk macros and other helper .gpp files
    that live alongside lectures in some repos.
    """
    csv_path = lamd_dir / "lectures.csv"
    if not csv_path.exists():
        return
    try:
        rows = csv_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except Exception:
        return
    if not rows:
        return
    for stub in rows[1:]:
        stub = stub.strip()
        if not stub:
            continue
        md = lamd_dir / f"{stub}.md"
        gpp = lamd_dir / f"{stub}.gpp.markdown"
        if md.exists():
            yield md
        elif gpp.exists():
            yield gpp


def parse_frontmatter_session(md_text: str) -> Optional[str]:
    """
    Best-effort frontmatter parse for 'session:' value.
    """
    lines = md_text.splitlines()
    if not (lines and lines[0].strip() == "---"):
        return None
    # find second ---
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None
    for line in lines[1:end]:
        if line.strip().startswith("session:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return None


def extract_includes(md_text: str) -> list[str]:
    return sorted({m.group(1).strip() for m in INCLUDE_RE.finditer(md_text)})


def resolve_include_path(
    include: str,
    *,
    source_file: Path,
    snippets_roots: list[Path],
) -> Optional[Path]:
    """
    Best-effort mapping from an \\include{...} target to a real file path.

    Rules:
    - If include is an absolute path and exists, use it.
    - If include starts with '_' (e.g. _ai/includes/foo.md), try snippets_roots/<include>.
    - Otherwise, treat as relative to the source file directory.
    """
    inc = include.strip()
    if not inc:
        return None

    p = Path(inc)
    if p.is_absolute():
        return p if p.exists() else None

    if inc.startswith("_"):
        for root in snippets_roots:
            cand = (root / inc).resolve()
            if cand.exists():
                return cand

    cand = (source_file.parent / inc).resolve()
    if cand.exists():
        return cand

    return None


def extract_includes_transitive(
    *,
    root_text: str,
    root_file: Path,
    snippets_roots: list[Path],
    max_depth: int = 5,
) -> list[str]:
    """
    Return transitive closure of includes by recursively expanding included snippets.

    Output is a sorted, de-duplicated list of include strings (the literal \\include{...} targets),
    including both direct and nested includes.
    """
    seen_includes: set[str] = set()
    seen_files: set[Path] = set()

    def walk(text: str, file_path: Path, depth: int) -> None:
        if depth > max_depth:
            return
        for inc in extract_includes(text):
            if inc in seen_includes:
                continue
            seen_includes.add(inc)
            resolved = resolve_include_path(inc, source_file=file_path, snippets_roots=snippets_roots)
            if resolved is None:
                continue
            if resolved in seen_files:
                continue
            seen_files.add(resolved)
            try:
                child_text = resolved.read_text(errors="ignore")
            except Exception:
                continue
            walk(child_text, resolved, depth + 1)

    walk(root_text, root_file, 0)
    return sorted(seen_includes)


@dataclasses.dataclass(frozen=True)
class FileInventory:
    path: str
    includes: list[str]
    includes_transitive: Optional[list[str]] = None
    session: Optional[str] = None
    last_changed: Optional[str] = None  # YYYY-MM-DD when available


def build_inventory(
    roots: list[Path],
    since: Optional[dt.date],
    *,
    transitive: bool,
    snippets_roots: list[Path],
    max_depth: int,
) -> list[FileInventory]:
    inv: list[FileInventory] = []
    for root in roots:
        repo_root = find_repo_root(root)
        files: Iterable[Path]
        if root.is_dir() and (root / "lectures.csv").exists():
            files = iter_lecture_files_from_csv(root)
        else:
            files = iter_source_files(root)
        for f in files:
            try:
                txt = f.read_text(errors="ignore")
            except Exception:
                continue
            includes = extract_includes(txt)
            if not includes:
                continue
            includes_transitive: Optional[list[str]] = None
            if transitive:
                includes_transitive = extract_includes_transitive(
                    root_text=txt,
                    root_file=f,
                    snippets_roots=snippets_roots,
                    max_depth=max_depth,
                )

            session = parse_frontmatter_session(txt)

            last_changed: Optional[dt.date] = None
            if repo_root is not None:
                last_changed = run_git_last_change_date(repo_root, f)
            if last_changed is None:
                try:
                    last_changed = dt.date.fromtimestamp(f.stat().st_mtime)
                except Exception:
                    last_changed = None

            if since is not None and last_changed is not None and last_changed < since:
                continue

            inv.append(
                FileInventory(
                    path=str(f),
                    includes=includes,
                    includes_transitive=includes_transitive,
                    session=session,
                    last_changed=last_changed.isoformat() if last_changed else None,
                )
            )
    return inv


def include_frequency(items: list[FileInventory]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for it in items:
        for inc in it.includes:
            freq[inc] = freq.get(inc, 0) + 1
    return dict(sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])))


def include_frequency_transitive(items: list[FileInventory]) -> dict[str, int]:
    """
    Frequency table based on transitive includes (includes inside included snippets).

    If a FileInventory has no includes_transitive, it contributes nothing.
    """
    freq: dict[str, int] = {}
    for it in items:
        if not it.includes_transitive:
            continue
        for inc in it.includes_transitive:
            freq[inc] = freq.get(inc, 0) + 1
    return dict(sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--execed-lamd", type=Path, default=Path("execed/_lamd"))
    ap.add_argument("--talks-dir", type=Path, action="append", default=[])
    ap.add_argument("--snippets-root", type=Path, action="append", default=[], help="Root of snippets repo (e.g. ~/lawrennd/snippets)")
    ap.add_argument("--transitive", action="store_true", help="Also compute transitive includes by expanding included snippets")
    ap.add_argument("--max-depth", type=int, default=5, help="Max recursion depth for transitive include expansion")
    ap.add_argument("--since", type=str, default=None, help="Only include files changed on/after YYYY-MM-DD")
    ap.add_argument("--out-dir", type=Path, default=None, help="Write outputs to this directory")
    args = ap.parse_args()

    since: Optional[dt.date] = None
    if args.since:
        since = dt.date.fromisoformat(args.since)

    snippets_roots = [p.expanduser().resolve() for p in (args.snippets_root or [])]

    execed_items = build_inventory(
        [args.execed_lamd],
        since=None,
        transitive=args.transitive,
        snippets_roots=snippets_roots,
        max_depth=args.max_depth,
    )
    talks_items = (
        build_inventory(
            args.talks_dir,
            since=since,
            transitive=args.transitive,
            snippets_roots=snippets_roots,
            max_depth=args.max_depth,
        )
        if args.talks_dir
        else []
    )

    out = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "since": since.isoformat() if since else None,
        "execed": {
            "root": str(args.execed_lamd),
            "files": [dataclasses.asdict(x) for x in execed_items],
            "include_frequency": include_frequency(execed_items),
            "include_frequency_transitive": include_frequency_transitive(execed_items) if args.transitive else {},
        },
        "talks": {
            "roots": [str(p) for p in args.talks_dir],
            "files": [dataclasses.asdict(x) for x in talks_items],
            "include_frequency": include_frequency(talks_items),
            "include_frequency_transitive": include_frequency_transitive(talks_items) if args.transitive else {},
        },
    }

    if args.out_dir:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        json_path = args.out_dir / "inventory.json"
        csv_path = args.out_dir / "include_frequency.csv"

        json_path.write_text(json.dumps(out, indent=2, sort_keys=True))

        # CSV: combined include frequency with execed + talks counts
        execed_freq = out["execed"]["include_frequency"]
        talks_freq = out["talks"]["include_frequency"]
        all_incs = sorted(set(execed_freq.keys()) | set(talks_freq.keys()))
        with csv_path.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["include", "execed_count", "talks_count", "total"])
            for inc in all_incs:
                e = int(execed_freq.get(inc, 0))
                t = int(talks_freq.get(inc, 0))
                w.writerow([inc, e, t, e + t])

    else:
        print(json.dumps(out, indent=2, sort_keys=True))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

