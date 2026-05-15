# Landscape — 57 posters by agent archetype

The agentic-AI slice of AACR 2026 was harvested via a phrase-quoted keyword union over AACR Abstracts Online (`"agentic AI"`, `"AI agent"`, `"multi-agent"`, `"agent-based"`, `"agentic workflow"`, `"large language model"`). Of 102 unique union hits, 57 survived filtering on `Activity` + `PlayerUrl`. 18 of those 57 sit inside the dedicated "Agentic AI in Cancer" poster session (SessionId 241 — the AT02 satellite track, Sun 4/19); the remaining 39 are drawn from "Large Language Models in the Clinic", AACR Project GENIE AI sessions, Integrative Computational Approaches, Late-Breaking Bioinformatics, and scattered specialty tracks.

Below, the 57 are bucketed by **agent archetype** based on their titles and abstracts: (1) research copilots / co-scientists, (2) workflow automation agents, (3) multi-agent systems, (4) LLM-as-classifier / extractor, (5) multimodal / graph / knowledge-base / specialty applications, and (6) a small **Other** bucket for loose keyword hits that matched the union but do not implement an agent per se. The archetype split is title-and-abstract-level — a few posters could defensibly go in two buckets; judgment calls are noted inline.

## Research copilots / co-scientists

Agents designed to sit alongside a working researcher — take a natural-language question, plan an analysis, call tools, and return an interpreted answer. This is one of the two densest families in the corpus (10 posters). All of them are LLM-fronted chat interfaces to computational biology workflows or databases; several (DrBioRight, GP CoPilot, CHARLES) advertise explicit self-critique or reasoning traces as a reliability feature. The family clusters heavily inside the SessionId-241 "Agentic AI in Cancer" track — 7 of the 10 are presented there.

| # | Title | Presenter | Session |
|---|---|---|---|
| 16 | DrBioRight: an AI research assistant for cancer data analysis | Han Liang | Agentic AI in Cancer |
| 18 | GP CoPilot: An AI-enhanced agent for cancer research | Michael Reich | Agentic AI in Cancer |
| 19 | GenerAItive: An AI system for interpretation of gene expression analyses in cancer | Muiz Khan | Agentic AI in Cancer |
| 23 | ImmunoVerse-Chat: A conversational agentic-AI engine for next-generation immunotherapeutic target discovery | Aman Sharma | Agentic AI in Cancer |
| 24 | CertisAI Assistant: An agentic AI platform for dynamic preclinical oncology model selection | Long Do | Agentic AI in Cancer |
| 28 | PortrAIgent: Co-scientist agent for end-to-end spatial transcriptomics discovery | Yuchang Seong | Agentic AI in Cancer |
| 31 | Charles: A self-critical agentic AI drug discovery analyst for cancer | Mehdi Orouji | Agentic AI in Cancer |
| 3 | Evaluation of an agentic LLM chatbot for clinico-genomic analysis of AACR GENIE BPC data | Likhita Sree Thiriveedi | AACR Project GENIE: Predictive Models and AI |
| 5451 | Omicology: A comprehensive AI/LLM/NLP-based web resource for the ontology, phylogeny, and practical navigation of omics literature | John Weinstein | Application of Bioinformatics to Cancer Biology 5 |
| 5497 | AI-augmented immersive 3D and 4D spatial analysis interface for cancer research | Jonathan Kim | New Software Tools for Data Analysis |

## Workflow automation agents

