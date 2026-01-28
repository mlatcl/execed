---
category: documentation
created: "2026-01-28"
id: 2026-01-28_execed-material-review-snippet-freshness
last_updated: "2026-01-28"
owner: Neil D. Lawrence
priority: High
related_cips:
  - "0002"
status: Proposed
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

