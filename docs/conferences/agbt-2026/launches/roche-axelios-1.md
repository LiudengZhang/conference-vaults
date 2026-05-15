# Axelios 1 — Roche

**Roche's nanopore "sequencing by expansion" (SBX) platform, pitched at a $150 / 30× duplex human genome.**

## At a glance

- **Vendor / launch date / availability:** Roche; revealed at AGBT 2026 (Marco Island, Feb 22–25); pre-orders open post-AGBT; formal commercial launch summer 2026 *per [GenomeWeb coverage dated Feb 2026](https://www.genomeweb.com/sequencing/promising-150-genome-roche-reveals-more-details-axelios-sequencer-agbt)*.
- **Chemistry / modality:** Nanopore sequencing-by-expansion (SBX) — template DNA is enzymatically expanded into a longer, more discriminable polymer before nanopore readout.
- **Throughput (PR):** 16 human genomes per run *per [GenomeWeb / Roche AGBT release](https://www.genomeweb.com/sequencing/promising-150-genome-roche-reveals-more-details-axelios-sequencer-agbt)* **(vendor PR — no independent benchmark)**.
- **Read length:** Average duplex ~230–250 bp *per [GenomeWeb Feb 2026](https://www.genomeweb.com/sequencing/promising-150-genome-roche-reveals-more-details-axelios-sequencer-agbt)*.
- **Accuracy (PR):** Q38 duplex *per [GenomeWeb Feb 2026](https://www.genomeweb.com/sequencing/promising-150-genome-roche-reveals-more-details-axelios-sequencer-agbt)* **(vendor PR — no independent benchmark)**.
- **List price / cost-per-genome:** $750k instrument; **$150 per 30× duplex genome**; $0.06 per million reads simplex *per [GenomeWeb Feb 2026](https://www.genomeweb.com/sequencing/promising-150-genome-roche-reveals-more-details-axelios-sequencer-agbt)*.

## What's new vs prior generation

Axelios is Roche's first commercial sequencer since exiting 454 — a wholly new modality rather than an incremental upgrade. SBX expands template DNA into a longer reporter polymer that is then read on a nanopore, decoupling read accuracy from native base-by-base translocation speed and giving Roche a route to compete on cost-per-genome rather than read length.

## Headline benchmarks

> 16 human genomes per run, average duplex 230–250 bp, Q38 duplex, $150 / 30× duplex genome **(vendor PR — no independent benchmark)** — *[GenomeWeb, Feb 2026](https://www.genomeweb.com/sequencing/promising-150-genome-roche-reveals-more-details-axelios-sequencer-agbt)*.

[omicsomics' run-pricing teardown (Mar 2026)](https://omicsomics.blogspot.com/2026/03/roche-axelios1-run-pricing-not-knockout.html) argues the $150 headline is conditional on full-run utilization and that effective cost rises sharply at lower batch sizes.

## Reception / competitive context

Roche entered AGBT 2026 as the most-watched re-entrant; the $150 genome anchors the lower bound of the AGBT 2026 short-read lineup alongside Element VITARI and Complete DNBSEQ-T7+ (both at $100/genome list). [Vilella Part 2](https://albertvilella.substack.com/p/roche-unveils-the-150-genome-with) flags the short duplex length (~230–250 bp) as the strategic weakness vs Element / Ultima / Complete on long-insert applications.

## Cross-links

- Downstream Bioconductor tools: [BSgenome](https://bioconductor.org/packages/BSgenome/), [VariantAnnotation](https://bioconductor.org/packages/VariantAnnotation/), [methylKit](https://bioconductor.org/packages/methylKit/) for duplex methylation calling.
- Long-read alternative at AGBT 2026: [PacBio CiFi](../launches/index.md) (chromosome-scale HiFi assembly from one SMRT cell).
- Direct AGBT 2026 short-read competitors: [Element VITARI](element-vitari.md), [Complete DNBSEQ-T7+](complete-dnbseq-t7-plus.md), [Ultima UG200](ultima-ug200.md).

## Sources

- [GenomeWeb — "Promising $150 Genome": Roche reveals more details of Axelios sequencer at AGBT](https://www.genomeweb.com/sequencing/promising-150-genome-roche-reveals-more-details-axelios-sequencer-agbt) — Feb 2026.
- [omicsomics — "Roche Axelios1 run pricing: not a knockout"](https://omicsomics.blogspot.com/2026/03/roche-axelios1-run-pricing-not-knockout.html) — Mar 2026.
- [Vilella Substack Part 2 — Roche unveils the $150 genome](https://albertvilella.substack.com/p/roche-unveils-the-150-genome-with) — Feb 2026.
- [biotech-now mirror of the GenomeWeb piece](https://www.biotech-now.co.uk/article/345691/promising-150-genome-roche-reveals-more-details-of-axelios-sequencer-at-agbt) — Feb 2026.
