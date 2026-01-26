---
id: "2026-01-26_execed-talk-snippet-themes"
title: "Summarise post-2024 talks and the snippet spines they use (exec-relevant)"
status: "In Progress"
priority: "Medium"
created: "2026-01-26"
last_updated: "2026-01-26"
owner: "Neil D. Lawrence"
related_cips: ["0001"]
related_requirements: ["0001"]
tags: ["execed", "talks", "snippets", "themes", "agents", "llm"]
---

# Task: Summarise post-2024 talks and snippet spines (exec-relevant)

## Description

For talks published since **2024-06-01**, extract and summarise the recurring “snippet spines” used in exec-relevant collections (e.g. `_ai`, `_atomic-human`, `_business`, `_policy`, `_governance`, `_execed`). Use this as evidence for what themes and examples have become central since the book was drafted.

## Acceptance Criteria

- [ ] A short list of recurring snippet spines exists (e.g. new flow of information, HAMs/atomic eye, trust/autonomy/embodiment, System Zero/manipulation).
- [ ] For each spine: provide canonical snippet filenames and representative talks where they appear.
- [ ] Identify what changed post‑2024: LLMs, coding agents, human–agent interaction (and where these themes appear in talks/snippets).

## Related

- **CIP**: `cip/cip0001.md`
- **Talks**: `~/lawrennd/talks/_*/` (source talks only)

## Progress Updates

### 2026-01-26
Status updated to **In Progress**. Added initial synthesis from a scan of source talks with `date >= 2024-06-01`.

## Summary (source talks since 2024-06-01)

Scan notes (source-only, excluding generated `.posts/.slides/.notes/.ipynb` artefacts):

- ~43 `_*/` collections scanned under `~/lawrennd/talks/`
- **125** source talks dated `>= 2024-06-01`

### Most reused snippet includes (overall)

These are the strongest “spines” that recur across multiple audiences:

- **New flow of information** (how data+compute mediate the world)
  - ~71× `_data-science/includes/new-flow-of-information.md`
  - ~70× `_data-science/includes/new-flow-of-information-ham.md`
- **Human–analogue machines / atomic eye** (what modern AI is, and why it feels human)
  - ~58× `_ai/includes/processor-ham.md`
  - ~51× `_ai/includes/the-atomic-eye.md`
- **Conversation / bandwidth / narrative hooks** (how humans relate to machines)
  - ~55× `_ai/includes/conversation-tedx.md`
  - ~48× `_ai/includes/conversation-computer.md`
  - ~39× `_ai/includes/baby-shoes.md`
  - ~29× `_ai/includes/diving-bell-butterfly.md`
  - ~31× `_ai/includes/cuneiform.md`
- **Trust and accountability** (delegation, oversight, governance)
  - ~30× `_atomic-human/includes/trust-autonomy-embodiment.md`
- **Business / operating model layer**
  - ~28× `_business/includes/attention-flywheel.md`
  - ~20× `_business/includes/supply-chain-of-ideas.md`
  - ~20× `_business/includes/the-productivity-flywheel.md`
  - ~29× `_business/includes/ft-op-ed.md`

### Exec-relevant collections (counts + dominant spines)

- **`_ai` (25 talks)**: `new-flow-of-information*`, `processor-ham`, `the-atomic-eye`, `conversation-*`
- **`_atomic-human` (24 talks)**: `the-atomic-eye`, `processor-ham`, `new-flow-of-information*`, `trust-autonomy-embodiment`
- **`_business` (17 talks)**: `conversation-computer`, `processor-ham`, `new-flow-of-information*`, plus `attention-flywheel` + productivity snippets
- **`_policy` (17 talks)**: `cuneiform`, `new-flow-of-information*`, and productivity/innovation-policy snippets

## What changed post‑2024 (implications for execed)

### 1) LLMs and agents become an operating-model problem (not just a model problem)

Signals:
- Increased appearance of “human + computer interacting” framing and explicit LLM-related themes in recent talk variants.
- In exec terms: delegation, oversight, auditability, and measurement of decision quality (avoid automation complacency).

Practical framing for execed:
- Where to allow agents (low consequence, reversible, sandboxed)
- Where to require supervision (high consequence, non-reversible, regulated decisions)
- What to measure (review rates, overrides, incident patterns, recovery time, downstream burden)

### 2) Trust / manipulation / System Zero becomes central to risk framing

Signals:
- The recurring trust/autonomy/embodiment spine, combined with policy/business snippets, indicates “risk” is increasingly about incentive design and scaled influence.

### 3) The “new flow of information” becomes the universal entry point

Signals:
- The most reused spine across talks is the information-flow reframing.
- This is likely the right opening lens for execed (before tools, before vendors).

## Representative talk anchors (examples)

Examples of talk files that typically carry the above spines (use as source references when rewriting execed):

- `_ai/*the-atomic-human*.md` variants (often combine conversation/bandwidth, atomic eye, new flow, trust)
- `_business/*ai-opportunities-and-challenges*.md` variants (often add attention/productivity flywheels)
- `_ai/information-in-the-age-of-ai.md` (explicitly bridges information framing and modern AI/LLM era)

## Acceptance Criteria checklist

- [x] A short list of recurring snippet spines exists.
- [x] Canonical snippet filenames are listed (with relative strength via counts).
- [ ] Add 2–3 representative talk filenames per spine (with links/paths) for quick reference during rewriting.

