# spatialLIBD

**Interactive visualization and analysis of spatially-resolved transcriptomics in R/Bioconductor** — LIBD's data + Shiny package for the human DLPFC Visium atlas and the surrounding infrastructure for adapting `SpatialExperiment` workflows to Visium HD.

- **Maintainer:** Leonardo Collado-Torres (LIBD) — `lcolladotor@gmail.com`
- **Key contributor (Visium HD work):** Nicholas J. Eagles (LIBD)
- **Bioconductor:** [spatialLIBD](https://www.bioconductor.org/packages/release/data/experiment/html/spatialLIBD.html)
- **Source:** [github.com/LieberInstitute/spatialLIBD](https://github.com/LieberInstitute/spatialLIBD)
- **Project site:** [research.libd.org/spatialLIBD](https://research.libd.org/spatialLIBD/)
- **Paper:** [Pardo et al., *BMC Genomics* 2022](https://link.springer.com/article/10.1186/s12864-022-08601-w)
- **License:** Artistic-2.0
- **Status at GBCC2025:** methods/perspective talk on extending the package to Visium HD

## Talk at GBCC2025

- **Speakers:** Nicholas J. Eagles, Sarah E. Maguire, et al. (Lieber Institute for Brain Development)
- **Day / session:** Day 3 (Wed Jun 25, 2025) — Oral Session 3, Grace Auditorium (chair: Lambda Moses)
- **Talk title:** "Computational considerations for analysis of Visium HD: A Bioconductor user's perspective"
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

spatialLIBD ships the LIBD DLPFC Visium dataset and an accompanying Shiny app for interactive layer-annotation, gene-expression overlay, and cluster comparison on `SpatialExperiment` objects. The Day-3 GBCC talk is about the *Visium HD* transition — Visium HD's 2-µm bins explode the data-volume and memory cost vs. classic 55-µm spots, and the talk walks through the practical Bioconductor-side adaptations (binning strategies, memory-mapped backends, plotting at scale) needed to keep the workflow tractable.

## How it works

**Core idea.** spatialLIBD is a `golem`-structured Shiny application backed by `SpatialExperiment` objects: the SE carries counts, spot coordinates, and image tiles, and the Shiny layer exposes interactive overlays (cluster labels, gene expression, layer annotations) on top of the histology image.

**Inputs / outputs.** Input is a `SpatialExperiment` (≥ 1.3.3) — typically built from 10x Genomics Visium SpaceRanger output — plus optional reference annotations (manual layer labels, registration coordinates). Output is the running Shiny app for interactive exploration, plus publication-quality static figures via `ggplot2` / `plotly` / `cowplot` and downstream cluster/annotation tables.

**Key innovation.** Pairing the LIBD human DLPFC Visium reference atlas with a reusable visualization app: the same `run_app()` machinery used for the DLPFC dataset is the substrate any new spatial dataset can plug into, so a lab gets the LIBD-style explorer for its own Visium data by supplying its own SpatialExperiment.

**Parameters / API surface worth knowing.**
- `run_app()` — launches the Shiny explorer against a supplied `SpatialExperiment`.
- `vis_gene()` / `vis_clus()` — static spot-overlay plotting for gene expression or cluster labels.
- Spatial-registration helpers (per the "Guide to Spatial Registration" vignette) for aligning new datasets to the LIBD reference.
- Multi-gene plotting helpers (per the "Guide to Multi-Gene Plots" vignette).

**Canonical example.** From the intro vignette: pull the LIBD DLPFC `SpatialExperiment` via `fetch_data()`, then `run_app(sce)` to open the interactive explorer — users can overlay any gene's expression on the H&E image, toggle between manually annotated cortical layers, and compare cluster assignments across samples. The Visium HD talk extends this pattern with binning and memory-aware backends for the 2-µm grid.

## Where it fits in the corpus

- **AACR 2026:** axis = single-cell & spatial omics; Visium HD adoption is one of the operative storylines for spatial-omics dossiers
- **OSTA** ([eurobioc entry](../../eurobioc-2025/tools/osta.md)) — both target spatial transcriptomics; OSTA is the book, spatialLIBD is one of the canonical case-study packages
- **SpatialData** ([eurobioc entry](../../eurobioc-2025/tools/spatialdata.md)) — Python-side spatial framework; the Visium HD scaling pressure is shared
- **EuroBioC 2025:** no direct Visium HD counterpart talk on the schedule
- **Nextflow Summit 2026:** not mentioned

## Notes

The talk frames "what changes when bins get small" as a Bioconductor-user problem rather than a new method — pragmatic, useful for anyone migrating an existing spatialLIBD pipeline to HD.
