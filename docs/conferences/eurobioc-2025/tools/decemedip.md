# decemedip

**Hierarchical Bayesian modeling for cell type deconvolution of immunoprecipitation-based DNA methylome** — a Bioconductor package that infers relative cell type and tissue abundances from MeDIP-Seq data, and can leverage reference datasets from alternative technologies (microarray, WGBS) to improve deconvolution.

- **Maintainer:** Ning Shen — `ning.shen.wk@gmail.com`
- **Bioconductor:** [decemedip v1.0.0](https://bioconductor.org/packages/release/bioc/html/decemedip.html)
- **Source:** [git.bioconductor.org/packages/decemedip](https://git.bioconductor.org/packages/decemedip)
- **Vignettes:** [How to use decemedip](https://bioconductor.org/packages/release/bioc/vignettes/decemedip/inst/doc/how-to-use-decemedip.html)
- **License:** MIT
- **Status at EuroBioC2025:** new release (v1.0.0)

## Talk at EuroBioC2025

- **Speaker:** Ning Shen
- **Day / session:** Day 2 (Thu Sep 18, 2025) — morning short-talk session, after the Sharpe keynote
- **Talk title:** "decemedip for DNA methylation deconvolution"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded — short talks at EuroBioC2025 were not part of the plenary YouTube playlist
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

decemedip fits a hierarchical Bayesian model to MeDIP-Seq signal to estimate the relative contribution of each reference cell type or tissue in a mixture sample. It can borrow strength from reference panels generated on other methylation platforms (microarray, WGBS), bridging across technologies rather than requiring matched-platform references.

## How it works

**Core idea.** A hierarchical Bayesian model couples a logit-normal prior on the cell-type proportion simplex with a generalized additive model (GAM) that maps fractional methylation level and CpG density to expected MeDIP-Seq read counts. The simplex prior keeps proportions on the unit simplex while letting cell types covary; the GAM absorbs MeDIP-specific enrichment bias.

**Inputs / outputs.** Input: MeDIP-Seq read counts at a fixed CpG-site panel, a reference methylation matrix (fractional methylation for each reference cell type), and per-site CpG-density values. Output: posterior cell-type / tissue proportions with credible intervals, plus MCMC convergence diagnostics (Rhat, effective sample size).

**Key innovation.** Two complementary reference panels are used jointly: ~2,500 cell-type-specific CpG sites (cell-type discrimination) and ~1,000 "anchor" methylation-universal sites (calibration of the read-count-to-methylation curve). The anchor sites let the model learn MeDIP enrichment bias separately from biology, which is what makes references generated on microarray or WGBS usable to deconvolute MeDIP-Seq.

**Parameters worth knowing.** Reference panel selection (`hg19.ref.cts.se` cell-type sites + `hg19.ref.anc.se` anchor sites). MCMC iterations (vignette uses 500 for the toy example; ~2,000 recommended). Prior on the simplex (logit-normal). Choice of cell types in the reference (controls which mixtures the model can resolve).

**Canonical example.** The vignette runs decemedip on a prostate-tumor PDX MeDIP-Seq sample (LuCaP_147CR), producing posterior tissue proportions across 25 reference tissues. Convergence diagnostics confirm the run is stable at the demo iteration count.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; relevant axis is epigenomics — methylation-based deconvolution is a recurring theme in liquid-biopsy / cfDNA work
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** not mentioned

## Notes

First Bioconductor release. The platform-bridging reference design — using microarray or WGBS panels to deconvolute MeDIP-Seq — is the methodological signature and unusual enough to be worth tracking.
