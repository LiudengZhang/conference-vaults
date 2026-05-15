# Talks — Cell Bio 2026

The primary artifact for the ASCB vault: **one Markdown file per talk** at Cell Bio 2026 — across keynotes, symposia, minisymposia, and Advanced Tools sessions. Each `talks/<slug>.md` page captures **either a cell-biology finding or a tool / method**, with the same schema but an explicit `anchor` field that surfaces which it is.

> **Status:** Template stub. Hybrid per-talk template carries over the [EuroBioC 2025 tools](../../eurobioc-2025/tools/index.md) structure (the closest sibling, since cell-bio talks often anchor on a tool or resource) with the **anchor field** added so that biological-finding talks aren't shoehorned into a tool-shaped schema. Once the program-at-a-glance posts in September – October 2026, ~30 – 50 entries get populated (4 keynotes + ~10 symposia + selected minisymposia + Advanced Tools talks).

## Per-talk entry template

Each talk gets its own page (`talks/<slug>.md`) following this structure:

````markdown
# <Talk title>

**One-line summary** — what the talk reports, in plain language.

- **Anchor type:** `tool` | `cell-bio finding` | `hybrid`
- **Speaker:** <name>, <position>, <institution>
- **Lab / group page:** [link]
- **Session:** <Keynote / Symposium / Minisymposium / Advanced Tools / Workshop>
- **Day / time slot:** ...
- **Abstract:** [ASCB abstract page]
- **Preprint:** [bioRxiv DOI if posted]
- **Paper:** [DOI if published, e.g., MBoC / Cell / Nature]
- **Status at Cell Bio 2026:** <keynote / symposium feature / minisymposium / new tool release / methods talk / workshop>

(If anchor type = `tool`, also include:)
- **Tool / package / platform name:** ...
- **Repo / source:** [GitHub / GitLab / vendor link]
- **Vignette / docs:** [link]
- **Domain:** <microscopy hardware / image-analysis / segmentation / live-cell / reporter / cell-line resource / AI foundation model / synthetic biology / etc.>

## Talk at Cell Bio 2026

- **Slides:** [link if shared]
- **Video:** [ASCB YouTube link if recorded]
- **ASCB abstract:** [link]

## What it reports / what it does

2–3 sentences. For `cell-bio finding` anchor: the biological question, the
mechanism / result, the cell-biology context (organelle / pathway / cell-type).
For `tool` anchor: the problem it solves, key methodological idea, what it
consumes / produces, validation claimed.

## Where it fits in the corpus

- **AACR 2026:** [link if mentioned in an AACR talk, poster, or topic dossier]
- **MICCAI 2026:** [link if methods-overlap with a MICCAI paper]
- **EuroBioC 2025:** [link if an analogous Bioconductor package was shown]
- **GBCC 2025:** [link if mentioned in Galaxy image-analysis context]
- **Nextflow Summit 2026:** [link if pipeline / workflow cross-link]
- **CSHL BDS 2026:** [link if mentioned at the methods venue]
- **NeurIPS 2026:** [link if AI / foundation-model cross-link]

## Notes

Free-form impressions. For findings: what's new vs the 2024 / 2025 state of
the field, what comparable groups have shown, why this matters for the AACR
overlap (if cancer cell biology). For tools: benchmarks claimed, comparisons
to alternatives, sample-prep / hardware / compute requirements, license,
availability state (preprint / paper / public repo / closed beta).
````

## Talk index

Pre-meeting shortlist of expected entries. Keynote stubs are firm (ASCB announced); symposium / minisymposium / tool entries are **expected, subject to program release**. To be replaced with named talks once Cell Bio 2026 posts the program-at-a-glance and minisymposium grid.

### Keynotes (verified slate — 4 talks)

