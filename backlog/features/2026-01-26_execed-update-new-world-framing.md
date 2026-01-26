---
category: features
created: '2026-01-26'
id: 2026-01-26_execed-update-new-world-framing
last_updated: '2026-01-26'
owner: Neil D. Lawrence
priority: High
related_cips:
- '0001'
status: Completed
tags:
- execed
- lecture
- framing
- atomic-human
- agents
- llm
title: Update/replace 'The New World' lecture framing based on course re-architecture
---

# Task: Update/replace the “The New World” lecture framing

## Description

Once the learning outcomes and course structure proposal are agreed, update the first lecture (now `execed/_lamd/the-ai-moment.md`, previously `execed/_lamd/the-new-world.md`) to set the new narrative spine:

- book-complete framing (*The Atomic Human*)
- post‑2024 landscape (LLMs, coding agents, human–agent interaction)
- executive emphasis (decision-making, accountability, uncertainty, trust)

This task may include **renaming** the lecture and/or changing its included snippets to match the new framing.

## Acceptance Criteria

- [x] The lecture (or its renamed replacement) introduces the course’s key themes in executive language.
- [x] Explicitly covers: capability vs entity, uncertainty, trust/accountability, and human–agent interaction.
- [x] Links clearly into the rest of the course structure (core pathway and/or extended series).
- [x] Builds successfully via `execed/_lamd/compile.sh`.

## Related

- **CIP**: `cip/cip0001.md`
- **Lecture source**: `execed/_lamd/the-ai-moment.md`

## Progress Updates

### 2026-01-26
Status updated to **In Progress**. Drafted proposed rename and lecture outline aligned to the new core pathway.

### 2026-01-26
Implemented the renamed first lecture as `execed/_lamd/the-ai-moment.md` and rebuilt lecture + slides outputs.

## Proposed rename (draft)

Current: **The New World**

Proposed options (pick one):

1. **The AI Moment: Decisions, Information, and the Atomic Human**
2. **The New World of AI: Leadership, Trust, and Uncertainty**
3. **AI at Scale: What Leaders Need to Know Now**

Suggest going with (1)

## Where this sits in the proposed structure

This lecture should cover **Module 0 (Intro)** and the start of **Module 1 (New flow of information)** from:

`backlog/features/2026-01-26_execed-course-structure-proposal.md`.

## Draft lecture outline (exec-facing)

1. **Why now**: the AI moment (branding, investment, deployment reality)
2. **What AI is (and is not)**: intelligent systems vs intelligent entities; why “superintelligence” framing misleads businesses
3. **The new flow of information**: data+compute mediating decisions; “scaled micro-decisions” as the real locus of value and risk
4. **Four executive questions (default framing for the course)**
   - What decision are we changing?
   - What information does it require (and what’s missing)?
   - How can it fail (and how will we notice early)?
   - Who is accountable (and what is the escalation path)?
5. **LLMs + agents**: what changed post‑2024; delegation vs responsibility; “automation complacency” and how to measure it
6. **What comes next**: preview the rest of the course (uncertainty, intent/incentives, trust/accountability, operating model)

## Candidate snippet “spines” to include (draft)

Use these as anchor inclusions (exact selection to be refined during editing):

- **Chapter-illustration opener (recommended)**:
  - `_atomic-human/includes/gods-and-robots-scribeysense.md` → `Atomic_H_1_Gods_Robots`
- **New flow of information**:
  - `_data-science/includes/new-flow-of-information.md` (and/or `...-ham.md`)
- **HAMs / atomic eye**:
  - `_ai/includes/processor-ham.md`
  - `_ai/includes/the-atomic-eye.md`
- **Conversation/bandwidth narrative**:
  - `_ai/includes/conversation-computer.md` and/or `_ai/includes/conversation-tedx.md`
- **Trust/accountability**:
  - `_atomic-human/includes/trust-autonomy-embodiment.md` (preview of later modules)
- **Human–agent interaction / modern landscape** (to select):
  - `_ai/includes/human-computers-interacting.md` (if available/appropriate)

## Acceptance Criteria checklist

- [ ] The lecture (or renamed replacement) introduces key themes in executive language.
- [ ] Covers: capability vs entity, uncertainty, trust/accountability, and human–agent interaction.
- [ ] Links clearly into the rest of the proposed course structure.
- [ ] Builds successfully via `execed/_lamd/compile.sh`.
