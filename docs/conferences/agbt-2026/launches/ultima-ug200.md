# UG200 / UG200 Ultra — Ultima Genomics

**Ultima's wafer-based single-end SBS platform at production scale — 162 Tb/wk ceiling and Q60 ppmSeq duplex-equivalent reads, optimized for cohort-scale exome and WGS.**

## At a glance

- **Vendor / launch date / availability:** Ultima Genomics; presented and shipping at AGBT 2026 *per [Vilella Substack Part 1](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)*.
- **Chemistry / modality:** Single-end sequencing-by-synthesis on circular silicon wafers using isothermal amplification; paired-end ("Solaris 2.0") on the 2026 roadmap *per [Vilella Substack Part 1](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)*.
- **Throughput (PR):** Up to 162 Tb/week maximum; 60 wafers/week throughput on UG200 Ultra; ~1,350 genome-equivalents/week (Ultra) *per [Vilella Substack Part 1](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)* **(vendor PR — no independent benchmark)**.
- **Read length:** Up to ~300 bp single-end; paired-end on the Solaris 2.0 roadmap *per [Vilella Substack Part 1](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)*.
- **Accuracy (PR):** Q60 ppmSeq duplex-equivalent *per [Vilella Substack Part 1](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)* **(vendor PR — no independent benchmark)**.
- **List price / cost-per-genome:** **$850k (UG200 / single wafer)** and **$1.25M (UG200 Ultra)** *per [Vilella Substack Part 1](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)*.

## What's new vs prior generation

UG200 follows the UG100 wafer-sequencer, doubling effective wafer throughput and introducing the UG200 Ultra tier (multi-wafer, ~1,350 genomes/week). Ppm­Seq accuracy moves from ~Q40 duplex-equivalent on the prior generation to **Q60** on UG200, narrowing the duplex-accuracy gap with PacBio HiFi and Roche SBX while preserving the single-end / cohort-scale economics that have been Ultima's pitch since launch. The Solaris 2.0 paired-end roadmap, if it ships, would close the historical gap vs Illumina/Element for variant callers tuned to PE inserts.

## Headline benchmarks

- 162 Tb/wk ceiling and ~1,350 genome-equivalents/week on UG200 Ultra **(vendor PR — no independent benchmark)** — *[Vilella Substack Part 1](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)*.
- Q60 ppmSeq duplex-equivalent across the production wafer **(vendor PR — no independent benchmark)** — *[Vilella Substack Part 1](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)*.

## Reception / competitive context

UG200 is the throughput ceiling of the AGBT 2026 short-read lineup; Element VITARI and Complete DNBSEQ-T7+ compete on price ($100 vs Ultima's higher capital cost) while Ultima retains the per-week genome-count advantage. Roche Axelios's $150 genome is an order of magnitude lower in instrument cost ($750k) but ships later (summer 2026). [GenomeWeb's "battle royale" recap](https://www.genomeweb.com/sequencing/agbt-sequencing-tech-updates-portend-battle-royale-high-throughput-clinical-applications) and the [GEN AGBT recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) both put Ultima in the "incumbent at cohort scale" position, with Element as the principal challenger.

## Cross-links

- Downstream Bioconductor tools: short-read aligners + variant callers; methylKit for any duplex methylation work; cohort-scale workflows in [GBCC 2025 spatialLIBD-adjacent population-genomics talks].
- Competitive context in this AGBT lineup: [Element VITARI](element-vitari.md) (price challenger), [Roche Axelios 1](roche-axelios-1.md) (cost-per-genome floor), [Complete DNBSEQ-T7+](complete-dnbseq-t7-plus.md) ($100 genome twin).
- AACR 2026 tie-in: AACR posters tagged "Ultima" / "single-end" + cancer cohort scale are the natural first wave of UG200-era data.

## Sources

- [Vilella Substack Part 1 — Illumina announcements and Ultima](https://albertvilella.substack.com/p/illumina-announcements-and-ultima) — Feb 2026.
- [GenomeWeb — "Battle Royale" recap](https://www.genomeweb.com/sequencing/agbt-sequencing-tech-updates-portend-battle-royale-high-throughput-clinical-applications) — Feb 2026.
- [GEN — AGBT 2026 Recap: NGS Big Bets and Spatial's Rising Momentum](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) — Feb–Mar 2026.
