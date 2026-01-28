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
- Include inventory outputs: `artifacts/material-review/inventory.json` (generated). Prefer `includes_transitive` / `include_frequency_transitive` when available.
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
- **Talk spines (candidates)**:
  - From `~/lawrennd/talks/_business/`:
    - `the-age-of-generative-ai-june-2024-alp.md`
    - `data-first-culture-november-24.md`
    - `ai-opportunities-and-challenges-may-2025.md`
    - `leading-with-ai-lloyds-bank.md`
    - `human-machine-collaboration.md`
  - From `~/lawrennd/talks/_atomic-human/` (many variants share the same spine; pick the most recent-delivered deck):
    - `how-ai-works-and-how-it-will-transform-our-lives.md`
    - `business-and-the-atomic-human.md`
    - `ai-and-capability-shaping-servicenow.md`
    - `translating-ai-into-practice-astrazeneca.md`
    - `humans-in-the-ai-world.md` (and cohort variants)
- **Current snippets (current lecture includes)**:
  - `_atomic-human/includes/gods-and-robots-scribeysense.md`
  - `_data-science/includes/new-flow-of-information.md`
  - `_ai/includes/processor-ham.md`
  - `_ai/includes/the-atomic-eye.md`
  - `_data-science/includes/evolved-relationship.md`
  - `_ai/includes/embodiment-factors.md`
  - `_ai/includes/centrifugal-governor.md`
  - `_ai/includes/conversation-computer.md`
  - `_atomic-human/includes/trust-autonomy-embodiment.md`
  - `_data-science/includes/three-data-science-challenges.md`

- **Transitive snippet usage (includes inside included snippets)** (highlights from latest transitive inventory):
  - From `_ai/includes/embodiment-factors.md`:
    - `_ai/includes/embodiment-factors-short.md` (contains the core `\addatomic{embodiment factor}{...}` block)
    - `_ai/includes/embodiment-factors-computer-human-table.html` (embedded figure/table)
    - `_ai/includes/formula-one-engine.md`, `_ai/includes/marcel-renault.md`, `_ai/includes/caleb-mcduff.md` (examples used by the embodiment section)
  - From `_ai/includes/centrifugal-governor.md`:
    - `_ai/includes/holborn-science-centrifugal-governor.md`, `_ai/includes/watt-steam-engine.md`, `_ai/includes/centrifugal-governor-diagram.md`
  - From `_atomic-human/includes/trust-autonomy-embodiment.md`:
    - `_atomic-human/includes/trust-autonomy-embodiment-diagram.md`
- **Notes to add/restore (Atomic Human-inspired)**:
  - The “AI moment” is a *change in the flow of information* that makes different decisions cheap to automate (and cheap to scale).
  - The executive risk is not “superintelligence”, it’s **scale + incentives + feedback**: a system that is *slightly wrong* can become *systemically harmful* when rolled out everywhere.
  - Distinguish:
    - **Intelligent entities** (anthropomorphic framing that invites magical thinking)
    - **Intelligent systems** (supply chains, platforms, credit systems: lots of small automated decisions, coordinated through data + incentives)
  - The core leadership question to keep repeating: *what is the decision, what information does it require, how can it fail, and who is on the hook?*
  - “Conversation” is a capability shift: the interface cost collapses, so delegation temptation rises — but accountability must remain with humans (preview Session 4/6).
  - Trust/autonomy is an operating design choice: devolve authority *only* where information is complete enough and escalation is real (preview Session 5 mission control).
- **Book references (`\addatomic`) to include** (seed list; extend as needed):
  - `\addatomic{embodiment factor}{13, 29, 35, 79, 87, 105, 197, 216-217, 249, 269, 327, 353, 363, 369}`
  - `\addatomic{topography, information}{34-9, 43-8, 57, 62, 104, 115-16, 127, 140, 192, 196, 199, 291, 334, 354-5}`
  - `\addatomic{printing press}{8, 9, 13, 24, 68, 75, 104-5, 106-8, 107-8, 345, 354-5}`
  - `\addatomic{Laplace’s demon}{111-14, 145}` (expand page list as needed)
  - `\addatomic{telepathy}{248-50}` (if we use the “Turing got fooled by social cues” point)
