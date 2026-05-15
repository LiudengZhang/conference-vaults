# spatialFDA

**A tool for spatial multi-sample comparisons** — calculates spatial statistics from `SpatialExperiment` objects using `spatstat`, then compares functions across samples via functional additive models (`refund`); provides exploratory visualizations through functional principal component analysis.

- **Maintainer:** Martin Emons (UZH) — `martin.emons@uzh.ch`
- **Bioconductor:** [spatialFDA v1.4.0](https://bioconductor.org/packages/release/bioc/html/spatialFDA.html)
- **Source:** [git.bioconductor.org/packages/spatialFDA](https://git.bioconductor.org/packages/spatialFDA)
- **Vignettes:** [Diabetes Islet Example](https://bioconductor.org/packages/release/bioc/vignettes/spatialFDA/inst/doc/DiabetesIsletExample.html)
- **License:** GPL (>=3)
- **Status at EuroBioC2025:** methods talk on cross-sample spatial comparison

## Talk at EuroBioC2025

- **Speaker:** Martin Emons (UZH)
- **Day / session:** Day 2 (Thu Sep 18, 2025) — late-morning short-talk session, before the Ferruz keynote
- **Talk title:** "spatialFDA for differential co-localization analysis"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

spatialFDA takes a `SpatialExperiment` and computes spatial summary functions (Ripley's K, pair correlation, mark correlation, etc.) per sample via `spatstat`, then treats each sample's function as a functional observation that can be compared across conditions through functional additive models implemented in `refund`. Functional principal component analysis surfaces the dominant modes of variation across samples, turning "how does co-localization differ between groups?" into a tractable statistical question.

## How it works

**Core idea.** Treat each per-sample spatial summary function (evaluated over a range of radii `r`) as a single functional observation, then fit functional additive mixed models (Goldsmith et al. 2024, via `refund`) that compare entire curves — rather than scalar summaries — across conditions, while functional PCA decomposes the cross-sample variation.

**Inputs / outputs.** Input: a `SpatialExperiment` (or compatible) with single-cell coordinates, cell-type labels, sample/patient identifiers, and condition annotation. Output: per-sample summary-function curves, FDA model fits comparing curves across conditions, fPCA scores and modes of variation, and functional boxplots.

**Key innovation.** The vignette positions spatialFDA against `spicyR`, `GraphCompass`, and `mxfda` and frames the differentiator as "functional comparison over the domain" — i.e. testing the whole curve over `r` instead of collapsing to a scalar (a single L-statistic at one radius, a single neighborhood-enrichment score). This recovers radius-dependent effects (e.g. co-localization that flips sign with distance) that scalar methods miss.

**Parameters worth knowing.** Cell-type pair (which two marks the summary function is computed on). Summary function choice (`Kest`, pair correlation `g`, mark correlation, L) — different functions interrogate different aspects of co-localization. Radius range `r` — controls the spatial scale being tested. Model formula — fixed effects (condition) and random effects (patient/donor) in the `refund` call.

**Canonical example.** Damond et al. (2019) IMC pancreatic-islet diabetes dataset — 12 donors split into healthy versus type-1-diabetic, with 35 markers including α/β/δ secretory cells and CD4+/CD8+ T cells. The pipeline computes pair correlation functions between selected cell-type pairs per donor, fits a functional model with condition as fixed effect, and surfaces radius ranges over which T1D donors show altered immune-cell-to-β-cell spatial relationships. Headline result not made fully explicit in the vignette excerpt; *full result details need talk slides*.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; relevant axis is single-cell & spatial omics — spatialFDA addresses the multi-sample comparison gap that most spatial-omics dossiers in the AACR vault leave open
- **DESpace** ([entry](despace.md)) — cousin tool from the same Zurich orbit, but DESpace targets within/between-cluster SVG/DSP while spatialFDA targets cross-sample functional comparisons
- **ISMB 2026:** scaffold; likely overlap on spatial-method talks
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** not mentioned

## Notes

Functional Data Analysis treatment of spatial co-localization — moves beyond single-sample SVG to multi-sample comparisons, which is where most cancer-spatial cohorts actually live.
