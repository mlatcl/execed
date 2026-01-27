---
category: features
created: '2026-01-26'
id: 2026-01-26_execed-update-remaining-lectures
last_updated: '2026-01-26'
owner: Neil D. Lawrence
priority: High
related_cips:
- '0001'
status: In Progress
tags:
- execed
- lectures
- atomic-human
- agents
title: Update remaining execed lectures (sessions 2–7) to match new framing
---

# Task: Update remaining execed lectures (sessions 2–7)

## Description

Now that Session 1 has been reframed as `execed/_lamd/the-ai-moment.md`, update the remaining lectures to align with:

- the completed *The Atomic Human* narrative spine
- post‑2024 changes (LLMs, agents, human–agent interaction)
- the exec tenets (`tenets/execed/`)
- the course structure proposal (core pathway + optional chapter-aligned series)

Lectures to update (current files):

- Session 2: `execed/_lamd/the-data-crisis.md`
- Session 3: `execed/_lamd/data-quality.md`
- Session 4: `execed/_lamd/intellectual-debt.md`
- Session 5: `execed/_lamd/project-management.md`
- Session 6: `execed/_lamd/ethics-and-privacy.md`
- Session 7: `execed/_lamd/bringing-together.md`

## Acceptance Criteria

- [ ] Each lecture has an updated title/abstract consistent with the new framing.
- [ ] Each lecture has an explicit “LLMs/agents” placement where relevant (capability, failure modes, governance, measurement).
- [ ] Each lecture is mapped (lightweight) to outcomes + tenets (can be via the crosswalk doc).
- [ ] `execed/_lamd/compile.sh` builds cleanly for the full lecture set in `execed/_lamd/lectures.csv`.
- [ ] A brief spot-check confirms the generated pages/slides are coherent and links resolve.

## Plan (draft sequence)

1. Update Session 2 (`the-data-crisis`) to foreground incentives/intent + System Zero risks.
2. Update Session 3 (`data-quality`) to tie DRLs to uncertainty thresholds and decision quality.
3. Update Session 4 (`intellectual-debt`) to connect maintainability, accountability, and auditability in the agent era.
4. Update Session 5 (`project-management`) as mission-control/operating-model.
5. Update Session 6 (`ethics-and-privacy`) as trust/accountability + data rights/asymmetry.
6. Update Session 7 (`bringing-together`) as an executive playbook and capstone synthesis.

## Shared assets: Atomic Human chapter illustrations (Scribeysense)

To support the per-session “Suggested chapter illustration” choices below, we should copy the missing chapter images from:

- Source: `/Users/neil/lawrennd/slides/diagrams/atomic-human/`
- Destination: `execed/slides/diagrams/atomic-human/`

**Already present in execed**:

- [x] `Atomic_H_1_Gods_Robots.png`
- [x] `Atomic_H_3_Intent.png`

**To copy into execed** (available in `/Users/neil/lawrennd/slides/diagrams/atomic-human/`):

- [ ] `Atomic_H_2_Automatons.png`
- [ ] `Atomic_H_4_Persistence.png`
- [ ] `Atomic_H_5_Enlightenment.png`
- [ ] `Atomic_H_6_Gremlin.png`
- [ ] `Atomic_H_7_Not_Rocket.png`
- [ ] `Atomic_H_8_System_Zero.png`
- [ ] `Atomic_H_9_Design_Brain.png`
- [ ] `Atomic_H_10_Gaslighting.png`
- [ ] `Atomic_H_11_Human_Analogue.png`
- [ ] `Atomic_H_12_Trust.png`
- [ ] `Atomic_H_Epilogue.png` (or `Atomic_H_Epilogue_scaled.png`)

## Progress Updates

### 2026-01-26
Task created.

### 2026-01-26
Status updated to **In Progress**. Next: draft Session 2 update plan before editing lecture sources.

## Session 2 plan (draft): `the-data-crisis`

**Goal (exec framing)**: shift from “data readiness levels” as a technical taxonomy to **governance of intent/incentives** and **System Zero risk**: what happens when optimisation targets (and data asymmetries) reshape behaviour at scale.

- **Proposed title**: “Intent, Incentives, and the Data Crisis”
- **Atomic Human anchors**: Chapter 3 (Intent), Chapter 8 (System Zero), Chapter 10 (Gaslighting)
- **Key outcomes** (from learning outcomes draft):
  - Outcome 3 (intent/incentives), Outcome 7 (manipulation risks), Outcome 10 (resilience)
