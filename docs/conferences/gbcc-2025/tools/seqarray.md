# SeqArray

**Big-data storage and analysis of whole-genome sequencing variant calls in R/Bioconductor** — an array-oriented, compressed GDS-backed container for genotypes and annotations from population-scale WGS, designed to scale to biobank-class cohorts where VCF stops being usable.

- **Maintainer:** Xiuwen Zheng (AbbVie, formerly UW Genetic Analysis Center) — `zhengx@u.washington.edu`
- **Bioconductor:** [SeqArray](https://bioconductor.org/packages/release/bioc/html/SeqArray.html)
- **Source:** [github.com/zhengxwen/SeqArray](https://github.com/zhengxwen/SeqArray)
- **Vignettes:** [SeqArray Data Format and Access](https://bioconductor.org/packages/release/bioc/vignettes/SeqArray/inst/doc/SeqArrayTutorial.html)
- **Paper:** [Zheng et al., *Bioinformatics* 2017](https://academic.oup.com/bioinformatics/article/33/15/2251/3072873)
- **License:** GPL-3
- **Status at GBCC2025:** methods talk on biobank-scale rare-variant annotation workflows using GDS files

## Talk at GBCC2025

- **Speakers:** Xiuwen Zheng, Raven Chen
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2B, Grace Auditorium (chair: Vincent Carey)
- **Talk title:** "Enhancing rare variant analysis in biobanks: whole-genome annotation using GDS files"
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

SeqArray builds on the GDS (Genomic Data Structure) format — a hierarchical, array-oriented, compressed on-disk container — to store genotype matrices, allele frequencies, and per-variant annotations from WGS at biobank scale. Access is through an R interface with C++-level performance, and the data layout is designed so that filtering by sample, variant, or annotation is fast without re-streaming the whole file. The GBCC2025 talk extends this with workflows for **whole-genome annotation** during rare-variant analysis — folding functional annotation directly into the GDS container so that downstream rare-variant tests (in SeqVarTools, SNPRelate, GENESIS) can access annotations without a separate join.

## How it works

**Core idea.** GDS is "a flexible and scalable data container with a hierarchical structure that can store multiple array-oriented data sets." Genotypes are compressed to fewer than 8 bits per diploid call, and the hierarchical layout supports random access — so per-sample / per-variant slicing happens without scanning the whole file. The C++ CoreArray library does the work; the `gdsfmt` package exposes it to R.

**Inputs / outputs.** Inputs are VCF or BCF files converted with `seqVCF2GDS()`. Outputs are `SeqVarGDSClass` objects against which filtered queries are run; extracted data (genotypes, allele frequencies, INFO/FORMAT fields) come back as standard R objects.

**Key innovation.** Random-access, compressed, on-disk storage that scales past available RAM — the same storage substrate underlies SeqVarTools, SNPRelate, and GENESIS, which is why SeqArray anchors UK Biobank, *All of Us*, and TOPMed rare-variant workflows. The biobank-scale advantage over VCF is filtering and aggregating without re-streaming.

**Parameters worth knowing.**
- `seqSetFilter()` — set sample / variant filters on the open GDS handle.
- `seqGetData()` — extract data (`"genotype"`, `"annotation/info/AF"`, etc.) under the current filter.
- `seqAlleleFreq()` — compute per-variant allele frequencies.
- `seqApply()` / `seqBlockApply()` — stream a function over variants/samples in blocks.

**Canonical example.** The vignette's typical access pattern:
```r
gds <- seqOpen("mydata.gds")
seqSetFilter(gds, sample.id = samples, variant.id = variants)
genotypes <- seqGetData(gds, "genotype")
af        <- seqAlleleFreq(gds)
seqClose(gds)
```
The original Zheng et al. 2017 *Bioinformatics* paper benchmarks this against VCF on population-scale WGS.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo / AI methods; biobank rare-variant infrastructure is upstream of any large-scale germline-cancer or pharmacogenomics analysis
- **EuroBioC 2025:** no direct counterpart; biobank-scale GDS work is GBCC-side
- **ISMB 2026:** scaffold; expect overlap on biobank methods
- **Nextflow Summit 2026:** not mentioned

## Notes

SeqArray anchors a multi-package ecosystem (SeqVarTools, SNPRelate, GENESIS) used across UK Biobank, All of Us, and TOPMed analyses. The Day-2 talk is an annotation-pipeline update layered on a mature substrate — the news is workflow ergonomics, not a new container.
