# scverse 2025

**scverse Conference 2025** — Li Ka Shing Center, Stanford University, Stanford, CA · November 17–19, 2025.

> **Status:** Scaffold — program ingested; per-tool / per-talk dossiers queued. The full 3-day program has been extracted from the official schedule (2 keynotes Day 1, 2 keynotes Day 2, 3 parallel tracks Day 3); bulk dossier generation is the next pass.

## Why this is in the vault

scverse 2025 is the **first US edition of the scverse community conference** (prior editions in Heidelberg/Cambridge). scverse — the ecosystem behind **Scanpy, AnnData, SpatialData, scvi-tools, decoupler, rapids-singlecell** — is the single-cell analysis stack used by most labs working at the **single-cell foundation models** and **virtual cells** frontier. The 2025 program is unusually load-bearing for the FM → Virtual Cells thesis:

- **Virtual cell content is first-class**, not a side-track: Day 3 Arc Institute track is an end-to-end virtual-cell workflow (data → processing → ML → progress panel with VCC teams).
- **A foundation-model showcase track** (Day 3 CZI) covers CxG foundation models, NVIDIA GPU acceleration, VCP benchmarking, LazySlide / SIMBA+ / Celldega.
- **An AI-agents track** (Day 3 Tahoe) covers Tahoe-x1 (3B-parameter FM), BioContextAI MCP servers, SigSpace LLM agents, large-scale dataset mining.
- **A dedicated agentic-workflows panel** with speakers from **Anthropic, NVIDIA, CZ Biohub, and Stanford** (Day 1, 15:30) — directly targets the [FM → Virtual Cells talk](https://liudengzhang.github.io/fm-to-virtual-cells/) thesis.

scverse 2025 is **sister-event to EuroBioC2025 (Sep 17–19, Barcelona) and GBCC 2025 (Jun 23–26, Cold Spring Harbor)** — together they form the three 2025 community-driven open-source-bioinformatics meetings already in this corpus. scverse covers the single-cell / spatial / virtual-cell axis those two don't.

## What we have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Conference site** | overview + schedule + abstracts | <https://scverse.org/conference2025/> |
| **Schedule page** | every talk: title, speaker, affiliation, session, chair, time | <https://scverse.org/conference2025/schedule/> |
| **Satellite workshops** | Nov 19 — three parallel tracks: Arc (Perturb-seq), CZI (Foundation Models), Tahoe (AI Agents) | linked from main schedule |
| **Recordings / proceedings** | not yet announced at meeting time; scverse historically posts plenary recordings to YouTube | placeholder — revisit post-meeting |
| **scverse community hubs** | code / packages / discussion | <https://scverse.org>, <https://github.com/scverse>, <https://discourse.scverse.org> |

## Program shape

### Day 1 — Monday, November 17 (LKSC)

- **Welcome / State of scverse** — Emma Dann · Mikaela Koutrouli
- **Keynote 1: John Marioni** (Genentech) — chair: Emma Dann
- **Perturbation & CRISPR session** (4 talks): Dillon Lue (Princeton — clonally resolved Perturb-seq) · Logan Blaine (Harvard — PerTurbo framework) · Kanishk Asthana (UCSD — ChronoSeq automated scRNA-seq) · Samantha Dale Strasser (Somite Therapeutics — virtual cell signaling model)
- **Keynote 2: Panos Roussos** (Mount Sinai) — chair: Mikaela Koutrouli
- **Regulatory / clinical prediction session**: Laura Gunsalus (Genentech — universal MPRA regulatory prediction) · Danai Vagiaki (EMBL — LIVI deep learning framework) · Kameron Rodrigues (Stanford — CAR T cell therapy prediction)
- **Panel: Agentic Workflows for Bioinformatics** — Jonah Cool (Anthropic) · Vega Shah (NVIDIA) · Loic Royer (CZ Biohub) · Kexin Huang (Stanford); chair: Giovanni Palla
- **Poster Session 1** · Reception

### Day 2 — Tuesday, November 18 (LKSC)

- **Keynote 3: Erika Alden de Benedictis** (Align Foundation / Pioneer Labs) — chair: Danila Bredikhin
- **Splicing & Transcriptomics session**: Jiayu Su (Columbia — SPLISOSM isoform analysis) · Smriti Vaidyanathan (Columbia — SpliceVI integration) · Johnny Yu (Tahoe Therapeutics — virtual-cell datasets)
- **Keynote 4: Elham Azizi** (Columbia) — chair: Pau Badia i Mompel
- **Perturbation / sequence-determinants / peak-calling session**: Ann Huang (Xaira — X-Atlas/Orion Perturb-seq platform) · Avantika Lal (Genentech — gene expression sequence determinants) · Tao Liu (Roswell Park — MACS3) · Angela Oliveira Pisco (CZI — AI and biology solutions)
- **Spatial proteomics & visualization session**: Max Frank (CZ Biohub — `grassp` spatial proteomics framework) · Eunice Lee (Harvard — InterSCellar 3D cell-interaction analysis) · Eric Mörth (Harvard — EasyVitessce visualization)
- **Closing remarks panel** (scverse core team) · **Poster Session 2**

### Day 3 — Wednesday, November 19 (three parallel tracks)

**Arc Institute track — Perturb-seq workflow** (Yusuf Roohani et al.)

- Session 1 — Generating data: Tony Hua · Po-Yuan Tung (Perturb-seq experimental design)
- Session 2 — Data processing: Noam Teyssier (Cell-eval evaluation suite) · Alexander Dobin (perturbation effect assessment) · Ilan Gold (AnnData scalability) · Logan Blaine (PerTurbo framework)
- Session 3 — ML models: Nick Youngblut & Chris Carpenter (scBaseCount — 500M+ cells) · Can Ergen (scvi-tools perturbation studies) · Ellie Haber & Shahul Alam (Heimdall tokenization framework) · Abhinav Adduri (State perturbation prediction tool)
- Session 4 — Virtual cell progress panel: Dave Burke · Alexander Dobin · Noam Teyssier · Hani Goodarzi (Arc) · Stefan Peidli (scverse/Genentech) · VCC teams; moderator: Yusuf Roohani

**CZI track — Foundation models & community**

- Max Lombardo (Biohub — CxG foundation landscape)
- TJ Chen · Gary Burnett (NVIDIA — GPU-accelerated single-cell analysis)
- Luca Marconato (Biohub — 3D spatial data showcase)
- Elizabeth Fahsbender · Katrina Kalantar · Alec Tarashansky · Max Lombardo (Biohub — VCP models & benchmarking)
- Yimin Zheng (LazySlide whole-slide imaging)
- Junxi Feng (SIMBA+)
- Zhenru Zhou (ProteoImager)
- Huan Wang (Celldega)

**Tahoe Therapeutics track — AI agents & scaling**

- Severin Dicks (scverse — rapids-singlecell GPU acceleration)
- Davide d'Ascenzo (University of Milan — scDataset deep-learning loader)
- Darius Schaub (UMCH Hamburg-Eppendorf — BioContextAI MCP servers)
- Siddhant Sanghi (UC Davis — SigSpace LLM drug-signature agent)
- Kepler team (large-scale biomedical dataset mining)
- Shreshth Gandhi (Tahoe — Tahoe-x1 foundation model, 3B parameters)
- Pau Badia i Mompel (scverse — decoupler enrichment analysis)
- Panel: Tahoe Therapeutics team discussion

**Counts:** 4 keynotes · ~30 contributed talks across Day 1–2 · 3 parallel Day-3 tracks (~30 additional talks) · 2 poster sessions.

## Organization

```
conferences/scverse-2025/
├── index.md                 # this page
├── themes.md                # cross-day synthesis (deferred)
├── digest/                  # day-by-day recap (deferred)
│   ├── day-1.md
│   ├── day-2.md
│   └── day-3.md
├── keynotes/                # 4 keynote dossiers (deferred)
│   ├── marioni.md
│   ├── roussos.md
│   ├── debenedictis.md
│   └── azizi.md
├── topics/                  # cross-cutting bins (deferred)
│   ├── virtual-cells/       # Arc track + Somite + Tahoe virtual-cell datasets
│   ├── foundation-models/   # CZI track + Tahoe-x1
│   ├── agentic-workflows/   # Day 1 panel + Tahoe AI-agents track
│   ├── perturbation/        # PerTurbo, Cell-eval, X-Atlas/Orion, State
│   └── spatial-imaging/     # grassp, InterSCellar, EasyVitessce, LazySlide
├── tools/                   # per-tool dossiers (deferred — see queued task)
│   └── index.md
└── sessions/                # full session abstracts (deferred)
    └── index.md
```

## Cross-links

- **FM → Virtual Cells talk** (companion site, password-gated): <https://liudengzhang.github.io/fm-to-virtual-cells/>. The agentic-workflows panel (Day 1) and the Tahoe AI-agents track (Day 3) sharpen the case for several sections of that talk — especially §3.11 (institutional landscape) and §11.4 (people-to-follow).
- **Arc Institute Virtual Cell program** — Day 3 Arc track is the most public-facing milestone for Arc's virtual-cell effort to date; State perturbation model (Adduri) and scBaseCount (Youngblut/Carpenter) are the headline artifacts. Tracked in the FM corpus' Arc dossier.
- **CZI CellxGene / VCP** — Day 3 CZI track lays out the CxG → foundation-model pipeline; ties into the FM dossiers for the CellxGene Census-pretrained models.
- **Tahoe-x1 (3B FM)** — single largest single-cell foundation model presented in 2025; companion dossier sits in the FM corpus on the FM→VC site.

## Sources

- [scverse Conference 2025 overview](https://scverse.org/conference2025/)
- [scverse Conference 2025 schedule](https://scverse.org/conference2025/schedule/)
- [scverse organization](https://scverse.org/)
- [scverse GitHub](https://github.com/scverse)
- [Arc Institute Virtual Cell program](https://arcinstitute.org/programs/virtual-cell-program)
- [CZI CellxGene Census](https://cellxgene.cziscience.com/)
- [Tahoe Therapeutics](https://www.tahoebio.ai/)

## Next step

The Day-3 Arc / CZI / Tahoe tracks are the highest-value bulk-build target — every talk there maps onto an existing FM-corpus dossier or seeds a new one. Queued as **#181 Bulk-build scverse 2025 dossiers (post-meeting)**.
