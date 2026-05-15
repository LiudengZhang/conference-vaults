# NeurIPS 2026 — Program Notes (pre-meeting prep)

> Internal working file. Today is **May 11, 2026** — the meeting is ~7 months out. Main paper notifications go Sep 24; workshop accept/reject Sep 29; accepted-paper lists post on OpenReview Oct–Nov. **No accepted-paper data exists yet.** This file holds the scaffolding so we can move fast once the lists drop.

## Verified facts

| Field | Value | Source |
|---|---|---|
| Conference | 40th Conference on Neural Information Processing Systems | neurips.cc |
| Model | three-city satellite (first time at three hubs) | neurips.cc |
| Sydney dates | Dec 6–12, 2026 | neurips.cc/Conferences/2026 |
| Atlanta dates | Dec 9–13, 2026 | neurips.cc/Conferences/2026 |
| Paris dates | Dec 9–13, 2026 | neurips.cc/Conferences/2026 |
| Paper submission deadline | May 6, 2026 (AoE) — past | neurips.cc |
| Workshop application deadline | Jun 6, 2026 (AoE) | CallForWorkshops |
| Workshop accept notifications | Jul 11, 2026 (AoE) | CallForWorkshops |
| Paper author notifications | Sep 24, 2026 | neurips.cc |
| Workshop final-decision deadline | Sep 29, 2026 | CallForWorkshops |
| Workshop suggested-contribution deadline | Aug 29, 2026 | CallForWorkshops |
| License | CC-BY (OpenReview default) | OpenReview |

## Sources we will rely on

