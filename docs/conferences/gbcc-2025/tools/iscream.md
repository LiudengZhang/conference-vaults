# iscream

**Fast, memory-efficient BED file queries** — a Bioconductor package with an Rcpp + htslib backend for querying compressed BED files and returning results as data frames, `GenomicRanges`, or matrices. The performance angle (vs. Rsamtools / native R parsers) is the headline.

- **Maintainer:** James Eapen (Van Andel Institute) — `james.eapen@vai.org`
- **Authors:** James Eapen (author/creator), Jacob Morrison (author), Nathan Spix (contributor), Hui Shen (author, supervisor, funding)
- **Bioconductor:** [iscream v1.2.0](https://bioconductor.org/packages/release/bioc/html/iscream.html)
- **Source:** [github.com/huishenlab/iscream](https://github.com/huishenlab/iscream)
- **Vignettes:** [Introduction](https://bioconductor.org/packages/release/bioc/vignettes/iscream/inst/doc/iscream.html) · [HTSlib guide](https://bioconductor.org/packages/release/bioc/vignettes/iscream/inst/doc/htslib.html) · [Performance](https://bioconductor.org/packages/release/bioc/vignettes/iscream/inst/doc/performance.html) · [Data structures](https://bioconductor.org/packages/release/bioc/vignettes/iscream/inst/doc/data_structures.html) · [Comparison with Rsamtools](https://bioconductor.org/packages/release/bioc/vignettes/iscream/inst/doc/tabix.html) · [TSS methylation](https://bioconductor.org/packages/release/bioc/vignettes/iscream/inst/doc/TSS.html)
- **License:** MIT
- **Status at GBCC2025:** lightning talk on a low-level BED query engine

## Talk at GBCC2025

- **Speaker:** James Eapen (Van Andel Institute)
- **Day / session:** Day 3 — lightning talks
- **Talk title:** "iscream: fast and efficient BED file queries"
- **Slides:** *to verify after publish*
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

iscream wraps htslib's tabix-indexed BED reader in Rcpp and exposes a query API that returns either a tibble, a `GenomicRanges` object, or a numeric matrix (e.g. methylation calls per region × sample) without round-tripping through R-level text parsers. The `tabix` vignette benchmarks against Rsamtools; the `TSS` vignette demonstrates the end-use case (per-TSS methylation matrices across many samples) where the throughput difference matters.

## How it works

**Core idea.** iscream binds htslib through Rcpp so that tabix-indexed BED queries run in C++ and parse directly into native R structures, skipping the R-level text-parsing step that dominates Rsamtools-based workflows. It compiles against Rhtslib by default but performs best when linked to htslib built with libdeflate.

**Inputs / outputs.** Input is one or more tabix-indexed, gzip-compressed BED (or BED-like) files plus a set of query regions. Output can be a `data.table`, a `GRanges`, a `RangedSummarizedExperiment`, a sparse matrix, or a `BSseq` object — chosen via the function called.

**Key innovation.** Multi-file tabix querying in a single call: unlike Rsamtools, which operates on one file at a time, iscream accepts a vector of BED files and returns parsed results in one shot — exactly the shape needed for building region × sample matrices across hundreds of methylation BEDs.

**Parameters worth knowing.**
- `tabix()` / `tabix_gr()` — query regions across multiple files, returning a `data.table` or `GRanges`.
- `summarize_regions()` — aggregate per-region statistics (mean, sum, median, variance) without first materializing the full table.
- `make_mat()` / `make_mat_se()` — assemble dense or sparse matrices with loci as rows and files as columns.
- Threading control — operations support parallel execution via a configurable thread count.

**Canonical example.** The vignette lists a directory of single-cell methylation BEDs (`cell[1-5].bed.gz`) and queries two regions:
```r
bedfiles <- list.files(data_dir, pattern = "cell[1-5].bed.gz$", full.names = TRUE)
regions  <- c("chr1:184577-680065", "chrY:56877780-56882524")
tabix_gr(bedfiles, regions, col.names = c("beta", "coverage"))
summarize_regions(bedfiles, regions, columns = c(4, 5), col_names = c("beta", "coverage"))
```

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo-tools (infrastructure layer; relevant to any methylation / ChIP / ATAC dossier that builds region × sample matrices)
- **Bioc-to-Galaxy** ([entry](bioc-to-galaxy.md)) — performance-critical Bioc tools are exactly the class that benefits from being wrapped as Galaxy workflow steps for non-R users
- **EuroBioC 2025:** not presented
- **Nextflow Summit 2026:** not mentioned

## Notes

The Rcpp + htslib backend signals a performance-focused tool, fitting alongside other low-level Bioc utilities (Rsamtools, GenomicFiles, VariantAnnotation). For methylation pipelines at VAI scale, the speedup likely matters most when assembling per-region matrices across hundreds of samples — the canonical tabix-bottleneck shape.
