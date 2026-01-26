---
category: documentation
created: '2026-01-26'
id: 2026-01-26_execed-tenet-outcome-lecture-crosswalk
last_updated: '2026-01-26'
owner: Neil D. Lawrence
priority: High
related_cips:
- '0001'
status: In Progress
tags:
- execed
- tenets
- outcomes
- lectures
- snippets
- traceability
title: Create tenet ↔ outcome ↔ lecture ↔ snippet crosswalk for execed
---

# Task: Tenet ↔ outcome ↔ lecture ↔ snippet crosswalk

## Description

Produce a single mapping artefact that makes the course coherent and maintainable:

- **Tenets (WHY)** in `tenets/execed/`
- **Learning outcomes (WHAT)** (from the chapter takeaways consolidation)
- **Lectures/modules** (current `execed/_lamd/lectures.csv`, plus any proposed renames/restructures)
- **Canonical snippets/examples (HOW content is delivered)** from the post‑2024 talk spines

## Acceptance Criteria

- [ ] A mapping exists that covers each tenet at least once in the core pathway.
- [ ] Each learning outcome is covered by at least one lecture/module (core and/or extended).
- [ ] Proposed renames/reorders are justified by the mapping (no “silent drift”).
- [ ] The mapping makes it easy to see where LLM/agent interaction is taught and how it is assessed.

## Related

- **CIP**: `cip/cip0001.md`
- **Lectures list**: `execed/_lamd/lectures.csv`

## Progress Updates

### 2026-01-26
Status updated to **In Progress**. Drafted an initial crosswalk for the *current* lecture list (subject to renaming/restructure).

## Reference sets

### Execed tenets (WHY)

- `strategy-before-tools`
- `communicate-uncertainty-explicitly`
- `move-fast-with-guardrails`
- `risk-is-part-of-roi`
- `automation-with-accountability`
- `measure-decision-quality`
- `operating-model-over-pilots`
- `human-capability-is-the-advantage`

### Draft exec learning outcomes (WHAT)

From `backlog/documentation/2026-01-26_execed-learning-outcomes.md`:

1. Frame AI correctly for leadership (system vs entity)
2. Identify where value comes from (information flow, scaled decisions)
3. Define intent and incentives (and anticipate gaming)
4. Reason explicitly under uncertainty (“pause when unsure”)
5. Design for operational reality (mission control)
6. Govern trust and accountability (owners, auditability, recourse)
7. Recognise and mitigate manipulation risks (System Zero)
8. Build human capability as the advantage (augmentation-first)
9. Lead the human–agent shift (LLMs/agents + measurement)
10. Prioritise resilience (robustness, recovery, risk-adjusted ROI)

### Current lecture list (baseline)

From `execed/_lamd/lectures.csv` (titles may be renamed):

- `the-new-world`
- `the-data-crisis`
- `data-quality`
- `intellectual-debt`
- `project-management`
- `ethics-and-privacy`
- `bringing-together`

## Crosswalk (draft)

This is a *first pass* mapping for coherence. It should be revised once the course structure proposal is agreed.

### Lecture → outcomes → tenets → canonical snippet spines

- **`the-new-world`** (framing lecture; likely to be renamed)
  - **Outcomes**: 1, 2, 3, 9, 10
  - **Tenets**: strategy-before-tools; measure-decision-quality; automation-with-accountability
  - **Canonical snippet spines to draw from**:
    - New flow of information: `_data-science/includes/new-flow-of-information*.md`
    - HAM/atomic eye: `_ai/includes/processor-ham.md`, `_ai/includes/the-atomic-eye.md`
    - Conversation/bandwidth: `_ai/includes/conversation-*.md`, `_ai/includes/bandwidth-vs-complexity.md`

- **`the-data-crisis`** (risk framing; likely to incorporate System Zero/manipulation)
  - **Outcomes**: 2, 3, 6, 7, 10
  - **Tenets**: risk-is-part-of-roi; move-fast-with-guardrails; automation-with-accountability
  - **Canonical snippet spines**:
    - Trust/autonomy/embodiment: `_atomic-human/includes/trust-autonomy-embodiment.md`
    - Policy/manipulation thread (to select from talk spines)

- **`data-quality`**
  - **Outcomes**: 4, 6, 10
  - **Tenets**: communicate-uncertainty-explicitly; measure-decision-quality; risk-is-part-of-roi
  - **Canonical snippet spines**:
    - Uncertainty + “pause when unsure” framing (to select)
    - Decision-quality measurement examples (overrides, exception rates)

- **`intellectual-debt`**
  - **Outcomes**: 3, 5, 6, 10
  - **Tenets**: operating-model-over-pilots; strategy-before-tools; move-fast-with-guardrails
  - **Canonical snippet spines**:
    - Decomposition/separation-of-concerns + maintainability
    - “Operating cadence” and ownership patterns (mission control adjacent)

- **`project-management`**
  - **Outcomes**: 5, 6, 8, 10
  - **Tenets**: operating-model-over-pilots; human-capability-is-the-advantage; move-fast-with-guardrails
  - **Canonical snippet spines**:
    - Mission control practices (roles, escalation, simulation)
    - Capability building (routines, incentives, adoption)

- **`ethics-and-privacy`**
  - **Outcomes**: 3, 6, 7, 10
  - **Tenets**: risk-is-part-of-roi; automation-with-accountability; communicate-uncertainty-explicitly
  - **Canonical snippet spines**:
    - Data rights / asymmetry / governance
    - Trust/accountability exemplars (and failure cases)

- **`bringing-together`**
  - **Outcomes**: synthesis across 1–10 (explicitly tie to structure proposal)
  - **Tenets**: all (capstone)
  - **Canonical snippet spines**:
    - Attention/productivity flywheel framing (business layer)
    - Clear “how to run this in your organisation” playbook (RACI, metrics, guardrails)

## Acceptance Criteria checklist

- [x] Draft mapping exists for each tenet and outcome.
- [ ] Refine mapping after the course structure proposal (rename/merge/split decisions).
- [ ] Explicitly identify where LLM/agent interaction is taught *and* assessed in the final structure.