| Source | When usable | Coverage |
|---|---|---|
| [NeurIPS 2026 home](https://neurips.cc/Conferences/2026) | now | dates, satellite hubs, organizers |
| [Call for Workshops](https://neurips.cc/Conferences/2026/CallForWorkshops) | now | workshop timeline |
| [OpenReview NeurIPS group](https://openreview.net/group?id=NeurIPS.cc) | from Sep 24 | accepted main-track papers |
| Per-workshop OpenReview venues | from Oct–Nov | workshop accepted papers |
| [SlidesLive (neurips)](https://slideslive.com/neurips) | from ~Dec 14 | recorded orals + workshop talks |
| bioRxiv / arXiv | continuous | preprints, filterable by "to appear at NeurIPS 2026" |
| `#NeurIPS2026` on Bluesky / Mastodon / X | Dec 6–13 | real-time talk reactions |
| Lab blogs (DeepMind, Anthropic, Insitro, Recursion, Genentech prescient design, Isomorphic Labs) | rolling | preprints + summary posts of NeurIPS papers from these labs |

## Filter criteria (locked — mirrors `tools/index.md`)

A paper enters this vault only if it matches **one** of three filters. Reproduced here for the pre-meeting screening pass.

### Filter 1 — workshop track

Accept anything in these workshops (canonical short names; 2026 roster TBD Sep 29):

- **MLSB** — Machine Learning in Structural Biology
- **AI4NewDrugs / AI4D3** — AI for New Drug Modalities / AI for Drug Discovery
- **LMRL** — Learning Meaningful Representations of Life
- **GenAI4Health** — Generative AI for Health
- **AIM-FM** — Advancements In Medical Foundation Models
- **AI4Science** — AI for Science (bio / chem subset only)

### Filter 2 — main-track keyword

Run this regex over titles + abstracts once the main-track list drops:

```
(cancer|oncolog|tumor|metasta|carcinom|melanoma|leukemi|lymphoma)
| (genomic|epigenom|transcriptom|proteom|metabolom|methyl)
| (single[- ]cell|scRNA|scATAC|spatial transcriptom|spatial omic)
| (perturbation|CRISPR|knockout|knockdown|sgRNA)
| (drug discover|target ident|molecular property|ADMET|small molecul|biologic|de novo design|generative chemistry)
| (protein structur|protein function|protein language|equivariant|RFdiffusion|AlphaFold|Boltz|ESM)
| (foundation model.*(biolog|cell|genom|tissue|pathol|clinical|medical))
| (electronic health record|EHR|clinical NLP|medical imaging|pathology|histolog|radiolog|diagnos)
| (virtual cell|cell atlas|cellular state)
```

### Filter 3 — agentic-AI / LLM-for-science subset

Independent of bio framing, accept any main-track or workshop paper on:

- LLM agents with tool-use, code-execution, or experiment-design loops
- Scientific-reasoning benchmarks (SWE-bench-class, sci-agent-class, lab-task benchmarks)
- Autonomous research / hypothesis-generation systems
- Multi-agent scientific workflows

Rationale: these adapt to oncology within 6 months (the empirical pattern from 2024 → AACR 2025 and 2025 → AACR 2026) and feed the AACR agentic-AI axis directly.

## Expected paper themes (5 anchors)

Pre-meeting predictions, to be reconciled against the actual list in September. These are the buckets we expect `tools/` entries to cluster into.

### Theme 1 — Foundation models for biology, second generation

scGPT, Geneformer, and ESM are 2022–2024 vintage. NeurIPS 2026 should feature the next-gen models: cross-modal (DNA + RNA + protein + tissue + clinical), multi-million-cell training corpora, instruction-tuned for downstream tasks (perturbation prediction, virtual-screen rerank), and benchmarked on virtual-cell tasks rather than embedding-quality proxies. Workshop home: **LMRL**, with main-track spillover.

### Theme 2 — Agentic AI for science

Tool-use LLMs that drive bioinformatics pipelines, design wet-lab experiments, or autonomously navigate clinical-decision trees. 2025 surfaced ChemCrow / Coscientist-class systems; 2026 should bring oncology-specific agents (tumor-board agents, trial-matching agents, multi-omics interpretation agents). Workshop home: main-track + **GenAI4Health** + **AIM-FM**.

### Theme 3 — Single-cell + spatial ML methods

Cell-state representation learning, perturbation-response prediction (replogle-class, sci-Plex-class benchmarks), spatial-transcriptomics imputation and cell-cell communication inference, virtual-tissue generation. Workshop home: **LMRL**; main-track for the methods-heavy contributions.

### Theme 4 — Generative chemistry and protein design for oncology targets

De novo small-molecule generation conditioned on oncology targets, antibody / TCR / peptide design, equivariant diffusion models for protein–ligand docking, RFdiffusion descendants, Boltz / AlphaFold3-class structure models. Workshop home: **MLSB** + **AI4D3**.

### Theme 5 — Medical foundation models and clinical NLP

Pathology FMs (CHIEF / GigaPath / Virchow successors), radiology FMs, EHR-derived patient-trajectory models, clinical-trial-matching language models, regulatory and safety work on medical LLMs. Workshop home: **AIM-FM** + **GenAI4Health**; main-track for the biggest model releases.

## Pre-meeting timeline (action items)

| Date | Action |
|---|---|
| Now → Sep 24, 2026 | passive monitoring; no extraction |
| **Sep 24, 2026** | main-track accepted list drops on OpenReview — run keyword regex, build candidate list |
| **Sep 29, 2026** | workshop roster finalized — confirm which of the six bio/health workshops actually run, identify any new entrants |
| Oct–Nov 2026 | per-workshop accepted-paper lists drop — extend candidate list |
| Nov 2026 | scaffold likely `tools/` pages from titles + bioRxiv mirrors (no waiting for the talks) |
| **Dec 6–13, 2026** | meeting week — opportunistic real-time capture from social, especially agentic-AI orals |
| Mid-Dec 2026 → Jan 2027 | bulk `tools/` population from SlidesLive recordings + camera-ready papers |

## Caveats

- **No accepted-paper list exists yet.** Everything above is anchored on past-year patterns. The 2026 workshop roster could drop a recurring bio workshop or add a new one we haven't planned for; the keyword filter is the safety net.
- **Three-hub model is new.** It's plausible that workshop programs differ across Sydney / Atlanta / Paris. Until the per-hub programs publish (~Oct), we assume a unified program; revisit if not.
- **OpenReview lag.** Camera-ready and supplementary materials sometimes lag the accept notification by weeks. Tool pages may need a "weights / code TBA" placeholder for the first month.
- **Agentic-AI scope creep risk.** Filter 3 is broader than Filters 1–2 by design, but it can swell if applied loosely. Keep the "science / tool-use benchmark required" caveat from `tools/index.md` open question 2.