- **Proposed snippet changes**:
  - Add a small Ch.5 anchor snippet (printing press ↔ social media) to make the “information revolution” analogy explicit *without* turning Session 1 into a history lecture.
  - Consider adding a Ch.9 “AI fallacy” micro-snippet (machines don’t understand like humans; social cue illusions) if we see repeated executive anthropomorphism in delivery feedback.

- **Per-snippet patch list (Session 1)** (proposals: add missing `\notes{...}` and `\addatomic{...}{...}`):
  - `_atomic-human/includes/gods-and-robots-scribeysense.md`
    - Add `\notes{...}`: “we project personhood onto machines; ‘god/robot’ imagery is a cognitive trap; keep the frame on decisions, incentives, and institutions.”
    - Add book refs:
      - `\addatomic{Terminator image embodies}{7, 9, 12, 13, 21, 30, 31, 216, 220, 257, 333, 353}`
      - `\addatomic{Terminator (movie character)}{7, 9, 12, 13, 21, 30, 31, 216, 220, 257, 333, 353}`
      - `\addatomic{anthropomorphization (‘anthrox’)}{30-31, 90-91, 93-4, 100, 132, 148, 153, 163, 216-17, 239, 276, 326, 342}`
  - `_data-science/includes/new-flow-of-information.md`
    - Add book refs (so the notes link back explicitly to the Atomic Human framing):
      - `\addatomic{topography, information}{34-9, 43-8, 57, 62, 104, 115-16, 127, 140, 192, 196, 199, 291, 334, 354-5}`
      - `\addatomic{anthropomorphization (‘anthrox’)}{30-31, 90-91, 93-4, 100, 132, 148, 153, 163, 216-17, 239, 276, 326, 342}` (since the notes already use the idea)
    - Do **not** anchor Shannon/information-theory references here; those belong more naturally with the embodiment/info-theory material (and should live in `_ai/includes/embodiment-factors-short.md` or a dedicated info-theory snippet).
  - `_ai/includes/processor-ham.md`
    - Add book refs:
      - `\addatomic{ignorance: HAMs}{347}` (if we explicitly use the “HAM” framing here)
      - `\addatomic{test pilot}{163-8, 189, 190, 192-3, 196, 197, 200, 211, 245}` (if we keep the Apollo/test‑pilot analogy in the notes)
  - `_ai/includes/the-atomic-eye.md`
    - No change required (already has notes and `\addatomic{atomic human, the}{13}`).
  - `_data-science/includes/evolved-relationship.md`
    - Optionally add book refs to tie the “phone distraction / misaligned objectives” story to the book’s System Zero language:
      - `\addatomic{System Zero}{242-7, 306, 309, 329, 350, 355, 359, 361, 363, 364}`
  - `_ai/includes/embodiment-factors.md`
    - Confirm that the included `_ai/includes/embodiment-factors-short.md` remains the canonical `\addatomic{embodiment factor}{...}` source for this deck (no new snippet needed unless we want a shorter page list for exec delivery).
  - `_ai/includes/centrifugal-governor.md`
    - Add book refs (so the “control/feedback” archetype is explicitly sourced):
      - `\addatomic{Watt’s governor}{122-5, 127, 131, 143, 144, 184, 198, 202-3, 206, 207, 221, 231, 234, 251, 254, 256-7, 263}`
      - `\addatomic{cybernetics founded by}{131, 143, 306}` (if we explicitly name cybernetics as “governor”)
  - `_ai/includes/conversation-computer.md`
    - Add book refs (to anchor the “conversation ≠ understanding” point back to the book):
      - `\addatomic{telepathy}{248-50}` (if we connect to the Turing anecdote / social cues)
      - `\addatomic{anthropomorphization (‘anthrox’)}{30-31, 90-91, 93-4, 100, 132, 148, 153, 163, 216-17, 239, 276, 326, 342}`
  - `_atomic-human/includes/trust-autonomy-embodiment.md`
    - Add `\notes{...}`: trust as infrastructure for devolved autonomy; accountability is the price of delegation; “earn trust” is an operating mechanism, not a slogan.
    - Add book refs:
      - `\addatomic{trust}{43, 79, 100}` (expand as needed once we decide which trust points are surfaced)
      - `\addatomic{embodiment factor}{13, 29, 35, 79, 87, 105, 197, 216-217, 249, 269, 327, 353, 363, 369}`
      - `\addatomic{topography, information}{34-9, 43-8, 57, 62, 104, 115-16, 127, 140, 192, 196, 199, 291, 334, 354-5}`
  - `_data-science/includes/three-data-science-challenges.md`
    - Optional: add `\addatomic{System Zero}{242-7, 306, 309, 329, 350, 355, 359, 361, 363, 364}` if we explicitly name “loss of control” as System Zero-style influence rather than generic privacy risk.

