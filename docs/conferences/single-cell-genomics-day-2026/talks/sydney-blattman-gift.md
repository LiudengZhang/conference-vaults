# Sydney Blattman — GIFT: Genotyping In Fixed Transcriptomes

**Speaker:** **Sydney B. Blattman** — postdoc, **Dana Pe'er Lab**, Memorial Sloan Kettering Cancer Center (PhD, Columbia); collaboration with the **Caleb LaReau Lab** + MSK Single-Cell Analytics Innovation Lab and **10x Genomics**. Shout-outs: Nabi (Nabih Maslah), Austin (Austin A. Varela) — both preprint co-authors.
**Talk title (SCGD26 program):** "Scalable genotyping in fixed transcriptomes resolves clonal heterogeneity"
**Slot:** SCGD26, Jun 12, 2026
**Method:** **GIFT** (Genotyping In Fixed Transcriptomes) / **GIFT-seq**
**Recording:** SCGD26 livestream; Q&A answered live by **Caleb LaReau**
**Preprint:** Blattman et al., "Scalable genotyping in fixed transcriptomes resolves clonal heterogeneity via single-cell sequencing," bioRxiv 2026 — [doi:10.64898/2026.04.11.717967](https://www.biorxiv.org/content/10.64898/2026.04.11.717967v1) · [PubMed 41993258](https://pubmed.ncbi.nlm.nih.gov/41993258/)
**Protocol:** [GIFT-seq Gapfill and Library Preparation Protocol (protocols.io)](https://www.protocols.io/view/gift-seq-gapfill-and-library-preparation-protocol-4r3l2zm3jl1y/v1)
**Status:** Captured from session transcript — preprint + protocols.io live (confirmed)

> **Name note:** the SCGD26 program and the bioRxiv author list both spell the speaker **Blattman** (not "Blackman" as auto-transcribed); affiliation is MSKCC (Pe'er / Chaligné / LaReau labs).

## Thesis

Read **somatic genotype and phenotype in the same single cell, at scale, including from FFPE/archival tissue.** Somatic mutations drive tumorigenesis, metastasis, drug resistance (and possibly autoimmunity); many have undetected phenotypes. GIFT pairs mutation calls with gene-expression for clonal/lineage reconstruction.

## How it works

Built on **10x Flex** probe-based chemistry (not reverse transcription). Standard Flex ligates two single-stranded DNA probes hybridized to an mRNA. **GIFT introduces a gap (up to ~10 bases) between the two probes**, adds a polymerase to fill the gap over the genotyping site, then ligates → the variant is read out as a single-cell-barcoded molecule alongside normal Flex gene-expression probes.

Addresses the three limits of **GOT** (Genotyping Of Transcriptomes, 2019): low variant throughput, restriction to transcript-end mutations, and FFPE-incompatibility.

## Key results

- **Accuracy:** cell-line mixing (K562 / SET-2 / etc.) → **>99% genotyping accuracy**; correctly calls **heterozygous** cells (needs ≥1 WT + ≥1 mutant count — a real test of capture rate).
- **Scale:** >600 probe pairs → median **~164 genotyped sites per cell** (orders of magnitude over GOT); essentially **no transcript-position bias**.
- **Best-of-both vs. "dual probes" / GOT-multi:** allele-specific hybridization probes give degraded accuracy with a long failure tail; GIFT's polymerization step keeps ~99% accuracy.
- **FFPE:** a **de-crosslinking step** raised gene-expression yield ~10× (from ~250 counts/cell) and genotyping-probe capture ~10×. Applied to an **FFPE glioblastoma** sample: three EGFR mutations resolved into clones (one EGFR co-occurs with an AXL mutation = same clone; the other two are mutually exclusive = independent clones) → coarse lineage tree beyond bulk VAF.
- **Cohort scale:** **35 myeloproliferative-neoplasm patients, ~700k cells, 66 loci.** JAK2 genotype tracks HSC + monocyte clusters; **dosage response** (WT → het → homozygous via LOH) with sequentially increasing interferon-γ response. An MPN→AML case reconstructed a CALR/TP53/ZRSR2/EZH2 lineage tree.

## Q&A highlights

- **RNA vs DNA genotyping (Caleb LaReau):** sensitivity scales with expression; for pre-malignant rare-mutation cases, DNA may be fundamentally better, but many target genes are well-expressed and the win is multi-omics + the ability to load **millions** of cells (Flex v…) to recover rare cells.
- **Beyond SNVs:** indels/large variants handled by staggering multiple probes (ratio read-out) rather than gap-fill (see preprint Fig 3, EGFR example).
- **Spatial / Visium HD:** the preprint confirms GIFT is **Visium HD–compatible** — adapted to a spatially-restricted three-cell-line pattern with 98.8–99.7% accuracy, though spatial GE/GIFT complexity was lower than dissociated single cells, so most applications used the dissociated workflow.

## Connections to the corpus

- Single-cell genotype↔phenotype + lineage, FFPE-compatible — directly relevant to AACR [single-cell-spatial-omics](../../aacr-2026/topics/single-cell-spatial-omics/) and clinical clonal-evolution work.
- Flex/probe-chemistry sibling to [Alex — VIP Perturb-seq](alex-vip-perturbseq.md) (also Flex-based) and Caleb LaReau's **perf-seq** (RNA-FISH enrichment).

## Sources

- SCGD26 program (speaker, affiliation, talk title) — <https://satijalab.org/scgd26/>
- Preprint: bioRxiv [doi:10.64898/2026.04.11.717967](https://www.biorxiv.org/content/10.64898/2026.04.11.717967v1) · [PubMed 41993258](https://pubmed.ncbi.nlm.nih.gov/41993258/) — confirms title, full author list (Blattman … Maslah, Varela … Pe'er, Chaligné, LaReau), >99% accuracy, FFPE, and Visium HD compatibility.
- Protocol: [GIFT-seq Gapfill and Library Preparation Protocol, protocols.io](https://www.protocols.io/view/gift-seq-gapfill-and-library-preparation-protocol-4r3l2zm3jl1y/v1)

_All header attributions confirmed against the SCGD26 program and the bioRxiv preprint; no open items remain._
