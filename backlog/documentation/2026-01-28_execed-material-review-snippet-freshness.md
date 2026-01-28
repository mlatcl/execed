---
category: documentation
created: "2026-01-28"
id: 2026-01-28_execed-material-review-snippet-freshness
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
  - git
title: "Material review: snippet freshness report (git-based)"
---

# Task: Material review — snippet freshness report (git-based)

## Description

Using the inventories from CIP-0002, compute snippet “freshness”:

- For each referenced snippet, find last-change date (git history) and last commit message.
- Flag stale snippets (e.g. older than a configurable threshold such as 12 months) and high-churn snippets (recently changing frequently).
- Produce a ranked list combining **usage frequency** (ExecEd + recent talks) with **staleness/churn** so we can prioritise refresh work.

## Acceptance Criteria

- [ ] A report exists listing snippet path → last updated date → last commit message.
- [ ] A “top candidates for refresh” list exists with rationale (high-impact + stale, or high-impact + unstable).
- [ ] Results are reproducible (one command/script regenerates them).

## Progress Updates

### 2026-01-28

Started implementation. Added `tools/material_review/snippet_freshness.py` and generated an initial report under `artifacts/material-review/`.

Re-run with updated inventory tooling:

- Uses **transitive include counts** (includes inside included snippets) via `--use-transitive`.
- Includes recent talks since `2024-06-01` from:
  - `/Users/neil/lawrennd/talks/_atomic-human`
  - `/Users/neil/lawrennd/talks/_business`

Command:

- `python3 tools/material_review/snippet_freshness.py --inventory artifacts/material-review/inventory.json --snippets-repo /Users/neil/lawrennd/snippets --out-dir artifacts/material-review --use-transitive`

Current high-impact candidates (high `total_count`; staleness varies) from `artifacts/material-review/snippet_freshness.json`:

- `_ai/includes/anne-bob-talk.md` (total 31, last_updated 2026-01-09, stale=False)
- `_ai/includes/processor-ham.md` (total 30, last_updated 2024-09-16, stale=True)
- `_data-science/includes/new-flow-of-information.md` (total 30, last_updated 2024-09-28, stale=True)
- `_data-science/includes/new-flow-of-information-ham.md` (total 29, last_updated 2024-05-17, stale=True)
- `_ai/includes/the-atomic-eye.md` (total 29, last_updated 2025-02-11, stale=False)
- `_simulation/includes/the-moniac.md` (total 28, last_updated 2024-03-28, stale=True)
- `_ai/includes/conversation-computer.md` (total 27, last_updated 2023-11-06, stale=True)
- `_ai/includes/conversation-tedx.md` (total 27, last_updated 2023-11-06, stale=True)
- `_atomic-human/includes/trust-autonomy-embodiment.md` (total 21, last_updated 2026-01-21, stale=False)

Notes:

- The “new flow of information” spine remains **high-usage and stale** → still a prime refresh target.
- Conversation snippets are **high-usage and stale** → good candidates for post‑2024 agent framing updates.

