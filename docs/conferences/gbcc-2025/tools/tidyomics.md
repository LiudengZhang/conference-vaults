# Tidyomics

**Tidy-syntax ecosystem for Bioconductor data classes** — a meta-package umbrella (~10 member packages) that lets analysts use dplyr / tidyverse verbs directly on `SummarizedExperiment`, `SingleCellExperiment`, `SpatialExperiment`, and `Seurat` objects without converting away from the canonical S4 representation. The GBCC2025 talk pitches Tidyomics as the substrate for democratizing Human Cell Atlas–scale single-cell analysis.

- **Lead author:** Stefano Mangiola (Adelaide University) — `mangiolastefano@gmail.com`
- **Co-authors:** Michael Love (UNC), William Hutchison, plus broader tidyomics community
- **Ecosystem hub:** [tidyomics on Bioconductor](https://bioconductor.org/packages/release/bioc/html/tidyomics.html) (umbrella, v1.8.0) plus member packages: tidySingleCellExperiment, tidybulk, tidySummarizedExperiment, tidyseurat, tidySpatialExperiment, plyranges (each on Bioconductor)
- **Source:** [github.com/tidyomics/tidyomics](https://github.com/tidyomics/tidyomics)
- **License:** MIT
- **Status at GBCC2025:** ecosystem talk spanning multiple constituent packages

## Talk at GBCC2025

- **Speaker:** Stefano Mangiola (Adelaide University)
- **Day / session:** Day 3 — Oral Session 4 (chair: Mike Love), talk #6; plus a Day 3 lightning-talk teaser
- **Talk title:** "Democratising the Analysis of the Human Cell Atlas with Bioconductor" (Oral 4 #6)
- **Slides:** *to verify after publish*
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

Tidyomics overloads dplyr/tidyverse verbs (`filter`, `mutate`, `group_by`, `summarise`, `nest`, `pivot_*`, etc.) so they operate directly on Bioconductor S4 containers without first coercing to a data frame. `tidySingleCellExperiment` makes a `SingleCellExperiment` look like a tibble (one row per cell, columns from `colData` + reduced dims), `tidybulk` wraps bulk RNA-seq, `tidySummarizedExperiment` handles the general SE case, `tidyseurat` covers Seurat objects, and `plyranges` provides tidy verbs over `GRanges`. All members share API conventions so a user who learns one transfers fluently to the others. The Mangiola GBCC talk frames this as the ergonomics layer that lets cell-atlas-scale analyses be written and read as readable pipelines.

## How it works

**Core idea.** `tidyomics` is an *umbrella* meta-package: loading it attaches the member packages in one call and guarantees they expose consistent dplyr/tidyverse method dispatch on top of Bioconductor's S4 containers. The S4 object stays the ground truth — tidy verbs are implemented as methods that intercept dispatch and route to the appropriate slot, so no coercion / flatten step is needed.

**Inputs / outputs.** Inputs are unchanged Bioconductor objects (`SummarizedExperiment`, `SingleCellExperiment`, `SpatialExperiment`, `Seurat`, `GRanges`). Outputs are the same objects after verb application — the tibble-like printing is a view, not a representation change.

**Key innovation.** Ecosystem-level coordination. Each member package independently provides a tibble abstraction for its respective S4 class, but they share API conventions and a single install/load entry point, so a user who learns `tidySingleCellExperiment` transfers fluently to `tidySpatialExperiment` or `tidybulk`. The 2024 Nature Methods paper benchmarks this by running a 7.5M-PBMC Human Cell Atlas analysis across six data frameworks and ten tools using shared tidy syntax ([Hutchison, Keyes, Crowell et al., *Nat Methods* 21:1166–1170, 2024](https://www.nature.com/articles/s41592-024-02299-2)).

**Parameters / API surface worth knowing.**
- `library(tidyomics)` — attaches `tidySummarizedExperiment`, `tidySingleCellExperiment`, `tidySpatialExperiment`, `tidyseurat`, `plyranges` (and others) in one call.
- Verb coverage: `filter`, `mutate`, `select`, `group_by`, `summarise`, `nest`, `pivot_*`, plus the package-specific extensions (e.g. `tidybulk`'s differential-expression wrappers).
- Philosophy — "tidy data principles on top of S4 objects": the container is canonical, the syntax is tidyverse.

**Canonical example.** *Not specified in vignette* (the umbrella package's own page mainly orchestrates loading); member-package vignettes carry the worked examples — e.g. `tidySingleCellExperiment` lets a user write `sce |> filter(cell_type == "T cell") |> ggplot(aes(UMAP_1, UMAP_2)) + geom_point()` directly on an SCE.

## Where it fits in the corpus

- **AACR 2026:** axes = single-cell-spatial-omics + bioinfo-tools (any AACR talk that ships an SCE / SE result is a candidate downstream user)
- **plyxp** ([entry](plyxp.md)) — both bridge Bioc S4 containers to dplyr-style syntax; plyxp is the newer, lazier `SummarizedExperiment` companion. Tidyomics is the umbrella; plyxp is a specific evaluation strategy in the same lineage
- **EuroBioC 2025:** not a dedicated talk, but tidyomics packages are referenced throughout the schedule
- **Nextflow Summit 2026:** not mentioned (R-side ecosystem)

## Notes

Tidyomics is a meta-ecosystem covered by a single vault page; constituent packages get dedicated pages only if they carried their own talks. The GBCC framing — "Democratising the Analysis of the Human Cell Atlas" — places this work alongside the cross-platform / cross-language integration storylines that anchor the joint Galaxy-Bioconductor event.
