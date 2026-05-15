# Rhapsody (refresh under Waters) — Waters (ex-BD)

**Waters re-introduces the BD Rhapsody single-cell multiomics platform under new ownership at AGBT 2026; the chemistry is unchanged but the portfolio framing and director-level hires are new.**

## At a glance

- **Vendor / launch date / availability:** Waters Corporation (acquired Rhapsody from BD); re-introduction at AGBT 2026 (Marco Island, Feb 22–25); platform is **shipping** as existing inventory under the new owner *per [GEN AGBT 2026 recap, Feb–Mar 2026](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Chemistry / modality:** Rhapsody microwell-based single-cell multiomics — magnetic-bead barcoded mRNA capture, optional AbSeq protein co-detection, optional TCR / BCR targeted assays; unchanged from the BD-era platform.
- **Throughput / plex:** Existing Rhapsody specs carry over; current figures are **TBD** under Waters branding (Waters has not republished a refreshed datasheet at AGBT).
- **Read length / accuracy:** n/a (library output goes to a third-party short-read sequencer — typically Illumina or AVITI).
- **Personnel signal:** Luciano Martelotto hired as director — flagged in [program-notes.md](../program-notes.md) as the most visible AGBT 2026 indicator that Waters intends to invest in the single-cell line rather than wind it down *per [GEN AGBT recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **List price / cost-per-sample:** **TBD** — Waters has not republished list pricing post-acquisition.

## What's new vs prior generation

The Rhapsody *instrument* is essentially the same hardware-and-chemistry stack BD has shipped since the mid-2010s. What's new at AGBT 2026 is the *portfolio framing*: Waters is folding Rhapsody into its broader analytical-instruments business and signaling — via the Martelotto hire and the AGBT booth presence — that the platform stays alive rather than being sunset post-acquisition. Effectively a positioning launch, not a technology launch.

## Headline benchmarks

> Existing BD Rhapsody specs carried over to Waters branding; no refreshed throughput, plex, or accuracy figure published at AGBT 2026 **(vendor PR — no independent benchmark)** — *[GEN AGBT 2026 recap, Feb–Mar 2026](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.

No new third-party benchmark accompanies the Waters re-introduction; cell-recovery, gene-detection, and AbSeq-protein-plex figures remain the BD-era numbers and should be treated as carry-over.

## Reception / competitive context

Single-cell multiomics is dominated commercially by [10x Genomics Chromium](https://www.10xgenomics.com/) at the high end and by Parse Biosciences / Scale Biosciences / Honeycomb / Fluent at the high-throughput / lower-cost end. Rhapsody's microwell architecture is a structural alternative to Chromium's droplet workflow with native AbSeq protein co-detection — historically a strong angle but commercially underexploited under BD ownership. AGBT 2026 coverage treats the Waters re-launch as a "will Waters actually invest?" question; the Martelotto director hire is the strongest answer-in-the-affirmative signal as of mid-May 2026. Indirect competition from Atera / Xenium / CosMx is now also relevant because in-situ spatial multiomics is pulling cancer-cohort budget that previously went to dissociated single-cell.

## Cross-links

- Primary single-cell competitor: [10x Genomics Chromium](https://www.10xgenomics.com/) ecosystem (out-of-vault).
- Spatial-multiomic crossover competitors at AGBT 2026: [10x Xenium RNA+Protein](../launches/index.md), [CosMx mouse WT + 64-protein](bruker-cosmx-mouse-wt.md) — both are pulling tumor-microenvironment work that historically used dissociated Rhapsody / Chromium.
- AACR 2026 cross-axis: single-cell talks — Rhapsody + AbSeq is a recurring AACR poster modality especially in immune-monitoring and CAR-T workflows; AACR 2026 posters are still labeled "BD Rhapsody" but AACR 2027 / 2028 will see the Waters-branded reagent on incoming posters.
- Bioconductor: standard [SingleCellExperiment](https://bioconductor.org/packages/SingleCellExperiment/) ecosystem applies; no Rhapsody-specific reader changes from the Waters re-brand.

## Sources

- [GEN — AGBT 2026 Recap: NGS Big Bets and Spatial's Rising Momentum](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) — Feb–Mar 2026.
- [GenomeWeb — Spatial Omics, Single-Cell Companies Roadmaps at AGBT](https://www.genomeweb.com/sequencing/spatial-omics-single-cell-companies-provide-updates-roadmaps-agbt) — Feb 2026.
- [AGBT 2026 program notes — vendor index](../program-notes.md) — entry for Waters (ex-BD) Rhapsody re-introduction and Martelotto hire.
