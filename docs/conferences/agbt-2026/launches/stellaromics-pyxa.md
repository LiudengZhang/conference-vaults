# Pyxa — Stellaromics

**Stellaromics debuts Pyxa at AGBT 2026 as the "first commercial 3D spatial imager," opening a category that until now has been research-prototype-only.**

## At a glance

- **Vendor / launch date / availability:** Stellaromics; AGBT 2026 newcomer launch (Marco Island, Feb 22–25); commercial availability and pre-order terms **TBD** *per [GEN AGBT 2026 recap, Feb–Mar 2026](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Chemistry / modality:** 3D spatial imaging — specifics (probe chemistry, optical sectioning approach, z-resolution) **TBD**; Stellaromics's AGBT messaging emphasizes "first commercial 3D spatial imager" without disclosing the underlying assay class *per [GEN AGBT recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)* **(vendor PR — no independent benchmark)**.
- **Plex / panel:** **TBD** — no gene-count or protein-plex figure disclosed at AGBT.
- **Throughput / sample type:** **TBD** — no per-sample run-time, tissue-thickness ceiling, or sample-format compatibility figure disclosed at AGBT.
- **Read length / accuracy:** n/a (imager, not sequencer).
- **List price / cost-per-sample:** **TBD**.

## What's new vs prior generation

Pyxa is a *category* launch rather than an incremental refresh. Existing commercial spatial imagers (Xenium, CosMx, MERSCOPE, Visium HD) are all 2D — they image thin tissue sections and reconstruct neighborhoods within a single z-plane. Pyxa's pitch is to image native 3D tissue volumes and produce single-molecule data with true z-coordinates, which would let users study tumor architecture, vascular branching, and tissue-scale gradients that 2D platforms see only by serial-section reconstruction. Independent of how the chemistry actually works (which Stellaromics has not disclosed at AGBT), the marketing position is "the first 3D entrant," with [Bruker's PaintScape](../launches/index.md) as the most directly comparable roadmap claim from an incumbent.

## Headline benchmarks

> "First commercial 3D spatial imager" **(vendor PR — no independent benchmark)** — *[GEN AGBT 2026 recap, Feb–Mar 2026](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.

No third-party benchmark, no spec table, no demo dataset URL has been published as of mid-May 2026. Stellaromics's category-defining claim is **unverifiable from public sources** at this point; AACR 2026 and follow-on user-group meetings are the next likely venues for spec disclosure.

## Reception / competitive context

Stellaromics is a category-creating newcomer and was covered as one of the AGBT 2026 spatial *surprise* stories alongside Singular Genomics G4X and the Bruker / NanoString consolidation. The most directly comparable claim is [Bruker PaintScape](../launches/index.md), which Bruker positions as "3D genome visualization" on its spatial roadmap. The two are likely to converge into a 3D-spatial subcategory over 2026–2027; until either ships, both are roadmap-only. The [GenomeWeb spatial recap](https://www.genomeweb.com/business-news/agbt-showcases-diversity-spatial-genomics-technologies) places Stellaromics squarely in the "AGBT showcased the diversity of spatial genomics" narrative arc.

## Cross-links

- Closest competitor on the AGBT 2026 roadmap: [Bruker PaintScape](../launches/index.md) — the other 3D entrant.
- 2D in-situ context: [10x Xenium RNA+Protein](../launches/index.md), [CosMx mouse WT + 64-protein](bruker-cosmx-mouse-wt.md), [MERSCOPE Ultra](vizgen-merscope-ultra.md), [Singular G4X](../launches/index.md).
- AACR 2026 cross-axis: 3D-genome / tissue-architecture — Pyxa, once shipping, would be the most natural AACR posters-on-tumor-architecture spatial-imager, where today users mostly serial-section Visium HD or Xenium.
- Bioconductor: no Pyxa reader exists yet; if Stellaromics adopts the Zarr-based SpatialData container, a [SpatialData](../../eurobioc-2025/tools/spatialdata.md) integration path opens immediately.

## Sources

- [GEN — AGBT 2026 Recap: NGS Big Bets and Spatial's Rising Momentum](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) — Feb–Mar 2026.
- [GenomeWeb — AGBT Showcases Diversity of Spatial Genomics Technologies](https://www.genomeweb.com/business-news/agbt-showcases-diversity-spatial-genomics-technologies) — Feb 2026.
- [GenomeWeb — Spatial Omics, Single-Cell Companies Roadmaps at AGBT](https://www.genomeweb.com/sequencing/spatial-omics-single-cell-companies-provide-updates-roadmaps-agbt) — Feb 2026.
