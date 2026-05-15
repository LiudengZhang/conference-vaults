# MIRit

**Integrate microRNA and gene expression to decipher pathway complexity** — a Bioconductor framework that investigates relationships between miRNAs and genes across biological conditions, supporting differential expression analysis and network characterization between miRNA and mRNA expression.

- **Maintainer:** Jacopo Ronchi (University of Milano-Bicocca, UniMiB) — `jacopo.ronchi@unimib.it`
- **Bioconductor:** [MIRit v1.8.0](https://bioconductor.org/packages/release/bioc/html/MIRit.html)
- **Source:** [git.bioconductor.org/packages/MIRit](https://git.bioconductor.org/packages/MIRit)
- **Vignettes:** [MIRit](https://bioconductor.org/packages/release/vignettes/MIRit/inst/doc/MIRit.html)
- **License:** GPL (>=3)
- **Status at EuroBioC2025:** methods talk on miRNA-mRNA network integration

## Talk at EuroBioC2025

- **Speaker:** Jacopo Ronchi (University of Milano-Bicocca)
- **Day / session:** Day 1 (Wed Sep 17, 2025) — afternoon short-talk session, after the Holmes keynote
- **Talk title:** "MIRit framework for miRNA-mRNA network identification"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded — short talks at EuroBioC2025 were not part of the plenary YouTube playlist
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

MIRit jointly models miRNA and mRNA expression to recover regulatory relationships across biological conditions. It performs differential expression analysis on both modalities and characterizes miRNA-mRNA interaction networks, so that pathway-level signal is interpreted through the regulatory layer rather than from gene expression alone.

## How it works

**Core idea.** A `MultiAssayExperiment`-based container (`MirnaExperiment`) holds matched miRNA and mRNA expression matrices; MIRit runs differential expression on each modality, retrieves predicted and validated miRNA-target interactions, and integrates the two sides — via correlation analysis for paired samples and via association tests / rotation gene-set tests for unpaired designs — to flag miRNA-target pairs whose joint dysregulation is consistent with regulatory action.

**Inputs / outputs.** Input: a gene-expression matrix (HGNC gene symbols × samples), a miRNA-expression matrix (miRBase miRNA names × samples), and a sample metadata data.frame keyed by subject ID with miRNA/gene column mappings and a condition variable. Output: a `MirnaExperiment` annotated with per-modality DE results, retrieved target interactions, integrative significance per miRNA-target pair, and enrichment results (ORA, GSEA, CAMERA).

**Key innovation.** Wraps the miRNA-target integration workflow — DE on both layers, target lookup, paired-vs-unpaired integration, enrichment, and SNP-disease association at miRNA loci — into a single Bioconductor container, rather than leaving it as a series of bespoke scripts. The specific DE algorithm and target databases are not explicitly named in the introduction vignette — *not specified in vignette excerpt; needs talk slides*.

**Parameters worth knowing.** `pairedSamples` in the `MirnaExperiment` constructor — switches the integrative test between correlation (paired) and association/rotation gene-set tests (unpaired). `primary` / `mirnaCol` / `geneCol` columns in the metadata data.frame — the join keys for the two matrices.

**Canonical example.** Vignette uses an RNA-Seq thyroid-cancer dataset from Riesco-Eizaguirre et al. (2015): 8 papillary thyroid carcinoma tumors with matched contralateral normal thyroid tissue from the same patients. Workflow: build the `MirnaExperiment` with `pairedSamples = TRUE`, visualize with `plotDimensions()` (MDS by condition), run DE on each modality, retrieve targets, then integrate to recover miRNA-gene pairs whose paired dysregulation is consistent with target repression.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; relevant axis is bioinfo / AI methods — network-based miRNA-mRNA integration is conceptually adjacent to MOSClip's pathway-based multi-omics
- **MOSClip** ([entry](mosclip.md)) — sibling pathway/network method on the same Day 1 short-talk session
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** not mentioned

## Notes

miRNA-mRNA integration sits in the network-based pathway analysis tradition; complement to MOSClip ([entry](mosclip.md)) on the same session, with MIRit emphasizing the regulatory-network framing rather than survival.