- **Tenets**:
  - `strategy-before-tools`
  - `risk-is-part-of-roi`
  - `automation-with-accountability` (preview: who owns consequences)
  - (optionally) `measure-decision-quality` (how to tell you’re being gamed)
- **Suggested chapter illustration**:
  - `slides/diagrams/atomic-human/Atomic_H_3_Intent.png` as featured image / opener
- **Canonical snippet spines to pull in**:
  - `_atomic-human/includes/trust-autonomy-embodiment.md` (intent/embodiment framing)
  - System Zero / manipulation thread (from `_atomic-human/includes/reality-is-more-humdrum.md` and `_atomic-human/includes/surveillance-goes-self-service.md` if/when needed)
  - Attention economy as the incentive engine (attention becomes the bottleneck → “gold”):
    - `_economics/includes/the-attention-economy.md` (includes the Herbert Simon attention quote)
    - `_business/includes/an-attention-economy.md` (business framing, if needed)
  - “New flow of information” refresher only if needed (keep Session 1 as main anchor)

**Edits to make in `execed/_lamd/the-data-crisis.md`** (when implementing):
- Update frontmatter title/abstract to match “intent + incentives + System Zero” framing.
- Keep DRLs, but reposition as **instrumentation**: “what do we know / what’s missing / what can be gamed?”
- Add an explicit “how it fails” segment: gaming, Goodhart’s law, adversarial behaviour, institutional drift.

## Session 3 plan (draft): `data-quality`

**Goal (exec framing)**: move from “data quality” as cleanliness to **decision-quality under uncertainty**: thresholds, calibration, and “pause when unsure” as an operating discipline.

- **Proposed title**: “Uncertainty, Data Quality, and Decision Thresholds”
- **Atomic Human anchors**: Chapter 6 (Gremlin of Uncertainty), Chapter 11 (Human–Analogue Machines)
- **Key outcomes**:
  - Outcome 4 (reason explicitly under uncertainty), Outcome 10 (resilience)
- **Tenets**:
  - `communicate-uncertainty-explicitly`
  - `measure-decision-quality`
  - `move-fast-with-guardrails`
- **Suggested chapter illustration**:
  - `slides/diagrams/atomic-human/Atomic_H_6_Gremlin.png` (copy into execed diagrams)
- **Canonical snippet spines to pull in**:
  - DRLs as “what we know / don’t know” scaffolding
  - any “pause when unsure / escalation” material used in recent agent talks

**Edits to make in `execed/_lamd/data-quality.md`** (when implementing):
- Reframe “DRLs” as uncertainty management and operational readiness.
- Add explicit examples: miscalibration, distribution shift, novelty; what to measure; who acts on signals.

## Session 4 plan (draft): `intellectual-debt`

**Goal (exec framing)**: connect “technical/intellectual debt” to **accountability** and **auditability** when systems include ML + agents (who can act, not just predict).

- **Proposed title**: “Intellectual Debt in the Agent Era”
- **Atomic Human anchors**: Chapter 3 (Intent), Chapter 11 (HAM fragility), Chapter 12 (Trust)
- **Key outcomes**:
  - Outcome 6 (trust/accountability), Outcome 9 (human–agent shift), Outcome 10 (resilience)
- **Tenets**:
  - `automation-with-accountability`
  - `risk-is-part-of-roi`
  - `operating-model-over-pilots`
- **Suggested chapter illustration**:
  - `slides/diagrams/atomic-human/Atomic_H_11_Human_Analogue.png` or `slides/diagrams/atomic-human/Atomic_H_12_Trust.png` (copy into execed diagrams)
- **Canonical snippet spines to pull in**:
  - “ownership”, “audit trail”, “rollback/kill switch”, “change control” patterns

**Edits to make in `execed/_lamd/intellectual-debt.md`** (when implementing):
- Add an explicit section: “debt creates accountability gaps” (who can explain/stop/override?).
- Add agent-specific failure modes: silent automation drift, unreviewed changes, brittle toolchains.

## Session 5 plan (draft): `project-management`

**Goal (exec framing)**: make project management the **operating model** for high-stakes socio-technical systems (mission control: roles, escalation, simulation, incident response).

- **Proposed title**: “Operating Model: Mission Control for AI”
- **Atomic Human anchors**: Chapter 7 (Not Rocket Science), Chapter 6 (Uncertainty)
- **Key outcomes**:
  - Outcome 5 (operational reality), Outcome 6 (trust/accountability), Outcome 8 (human capability)
- **Tenets**:
  - `operating-model-over-pilots`
  - `move-fast-with-guardrails`
  - `human-capability-is-the-advantage`
