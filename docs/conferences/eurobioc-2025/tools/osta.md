# OSTA — Orchestrating Spatial Transcriptomics Analysis with Bioconductor

**Open-source online book and companion data package** — reproducible code examples and end-to-end workflows for spatial-omics analysis using Bioconductor in R, including interoperability with Python; the companion `OSTA.data` package ships example datasets across multiple spatial-omics platforms.

- **Maintainer (data package):** Yixing E. Dong — `estelladong729@gmail.com`
- **Authors:** Helena L. Crowell, Yixing Dong, Ilaria Billato, Peiying Cai, Martin Emons, Lukas Weber, Stephanie Hicks, Ellis Patrick, Mark Robinson, Vince Carey, others
- **Bioconductor (companion data):** [OSTA.data v1.4.0](https://bioconductor.org/packages/release/bioc/html/OSTA.data.html)
- **Book:** [bioconductor.org/books/OSTA/](https://bioconductor.org/books/OSTA/)
- **Source:** [github.com/lmweber/OSTA](https://github.com/lmweber/OSTA)
- **License:** Artistic-2.0
- **Status at EuroBioC2025:** workshop / book in active development

## Workshop at EuroBioC2025

- **Presenters:** Yixing Dong & Ellis Patrick
- **Day / session:** Day 2 (Thu Sep 18, 2025) — afternoon hands-on workshop (parallel with mia, msqrob2, Workshop Platform, iSEE)
- **Workshop title:** "OSTA: Orchestrating Spatial Transcriptomics Analysis with Bioconductor"
- **Format:** hands-on tutorial walking through book chapters using `OSTA.data` example datasets
- **Workshop materials:** [github.com/lmweber/OSTA](https://github.com/lmweber/OSTA) and [bioconductor.org/books/OSTA/](https://bioconductor.org/books/OSTA/)
- **Video:** workshops not recorded; the Bioconductor YouTube playlist covers plenaries only
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

OSTA is an online textbook (in the OSCA / OHCA tradition) that walks through spatial-transcriptomics analysis end-to-end on the Bioconductor stack — preprocessing, QC, normalization, clustering, spatially-variable-gene detection, cell-type deconvolution, and cross-language interop with Python. The companion `OSTA.data` Bioconductor package provides the example datasets across multiple spatial-omics platforms (Visium, Xenium, MERFISH, etc.) so every chapter is runnable.

## How it works

**Core idea.** OSTA is a Quarto-rendered book, not a package — its "mechanism" is editorial: it organizes the spatial-transcriptomics workflow into six parts (Background, Sequencing-based platforms, Imaging-based platforms, Platform-independent analyses, Multiple-sample analyses, Cross-platform analyses) so that the same dataset can be carried through preprocessing → QC → normalization → dimensionality reduction → clustering → spatial statistics → deconvolution → cell-cell communication chapters.

**Inputs / outputs.** Input for the reader: an R session with Bioconductor (the book reports being compiled on Bioconductor 3.23 / R 4.6.0). Input for the chapters: example datasets shipped by the `OSTA.data` companion package, loaded by name so every chapter is runnable without external downloads. Output: a `SpatialExperiment` (or platform-specific subclass) carried across chapters as the running object.

**Key innovation.** The book/data-package split is the operational design: chapters reference datasets by stable identifier, `OSTA.data` ships those datasets versioned on Bioconductor, and a Python-interop section bridges to the SpatialData / scverse stack so the book can teach R-side analysis without pretending the rest of the ecosystem doesn't exist. Splitting code (chapter) from data (package) keeps the book reproducible across Bioc releases.

**Parameters worth knowing.** Reader-facing decisions are mostly per-chapter (which clustering algorithm, which SVG method, which normalization). At the book level: which platform substrate to follow — sequencing-based (Visium / Visium HD) or imaging-based (Xenium, CosMx) — since the two halves diverge on QC and segmentation. *MERFISH coverage not confirmed in the current table of contents (book lists Visium, Visium HD, Xenium, CosMx explicitly).*

**Canonical example.** Each chapter pulls a worked dataset from `OSTA.data`; the sequencing-based section is anchored on Visium (including HD with binned and segmented variants), the imaging-based section on Xenium and CosMx. The multi-sample and cross-platform parts then re-use those same objects to demonstrate integration without re-importing raw data.

## Where it fits in the corpus

- **AACR 2026:** axis = single-cell & spatial omics — OSTA is the curricular spine for the R/Bioconductor side of the spatial-omics dossiers
- **DESpace** ([entry](despace.md)) — Peiying Cai is both the DESpace presenter and an OSTA author; OSTA is the natural place a DESpace tutorial would live
- **SpatialData** ([entry](spatialdata.md)) — the Python-side framework that OSTA's interop chapters bridge to
- **Helena Crowell Day 1 keynote** — overlaps directly; Crowell is both a keynote speaker and an OSTA author
- **ISMB 2026:** scaffold; spatial-omics tracks
- **GBCC 2025:** queued

## Notes

OSTA is the consensus textbook around which much of the European spatial-omics Bioconductor work is converging. Tracking OSTA chapter additions is a good proxy for which spatial methods the Bioc community considers stable enough to teach.
