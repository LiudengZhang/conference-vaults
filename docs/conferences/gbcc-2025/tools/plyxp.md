# plyxp

**rlang data masks for SummarizedExperiment** — a Bioconductor package that lets users evaluate dplyr-style unquoted expressions against `SummarizedExperiment` objects across rowData, colData, and assay contexts, without converting to a rectangular `data.frame` first.

- **Maintainer:** Justin T Landis (Love Lab, UNC Chapel Hill) — `jtlandis314@gmail.com`
- **Bioconductor:** [plyxp v1.6.1](https://bioconductor.org/packages/release/bioc/html/plyxp.html)
- **Source:** [github.com/jtlandis/plyxp](https://github.com/jtlandis/plyxp) · [project site](https://jtlandis.github.io/plyxp)
- **Vignettes:** [plyxp intro](https://bioconductor.org/packages/release/bioc/vignettes/plyxp/inst/doc/plyxp.html)
- **License:** MIT
- **Status at GBCC2025:** methods talk on tidy-style SummarizedExperiment manipulation

## Talk at GBCC2025

- **Speakers:** Justin T Landis, Michael I Love (UNC Chapel Hill)
- **Day / session:** Day 4 (Thu Jun 26, 2025) — Oral Session 5, Grace Auditorium (chair: Scott Cain)
- **Talk title:** "plyxp: reimagining dplyr syntax for SummarizedExperiment objects"
- **Slides (Zenodo DOI):** *TBD — Zenodo deposits typically 2–4 weeks post-conference*
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

plyxp uses rlang data masks to make a `SummarizedExperiment` behave like a tidy data context for dplyr verbs — `mutate()`, `filter()`, `summarise()` — across the three logical "frames" of an SE: row metadata, column metadata, and assay matrices. The user keeps the SE structure (no flatten / pivot round-trip) but writes expressions in dplyr syntax. It's a syntactic bridge, not a replacement for the underlying S4 contract.

## How it works

**Core idea.** plyxp wraps a `SummarizedExperiment` in a `plyxp` object that exposes three rlang data masks — one each for the assay matrix, `rowData`, and `colData` — and dispatches standard dplyr verbs so expressions evaluate against the appropriate context without flattening the SE to a tibble.

**Inputs / outputs.** Input is a `SummarizedExperiment` (the vignette uses `airway`). Output is a `plyxp` object that retains the SE structure; `se()` extracts the underlying `SummarizedExperiment` back out when the user is done piping.

**Key innovation.** Context routing inside a single `mutate()`/`filter()` call. Rather than an `@`-prefix grammar, plyxp uses **contextual helper functions**: `rows()` directs an expression to `rowData`, `cols()` directs it to `colData`, and bare expressions operate on the assay matrix — so one piped verb can write to all three frames simultaneously.

**Parameters / API surface worth knowing.**
- `new_plyxp(se)` — constructor wrapping an SE in the plyxp context.
- `rows(...)` / `cols(...)` — helpers that scope expressions to `rowData` / `colData`; bare expressions hit assays.
- Supported verbs: `mutate`, `select`, `summarize`, `pull`, `filter`, `arrange` — standard dplyr API.
- `se()` — accessor that returns the underlying `SummarizedExperiment`.

**Canonical example.** From the vignette: `xp <- new_plyxp(airway); xp |> mutate(log_counts = log1p(counts), cols(treated = dex == "trt"), rows(new_id = paste0("gene-", gene_name)))`. A single piped `mutate()` adds a log-transformed assay, a treatment indicator on `colData`, and a renamed gene ID on `rowData` — three frames updated in one expression.

## Where it fits in the corpus

- **Tidyomics** ([entry](tidyomics.md)) — same axis (tidy syntax for Bioc data classes); plyxp + tidyomics together signal the maturity shift in how Bioc users interact with their data
- **DeeDeeExperiment** ([entry](../../eurobioc-2025/tools/deedeeexperiment.md)) — related "extensions to SummarizedExperiment" pattern; DDE adds result-table slots, plyxp adds expression-language ergonomics — orthogonal but composable
- **AACR 2026:** plumbing rather than science; relevant insofar as AACR analysts increasingly hand off SE/SCE objects in tidy-friendly form
- **ISMB 2026:** scaffold

## Notes

Mike Love's group (UNC) is bridging Bioconductor's S4 world to dplyr / tidyverse syntax — plyxp is the SummarizedExperiment-specific surface, and Tidyomics is the broader umbrella. Together they signal a maturity shift: Bioc data classes are the ground truth, but the user-facing language is the tidyverse. Mature package (Bioconductor 3.23, v1.6.1).
