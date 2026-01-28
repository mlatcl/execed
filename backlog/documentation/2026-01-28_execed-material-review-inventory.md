---
category: documentation
created: "2026-01-28"
id: 2026-01-28_execed-material-review-inventory
last_updated: "2026-01-28"
owner: Neil D. Lawrence
priority: High
related_cips:
  - "0002"
status: In Progress
tags:
  - execed
  - material-review
  - snippets
title: "Material review: build inventories (lectures, talks, snippets)"
---

# Task: Material review — build inventories (lectures, talks, snippets)

## Description

Create the repeatable “inventory layer” for CIP-0002:

- Parse `execed/_lamd/*.md` to extract `\include{...}` usage per session.
- Parse recent talks (at least `~/lawrennd/talks/_atomic-human/`, `_business/`, `_policy/`, `_economics/`) to extract snippet usage since a cutoff date (default `2024-06-01`).
- Produce machine-readable outputs (JSON/CSV) suitable for reuse in future reviews.

## Acceptance Criteria

- [ ] We can answer “which snippets does ExecEd use?” (session → includes, include → sessions).
- [ ] We can answer “which talks use these snippets since 2024-06-01?” (include → talks, talk → includes).
- [ ] We can answer “which snippets are pulled in transitively?” (includes inside included snippets).
- [ ] Outputs are written to a deterministic location (e.g. `backlog/artifacts/` or similar) and can be regenerated.

## Notes

- Backlog items should link to CIPs (HOW), not requirements (WHAT).
- This task is intentionally “inventory only” — recommendations and refresh proposals come in follow-on tasks.

## Progress Updates

### 2026-01-28

Started implementation. Initial inventory script added under `tools/material_review/` and can write outputs to `artifacts/material-review/`.

Updated approach:

- Inventory now prefers `_lamd/lectures.csv` when present, so it only indexes the actual lecture source files (avoids pulling in macro `.gpp` helper files).
- Added an optional transitive mode for nested snippet usage:
  - `--transitive` computes `includes_transitive` per file by expanding `\include{...}` inside included snippets.
  - `--snippets-root /Users/neil/lawrennd/snippets` is used to resolve include targets like `_ai/includes/foo.md` to real paths.
- Current command (ExecEd + recent talks, transitive):

  - `python3 tools/material_review/inventory.py --execed-lamd _lamd --talks-dir /Users/neil/lawrennd/talks/_atomic-human --talks-dir /Users/neil/lawrennd/talks/_business --since 2024-06-01 --snippets-root /Users/neil/lawrennd/snippets --transitive --out-dir artifacts/material-review`

