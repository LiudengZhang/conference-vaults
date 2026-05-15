# KRSA

**Kinome Random Sampling Analyzer — end-to-end upstream-kinase analysis from PamChip kinome-array data** — an R package and R Shiny application from the Cognitive Disorders Research Lab (CogDisResLab, University of Toledo) that automates peptide filtering, random-sampling permutation analysis, heatmap generation, and kinase-network visualization for PamChip functional-proteomics datasets.

- **Maintainer:** Ali Sajid Imami (University of Toledo)
- **R-universe:** [KRSA on CogDisResLab R-universe](https://cogdisreslab.r-universe.dev/KRSA)
- **Project site:** [cogdisreslab.github.io/KRSA](https://cogdisreslab.github.io/KRSA/)
- **Source:** [github.com/CogDisResLab/KRSA](https://github.com/CogDisResLab/KRSA)
- **Paper:** [Imami et al., *PLOS ONE* 2021](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0260440) — "KRSA: An R package and R Shiny web application for an end-to-end upstream kinase analysis of kinome array data"
- **License:** MIT (per CogDisResLab repos)
- **Status at GBCC2025:** lightning talk (Day 3 lightning session) — opening speaker

## Talk at GBCC2025

- **Speaker:** Ali Sajid Imami (University of Toledo)
- **Day / session:** Day 3 (Wed Jun 25, 2025) — lightning-talks block, 10:30–11:15 AM, Grace Auditorium (opening speaker)
- **Talk title:** Demystifying kinome analysis through a streamlined R package designed for functional proteomics
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/) · [Galaxy June 2025 meeting report](https://galaxyproject.org/news/2025-07-11-june2025-newsletter/)

## What it does

KRSA targets the specific data product of the PamGene PamChip system — a kinome microarray that measures peptide-substrate phosphorylation across hundreds of peptides as a proxy for kinase activity. The package automates the full upstream-kinase-analysis workflow: filtering noisy peptides, running random-sampling permutation tests to identify enriched upstream kinases, generating diagnostic heatmaps, and emitting kinase-network visualizations. The Shiny app makes the same pipeline accessible to wet-lab users who don't want to script R directly. It's a tightly scoped tool — built around one specific functional-proteomics modality — but exhaustive within that scope.

## How it works

**Core idea.** For each candidate upstream kinase, KRSA repeatedly draws random subsets of peptides (matched in size to that kinase's known substrate set) from the full PamChip peptide universe and builds a null distribution of phosphorylation summary statistics, then scores the observed substrate set against that random background.

**Inputs / outputs.** Inputs are (1) raw PamChip kinome-array signal — median peptide-spot intensities across conditions — and (2) a kinase–peptide association file (e.g. from GPS 3.0 or Kinexus Phosphonet) that maps each peptide to its known upstream kinases. Output is a ranked kinase table with mean phosphorylation, SD, and Z-score against the random background, plus peptide heatmaps and a kinase-signaling-network visualization.

**Key innovation.** Random-sampling permutation as the null model: instead of assuming a parametric distribution of peptide-level effects, KRSA bootstraps a background per-kinase by sampling matched-size peptide sets, sidestepping the small-N problem typical of PamChip experiments and providing a Z-score with a directly empirical interpretation.

**Parameters / API surface worth knowing.**
- Number of random-sampling iterations (controls null-distribution resolution).
- Peptide filter thresholds (signal/quality cutoffs before analysis).
- Kinase–peptide mapping database (GPS, Kinexus, or user-supplied).
- Comparison contrast (which experimental conditions to score against each other).

**Canonical example.** From the project documentation: load PamChip median-intensity output → filter low-quality peptides → fit a per-peptide effect across conditions → run KRSA's random-sampling routine against a kinase-peptide table → emit a ranked kinase table with Z-scores plus a network plot showing the implicated signaling cascade. The Shiny app exposes the same pipeline through point-and-click.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo / AI methods; functional-kinome readouts are upstream of any kinase-inhibitor pharmacology dossier
- **EuroBioC 2025:** no direct counterpart on kinome arrays
- **ISMB 2026:** scaffold
- **Nextflow Summit 2026:** not mentioned

## Notes

Imami opened the GBCC2025 lightning-talk session. The Imami group also has `drugfindR` (iLINCS drug-signature screening) under Bioconductor consideration, but the GBCC2025 lightning talk was specifically the kinome/PamChip tool — i.e. KRSA, not drugfindR.
