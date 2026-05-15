# omicsGMF

**Generalized matrix factorization for omics dimensionality reduction** — performs matrix factorization for dimensionality reduction, visualization, and imputation of RNA-seq, proteomics, and single-cell omics data without requiring log-transformation, with built-in batch-effect correction via covariate adjustment and missing-value handling.

- **Maintainer:** Alexandre Segers — `alexandresegers@outlook.com`
- **Bioconductor:** [omicsGMF v1.2.0](https://bioconductor.org/packages/release/bioc/html/omicsGMF.html)
- **Source:** [git.bioconductor.org/packages/omicsGMF](https://git.bioconductor.org/packages/omicsGMF)
- **Vignettes:** [Proteomics](https://bioconductor.org/packages/release/bioc/vignettes/omicsGMF/inst/doc/Proteomics-vignette.html) · [RNA-Seq](https://bioconductor.org/packages/release/bioc/vignettes/omicsGMF/inst/doc/RNASeq-vignette.html)
- **License:** Artistic-2.0
- **Status at EuroBioC2025:** methods talk on proteomics-specific application

## Talk at EuroBioC2025

- **Speaker:** Lieven Clement (Ghent University) — senior author
- **Day / session:** Day 1 (Wed Sep 17, 2025) — morning short-talk session, after the Crowell keynote
- **Talk title:** "omicsGMF for proteomics dimensionality reduction"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

omicsGMF takes counts (or intensities) plus a sample-covariate matrix and returns a low-dimensional factorization that simultaneously denoises, imputes, and corrects for known batch covariates. It accepts SummarizedExperiment, SingleCellExperiment, and QFeatures inputs, so it slots cleanly into existing Bioconductor pipelines — RNA-seq, bulk proteomics, single-cell proteomics — without an upstream log step.

## How it works

**Core idea.** Generalized matrix factorization (GMF) on the `sgdGMF` engine: the assay matrix is modeled as the sum of an offset from sample/feature covariates and a low-rank factor product, fit by stochastic gradient descent with adaptive learning rates. The distribution family is user-selectable (e.g. `gaussian()` for log-intensity proteomics, count families for RNA-seq), and missing values are handled natively inside the likelihood rather than imputed upstream.

**Inputs / outputs.** Input: a `SummarizedExperiment` / `SingleCellExperiment` / `QFeatures` with an assay matrix, plus optional sample-level (`X`) and feature-level (`Z`) covariate matrices for batch adjustment. Output: factor scores and loadings stored back on the object, plus per-cell imputed values via `imputeGMF` and a 2-D plot via `plotGMF`.

**Key innovation.** Operates directly on raw counts / non-log intensities (no upstream log transform required), handles missingness inside the model (no prior imputation), and absorbs batch covariates into the factorization itself — three things conventional PCA cannot do simultaneously.

**Parameters worth knowing.** `family` — likelihood (e.g. `gaussian()` for proteomics intensities). `ncomponents` — number of latent factors; pick via `runCVGMF` cross-validation or `calculateRankGMF` (a scree-plot analogue on deviance residuals). `X`, `Z` — sample- and feature-level covariate matrices for batch / known-effect adjustment. `assay.type` — which assay to factorize.

**Canonical example.** Proteomics vignette: simulated Gaussian-distributed proteomics intensities (20 samples × 50 features) with 30% artificial missingness and an injected batch effect. The workflow runs `runCVGMF` over `ncomponents = 1:5` to pick the rank, then `runGMF` to fit the factorization with the batch covariate in `X` — the resulting `plotGMF` shows samples grouped by biology with the batch axis absorbed into the covariate term.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; relevant axis is bioinfo / AI methods
- **GBCC 2025:** queued
- **iSEE** ([entry](isee.md)) — natural visualization substrate for the factorization output

## Notes

Lieven Clement's group (UGent) is a frequent EuroBioC contributor — also behind msqrob2. omicsGMF complements that line of work by being agnostic to the input modality.
