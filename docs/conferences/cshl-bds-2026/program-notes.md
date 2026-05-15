# CSHL GI 2026 / BDS 2026 — Program Notes (pre-meeting prep)

> **Internal working file.** Pre-meeting prep notes capturing dates, venue, sources, expected major sessions, and cross-vault overlap watch for CSHL's late-fall 2026 methods meeting. The actual meeting in this slot is **Biological Data Science 2026** (Nov 4–7) — Genome Informatics is biennial and runs in odd years; the next GI is Nov 2027. See [`index.md`](index.md) for the public-facing version of this context.

## Verified facts (May 2026)

- **Meeting:** Biological Data Science 2026 (CSHL "DATA" meeting code) — the 7th biennial BDS, filling the late-fall methods slot that alternates with Genome Informatics (GI, the "INFO" code, which last ran Nov 2025 and runs again Nov 2027).
- **Dates:** Wednesday Nov 4, 2026 (7:30 PM start) → Saturday Nov 7, 2026 (lunch).
- **Venue:** Cold Spring Harbor Laboratory, One Bungtown Road, Cold Spring Harbor, NY 11724. Main program in Grace Auditorium (single-track). Posters in Bush Lecture Hall + adjacent corridors.
- **Organizers (BDS 2026):** Elinor Karlsson (UMass Chan Medical School / Broad Institute), Michael Schatz (Johns Hopkins University), Catalina Vallejos (University of Edinburgh / Alan Turing Institute, UK).
- **Reference organizer roster — GI 2025 (last GI):** Zamin Iqbal (University of Bath, UK), Ben Langmead (Johns Hopkins University), Camille Marchet (University of Lille, France). Schatz is a recurring CSHL late-fall-methods organizer across both meetings.
- **Six BDS 2026 sessions (announced):**
  1. **Algorithmics** — sequence algorithms, indexing, pangenomes, de Bruijn graphs, minimizers
  2. **Population Genetics and Personalized Medicine** — PRS, biobank-scale GWAS, ancestry-aware methods, rare-variant inference
  3. **Machine Learning** — deep learning for regulatory genomics, foundation models, protein/RNA ML, expected agentic-AI presence
  4. **Tools, Visualization, and Infrastructure** — Galaxy/Nextflow/AnVIL/Snakemake-adjacent; JBrowse-class viewers; cloud-native pipelines
  5. **Functional Genomics** — perturbation/CRISPR-screen analysis, regulatory inference, multi-modal integration
  6. **Spatial Genomics and Spatial Biology** — Visium HD, MERFISH/seqFISH/Xenium analysis, spatial-graph methods, tissue-aware deep learning
- **Keynote speakers (2026):** not yet announced as of May 2026. GI 2025 had two keynotes (Yana Safonova, Penn State — adaptive immune repertoire methods; Marinka Zitnik, Harvard — therapeutic-graph foundation models). BDS 2024 followed the same 2-keynote pattern. Expect BDS 2026 keynotes to be announced ~July–August 2026.
- **Abstract deadline (2026):** not yet posted; historical pattern is early September for a Nov meeting.
- **Recording policy:** **none** (CSHL policy — applies to both GI and BDS). Slides are speaker-deposited (Zenodo / lab sites); social signal lives at #CSHLmeetings on Bluesky + X.

## Expected major sessions — shape inference

Inference from BDS 2024 (last BDS), GI 2025 (last GI), and the six announced 2026 sessions. **None of the 2026-specific talk titles are public yet** — what follows is sessionwise expectation, not extracted content.

### Algorithmics

- **Pangenomes** — Cuttlefish 3-class assemblies (Rob Patro group; Rayan Chikhi group), VG / GBZ indexing updates, ODGI/PGGB pipeline maturity. Pangenome panel at HG003-class scale.
- **Long-read assembly and polishing** — herro-class neural polishing, T2T-CHM13 derivative assemblies, Verkko / hifiasm / HiCanu updates.
- **k-mer / minimizer / sketching infrastructure** — `mash`, `sourmash`, `dashing`, KMC successors. High likelihood of a tool talk on space-efficient pangenome indexing.
- **Expected debut tools:** ~6–10 talks; ~5–8 likely to get tool pages.

