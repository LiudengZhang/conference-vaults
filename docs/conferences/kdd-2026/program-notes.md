# KDD 2026 — Program Notes (pre-meeting prep)

> Internal working file. Today is **May 11, 2026** — the meeting is ~3 months out (Aug 9–13, 2026, Jeju). Cycle 2 main-track notifications are due May 16, 2026 (this week); BIOKDD 2026 submissions close May 14, 2026 (extended) with notifications June 4; other workshop accepts roll through May–July. **Partial accepted-paper data exists** (Cycle 1 notifications dropped Nov 23, 2025) but the BIOKDD / Cycle-2 bulk is still ahead. This file holds the scaffolding so we can move fast once the remaining lists drop.

## Verified facts

| Field | Value | Source |
|---|---|---|
| Conference | 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining | kdd2026.kdd.org |
| City | Jeju, South Korea | kdd2026.kdd.org |
| Venue | International Convention Center Jeju (ICC Jeju) | kdd2026.kdd.org |
| Main conference | Aug 9–13, 2026 | kdd2026.kdd.org |
| Submission cycles | 2 cycles per year | Research Track CFP |
| Cycle 1 abstract deadline | Jul 24, 2025 — past | Research Track CFP |
| Cycle 1 paper deadline | Jul 31, 2025 — past | Research Track CFP |
| Cycle 1 rebuttal | Oct 4–18, 2025 — past | Research Track CFP |
| Cycle 1 notifications | Nov 23, 2025 — past | Research Track CFP |
| Cycle 2 abstract deadline | Feb 1, 2026 — past | Research Track CFP |
| Cycle 2 paper deadline | Feb 8, 2026 — past | Research Track CFP |
| Cycle 2 rebuttal | Apr 4–17, 2026 — past | Research Track CFP |
| Cycle 2 notifications | **May 16, 2026** — this week | Research Track CFP |
| BIOKDD 2026 submission | May 14, 2026 (extended) — this week | biokdd.org/biokdd26/ |
| BIOKDD 2026 notification | Jun 4, 2026 | biokdd.org/biokdd26/ |
| epiDAMIK 2026 workshop day | Aug 9 or 10, 2026 | epidamik.github.io |
| Tracks | Research / Applied Data Science (ADS) / Datasets & Benchmarks / **AI for Sciences (inaugural)** / Blue Sky | kdd2026.kdd.org |
| Paper format | 8 pages full + 2-page extended abstract option (ADS / AI4Sciences) | AI4Sciences CFP |
| Required section | "Limitations and Ethical Considerations" mandatory in all submissions | AI4Sciences CFP |
| Proceedings | ACM Digital Library | kdd2026.kdd.org |

## Sources we will rely on

