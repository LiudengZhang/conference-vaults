# KDD 2026

**32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining** — International Convention Center Jeju (ICC Jeju), **Jeju, South Korea**, **August 9–13, 2026**.

> **Status:** Scaffold — meeting ~3 months out (today is May 11, 2026). Cycle 2 main-track notifications are due May 16, 2026 (this week); BIOKDD submissions close May 14, 2026 with notification June 4, 2026. This is a **light build**, not full coverage — see "Scope" below.

## Why this is in the vault

KDD is the premier general-purpose data-mining conference (~3,500 attendees in recent years), with an unusually strong **applied research / industry track (ADS)** alongside its academic Research Track. Unlike NeurIPS / ICML / ICLR — which are the deep-learning methods venues — KDD's center of gravity sits on **structured-data ML, graph mining, recommender systems, time-series, EHR mining, clinical NLP, and large-scale productionized pipelines**. That makes its cancer-relevant subset distinct from the ML venues: less foundation-model preprint-bait, more EHR-cohort / claims-data / multi-omics-pipeline / drug-repurposing graph work that lands closer to the clinic.

Three concrete reasons to keep a scoped presence:

- **EHR mining + clinical NLP pipeline.** KDD historically hosts the largest non-AMIA cluster of EHR / claims / longitudinal-cohort papers in the ML world, including the recurring **epiDAMIK** workshop on data-driven public/population health. These pipelines feed AACR's outcomes-research and clinico-genomics axes.
- **Bioinformatics + multi-omics ML.** **BIOKDD 2026** is the workshop's 25th edition; the 2026 theme is "Digital Twins" — disease-trajectory simulation, cell-cell communication, microenvironmental interactions, post-treatment outcome prediction. This is the closest KDD analog to ICML's GenBio / FM4LS bio cluster, but with a tilt toward applied multi-omics rather than de novo design.
- **Healthcare agentic-AI + LLM-grounding.** KDD 2026 has an unusually heavy agentic-AI workshop slate (RelSciFM, SciSoc Agents & LLMs, Enterprise AI Agents, AEGIS for evidence-grounded interventional systems, KDD Eval for agentic-AI trustworthiness). Many of these reliably adapt to clinical / oncology use within 6 months.

KDD 2026 introduces a new **AI for Sciences track** (inaugural year) that explicitly welcomes "health sciences, healthcare, bioinformatics, epidemiology, pharmaceuticals, systems biology, multiomics, neuroscience." This consolidates work that previously spread across Research and ADS tracks and is our primary main-track filter target.

## Scope (what this vault covers — and what it does not)

**In scope (light build):**

- The **bio / health / drug-discovery / clinical-NLP / public-health workshops** at KDD 2026 (see roster below).
- **AI for Sciences track** papers in the biomedical / health subset.
- **Research Track + ADS Track** papers matching a **cancer / genomics / single-cell / spatial / drug-discovery / EHR / clinical-NLP / pathology / healthcare-graph keyword filter** (anticipate a few dozen out of ~700 main-track papers across two cycles).
- The **agentic-AI / LLM-for-science** subset of the main-track + agentic-AI workshops, regardless of explicit bio framing.

**Out of scope:**

- General data-mining bulk: recommender systems, e-commerce, advertising (AdKDD), search/discovery (TSMO), urban computing (UrbComp), finance (MLF), talent computing (TMC), fraud / integrity work without a healthcare hook.
- Tutorials and KDD Cup challenges outside the bio / health niches.
- The full main proceedings (~700 papers across two cycles); bulk extraction is explicitly **not** planned.
- Korea Day / Special Days programming unless content overlaps.

## Anticipated bio / health-relevant workshops

The 2026 workshop roster is finalized (30 workshops total). The bio / health / clinical / agentic-AI-with-science-hook subset:

