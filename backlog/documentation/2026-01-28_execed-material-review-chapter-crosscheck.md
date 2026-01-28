---
category: documentation
created: "2026-01-28"
id: 2026-01-28_execed-material-review-chapter-crosscheck
last_updated: "2026-01-28"
owner: Neil D. Lawrence
priority: Medium
related_cips:
  - "0002"
status: In Progress
tags:
  - execed
  - material-review
  - atomic-human
title: "Material review: cross-check sessions vs book chapters"
---

# Task: Material review — cross-check sessions vs book chapters

## Description

Cross-check the ExecEd session framing against `~/lawrennd/the-atomic-human/_chapters/`:

- For each session (1–7), list intended chapter anchors and confirm key takeaways are represented.
- Identify gaps (chapter ideas relevant to a session but missing in the lecture/snippets).
- Identify redundancies (same chapter point repeated across sessions without purpose).

## Acceptance Criteria

- [ ] A session-by-session table exists: session → chapter anchors → “covered / partial / missing”.
- [ ] A short list of “highest value additions” exists (by session).
- [ ] Proposed changes are expressed as candidate snippet swaps/additions (not lecture edits yet).

## Progress Updates

### 2026-01-28

Verified “missing chapters” scan (skimmed Ch.2, Ch.5, Ch.9 in `~/lawrennd/the-atomic-human/_chapters/`), and mapped **where they best reinforce the 7-session core**.

| Session | Current exec framing | Primary chapter anchors | Coverage (updated) | Notes / candidate additions (snippets, not lecture edits) |
|---|---|---|---|---|
| 1 | AI moment + trust/autonomy | Prologue, Ch.1, Ch.3, Ch.12 | Partial | Add a Ch.5 “information revolution” micro-anchor; add a Ch.9 “AI fallacy / machines don’t ‘understand’ like humans” micro-anchor; optionally add a Ch.2 “information topography / devolution” micro-anchor |
| 2 | Intent/incentives + System Zero + attention | Ch.3, Ch.8, Ch.10 | Partial | Consider a Ch.5 “printing press → social media” anchor to frame incentive shocks; optionally add a Ch.2 “information is power (crypto)” anchor where it supports data-rights thinking |
| 3 | Uncertainty + thresholds | Ch.6, Ch.7, Ch.11 | Partial | Add a Ch.9 “threshold logic + homeostasis” anchor to reinforce calibrated thresholds and escalation; add a Ch.5 “prediction vs control/feedback” contrast anchor |
| 4 | Intellectual debt in agent era | Ch.3, Ch.11, Ch.12, Epilogue | Partial | Add a Ch.2 “decomposition/assembly line hides system-level understanding” anchor as an intellectual-debt precursor |
| 5 | Mission control operating model + Conway/API | Ch.7 (operating discipline) | Partial | Add a Ch.5 “Watt governor / control systems” anchor as a concrete archetype for operations vs prediction; add a Ch.2 “information factory / division of labour” anchor |
| 6 | Trust + data rights + attention + System Zero | Ch.8, Ch.10, Ch.12, Epilogue | Partial | If needed, add a Ch.5 “information revolution → cultural disruption” anchor to connect trust failures to media incentives |
| 7 | Executive playbook capstone | Epilogue, Ch.12 | Partial | Ensure capstone recap explicitly references: Ch.5 info revolutions, Ch.2 devolution/topography, Ch.9 AI fallacy + human responsibility |

Missing chapters: “must surface” points + proposed placement

- **Ch.2 (Automatons)**: what’s unique and worth surfacing
  - **Information topography + devolution of authority**: leaders cannot directly control everything; culture/topography shapes what decisions reach the top.
    - **Best session placement**: Session 1 (AI moment + org decision-making) as a framing anchor.
  - **Automation requires “information complete” tasks; decomposition/assembly lines hide system-level failure**: industrialized information processing creates scale and brittleness (and sets up intellectual debt).
    - **Best session placement**: Session 5 (operating model) and/or Session 4 (intellectual debt).
  - **Candidate snippet action**:
    - Upgrade existing (currently placeholder) snippet `~/lawrennd/snippets/_atomic-human/includes/narratives-vs-statistics.md` (it contains the Chapter 2 Scribeysense figure but is marked `\\editme`) into a short, reusable anchor (story + takeaway).
    - If we prefer smaller pieces, split into two micro-snippets: one for “information topography/devolution”, one for “information factory/decomposition”.

- **Ch.5 (Enlightenment)**: what’s unique and worth surfacing
  - **Information revolutions reshape culture**: printing press as historical analogue for computers/social media; disruption is structural, not just “bad actors”.
    - **Best session placement**: Session 1 (opening context) and/or Session 2 (incentives + attention).
  - **Laplace’s demon → modern ML recipe**: \(model + data \\rightarrow compute \\rightarrow prediction\); pairs well with “what AI is / isn’t”.
    - **Best session placement**: Session 1 (AI moment) as the “what most AI is” anchor.
  - **Prediction vs control/feedback**: Watt’s governor / fly-ball as a counterpoint to pure prediction (operational control beats omniscience).
    - **Best session placement**: Session 3 (thresholds) and Session 5 (mission control / operating model).
  - **Candidate snippet action**:
    - Create a small canonical snippet for each of:
      - “printing press ↔ social media” (context shock)
      - “Laplace recipe” (what ML is)
      - “prediction vs control” (Watt governor archetype)

- **Ch.9 (Design for a Brain)**: what’s unique and worth surfacing
  - **AI fallacy + social ‘telepathy’ cues**: Turing’s telepathy belief (and the role of weak experiments / social cues) is a vivid way to teach “don’t over-infer intelligence”.
    - **Best session placement**: Session 1 (AI moment / what we mistake for intelligence).
  - **Homeostasis + thresholds as a model for robust systems**: adaptive stability, thresholds, and feedback as a bridge to governance/ops thinking.
    - **Best session placement**: Session 3 (uncertainty + thresholds), with a pointer to Session 5 (feedback/ops).
  - **Candidate snippet action**:
    - Create a “Ch.9 thresholds/homeostasis” micro-snippet for Session 3.
    - Create a “Ch.9 AI fallacy” micro-snippet for Session 1.

