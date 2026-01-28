---
category: documentation
created: "2026-01-28"
id: 2026-01-28_execed-material-review-session-walkthrough
last_updated: "2026-01-28"
owner: Neil D. Lawrence
priority: Medium
related_cips:
  - "0002"
status: In Progress
tags:
  - execed
  - material-review
  - sessions
  - atomic-human
  - talks
  - snippets
title: "Material review: session-by-session walkthrough (propose snippet changes)"
---

# Task: Material review — session-by-session walkthrough (propose snippet changes)

## Description

Run a structured, session-by-session walkthrough for ExecEd Sessions 1–7 to support **CIP-0002**.

For each session, consolidate:

- **Atomic Human chapter anchors** (explicitly what chapter points we intend to surface)
- **Talk spines** (recent talks that already carry the same message/snippets)
- **Canonical snippets** currently used in the session (from the include inventory)
- **Snippet freshness flags** (from the freshness report)
- **Notes plan**: what speaker notes we need to add/restore in the session (Atomic Human-inspired)
- **Book back-references**: which concepts should be tagged with `\addatomic{...}{...}` (with page numbers)

Then propose **candidate snippet swaps/additions** and **notes additions** (not lecture edits yet — only proposals).

**Macro convention (book references)**:

- Use `\addatomic{<index term>}{<page list>}` to connect a concept back to *The Atomic Human*.
- Page lists should be pulled from the index in `Lawrence_Neil_thesis_index.pdf` (we keep a text extraction for quick lookup: `artifacts/material-review/Lawrence_Neil_thesis_index.txt`).

## Inputs

- Lecture sources: `execed/_lamd/*.md`
- Include inventory outputs: `artifacts/material-review/inventory.json` (generated)
- Freshness outputs: `artifacts/material-review/snippet_freshness.json` (generated)
- Chapter cross-check notes: `backlog/documentation/2026-01-28_execed-material-review-chapter-crosscheck.md`
- Talk sources (scope): `~/lawrennd/talks/_atomic-human/`, `~/lawrennd/talks/_business/` (optionally `_policy`, `_economics`)
- Book index for page numbers: `execed/Lawrence_Neil_thesis_index.pdf`
- Text extraction (for grep/search): `artifacts/material-review/Lawrence_Neil_thesis_index.txt` (generated)

## Acceptance Criteria

- [ ] A table exists with **Sessions 1–7**: chapter anchors, talk spine(s), and current canonical snippets.
- [ ] Each session has a short **“proposed snippet changes”** list (adds/swaps) with rationale.
- [ ] Each session has a **speaker notes plan** (Atomic Human-inspired) with concrete bullets to add as `\notes{...}` in the lecture source.
- [ ] Each session includes a **book reference block** that lists the intended `\addatomic{...}{...}` tags (with index-page numbers).
- [ ] Any proposed new/updated snippets are recorded as follow-on backlog tasks (separate tasks) before implementation.

## Session walkthrough (working notes)

### Session 1 — `the-ai-moment`

- **Current framing**: AI moment + decisions + trust/autonomy
- **Chapter anchors (target)**: Prologue, Ch.1, Ch.3, Ch.12 (+ optional Ch.2/Ch.5/Ch.9 micro-anchors)
- **Talk spines (candidates)**: TBD (from talk inventory)
- **Current snippets**: TBD (from include inventory)
- **Notes to add/restore (Atomic Human-inspired)**:
  - TBD (exec-facing narrative, the “AI moment” framing, and why this is about decisions and institutions, not sci‑fi)
- **Book references (`\addatomic`) to include** (seed list; extend as needed):
  - `\addatomic{embodiment factor}{13, 29, 35, 79, 87, 105, 197, 216-217, 249, 269, 327, 353, 363, 369}`
  - `\addatomic{topography, information}{34-9, 43-8, 57, 62, 104, 115-16, 127, 140, 192, 196, 199, 291, 334, 354-5}`
  - `\addatomic{printing press}{8, 9, 13, 24, 68, 75, 104-5, 106-8, 107-8, 345, 354-5}`
  - `\addatomic{Laplace’s demon}{111-14, 145}` (expand page list as needed)
  - `\addatomic{telepathy}{248-50}` (if we use the “Turing got fooled by social cues” point)
- **Proposed snippet changes**:
  - TBD

### Session 2 — `the-data-crisis`

- **Current framing**: intent/incentives + System Zero + attention
- **Chapter anchors (target)**: Ch.3, Ch.8, Ch.10 (+ optional Ch.5 printing press → social media)
- **Talk spines (candidates)**: TBD
- **Current snippets**: TBD
- **Notes to add/restore (Atomic Human-inspired)**:
  - TBD (incentives → optimisation → drift; how “intent” becomes legible and therefore gameable)