- **Book/chapter alignment check (Session 1)** (re-checked against chapter sources + index):
  - **Prologue (AI “moment” as investment/expectations shift)**: covered by the opening slides (branding + investment jump framing). Good.
  - **Ch.1 (mythic AI framing; Terminator/God imagery; Narcissus; anthropomorphization)**: covered via `_atomic-human/includes/gods-and-robots-scribeysense.md` notes + `\addatomic` tags. Good.
  - **Ch.3 (Intent)**: only indirectly present (via “what decision / what information” questions). Candidate improvement: add a short, explicit “intent” anchor (either a small snippet or a 2–3 bullet note block) so Session 1 names the concept.
  - **Ch.12 (Trust / accountability)**: partially covered via trust/autonomy snippet. Candidate improvement: add one line in notes linking trust to “intelligent accountability” (Baroness O’Neill framing) to sharpen the business-facing takeaway.
  - **Ch.5 (information revolutions / printing press analogue)**: not explicitly anchored yet (still a proposed addition).
  - **Ch.9 (AI fallacy / conversation ≠ understanding)**: partially covered by conversation + anthropomorphization, but not explicitly named; optional micro-anchor remains sensible.

### Session 2 — `the-data-crisis`

- **Current framing**: intent/incentives + System Zero + attention
- **Chapter anchors (target)**: Ch.3, Ch.8, Ch.10 (+ optional Ch.5 printing press → social media)
- **Talk spines (candidates)** (examples that already carry key Session 2 snippets):
  - Attention economy:
    - `~/lawrennd/talks/_business/leading-with-ai-lloyds-bank.md`
    - `~/lawrennd/talks/_business/ai-opportunities-and-challenges-may-2025.md`
    - `~/lawrennd/talks/_business/the-transformative-power-of-ai-and-its-challenges.md`
    - `~/lawrennd/talks/_atomic-human/humans-in-the-ai-world.md` (and cohort variants)
    - `~/lawrennd/talks/_economics/ai-cannot-replace-the-atomic-human-mimit.md` (and variants across `_economics`, `_policy`)
  - “Data crisis” framing:
    - `~/lawrennd/talks/_business/data-first-culture.md` (includes `_data-science/includes/the-data-crisis.md`)
    - `~/lawrennd/talks/_business/post-digital-transformation.md` (includes `_data-science/includes/data-readiness-levels.md`)
- **Current snippets (current lecture includes)**:
  - `_atomic-human/includes/trust-autonomy-embodiment.md`
  - `_economics/includes/the-attention-economy.md`
  - `_data-science/includes/the-data-crisis.md`
  - `_data-science/includes/lies-damned-lies.md`
  - `_data-science/includes/value-of-data.md`
  - `_data-science/includes/data-science-as-debugging.md`
  - `_data-science/includes/data-readiness-levels.md`
  - `_atomic-human/includes/reality-is-more-humdrum.md`

- **Transitive snippet usage (includes inside included snippets)** (highlights):
  - From `_economics/includes/the-attention-economy.md`:
    - `_economics/includes/herbert-simon-information.md`
  - From `_data-science/includes/data-readiness-levels.md`:
    - `_data-science/includes/data-readiness-levels-short.md`
    - `_data-science/includes/three-grades-of-data-readiness.md`
    - `_data-science/includes/data-joel-tests.md`
  - From `_data-science/includes/lies-damned-lies.md`:
    - `_data-science/includes/lies-damned-lies-big-data.md`
  - Supporting/background pulled in by DRL/transparency framing:
    - `_statistics/includes/mathematical-statistics.md`
  - From trust/autonomy:
    - `_atomic-human/includes/trust-autonomy-embodiment-diagram.md`
