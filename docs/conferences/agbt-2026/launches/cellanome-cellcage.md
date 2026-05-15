# CellCage — Cellanome

**Cellanome's CellCage pitches temporal single-cell tracking — repeated transcriptome readouts from the same physical cell over time — addressing the destructive-readout limitation that has dogged single-cell RNA-seq since its inception.**

## At a glance

- **Vendor / launch date / availability:** Cellanome; profiled at AGBT 2026 (Marco Island, Feb 22–25); roadmap (not commercially shipping at AGBT) *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Chemistry / modality:** Temporal single-cell tracking — transcriptome measurement over time per cell rather than the destructive end-point single-readout of conventional scRNA-seq *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Throughput (PR):** **TBD** — cells per run, timepoints per cell, and run-time figures not enumerated in public AGBT 2026 coverage.
- **Read length:** n/a (CellCage is a single-cell sample-handling / readout platform; downstream sequencing chemistry not specified in public coverage).
- **Accuracy (PR):** **TBD** — no per-cell capture efficiency, transcript-detection sensitivity, or temporal-resolution figures in public AGBT coverage.
- **List price / cost-per-sample:** **TBD** — roadmap-status platform, no pricing surfaced.

> **Source caveat:** AGBT 2026 public coverage of Cellanome is limited to the [GEN recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) inclusion and the [program-notes](../program-notes.md) line noting **Gary Schroth (formerly Illumina) as CSO**. Most quantitative fields are flagged **TBD**; **(vendor PR — no independent benchmark)** applies to all spec claims.

## What's new vs prior generation

The defining limitation of single-cell RNA-seq is that the readout destroys the cell — every dataset is a snapshot of a different population, and "temporal" inference relies on RNA-velocity modeling or pseudotime reconstruction rather than direct measurement. CellCage's pitch inverts that constraint: track the *same* cell across multiple timepoints, enabling direct trajectory measurement for differentiation, drug-response kinetics, and clonal-fate mapping. This places CellCage adjacent to (but mechanistically distinct from) lineage-barcoding methods like Watermelon, LARRY, and barbieQ that infer trajectories via clonal barcoding rather than direct repeated measurement.

## Headline benchmarks

> **TBD** — no published demonstration cohort, no third-party comparison, no methods paper indexed at time of writing.

## Reception / competitive context

CellCage entered AGBT 2026 as a category-defining roadmap announcement rather than a head-to-head competitor to a specific shipping product. The Gary Schroth CSO appointment signals serious chemistry pedigree (Schroth led Illumina's library-prep R&D for years). Conceptually adjacent platforms and methods at the same meeting / cross-conference:

- **Clonal-tracking methods** at EuroBioC / GBCC — [barbieQ](https://bioconductor.org/) and similar clone-tracking statistical frameworks are conceptually adjacent (both reconstruct cell-level trajectories, but barbieQ uses barcoded clonal inference; CellCage measures the same cell directly).
- **AACR axis — drug resistance / lineage tracing:** CellCage's natural AACR application is direct measurement of drug-response trajectories in tumor cells (kinetics of resistance emergence per cell), competing with Watermelon and LARRY barcoding approaches that dominate current AACR drug-resistance posters.

## Cross-links

- **Conceptually adjacent (clonal tracking):** [GBCC / EuroBioC barbieQ](../../eurobioc-2025/index.md) — clone-tracking statistical framework, complementary rather than directly competitive.
- **Single-cell platforms at AGBT 2026:** [Waters Rhapsody refresh](index.md), [Codetta Concerto](codetta-concerto.md) (different angle — multimodal bulk rather than temporal single-cell).
- **AACR axis — drug-resistance / lineage tracing:** CellCage is too early-stage for AACR 2026 data posters; expect first methods abstracts at AACR 2027 / AGBT 2027 if the platform ships on schedule.
- **Bioconductor downstream:** temporal single-cell data lands naturally in [SingleCellExperiment](https://bioconductor.org/packages/SingleCellExperiment/) with custom time-dimension annotations; trajectory tools (slingshot, tradeSeq) become *direct measurement* tools rather than inference tools when fed CellCage data.

## Sources

- [GEN — AGBT 2026 Recap: NGS Big Bets and Spatial's Rising Momentum](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) — Feb–Mar 2026 (Cellanome listed in emerging-platforms recap; specifics not enumerated).
- [AGBT 2026 program-notes vendor index](../program-notes.md) — Cellanome entry noting Gary Schroth CSO.

> **Open items:** locate a primary Cellanome press release or Schroth public talk enumerating CellCage's per-cell timepoint count, throughput, and shipping window. Backfill spec table when a primary source is reachable.