- **Book references (`\addatomic`) to include** (seed list; extend as needed):
  - `\addatomic{System Zero}{242-7, 306, 309, 329, 350, 355, 359, 361, 363, 364}`
  - `\addatomic{Gas Light (play)/gaslighting}{302-3}` (expand if needed)
  - `\addatomic{trust}{43, 79, 100}` (expand if needed)
  - `\addatomic{printing press}{8, 9, 13, 24, 68, 75, 104-5, 106-8, 107-8, 345, 354-5}` (if using the “info revolution” analogue)
- **Proposed snippet changes**:
  - TBD

### Session 3 — `data-quality`

- **Current framing**: uncertainty + thresholds + decision quality
- **Chapter anchors (target)**: Ch.6, Ch.7, Ch.11 (+ optional Ch.9 thresholds/homeostasis + Ch.5 prediction vs control)
- **Talk spines (candidates)**: TBD
- **Current snippets**: TBD
- **Notes to add/restore (Atomic Human-inspired)**:
  - TBD (uncertainty is structural; thresholds are governance; “pause when unsure” and escalation discipline)
- **Book references (`\addatomic`) to include** (seed list; extend as needed):
  - `\addatomic{threshold logic}{262-3}`
  - `\addatomic{Laplace’s gremlin}{161, 178, 179, 181, 276}` (if using gremlin framing explicitly)
- **Proposed snippet changes**:
  - TBD

### Session 4 — `intellectual-debt`

- **Current framing**: intellectual debt in the agent era
- **Chapter anchors (target)**: Ch.3, Ch.11, Ch.12, Epilogue (+ optional Ch.2 decomposition/assembly line)
- **Talk spines (candidates)**: TBD
- **Current snippets**: TBD
- **Notes to add/restore (Atomic Human-inspired)**:
  - TBD (decomposition hides accountability; why “understanding” becomes the scarce capability)
- **Book references (`\addatomic`) to include** (seed list; extend as needed):
  - `\addatomic{automation}{6, 24, 46-7, 77-8, 80-81, 83, 85-87, 363-6, 368-369}` (expand as needed)
  - `\addatomic{topography, information}{34-9, 43-8, 57, 62, 104, 115-16, 127, 140, 192, 196, 199, 291, 334, 354-5}` (as the “why debt emerges” precursor)
- **Proposed snippet changes**:
  - TBD

### Session 5 — `project-management`

- **Current framing**: operating model / mission control + Conway/API
- **Chapter anchors (target)**: Ch.7 (+ optional Ch.5 prediction vs control + Ch.2 information factory)
- **Talk spines (candidates)**: TBD
- **Current snippets**: TBD
- **Notes to add/restore (Atomic Human-inspired)**:
  - TBD (mission control as governance; feedback beats prediction; roles + escalation + drills)
- **Book references (`\addatomic`) to include** (seed list; extend as needed):
  - `\addatomic{Laplace’s demon}{111-14, 145}` (as “prediction thinking”)
  - `\addatomic{topography, information}{34-9, 43-8, 57, 62, 104, 115-16, 127, 140, 192, 196, 199, 291, 334, 354-5}` (operating model as topography design)
- **Proposed snippet changes**:
  - TBD

### Session 6 — `ethics-and-privacy`

- **Current framing**: trust + data rights + accountability
- **Chapter anchors (target)**: Ch.8, Ch.10, Ch.12, Epilogue (+ optional Ch.5 info revolution context)
- **Talk spines (candidates)**: TBD
- **Current snippets**: TBD
- **Notes to add/restore (Atomic Human-inspired)**:
  - TBD (trust infrastructure; data-rights as power; System Zero as influence below awareness)
- **Book references (`\addatomic`) to include** (seed list; extend as needed):
  - `\addatomic{System Zero}{242-7, 306, 309, 329, 350, 355, 359, 361, 363, 364}`
  - `\addatomic{Gas Light (play)/gaslighting}{302-3}` (expand if needed)
  - `\addatomic{trust}{43, 79, 100}` (expand if needed)
- **Proposed snippet changes**:
  - TBD

### Session 7 — `bringing-together`

- **Current framing**: executive playbook capstone
- **Chapter anchors (target)**: Epilogue, Ch.12 (+ explicit recap of Ch.2/5/9 as needed)
- **Talk spines (candidates)**: TBD
- **Current snippets**: TBD
- **Notes to add/restore (Atomic Human-inspired)**:
  - TBD (playbook narrative + institutional responsibility; recap the course “spine” explicitly)
- **Book references (`\addatomic`) to include** (seed list; extend as needed):
  - `\addatomic{trust}{43, 79, 100}` (expand if needed)
  - `\addatomic{System Zero}{242-7, 306, 309, 329, 350, 355, 359, 361, 363, 364}` (as a recap of the core risk)
- **Proposed snippet changes**:
  - TBD

## Progress Updates

### 2026-01-28

Task created. Next:

- Populate “current snippets” per session from the include inventory and annotate with freshness flags.
- Draft a first-pass **notes plan** per session and add `\addatomic{...}{...}` tags (using `artifacts/material-review/Lawrence_Neil_thesis_index.txt` for page numbers).

