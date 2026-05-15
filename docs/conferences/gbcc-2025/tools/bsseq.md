# bsseq

**Whole-genome bisulfite and long-read methylation analysis in R/Bioconductor** — the Hansen-lab workhorse for processing, smoothing, and differentially testing methylation from WGBS, and (as of bsseq >=1.45.1) the substrate for allele-specific methylation analysis from Oxford Nanopore long-read sequencing.

- **Maintainer:** Kasper D. Hansen (Johns Hopkins Bloomberg School of Public Health) — `kasperdanielhansen@gmail.com`
- **Bioconductor:** [bsseq](https://bioconductor.org/packages/release/bioc/html/bsseq.html)
- **Source:** [github.com/hansenlab/bsseq](https://github.com/hansenlab/bsseq)
- **Vignettes:** [bsseq Analysis](https://bioconductor.org/packages/release/bioc/vignettes/bsseq/inst/doc/bsseq_analysis.html)
- **Preprint (ASM extension):** [biorxiv 2025.04.30.651558](https://www.biorxiv.org/content/10.1101/2025.04.30.651558v1.full) — "Sample-specific CpG loci are important for accurate long-read methylation analysis"
- **License:** Artistic-2.0
- **Status at GBCC2025:** methods talk on the allele-specific-methylation (ASM) extension from ONT long reads

## Talk at GBCC2025

- **Speaker:** Kasper D. Hansen (Johns Hopkins)
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2B, Grace Auditorium (chair: Vincent Carey)
- **Talk title:** "Analyzing allele-specific methylation using Oxford Nanopore long-read DNA sequencing"
- **Slides:** TBD (Zenodo deposit typically 2-4 weeks post-conference)
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

bsseq stores and analyzes whole-genome cytosine methylation data — originally from WGBS but now extended to Oxford Nanopore long reads. Core capabilities: smoothing methylation estimates (BSmooth), F-statistic-based differentially methylated region (DMR) calling, and methylation summarization across regions. The Hansen-lab 2025 extension (bsseq >=1.45.1, slated for Bioconductor 3.22) adds allele-specific methylation (ASM) analysis from ONT long reads, leveraging the fact that long reads physically link CpG sites to the haplotype they sit on — letting an analyst test for methylation differences between maternal and paternal alleles without needing trio data or a separate phasing step.

## How it works

**Core idea.** BSmooth fits a local-likelihood (locally weighted) regression of methylation along the genome, borrowing strength across nearby CpGs within a CpG cluster so sparse-coverage loci still get a stable estimate. A two-group t-statistic with optional large-scale-bias correction is then thresholded, and contiguous super-threshold runs are emitted as DMRs.

**Inputs / outputs.** Input is a `BSseq` object holding per-CpG coverage matrices and methylated-read (M) counts from WGBS aligners (the reference implementation uses Merman output); for the ONT extension, methylation calls from long-read pipelines are loaded into the same container. Output is smoothed methylation estimates per CpG and a DMR table with `areaStat`, `meanDiff`, width, and cluster membership.

**Key innovation.** Adaptive local smoothing that preserves spatial resolution while sharing power across neighboring CpGs, with explicit handling of large-scale methylation shifts (common in cancer). The 2025 extension layers haplotype-resolved ASM on top by exploiting the physical phasing native to ONT long reads — no trio or separate phasing step required.

**Parameters worth knowing.**
- `h` — half-width of the smoothing window (default 1000 bp).
- `ns` — minimum CpGs per window (default 70).
- `maxGap` — distance at which CpG clusters are split (default 100 Mb).
- `mc.cores` — parallelization across samples.

**Canonical example.** The vignette uses `BS.cancer.ex` (chr21–22 cancer vs. normal colon, ABI SOLiD 50 bp):
```r
library(bsseq)
data(BS.cancer.ex)
BS.fit   <- BSmooth(BS.cancer.ex, mc.cores=6)
BS.tstat <- BSmooth.tstat(BS.fit, group1=c("C1","C2","C3"), group2=c("N1","N2","N3"))
dmrs     <- dmrFinder(BS.tstat, cutoff=c(-4.6, 4.6))
```

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo / AI methods; ASM is one of the more interesting non-cancer-specific extensions of long-read methylation analysis with cancer-imprinting and tumor-suppressor-silencing implications
- **EuroBioC 2025:** no direct counterpart; methylation-from-long-reads is GBCC-side this year
- **ISMB 2026:** scaffold; expect overlap on long-read methylation methods
- **Nextflow Summit 2026:** not mentioned

## Notes

bsseq is a mature, foundational Bioconductor package (in continuous development since ~2012). The ASM extension is the news at GBCC2025 — it folds ONT-specific phasing-aware logic into the same `BSseq` container that the WGBS community has been using for over a decade, which keeps the analysis ergonomics consistent for users who are switching modalities.
