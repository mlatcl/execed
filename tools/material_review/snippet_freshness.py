#!/usr/bin/env python3
"""
Snippet freshness report (CIP-0002).

Reads an inventory.json produced by tools/material_review/inventory.py and computes:
- last change date + subject line (git) for each referenced snippet in ~/lawrennd/snippets
- frequency signals (execed_count, talks_count)

No third-party dependencies.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import subprocess
from pathlib import Path
from typing import Optional


def git_last_change(repo_dir: Path, rel_path: str) -> tuple[Optional[str], Optional[str]]:
    """
    Return (YYYY-MM-DD, subject) for rel_path inside repo_dir, or (None, None).
    """
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_dir), "log", "-1", "--format=%cs%n%s", "--", rel_path],
            stderr=subprocess.DEVNULL,
            text=True,
        )
    except Exception:
        return None, None
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    if not lines:
        return None, None
    date = lines[0]
    subject = lines[1] if len(lines) > 1 else None
    return date, subject


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory", type=Path, default=Path("artifacts/material-review/inventory.json"))
    ap.add_argument("--snippets-repo", type=Path, default=Path("/Users/neil/lawrennd/snippets"))
    ap.add_argument("--out-dir", type=Path, default=Path("artifacts/material-review"))
    ap.add_argument("--stale-days", type=int, default=365)
    ap.add_argument(
        "--use-transitive",
        action="store_true",
        help="Use include_frequency_transitive (includes inside included snippets) when available",
    )
    args = ap.parse_args()

    inv = json.loads(args.inventory.read_text())
    freq = {}
    # include_frequency.csv has combined totals, but inventory.json has separate dicts.
    execed_key = "include_frequency_transitive" if args.use_transitive else "include_frequency"
    talks_key = "include_frequency_transitive" if args.use_transitive else "include_frequency"
    execed_freq = inv.get("execed", {}).get(execed_key, {}) or {}
    talks_freq = inv.get("talks", {}).get(talks_key, {}) or {}
    all_includes = sorted(set(execed_freq.keys()) | set(talks_freq.keys()))

    rows = []
    today = dt.date.today()
    for inc in all_includes:
        # Only treat snippet paths as those that look like snippets includes.
        if not (inc.startswith("_") and "/includes/" in inc and inc.endswith(".md")):
            continue
        rel = inc.lstrip("/")  # snippets repo paths are like "_ai/includes/foo.md"
        date_s, subject = git_last_change(args.snippets_repo, rel)
        stale = None
        if date_s:
            try:
                d = dt.date.fromisoformat(date_s)
                stale = (today - d).days
            except ValueError:
                stale = None
        rows.append(
            {
                "include": inc,
                "snippets_path": str(args.snippets_repo / rel),
                "execed_count": int(execed_freq.get(inc, 0)),
                "talks_count": int(talks_freq.get(inc, 0)),
                "total_count": int(execed_freq.get(inc, 0)) + int(talks_freq.get(inc, 0)),
                "last_updated": date_s,
                "last_commit_subject": subject,
                "days_since_update": stale,
                "stale": bool(stale is not None and stale > args.stale_days),
            }
        )

    # sort: high total usage, then stalest
    rows.sort(key=lambda r: (-r["total_count"], -(r["days_since_update"] or -1), r["include"]))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_json = args.out_dir / "snippet_freshness.json"
    out_csv = args.out_dir / "snippet_freshness.csv"

    out_json.write_text(
        json.dumps(
            {
                "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                "snippets_repo": str(args.snippets_repo),
                "stale_days": args.stale_days,
                "use_transitive": bool(args.use_transitive),
                "rows": rows,
            },
            indent=2,
            sort_keys=True,
        )
    )

    with out_csv.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "include",
                "snippets_path",
                "execed_count",
                "talks_count",
                "total_count",
                "last_updated",
                "days_since_update",
                "stale",
                "last_commit_subject",
            ]
        )
        for r in rows:
            w.writerow(
                [
                    r["include"],
                    r["snippets_path"],
                    r["execed_count"],
                    r["talks_count"],
                    r["total_count"],
                    r["last_updated"],
                    r["days_since_update"],
                    r["stale"],
                    r["last_commit_subject"] or "",
                ]
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

