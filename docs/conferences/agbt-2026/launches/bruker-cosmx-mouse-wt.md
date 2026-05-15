# CosMx mouse whole-transcriptome + 64-protein — Bruker (NanoString)

**Bruker's post-acquisition CosMx roadmap extends the platform into mouse whole-transcriptome plus 64-plex co-detected protein, positioning CosMx as the rodent-model counterpart to Xenium RNA+Protein.**

## At a glance

- **Vendor / launch date / availability:** Bruker Spatial Biology (post-NanoString acquisition); roadmap previewed at AGBT 2026 (Marco Island, Feb 22–25); commercial availability **TBD** *per [GEN — AGBT 2026 Recap, Feb–Mar 2026](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Chemistry / modality:** CosMx spatial molecular imager — cyclic in-situ hybridization for RNA, sequential immunofluorescence for protein, single-molecule resolution on FFPE / fresh-frozen sections.
- **Throughput (PR):** Mouse whole-transcriptome panel (gene count **TBD**, vendor has not published a precise plex figure at AGBT) *per [GEN AGBT recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)* **(vendor PR — no independent benchmark)**.
- **Multiomic plex:** 64-plex protein co-detection on the same section *per [GenomeWeb — Spatial Omics roadmaps at AGBT](https://www.genomeweb.com/sequencing/spatial-omics-single-cell-companies-provide-updates-roadmaps-agbt)* **(vendor PR — no independent benchmark)**.
- **Sample type:** FFPE and fresh-frozen mouse tissue; specifics **TBD** pending Bruker's formal datasheet.
- **List price / cost-per-sample:** **TBD** — Bruker has not published reagent kit pricing for the mouse WT panel.

## What's new vs prior generation

CosMx's prior human-only 6k / 18k-plex RNA panels and ~64-plex protein panels are extended into a *mouse* whole-transcriptome panel — the first time CosMx ships a rodent-scale WTA reagent rather than a curated human cancer / neuroscience panel. The 64-protein co-detection on the same section is the multiomic angle, mirroring the messaging 10x is using for Xenium RNA+Protein. This is also the first roadmap announcement under Bruker's post-acquisition ownership; messaging has shifted from NanoString-as-spatial-pureplay to CosMx-as-one-pillar of Bruker's CellScape + PaintScape + CosMx portfolio.

## Headline benchmarks

> Mouse whole-transcriptome RNA panel + 64-plex protein co-detection on the same FFPE / fresh-frozen section **(vendor PR — no independent benchmark)** — *[GEN AGBT 2026 recap, Feb–Mar 2026](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.

No third-party benchmark dataset has been published for the mouse WTA panel as of mid-May 2026; sensitivity, specificity, and per-cell transcript-detection metrics relative to MERSCOPE-mouse or Visium HD-mouse are **TBD**.

## Reception / competitive context

The mouse WTA panel is Bruker's direct counter to Vizgen's predesigned mouse MERFISH panels and to 10x's Xenium mouse Multi-Tissue v1 / v2 panel set. The 64-protein co-detection re-asserts CosMx's multiomic story against [Xenium RNA+Protein](https://www.genomeweb.com/business-news/agbt-showcases-diversity-spatial-genomics-technologies) (500-plex RNA + 28-plex protein, commercial mid-2026), where CosMx's protein plex is currently higher but Xenium's RNA plex is currently higher. The [GenomeWeb roadmap recap](https://www.genomeweb.com/tissue-based-testing/agbt-nanostring-10x-genomics-plan-high-resolution-spatial-assays-detect) frames CosMx-under-Bruker and Xenium as the two principal in-situ multiomic platforms going into H2 2026.

## Cross-links

- Bioconductor stack: [SpatialData](../../eurobioc-2025/tools/spatialdata.md) (CosMx reader), [SpatialExperiment](https://bioconductor.org/packages/SpatialExperiment/), [SOSTA](../../gbcc-2025/tools/sosta.md) — all consume CosMx outputs natively.
- Direct competitor at AGBT 2026: [10x Xenium RNA+Protein](../launches/index.md) (500-plex RNA + 28-plex protein, mid-2026).
- Sibling Bruker launches: [CellScape](../launches/index.md), [PaintScape](../launches/index.md) — same portfolio narrative.
- AACR 2026 cross-axis: single-cell-spatial-omics — CosMx mouse WTA opens preclinical-model tumor-microenvironment posters that previously had to rely on Visium / MERFISH mouse panels.

## Sources

- [GEN — AGBT 2026 Recap: NGS Big Bets and Spatial's Rising Momentum](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) — Feb–Mar 2026.
- [GenomeWeb — Spatial Omics, Single-Cell Companies Roadmaps at AGBT](https://www.genomeweb.com/sequencing/spatial-omics-single-cell-companies-provide-updates-roadmaps-agbt) — Feb 2026.
- [GenomeWeb — AGBT NanoString + 10x plan high-resolution spatial assays](https://www.genomeweb.com/tissue-based-testing/agbt-nanostring-10x-genomics-plan-high-resolution-spatial-assays-detect) — Feb 2026.
- [GenomeWeb — AGBT Showcases Diversity of Spatial Genomics Technologies](https://www.genomeweb.com/business-news/agbt-showcases-diversity-spatial-genomics-technologies) — Feb 2026.