| Talk | Anchor | Speaker | Institution | Day | Cross-vault link |
|---|---|---|---|---|---|
| Skin stem cells, niche signaling, and cancer initiation (TBD title) | cell-bio finding | Elaine Fuchs, PhD | HHMI / Rockefeller | TBD | [AACR 2026](../../aacr-2026/index.md) cancer-stem-cell biology |
| Protein quality control and the ER membrane (TBD title) | cell-bio finding | Ramanujan Hegde, PhD | MRC LMB, Cambridge | TBD | AACR 2026 proteostasis sessions |
| Neural-circuit assembly and cell-type taxonomy (TBD title) | hybrid (finding + tool) | Liqun Luo, PhD | Stanford / HHMI | TBD | [AACR 2026 virtual-cells dossier](../../aacr-2026/topics/virtual-cells/index.md) |
| Regeneration biology and blastema cell-state programming (TBD title) | cell-bio finding | Elly Tanaka, PhD | IMBA, Vienna | TBD | AACR 2026 single-cell axis; [organoid programs](../../aacr-2026/index.md) |

### Anticipated symposium / minisymposium themes (~10 – 20 entries)

To be expanded into named talks when ASCB posts the program. Categorized by the five anticipated themes from `program-notes.md`.

| Category | Anticipated angle | Anchor expected | Cross-vault link |
|---|---|---|---|
| **Organelle contact sites** | ER – mitochondria, ER – lysosome biology in cancer / neurodegeneration | cell-bio finding | AACR 2026 ferroptosis / autophagy sessions |
| **Selective autophagy** | mitophagy, ER-phagy, lipophagy mechanism | cell-bio finding | AACR 2026 pancreatic / NSCLC autophagy programs |
| **Lysosomal biogenesis (TFEB)** | druggable axis in cancer / lysosomal-storage disease | cell-bio finding | AACR 2026 lysosomal-targeting programs |
| **Mitosis and chromosomal instability** | Aurora / PLK1 / KIF, centrosome amplification | cell-bio finding | AACR 2026 mitotic-inhibitor mechanism sessions |
| **Cell-cycle checkpoints** | CDK inhibition mechanism, replication stress, ATR / ATM | cell-bio finding | AACR 2026 DDR sessions; CDK inhibitor classes |
| **Cell death (ferroptosis / necroptosis)** | mechanism + therapeutic substrate | cell-bio finding | AACR 2026 ferroptosis-induction programs |
| **EMT and cell migration** | actin / Rho-GTPase biology in metastasis | cell-bio finding | AACR 2026 metastasis sessions |
| **Tumor microenvironment cell biology** | stromal-immune signaling at single-cell resolution | cell-bio finding | [AACR 2026 single-cell / spatial dossier](../../aacr-2026/topics/single-cell-spatial-omics/index.md); [SITC 2026 tools](../../sitc-2026/tools/index.md) |
| **Image-foundation models in cell biology** | CellSAM / MicroSAM / Cellpose 3 demos | tool | [MICCAI 2026 tools](../../miccai-2026/tools/index.md) |
| **Single-cell foundation models** | scGPT / Geneformer / scFoundation in cell-state biology | tool | [AACR 2026 virtual-cells dossier](../../aacr-2026/topics/virtual-cells/index.md) |
| **Virtual-cell models** | CZI Virtual Cell Initiative, Tahoe-100M class | tool | AACR 2026 virtual-cells axis |
| **Super-resolution updates (MINFLUX / DNA-PAINT)** | sub-10 nm single-molecule localization | tool | Microscopy hardware vendor sessions |
| **Expansion microscopy variants** | iterative ExM, magnify, X10 ExM | tool | Cell-bio ultrastructure workflows |
| **Cellpose 3 / Stardist / napari** | open-source image-analysis tooling | tool | [EuroBioC 2025 HistoImagePlot](../../eurobioc-2025/tools/histoimageplot.md); MICCAI cross-links |
| **OpenCell-style endogenous-tagging atlases** | CRISPR knock-in cell-line resources | tool | Cell-line resource sessions |
| **Optogenetic / chemogenetic recruitment** | engineered perturbation tools | tool | Synthetic-biology track |
| **Organoid / assembloid cell-state mapping** | single-cell + spatial atlases | hybrid | [AACR 2026](../../aacr-2026/index.md); ASCO patient-derived-organoid trials |

### Anticipated Advanced Tools session entries (~10 – 15 entries)

The Advanced Tools track is the highest-density tool-anchor section of the program. Pre-meeting shortlist (to be replaced with named talks once announced):

