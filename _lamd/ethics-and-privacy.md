---
session: 6
featured_image: slides/diagrams/atomic-human/Atomic_H_8_System_Zero.png
title: "Trust, Data Rights, and Accountability"
abstract: >
  Privacy and ethics reframed as trust infrastructure for AI and agents: attention as the bottleneck,
  data rights as power, and accountability as an operating discipline. We connect System Zero and
  manipulation risks to concrete governance, recourse, and auditability.
transition: None

---

\section{Trust infrastructure (executive framing)}

\include{_economics/includes/the-attention-economy.md}

\newslide{Executive framing}
\slides{
* If attention is the bottleneck, then influence is the prize.
* Privacy is not “compliance”: it is **control of information flows**.
* Ethics is not “values statements”: it is **recourse**, **auditability**, and **accountable escalation**.
}

\notes{For executives, “ethics and privacy” is not primarily about abstract principles. It is about power and control in information systems: who can see what, who can act on it, and what happens when the system is wrong. If people cannot challenge decisions, cannot understand the evidence, and cannot trigger escalation, then trust collapses and the system becomes a manipulation surface.}

\addatomic{trust}{43, 79, 100}
\addatomic{privacy}{27, 82, 84, 365}
\addatomic{personal data/personal data rights}{82-4, 216, 221, 222, 242-4, 246, 257, 309, 363-5}

\section{System Zero: influence below awareness}

\include{_atomic-human/includes/reality-is-more-humdrum.md}
\include{_atomic-human/includes/surveillance-goes-self-service.md}

\newslide{What makes System Zero risky at scale}
\slides{
* **Asymmetry**: systems see more about us than we see about them.
* **Homogeneity**: one ranking model becomes a society-wide control surface.
* **Optimisation**: incentives push toward engagement/manipulation unless constrained.
}

\notes{System Zero is the "below-awareness" risk: influence without an explicit decision point. The combination of knowledge asymmetry, homogeneity, and optimisation pressure produces a new kind of governance problem: you are managing a control system that can steer behaviour.}

\addatomic{System Zero}{242-7, 306, 309, 329, 350, 355, 359, 361, 363, 364}
\addatomic{knowledge asymmetry}{367}
\addatomic{power asymmetries}{363, 364, 366, 369}
\addatomic{social media}{15, 80, 81, 86, 108, 226, 243, 244, 245, 247, 359, 360, 362, 364}
\addatomic{surveillance capitalism}{222, 244, 257}
\addatomic{digital surveillance}{303-4, 309-10}
\addatomic{state surveillance}{303-6, 308-11, 352}
\addatomic{Gas Light (play)/gaslighting}{302-3}

\section{Data rights, governance, and recourse}

\include{_ai/includes/embodiment-factors-short.md}
\include{_governance/includes/data-property.md}
\include{_governance/includes/gdpr-origins.md}
\include{_governance/includes/feudal-era-data-ecosystem.md}
\include{_governance/includes/digital-highway-code.md}
\include{_governance/includes/data-trusts2.md}

\newslide{Recourse and accountability (minimum viable)}
\slides{
* **Right to challenge**: how can someone appeal a decision?
* **Right to explanation**: what evidence is recorded and reviewable?
* **Named owner**: who is accountable for outcomes (not just the tooling)?
* **Escalation path**: when do we pause automation and revert to humans?
}

\notes{These are the “trust infrastructure” primitives. Without recourse, auditability, and named accountable owners, you do not have governance, you have delegation to an opaque system.}

\newslide{Agent-era governance checklist}
\slides{
* Log what the agent saw, what tools it used, and what it changed.
* Limit blast radius: scopes, rate limits, sandboxes, and kill switches.
* Monitor drift/novelty and route to human escalation.
* Treat failures as incidents: postmortems and control upgrades.
}

\thanks

\reading

\references