Agents that own an end-to-end analytical pipeline — RNA-seq, spatial biology, cohort curation, pathology report abstraction, adverse-event exploration — and run it with minimal human intervention. Distinguished from the co-scientist family by being more vertically focused (one pipeline, deep) rather than conversationally open-ended (many tools, shallow). Six posters. Three of them (#20, #30, #LB450) are the clinical-text-to-structured-data cohort most directly aligned with Bitterman's AT02 worked example.

| # | Title | Presenter | Session |
|---|---|---|---|
| 20 | An agentic AI workflow for automated, high-fidelity curation of cancer diagnosis and staging from unstructured patient records | Tian Kang | Agentic AI in Cancer |
| 21 | AI analysis agent to accelerate end-to-end spatial biology analysis for MERSCOPE | Lorenz Rognoni | Agentic AI in Cancer |
| 25 | Agentic AI for RNA-Seq: From workflow automation to actionable insights | Arthur Liberzon | Agentic AI in Cancer |
| 30 | Automated cohort extraction from real-world oncology data using adaptive LLM-based agentic systems for clinical trial feasibility and patient selection | Brandon Theodorou | Agentic AI in Cancer |
| 32 | Agentic AI-enabled exploration of real-world immune-related adverse events | Gabriela Fort | Agentic AI in Cancer |
| LB450 | AI-assisted pathology report abstraction for breast cancer | Sarah Van Alsten | Late-Breaking Research: Bioinformatics |

## Multi-agent systems

Posters that explicitly compose multiple specialized agents (target-discovery agent + toxicity-prediction agent + design agent, or orchestrator + sub-agents). Seven posters. Application domains span CAR-T development, immune-checkpoint response analysis, SDOH extraction, precision-oncology ecosystems, and — uniquely — in-silico rotational-therapy scheduling. #22 (autonomous CAR-T) and #4 (multi-agent CRC precision-oncology ecosystem) are the most architecturally ambitious; the rest are narrower two-to-three-agent compositions.

| # | Title | Presenter | Session |
|---|---|---|---|
| 22 | Multi-agent AI system for autonomous CAR-T development: Integrated target discovery, toxicity prediction, and rational molecular design for cancer immunotherapy | Yi Ni | Agentic AI in Cancer |
| 26 | Multi-agent AI orchestration for temporal-aware extraction of social determinants of health from unstructured clinical records in cancer populations | Asim Waqas | Agentic AI in Cancer |
| 4 | A multi-agent conversational artificial intelligence ecosystem for real-time integration of clinical, genomic, and social determinants of health data in colorectal cancer precision oncology | Enrique Velazquez-Villarreal | AACR Project GENIE: Predictive Models and AI |
| 2444 | Multi-agent-augmented analysis of PD-1 checkpoint inhibitor response | ADA SHAW | Biomarkers Predictive of Therapeutic Benefit 3 |
| 6832 | Toward personalized rotational multi-agent therapies to overcome treatment resistance in pancreatic cancer: A virtual trial framework in mice | Krithik Vishwanath | Mathematical Modeling and Statistical Methods |
| 29 | Reasoning-guided retrieval improves oncology trial eligibility matching from clinical notes | Patrycja Krawczuk | Agentic AI in Cancer |
| 1393 | Design of a prospective implementation study to evaluate the efficacy of an AI-assisted workflow intervention to increase breast cancer clinical trial participation | Jacob Rosenthal | Regulatory Science and Policy |

*Note: #29 and #1393 use multi-step retrieval / orchestration patterns that meet the multi-agent criterion even without the phrase "multi-agent" in the title. #6832 ("multi-agent therapies") is a border case — the "multi-agent" refers to multi-drug regimens rather than multi-LLM-agent systems, but the framework itself is a virtual-trial agent that schedules them, so it is listed here.*

## LLM-as-classifier / extractor

The largest single archetype by count (16 posters) — LLMs used not as agents but as classification, extraction, or triage engines on clinical text. Dominated by the "Large Language Models in the Clinic" session (13 of the 16). Most of these are not agentic in Bitterman's sense (no multi-step planning, no tool calls), but they share the LLM substrate and were pulled in by the keyword harvest. Included for completeness and because the boundary between "structured extraction pipeline" and "one-shot agent" is fuzzy in practice.

| # | Title | Presenter | Session |
|---|---|---|---|
| 2738 | From chaos to columns: High-accuracy clinical data extraction with CIDER | Balazs Gyorffy | Large Language Models in the Clinic |
| 2739 | Evaluation of large language models for automated clinical trial matching in oncology | Aakash Desai | Large Language Models in the Clinic |
| 2740 | Applications of large language models to CAR-T cell therapy clinical data using Google cloud computing | Emmanuel Contreras Guzman | Large Language Models in the Clinic |
| 2741 | Large language model-based triage of Hematology/Oncology patient messages: Performance, safety, and clinical implications | Dinh Nguyen | Large Language Models in the Clinic |
| 2744 | Automating clinical and pathological staging for breast cancer patients | Arshad Mohammed | Large Language Models in the Clinic |
| 2747 | Source discipline matters: Guideline anchored large language model outperforms Open Evidence for decision support in acute leukemias | Peter Palumbo | Large Language Models in the Clinic |
| 2750 | Rapid curation of colon cancer cohorts using on-site peta-scale language model for MSI classification from pathology reports | Joshua Levy | Large Language Models in the Clinic |
| 2751 | Large language model-derived molecular patient similarity from real-world MTB data | Sophie Lugani | Large Language Models in the Clinic |
| 2753 | Ontology-guided hierarchical cell typing with large language models for analyzing tumor microenvironment | Yuchang Seong | Large Language Models in the Clinic |
| 2755 | Large scale extraction of adverse events by large language models uncovers latent structure of treatment toxicity | John Lazar | Large Language Models in the Clinic |
| 2761 | Large language model-derived re-contextualization reveals functional landscapes across cancers | Yibing Guo | Large Language Models in the Clinic |
| 2762 | LLM-based extraction of immunotherapy toxicities reveals severity-dependent effects on overall survival | Zeyun Lu | Large Language Models in the Clinic |
| 2763 | Leveraging large language models to classify pathology reports into ontological hierarchies | Brenda Fried | Large Language Models in the Clinic |
| 4100 | Large language models for tumor genomic interpretation | Jennifer Yu | AACR Project GENIE: Genomic Characterization |
| LB169 | scCAP: An ontology-aware large language model framework for hierarchical and standardized single-cell type annotation | Seok-Won Jang | Late-Breaking Research: Bioinformatics |
| 2337 | Mapping the associations of 144 incidence risk factors with 39 cancers: An AI-driven systematic review and meta-analysis | Shiyuan Tong | Epidemiology: Cancer Incidence, Mortality, Patterns |

## Multimodal / graph / knowledge-base / specialty applications

Posters that embed an LLM or agent inside a broader multimodal or knowledge-graph architecture, or apply agentic / LLM methods to niche specialty problems (variant interpretation, epitope mining, metabolic KB construction, patient-perception surveys). Nine posters.

| # | Title | Presenter | Session |
|---|---|---|---|
| 33 | A healthcare system scale multimodal whole patient temporal foundation model | Andrew Zhang | Agentic AI in Cancer |
| 2754 | VGL: Vision-Gene-Language multimodal LLM integrating histopathology and gene expression for cell type classification in lung cancer | Haenara Shin | Large Language Models in the Clinic |
| 4195 | OncoGraphDB: Rapid projections of patient-level multimodal graph database facilitates efficient exploration of tumor subtypes and identifies new combinatorial biomarkers of patient outcomes and gene essentiality | Jacob Pfeil | Integrative Computational Approaches 2 |
| 4213 | Generative genomics accurately predicts cancer gene expression | Alexander Abbas | Machine Learning Approaches for Cancer Prediction |
| 5465 | Improving early cancer detection by training scalable deep neural networks to extract tumor signal from cell-free DNA | Jackson Killian | Deep Learning in Cancer |
| 5521 | MeDOC-KB: Knowledge base for unraveling the metabolic links between obesity-related cancers | Madhan Subramanian | New Software Tools for Data Analysis |
| 6272 | Enhancing variant interpretation through multi-database and systematic variant classification: Reducing uncertainty in clinical genomics | Gowhar Shafi | Genetic Epidemiology 2 |
| 6698 | EpitopeMiner: Scalable knowledge mining for evidence-driven personalized cancer vaccine design | Mai Chan Lau | Vaccines and Other Immunomodulatory Agents |
| 1486 | From animals to computational oncology: Digital twins as ethical enablers of next-generation bone metastasis research | Eleonora Dondossola | Integrative Computational Approaches 1 |

## Other (loose harvest hits — human-factors, wet-lab, unrelated DL)

Posters that matched the keyword union but do not implement an agent, LLM classifier, or agentic workflow. Kept for completeness; several are valuable human-factors / policy / wet-lab papers adjacent to agentic AI (patient-perception surveys, AI-assisted trial-accrual implementation), and a couple (#455, #5677, #4940, #1551, #CT090, #2687, #42) are wet-lab or classical-modeling papers that hit a keyword string incidentally and should probably have been filtered out at harvest.

| # | Title | Presenter | Session |
|---|---|---|---|
| 34 | Attitudes and perception of artificial intelligence in healthcare: A cross-sectional survey among Arkansas-Louisiana-Texas veterans with cancer | Philip Haddad | Agentic AI in Cancer |
| 35 | Humans cannot live by artificial intelligence (AI) alone | Kim Blenman | Agentic AI in Cancer |
| 455 | MC001: A novel chemoimmunotherapy antibody drug conjugate for treating folate receptor alpha expressing pancreatic cancer | Seah Lim | Novel Therapeutics and Drug Targets 1 |
| 1551 | Intratumoral biodegradable nanofluidic platform for localized multimodal immunotherapy enhances tumor eradication and immune memory | Jingyi Wang | Combination Immunotherapies |
| CT090 | Pilot study of an implantable microdevice for in situ evaluation of drug response in patients with pancreatic cancer | Oliver Standring | Phase I Clinical Trials in Progress |
| 5677 | GPX4-FTH1-ARNT signaling regulates iron efflux to suppress ferroptotic cell death and promote immune remodeling in osteosarcoma | Md Abdullah | Cell Death Pathways and Treatment |
| 4940 | A hybrid mathematical model: Emergent CAF structures and their impact on cancer progression | Junho Lee | Novel Experimental Platforms and Causal Inference |
| 2687 | First single slide spatially resolved multiomic integration of pancreatic cancer: High-plex proteomic and whole transcriptome analysis | Mari-Claire McGuigan | Application of Bioinformatics to Cancer Biology 3 |
| 42 | Engineering antigen-dependent stability in nanobodies: A bioinformatics tool for tuning intracellular nanobody stability | Alvin Fu | Application of Bioinformatics to Cancer Biology 1 |

## Tally

- Research copilots / co-scientists: **10**
- Workflow automation agents: **6**
- Multi-agent systems: **7**
- LLM-as-classifier / extractor: **16**
- Multimodal / graph / KB / specialty: **9**
- Other / loose harvest hits: **9**

Total: **57**.

Keyword families most represented in titles: "large language model" / "LLM" (21 posters), "agentic" (9), "multi-agent" (5), "AI agent" / "agent" stand-alone (4), "co-scientist" / "copilot" / "assistant" (5). The phrase "agentic AI" appears in the title of **7** posters — all but one of them inside the SessionId-241 "Agentic AI in Cancer" track.

## Notes on the bucketing

- **Copilot vs workflow-automation boundary.** Both families call tools from an LLM; the split is on breadth. Copilots (#16 DrBioRight, #18 GP CoPilot, #19 GenerAItive, #31 CHARLES) expose an open-ended chat surface and a broad tool menu. Workflow automation (#20 Kang, #21 Rognoni, #25 Liberzon, #32 Fort, #30 Theodorou, #LB450 Van Alsten) is vertical and closed — one pipeline, end-to-end, minimal dialogue. This distinction matches the Bitterman/Foersch framing from AT02 and is worth preserving even though the literal "agentic AI" keyword doesn't privilege one over the other.
- **Multi-agent vs copilot boundary.** A copilot that internally calls sub-tools is not counted as multi-agent; multi-agent requires *multiple reasoning agents* with distinct roles composed together. #22 (CAR-T), #4 (CRC ecosystem), #26 (SDOH), and #2444 (PD-1 response) pass that bar explicitly.
- **LLM-as-classifier bucket is not agentic in the strict sense.** It is kept in the landscape because the keyword harvest pulled it in, and the 13-poster "Large Language Models in the Clinic" session was structurally adjacent to the Agentic AI in Cancer track; excluding it would misrepresent what was on the AACR 2026 floor under the LLM-in-oncology banner.
- **Naming coincidences.** **Yuchang Seong** presents twice (#28 PortrAIgent, #2753 ontology-guided hierarchical cell typing), and **Haenara Shin** presents #2754 here as well as additional posters in the virtual-cells corpus. Spatial-transcriptomics copilots surface in three different buckets (#28, #21, #2753) — a genuine community focus rather than a classification ambiguity.
- **Two border-case placements worth noting.** #6832 (Vishwanath, "personalized rotational multi-agent therapies") uses "multi-agent" in the drug-combination sense, not the LLM-agent sense — placed in Multi-agent systems because the virtual-trial wrapper itself is an agentic scheduler. #1486 (Dondossola, digital twins for bone metastasis) is included in the specialty bucket because the abstract frames digital twins as the ethical / governance layer for agentic-AI-driven in-silico research — but it is not itself an agent.

## Overlap with other topic slices

This corpus has non-trivial overlap with the other three AACR-2026 knowledge-base topics:

- **Virtual cells (48 posters).** Shared posters include #33 (whole-patient temporal FM), #2754 (VGL multimodal LLM), #4213 (GEM-1 generative genomics), #LB169 (scCAP), #1486 (digital twins), and #30 (Theodorou cohort-extraction agent, listed there as the only "agentic systems" representative). The agentic-AI slice captures the agent-layer view of roughly 6 posters that the virtual-cells slice captures at the model layer.
- **Single-cell / spatial omics.** #2753 (ontology-guided hierarchical cell typing), #LB169 (scCAP), #21 (MERSCOPE agent), and #2687 (single-slide spatial multiomic) overlap, reflecting the spatial-transcriptomics / cell-type-annotation frontier.
- **Bioinformatics tools.** #5451 (Omicology), #5521 (MeDOC-KB), #5497 (3D / 4D spatial interface), and the LLM-pathology-curation cluster all overlap — the bioinfo-tools view treats them as software, the agentic-AI view treats them as reasoning agents over that software.

Dedup key is `Id` in the JSONL. A poster appearing in multiple topic folders is file-duplicated (not symlinked) per `docs/notes/caveats.md`.
