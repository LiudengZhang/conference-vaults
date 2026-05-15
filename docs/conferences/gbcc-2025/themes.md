# Themes & takeaways — GBCC 2025

Cross-day synthesis of the recurring threads, surprises, and named entities across [Day 2](digest/day-2.md), [Day 3](digest/day-3.md), and [Day 4](digest/day-4.md) (Day 1 was arrival-only). GBCC 2025 was the first-ever joint Galaxy + Bioconductor Community Conference — a 4-day, 3-keynote / 53-oral-talk / 11-lightning-talk / 10-workshop / 50+-poster / 2-day-CoFest meeting at Cold Spring Harbor — and the themes below are what the program *converges on* once you read the schedule as one document rather than four. The single most important thing about the meeting is that it was joint at all: the rest follows from that.

> **Source caveat:** Plenary recordings are referenced as a "GBCC2025 YouTube playlist" in the meeting report, but the playlist URL was not surfaced in the current crawl. Slides typically land on Zenodo within a few weeks. The CSHL-hosted abstract-book PDF returned 404 at fetch time, so the full lightning-talk lineup and several methods-talk package anchors are still TBD. Claims below are anchored to talk titles, package READMEs, the Galaxy June 2025 newsletter recap, and the Bioconductor "Bringing Bioconductor to Galaxy" CoFest blog post.

---

## The five threads

### 1. The "joint" rationale — Bioc-into-Galaxy as the load-bearing story

The single thread that distinguishes GBCC from EuroBioC, and the one that makes "GBCC" a coherent conference rather than two co-located meetings:

