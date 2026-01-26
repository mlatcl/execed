---
id: "2026-01-26_execed-course-structure-proposal"
title: "Draft execed course structure proposal (core pathway + extended chapter series)"
status: "In Progress"
priority: "High"
created: "2026-01-26"
last_updated: "2026-01-26"
owner: "Neil D. Lawrence"
related_cips: ["0001"]
related_requirements: ["0001", "0002"]
tags: ["execed", "curriculum", "structure", "atomic-human", "agents", "llm"]
---

# Task: Draft course structure proposal (core + extended)

## Description

Draft a concrete proposal for the course structure that supports:

1. **Core executive pathway** (6–8 lectures/modules): outcome-driven, decision-making focused.
2. **Extended pathway** (intro + one lecture per book chapter): seminar format for deeper study.

This proposal should *not* be beholden to the existing lecture titles; it may recommend renaming, merging, splitting, or reordering lectures, guided by the completed book and post‑2024 themes.

## Acceptance Criteria

- [ ] A proposed core pathway exists with 6–8 modules, each with: title, purpose, key outcomes, and linked tenets.
- [ ] A proposed extended pathway exists: intro + chapters 1–12 (and epilogue as appropriate).
- [ ] Explicit placement for LLMs/coding agents/human–agent interaction is defined (capability, failure modes, governance, measurement).
- [ ] A migration note exists: how current lectures map to the new structure (rename/merge/split guidance).

## Related

- **CIP**: `cip/cip0001.md`
- **Requirements**: REQ-0001, REQ-0002

## Progress Updates

### 2026-01-26
Status updated to **In Progress**. Drafted an initial structure proposal (core + extended) and a migration map from the current lecture set.

## Proposal (draft)

### 1) Core executive pathway (7 modules)

Each module lists: purpose, key outcomes (1–10), and tenets.

#### Module 0 (Intro): Why this course now (The Atomic Human + agents)
- **Purpose**: Set the spine: intelligent systems vs entities, the “new flow of information”, and why LLMs/agents make governance and operating model urgent.
- **Key outcomes**: 1, 2, 9, 10
- **Tenets**: strategy-before-tools; measure-decision-quality

#### Module 1: The new flow of information (and what AI actually is)
- **Purpose**: Reframe AI as scaled prediction/coordination; show how data+compute mediate reality and change organisational advantage.
- **Key outcomes**: 1, 2
- **Tenets**: strategy-before-tools; human-capability-is-the-advantage

#### Module 2: Intent, incentives, and adversarial dynamics
- **Purpose**: Explain optimisation targets, misalignment, and gaming; connect engagement-optimised systems to predictable failure modes.
- **Key outcomes**: 3, 7, 10
- **Tenets**: strategy-before-tools; risk-is-part-of-roi

#### Module 3: Uncertainty as an executive primitive
- **Purpose**: Teach probability/ranges/thresholds; design “pause when unsure”; link uncertainty to accountability and escalation.
- **Key outcomes**: 4, 10
- **Tenets**: communicate-uncertainty-explicitly; measure-decision-quality; move-fast-with-guardrails

#### Module 4: Trust, accountability, and governance in the agent era
- **Purpose**: Decide what to delegate; set decision rights; ensure auditability and recourse; treat agents as governed actors in workflows.
- **Key outcomes**: 6, 9, 10
- **Tenets**: automation-with-accountability; risk-is-part-of-roi; measure-decision-quality

#### Module 5: Operating model and mission control
- **Purpose**: Move beyond pilots: roles, escalation, simulation, incident response, and the “feel” of good interfaces and handoffs.
- **Key outcomes**: 5, 8, 10
- **Tenets**: operating-model-over-pilots; move-fast-with-guardrails; human-capability-is-the-advantage

#### Module 6 (Capstone): Translating into practice
- **Purpose**: Integrate: strategy → decisions → governance → operating model → metrics; define next steps for participants’ organisations.
- **Key outcomes**: 1–10 (explicit synthesis)
- **Tenets**: all (capstone)

> **Explicit LLM/agent placement**: Module 4 is the primary anchor; Modules 3 and 5 reinforce measurement and operating safeguards.

### Chapter illustration assets (Dan Andrews / Scribeysense)

There is a coherent set of **one illustration per chapter** (plus epilogue) under:

- `~/lawrennd/snippets/_atomic-human/includes/` (snippet wrappers)
- images referenced as `\includepng{\diagramsDir/atomic-human/Atomic_H_*}`

These can be used as **section dividers** and as a visual “spine” across both pathways.

#### Canonical mapping: chapter → snippet wrapper → image

