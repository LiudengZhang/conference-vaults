# Junyue Cao (keynote ★) — scalable combinatorial-indexing single-cell, plus temporal and spatial dynamics

**Speaker:** **Junyue Cao**, Rockefeller University (confirmed — [SCGD26 speaker page](https://satijalab.org/scgd26/)). (Trained as an early student in the **Shendure Lab**, UW; colleague **Darren** (Cusanovich) on sci-ATAC-seq.)
**Slot:** SCGD26, Jun 12, 2026 — 3:40–4:20 PM EDT (40-min featured talk), *"Scalable genomic approaches to investigate cellular dynamics in aging and disease"*
**Recording:** SCGD26 livestream (YouTube) — verify archived link
**Status:** Captured from session transcript

## Thesis

The body makes millions of new cells per second across thousands of cell types defined by thousands of integrated molecular features — so studying one gene or one cell misses the drivers and the cross-cell interactions. The lab builds **highly scalable tools** to quantify cell-population dynamics: which populations change, their temporal (proliferation/differentiation) and spatial interactions, and the molecular drivers.

## Scalable single-cell (combinatorial indexing)

- **Combinatorial indexing** barcodes molecules by repeated split-pool — no single-cell isolation. Lineage: sci-ATAC-seq (Darren) → sci-RNA-seq → **sci-CAR** (RNA+ATAC co-assay, 2018) → sci-RNA-seq3 (millions of cells, embryo).
- **EasySci** (students **Andras** [Sziraki] + **Jasper**): full-gene-body capture (exon-level → splice/isoform + cell-state) at **~$700 library prep / 1M cells**. Used across the brain (~2M cells, rare neurons) and a whole-organism atlas (>20 tissues, >1,000 tissues / >30M cells). Quantifies per-cell-type dynamics across aging (e.g. GZMK⁺ CD8 T-cell female-specific expansion; Th17 male-specific expansion; ~100 immune states × >20 tissues).
- **EnrichSci** ([bioRxiv 2025.05.02.651937](https://www.biorxiv.org/content/10.1101/2025.05.02.651937v1); *Cell Genomics* [S2666-979X(25)00357-X](https://www.cell.com/cell-genomics/fulltext/S2666-979X(25)00357-X)): RNA-probe enrichment against cell-type-specific **gene modules** (program-level, not single-gene/antibody) to target rare types — one module dimension separates/enriches 4 cell types in one experiment.

## Temporal dynamics (proliferation + differentiation)

- **sci-fate** (heard as "SkyFate"; [Cao et al., *Nat. Biotechnol.* 38, 980–988, 2020](https://www.nature.com/articles/s41587-020-0480-9)): scRNA + **4sU** metabolic labeling → two transcriptomes (newly synthesized + pre-labeling) per cell → infer **cell-state transition trajectories and probabilities** from one experiment; reconstructs cell-cycle transitions and predicts population dynamics over hours.
- **TrackerSci** ("Tracking cell-type-specific temporal dynamics in human and mouse brains," [*Cell*, 2023](https://www.sciencedirect.com/science/article/pii/S0092867423009765)): **EdU** labeling of newborn cells + scRNA/ATAC → quantify **proliferation and differentiation rates in vivo** across >20 tissues (>2M newborn cells; e.g. reduced neural-progenitor proliferation + increased microglial proliferation in aged brain; reduced OPC differentiation), mapping the gene/chromatin regulators of turnover.

## Spatial dynamics (sequencing, not imaging)

- **IRISeq** (image reconstruction by sequencing; "Optics-free Spatial Genomics for Mapping Mouse Brain Aging," [bioRxiv 2024.08.06.606712](https://www.biorxiv.org/content/10.1101/2024.08.06.606712v1) / [PMC11326199](https://pmc.ncbi.nlm.nih.gov/articles/PMC11326199/)): instead of scanning each cell's location, every bead records its **neighbors** (Hi-C-like), so location is reconstructed from local neighborhoods at **constant time regardless of area**. (Concurrent with related approaches — e.g. **SCOPE** and other imaging-free spatial genomics.)
- Implementation (first author **Abdul** [Abdulraouf Abdulraouf]; senior author Wei Zhou): tens of millions of in-house **sender + receiver beads**, combinatorially barcoded; receiver beads capture nearby tissue mRNA (polyT) + photocleaved sender-bead signal → reconstruct bead positions + cluster into regions. Validated on mouse brain (30 regions), 5–50 µm beads, **~$30/section (<$1/mm²)**; mapped region-specific cell-population changes (and interactions) in adult (4 mo) vs. aged (23 mo) brain.
- **PerturbFate** (grad student Zihan Xu; [Rockefeller news, 2026](https://www.rockefeller.edu/news/39376-novel-tool-could-identify-new-therapeutic-targets-in-complex-diseases-like-cancer/); builds on **PerturbSci-Kinetics**, [Xu et al., *Nat. Biotechnol.* 2023](https://www.nature.com/articles/s41587-023-01948-9)): couples high-throughput perturbation with the scalable single-cell + multi-layer (4sU nascent-RNA + ATAC) read-out to find molecular/cellular regulators of cellular alterations.

## Connections to the corpus

- The ultra-scalable combinatorial-indexing backbone underlies much of the AACR [single-cell-spatial-omics](../../aacr-2026/topics/single-cell-spatial-omics/) tooling; sci-RNA-seq3 lineage overlaps the GRC/Wellcome cohort in [`single-cell-genomics-2026/`](../../single-cell-genomics-2026/).
- Perturbation + temporal/spatial read-out connects to [Xin Jin](xin-jin-in-vivo-perturbseq.md), [Alex — VIP Perturb-seq](alex-vip-perturbseq.md), and [Aviv Regev](aviv-regev-virtual-cell.md).

## Verify / open questions

- **Confirmed:** speaker = Junyue Cao (Rockefeller), talk title, and slot (SCGD26 page). Method names corrected/confirmed: EasySci, EnrichSci, **sci-fate** (was "SkyFate"), TrackerSci, PerturbFate, **IRISeq** (the spatial image-reconstruction method) — see Sources.
- **Still unverified:** archived recording URL; student "**Jasper**" surname; whether "**EasySci**" inline DOI should be the brain-aging atlas paper vs. the method protocol (not pinned here).

## Sources

- SCGD26 speaker/schedule page: https://satijalab.org/scgd26/
- Junyue Cao lab (Rockefeller): https://www.rockefeller.edu/our-scientists/heads-of-laboratories/8704-junyue-cao/
- EnrichSci — bioRxiv: https://www.biorxiv.org/content/10.1101/2025.05.02.651937v1 ; *Cell Genomics*: https://www.cell.com/cell-genomics/fulltext/S2666-979X(25)00357-X
- sci-fate — *Nat. Biotechnol.* 2020: https://www.nature.com/articles/s41587-020-0480-9
- TrackerSci — *Cell* 2023: https://www.sciencedirect.com/science/article/pii/S0092867423009765
- IRISeq — bioRxiv 2024.08.06.606712 / PMC11326199: https://pmc.ncbi.nlm.nih.gov/articles/PMC11326199/
- PerturbFate — Rockefeller news 2026: https://www.rockefeller.edu/news/39376-novel-tool-could-identify-new-therapeutic-targets-in-complex-diseases-like-cancer/ ; PerturbSci-Kinetics — *Nat. Biotechnol.* 2023: https://www.nature.com/articles/s41587-023-01948-9
