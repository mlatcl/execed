---
category: features
created: '2026-01-26'
id: 2026-01-26_execed-update-remaining-lectures
last_updated: '2026-01-26'
owner: Neil D. Lawrence
priority: High
related_cips:
- '0001'
status: Proposed
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

## Progress Updates

### 2026-01-26
Task created.