- **Suggested chapter illustration**:
  - `slides/diagrams/atomic-human/Atomic_H_7_Not_Rocket.png` (copy into execed diagrams)

- **Where to introduce Conway’s Law + the API mandate (this session)**:
  - **Why here**: it’s the cleanest bridge from “organisations are information topographies” to an **operating model** for agents: your API boundaries *become* your autonomy boundaries, and Conway’s Law predicts what you’ll ship if you don’t redesign communication/decision rights.
  - **Snippets to use**:
    - `_business/includes/the-api-mandate-bezos.md` (API mandate; includes a Conway’s Law slide/quote)
    - `_business/includes/institutional-character.md` (optional supporting framing)
  - **Talk anchors where this already appears**:
    - `lawrennd/talks/_ai/information-in-the-age-of-ai.md` (includes `_business/includes/the-api-mandate-bezos.md`)
    - `lawrennd/talks/_business/leading-with-ai-lloyds-bank.md` (includes `_business/includes/the-api-mandate-bezos.md`, and references Conway’s Law)

**Edits to make in `execed/_lamd/project-management.md`** (when implementing):
- Make “roles + decision rights + escalation” explicit (not just delivery milestones).
- Include “simulation / pre-mortem / incident drills” as the executive path to reliability.

## Session 6 plan (draft): `ethics-and-privacy`

**Goal (exec framing)**: frame privacy/ethics as **trust infrastructure** and **data-rights power** (asymmetry, manipulation, recourse).

- **Proposed title**: “Trust, Data Rights, and Accountability”
- **Atomic Human anchors**: Chapter 8 (System Zero), Chapter 10 (Gaslighting), Chapter 12 (Trust), Epilogue (institutions)
- **Key outcomes**:
  - Outcome 6 (trust/accountability), Outcome 7 (manipulation risk), Outcome 10 (resilience)
- **Tenets**:
  - `automation-with-accountability`
  - `risk-is-part-of-roi`
  - `strategy-before-tools`
- **Suggested chapter illustration**:
  - `slides/diagrams/atomic-human/Atomic_H_8_System_Zero.png` or `slides/diagrams/atomic-human/Atomic_H_10_Gaslighting.png` or `slides/diagrams/atomic-human/Atomic_H_12_Trust.png` (copy into execed diagrams)

- **Where to introduce Herbert Simon + the Attention Economy (this session)**:
  - **Why here**: it links System Zero (influence below awareness) to business model incentives: a “wealth of information” produces a “poverty of attention” — so attention becomes the scarce resource (“gold”) and is systematically harvested/steered unless governed.
  - **Snippets to use**:
    - `_economics/includes/the-attention-economy.md` (core; includes Herbert Simon quote)
    - `_economics/includes/herbert-simon-information.md` (optional: use the quote standalone)
    - `_ai/includes/attention-cycles.md` and `_policy/includes/attention-reinvestment-cycle.md` (optional: dynamics/feedback framing)
  - **Talk anchors where this already appears**:
    - `lawrennd/talks/_economics/ai-cannot-replace-the-atomic-human-mimit.md` (includes `_economics/includes/the-attention-economy.md`)
    - `lawrennd/talks/_business/the-transformative-power-of-ai-and-its-challenges.md` (includes `_economics/includes/the-attention-economy.md`)

**Edits to make in `execed/_lamd/ethics-and-privacy.md`** (when implementing):
- Add “recourse” and “auditability” as design requirements (not compliance afterthoughts).
- Add “System Zero” framing: influence below awareness, homogeneity risk, institutional safeguards.

## Session 7 plan (draft): `bringing-together`

**Goal (exec framing)**: a capstone playbook: connect strategy → decisions → governance → operating model → metrics; explicitly include agents and decision-quality measurement.

- **Proposed title**: “Executive Playbook: Leading AI and Agents”
- **Atomic Human anchors**: Epilogue (institutions/resilience), Chapter 12 (Trust)
- **Key outcomes**:
  - Synthesis across Outcomes 1–10 (explicitly)
- **Tenets**:
  - all (capstone synthesis), with emphasis on `strategy-before-tools` + `automation-with-accountability` + `measure-decision-quality`
- **Suggested chapter illustration**:
  - `slides/diagrams/atomic-human/Atomic_H_Epilogue.png` (or `Atomic_H_Epilogue_scaled.png`) (copy into execed diagrams)

**Edits to make in `execed/_lamd/bringing-together.md`** (when implementing):
- Provide a “first 30/60/90 days” checklist: what to change, what to measure, where to put governance.
- Add explicit agent adoption guardrails: sandbox → supervised → higher autonomy, with decision-quality gates.

