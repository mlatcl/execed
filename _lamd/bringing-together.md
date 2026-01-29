---
session: 7
featured_image: slides/diagrams/atomic-human/Atomic_H_Epilogue.png
title: "Executive Playbook: Leading AI and Agents"
abstract: >
  Capstone synthesis: connect strategy → decisions → data rights → operating model → metrics.
  Provide an executive playbook for adopting AI and agents with accountability, escalation, and resilience.
transition: None
---

\section{Synthesis: what leaders must control}

\newslide{The executive frame (one sentence)}
\slides{
* AI and agents are a change in **how decisions are made** and **how information flows** — at scale.
}

\newslide{Four questions (repeatable)}
\slides{
* What decision are we changing?
* What information does it require (and what’s missing)?
* How can it fail (and how will we notice early)?
* Who is accountable (and what is the escalation path)?
}

\newslide{Where to focus (control points)}
\slides{
* **Incentives/intent**: what is being optimised, and by whom?
* **Uncertainty**: thresholds and “pause when unsure”.
* **Trust & data rights**: asymmetry, recourse, and auditability.
* **Operating model**: roles, decision rights, drills, incident response.
}

\notes{This capstone is a control-point recap. Each item corresponds to an "executive lever" that limits failure at scale: define objectives, make uncertainty legible with thresholds, build trust infrastructure (rights, recourse, auditability), and operate with an explicit model of roles and escalation.}

\addatomic{objectives}{29, 36, 83-4, 148, 149, 179}
\addatomic{topography, information}{34-9, 43-8, 57, 62, 104, 115-16, 127, 140, 192, 196, 199, 291, 334, 354-5}
\addatomic{trust}{43, 79, 100}
\addatomic{System Zero}{242-7, 306, 309, 329, 350, 355, 359, 361, 363, 364}
\addatomic{accountability}{352, 363}
\addatomic{intelligent accountability}{363-4}
\addatomic{automation}{6, 24, 46-7, 77-8, 80-81, 83, 85-87, 363-6, 368-369}

\section{Agents: capability with constraints}

\newslide{Agent rollout ladder}
\slides{
* Sandbox → supervised operation → constrained autonomy → broader autonomy
* Increase autonomy only when monitoring + incident response prove reliable.
* Treat each step as a control upgrade, not just a capability upgrade.
}

\newslide{Minimum viable controls}
\slides{
* **Audit trail**: inputs, tools used, outputs, approvals.
* **Blast radius limits**: scopes, rate limits, sandboxes, kill switches.
* **Monitoring**: drift/novelty, complaints, anomalies.
* **Recourse**: challenge/appeal path and named accountable owner.
}

\notes{Treat documentation as a control surface. Keep “breadcrumbs” that connect WHY → WHAT → HOW → DO so that decisions can be challenged, reviewed, and unwound. If you can’t trace intent to action, you don’t have governance — you have hope.}

\section{30/60/90 day playbook}

\newslide{First 30 days: choose and instrument}
\slides{
* Pick 1–2 high-stakes decisions and write down:
  * objective, data, failure modes, triggers, owner.
* Establish logging/audit expectations (before automation).
* Identify where data rights and privacy constraints bite.
}

\newslide{Days 31–60: operate and drill}
\slides{
* Put the decision into supervised operation with clear escalation.
* Run a pre‑mortem and an incident drill.
* Define metrics for decision quality (not just model accuracy).
}

\newslide{Days 61–90: scale with governance}
\slides{
* Expand scope only after controls work in practice.
* Standardise runbooks, ownership, and post‑incident upgrades.
* Organise an executive debriefs: decisions, controls, incidents, outcomes.
}

\section{Myths to avoid (optional wrap)}

\include{_ai/includes/five-ai-myths.md}

\reading

\thanks

\references