- **Ch1 Gods and Robots** → `_atomic-human/includes/gods-and-robots-scribeysense.md` (or `fascination-with-ourselves.md`) → `Atomic_H_1_Gods_Robots`
- **Ch2 Automatons** → `_atomic-human/includes/narratives-vs-statistics.md` → `Atomic_H_2_Automatons`
- **Ch3 Intent** → `_atomic-human/includes/trust-autonomy-embodiment-diagram.md` → `Atomic_H_3_Intent`
- **Ch4 Persistence** → `_atomic-human/includes/the-trick-doesnt-replace-the-truth.md` → `Atomic_H_4_Persistence`
- **Ch5 Enlightenment** → `_atomic-human/includes/enlightenment-scribeysense.md` → `Atomic_H_5_Enlightenment`
- **Ch6 Gremlin of Uncertainty** → `_atomic-human/includes/a-diversity-of-approaches-brings-resilience.md` → `Atomic_H_6_Gremlin`
- **Ch7 Not Rocket Science/Brain Surgery** → `_atomic-human/includes/reflective-or-reactive.md` → `Atomic_H_7_Not_Rocket`
- **Ch8 System Zero** → `_atomic-human/includes/reality-is-more-humdrum.md` → `Atomic_H_8_System_Zero`
- **Ch9 Design for a Brain** → `_atomic-human/includes/us-that-adapt-to-the-machine.md` → `Atomic_H_9_Design_Brain`
- **Ch10 Gaslighting** → `_atomic-human/includes/surveillance-goes-self-service.md` → `Atomic_H_10_Gaslighting`
- **Ch11 Human–Analogue Machines** → `_atomic-human/includes/river-gods-decide.md` → `Atomic_H_11_Human_Analogue`
- **Ch12 Trust** → `_atomic-human/includes/nothing-to-worry-about.md` → `Atomic_H_12_Trust`
- **Epilogue** → `_atomic-human/includes/societys-wicked-problems-diagram.md` → `Atomic_H_Epilogue`

#### Allocation across the **core pathway** (recommended)

Use one illustration as the “cover slide” for each module to keep the narrative grounded in the book:

- **Module 0 (Intro)**: Ch1 (`Atomic_H_1_Gods_Robots`) — fascination with intelligence and the “AI moment”
- **Module 1 (New flow of information)**: Ch5 (`Atomic_H_5_Enlightenment`) — information revolutions + prediction recipe
- **Module 2 (Intent/incentives)**: Ch3 (`Atomic_H_3_Intent`) — objectives, context, and gaming
- **Module 3 (Uncertainty)**: Ch6 (`Atomic_H_6_Gremlin`) — uncertainty as an executive primitive
- **Module 4 (Trust/accountability)**: Ch12 (`Atomic_H_12_Trust`) — delegation vs responsibility
- **Module 5 (Operating model/mission control)**: Ch7 (`Atomic_H_7_Not_Rocket`) — roles, escalation, simulation
- **Module 6 (Capstone)**: Epilogue (`Atomic_H_Epilogue`) — institutional resilience and wicked problems

Keep the remaining chapter illustrations as optional dividers within modules (e.g. Ch8/Ch10 within Module 2–4).

### 2) Extended pathway (intro + chapter-aligned series)

Recommended format: seminar series (13 sessions) with pre-reading and discussion.

- **Intro**: Prologue + course framing (Module 0)
- **Ch1**: Gods and Robots
- **Ch2**: Automatons
- **Ch3**: Intent
- **Ch4**: Persistence
- **Ch5**: Enlightenment
- **Ch6**: The Gremlin of Uncertainty
- **Ch7**: It’s Not Rocket Science or Brain Surgery
- **Ch8**: System Zero
- **Ch9**: Design for a Brain
- **Ch10**: Gaslighting
- **Ch11**: Human–Analogue Machines
- **Ch12**: Trust
- **Outro**: Epilogue (institutional resilience)

### 3) Migration note (current execed lectures → proposed modules)

Current lectures in `execed/_lamd/lectures.csv`:

- `the-new-world` → Module 0–1 (framing + new flow of information); likely rename
- `the-data-crisis` → Module 2 (incentives/adversaries) and Module 4 (governance), depending on emphasis
- `data-quality` → Module 3 (uncertainty + decision thresholds)
- `intellectual-debt` → Module 5 (operating model, maintainability, responsibility)
- `project-management` → Module 5 (mission control + operating cadence)
- `ethics-and-privacy` → Module 4 (trust/accountability) + Module 2/6 (risk framing)
- `bringing-together` → Module 6 (capstone synthesis)

## Acceptance Criteria checklist

- [x] A proposed core pathway exists (draft) with 6–8 modules.
- [x] A proposed extended pathway exists (draft).
- [x] Explicit placement for LLMs/agents is defined.
- [x] A migration note exists (draft mapping from current lectures).