| Workshop | Theme | Acronym | Notes |
|---|---|---|---|
| 25th International Workshop on Data Mining in Bioinformatics | data mining for bioinformatics, biomedical informatics; 2026 theme "Digital Twins" — disease trajectories, cell-cell comm, treatment-response prediction | **BIOKDD 2026** | Submission May 14, notification Jun 4, 2026; IEEE/ACM TCBB special issue for full papers |
| Workshop on Data-driven Decision Making for Public and Population Health | epidemiology, public health, AI/data systems for population health; recurring since 2018 | **epiDAMIK 2026** | Aug 9 or 10, 2026 |
| Adaptation and Evidence-grounding of Generative Interventional Systems | evidence-grounded generative AI for interventional / clinical decision systems; UF College of Public Health & Health Professions affiliated | **AEGIS 2026** | First edition; clinical decision-support focus |
| Reliable Scientific Foundation Models: Design, Training, Grounding, Verification | trustworthy FMs for science — design, evaluation, grounding | **RelSciFM 2026** | Bio/chem subset only; skip generic FM theory |
| The Second Workshop on SciSoc Agents & LLMs: Agentic AI for Scientific and Societal Advances | LLM agents for scientific and societal applications | **SciSoc LLM 2026** | Science-agent subset only |
| KDD workshop on Evaluation and Trustworthiness of Agentic AI | agentic-AI evaluation, safety, trustworthiness | **AgenticAI-Eval 2026** | Healthcare-deployment subset |
| The International Workshop on AI for Cognitive and Mental Health Support | clinical AI for mental health, cognitive support | **AI4Mental 2026** | First edition; psycho-oncology adjacent |
| Responsible Multimodal Foundation Models for Knowledge Discovery | multimodal FMs, responsible / robust deployment | **RespMultimodal 2026** | Medical-imaging / clinical-multimodal subset |
| Enterprise AI Agents: From Prototypes to Production | productionizing agentic systems; relevant where pharma / biotech is in scope | **EntAIAgents 2026** | Pharma/biotech-deployment subset only |

The seven core bio/health/agentic-with-science workshops above are the anchor; another ~3 (RelSciFM, RespMultimodal, EntAIAgents) get filtered partial coverage. The remaining ~20 workshops (advertising, finance, urban, fraud, recsys, time-series-generic, federated-generic) are out of scope.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Main proceedings** | ~700 accepted papers across Cycle 1 + Cycle 2 | ACM Digital Library / KDD proceedings; OpenReview KDD.org/2026/Conference group hosts decision records. Cycle 1 notifications were Nov 23, 2025; Cycle 2 notifications due May 16, 2026. |
| **AI for Sciences track** | inaugural track | Biomedical / health applications consolidated here; cleanest filter target. |
| **Workshop OpenReview / sites** | one venue per workshop | BIOKDD, epiDAMIK, AEGIS, RelSciFM, SciSoc LLM, AgenticAI-Eval, AI4Mental, RespMultimodal each host their own site. |
| **bioRxiv / medRxiv mirrors** | most bio-relevant KDD papers have a preprint | Filter for "KDD 2026" mentions; especially for BIOKDD digital-twin contributions. |
| **Twitter/Bluesky** | real-time reactions | `#KDD2026`; useful for agentic-AI-for-science orals. |
| **Recorded talks** | YouTube + KDD virtual platform | KDD records ADS orals + most workshop keynotes; posts within ~2–4 weeks of meeting. |
| **Cross-link with NeurIPS / ICML** | author + tool overlap | KDD's August slot sits between ICML (July) and NeurIPS (December); the same agentic-AI / FM-bio authors often appear at all three. |
| **Cross-link with AMIA / ML4H** | EHR / clinical-NLP author overlap | KDD's EHR cluster heavily overlaps with AMIA Annual Symposium (Nov) and ML4H @ NeurIPS. |

## Organization

```
conferences/kdd-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep — dates, filter criteria, expected themes
└── tools/               # per-paper / per-tool entries, populated post-notification
    └── index.md         # template + scope-filter note
```

No `digest/`, no `themes.md`, no `keynotes/`. The light-build pattern mirrors NeurIPS 2026 / ICML 2026 / CVPR 2026: only `tools/` gets populated, and only with the filtered subset.

## What's different from full-conference vaults

