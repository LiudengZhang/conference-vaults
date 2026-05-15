# ATAC-seq bias correction & differential motif accessibility (Wang)

**Bias correction for differential motif-accessibility testing in ATAC-seq** — a methods short-talk at EuroBioC2025 by Jiayi Wang on correcting systematic Tn5-insertion-bias and composition artefacts in ATAC-seq before running motif-accessibility differential tests with chromVAR-style pipelines plus limma-voom.

- **Speaker / lead:** Jiayi Wang (affiliation TBD from slides)
- **Building on:** [chromVAR](https://bioconductor.org/packages/release/bioc/html/chromVAR.html) (Greenleaf-lab motif-accessibility deviations) and the limma-voom pipeline
- **Standalone package:** *no public package name surfaced from the talk title or schedule entry* — methods extension; release status TBD
- **Status at EuroBioC2025:** methods short-talk — work-in-progress, no public package URL yet identified

## Talk at EuroBioC2025

- **Speaker:** Jiayi Wang
- **Day / session:** Day 2 (Thu Sep 18, 2025) — morning short-talk session, 9:30 AM
- **Talk title:** "Bias Correction and Differential Motif Accessibility in ATAC-seq Data"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

ATAC-seq motif-accessibility analyses (chromVAR and successors) compute per-cell or per-sample motif-deviation scores that summarize accessibility at TF binding sites — but those scores inherit several biases (Tn5 sequence preference, GC-content effects, library-composition shifts) that distort the downstream differential test. The Wang EuroBioC2025 talk presents a correction strategy that adjusts these biases before passing the deviation matrix into a limma-voom differential test, with the goal of getting valid effect sizes and FDR control on motif-accessibility changes between conditions.

## How it works

**Core idea.** chromVAR-style motif-accessibility scoring builds, for each TF motif, a "deviation" — observed accessibility at motif-containing peaks vs an expectation derived from GC-content / accessibility-matched background peaks — and normalizes it into a z-score using a permutation null. The Wang correction sits between this deviation matrix and the downstream differential test, adjusting the deviation scores for residual Tn5 sequence preference, GC content, and library-composition effects before passing them into a limma-voom contrast model. *Exact correction model pending speaker's slides / paper.*

**Inputs / outputs.** Input: an ATAC-seq peak × sample (or × cell) count matrix, a motif × peak annotation (e.g., from `motifmatchr`), and sample metadata for the contrast. Output: a corrected motif × sample deviation matrix plus limma-voom differential-accessibility results (effect sizes, moderated t-statistics, FDR) on motif activity between conditions. *Exact output schema pending speaker's slides / paper.*

**Key innovation.** Rather than treating chromVAR's GC-matched background sampling as the whole bias model, the talk argues remaining Tn5 / composition biases still corrupt downstream limma-voom tests and proposes an explicit correction step on the deviation matrix. *Specific correction estimator (regression-based residualization vs reweighting vs other) pending speaker's slides / paper.*

**Parameters worth knowing.** *Pending speaker's slides / paper.* Likely candidates by analogy to the methodological space: background-peak set definition (GC/length matching parameters), choice of bias covariates to regress out (Tn5 k-mer bias track, GC content, peak width, library size), and the limma-voom design / contrast specification.

**Canonical example.** *Pending speaker's slides / paper.* No public package URL or worked dataset was surfaced from the EuroBioC2025 schedule entry or talk title at the time of writing; recheck when the Zenodo DOI or preprint is posted.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo / AI methods (epigenomics); valid differential motif accessibility matters for any cis-regulatory cancer-biology dossier
- **EuroBioC 2025:** complements [footprintR](footprintr.md) (the Soneson-lab ATAC-seq footprinting talk) — both target ATAC-seq downstream rigor
- **chromVAR upstream:** the canonical motif-deviation tool that this work corrects
- **GBCC 2025:** no direct counterpart
- **Nextflow Summit 2026:** not mentioned

## Notes

No standalone package name was confirmed from the EuroBioC2025 schedule entry. The methods are positioned as a correction *applied to existing chromVAR + limma-voom workflows* rather than a new container, so the eventual release form is more likely to be a small bias-correction R package or a set of functions contributed upstream than a new analysis framework. Listed here as a flagged work-in-progress (external / pre-release) until a package URL surfaces.
