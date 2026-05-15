# consICA

**Consensus Independent Component Analysis** — data-driven deconvolution method using consensus ICA to decompose heterogeneous omics data and extract features for patient diagnostics and prognostics.

- **Maintainer:** Petr V. Nazarov — `petr.nazarov@lih.lu`
- **Bioconductor:** [consICA v2.10.0](https://bioconductor.org/packages/release/bioc/html/consICA.html)
- **Source:** [git.bioconductor.org/packages/consICA](https://git.bioconductor.org/packages/consICA)
- **Vignettes:** [consICA introduction](https://bioconductor.org/packages/release/bioc/vignettes/consICA/inst/doc/ConsICA.html)
- **License:** MIT
- **Status at EuroBioC2025:** methods talk on signal decomposition for omics deconvolution

## Talk at EuroBioC2025

- **Speaker:** Maryna Chepeleva (presented; Nazarov is the maintainer / senior author)
- **Day / session:** Day 2 (Thu Sep 18, 2025) — late-morning short-talk session, before the Ferruz keynote
- **Talk title:** "consICA for functional signal decomposition"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

consICA runs Independent Component Analysis many times with different initializations, then aggregates the results into stable consensus components — the "consensus" step is what turns ICA from a stochastic exploratory method into a reproducible deconvolution tool. The output is a set of statistically independent signal components extracted from heterogeneous omics data, with downstream utilities for linking components to patient survival, clinical covariates, and gene-set enrichment.

## How it works

**Core idea.** Run fastICA `ntry` times with different random initializations on the same expression matrix, then aggregate the per-run components into stable "consensus" components — a standard remedy for the well-known non-determinism of single-run ICA. The aggregation step (matching components across runs and averaging) is what turns ICA from an exploratory tool into a reproducible deconvolution method.

**Inputs / outputs.** Input: a `SummarizedExperiment` carrying an expression matrix (genes × samples), sample metadata, and optionally survival time/event columns. Output: an `S` matrix of consensus metagenes (genes × components), an `M` matrix of component weights per sample (components × samples), and per-component stability scores; downstream utilities link components to survival, clinical covariates, and gene-set enrichment.

**Key innovation.** The consensus criterion — components from independent runs that match consistently across initializations are kept; unstable components are flagged or discarded — is the methodological signature. Components are then explicitly framed as deconvolution signals to be tested against clinical metadata and pathway databases rather than treated as black-box features.

**Parameters worth knowing.** `ncomp` — the number of independent components to extract (analyst-chosen, the primary modeling decision). `ntry` — how many ICA restarts to aggregate (more restarts → more stable consensus, more compute). Sample metadata columns to test against (`Var`) and survival columns drive the downstream component-interpretation tooling. *Specific aggregation algorithm not detailed in the vignette excerpt accessed.*

**Canonical example.** The vignette uses TCGA skin cutaneous melanoma (SKCM) — 472 samples × the 2,454 most variable genes, plus 103 metadata columns and survival data — pre-loaded as a `SummarizedExperiment` via `data("samples_data")`. Consensus components are then linked to melanoma subtype and survival as the worked example.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; relevant axis is bioinfo / AI methods — consICA complements PCA/NMF/omicsGMF dimensionality reduction with an ICA-based alternative
- **omicsGMF** ([entry](omicsgmf.md)) — adjacent matrix-factorization framing, different statistical assumptions
- **ISMB 2026:** scaffold
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** not mentioned

## Notes

ICA-based deconvolution — explicitly oriented toward extracting clinically interpretable signal components, with the consensus step addressing the standard ICA reproducibility concern.
