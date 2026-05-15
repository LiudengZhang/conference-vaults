# notame

**Workflow for non-targeted LC-MS metabolic profiling** — a Bioconductor package covering tabular preprocessing, quality control, and uni-/multi-variate analysis of untargeted LC-MS metabolomics data, packaging the recommendations from the *Metabolomics Data Processing and Data Analysis — Current Best Practices* special issue.

- **Maintainer:** Vilhelm Suksi (University of Turku) — `vksuks@utu.fi`
- **Bioconductor:** [notame v1.2.0](https://bioconductor.org/packages/release/bioc/html/notame.html)
- **Source:** [git.bioconductor.org/packages/notame](https://git.bioconductor.org/packages/notame)
- **Vignettes:** [Introduction](https://bioconductor.org/packages/release/vignettes/notame/inst/doc/introduction.html)
- **License:** MIT
- **Status at EuroBioC2025:** methods talk on the package's analysis workflow

## Talk at EuroBioC2025

- **Speaker:** Vilhelm Suksi (University of Turku)
- **Day / session:** Day 1 (Wed Sep 17, 2025) — morning short-talk session, after the Crowell keynote
- **Talk title:** "notame package for LC–MS metabolomics analysis"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

notame is a one-stop workflow for untargeted LC-MS metabolomics: it ingests feature tables, runs QC visualizations and drift correction, performs univariate and multivariate analysis (PCA, PLS-DA, etc.), and emits diagnostic reports — a curated translation of the field's best-practice recommendations into runnable R.

## How it works

**Core idea.** notame layers QC-pooled-sample-aware preprocessing on top of a `SummarizedExperiment`: it models analytical drift per feature with cubic-spline regression fit through the pooled QC injections, then flags features by detection rate and robust dispersion metrics (RSD\*, D-ratio\*) computed on those same QCs. Flagged features are not deleted — they are kept in the object but silently excluded from downstream operations (PCA, imputation, statistics) so the user can audit them.

**Inputs / outputs.** Input: a feature × sample abundance table plus sample metadata identifying pooled QCs and injection order, wrapped in a `SummarizedExperiment`. Output: the same object with drift-corrected assays, per-feature QC flags in `rowData`, missing values imputed (random-forest), and figures / Rmd-style diagnostic reports.

**Key innovation.** The flagging-not-filtering convention plus codifying the *Metabolomics Data Processing — Current Best Practices* recommendations into a single importable pipeline. Drift correction is the cubic-spline-on-QCs approach standard in the field rather than a novel method.

**Parameters worth knowing.** Spline smoothing parameter range (default 0.5–1.5, CV-selected). Detection-rate threshold (default ≥0.5). Robust RSD\* limit (≤0.2 recommended). Robust D-ratio\* limit (≤0.4 recommended).

**Canonical example.** Vignette uses the bundled `toy_notame_set`: call `mark_nas()` to convert zeros to NA, `correct_drift()` for spline-based drift correction, `flag_detection()` / `flag_quality()` to mark poor features against the QC thresholds, then `impute_rf()` for random-forest imputation. The result is a QC-cleaned SummarizedExperiment ready for PCA / PLS-DA.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; relevant axis is bioinfo / AI methods (metabolomics is adjacent to the cancer-metabolism talks)
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** not mentioned

## Notes

Mature workflow package (Bioconductor 3.23, v1.2.0). The value is curation more than novelty — converting consensus best-practice into one importable pipeline.