Compared to ISMB 2026, RECOMB 2026, AACR 2026, ASCO 2026, or EuroBioC 2025 — which aim at near-complete program coverage — KDD 2026 is **scope-limited by design**:

- No per-session digests, no per-day digests, no themes synthesis. The general-purpose data-mining bulk is irrelevant.
- No keynote / plenary coverage unless the speaker is a known bio / clinical-AI author.
- Tool entries are filtered down to a few dozen, not exhaustive. The filter is keyed on the AACR axes, not on KDD's own taxonomy.
- Most KDD 2026 tool entries should explicitly cross-link to a **NeurIPS 2026 / ICML 2026 / AMIA 2026 cousin paper** — KDD's EHR-cluster overlaps AMIA, its bio-cluster overlaps NeurIPS LMRL / ICML FM4LS, and its agentic-AI cluster overlaps all three ML venues.

## Key dates

| Date | Event |
|---|---|
| Jul 24, 2025 | Cycle 1 abstract deadline — past |
| Jul 31, 2025 | Cycle 1 full-paper deadline — past |
| Oct 4–18, 2025 | Cycle 1 rebuttal period — past |
| Nov 23, 2025 | Cycle 1 notifications — past |
| Feb 1, 2026 | Cycle 2 abstract deadline — past |
| Feb 8, 2026 | Cycle 2 full-paper deadline — past |
| Apr 4–17, 2026 | Cycle 2 rebuttal period — past |
| May 14, 2026 | BIOKDD 2026 submission deadline (extended) — **this week** |
| **May 16, 2026** | Cycle 2 main-track notifications — **this week** |
| Jun 4, 2026 | BIOKDD 2026 notification |
| **Aug 9–13, 2026** | KDD 2026 main meeting, Jeju, ICC Jeju |
| Aug 9 or 10, 2026 | epiDAMIK 2026 (workshop day) |

## Sources

- [KDD 2026 home](https://kdd2026.kdd.org/)
- [KDD 2026 Workshops list](https://kdd2026.kdd.org/workshops/)
- [KDD 2026 Research Track CFP](https://kdd2026.kdd.org/research-track-call-for-papers/)
- [KDD 2026 AI for Sciences Track CFP](https://kdd2026.kdd.org/ai4sciences-track-call-for-papers/)
- [KDD 2026 Applied Data Science Track CFP](https://kdd2026.kdd.org/applied-data-science-ads-track-call-for-papers/)
- [BIOKDD 2026](https://biokdd.org/biokdd26/)
- [epiDAMIK 2026](https://epidamik.github.io/)
- [AEGIS 2026](https://phhp.ufl.edu/aegis-2026/)
- [RelSciFM 2026](https://kdd26-relscifm.github.io/)
- [SciSoc LLM 2026](https://kdd26scisocllm.github.io/)
- [AgenticAI-Eval 2026](https://kdd-eval-workshop.github.io/agenticai-evaluation-kdd2026/)
- [AI4Mental 2026](https://chrystalii.github.io/AI4mental/)
- [RespMultimodal 2026](https://respmultimodal2026.github.io/)
- [KDD 2026 OpenReview](https://openreview.net/group?id=KDD.org/2026/Conference)

## Next step

- **Now → mid-May 2026:** monitor Cycle 2 main-track notifications (May 16) and BIOKDD notification (Jun 4). No bulk content extraction until accept lists drop.
- **Late May – Jul 2026:** scaffold likely bio / health workshop pages; run the keyword filter against the Cycle 1 + Cycle 2 accepted list to identify the ~few-dozen bio-relevant papers; cross-check author lists against ICML 2026 (Jul 6–11) bio-workshop acceptances.
- **Aug 9–13, 2026 (during the meeting):** opportunistic capture of social reactions, especially BIOKDD / epiDAMIK / AEGIS / RelSciFM orals and AI-for-Sciences track talks.
- **Post-meeting (mid-Aug 2026 onward):** populate `tools/` with the filtered subset; cross-link into AACR 2026 agentic-AI, virtual-cells, and outcomes-research axes, plus NeurIPS 2026 / ICML 2026 / AMIA 2026 cousins.
