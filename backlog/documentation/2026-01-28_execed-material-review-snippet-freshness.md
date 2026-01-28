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

Initial high-impact stale candidates (high `total_count`, `stale=True`) from `artifacts/material-review/snippet_freshness.csv`:

- `_data-science/includes/new-flow-of-information.md` (total 41, last_updated 2024-09-28)
- `_data-science/includes/new-flow-of-information-ham.md` (total 39, last_updated 2024-05-17)
- `_ai/includes/processor-ham.md` (total 31, last_updated 2024-09-16)
- `_ai/includes/conversation-computer.md` (total 29, last_updated 2023-11-06)
- `_simulation/includes/the-moniac.md` (total 28, last_updated 2024-03-28)
- `_ai/includes/conversation-tedx.md` (total 27, last_updated 2023-11-06)

Notes:

- The “new flow of information” spine is both high-usage and stale → a prime refresh target for long-term coherence.
- Conversation snippets are high-usage and stale → consider a refresh to align language/examples with the post‑2024 agent framing.

