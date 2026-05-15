# SPRQ-Hq + SMRT-cell reuse — PacBio

## At a glance

- **Vendor:** PacBio
- **Launch date / venue:** AGBT 2026 (Marco Island, FL, Feb 22–25, 2026)
- **Availability:** Beta at AGBT → international early access **Feb 2026**; broad rollout 2026 *per [PacBio AGBT 2026 coverage / GEN recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*
- **Modality:** Revio chemistry update enabling **2 sequencing runs per SMRT cell** (beta) *per PacBio AGBT 2026 disclosure* **(vendor PR — no independent benchmark)**
- **Accuracy:** HiFi accuracy retained (Q≥30 base; >Q40 consensus) *per PacBio*
- **Cost-per-genome:** **$300 / 30× HiFi genome** when paired with SPRQ-Nx *per [Bio-IT World on PacBio JPM 2026 SPRQ-Nx economics](https://www.bio-itworld.com/news/2026/01/13/pacbio-at-jpm-2026--clinical-momentum-and-sprq-nx-economics)* **(vendor PR — no independent benchmark)**

## What's new

SPRQ-Hq lets a single Revio SMRT cell run twice in sequence, effectively doubling output per consumable without instrument changes. Paired with SPRQ-Nx volume economics communicated at JPM 2026, PacBio's pitch is that population-scale long-read WGS reaches a per-genome price point competitive with mid-tier short-read offerings, while retaining HiFi accuracy and read length.

## Headline benchmarks

- 2 runs/SMRT cell in beta — vendor claim; independent throughput-stability and run-to-run cross-contamination data not yet released *per PacBio AGBT 2026 sessions* **(vendor PR — no independent benchmark)**.
- $300 per 30× HiFi genome (paired with SPRQ-Nx) *per [Bio-IT World JPM 2026 coverage](https://www.bio-itworld.com/news/2026/01/13/pacbio-at-jpm-2026--clinical-momentum-and-sprq-nx-economics)* — list-price equivalent; absent volume-discount and amortization terms.

## Reception / competitive context

SPRQ-Hq is PacBio's direct rebuttal to Roche Axelios 1's "$150 / 30× duplex genome" pitch and Illumina TruPath's "$395 / genome" synthetic long-read offering. On the long-read side, it puts PacBio in the same per-genome price band as Axelios while keeping HiFi's accuracy and read-length advantage and the existing Revio install base.

## Cross-links

- Companion launch: **[CiFi](pacbio-cifi.md)** (built on SPRQ-Hq chemistry).
- Competitive: **[Roche Axelios 1](roche-axelios-1.md)** (long-read $/30× battle), **[Illumina TruPath](illumina-trupath.md)** (synthetic long-read).
- Downstream Bioconductor: [BSgenome](https://bioconductor.org/packages/release/bioc/html/BSgenome.html), [VariantAnnotation](https://bioconductor.org/packages/release/bioc/html/VariantAnnotation.html).

## Sources

- [PacBio Q1 2026 financial results](https://www.pacb.com/press_releases/pacbio-announces-first-quarter-2026-financial-results/)
- [Bio-IT World — PacBio at JPM 2026: SPRQ-Nx economics](https://www.bio-itworld.com/news/2026/01/13/pacbio-at-jpm-2026--clinical-momentum-and-sprq-nx-economics)
- [GEN — AGBT 2026 Recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)
- [GenomeWeb — Battle Royale in High-Throughput Clinical Applications](https://www.genomeweb.com/sequencing/agbt-sequencing-tech-updates-portend-battle-royale-high-throughput-clinical-applications)
