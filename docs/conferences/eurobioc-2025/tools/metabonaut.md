# Metabonaut

**Exploring and analyzing LC-MS data** — an online tutorial book and end-to-end workflows for LC-MS/MS metabolomics analysis using R/Bioconductor packages. Covers preprocessing, normalization, differential abundance, and annotation; ships a small example LC-MS/MS dataset for reproducible demos.

- **Maintainer:** Philippine Louail (RforMassSpectrometry community)
- **Source / install:** [github.com/rformassspectrometry/metabonaut](https://github.com/rformassspectrometry/metabonaut) · `BiocManager::install("rformassspectrometry/Metabonaut")` (not in Bioconductor release as of 3.23)
- **Website:** [rformassspectrometry.github.io/Metabonaut](https://rformassspectrometry.github.io/Metabonaut/)
- **R-universe:** [rformassspectrometry.r-universe.dev/Metabonaut](https://rformassspectrometry.r-universe.dev/Metabonaut)
- **Status at EuroBioC2025:** external / tutorial book (R-universe distribution)

## Talk at EuroBioC2025

- **Speaker:** Philippine Louail
- **Day / session:** Day 1 (Wed Sep 17, 2025) — morning short-talk session, after the Crowell keynote
- **Talk title:** "Metabonaut tutorials for metabolomics workflows"
- **Slides:** [Zenodo 10.5281/zenodo.17120470](https://zenodo.org/records/17120470)
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

Metabonaut is curriculum-shaped, not a method package: it walks LC-MS/MS metabolomics analysis end-to-end on the Bioconductor mass-spec stack (xcms, MsExperiment, Spectra, MetaboAnnotation, …) — preprocessing, normalization, differential abundance, and compound annotation — with a small example dataset embedded so each chapter is runnable.

## How it works

**Core idea.** The "method" here is the curriculum architecture itself: chapters are composed so that the output object of one chapter is the input of the next, threading a small example LC-MS/MS dataset through the full Bioconductor mass-spec stack from raw `mzML` to annotated metabolite list.

**Inputs / outputs.** Input: a small bundled LC-MS/MS dataset (mzML files) plus a sample metadata table. Output for the learner: a runnable end-to-end notebook covering preprocessing, QC, statistical analysis, and annotation, and the skills to run the same on their own data.

**Key innovation.** Filling the gap between per-package vignettes and a real-world workflow. Each Bioconductor mass-spec package has its own vignette in isolation — Metabonaut sequences them into one continuous pipeline, including the R↔Python crossover via SpectriPy.

**Parameters worth knowing.** *not specified in vignette; needs talk slides* — the book is structured around chapters rather than a parameter surface. Reader-relevant choices are which chapters to skip based on data size and whether to run the SpectriPy/Python-annotation chapter.

**Canonical example.** The book is organized into eight modules: end-to-end workflow overview; dataset investigation; QC and feature selection (notame); large-scale processing with xcms (>4,000 files); annotation-resource curation; LC-MS/MS annotation via SpectriPy; advanced annotation with RuSirius for formula/structure ID; and dataset alignment for integrating new data with existing references. The small embedded LC-MS/MS dataset carries through every chapter so each step is executable in-place.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo / AI methods; metabolomics is adjacent to cancer-metabolism dossiers
- **notame** ([entry](notame.md)) — same LC-MS metabolomics audience and complementary roles (Metabonaut = curriculum, notame = workflow library)
- **SpectriPy** ([entry](spectripy.md)) — same Bioconductor mass-spec subcommunity (Johannes Rainer's group)
- **ISMB 2026:** scaffold
- **GBCC 2025:** queued

## Notes

Sister to notame in role — curriculum, not a method package. Useful as the "where to send a new lab member" link for anyone starting LC-MS metabolomics on the Bioconductor stack.
