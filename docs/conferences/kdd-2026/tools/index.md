# KDD 2026 — Tools / Methods (filtered)

> **Status:** Template stub. Meeting is ~3 months out (Aug 9–13, 2026, Jeju). Cycle 2 main-track notifications drop May 16, 2026 (this week); BIOKDD notifications June 4, 2026; other workshop accepted-paper lists land May–Jul. No entries are populated yet — this page exists to lock the per-tool format and the **scope filter** before extraction begins.

## Scope filter (load-bearing — this is a light build)

KDD 2026 accepts ~700 main-track papers across Cycle 1 + Cycle 2 + ~hundreds more across workshops. We do **not** extract them all. An entry lands in this directory **only if** it satisfies one of:

1. **Workshop filter** — appears in one of the bio / health / clinical / agentic-AI-with-science workshops at KDD 2026:
   - **BIOKDD 2026** — Data Mining in Bioinformatics (2026 theme: Digital Twins; disease trajectories, cell-cell comm, treatment-response prediction)
   - **epiDAMIK 2026** — Data-driven Decision Making for Public and Population Health
   - **AEGIS 2026** — Adaptation and Evidence-grounding of Generative Interventional Systems (clinical decision-support FMs)
   - **RelSciFM 2026** — Reliable Scientific Foundation Models (bio/chem subset only; skip generic FM theory)
   - **SciSoc LLM 2026** — Agentic AI for Scientific and Societal Advances (science-agent subset only)
   - **AgenticAI-Eval 2026** — Evaluation and Trustworthiness of Agentic AI (healthcare-deployment subset)
   - **AI4Mental 2026** — AI for Cognitive and Mental Health Support
   - **RespMultimodal 2026** — Responsible Multimodal Foundation Models (medical-imaging / clinical-multimodal subset)
   - **EntAIAgents 2026** — Enterprise AI Agents (pharma/biotech-deployment subset only)
2. **AI for Sciences track filter** — every accepted paper in the biomedical / health subset of KDD 2026's inaugural AI for Sciences track. The track's biomedical scope is explicit: "health sciences, healthcare, bioinformatics, epidemiology, pharmaceuticals, systems biology, multiomics, neuroscience."
3. **Research-Track / ADS keyword filter** — title or abstract contains any of: *cancer, oncology, tumor, genomics, single-cell, scRNA, spatial transcriptomics, perturbation, CRISPR, drug discovery, drug repurposing, molecular property, protein, foundation model for biology, electronic health record, EHR, claims, clinical NLP, pathology, histology, radiology, virtual cell, digital twin, healthcare graph, biomedical knowledge graph, multi-omics, pharmacogenomics, survival, longitudinal cohort, mortality prediction, ICU*.
4. **Agentic-AI / LLM-for-science filter** — main-track or workshop paper on LLM agents, tool-use, scientific-reasoning benchmarks, evidence-grounded clinical decision systems, or autonomous experimentation, regardless of explicit bio framing. These reliably adapt to oncology within 6 months and feed the AACR agentic-AI axis.

Everything else — recommender systems, e-commerce, advertising, urban computing, finance, talent computing, fraud / integrity without a healthcare hook, generic time-series, generic federated learning — is **out of scope** and gets no entry here. Reviewer bandwidth is the binding constraint, not source availability.

## Per-entry template

Each in-scope paper gets a file (`tools/<paper-slug>.md`) following this structure:

````markdown
# <Method / Tool name>

**One-line description** — what the method does in plain language.

- **Authors:** <first author + lab + institution>
- **Track:** Research / ADS / AI4Sciences / BIOKDD / epiDAMIK / AEGIS / RelSciFM / SciSoc LLM / AgenticAI-Eval / AI4Mental / RespMultimodal / EntAIAgents
- **Cycle (if main-track):** Cycle 1 (Aug 2025 submission) / Cycle 2 (Feb 2026 submission)
- **OpenReview:** [paper page]
- **ACM DL / proceedings:** [final paper link, once camera-ready posts]
- **arXiv / bioRxiv / medRxiv:** [preprint link]
- **Code:** [GitHub link]
- **Pretrained weights / data:** [HF Hub / Zenodo / PhysioNet link if applicable]

## Presentation at KDD 2026

- **Format:** oral / poster / workshop talk / KDD Cup demo
- **Day / session:** Aug 9–13 (workshops bookend main conference)
- **Recording:** [YouTube / KDD virtual platform link, post-meeting]

## What it does

2–3 sentences: the problem it solves, the methodological idea, what it consumes and produces.

## Why it matters for cancer / biology

Explicit statement of the bridge to oncology — even for main-track papers that don't claim cancer relevance. Example: "Heterogeneous-graph EHR mining for adverse-event prediction; directly applicable to immune-related adverse event (irAE) cohorts in checkpoint-inhibitor oncology." Or: "Digital-twin framework for disease-trajectory simulation; BIOKDD theme paper, plausibly adaptable to tumor-evolution / therapy-response modeling."