- **[bioc-to-galaxy](tools/bioc-to-galaxy.md)** (Joshi, Cumbo, Blankenberg, Day 2 / Oral 1 #3) — the automatic R/Bioconductor → Galaxy wrapping pipeline that the rest of the joint thread depends on.
- **anvi'o auto-wrapping case study** (Cumbo, Joshi, Blankenberg, Day 2 / Oral 2A #8) — the same pipeline applied end-to-end to a non-trivial software suite.
- **Bioconductor-R-Shiny-on-Galaxy** (Videm, Zierep, Day 2 / Oral 2A #12) — the inverse direction: keep R-side interactive analytics, run them inside Galaxy.
- **Daniel Blankenberg's Day 3 workshop** — *Streamlining Bioinformatics: Adding Bioconductor Tools in Galaxy* — the workshop-form of the same pipeline, a precursor to the CoFest.
- **[GSVA→Galaxy](tools/gsva-galaxy.md)** (Cumbo, Joshi, Raubenolt, Blankenberg + on-site Doyle, Yagudayeva, Soneson, Ramos Pérez; CoFest, Jun 27–28) — the *concrete shipped wrapper* that the entire thread builds toward.

Five contributions across four days that all describe one workflow: a Bioconductor package becomes a Galaxy tool. The CoFest GSVA wrapper is the proof-of-concept that the pipeline actually works end-to-end. Without this thread, GBCC is just two conferences sharing a venue; with it, "joint" is a research artifact.

### 2. AI-augmented analysis arrives in the workflow ecosystem

A clear inflection in 2025: AI agents and protocols moved from isolated demos to a coherent axis of platform-level work, especially on the Galaxy side.

- **[Pond's Day-2 keynote](keynotes/pond.md)** — *responsive notebooks, in-the-browser computation, and AI-assisted development* — frames the whole axis as a triad.
- **[GAIA](tools/gaia.md)** (Qiu, Goecks, Day 2 / Oral 1 #1) — natural-language interface across Galaxy instances.
- **[GalaxyMCP](tools/galaxymcp.md)** (Baker, Qiu, Goecks, Schatz, Day 2 / Oral 1 #2) — Model Context Protocol for Galaxy, the open hook external AI assistants plug into.
- **[Galaxy-ML2](tools/galaxy-ml2.md)** (Lyra Junior, Qiu, Day 2 / Oral 2A #6) — best-practices-encoded ML toolkit.
- **AI-augmented data analyses in Galaxy** (Qiu, Goecks, Day 2 / Oral 2A #3) — likely a GAIA extension; the doubling-down within the same session is itself the signal.
- **anvi'o + AI-driven automation** (Cumbo et al., Day 2 / Oral 2A #8) — AI in the wrapping pipeline itself, not just in user-facing analysis.

The contrast with EuroBioC 2025 is the single sharpest cross-vault signal: EuroBioC has *one* AI keynote ([Ferruz on protein design ↗](../eurobioc-2025/keynotes/ferruz.md)) and effectively zero short talks on agentic tooling for Bioconductor itself. GBCC has six AI-adjacent contributions and a keynote, and most of them are on the Galaxy side. The Galaxy ecosystem absorbed agentic AI as a 2025 theme; the Bioconductor ecosystem largely did not — and that asymmetry is one of the most interesting things visible only when you read both vaults together.

### 3. Tidyverse-for-Bioconductor matures

Mike Love's group is consolidating a tidy interface to S4 data classes, and the meeting put both arms of it on stage:

- **[Tidyomics](tools/tidyomics.md)** (Mangiola, Day 3 / Lightning + Oral 4 #6) — the ecosystem (tidySingleCellExperiment, tidybulk, tidySpatialExperiment, …) that wraps S4 omics objects in a dplyr-shaped API.
- **[plyxp](tools/plyxp.md)** (Landis, Love, Day 4 / Oral 5 #1) — *reimagining dplyr syntax for SummarizedExperiment objects* — a separate but adjacent take on the same idea.
- **Mike Love chairs the Day 3 community session**, where Mangiola gives the tidyomics talk — the chairing assignment is itself a coordination signal.

Pair this with EuroBioC 2025's [DeeDeeExperiment ↗](../eurobioc-2025/tools/deedeeexperiment.md) (Abassi) and [edgeR ↗](../eurobioc-2025/tools/edger.md) (Chen) and a clean picture emerges: the European leg shipped infrastructure / data-class extensions, the joint US leg shipped the tidy-API layer on top. Two events, one direction of travel.

### 4. Spatial-omics axis converges with EuroBioC — same European community, two events

GBCC's spatial track is small but the speakers are diagnostic:

- **[sosta](tools/sosta.md)** (Gunz, Robinson, Day 3 / Oral 3 #5) — Robinson lab again — the same lineage as [DESpace ↗ EuroBioC](../eurobioc-2025/tools/despace.md) and adjacent to the broader European spatial stack.
- **Ellis Patrick's Day-2 spatial-omics workshop** — strategies for analyzing spatial-omics data, explicitly methodological.
- **Eagles on Visium HD** (Day 3 / Oral 3 #4) — a Bioconductor-user perspective on a new platform; likely SpatialExperiment-extended.
- **Moses on multiscale lung-adenocarcinoma spatial-transcriptomics** (Day 2 / Oral 2B #9) — Voyager / SpatialFeatureExperiment lineage.

Cross-link directly to the much larger EuroBioC spatial stack: [SpatialData ↗](../eurobioc-2025/tools/spatialdata.md), [DESpace ↗](../eurobioc-2025/tools/despace.md), [spatialFDA ↗](../eurobioc-2025/tools/spatialfda.md), [OSTA ↗](../eurobioc-2025/tools/osta.md), and [Crowell's CRC keynote ↗](../eurobioc-2025/keynotes/crowell.md). The same European spatial-omics community is running a 2-conference rotation, and GBCC gets the methods-extension talks (sosta, Visium HD, multiscale LUAD) while EuroBioC gets the data-structure / curriculum / DE-method talks. Read together they're a single research program.

### 5. Cross-vault people overlap — the same calendar, two stops

The most striking pattern when you cross-walk the GBCC and EuroBioC programs by speaker:

| Speaker | GBCC 2025 contribution | EuroBioC 2025 contribution |
|---|---|---|
| **Charlotte Soneson** | [Day 3 keynote](keynotes/soneson.md) — *From classes to community* | footprintR short talk + on-site CoFest support |
| **Stefano Mangiola** | [Tidyomics](tools/tidyomics.md) lightning + Oral 4 #6 | tidyomics-adjacent EuroBioC contribution |
| **Robert Castelo** | [atena](tools/atena.md) lightning + remote CoFest support for [GSVA→Galaxy](tools/gsva-galaxy.md) | EuroBioC presence (atena / GSVA lineage) |
| **Stefania Pirrotta** | [signifinder](tools/signifinder.md) Oral 2B + [mitology](tools/mitology.md) Oral 5 | EuroBioC short talk |
| **Tuomas Borman** | [mia](tools/mia.md) Oral 5 + Day-3 workshop | [mia ↗ EuroBioC](../eurobioc-2025/tools/mia.md) workshop / talk + [miaTime ↗](../eurobioc-2025/tools/miatime.md) |
| **Ilaria Billato** | Oral 3 #2 — histopath + multi-omics | EuroBioC short talk |
| **Marcel Ramos Pérez** | Oral 3 #2 + on-site CoFest | EuroBioC presence |

Seven names with confirmed appearances at both meetings, and almost certainly more once the EuroBioC lineup is fully cross-walked. This is the *same people running the same 2-conference rotation* — and it's why the per-tool pages cross-link both directions: the package versioned at GBCC is often the package re-presented at EuroBioC three months later, by the same maintainer, to a partly different audience.

---

## Surprises worth flagging

| Surprise | Day | Why it stood out |
|---|---|---|
| **Six AI / MCP / agentic-Galaxy contributions** | 2 | Galaxy absorbed agentic AI as a 2025 theme; Bioconductor (per EuroBioC) largely did not |
| **bioc-to-galaxy as a *talk*, a *workshop*, and a *CoFest deliverable*** | 2 + 3 + post-conf | Three rungs on one ladder — the integration story is genuinely engineered |
| **Pirrotta double-bill (signifinder + mitology)** | 2 + 4 | One author, two distinct packages, two days apart |
| **Soneson keynoting GBCC and contributing at EuroBioC** | 3 | The cross-vault rotation is real and visible at the keynote level |
| **Lambda Moses chairing Oral Session 3 *and* presenting in 2B** | 2 + 3 | Voyager / SpatialFeatureExperiment lineage represented twice |
| **Mike Love chairing the community session, not a methods session** | 3 | Tidyomics + plyxp lineage shows up under "community" rather than "Bioconductor packages" — telling about how the project is organizing the tidy-Bioc thread |
| **Galaxy 20th Anniversary celebration is the closing-night party, not a plenary** | 3 evening | Symbolism: the joint conference is itself the deliverable, not a retrospective talk |

---

## Tools, keynotes & entities — quick index

| Item | Day 2 | Day 3 | Day 4 |
|---|:-:|:-:|:-:|
| [Sergei Kosakovsky Pond — interactive genomic analytics](keynotes/pond.md) | x | | |
| [Charlotte Soneson — classes to community](keynotes/soneson.md) | | x | |
| [Jason Williams — conquest of abundance](keynotes/williams.md) | | | x |
| [GAIA](tools/gaia.md) | x | | |
| [GalaxyMCP](tools/galaxymcp.md) | x | | |
| [bioc-to-galaxy](tools/bioc-to-galaxy.md) | x | x | |
| [AnVIL](tools/anvil.md) | x | x | |
| [torch](tools/torch.md) | x | | |
| [Galaxy-ML2](tools/galaxy-ml2.md) | x | | |
| [NOVA](tools/nova.md) | x | | |
| [TPV Broker](tools/tpv-broker.md) | x | | |
| [gINTomics](tools/gintomics.md) | x | | |
| [RAIDS](tools/raids.md) | x | | |
| [signifinder](tools/signifinder.md) | x | | |
| [SEMplR](tools/semplr.md) | x | | |
| [Meta-iPep](tools/meta-ipep.md) | x | | |
| [HiFi-MAG](tools/hifi-mag.md) | x | | |
| [iscream](tools/iscream.md) | | x | |
| [atena](tools/atena.md) | | x | |
| [Tidyomics](tools/tidyomics.md) | | x | |
| [IWC](tools/iwc.md) | | x | |
| [sosta](tools/sosta.md) | | x | |
| [mia](tools/mia.md) | | x | x |
| [plyxp](tools/plyxp.md) | | | x |
| [mitology](tools/mitology.md) | | | x |
| [FAIR-EASE](tools/fair-ease.md) | | | x |
| [GSVA→Galaxy](tools/gsva-galaxy.md) | | | post-conf |

**Speakers / institutions named in the program:** Sergei Kosakovsky Pond (Temple), Charlotte Soneson (FMI), Jason Williams (CSHL), Jeremy Goecks / Junhao Qiu (Cleveland Clinic / OHSU lineage), Mike Schatz / Dannon Baker (JHU), Daniel Blankenberg / Fabio Cumbo / Jayadev Joshi (Cleveland Clinic), Marius van den Beek / John Chilton / Ahmed Awan (Galaxy core), Vincent Carey (Channing/Harvard), Mike Love / Justin Landis (UNC), Stefano Mangiola (Adelaide), Charlotte Soneson (FMI), Stefania Pirrotta / Enrica Calura (Padova), Robert Castelo (Pompeu Fabra), Tuomas Borman / Leo Lahti (Turku), Lambda Moses (Caltech-adjacent), Mark Robinson / Samuel Gunz (Zürich), Marcel Ramos Pérez / Ilaria Billato (CUNY / Padova), Pascal Belleau / Astrid Deschênes (Roswell Park), Maria Doyle (Limerick), Bryan Raubenolt / Gretta Yagudayeva (Cleveland Clinic CoFest team), and the broader oral / lightning / poster roster captured in [tools/index.md](tools/index.md) and [program-notes.md](program-notes.md).

**Domains represented:** Galaxy infrastructure, AI / MCP / agentic workflows, R↔Galaxy auto-wrapping, ML in workflows, multi-omics integration, microbiome, ancestry inference, cancer signatures, TF-binding variant prediction, mitochondrial activity, spatial omics, histopathology imaging, long-read metagenomics, immunopeptidogenomics, transposable elements, BED-file query infrastructure, tidy-API for SummarizedExperiment, ecology / Earth-system on Galaxy, genome-assembly curation, training / global access (Africa, Canada, Brazil, AnVIL).

---

## What's notably absent

- **No agentic-AI track on the Bioconductor side.** Galaxy got six AI / MCP / Galaxy-ML2 / agentic contributions; Bioconductor R-package talks are essentially AI-free. The same pattern is visible at EuroBioC 2025 ([themes ↗](../eurobioc-2025/themes.md#whats-notably-absent)). A Bioc-side LLM / MCP / agentic-tooling track would be a genuine 2026 opportunity — and the [bioc-to-galaxy](tools/bioc-to-galaxy.md) pipeline is the obvious place for it to land first.
- **No comparative-benchmark session.** GBCC follows the EuroBioC pattern of front-loading benchmarks into vignettes; a dedicated methods-comparison session is missing. Especially noticeable given how many of the package talks (signifinder, RAIDS, sosta, plyxp, gINTomics) make claims that would benefit from a head-to-head against alternatives — the talks describe the new thing but rarely the comparison.

---

## Where the corpus connects

- **EuroBioC 2025 ([../eurobioc-2025/](../eurobioc-2025/index.md))** — the sister vault. Seven speakers overlap (Soneson, Mangiola, Castelo, Pirrotta, Borman, Billato, Ramos Pérez); the spatial stack splits cleanly across the two events (methods-extensions here, data-structures + curriculum there); the tidyverse-for-Bioc thread is consolidated across both. Cross-walk is direction-agnostic — the same package often has pages in both vaults.
- **AACR 2026 ([../aacr-2026/](../aacr-2026/index.md))** — when AACR speakers cite "we used SpatialExperiment / SpatialData / multi-assay infrastructure," GBCC is one of the meetings where the underlying tooling got versioned. The histopath × multi-omics / Visium HD / cancer-signature thread (signifinder, mitology, gINTomics, RAIDS) is the cleanest cross-vault content link.
- **Nextflow Summit 2026 ([../nextflow-2026/](../nextflow-2026/index.md))** — the contrast vault. Nextflow is pipelines / orchestration / agents; GBCC's Galaxy side is the same surface area from a different engine. The agentic-AI thread (GAIA, GalaxyMCP, Galaxy-ML2) is conceptually adjacent to Nextflow's Co-Scientist / MCP-per-pipeline / LLM-driven-QC threads — same problem, two communities, different toolchains. The seam to watch is which papers cite which.
- **JPM 2026 ([../jpm-2026/](../jpm-2026/themes.md))** — distant on content but worth noting that the AnVIL / cloud-genomics / training-equity thread (Mosher Day-2 oral, Williams Day-4 keynote, Kucher Day-3 community talk) sits adjacent to the AI-pharma announcements that JPM circles around. Methods first, deals later.

---

## Caveat

GBCC 2025 has a public schedule, a public scientific-program page with every oral talk listed, a Galaxy newsletter recap, and a Bioconductor blog CoFest recap. What's missing from the current crawl: the YouTube playlist URL, the abstract-book PDF (404 at fetch time), Zenodo-deposited slides (typically 2–4 weeks post-conference), and the full lightning-talk roster (only 5 of 11 names surfaced). This synthesis is built from titles + package documentation + the two recap sources, with abstract-book-gated facts explicitly flagged as TBD.
