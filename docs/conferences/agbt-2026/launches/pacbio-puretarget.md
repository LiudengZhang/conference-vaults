# PureTarget — PacBio

## At a glance

- **Vendor:** PacBio
- **Launch date / venue:** Showcased at AGBT 2026 (Marco Island, FL, Feb 22–25, 2026)
- **Availability:** Shipping *per [PacBio AGBT 2026 coverage](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*
- **Modality:** Capture-based **targeted long-read enrichment** on Revio (HiFi reads)
- **Accuracy:** HiFi (Q≥30 base, >Q40 consensus) *per PacBio AGBT messaging* **(vendor PR — no independent benchmark)**
- **List price:** TBD (kit-only reagent; instrument is existing Revio)

## What's new

PureTarget brings capture-based enrichment — long the standard for short-read clinical panels — to PacBio Revio HiFi reads. The combination targets clinical-genomics use cases that need both deep targeted coverage and long-read phasing / SV / methylation: pharmacogenomics, repeat expansions, HLA, large structural variants, and full-gene phasing of clinically relevant loci where short-read panels lose information.

## Headline benchmarks

- Capture footprint, on-target rate, multiplexing capacity, and panel sizes not yet disclosed in publicly visible PacBio materials post-AGBT *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)* **(vendor PR — no independent benchmark)**.
- HiFi base accuracy carried over from Revio platform — no PureTarget-specific concordance study published as of AGBT.

## Reception / competitive context

PureTarget is PacBio's clinical-genomics wedge: it brings long-read advantages (phasing, structural-variant resolution, methylation) into the targeted-panel workflows that drive most clinical sequencing volume today. Direct competitors include Twist / IDT short-read clinical panels and Oxford Nanopore adaptive-sampling targeted approaches; the differentiator is HiFi accuracy on capture.

## Cross-links

- Companion launches: **[CiFi](pacbio-cifi.md)**, **[SPRQ-Hq](pacbio-sprq-hq.md)** (same Revio platform).
- Downstream Bioconductor: [VariantAnnotation](https://bioconductor.org/packages/release/bioc/html/VariantAnnotation.html), [ensemblVEP](https://bioconductor.org/packages/release/bioc/html/ensemblVEP.html) — standard clinical-grade variant annotation stack.
- AACR clinical-trials axis: clinical-genomics applications (PGx, HLA, repeat-expansion disorders, somatic SVs in cancer panels) connect directly to AACR 2026 clinical-track posters; flag PureTarget vendor presence at AACR 2026 even though data-bearing posters are unlikely this cycle.

## Sources

- [GEN — AGBT 2026 Recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)
- [PacBio Q1 2026 financial results](https://www.pacb.com/press_releases/pacbio-announces-first-quarter-2026-financial-results/)
- [GenomeWeb — AGBT sequencing tech updates](https://www.genomeweb.com/sequencing/agbt-sequencing-tech-updates-portend-battle-royale-high-throughput-clinical-applications)