## Where it fits in the corpus

- AACR 2026 agentic-AI axis: [link if relevant]
- AACR 2026 virtual-cells / digital-twin axis: [link if relevant]
- AACR 2026 outcomes-research / clinico-genomics axis: [link if EHR / claims / longitudinal]
- **NeurIPS 2026 cousin paper / author overlap:** [link — KDD agentic-AI ↔ NeurIPS rule]
- **ICML 2026 cousin paper / author overlap:** [link — KDD bio ↔ ICML FM4LS / GenBio rule]
- **AMIA 2026 cousin paper:** [link — KDD EHR cluster ↔ AMIA rule]
- ISMB 2026: [link if benchmarked / cited]
- ASCO 2026: [link if clinically translated]

## Notes

Free-form: benchmarks claimed, comparisons to scGPT / Geneformer / clinical-LM baselines (Clinical-T5, Med-PaLM, BioGPT, GatorTron) / drug-discovery baselines (MoLFormer, Uni-Mol, MolE), graph-mining comparisons (GraphSAGE / GAT / GIN), agentic-AI capabilities, regulatory implications, EHR-cohort sizes, validation cohorts (MIMIC, eICU, UK Biobank, All of Us, OneFlorida).
````

## Tool index

*Empty — populates from late May 2026 (Cycle 2 notifications) onward, with the BIOKDD batch landing post-Jun 4. Anticipated final count: ~25–40 entries — smaller than NeurIPS 2026 but larger than ICML 2026 in the EHR / clinical-NLP segment because KDD's applied-research orientation surfaces more of that work than the ML venues. The agentic-AI subset is unusually heavy at KDD 2026 (six workshops with agentic-AI hooks) so that bucket may dominate.*

| Method / Tool | Track | Modality | Authors | Format | OpenReview | Code | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|

## Why this format

- **Track field** — KDD 2026 has 5 main-track sub-tracks (Research, ADS, Datasets & Benchmarks, **AI for Sciences (new)**, Blue Sky) plus 30 workshops; disambiguating where a result lived is essential for downstream attribution.
- **Cycle field** — KDD's two-cycle submission system means Cycle 1 papers (Nov 2025 notifications) and Cycle 2 papers (May 2026 notifications) have different preprint vintages; the field flags which deadline shaped the work.
- **"Why it matters for cancer / biology" is mandatory** — most KDD work is not explicitly oncology, but the only reason it's in this vault is the cancer downstream. Forcing this field keeps the filter honest. KDD's tilt toward EHR / claims / cohort work means many entries will phrase the bridge as a "clinical-NLP pipeline applicable to oncology cohorts" rather than "method for tumor biology."
- **Multiple cousin fields (NeurIPS / ICML / AMIA)** — KDD straddles the ML-venue community and the clinical-informatics community; both cross-links are load-bearing. Tracking the overlap prevents duplicated tool entries.
- **EHR cohort row in Notes** — clinical-NLP / EHR-mining papers at KDD frequently train on MIMIC / eICU / UK Biobank / All of Us / OneFlorida; tracking which cohort grounded a method is the difference between an academic toy and a usable clinical tool.
- **Cross-vault links to AACR axes** — the load-bearing purpose: a KDD August result on, e.g., heterogeneous-graph EHR mining for adverse-event prediction should be one click from the AACR April session where it gets demonstrated on a checkpoint-inhibitor irAE cohort (the following spring).

## Open questions

1. **AI for Sciences track is inaugural** — granularity unclear; the track may pull most of the bio work out of Research, in which case Research-Track keyword filter hits should be near-zero. *Tentative: treat AI4Sciences as the primary main-track filter target; spot-check Research / ADS for stragglers.*
2. **BIOKDD digital-twin theme overlap with AACR virtual-cells axis** — many BIOKDD 2026 papers will plausibly cross-list with the AACR virtual-cells axis; should those be dual-entered? *Tentative: single entry under KDD with explicit AACR axis cross-link.*
3. **Six agentic-AI workshops** — RelSciFM, SciSoc LLM, AgenticAI-Eval, EntAIAgents, AEGIS, AI4Mental all have agentic-AI hooks; do all six get filtered coverage or just the most bio-adjacent? *Tentative: filter all six on the keyword filter + agentic-AI-for-science filter; expect ~5–10 hits per workshop.*
4. **Consolidating KDD + NeurIPS + ICML cousin papers** — when the same lab ships an evolved version across the three meetings, one entry or three? *Tentative: three entries (one per venue), with explicit version / delta notes; the 6-month evolution arc through Jul/Aug/Dec is informative.*
5. **AMIA 2026 cross-link mechanics** — AMIA Annual Symposium is November; KDD EHR papers often replay there. Should the AMIA cousin field be required for EHR papers? *Tentative: required for EHR / clinical-NLP papers, optional otherwise.*
