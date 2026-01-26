---
id: "automation-with-accountability"
title: "Automate with accountability"
status: "Active"  # Active, Under Review, Archived
created: "2026-01-26"
last_reviewed: "2026-01-26"
review_frequency: "Annual"
conflicts_with:
  - "move-fast-with-guardrails"
tags:
  - tenet
  - execed
  - exec-mba
  - trust
  - governance
  - accountability
---

# Tenet: Automate with accountability

## Tenet

**Title**: Automate with accountability

**Description**: Automation can scale decisions, but it cannot carry responsibility. We treat accountability as a deliberate design choice: clear owners, explicit decision rights, defined escalation paths, and auditability. “Human in the loop” is not a slogan; it is a governed operating model for consequential decisions.

**Quote**: *"Delegation is a choice; responsibility is not."*

**Examples**:
- Define which decisions can be automated end-to-end vs which require human sign-off (and under what conditions).
- Build “pause when unsure” and escalation triggers (uncertainty thresholds, novelty detection, exception routing).
- Require an owner for model/system outcomes (harms, incidents, overrides), not just an owner for delivery.

**Counter-examples**:
- Treating “the model decided” as an answer when a customer, regulator, or employee asks “why?”
- Shipping an agent/tool that can act, without logs, controls, or a way to stop/roll back safely.
- Optimising for throughput while hiding error costs in downstream teams (support, compliance, frontline staff).

**Conflicts**:
- Potential conflict with **move-fast-with-guardrails** when speed pressures reduce oversight.
- Resolution: Scale autonomy progressively: sandbox → assisted → supervised → (only then) higher autonomy, with measurable decision quality at each stage.

## Alignment with *The Atomic Human* takeaways

- **Prologue**: the executive question is what decisions you are automating and who bears the risk when it’s wrong.
- **Chapter 11 (HAM fragility)**: systems can be brilliant and still fail confidently; don’t outsource judgment.
- **Chapter 12 (Trust)**: accountability must stay human; treat AI like fire—enablement requires containment and competent stewardship.

