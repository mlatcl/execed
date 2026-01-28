---
session: 2
featured_image: slides/diagrams/atomic-human/Atomic_H_3_Intent.png
title: "Intent, Incentives, and the Data Crisis"
abstract: >
  We reframe “data readiness” as an executive problem: intent and incentives, attention as the bottleneck,
  and how scaled optimisation creates System Zero risks. We keep DRLs, but treat them as instrumentation
  for decision quality, escalation, and accountability.
transition: None
---

\section{Intent, incentives, and the data crisis}

\include{_atomic-human/includes/trust-autonomy-embodiment.md}

\newslide{Executive framing}
\slides{
* Data isn’t an asset in isolation: it's leverage over **decisions**.
* The crisis is rarely "dirty data" — it's **misaligned intent**, **hidden incentives**, and **unobserved failure** at scale.
* Your default questions: what is the system optimising, who benefits, and who pays when it’s wrong?
}

\notes{The key move in this session is to treat "data readiness" as an executive governance question. Data only matters because it changes decisions. Once decisions are automated or scaled, incentives and optimisation pressure reshape behaviour - and the failure modes stop looking like “bad data” and start looking like organisational blind spots.}

\addatomic{objectives}{29, 36, 83-4, 148, 149, 179}
\addatomic{topography, information}{34-9, 43-8, 57, 62, 104, 115-16, 127, 140, 192, 196, 199, 291, 334, 354-5}

\include{_economics/includes/the-attention-economy.md}

\newslide{How data-driven systems fail (at scale)}
\slides{
* **Goodhart dynamics**: when a measure becomes a target, it stops being a good measure.
* **Gaming/adversaries**: once the objective is learnable, it's exploitable.
* **Homogeneity risk**: one ranking/decision rule becomes a society-wide single point of failure.
* **Accountability gaps**: "the model said so" is not a control system.
}

\notes{These are incentive-shaped failures. If a metric becomes consequential, people (and systems) optimise against it. Once optimisation is legible, it can be gamed. And once many organisations adopt the same decision rule, small flaws become systemic. “The model said so” is not a control system: it’s a delegation without responsibility.}

\section{DRLs as instrumentation (not a checklist)}

\include{_data-science/includes/the-data-crisis.md}
\include{_data-science/includes/lies-damned-lies.md}
\include{_data-science/includes/value-of-data.md}
\include{_data-science/includes/data-science-as-debugging.md}
\include{_data-science/includes/data-readiness-levels.md}

\newslide{Access / Assess / Address (make DRLs operational)}
\slides{
* **Access** (DRL-C): can we legally/ethically/technically get the data?
* **Assess** (DRL-B): what can we learn about the data *before* the downstream question?
* **Address** (DRL-A): what is decision-specific (context, thresholds, deployment)?
}
\notes{Use Access/Assess/Address as the vocabulary that makes DRLs actionable. It separates what can be made reusable (assess) from what must remain decision-specific (address). This is the executive-friendly version of “instrumentation”: it tells you what work reduces future cost, and what work must be governed tightly because it encodes intent.}

\newslide{Background: Big Data}
\slides{
* Data is Pervasive phenomenon that affects all aspects of our activities

* Data diffusiveness is both a challenge and an opportunity
}

\section{System Zero and executive controls}

\include{_atomic-human/includes/reality-is-more-humdrum.md}

\newslide{Controls that survive incentives}
\slides{
* Treat metrics as **attack surfaces**: what can be gamed, and how will you know?
* Build an **escalation path**: “pause when unsure”, human override, and incident response.
* Demand **recourse**: who can challenge/appeal a decision, and what evidence is recorded?
* Keep **accountability human**: delegation is optional; responsibility is not.
}

\notes{System Zero is the reminder that influence can operate below conscious awareness: the system can steer behaviour without an explicit "decision point". That's why auditability, recourse, and escalation aren't compliance theatre - they're control surfaces.}

\addatomic{System Zero}{242-7, 306, 309, 329, 350, 355, 359, 361, 363, 364}
\addatomic{Gas Light (play)/gaslighting}{302-3}
\addatomic{social media}{15, 80, 81, 86, 108, 226, 243, 244, 245, 247, 359, 360, 362, 364}

\newslide{What to do on Monday (practical)}
\slides{
* Pick one high-stakes decision and write down:
  * objective (what are we optimising?),
  * data (what is missing?),
  * failure modes (how can it be gamed?),
  * monitoring (what triggers escalation?),
  * owner (who is accountable?).
* Use DRLs as a readiness instrument, not a maturity badge.
}

\thanks

\reading

\references
