---
category: features
created: "2026-01-28"
id: 2026-01-28_execed-material-review-tooling
last_updated: "2026-01-28"
owner: Neil D. Lawrence
priority: Medium
related_cips:
  - "0002"
status: Proposed
tags:
  - execed
  - material-review
  - tooling
  - lamd
title: "Material review tooling: scripts now, upstream to lamd later"
---

# Task: Material review tooling — scripts now, upstream to `lamd` later

## Description

Create reusable tooling to run the CIP-0002 inventories repeatedly and share them with others.

Phase 1 (ExecEd-local):

- Add scripts under `execed/scripts/` that generate:
  - snippet usage inventory for a target directory (lectures, talks)
  - snippet freshness report from git history
  - a markdown summary report + JSON/CSV artifacts

Phase 2 (Upstream design):

- Identify which commands should become `lamd` tooling (e.g. a subcommand or helper CLI).
- Draft the interface (inputs, outputs, flags like `--since`, `--scope`, `--format json/csv/md`).

## Acceptance Criteria

- [ ] A new script entrypoint exists for running the inventories end-to-end.
- [ ] Outputs are stable and suitable for long-term reuse (machine-readable + human report).
- [ ] A short upstream proposal is written (what should land in `lamd`, with CLI shape).

