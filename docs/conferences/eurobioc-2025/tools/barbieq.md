# barbieQ

**Analyze barcode data from clonal tracking experiments** — statistical tools for barcode count data from cell clonal tracking experiments, where each clone carries a unique inherited barcode; supports preprocessing, statistical testing, and visualization of clone abundance changes under experimental conditions.

- **Maintainer:** Liyang Fei (Peter MacCallum Cancer Centre) — `liyang.fei@petermac.org`
- **Bioconductor:** [barbieQ v1.4.0](https://bioconductor.org/packages/release/bioc/html/barbieQ.html)
- **Source:** [git.bioconductor.org/packages/barbieQ](https://git.bioconductor.org/packages/barbieQ)
- **Vignettes:** [barbieQ introduction](https://bioconductor.org/packages/release/vignettes/barbieQ/inst/doc/barbieQ.html)
- **License:** GPL-3
- **Status at EuroBioC2025:** methods talk on clonal-tracking statistics

## Talk at EuroBioC2025

- **Speaker:** Liyang Fei (Peter MacCallum Cancer Centre)
- **Day / session:** Day 2 (Thu Sep 18, 2025) — late-morning short-talk session, before the Ferruz keynote
- **Talk title:** "barbieQ package for clonal tracking barcode analysis"
- **Slides:** [Zenodo 10.5281/zenodo.17239082](https://zenodo.org/records/17239082)
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

barbieQ ingests barcode count tables from clonal-tracking experiments (lentiviral or CRISPR-based barcode libraries delivered into cell populations), performs preprocessing and quality filtering, runs statistical tests for differential clone abundance across experimental conditions, and visualizes how individual clones expand or contract over time. The package is built around a dedicated barcode-experiment data class so that downstream comparisons stay aware of clone-level structure rather than collapsing to bulk counts.

## How it works

**Core idea.** barbieQ wraps a barcode count matrix in a `SummarizedExperiment`-backed `barbieQ` object, partitions clones into "top" vs. low-abundance tails, and applies regression-based tests for significant clonal change across conditions. The specific distribution family used by `testBarcodeSignif()` is *not specified in vignette; needs talk slides*.

**Inputs / outputs.** Input is a barcode-by-sample count matrix plus a sample-metadata data frame; the vignette example is a 16,603 × 62 monkey HSPC matrix. Output is the augmented `barbieQ` object carrying preprocessing flags (top-barcode tags, automatic transformations), pairwise correlations, and test results.

**Key innovation.** Clonal-tracking-specific workflow rather than re-purposing bulk DE machinery — the object carries a top/bottom-barcode partition through downstream steps, so abundance tests are anchored to clones that have enough support to model rather than to the long tail of singletons.

**Parameters worth knowing.**
- `nSampleThreshold` (in `tagTopBarcodes`) — minimum number of samples a barcode must appear in to qualify as "top"; controls the abundance-tail cut.
- `sampleMetadata` (in `createBarbieQ`) — the condition / time-point design used by downstream tests.
- Automatic transformations on object creation — exact set of transformations *not specified in vignette; needs talk slides*.

**Canonical example.** The vignette builds `exampleBBQ <- createBarbieQ(object = assay(monkeyHSPC), sampleMetadata = colData(monkeyHSPC)$sampleMetadata)`, tags abundant clones with `tagTopBarcodes(barbieQ = exampleBBQ, nSampleThreshold = 6)`, then visualizes the partition with `plotBarcodePareto()` and `plotBarcodeSankey()`. Pairwise QC uses `plotBarcodePairCorrelation()` and `plotSamplePairCorrelation()`; statistical testing for condition-specific abundance change runs through `testBarcodeSignif()`.

## Where it fits in the corpus

- **AACR 2026:** clinical-trials axis — clonal tracking is heavily used for drug-resistance and metastasis lineage analysis, which is core AACR territory
- **ISMB 2026:** scaffold
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** not mentioned (different ecosystem)

## Notes

Cancer-research relevance: clonal tracking sees use in CRISPR screens, drug-resistance studies, and metastasis seeding experiments — direct overlap with AACR's clinical-research lineage analyses, and one of the more clinically-anchored methods talks at EuroBioC2025.
