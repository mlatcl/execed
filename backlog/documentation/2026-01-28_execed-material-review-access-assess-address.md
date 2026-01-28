---
category: documentation
created: "2026-01-28"
id: 2026-01-28_execed-material-review-access-assess-address
last_updated: "2026-01-28"
owner: Neil D. Lawrence
priority: Medium
related_cips:
  - "0002"
status: Proposed
tags:
  - execed
  - material-review
  - data-readiness
  - fynesse
  - access-assess-address
title: "Material review: integrate Access/Assess/Address (Fynesse) with ExecEd DRLs"
---

# Task: Material review — integrate Access/Assess/Address (Fynesse) with ExecEd DRLs

## Description

ExecEd Session 2 (`_lamd/the-data-crisis.md`) uses **Data Readiness Levels** (DRLs) as “instrumentation”, but it does not currently surface the **Access / Assess / Address** (Fynesse) framing that makes DRLs operational and memorable.

AdvDS has a mature treatment of this, including a canonical snippet:

- `~/lawrennd/snippets/_data-science/includes/access-assess-address.md`

…which explicitly links:

- **Access** ↔ **DRL-C**
- **Assess** ↔ **DRL-B**
- **Address** ↔ **DRL-A**

This task ensures we don’t miss that material, and decides how best to bring it into ExecEd (likely as a short executive-friendly “micro-anchor” rather than the full long-form snippet).

## Inputs

- ExecEd Session 2 source: `execed/_lamd/the-data-crisis.md`
- ExecEd walkthrough: `backlog/documentation/2026-01-28_execed-material-review-session-walkthrough.md`
- AdvDS lecture sources that already integrate the framework:
  - `~/mlatcl/advds/_lamd/a-data-science-process.md` (includes `access-assess-address` + `fynesse-template`)
  - `~/mlatcl/advds/_lamd/the-data-science-landscape.md` (also includes `access-assess-address`)
- AdvDS tenet (for framing language): `~/mlatcl/advds/tenets/advds/fynesse-framework.md`
- Canonical snippet sources (snippets repo):
  - `~/lawrennd/snippets/_data-science/includes/access-assess-address.md`
  - `~/lawrennd/snippets/_data-science/includes/fynesse-template.md`
  - (related, practical example) `~/lawrennd/snippets/_ml/includes/access-assess-address-framework.md`

## Acceptance Criteria

- [ ] We have a short summary of the AdvDS “Access/Assess/Address” framing in ExecEd terms (decisions, incentives, accountability).
- [ ] We decide whether ExecEd should:
  - [ ] reuse `_data-science/includes/access-assess-address.md` directly, or
  - [ ] create an **exec micro-snippet** (preferred) that captures the mapping to DRLs without the long examples.
- [ ] Session 2 walkthrough includes a clear “proposed snippet change” to introduce the framework alongside DRLs.
- [ ] If a new micro-snippet is needed, a follow-on backlog task is created to implement it (in `~/lawrennd/snippets/`) and to update ExecEd Session 2 once ready.

## Notes (initial findings)

- AdvDS already treats “Access/Assess/Address” as the **process vocabulary** that makes DRLs usable in practice (not just maturity badges).
- ExecEd Session 2 already has the right narrative space for this: it frames DRLs as instrumentation and focuses on incentives, escalation, and accountability.
