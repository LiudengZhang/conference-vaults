# Themes & takeaways — EuroBioC 2025

Cross-day synthesis of the recurring threads, surprises, and named entities across [Day 1](digest/day-1.md), [Day 2](digest/day-2.md), and [Day 3](digest/day-3.md). EuroBioC 2025 was a 3-day, ~5-keynote / ~25-short-talk / 5-workshop event in Barcelona — the European leg of the Bioconductor calendar, tighter and more methodological than the joint GBCC counterpart. The themes below are what the program *converges on* once you read the schedule as one document rather than three.

> **Source caveat:** Plenary recordings are public on the Bioconductor YouTube playlist; short-talk slides typically land on Zenodo within a few weeks but were largely TBD at recap time. Claims below are anchored to talk titles, package READMEs, and the official community recap — recordings will tighten the specifics.

---

## The five threads

### 1. Spatial-omics convergence

The single loudest thread of the meeting. The European Bioconductor scene is consolidating fast around spatial methods, and Day 2 was where it surfaced as a coordinated stack:

- **[Helena Crowell's Day 1 keynote](keynotes/crowell.md)** anchored the case for whole-transcriptome imaging in colorectal cancer.
- **[SpatialData](tools/spatialdata.md)** (Marconato) provides a Python-primary data structure with an in-development R interop layer — the meeting's clearest acknowledgment that spatial data formats are now cross-language by default.
- **[DESpace](tools/despace.md)** (Cai) layers spatial differential expression on top of edgeR's NB machinery — i.e., a classical Bioconductor workhorse extended with spatial context.
- **[spatialFDA](tools/spatialfda.md)** (Emons) pushes the same problem into the multi-sample regime where clinical use lives.
- **[OSTA](tools/osta.md)** (Day 2 workshop) — the *Orchestrating Spatial Transcriptomics Analysis* book, taught in person, locks the curriculum.

Five contributions, four different speakers, one consistent direction. This is what Bioconductor convergence actually looks like in real time.

### 2. Cross-language interop as a first-class concern

Two talks foregrounded language bridges in their *titles*, not as footnotes:

- **[SpectriPy](tools/spectripy.md)** (Rainer) — explicit R↔Python mass-spec interop, named for the bridge.
- **[SpatialData](tools/spatialdata.md)** — Python-primary, R interop *in development*, openly acknowledged.

The implicit version of the same thread runs through the [Workshop Platform](tools/workshop-platform.md) (containerized environments that don't care which language), [Metabonaut](tools/metabonaut.md) (a tutorial framework that has to interoperate with SpectriPy), and the broader pattern of Python-primary frameworks (anndata, scanpy, MuData) that the R-side is increasingly mirroring rather than competing with. The Bioconductor stance has shifted from "we are the R ecosystem" to "we are the R-anchored interoperable ecosystem."

### 3. Latent-variable / dimensionality-reduction methods proliferate

Statistically, this was the year's centerpiece — and it was visible across both days:

- **[Susan Holmes' keynote](keynotes/holmes.md)** — *Latent variables as the best medicine for heterogeneity* — argued the methodological frame head-on.
- **[omicsGMF](tools/omicsgmf.md)** (Clement) — generalized matrix factorization usable across modalities.
- **[consICA](tools/consica.md)** (Chepeleva) — independent-component analysis with a consensus / stability layer.

Three contributions, three different angles (latent factor models, GMF, ICA), one common claim: when the biology is heterogeneous, the right primitive is a latent representation. Pair this with the spatial track and the picture sharpens — spatial heterogeneity is heterogeneity, and the same tools apply.

### 4. Proteomics renaissance from the Clement lineage

A quieter but striking thread: multiple proteomics-flavored tools traceable to Lieven Clement's group, with complementary roles:

- **[omicsGMF](tools/omicsgmf.md)** (Clement himself, Day 1) — dimensionality reduction.
- **[msqrob2](tools/msqrob2.md)** (Vanderaa, Day 2 workshop) — robust statistical proteomics, the workhorse downstream of search engines.
- Lucas Beerland's distributional-inference single-cell proteomics talk (skipped from the tools index but in the program) — the experimental frontier of the same lineage.

Bioconductor proteomics is having a moment, and one Belgian group is producing much of the gravitational mass. This complements the metabolomics track ([notame](tools/notame.md), [Metabonaut](tools/metabonaut.md), [SpectriPy](tools/spectripy.md)) — the small-molecule side is healthy too.

### 5. Workshop Platform + BiocBook = the meta-infrastructure

The most strategic thread runs *underneath* the talks:

- **[Workshop Platform](tools/workshop-platform.md)** (Mahmoud, Day 2 workshop) — the containerized environment that runs all the workshops in the room, deployable as a per-event service.
- **[Jacques Serizay's Day 3 keynote](keynotes/serizay.md)** — community-driven flexible software, BiocBook, the ecosystem-as-coordination-mechanism argument.
- **[OSTA](tools/osta.md)** as a *book* taught as a *workshop* on a *platform* — the three layers compose.

The closing argument of the meeting is that the value Bioconductor delivers is not packages, it's the *production line that turns research into a reproducible, shareable, runnable artifact*. Workshop Platform is to a workshop what BiocBook is to a vignette is to a peer-reviewed package — three rungs on the same ladder.

---

## Surprises worth flagging

| Surprise | Day | Why it stood out |
|---|---|---|
| **Five distinct spatial-omics tools across two days** | 1 + 2 | The European scene is now coordinating on spatial, not competing |
| **SpatialData as a Python-primary "Bioconductor" talk** | 2 | Explicit acknowledgment that the data-structure standard isn't R-only |
| **SpectriPy named for its language bridge** | 1 | Cross-language interop is a *title-worthy* contribution now |
| **Holmes keynote framing latent variables as "medicine"** | 1 | Methodological argument, not a results talk — the rhetorical centerpiece |
| **edgeR still getting a methods-talk slot 20 years in** | 1 | The classical workhorses are not done; Lizhong Chen's update went alongside the new spatial-DE tools |
| **Workshop Platform as a *workshop* about workshops** | 2 | The infrastructure-of-infrastructure show, quietly the most leveraged talk in the room |
| **No agentic-AI / LLM track at all** | all | In contrast to Nextflow Summit 2026; see "notably absent" below |

---

## Tools, keynotes & entities — quick index

| Item | Day 1 | Day 2 | Day 3 |
|---|:-:|:-:|:-:|
| [Vince Carey — 25 years of Bioconductor](keynotes/carey.md) | ✓ | | |
| [Helena Crowell — CRC imaging](keynotes/crowell.md) | ✓ | | |
| [Susan Holmes — latent variables](keynotes/holmes.md) | ✓ | | |
| [James Sharpe — C3PO](keynotes/sharpe.md) | | ✓ | |
| [Noelia Ferruz — protein LMs](keynotes/ferruz.md) | | ✓ | |
| [Jacques Serizay — community software](keynotes/serizay.md) | | | ✓ |
| [notame](tools/notame.md) | ✓ | | |
| [Metabonaut](tools/metabonaut.md) | ✓ | | |
| [SpectriPy](tools/spectripy.md) | ✓ | | |
| [omicsGMF](tools/omicsgmf.md) | ✓ | | |
| [miaTime](tools/miatime.md) | ✓ | | |
| [RCX](tools/rcx.md) | ✓ | | |
| [MIRit](tools/mirit.md) | ✓ | | |
| [DeeDeeExperiment](tools/deedeeexperiment.md) | ✓ | | |
| [edgeR](tools/edger.md) | ✓ | | |
| [MOSClip](tools/mosclip.md) | ✓ | | |
| [Rega](tools/rega.md) | ✓ | | |
| [footprintR](tools/footprintr.md) | | ✓ | |
| [decemedip](tools/decemedip.md) | | ✓ | |
| [SpatialData](tools/spatialdata.md) | | ✓ | |
| [DESpace](tools/despace.md) | | ✓ | |
| [spatialFDA](tools/spatialfda.md) | | ✓ | |
| [consICA](tools/consica.md) | | ✓ | |
| [barbieQ](tools/barbieq.md) | | ✓ | |
| [OSTA](tools/osta.md) | | ✓ | |
| [mia](tools/mia.md) | | ✓ | |
| [msqrob2](tools/msqrob2.md) | | ✓ | |
| [Workshop Platform](tools/workshop-platform.md) | | ✓ | |
| [iSEE](tools/isee.md) | | ✓ | |

**Speakers / institutions named in the program:** Vince Carey (Channing/Harvard), Helena Crowell (CNAG), Susan Holmes (Stanford), James Sharpe (EMBL Barcelona), Noelia Ferruz (CSIC), Jacques Serizay (Institut Pasteur), Lieven Clement (Ghent), Christophe Vanderaa (Ghent), Charlotte Soneson (FMI/SIB), Federico Marini (Mainz), Luca Marconato (EMBL), Tuomas Borman (Turku), Johannes Rainer (Eurac), Alexandru Mahmoud (Bioconductor core), and the short-talk roster captured in the [tools index](tools/index.md).

**Domains represented:** spatial omics, single-cell, microbiome, mass spec / metabolomics, proteomics, RNA-seq, miRNA-mRNA, multi-omics survival, methylation, networks, clonal tracking, EGA submission, visualization, infrastructure / data classes, books / training.

---

## What's notably absent

- **No agentic-AI / LLM-driven-pipeline track.** The Nextflow Summit 2026 vault is dominated by [agentic AI threads](../nextflow-2026/themes.md) — Co-Scientist, MCP-per-pipeline, LLM-driven QC rewrites. EuroBioC 2025 has *one* AI keynote (Ferruz on protein design) and effectively zero short talks on agentic tooling for Bioconductor itself. Striking, given the topic's gravity elsewhere; an opening for BioC2026.
- **Light on benchmarks-of-benchmarks.** Most short talks present *new* tools; few revisit the comparative-benchmark genre that the AACR / ISMB methods circuits have been pushing. The Bioconductor review process front-loads this work into vignettes, but a session-format methods-comparison track is missing.

---

## Where the corpus connects

- **AACR 2026 ([../aacr-2026/](../aacr-2026/index.md))** — the bioinfo-tools and single-cell/spatial-omics topics share a substantial subset of the spatial stack here ([SpatialData](tools/spatialdata.md), [DESpace](tools/despace.md), [OSTA](tools/osta.md)). When AACR speakers cite "we used SpatialExperiment / SpatialData" — this is the meeting where the underlying tooling got versioned.
- **Nextflow Summit 2026 ([../nextflow-2026/](../nextflow-2026/index.md))** — opposite framing: Nextflow is pipelines / orchestration / agents, EuroBioC is methods / packages / statistics. The two are complementary halves of the bioinformatics stack — Nextflow ships the spatial-preprocessing pipeline, Bioconductor ships the spatial-DE method that consumes its output. The contrast on agentic AI (heavy at Nextflow, near-absent here) is the most legible cross-vault signal.
- **GBCC 2025** (queued sister vault) — the Galaxy + Bioconductor joint event. The OSTA / mia / iSEE workshops in particular will likely show up there in re-taught form; cross-linking once GBCC is populated.
- **JPM 2026 ([../jpm-2026/](../jpm-2026/themes.md))** — distant from this vault on content but worth noting that the Crowell-keynote disease focus (CRC, whole-transcriptome imaging) sits in a space that AI-pharma announcements are starting to circle (multi-modal foundation models for oncology — see Modella AI). Methods first, then deals.

---

## Caveat

EuroBioC 2025 has a public schedule, public plenary recordings, and a public community recap; short-talk slides land on Zenodo on a multi-week lag. This synthesis is built from titles + package documentation + the recap blog, with a small number of inferences explicitly flagged ("the talk title suggests…"). Recordings should be the source of truth where the precise methodological claim matters.
