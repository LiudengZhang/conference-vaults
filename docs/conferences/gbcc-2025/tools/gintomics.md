# gINTomics

**Multi-omics data integration and visualization** — a Bioconductor package that identifies associations between a target gene's expression and its regulatory factors (Copy Number Variations, methylation), bundling the integration models with a Shiny app for interactive exploration of the results.

- **Maintainer:** Angelo Velle (University of Padua) — `angelo.velle@unipd.it`
- **Bioconductor:** [gINTomics v1.8.0](https://bioconductor.org/packages/release/bioc/html/gINTomics.html)
- **Source:** [github.com/angelovelle96/gINTomics](https://github.com/angelovelle96/gINTomics)
- **Vignettes:** [gINTomics intro](https://bioconductor.org/packages/release/bioc/vignettes/gINTomics/inst/doc/gINTomics.html)
- **License:** AGPL-3
- **Status at GBCC2025:** methods talk on multi-omics integration

## Talk at GBCC2025

- **Speakers:** Angelo Velle, Francesco Patanè, Chiara Romualdi (University of Padua)
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2A, Bush Hall (chair: Jenny Drnevich)
- **Talk title:** "gINTomics, a powerful Bioconductor package for multiomics data integration and visualization"
- **Slides (Zenodo DOI):** *TBD — Zenodo deposits typically 2–4 weeks post-conference*
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

gINTomics ties expression data to its regulatory layer — CNV and methylation — and tests for associations gene by gene. The output is a per-target model surfaced through a Shiny-based app, so the integration step and the visualization step ship together rather than expecting the user to wire one to the other. The Romualdi lab's positioning is "powerful + visual" rather than "novel statistics."

## How it works

**Core idea.** For each target gene, gINTomics fits a regression of expression against its candidate regulators — CNV at the gene locus, methylation, miRNAs, and TFs — choosing a negative-binomial model for RNA-seq counts or a linear model for microarray / continuous data. When the regulator set is large, a random-forest pre-selection prunes to the most important covariates before the regression is fit.

**Inputs / outputs.** Inputs are a `MultiAssayExperiment` carrying any combination of gene expression (RNA-seq or microarray), miRNA expression, methylation, gene CNV, and miRNA CNV. Regulator dictionaries are pulled automatically: TF–target and miRNA–target relations via `OmnipathR`, TF–miRNA via `TransmiR`. Output is a per-target list of integration models, which is then fed directly into the Shiny visualization layer.

**Key innovation.** Pairing the integration step with a packaged Shiny app surfaced by `run_shiny()` — so the same object that holds the regression results is also the input the GUI consumes, rather than requiring the analyst to bridge between modeling output and a separate visualization stack.

**Parameters worth knowing.**
- Data-type switch — model family flips between negative binomial (counts) and linear (microarray); chosen from input type.
- Regulator-dictionary source — `OmnipathR` for TF / miRNA targets, `TransmiR` for TF→miRNA edges; affects which covariates enter each gene's model.
- Random-forest pre-selection — engaged when the regulator count is high; trims covariates before regression. Exact threshold *not specified in vignette; needs talk slides*.

**Canonical example.** The vignette loads `mmultiassay_ov`, a 20-patient TCGA ovarian-cancer `MultiAssayExperiment` carrying expression, miRNA, methylation, and gene/miRNA CNV. Users extract the individual matrices, rebuild a clean `MultiAssayExperiment`, and run `run_multiomics()` to fit the integration models; the resulting object is passed directly to `run_shiny()` to launch the interactive viewer.

## Where it fits in the corpus

- **AACR 2026:** axis bioinfo / AI methods — gINTomics is one of the multi-omics-integration tools relevant to the cancer-genomics dossiers
- **MOSClip** ([entry](../../eurobioc-2025/tools/mosclip.md)) — same lab family; both are multi-omics integration packages, but MOSClip is survival-focused while gINTomics is regulator-association-focused with explicit visualization
- **ISMB 2026:** scaffold
- **Nextflow Summit 2026:** not mentioned

## Notes

Mature package (Bioconductor 3.23, v1.8.0). The differentiator versus MOSClip and the broader multi-omics ecosystem is the embedded Shiny app — Romualdi's group is consolidating an "integration + interactive exploration" workflow rather than shipping a bare modeling library.