### Population Genetics and Personalized Medicine

- **PRS at scale** — multi-ancestry PRS portability, PRS-CSx / SBayesRC updates, biobank-PRS pipelines (UK Biobank, All of Us, FinnGen).
- **Statistical genetics methods** — rare-variant collapsing, GxE inference, fine-mapping (SuSiE-class), TWAS extensions, conditional/joint analysis at All-of-Us scale.
- **Personalized-medicine bridges** — clinical-genomics pipelines, ACMG-class variant interpretation automation.
- **Expected debut tools:** ~5–8 talks; ~4–6 likely to get tool pages. Heavy preprint signal.

### Machine Learning

- **Foundation models for genomics** — Enformer/Borzoi successor work, DNA-language-model variants (Caduceus, HyenaDNA, DNABert-2), single-cell foundation models (Geneformer/scGPT/scFoundation lineage).
- **Deep learning for regulatory** — basenji-class enhancer prediction, allele-specific deep models (overlap with RECOMB 2026 paper #19 Mostafavi-coauthored).
- **Protein / RNA ML** — ESM-3 derivative work, RNA-FM, AlphaFold3 downstream applications.
- **Agentic AI** — if 2025 pattern continues (GI 2025 had agentic-AI track presence), expect 2–3 talks on LLM-driven bioinformatics agents (overlap with GBCC 2025 GalaxyMCP, ISMB 2026 BOSC agentic-pipeline track).
- **Expected debut tools:** ~6–10 talks; ~5–7 likely to get tool pages.

### Tools, Visualization, and Infrastructure

- **Pipeline frameworks** — Nextflow-adjacent work (overlap with Nextflow Summit 2026 Oct slot), Snakemake updates, Galaxy infrastructure (overlap with GBCC 2025).
- **Genome browsers and viewers** — JBrowse 3, IGV.js updates, pangenome viewers (Bandage successors, Panagram-class).
- **Cloud-native genomics infrastructure** — AnVIL, Terra, Seqera Platform, DNAnexus-adjacent.
- **Reproducibility / packaging** — Bioconda updates, container-orchestration, WDL/CWL refresh.
- **Expected debut tools:** ~5–8 talks; ~5–7 likely to get tool pages. **Highest sibling-vault overlap.**

### Functional Genomics

- **Perturbation analysis** — Perturb-seq / CROP-seq analysis methods (overlap with EuroBioC spatialFDA-class work).
- **Single-cell regulatory inference** — multi-modal ATAC + RNA + protein integration, GRN inference (overlap with RECOMB 2026 single-cell papers).
- **CRISPR-screen analysis** — MAGeCK successors, dual-guide statistical methods.
- **Expected debut tools:** ~5–7 talks; ~4–6 likely to get tool pages.

### Spatial Genomics and Spatial Biology

- **Visium HD analysis** — sub-spot deconvolution, neighborhood inference, multi-sample comparison (overlap with EuroBioC 2025 DESpace / spatialFDA / SpatialData / OSTA).
- **Imaging-based ST** — MERFISH / seqFISH / Xenium analysis pipelines, segmentation-aware quantification (overlap with RECOMB 2026 MOSAICField / DIME / LineageMap).
- **Tissue-aware deep learning** — histopathology FMs (overlap with EuroBioC HistoImagePlot, AACR 2026 spatial dossier), Visium-HD-trained transformers.
- **Expected debut tools:** ~5–8 talks; ~5–7 likely to get tool pages. **Highest AACR-axis fit.**

**Total expected:** ~30–40 tool-pages across the six sessions. Plus posters: ~120–150 posters total, of which ~30–50 have associated preprints and warrant tool entries (or a lighter-weight `posters/index.md` table).

## Cross-vault overlap watch

Authors / labs / tools likely to appear at CSHL BDS 2026 *and* at another vault'd meeting. This list drives the pre-meeting tool-page scaffolding pass — for each entry below, the BDS 2026 page either is the canonical or links back to the canonical sibling-vault entry.

### People expected to appear

| Person | Lab / institution | Sibling-vault appearance | BDS 2026 likely session |
|---|---|---|---|
| Michael Schatz | JHU | BDS 2026 organizer; GBCC 2025 (sibling CSHL); ISMB 2026 (BOSC history) | Algorithmics / Spatial (his lab spans both) |
| Ben Langmead | JHU | GI 2025 organizer; ISMB 2026 (Bowtie2 lineage); RECOMB 2026 (sequence algorithms) | Algorithmics |
| Rob Patro | Maryland | RECOMB 2026 (Cuttlefish 3, paper #49); GBCC 2025 (tximeta/fishpond); EuroBioC 2025 sibling | Algorithmics |
| Rayan Chikhi | Institut Pasteur | RECOMB 2026 PC Chair; ISMB 2026; sequence algorithms | Algorithmics |
| Zamin Iqbal | Bath / EMBL-EBI | GI 2025 organizer; ISMB 2026 (pangenome track) | Algorithmics / Tools-Viz-Infra |
| Catalina Vallejos | Edinburgh / Turing | BDS 2026 organizer; EuroBioC (BASiCS scRNA stats) | ML / Functional Genomics |
| Elinor Karlsson | UMass / Broad | BDS 2026 organizer; AGBT 2026 platform-launch axis (Darwin's Ark) | PopGen / Functional Genomics |
| Olga Troyanskaya | Princeton | ISMB 2026 keynote (Mon Jul 13); RECOMB 2026 (Aggarwal/Sokolova co-author) | ML / Spatial |
| Anshul Kundaje | Stanford | ISMB 2026; ML for regulatory genomics; basenji/borzoi lineage | ML |
| Sara Mostafavi | UW / Allen | RECOMB 2026 keynote (Fri May 29); allele-specific deep models | ML |
| Jingyi Jessica Li | UCLA | RECOMB 2026 (3 papers: Information-Geometry, Nullstrap-DE, scDesignPop); ISMB 2026 MLCSB | ML / Functional Genomics |
| Bonnie Berger | MIT | RECOMB 2026 steering chair; ISMB 2026 MLCSB | ML |
| Michael Love | UNC | GBCC 2025 (Session 4 chair); EuroBioC sibling; RNA-seq stats | Tools-Viz-Infra / Functional Genomics |
| Charlotte Soneson | FMI / Basel | GBCC 2025 keynote 2; EuroBioC 2025 (footprintR) | Tools-Viz-Infra |
| Lambda Moses | Caltech | GBCC 2025 (Session 3 chair); Voyager; spatial-omics infra | Spatial |
| Sehyun Oh | CUNY | GBCC 2025 (Session 1 chair) | Tools-Viz-Infra |
| Marinka Zitnik | Harvard | GI 2025 keynote 2; therapeutic-graph FMs | ML (if invited again) |
| Yana Safonova | Penn State | GI 2025 keynote 1; adaptive immune repertoire | Algorithmics / Functional Genomics |
| Tuuli Lappalainen | NYGC / KTH | ISMB 2026; statistical genetics + functional genomics | PopGen / Functional Genomics |
| Alkes Price | Harvard Chan | PRS at scale; statistical genetics | PopGen |
| Adam Siepel | CSHL home turf | CSHL-resident; phylogenetic / population-genetic models | PopGen / Algorithmics |
| Ben Raphael | Princeton | RECOMB 2026 (3 papers); cancer evolution + spatial | Spatial / Functional Genomics |

### Tools / methods likely to be presented (with sibling-vault links)

| Tool / method | Domain | Sibling-vault page | Expected BDS 2026 angle |
|---|---|---|---|
| **Cuttlefish 3** | pangenome indexing | RECOMB 2026 paper #49 | release talk or follow-on benchmark |
| **SpatialData** | spatial-omics framework | EuroBioC 2025 SpatialData entry | Python + R interop update |
| **Voyager** | spatial-omics SpatialFeatureExperiment | GBCC 2025 (Lambda Moses) | spatial-graph methods extension |
| **DESpace / spatialFDA** | spatial DE | EuroBioC 2025 DESpace / spatialFDA | post-EuroBioC follow-on |
| **OSTA** | spatial book / curriculum | EuroBioC 2025 OSTA workshop | possible book-launch retrospective |
| **Borzoi / Enformer-class** | regulatory deep learning | ISMB 2026 MLCSB; AACR 2026 FM dossier | next-gen successor talk |
| **Geneformer / scGPT / scFoundation** | single-cell FM | AACR 2026 FM dossier; ISMB 2026; RECOMB 2026 | scaling + downstream-task benchmarks |
| **VG / GBZ / PGGB** | pangenome graphs | RECOMB-Seq 2026 satellite | T2T-pangenome reference panel updates |
| **Galaxy MCP / agentic-AI agents** | bioinformatics agents | GBCC 2025 (GalaxyMCP); ISMB 2026 BOSC | cross-platform agent benchmark |
| **PRS-CSx / SBayesRC-class** | multi-ancestry PRS | (new — not yet in corpus) | new sibling-vault entry candidate |
| **MAGeCK successors / CRISPR-screen** | perturbation stats | (new — not yet in corpus) | new sibling-vault entry candidate |
| **JBrowse 3** | genome viewer | (new — not yet in corpus) | infra-track candidate |

### Cross-vault link targets (concrete)

When BDS 2026 tool pages get scaffolded post-meeting, the following inbound/outbound links should be checked:

- **EuroBioC 2025** (`../eurobioc-2025/tools/`) — every spatial-omics talk; every Bioconductor-package-update talk.
- **GBCC 2025** (`../gbcc-2025/`) — every Galaxy-infra talk; every Bioc-to-Galaxy wrapping update; Schatz / Williams / Soneson sibling appearances.
- **RECOMB 2026** (`../recomb-2026/tools/`) — every Algorithmics talk (pangenome, sequence indexing); every ML talk (foundation models, protein/RNA ML); every Spatial talk (MOSAICField / DIME / LineageMap follow-ons).
- **ISMB 2026** (`../ismb-2026/`) — MLCSB co-publications; BOSC tool-release co-announcements; Troyanskaya keynote spillover.
- **Nextflow Summit 2026** (`../nextflow-2026/`) — every Tools/Viz/Infra pipeline-framework talk; every cloud-native infrastructure talk.
- **AACR 2026** (`../aacr-2026/`) — every Spatial talk (Visium HD analysis, histopathology FMs); every FM talk (downstream cancer-research applications); every ML-for-regulatory talk with cancer-context examples.
- **JPM 2026** (`../jpm-2026/`) — sparse overlap, but Seqera Platform / DNAnexus-adjacent infrastructure talks may name-drop platforms covered there.

## Pre-meeting checklist

- [ ] **Sep 2026:** when the BDS 2026 program drops, populate `_program-extracted.md` (working file) with the session-by-session schedule + speaker list.
- [ ] **Sep–Oct 2026:** preprint sweep — for each oral talk, locate the speaker's most recent bioRxiv preprint. Pre-scaffold tool-page skeletons.
- [ ] **Oct 2026:** keynote announcements typically drop ~6–8 weeks pre-meeting. Update [`index.md`](index.md) when known.
- [ ] **Nov 4–7, 2026:** track #CSHLmeetings on Bluesky/X during the meeting for talk-day reactions. CSHL has no recordings, so social is the only real-time signal.
- [ ] **Nov 8+, 2026:** post-meeting bulk extraction. Cross-vault link sweep. Abstract book PDF backfill.
- [ ] **Dec 2026:** slide-deposit re-sweep (~4 weeks post-meeting). ~30–50% of speakers will have deposited by then.

## Sources (verified May 2026)

- [CSHL Biological Data Science 2026 meeting page](https://meetings.cshl.edu/meetings.aspx?meet=DATA) — primary source for dates, venue, organizers, six sessions.
- [CSHL Genome Informatics 2025 meeting page](https://meetings.cshl.edu/meetings.aspx?meet=info) — reference for prior-year shape.
- [CSHL Meetings homepage (2026 calendar)](https://meetings.cshl.edu/meetings) — confirms no GI 2026 on calendar; BDS holds the Nov slot.
- [CSHL Genetics Meetings 2026/2027](https://meetings.cshl.edu/genetics-meetings) — biennial pattern check.
- [JXTX Foundation scholarships](https://jxtxfoundation.org/scholarships/) — Taylor Foundation grad scholarships available at both GI and BDS.
