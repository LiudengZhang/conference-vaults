# TruPath — Illumina

**Illumina's synthetic long-read add-on for NovaSeq X — phasing short reads into long-range "constellation mapped reads" at $395 / genome list.**

## At a glance

- **Vendor / launch date / availability:** Illumina; announced at AGBT 2026 and shipping *per [Illumina AGBT 2026 event page](https://www.illumina.com/events/conferences/2026/agbt-2026.html)*.
- **Chemistry / modality:** Synthetic long-read workflow on existing NovaSeq X — short reads are tagged and computationally reassembled into phased "constellation mapped reads" spanning kilobase-scale haplotypes.
- **Throughput (PR):** 16 human genomes per day per NovaSeq X under the TruPath workflow *per [Illumina AGBT 2026 page](https://www.illumina.com/events/conferences/2026/agbt-2026.html)* **(vendor PR — no independent benchmark)**.
- **Read length:** Native short reads (2×150 NovaSeq X), phased into long-range constellation mapped reads.
- **Accuracy (PR):** NovaSeq X base-call Q-scores carry through (Illumina has not published a TruPath-specific per-base accuracy figure) **(vendor PR — no independent benchmark)**.
- **List price / cost-per-genome:** **$395 / genome** at the TruPath workflow configuration *per [Illumina AGBT 2026 page](https://www.illumina.com/events/conferences/2026/agbt-2026.html)*.

## What's new vs prior generation

TruPath is a chemistry + bioinformatics layer on top of the existing NovaSeq X — Illumina's answer to PacBio HiFi and Oxford Nanopore for haplotype phasing and structural-variant resolution without buying a separate long-read instrument. It is the consumer-side counterpart to Illumina's separately previewed Q70 duplex chemistry roadmap (early access H2 2026). [GenomeWeb's spatial / multiomics AGBT recap](https://www.genengnews.com/topics/omics/illumina-unveils-spatial-technology-days-before-agbt-meeting/) frames the combined TruPath + Q70 + spatial announcement as Illumina's broadest single-AGBT release in years.

## Headline benchmarks

- 16 genomes / day per NovaSeq X under the TruPath workflow at $395 / genome **(vendor PR — no independent benchmark)** — *[Illumina AGBT 2026 page](https://www.illumina.com/events/conferences/2026/agbt-2026.html)*.

Independent benchmark data on phasing accuracy, SV recall, and effective long-range read length **has not yet surfaced** — third-party validation gap noted.

## Reception / competitive context

TruPath competes with PacBio HiFi / Revio SPRQ (native long-read at HiFi accuracy, ~$300 / genome with SPRQ-Nx per [Bio-IT World JPM 2026 coverage](https://www.bio-itworld.com/news/2026/01/13/pacbio-at-jpm-2026--clinical-momentum-and-sprq-nx-economics)) on cost, and with Oxford Nanopore on read length. Illumina's bet is that most NovaSeq X sites would rather add a synthetic long-read chemistry than acquire a separate long-read instrument. The companion **Q70 duplex kits** (early access H2 2026) target the duplex-accuracy floor that PacBio HiFi and Roche SBX have been pulling toward.

## Cross-links

- Downstream Bioconductor tools: VariantAnnotation, StructuralVariantAnnotation, methylKit; haplotype-aware variant callers as TruPath data formats stabilize.
- Native long-read competitor in this AGBT lineup: [PacBio CiFi](../launches/index.md) and Revio SPRQ-Hq.
- Companion Illumina roadmap item: Q70 duplex kits (separate dossier row in [`launches/index.md`](index.md)).
- Pre-AGBT context: [Illumina spatial teaser (GEN)](https://www.genengnews.com/topics/omics/illumina-unveils-spatial-technology-days-before-agbt-meeting/) and the [Illumina multiomic press release](https://www.illumina.com/company/news-center/press-releases/press-release-details.html?newsid=15da9928-16c1-453a-b908-a4469a1fc91c).

## Sources

- [Illumina AGBT 2026 event page](https://www.illumina.com/events/conferences/2026/agbt-2026.html) — Feb 2026.
- [Illumina multiomic press release](https://www.illumina.com/company/news-center/press-releases/press-release-details.html?newsid=15da9928-16c1-453a-b908-a4469a1fc91c) — Feb 2026.
- [GEN — Illumina unveils spatial technology days before AGBT meeting](https://www.genengnews.com/topics/omics/illumina-unveils-spatial-technology-days-before-agbt-meeting/) — Feb 2026.
- [Vilella Substack Part 1 — Illumina announcements and Ultima](https://albertvilella.substack.com/p/illumina-announcements-and-ultima) — Feb 2026.
- [Bio-IT World — PacBio at JPM 2026: SPRQ-Nx economics](https://www.bio-itworld.com/news/2026/01/13/pacbio-at-jpm-2026--clinical-momentum-and-sprq-nx-economics) — Jan 2026 (long-read pricing context).