| Tool / platform | Domain | Lab / vendor | Anticipated angle |
|---|---|---|---|
| Cellpose 3 | image segmentation | Stringer / Pachitariu (Janelia) | Generalist cell-segmentation foundation model update |
| Stardist | nuclear segmentation | Weigert / Schmidt (TU Dresden / MPI-CBG) | Star-convex polygon detection updates |
| napari + plugin ecosystem | image visualization / analysis | napari core team | New plugins, napari-hub status |
| ZeroCostDL4Mic | DL training for biologists | Henriques lab (King's College London) | Accessible training pipelines |
| BiaPy | DL microscopy | CSIC / collaborators | DL workflow ecosystem |
| OpenCell endogenous-tagging atlas | CRISPR cell-line resource | Leonetti (CZ Biohub) | Atlas expansion / new modalities |
| MINFLUX / DNA-PAINT updates | super-resolution | Various | Sub-10 nm single-molecule localization |
| Janelia mesoSPIM / lattice light-sheet 2.0 | live imaging hardware | Janelia, ETH Zurich | Adaptive optics, speed, depth in live tissue |
| Expansion microscopy (iterative ExM / magnify) | ultrastructural light microscopy | Boyden / others | Iterative protocols, magnify |
| MERFISH / seqFISH / Xenium subcellular | spatial transcriptomics at subcellular | Zhuang / Cai / 10x Genomics | RNA-localization at cell-bio resolution |
| CODEX / MIBI / IBEX | multiplex protein imaging | Akoya / Standard BioTools / academic IBEX | Cell-bio panel updates |
| napari-imagej / DeepImageJ | DL bridge to ImageJ | Various | Bridge ecosystem |
| Cryo-CLEM / cryo-FIB-SEM | structural – functional bridge | Various | Connecting cell-bio FL to structural biology |
| CellSAM / MicroSAM / nnU-Net derivatives | image-foundation segmentation | Pathlab / Anwai labs | SAM-derivative validation in cell-bio settings |
| Virtual-cell prediction models | AI / foundation models | CZI Virtual Cell consortium | Cell-state prediction frameworks |

### Workshops (~5 – 10 entries when announced)

ASCB pre-meeting and concurrent workshops on cell-biology methods. Past workshops have covered Cellpose / Stardist hands-on, expansion microscopy protocols, single-molecule imaging, CRISPR design and screening, and DEI / training topics.

## Why this format

- **Anchor field is the load-bearing piece** — Cell Bio talks split roughly half between biological findings and tool / resource demos. A single schema with a typed anchor surfaces this split without forcing a forked template.
- **bioRxiv preprint field is upgraded relative to clinical templates** — for ASCB, the preprint is often the citable record, not the abstract. Per-talk pages should track the preprint as a first-class field.
- **MBoC paper field** — many Cell Bio talks become MBoC papers within 6 – 12 months. Surfacing this in the schema makes it easy to back-link talks to their published-paper record once those drop.
- **Cross-vault links surface the AACR / MICCAI / EuroBioC overlap directly** — the corpus payoff for this vault is the cross-link to the cancer-cell-biology axis at AACR and to the image-analysis methods at MICCAI / EuroBioC.

## Open questions for the build

1. **Keynotes vs symposia depth** — keynotes get full pages with preprint + paper history; symposia probably also full pages; minisymposia covered selectively where they intersect with the cancer / tools axes. Open: how aggressively to populate minisymposium pages outside the cancer / imaging-tools tracks?
2. **bioRxiv preprint matching pre-meeting** — many Cell Bio 2026 talks already have preprints posted (or will, in the Oct – Nov 2026 window). Open: build a preprint-search script to match by speaker / lab / topic into pre-populated stubs?
3. **Tools that are commercial platforms vs open-source** — same Status badge treatment as SITC: `Platform / vendor / open-source repo / vignette / preprint`. Commercial microscopy vendors (Zeiss, Leica, Nikon, Olympus, ONI, Abberior, Lattice Bio) run industry symposia — treat as `Status: vendor case-study`?
4. **AI foundation-model talks** — these are increasingly cross-cutting between Cell Bio's Advanced Tools track and the NeurIPS / ICML / ICLR foundation-models-for-science workshops. Open: build a unified foundation-model index across all four vaults?
5. **AACR cross-link granularity** — at session level (e.g., "AACR 2026 mitosis sessions") vs at named-talk level (specific AACR talk → specific ASCB talk). Open: which is more useful as the join key?