| Source | When usable | Coverage |
|---|---|---|
| [KDD 2026 home](https://kdd2026.kdd.org/) | now | dates, venue, tracks, registration |
| [KDD 2026 Workshops list](https://kdd2026.kdd.org/workshops/) | now | full 30-workshop roster |
| [Research Track CFP](https://kdd2026.kdd.org/research-track-call-for-papers/) | now | submission rules, two-cycle timeline |
| [AI for Sciences Track CFP](https://kdd2026.kdd.org/ai4sciences-track-call-for-papers/) | now | biomedical scope, AI4Sciences rules |
| [ADS Track CFP](https://kdd2026.kdd.org/applied-data-science-ads-track-call-for-papers/) | now | applied-research rules |
| [OpenReview KDD 2026](https://openreview.net/group?id=KDD.org/2026/Conference) | rolling | accept lists by cycle |
| [BIOKDD 2026](https://biokdd.org/biokdd26/) | now | bio workshop scope, digital-twin theme |
| [epiDAMIK 2026](https://epidamik.github.io/) | now | public health workshop scope |
| [AEGIS 2026](https://phhp.ufl.edu/aegis-2026/) | now | evidence-grounded interventional FMs |
| [RelSciFM 2026](https://kdd26-relscifm.github.io/) | now | reliable scientific FM workshop |
| [SciSoc LLM 2026](https://kdd26scisocllm.github.io/) | now | agentic AI for science workshop |
| [AgenticAI-Eval 2026](https://kdd-eval-workshop.github.io/agenticai-evaluation-kdd2026/) | now | agentic-AI evaluation workshop |
| [AI4Mental 2026](https://chrystalii.github.io/AI4mental/) | now | mental health AI workshop |
| [RespMultimodal 2026](https://respmultimodal2026.github.io/) | now | responsible multimodal FMs |
| ACM Digital Library | from ~Aug 2026 | camera-ready, citeable |
| KDD YouTube channel + virtual platform | from ~Aug 15 onward | recorded keynotes + ADS orals + workshop talks |
| bioRxiv / medRxiv / arXiv | continuous | preprints, filterable by "accepted at KDD 2026" / "to appear at KDD 2026" |
| `#KDD2026` on Bluesky / X / Mastodon | Aug 9–13 | real-time talk reactions |
| AMIA 2026 (Nov 2026) | post-meeting | KDD EHR papers often replay at AMIA |
| Lab blogs (Google Health, Microsoft Research Health Futures, Insitro, Nference, Flatiron Health, Tempus, Recursion, Owkin, Komodo Health) | rolling | preprints + KDD paper summaries |

## Filter criteria (locked — mirrors `tools/index.md`)

A paper enters this vault only if it matches **one** of four filters. Reproduced here for the pre-meeting screening pass.

### Filter 1 — workshop track

Accept anything in these workshops (canonical short names; 2026 roster is finalized):

- **BIOKDD 2026** — Data Mining in Bioinformatics (2026 theme: Digital Twins)
- **epiDAMIK 2026** — Public and Population Health
- **AEGIS 2026** — Evidence-grounding of Generative Interventional Systems
- **RelSciFM 2026** — Reliable Scientific Foundation Models (bio/chem subset only)
- **SciSoc LLM 2026** — Agentic AI for Scientific and Societal Advances (science-agent subset)
- **AgenticAI-Eval 2026** — Evaluation and Trustworthiness of Agentic AI (healthcare subset)
- **AI4Mental 2026** — AI for Cognitive and Mental Health Support
- **RespMultimodal 2026** — Responsible Multimodal Foundation Models (medical / clinical subset)
- **EntAIAgents 2026** — Enterprise AI Agents (pharma / biotech deployment subset only)

### Filter 2 — AI for Sciences track

Accept **all** AI4Sciences track papers whose stated domain is biomedical: health sciences, healthcare, bioinformatics, epidemiology, pharmaceuticals, systems biology, multiomics, neuroscience. This is KDD 2026's cleanest filter target.

### Filter 3 — Research / ADS keyword filter

Run this regex over titles + abstracts on the Cycle 1 + Cycle 2 accept list:

```
(cancer|oncolog|tumor|metasta|carcinom|melanoma|leukemi|lymphoma)
| (genomic|epigenom|transcriptom|proteom|metabolom|methyl|pharmacogen)
| (single[- ]cell|scRNA|scATAC|spatial transcriptom|spatial omic|multi[- ]?omic)
| (perturbation|CRISPR|knockout|knockdown|sgRNA)
| (drug discover|drug repurpos|target ident|molecular property|ADMET|small molecul|biologic|de novo design)
| (protein structur|protein function|protein language)
| (foundation model.*(biolog|cell|genom|tissue|pathol|clinical|medical|EHR))
| (electronic health record|EHR|claims data|clinical NLP|medical imaging|pathology|histolog|radiolog|diagnos|ICU|mortality|survival|adverse event|hospital readmission)
| (longitudinal cohort|biobank|MIMIC|eICU|UK Biobank|All of Us|OneFlorida|trial match)
| (virtual cell|digital twin|disease trajectory|cell.cell commun)
| (biomedical knowledge graph|healthcare graph|drug.drug interaction|drug.target)
```

### Filter 4 — agentic-AI / LLM-for-science subset

Independent of bio framing, accept any main-track or workshop paper on:

- LLM agents with tool-use, code-execution, or experiment-design loops
- Scientific-reasoning benchmarks (SWE-bench-class, sci-agent-class, lab-task benchmarks)
- Evidence-grounded clinical decision systems (AEGIS-class)
- Autonomous research / hypothesis-generation systems
- Multi-agent scientific workflows
- Agentic-AI evaluation, safety, trustworthiness frameworks (with healthcare-deployment relevance)

Rationale: these adapt to oncology within ~6 months (the empirical pattern from 2024 → AACR 2025 and 2025 → AACR 2026) and feed the AACR agentic-AI axis directly. KDD 2026's slate has six agentic-AI workshops (RelSciFM, SciSoc LLM, AgenticAI-Eval, AEGIS, AI4Mental, EntAIAgents) which is unusually heavy and signals where the community is converging.

## Expected paper themes (5 anchors)

Pre-meeting predictions, to be reconciled against the actual list in late May / June / early August. These are the buckets we expect `tools/` entries to cluster into.

### Theme 1 — EHR mining, clinical NLP, and longitudinal-cohort ML

KDD's historical strength. Expect heterogeneous-graph models over EHR, claims, and biobank data; longitudinal-trajectory LMs over multi-year clinical records; mortality / adverse-event / readmission / survival prediction with explicit oncology cohort framing; trial-matching and synthetic-control methods. Workshop home: **epiDAMIK** + Research / ADS spillover. Expect heavy overlap with AMIA Annual Symposium (Nov 2026) and ML4H @ NeurIPS (Dec 2026). The cancer hook: most of these methods get demonstrated first on MIMIC / eICU / UK Biobank generic populations, then translated to checkpoint-inhibitor / CAR-T / TKI-toxicity cohorts within 6–18 months.

### Theme 2 — Digital-twin biology (BIOKDD 2026 theme)

BIOKDD 2026's announced theme: disease-trajectory simulation, microenvironmental interactions, cell-cell communication, post-treatment outcome prediction. This is the closest KDD has come to AACR's virtual-cells axis. Expect heterogeneous-graph models over tumor / microenvironment / clinical state; mechanistic-ML hybrids; treatment-response simulators; cell-cell communication GNNs. Workshop home: **BIOKDD**. Cross-link to AACR 2026 virtual-cells axis and to ICML 2026 FM4LS / GenBio.

### Theme 3 — Agentic AI for science and clinical decisions

Tool-use LLMs that drive bioinformatics pipelines, design wet-lab experiments, navigate clinical decision trees, or evaluate other agents. 2025 surfaced ChemCrow / Coscientist-class systems; 2026 should bring oncology-tumor-board agents, trial-matching agents, multi-omics interpretation agents, and evidence-grounded clinical decision systems. Workshop home: distributed across **AEGIS, SciSoc LLM, AgenticAI-Eval, RelSciFM, EntAIAgents** — KDD 2026's six-workshop agentic-AI footprint is the heaviest of any 2026 conference in this vault. Cross-link to NeurIPS 2026, ICML 2026, and AACR 2026 agentic-AI axis.

### Theme 4 — Multi-omics ML and pharmacogenomics

Multi-omics fusion (DNA + RNA + protein + clinical) for drug-response / drug-repurposing / target-identification; graph-based drug-target / drug-drug-interaction prediction; pharmacogenomic-cohort ML; perturbation-response prediction on cancer cell lines. Workshop home: **BIOKDD** + AI4Sciences track. Cross-link to ISMB 2026 / ICML 2026 FM4LS; this is where KDD's data-mining strength on heterogeneous-graph structures meets oncology drug discovery.

### Theme 5 — Public-health, population-health, and trustworthy clinical AI

epiDAMIK's recurring scope plus the 2026 trustworthiness emphasis from AEGIS, AgenticAI-Eval, RespMultimodal. Expect: disease-surveillance models, health-disparity audits, fairness in clinical-decision support, evaluation frameworks for clinical agentic systems, evidence-grounding methods for generative interventional systems. Workshop home: **epiDAMIK + AEGIS + AgenticAI-Eval + RespMultimodal**. The oncology bridge: cancer-care disparities, trial-enrollment equity, validation of LLM-generated clinical recommendations against guideline-grounded evidence. Cross-link to AACR Disparities axis and the AACR Annual Meeting public-health sessions.

## Pre-meeting timeline (action items)

| Date | Action |
|---|---|
| Now → May 14, 2026 | passive monitoring; verify BIOKDD submission deadline lands as expected |
| **May 14, 2026** | BIOKDD submission deadline (extended) |
| **May 16, 2026** | Cycle 2 main-track notifications — run keyword regex against accept list, identify candidate papers; cross-check against Cycle 1 already-known accepts |
| Late May 2026 | OpenReview Cycle 2 accept list publishes — build candidate paper list; cross-check authors against ICML 2026 (Jul 6–11) workshop expected roster |
| **Jun 4, 2026** | BIOKDD 2026 notifications — extract bio-relevant paper list |
| Jun–Jul 2026 | other workshop accept lists drop on a rolling basis (epiDAMIK, AEGIS, RelSciFM, SciSoc LLM, AgenticAI-Eval, AI4Mental, RespMultimodal) — extend candidate list |
| Jul 2026 | scaffold likely `tools/` pages from titles + bioRxiv / medRxiv mirrors |
| Late Jul 2026 | cross-check ICML 2026 (Jul 6–11) bio-workshop accepts for KDD-ICML author overlap; consolidate cousin-paper cross-links |
| **Aug 9–13, 2026** | meeting week — opportunistic real-time capture from social, especially BIOKDD digital-twin orals, AEGIS evidence-grounding orals, AI4Sciences track keynotes |
| Mid-Aug → Sep 2026 | bulk `tools/` population from KDD virtual platform recordings + ACM DL camera-ready papers; tag NeurIPS 2026 candidate cousin papers |
| Nov 2026 | revisit for AMIA Annual Symposium cross-links on EHR cluster |

## Caveats

- **Partial accept data — Cycle 2 dominates.** Cycle 1 accept list has been public since Nov 2025 but represents only ~30–40% of main-track volume historically. Cycle 2 lands May 16, 2026 with the bulk. Filter screening should run twice: once now on Cycle 1, again post-May-16 on Cycle 2.
- **AI for Sciences track is inaugural.** Volume unknown. May pull most bio work out of Research / ADS, in which case the keyword filter on Research / ADS yields near-zero. May also be small and selective, in which case Research / ADS still hold most bio work. Plan for both contingencies.
- **BIOKDD is the anchor bio workshop.** 25th edition, IEEE/ACM TCBB special issue downstream, established author community. The digital-twin theme is the freshest 2026 angle and aligns directly with AACR virtual-cells. Prioritize BIOKDD coverage.
- **Six-workshop agentic-AI footprint risks scope creep.** Filter 4 is broad by design but can swell across six workshops. Keep the "science / clinical / tool-use benchmark required" caveat enforced; pure dialog-agent or pure red-teaming work without a healthcare hook is out.
- **KDD ↔ NeurIPS ↔ ICML ↔ AMIA author overlap.** Tool-entry consolidation policy is in `tools/index.md` open question 4. Default to separate entries per venue with explicit version / delta notes; the 6-month Jul → Aug → Nov → Dec arc through ICML → KDD → AMIA → NeurIPS is informative.
- **Jeju-venue logistics.** ICC Jeju is on Jeju Island, more remote than Seoul (ICML 2026). Limited Western-press coverage expected; social-media reactions will be the primary real-time signal. KST time-zone offset matches ICML 2026.
- **KDD Cup challenges noted but out of scope.** The Tencent UNI-REC Challenge and HKUST Data Agents Challenge are listed; neither has explicit oncology framing. Skip unless a healthcare-relevant challenge surfaces post-May.
