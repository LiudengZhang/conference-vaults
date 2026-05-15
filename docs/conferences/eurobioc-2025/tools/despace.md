# DESpace

**Discover spatially variable genes and differential spatial patterns across conditions** — a Bioconductor framework that uses negative binomial modeling (via edgeR) on pre-annotated spatial clusters to detect (a) genes whose expression varies across tissue space within a sample and (b) genes whose spatial expression *pattern* differs between experimental conditions.

- **Maintainer:** Peiying Cai (University of Zurich) — `peiying.cai@uzh.ch`
- **Bioconductor:** [DESpace v2.4.0](https://bioconductor.org/packages/release/bioc/html/DESpace.html)
- **Source:** [github.com/peicai/DESpace](https://github.com/peicai/DESpace)
- **Vignettes:** [Spatially variable genes (SVG)](https://bioconductor.org/packages/release/bioc/vignettes/DESpace/inst/doc/SVG.html) · [Differential spatial patterns (DSP)](https://bioconductor.org/packages/release/bioc/vignettes/DESpace/inst/doc/DSP.html)
- **License:** GPL-3
- **Status at EuroBioC2025:** methods talk on the differential-spatial-patterns (DSP) capability

## Talk at EuroBioC2025

- **Speaker:** Peiying Cai (University of Zurich)
- **Day / session:** Day 2 (Thu Sep 18, 2025) — morning short-talk session, before the Ferruz keynote
- **Talk title:** "DESpace for differential spatial patterns detection"
- **Slides (Zenodo DOI):** *to verify after publish — Bioconductor speakers typically deposit within ~2 weeks of the meeting*
- **Video:** not recorded — short talks at EuroBioC2025 were not part of the plenary YouTube playlist
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

DESpace takes spatial-transcriptomics counts plus a pre-annotated spatial cluster label (from any clustering pipeline) and asks two questions: (1) which genes vary significantly in expression across the spatial clusters within a single sample (SVG mode), and (2) which genes show *different* spatial expression patterns between conditions or samples (DSP mode). The DSP capability — the focus of the EuroBioC2025 talk — treats "pattern" as a first-class statistical object rather than running gene-by-gene SV testing per condition and post-hoc comparing.

## How it works

**Core idea.** Fit a negative-binomial GLM (via `edgeR`) to gene-level counts using the pre-annotated spatial cluster label as a covariate. For SVG mode, significance of the cluster term identifies genes whose expression varies across tissue space; for DSP mode, an interaction term between cluster and condition flags genes whose *spatial pattern* differs across experimental groups.

**Inputs / outputs.** Input: a `SpatialExperiment` with raw counts, spatial coordinates, a spatial-cluster column (from any external clustering — BayesSpace, Banksy, manual annotation), and — for DSP — condition and sample columns. Output: a ranked table of SVG or DSP genes with p-values/FDR, plus per-cluster contributions that show which spatial regions drive the signal.

**Key innovation.** Reframes SVG detection as a familiar NB-GLM problem rather than a Gaussian-process or moment-statistic problem, which makes it faster than most SV methods and gives joint multi-sample fitting "for free." The DSP framing — testing the cluster × condition interaction directly — is the explicit differentiator from running SV tests per condition and post-hoc comparing. Vignettes cite BayesSpace and Banksy as upstream clustering substrates rather than head-to-head competitors.

**Parameters worth knowing.** `cluster_col` — name of the spatial-cluster covariate (analysis is conditional on this annotation being sensible). `coordinates` — spatial coordinate columns. `replicates` — toggles multi-sample joint fitting versus per-sample SVG calls. Gene-detection filter (e.g. ≥20 cells) controls which genes enter the model.

**Canonical example.** SVG vignette: human DLPFC Visium (three donors, manual layer annotations) — DESpace ranks genes by their across-layer variation and returns the laminar marker set. DSP vignette: Stereo-seq axolotl telencephalon regeneration at 2/10/20 days post-injury (two sections each) with Banksy clusters partitioning the tissue into five compartments, and the cluster × DPI interaction identifies genes whose spatial layout changes over the regeneration time course.

## Where it fits in the corpus

- **AACR 2026:** no direct dossier; relevant axis is single-cell & spatial omics — DESpace is a methodological complement to the foundation-model-based spatial dossiers (Cell2Location, etc.) in the AACR vault
- **ISMB 2026:** scaffold; likely overlap on spatial-method talks
- **RECOMB 2026:** scaffold
- **GBCC 2025:** queued — possible overlap if Cai also presented there
- **Nextflow Summit 2026:** not mentioned

## Notes

Mature package (v2.4.0 in Bioconductor 3.23). Negative-binomial modeling via edgeR is a familiar substrate to the Bioconductor audience — that choice plus the explicit DSP framing is what differentiates DESpace from purely SVG-focused methods.
