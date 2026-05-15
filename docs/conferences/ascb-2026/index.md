# ASCB | EMBO Cell Bio 2026

**Cell Bio 2026 — An ASCB | EMBO Meeting** · San Diego Convention Center, San Diego, CA · December 12 – 15, 2026. The joint annual meeting of the American Society for Cell Biology and the European Molecular Biology Organization — historically ~6,000 attendees, the largest pure cell-biology venue of the year.

> **Status:** Scaffold — meeting is **7 months out** as of today (May 11, 2026). The vault is being seeded now so we can move on the abstract cycle (submission site opened Apr 7, 2026; talk + early-poster deadline Jun 9; late-poster deadline Aug 4). Anything in this vault dated before Cell Bio 2026 is built from the published keynote / symposia slate, Cell Bio 2025 program shape, and ASCB-announced abstract topic categories — flagged inline.

## Why this is in the vault

ASCB Cell Bio is the **cell-biology basic-science counterpart** to the AACR clinical-and-mechanistic axis. Its overlap with the AACR corpus is modest but specific:

1. **Cancer cell biology** — explicit ASCB topic category. Signaling, mitosis, autophagy, organelle biology, and cell-cycle work that lands at AACR as "mechanism of disease" sessions originates in labs that present basic findings at ASCB first.
2. **Advanced imaging and tools** — ASCB is the **bioimaging methods venue**, where new microscopy modalities (super-resolution, lattice light-sheet, expansion microscopy, AI segmentation) and image-analysis pipelines (Cellpose, Stardist, napari, ZeroCostDL4Mic, MorphoNet) get their largest cell-biology audience. This is the methods axis that ties to MICCAI (medical imaging methods) and to EuroBioC / GBCC (image-analysis Bioconductor / Python packages).
3. **Organoids and 3D models** — ASCB is one of the main venues where stem-cell-derived organoid biology and assembloid work is presented as cell-biology rather than clinical translation. Cross-links to AACR's translational organoid programs.
4. **AI / foundation models for cell biology** — emerging track. Virtual-cell, cell-state, and image-foundation-model work is starting to land at ASCB alongside (and sometimes ahead of) AACR.

