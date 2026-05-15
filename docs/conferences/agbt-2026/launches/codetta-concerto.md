# Concerto — Codetta Bio

**Codetta Bio's Concerto positions as a multimodal biomarker platform measuring DNA, RNA, and protein from the same sample — pitched as a single-instrument alternative to stacking separate genomics, transcriptomics, and proteomics workflows.**

## At a glance

- **Vendor / launch date / availability:** Codetta Bio; profiled at AGBT 2026 (Marco Island, Feb 22–25); commercially available *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Chemistry / modality:** Multimodal biomarker platform — co-measurement of DNA, RNA, and protein analytes from a single workflow *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Throughput (PR):** **TBD** — public AGBT coverage did not enumerate samples/run or analytes/sample for Concerto.
- **Read length:** n/a (Concerto is a biomarker-readout instrument, not a sequencer; outputs are analyte counts/signals, not reads).
- **Accuracy (PR):** **TBD** — no LoD / sensitivity / specificity figures in the public AGBT 2026 trade-press coverage indexed in [program-notes](../program-notes.md).
- **List price / cost-per-sample:** **TBD** — no public list price or per-sample reagent cost surfaced in AGBT 2026 coverage.

> **Source caveat:** AGBT 2026 public coverage of Codetta Bio is sparse — the [GEN recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) names Concerto in the multi-vendor sweep but does not break out chemistry or specs. Most quantitative fields here are flagged TBD pending a dedicated Codetta press release or third-party benchmark. **(vendor PR — no independent benchmark)** applies to all spec claims below.

## What's new vs prior generation

Codetta Bio is a newer entrant in the multimodal-biomarker category; Concerto is its AGBT 2026 commercial entry. The strategic differentiation versus single-cell multiomics workflows (10x Chromium multiome, BD Rhapsody, Parse Biosciences) is bulk multimodal measurement on the *same physical sample* without the dissociation/microfluidic overhead of single-cell methods, optimized for biomarker discovery and clinical-trial sample throughput rather than single-cell resolution.

## Headline benchmarks

> **TBD** — no public benchmarks indexed at time of writing. Backfill when Codetta posts a methods paper, application note, or independent third-party comparison.

## Reception / competitive context

Concerto sits at the intersection of two AGBT 2026 narratives: (a) the multiomics-from-one-sample push that 10x's Atera/Xenium-RNA+Protein and Bruker's CosMx + Singular's G4X are all pushing on the spatial side, and (b) the biomarker / clinical-trial-readout segment that traditionally relies on stacking ELISA + qPCR + NGS panels. For AACR-axis applications (clinical-trial biomarker panels, drug-response signatures), Concerto's pitch competes with single-cell multiome (Rhapsody, 10x Chromium multiome) on multimodal coverage and with Olink / SomaScan + RNA-seq stacks on workflow consolidation.

## Cross-links

- **Single-cell multiomics competitors** at AGBT 2026: [Waters Rhapsody refresh](../launches/index.md), [10x Genomics Atera + Xenium RNA+Protein](../launches/index.md).
- **AACR axis — biomarker / clinical trials:** multimodal biomarker platforms feed clinical-trial pharmacodynamic readouts and pretreatment biomarker stratification; expect Concerto application notes to surface in AACR 2027 (too new for AACR 2026 *data* posters).
- **Bioconductor downstream:** multimodal biomarker output naturally lands in [MultiAssayExperiment](https://bioconductor.org/packages/MultiAssayExperiment/) for harmonized multi-modality storage.
- **AGBT 2026 lineage:** Codetta Bio is profiled alongside Cellanome, Syndex Bio, and Volta Labs in the [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) as part of the "emerging platforms" sweep.

## Sources

- [GEN — AGBT 2026 Recap: NGS Big Bets and Spatial's Rising Momentum](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) — Feb–Mar 2026 (Codetta listed in multi-vendor recap; specifics not enumerated).
- [AGBT 2026 program-notes vendor index](../program-notes.md) — Codetta Bio entry under "Vendor PR coverage indexed by company".

> **Open items:** locate a primary Codetta Bio press release or product page enumerating Concerto's analyte panel, throughput, and pricing. Backfill spec table and benchmarks lines once a primary source is reachable.
