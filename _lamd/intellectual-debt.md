---
session: 4
featured_image: slides/diagrams/atomic-human/Atomic_H_11_Human_Analogue.png
title: "Intellectual Debt in the Agent Era"
abstract: >
  Connect “technical/intellectual debt” to accountability and auditability when systems include ML and agents.
  The core risk is not just complexity, but loss of understanding and control: who can explain, stop, or override
  when automation drifts or fails?
transition: None
---

\section{Intellectual debt as an accountability gap}

\include{_ai/includes/the-sorcerers-apprentice.md}

\newslide{Executive framing}
\slides{
* Debt is not a metaphor — it’s an **interest rate on change** (every modification gets slower and riskier).
* Intellectual debt creates **control loss**: nobody can explain end-to-end behaviour under stress.
* With agents, that becomes **operational risk**: actions happen faster than review and across more surfaces.
}

\include{_ai/includes/intellectual-debt-short.md}
\include{_ai/includes/data-and-intellectual-debt.md}

\include{_ai/includes/the-great-ai-fallacy.md}
\include{_ai/includes/artificial-vs-natural-systems.md}
\include{_engineering/includes/mythical-man-month.md}
\include{_ai/includes/ml-system-decomposability.md}
\include{_ai/includes/ride-allocation-prediction.md}
\include{_ai/includes/ml-systems-design-short.md}
\include{_ml/includes/ml-paradigm-shift.md}
\include{_ai/includes/peppercorn.md}
\include{_data-science/includes/experiment-analyze-design.md}
\include{_data-science/includes/data-oriented-architectures.md}

\newslide{Agent-era guardrails (minimum viable control)}
\slides{
* **Declare** models/agents as first-class dependencies (ownership + versioning).
* **Instrument** drift/novelty and route to escalation (“pause when unsure”).
* **Record** an audit trail: inputs, tools used, outputs, and approvals.
* **Limit blast radius**: scopes, sandboxes, rate limits, and kill switches.
}

\thanks

\reading

\references
