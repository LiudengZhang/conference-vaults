# footprintR

**Tools for working with single-molecule footprinting data** — reads base modifications from BAM files or `modkit` output, represents single-molecule footprinting data efficiently as R objects, and provides functions to manipulate and visualize them. Output is a `SummarizedExperiment` with positions × samples and assays for modified/total base counts.

- **Authors:** Charlotte Soneson, Panagiotis Papasaikas, Sebastien Smallwood, Michael Stadler — FMI Basel (Friedrich Miescher Institute)
- **Source / install:** [github.com/fmicompbio/footprintR](https://github.com/fmicompbio/footprintR) · `BiocManager::install("fmicompbio/footprintR")` (not in Bioconductor release as of 3.23)
- **Pkgdown:** [fmicompbio.github.io/footprintR](https://fmicompbio.github.io/footprintR/)
- **Status at EuroBioC2025:** external / GitHub-distributed (Bioconductor submission likely pending)

## Talk at EuroBioC2025

- **Speaker:** Charlotte Soneson (FMI Basel)
- **Day / session:** Day 2 (Thu Sep 18, 2025) — morning short-talk session, after the Sharpe keynote
- **Talk title:** "footprintR for single molecule footprinting data"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded — short talks at EuroBioC2025 were not part of the plenary YouTube playlist
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

footprintR ingests base-modification calls (from BAM files or from `modkit`) and lays them out as a `SummarizedExperiment` keyed by genomic position × sample, with assays for modified and total base counts. From there it provides manipulation and visualization functions tailored to single-molecule footprinting (SMF) experiments — where exogenous methyltransferase footprints reveal TF binding at single-DNA-molecule resolution.

## How it works

**Core idea.** Read per-base modification calls (typically from Oxford Nanopore data processed by `modkit`) into a `SummarizedExperiment` whose rows are genomic positions and columns are samples, with two key assays: `Nmod` (count of modified bases observed at that position in that sample) and `Nvalid` (count of total valid base calls at the same position). Methylation rate per position per sample is then simply `Nmod / Nvalid`, but keeping the two counts separate preserves the coverage information needed for downstream statistics.

**Inputs / outputs.** Input: BAM files with MM/ML modification tags, or a bedMethyl-format file produced by `modkit pileup`. Output: a `SummarizedExperiment` with `rowRanges` of positions, `colData` of samples, and `Nmod` / `Nvalid` assays.

**Key innovation.** Modern Bioconductor-style data class for SMF data — `SummarizedExperiment` rather than bespoke list/array structures — which makes SMF analyses composable with the rest of the Bioconductor ecosystem (e.g. `GenomicRanges` subsetting, `plyranges` operations). Successor in spirit to the older `SingleMoleculeFootprinting` package from the same FMI group, with more modern data structures.

**Parameters worth knowing.** `readBedMethyl()` arguments controlling which modification type to ingest (e.g. 5mC vs 6mA from a multi-mod modkit output). Standard `SummarizedExperiment` subsetting on `rowRanges` to restrict to regions of interest before plotting.

**Canonical example.** The package ships an example `modkit_pileup_1.bed.gz` (accessible via `system.file("extdata", ...)`). Vignette workflow: `readBedMethyl()` loads the bedMethyl file into a `SummarizedExperiment`, `plotRegion()` then visualizes modification rates across a genomic region of interest — the SMF readout that maps TF footprints at single-molecule resolution.

## Where it fits in the corpus

- **AACR 2026:** axis = epigenomics / regulatory genomics; SMF is a niche but powerful TF-binding readout
- **ISMB 2026:** scaffold; epigenomics methods
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** not mentioned — modkit upstream is CLI-based but the analysis side is R

## Notes

Single-molecule footprinting (SMF) reads out TF binding at single-DNA-molecule resolution by exposing chromatin to an exogenous methyltransferase whose footprint marks bound vs. unbound DNA. footprintR sits downstream of `modkit` calls and is complementary to the older `SingleMoleculeFootprinting` package on Bioconductor — same FMI lineage, more modern data structures.
