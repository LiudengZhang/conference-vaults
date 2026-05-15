# DeeDeeExperiment

**An S4 class for managing and exploring omics analysis results** — extends `SingleCellExperiment` with dedicated slots for storing differential-expression and functional-enrichment outputs alongside the data they came from, so a downstream user can ship one object instead of a folder of CSVs.

- **Maintainer:** Najla Abassi (IMBEI Mainz) — `abassi.nejla96@gmail.com`
- **Bioconductor:** [DeeDeeExperiment v1.2.0](https://bioconductor.org/packages/release/bioc/html/DeeDeeExperiment.html)
- **Source:** [github.com/imbeimainz/DeeDeeExperiment](https://github.com/imbeimainz/DeeDeeExperiment)
- **Vignettes:** [User's Guide](https://bioconductor.org/packages/release/bioc/vignettes/DeeDeeExperiment/inst/doc/DeeDeeExperiment_manual.html) · [With single-cell data](https://bioconductor.org/packages/release/bioc/vignettes/DeeDeeExperiment/inst/doc/dde_with_single_cell.html)
- **License:** MIT
- **Status at EuroBioC2025:** new release (Bioconductor 3.23, v1.2.0) — first major conference presentation

## Talk at EuroBioC2025

- **Speaker:** Najla Abassi (IMBEI Mainz)
- **Day / session:** Day 1 (Wed Sep 17, 2025) — afternoon short-talk session, after the Susan Holmes keynote
- **Talk title:** "DeeDeeExperiment class for omics analysis results"
- **Slides:** [Zenodo 10.5281/zenodo.17184376](https://zenodo.org/records/17184376)
- **Video:** not recorded — short talks were not part of the plenary YouTube playlist
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

DeeDeeExperiment is a thin extension on top of `SingleCellExperiment` that adds dedicated, schema-validated slots for differential-expression results (e.g. DESeq2, edgeR, limma output tables) and functional-enrichment results (e.g. GSEA, ORA). Instead of a downstream user keeping the SCE alongside loose result `data.frame`s, everything travels together in one object — which makes apps like iSEE, gating pipelines, and reproducibility wrappers trivially aware of "what tests were run on this data."

## How it works

**Core idea.** `DeeDeeExperiment` is an S4 class that inherits from `SingleCellExperiment`, adding named slots for DEA (differential expression) and FEA (functional enrichment) result tables — so the result objects ride inside the same container as the counts, `colData`, `rowData`, and reduced dimensions they were derived from.

**Inputs / outputs.** Construction takes an existing `SingleCellExperiment` plus a named list of result tables; the returned `DeeDeeExperiment` preserves every SCE component and exposes the results through dedicated accessors. Downstream tools that already speak SCE (iSEE, scran, scater) keep working unchanged.

**Key innovation.** A schema-validated, single-object contract for DEA/FEA results. Prior practice scattered result `data.frame`s as loose files alongside the SCE; DeeDeeExperiment standardizes the contract so consumers can introspect what tests were run without bespoke parsing.

**Parameters / API surface worth knowing.**
- `DeeDeeExperiment(sce = ..., de_results = ...)` — constructor; accepts an SCE plus a named list of DEA tables.
- `getDEA()`, `getDEANames()` — accessors that retrieve named DEA result tables (analogous accessors exist for FEA).
- Expected single-cell `colData` columns when working with pseudobulk: `sample_id`, `cluster_id`, `group_id`.
- Naming convention for results: `"contrast_celltype"` (e.g. `"stim-ctrl_NK cells"`), so per-cluster contrasts are addressable by name.

**Canonical example.** The single-cell vignette walks SCE → QC with scater → `prepSCE()` → pseudobulk via muscat's `aggregateData()` and `pbDS()` → conversion with `muscat_list_for_dde()` → `dde <- DeeDeeExperiment(sce = sce, de_results = muscat_list)`. The resulting object is then queried with `getDEA()` / `getDEANames()` to inspect contrasts by cell type.

## Where it fits in the corpus

- **AACR 2026:** no current dossier — this is plumbing rather than science; relevant if any AACR talk uses iSEE / SCE infrastructure to ship results
- **iSEE** ([entry](isee.md)) — natural consumer; DDE's DEA/FEA slots are exactly the result shape that iSEE custom panels could surface
- **ISMB 2026:** scaffold
- **GBCC 2025:** queued — IMBEI Mainz is an active workshop contributor at both events
- **Nextflow Summit 2026:** conceptually adjacent (single-object shipping is also a Nextflow design pattern); no direct mention in the Nextflow vault

## Notes

The kind of package that's invisible until you don't have it. Bioconductor has long had `SingleCellExperiment` as the canonical container, but result-level schema (DEA / FEA outputs) has been ad-hoc — every downstream tool reinvents its own contract. DeeDeeExperiment is a bet that standardizing that schema unlocks better composability — Federico Marini's iSEE workshop on Day 2 is a natural consumer.
