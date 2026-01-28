---
session: 5
featured_image: slides/diagrams/atomic-human/Atomic_H_7_Not_Rocket.png
title: "Operating Model: Mission Control for AI"
abstract: >
  Project management reframed as an operating model for high‑stakes socio‑technical systems: decision rights,
  escalation, simulation, and incident response. We connect organisational structure to system structure
  (Conway’s Law, the API mandate) and show how this becomes essential in the agent era.
transition: None

---

\section{Operating model, not pilots}

\newslide{Executive framing}
\slides{
* “AI delivery” fails when it's treated as a tool rollout.
* It succeeds when it's treated as an **operating model change**:
  * decision rights,
  * escalation,
  * accountability,
  * and practice under failure.
}

\newslide{What changes in the agent era}
\slides{
* Systems don’t just predict — they can **act** (via tools, workflows, and delegation).
* That increases speed and surface area.
* The question becomes: what is allowed to run unattended, and how do we stop it?
}

\section{Organisation ↔ architecture}

\include{_business/includes/institutional-character.md}

\section{Mission control: roles, escalation, practice}

\newslide{Mission control primitives (minimum viable)}
\slides{
* **Roles**: operator, reviewer, owner, risk/compliance, incident lead.
* **Decision rights**: automate / assist / escalate (make it explicit).
* **Runbooks**: “what do we do when it fails?” (before it fails).
* **Drills**: pre‑mortems, simulations, and incident exercises.
}

\newslide{Escalation design}
\slides{
* Define triggers for human escalation (uncertainty, novelty, drift, complaints, anomalies).
* Include “pause when unsure” as a first-class action.
* Make override real: time-bounded decisions, rollback paths, and audit trails.
}

\newslide{How to structure a rollout}
\slides{
* Sandbox → supervised operation → constrained autonomy → broader autonomy.
* Increase autonomy only when monitoring + incident response prove reliable.
* Treat each step as a control upgrade, not just a capability upgrade.
}

\newslide{What to do on Monday (practical)}
\slides{
* Pick one automated (or candidate) decision and document:
  * owner/accountable person,
  * decision rights (what can run without approval),
  * triggers + escalation path,
  * logs/audit trail expectations,
  * “kill switch” and rollback.
}

\notes{A simple governance rhythm you can reuse: WHY → WHAT → HOW → DO → DOCUMENT. WHY: principles you won’t trade off. WHAT: outcomes that must be true. HOW: operating design (roles, escalation, interfaces). DO: this week’s tasks. DOCUMENT: keep decision breadcrumbs so you can explain and unwind. This is the difference between "pilot theatre" and an operating model that survives scale.}

\thanks

\reading

\references