- **Notes to add/restore (Atomic Human-inspired)**:
  - “Data crisis” is mostly not about cleanliness — it’s about **objectives**: what the system is optimising, what it rewards, and what it makes invisible.
  - Attention is the bottleneck: when attention is scarce, **rankings become power**, and incentives to manipulate the information topography intensify.
  - Goodhart dynamics should be treated as a default: assume metrics will be gamed once they become consequential.
  - System Zero is the “below-awareness” failure mode: influence and manipulation can occur without explicit persuasion.
  - Executive control primitives to emphasise: escalation (“pause when unsure”), recourse/appeals, audit trails, and named accountable owners.
- **Book references (`\addatomic`) to include** (seed list; extend as needed):
  - `\addatomic{System Zero}{242-7, 306, 309, 329, 350, 355, 359, 361, 363, 364}`
  - `\addatomic{Gas Light (play)/gaslighting}{302-3}` (expand if needed)
  - `\addatomic{trust}{43, 79, 100}` (expand if needed)
  - `\addatomic{printing press}{8, 9, 13, 24, 68, 75, 104-5, 106-8, 107-8, 345, 354-5}` (if using the “info revolution” analogue)
  - `\addatomic{objectives}{29, 36, 83-4, 148, 149, 179}` (for the “what are we optimising?” framing)
  - `\addatomic{social media}{15, 80, 81, 86, 108, 226, 243, 244, 245, 247, 359, 360, 362, 364}` (if we explicitly name the incentive/attention context)
  - `\addatomic{topography, information}{34-9, 43-8, 57, 62, 104, 115-16, 127, 140, 192, 196, 199, 291, 334, 354-5}` (if we make “information topography” explicit rather than implicit)
- **Proposed snippet changes**:
  - Consider adding an exec-friendly “Access / Assess / Address” micro-anchor (Fynesse framework) to make the DRL story actionable:
    - Canonical source snippet: `_data-science/includes/access-assess-address.md`
    - Rationale: it explicitly maps to DRLs (**Access ↔ DRL-C**, **Assess ↔ DRL-B**, **Address ↔ DRL-A**) and gives an operating vocabulary that integrates cleanly with “DRLs as instrumentation”.
  - If we want a stronger explicit Ch.3 “Intent” anchor, consider adding a short atomic-human intent snippet (or a very small `\notes{...}` block) that defines intent vs observed behaviour (“objective is learnable, therefore gameable”).
  - Ch.10 (Gaslighting) is currently referenced in the framing but not strongly anchored in the snippet set for Session 2 (it is more central in Session 6). Decide whether to:
    - keep gaslighting as a light mention here, or
    - add a small Ch.10-aligned snippet (only if it improves the narrative and doesn’t duplicate Session 6).

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
- **Breadcrumbs / governance micro-anchor (VibeSafe-inspired)**:
  - Add 2–3 speaker-note bullets that translate “breadcrumbs” into exec language:
    - make **intent explicit before implementation** (what are we trying to do?),
    - keep **audit trails** (what changed, why, and who approved it),
    - define **breakpoints for review** (when humans must re-check).
  - Use as a bridge from “intellectual debt” → “agent era”: the cost of misinterpretation is drift you can’t unwind.
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
- **Breadcrumbs / governance micro-anchor (VibeSafe-inspired)**:
  - Add a “WHY → WHAT → HOW → DO → DOCUMENT” framing line as a practical operating rhythm:
    - **WHY**: principles (what we will not trade off)
    - **WHAT**: outcomes (what must be true)
    - **HOW**: operating design (roles, escalation, interfaces)
    - **DO**: tasks (who does what this week)
    - **DOCUMENT**: keep decision breadcrumbs (so the system stays maintainable)
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
- **Breadcrumbs / governance micro-anchor (VibeSafe-inspired)**:
  - In the capstone recap, include a “minimum viable governance loop” slide/note:
    - keep a short chain from **WHY** to **DO** (so people can challenge decisions),
    - keep breadcrumbs so you can **explain and unwind**,
    - treat documentation as a **control surface** (not an afterthought).
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

