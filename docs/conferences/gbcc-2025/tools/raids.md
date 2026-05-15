# RAIDS

**Robust Ancestry Inference using Data Synthesis** — a Bioconductor package for genetic-ancestry inference from cancer-derived molecular data (RNA-seq, exome, whole-genome), using synthetic-cancer-data augmentation to keep the inference stable on the kinds of fragmented, low-coverage samples that break standard PCA-projection pipelines.

- **Maintainer:** Pascal Belleau (Cold Spring Harbor Laboratory / Krasnitz Lab) — `pascal_belleau@hotmail.com`
- **Bioconductor:** [RAIDS v1.10.0](https://bioconductor.org/packages/release/bioc/html/RAIDS.html)
- **Source:** [github.com/KrasnitzLab/RAIDS](https://github.com/KrasnitzLab/RAIDS) · [project site](https://krasnitzlab.github.io/RAIDS/)
- **Vignettes:** [Robust Ancestry Inference using Data Synthesis](https://bioconductor.org/packages/release/bioc/vignettes/RAIDS/inst/doc/RAIDS.html) · Population reference GDS files · Wrapper functions
- **License:** Apache License (>= 2)
- **Status at GBCC2025:** methods talk on robust ancestry inference

## Talk at GBCC2025

- **Speakers:** Pascal Belleau, Xintong Li, Astrid Deschênes, et al. (Krasnitz Lab, CSHL)
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2B, Grace Auditorium (chair: Vincent Carey)
- **Talk title:** "Robust ancestry inference from challenging human molecular data with RAIDS"
- **Slides (Zenodo DOI):** *TBD — Zenodo deposits typically 2–4 weeks post-conference*
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

RAIDS infers genetic ancestry from cancer sequencing data — RNA-seq, exome, WGS — without requiring matched germline sequencing. The "data synthesis" angle is the differentiator: rather than projecting samples onto a 1000G PCA and hoping the variant calls survive low coverage, RAIDS synthesizes cancer-like reference data and uses it to anchor a more robust inference. That makes it usable on the kinds of inputs (FFPE exomes, shallow tumor RNA-seq) that biobank- and TCGA-style retrospective cohorts actually have.

## How it works

**Core idea.** RAIDS generates *synthetic* genotype profiles for reference-panel donors that mimic the coverage and noise characteristics of the target sample, then projects the target onto the reference PCA and classifies its ancestry against those synthetics — so the inference parameters (PC count, k-NN window) are tuned on profiles that look like the actual data, not on idealized reference genotypes.

**Inputs / outputs.** Input is germline-overlapping reads or genotype calls at variant positions with sufficient coverage and population frequency, plus a population reference dataset (1000 Genomes is the canonical panel). Output is an ancestry classification, ancestry probabilities, and a profile-specific accuracy estimate.

**Key innovation.** Profile-specific inference parameter optimization via data synthesis — RAIDS uses synthetic profiles built from reference donors to estimate per-sample accuracy and pick parameters, instead of using one global setting for all inputs. This is what makes the method robust on cancer-derived, low-coverage, or fragmented data.

**Parameters worth knowing.**
- Reference panel selection — determines which ancestral backgrounds can be assigned.
- Coverage threshold — minimum read depth per variant for inclusion.
- Variant frequency cutoff — restricts inference to common population variants.
- PCA projection dimensionality — number of principal components retained.

**Canonical example.** The vignette walks through setting up a working directory with the population-reference GDS files, sampling reference donors to generate synthetic profiles, optimizing inference parameters on those synthetics, running ancestry inference on the target, and inspecting the resulting calls and accuracy estimates. The accompanying Belleau et al. 2023 *Cancer Research* paper benchmarks the approach on TCGA samples.

## Where it fits in the corpus

- **AACR 2026:** axis clinical-trials / translational-genomics — ancestry-aware QC is a prerequisite for fair biomarker discovery across diverse cohorts
- **ISMB 2026:** scaffold; population-genetics / cancer-genomics overlap
- **RECOMB 2026:** scaffold
- **Nextflow Summit 2026:** not mentioned (but RAIDS is the kind of step that lives inside a Nextflow tumor-only QC pipeline)

## Notes

Robust to "challenging" inputs is the point — the talk title's framing matches the package's design intent. CSHL hosting GBCC2025 makes this a hometown talk for the Krasnitz lab. For biobank-scale cancer-genomics work, ancestry inference from tumor-only data is a real bottleneck, and RAIDS is one of the few packages explicitly built for it.