**Hybrid template (and the design decision behind this vault):** Cell Bio is **neither pure-clinical (ASCO) nor pure-tools (EuroBioC) nor pure-AI (NeurIPS)** — it's a basic-biology meeting where the unit of contribution can be either a **biological finding** (e.g., "this organelle contacts that one to do X") or a **tool / method** (e.g., "this new microscope / pipeline / cell line resource"). We're running **one combined per-talk template** in [`talks/`](talks/index.md) with an explicit **anchor type** field (`tool` vs `cell-bio finding`) — same schema, different surfaces. This matches the actual structure of the ASCB program where adjacent talks in a minisymposium can be a microscopy method and a mitosis-regulation finding.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Cell Bio 2026 site** | program-at-a-glance, plenary slate, symposia, minisymposia, workshops | [ascb.org/cellbio2026](https://www.ascb.org/cellbio2026/) — primary |
| **ASCB Newsletter / ASCB Post** | curated session writeups, pre-meeting features | [ascb.org/ascb-news](https://www.ascb.org/ascb-news/) |
| **Molecular Biology of the Cell (MBoC)** | the ASCB-published journal where many Cell Bio talks become papers | [molbiolcell.org](https://www.molbiolcell.org/) |
| **Image-of-the-Year + Celldance video archive** | ASCB's visual record; useful as a cross-reference for imaging-methods talks | ASCB site |
| **#CellBio2026 (X / Bluesky / Mastodon)** | real-time session reactions; cell-bio Mastodon presence is substantial | community channels |
| **bioRxiv preprint timing** | many ASCB talks have a bioRxiv preprint posted within ~30 days of the meeting | search by speaker |
| **YouTube ASCB channel** | keynote + select symposium replays (typically posted weeks after the meeting) | [youtube.com/ASCBtube](https://www.youtube.com/user/ASCBtube) |
| **Cell Bio virtual platform** | hybrid registration; session replay for remote attendees | ASCB Hubb / Cvent platform |

The **primary citable record is the abstract supplement** indexed alongside MBoC, plus per-talk preprints on bioRxiv. Unlike clinical conferences (SITC's JITC, ASCO Meeting Library), Cell Bio's preprint-mediated citation pattern means a talk's "permanent record" often lives in the speaker's bioRxiv link, not the ASCB-hosted abstract.

## Program shape (verified slate + Cell Bio 2025 program shape)

Cell Bio 2026 runs **Saturday Dec 12 – Tuesday Dec 15**, four days. The structure (per ASCB 2025 / 2026 cadence):

- **Sat Dec 12 (PM):** Opening Keynote + welcome reception. Subgroup meetings earlier in the day.
- **Sun Dec 13 – Tue Dec 15:** Symposia + minisymposia + workshops + poster halls. Three keynote slots run across the meeting body.
- **Verified keynote speakers (4 total, ASCB announced):**
  - **Elaine Fuchs, PhD** (HHMI / Rockefeller) — Rebecca C. Lancefield Professor; skin / stem-cell biology, niche signaling, cancer initiation.
  - **Ramanujan Hegde, PhD** (MRC Laboratory of Molecular Biology, Cambridge) — protein quality control, co-translational folding, ER membrane biology.
  - **Liqun Luo, PhD** (Stanford / HHMI) — neural-circuit assembly, single-neuron tracing methods, cell-type taxonomy.
  - **Elly Tanaka, PhD** (IMBA, Austrian Academy of Sciences) — regeneration biology (axolotl), limb / spinal-cord repair, blastema cell-state programming.
- **Symposia speakers (16 named):** Yale, Fred Hutchinson Cancer Center, King's College London, UC San Diego, Washington University, UCLA, ETH Zurich, others — full slate on the Cell Bio 2026 site.
- **Abstract scale:** typical Cell Bio meeting runs ~2,500 – 3,500 abstracts across talks + posters, several hundred per minisymposium track, with ~50 minisymposia and ~8 – 12 keynote / symposia slots.
- **Tracks dominating the corpus** (per Cell Bio abstract category list):
  - **Genome biology** — chromatin, transcription, DNA replication / repair, RNA biology
  - **Membrane biology and trafficking** — ER / Golgi / endosomal, secretion, exocytosis
  - **Cytoskeleton and motility** — actin, microtubules, intermediate filaments, cell migration
  - **Signal transduction** — kinase cascades, GPCR, second messengers, mechanotransduction
  - **Organelles and cell division** — mitosis, meiosis, centrosomes, cytokinesis
  - **Cell metabolism and stress response** — autophagy, UPR, integrated stress response
  - **Cell death and aging** — apoptosis, necroptosis, ferroptosis, senescence
  - **Disease mechanisms** — neurodegeneration, infection, inflammation
  - **Developmental and stem cell biology** — pluripotency, lineage commitment, organoids
  - **Cancer cell biology** — *the explicit AACR overlap category*
  - **Immune cell biology** — innate / adaptive at the cellular level
  - **Plant and evolutionary cell biology** — comparative / non-model cell biology
  - **Advanced tools and technologies** — microscopy, image analysis, genome engineering, reporter systems
  - **Systems biology and bioengineering** — modeling, synthetic biology, organ-on-chip
  - **Science education** — pedagogy / DEI track

## Organization

```
conferences/ascb-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep: dates, venue, tracks, expected themes, tool / cell-bio watch list, key dates
└── talks/               # hybrid per-talk template — anchor type: tool OR cell-bio finding
    └── index.md         # template + master talk index table (keynotes, symposia, minisymposia, methods)
```

Day-by-day digest (`digest/day-N-*.md`) and cross-day themes (`themes.md`) deferred until post-meeting, modeled on the JPM 2026 / Nextflow 2026 vaults.

## What's different from the rest of the corpus

- **Basic-science, not clinical.** No drug readouts, no trials, no FDA-state surface. Cancer cell biology appears as mechanism work, not as therapeutic-class status.
- **Findings + tools in the same per-talk schema.** Unlike SITC (trials/ + tools/ split) or EuroBioC (pure tools), Cell Bio mixes biological-finding talks and method-demonstration talks within the same minisymposium. The `talks/` template carries an `anchor` field so the corpus surfaces this directly.
- **bioRxiv-mediated citation.** Unlike SITC's JITC DOI per abstract, Cell Bio talks are best cited via the speaker's bioRxiv preprint. Per-talk pages should track the preprint link, not just the abstract.
- **December slot, with limited overlap.** Cell Bio runs the same week as ASH (clinical hematology) and the week after SABCS (clinical breast cancer). Anyone attending ASCB is not at ASH — the corpus inherits zero scheduling conflict surface, but does inherit some readership conflict.
- **Hybrid format, smaller virtual surface than clinical meetings.** ASCB has run hybrid Cell Bio meetings since 2021 but with less elaborate virtual infrastructure than ASCO / AACR — many minisymposia are in-person only.

## Cross-vault links

- **[AACR 2026](../aacr-2026/index.md)** — cancer cell biology overlap. Mitosis / autophagy / cell-cycle / signaling work presented at ASCB often reappears at AACR as "mechanism of disease" sessions. Single-cell axis touches both meetings.
- **[MICCAI 2026](../miccai-2026/index.md)** — bioimaging methods overlap. ASCB advanced-tools track includes super-resolution and AI segmentation; MICCAI is the medical-imaging methods venue. Tool talks at ASCB frequently cite or extend MICCAI-published methods.
- **[EuroBioC 2025](../eurobioc-2025/index.md)** — image-analysis tooling overlap. Bioconductor and Python image-analysis packages (Cellpose, napari, Stardist, etc.) appear in both venues; ASCB is where they're demonstrated in cell-biology workflows, EuroBioC is where the R / Bioconductor wrappers are released.
- **[CSHL BDS 2026](../cshl-bds-2026/index.md)** — overlapping early-November / December date band on biological-data-science methods.
- **[Nextflow Summit](../nextflow-2026/index.md)** — pipeline / workflow axis intersects with imaging-pipeline talks at ASCB.
- **[Conferences timeline](../../timeline.md)** — Cell Bio's position in the year's cycle (AACR Apr → ASCO May/Jun → ESMO Oct → SITC Nov → SABCS Dec → ASH Dec → **Cell Bio Dec** → JPM Jan).

## Next step

- **Now (May – Jun 2026, abstract window open):** populate `program-notes.md` with the expected-theme shortlist and watch list for cancer-cell-biology and bioimaging-tool talks. Pre-build keynote stubs for Fuchs, Hegde, Luo, Tanaka in `talks/`.
- **Talk + early-poster deadline (Jun 9, 2026):** abstract submission closes for symposium / minisymposium consideration.
- **Late-poster deadline (Aug 4, 2026):** poster-only abstract close.
- **Program release (~Sep – Oct 2026):** when ASCB posts the program-at-a-glance + minisymposium grid, expand `talks/` stubs to match the actual session slate.
- **Live meeting (Dec 12 – 15):** real-time capture per day. Hybrid platform means selected sessions are available for remote watching; in-person-only minisymposia get covered via social + bioRxiv linkage.
- **Post-meeting (Dec 2026 – Jan 2027):** finalize `themes.md`. Expected threads (speculative, to be revised): organelle contact-site biology maturation, autophagy / lysosomal therapeutic mechanism, AI-foundation-models for cell biology, super-resolution + AI segmentation convergence, organoid / assembloid cell-state programming.

## Sources

- [Cell Bio 2026 — An ASCB | EMBO Meeting (home)](https://www.ascb.org/cellbio2026/)
- [Cell Bio 2026 — Abstract submission](https://www.ascb.org/cellbio2026/abstracts-2026/)
- [Future Cell Bio Meetings](https://www.ascb.org/meetings-events/future-ascb-meetings/)
- [ASCB main site](https://www.ascb.org/)
- [Molecular Biology of the Cell (MBoC)](https://www.molbiolcell.org/)
- [ASCB YouTube channel](https://www.youtube.com/user/ASCBtube)
- [Cell Bio 2025 (reference)](https://www.ascb.org/cellbio2025/)
