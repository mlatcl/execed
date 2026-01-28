---
session: 3
featured_image: slides/diagrams/atomic-human/Atomic_H_6_Gremlin.png
title: "Uncertainty, Data Quality, and Decision Thresholds"
abstract: >
  Reframe “data quality” as executive decision-quality under uncertainty: what to measure, when to escalate,
  and how to “pause when unsure”. We keep DRLs, but connect them to calibration, thresholds, and operational readiness.
transition: None
---

\section{Decision quality under uncertainty}

\include{_atomic-human/includes/a-diversity-of-approaches-brings-resilience.md}

\newslide{Executive framing}
\slides{
* Data quality is not cleanliness — it’s whether decisions are **reliable enough** for their consequences.
* Uncertainty is unavoidable; governance is about **thresholds**, **monitoring**, and **escalation**.
* Default rule: when uncertainty is high, slow down and widen the loop.
}

\notes{This is the "gremlin" lesson: uncertainty never disappears, it only gets hidden. So the executive question is not “is the data perfect?” but “is the decision reliable enough, and what happens when it isn’t?” Good governance makes uncertainty legible: calibrated confidence, explicit thresholds, and real escalation paths.}

\addatomic{uncertainty}{150-52, 158, 160, 168}
\addatomic{Laplace’s gremlin}{161, 178, 179, 181, 276}

\include{_atomic-human/includes/reflective-or-reactive.md}

\newslide{A simple operating discipline}
\slides{
* Define decision thresholds (automate / assist / escalate).
* Instrument uncertainty (calibration, drift, novelty) and set triggers.
* Practice incident response: “pause when unsure” and rollback/override.
}

\notes{Threshold logic is governance: it defines what can run unattended and what must route to humans. Calibration matters because "confidence" only helps if it means what it says. “Pause when unsure” is the organisational commitment to treat uncertainty as a first-class signal.}

\addatomic{threshold logic}{262-3}
\addatomic{probability}{111, 136, 161, 162, 168-70}

\include{_data-science/includes/gartner-hype-cycle-ai-bd-dm-dl-ml.md}
<!--include{_ai/includes/game-playing-ai.md}-->
\subsection{Machine Learning}
$$
\text{data} + \text{model} \stackrel{\text{compute}}{\rightarrow} \text{prediction}
$$

\subsection{Code and Data Separation}

* Classical computer science separates code and data.
* Machine learning short-circuits this separation.


\subsection{Example: Supply Chain}

\include{_data-science/includes/why-didnt-electricity.md}

\include{_supply-chain/includes/bits-and-atoms.md}
\include{_supply-chain/includes/experiment-analyze-design-supply-chain.md}
\include{_supply-chain/includes/supply-chain.md}
\include{_supply-chain/includes/ml-and-supply-chain.md}

<!--Duke of York Effect -->

\include{_ml/includes/or-control-econometrics-statistics-ml.md}

\include{_data-science/includes/data-readiness-levels.md}
\include{_business/includes/data-maturity-assessment.md}
<!--include{_ml/includes/shiny-bike-model.md}-->

\section{Introduction}



\subsection{Conclusions}

* Data is modern software
* We need to revisit software engineering and computer science in this context.

\notes{Practical takeaway: pick one automated (or candidate) decision and write down the threshold ladder (automate/assist/escalate), the monitoring triggers, and the escalation owner. Then treat each incident as a feedback loop: adjust thresholds, improve instrumentation, and reduce intellectual debt rather than patching ad hoc.}


\thanks

\reading

\references
