# CiFi — PacBio + UC Davis

## At a glance

- **Vendor:** PacBio (in collaboration with UC Davis; Megan Dennis lab)
- **Launch date / venue:** Announced 2026-01-08 (pre-AGBT); featured at AGBT 2026
- **Availability:** Shipping (reagent-only protocol) *per [PacBio CiFi press release, 2026-01-08](https://www.pacb.com/press_releases/pacbio-and-uc-davis-researchers-introduce-cifi-a-new-long-read-3c-method-that-enables-chromosome-scale-assemblies-from-a-single-smrt-cell/)*
- **Modality:** Long-read 3C / Hi-C variant on Revio (HiFi reads)
- **Output:** Chromosome-scale de novo assembly from **1 SMRT cell** *per [PacBio CiFi PR](https://www.pacb.com/press_releases/pacbio-and-uc-davis-researchers-introduce-cifi-a-new-long-read-3c-method-that-enables-chromosome-scale-assemblies-from-a-single-smrt-cell/)* **(vendor PR — no independent benchmark)**
- **Accuracy:** HiFi base accuracy retained, Q≥30 per base *per PacBio CiFi PR*
- **Price:** Reagent-only (consumes existing Revio SMRT cell footprint)

## What's new

CiFi captures 3D chromatin proximity ligations (like Hi-C) but reads them on Revio as HiFi long reads rather than on a short-read sequencer. The combination of HiFi base accuracy and proximity signal collapses what historically required separate HiFi + short-read Hi-C runs into a single SMRT cell run, dropping chromosome-scale assembly cost and turnaround for non-model organism genomics.

## Headline benchmarks

- Chromosome-scale assembly of human and selected non-human references from a single SMRT cell — disclosed in the PacBio/UC Davis announcement; independent N50 / haplotype-resolution metrics from non-UC-Davis groups not yet published as of AGBT *per [PacBio CiFi PR](https://www.pacb.com/press_releases/pacbio-and-uc-davis-researchers-introduce-cifi-a-new-long-read-3c-method-that-enables-chromosome-scale-assemblies-from-a-single-smrt-cell/)* **(vendor PR — no independent benchmark)**.

## Reception / competitive context

CiFi targets the de novo / pangenome / conservation genomics segment where Hi-C scaffolding is mandatory. By eliminating the short-read Hi-C arm, it tightens PacBio's grip on the chromosome-scale-assembly workflow and complements SPRQ-Hq's per-genome economics for population-scale long-read.

## Cross-links

- Companion chemistry: **[SPRQ-Hq / SMRT-cell reuse](pacbio-sprq-hq.md)** (CiFi runs on this chemistry).
- Downstream Bioconductor: [BSgenome](https://bioconductor.org/packages/release/bioc/html/BSgenome.html) and [GenomicRanges](https://bioconductor.org/packages/release/bioc/html/GenomicRanges.html) consume chromosome-scale assemblies for reference packaging and coordinate operations.
- AGBT 2026 plenary cross-ref: Megan Dennis (UC Davis) on Day 2 AI-in-Genomics plenary.

## Sources

- [PacBio + UC Davis CiFi press release (2026-01-08)](https://www.pacb.com/press_releases/pacbio-and-uc-davis-researchers-introduce-cifi-a-new-long-read-3c-method-that-enables-chromosome-scale-assemblies-from-a-single-smrt-cell/)
- [PacBio Q1 2026 financial results recap](https://www.pacb.com/press_releases/pacbio-announces-first-quarter-2026-financial-results/)
- [GEN — AGBT 2026 Recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)
