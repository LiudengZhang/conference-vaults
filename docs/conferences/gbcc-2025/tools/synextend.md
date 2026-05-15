# SynExtend

**Tools for orthology detection, synteny analysis, and comparative genomics on top of DECIPHER** — a Bioconductor companion to Erik Wright's DECIPHER package, providing functions to compute synteny hits, predict gene-functional associations (EvoWeaver), and cluster orthology networks at billion-edge scale (ExoLabel).

- **Maintainers:** Nicholas Cooley, Aidan H. Lakshman, Erik S. Wright (University of Pittsburgh) — `npc19@pitt.edu`
- **Bioconductor:** [SynExtend](https://bioconductor.org/packages/release/bioc/html/SynExtend.html)
- **Source:** [github.com/ahl27/SynExtend](https://github.com/ahl27/SynExtend) (Lakshman fork) · upstream Bioconductor git
- **Vignettes:** [Using SynExtend](https://bioconductor.org/packages/release/bioc/vignettes/SynExtend/inst/doc/UsingSynExtend.html)
- **EvoWeaver paper:** [Lakshman & Wright, *Nature Communications* 2025](https://www.nature.com/articles/s41467-025-) — large-scale prediction of gene functional associations
- **ExoLabel:** disk-backed linear-time community-detection algorithm shipped inside SynExtend
- **License:** GPL-3
- **Status at GBCC2025:** methods talk on the orthology-clustering extension (ExoLabel)

## Talk at GBCC2025

- **Speakers:** Aidan H. Lakshman, Erik S. Wright (University of Pittsburgh)
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2B, Grace Auditorium (chair: Vincent Carey)
- **Talk title:** "Orthology Detection at the Scale of Modern Genomics"
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

SynExtend extends DECIPHER's sequence-comparison primitives into a full comparative-genomics stack: pairwise-similarity computation, synteny-block detection, orthology-network construction, and clustering of the resulting graph into orthologous groups. The GBCC2025 emphasis is on **ExoLabel** — a community-detection algorithm that uses disk storage to identify clusters on arbitrarily large similarity networks in linear time with bounded RAM, which sidesteps the memory wall that conventional orthology pipelines (MCL, OrthoFinder) hit at the scale of thousands of genomes.

## How it works

**Core idea.** SynExtend bootstraps orthology from synteny: DECIPHER's `FindSynteny()` first locates "exactly matched shared k-mers" between genomes and stitches proximate matches into significant syntenic blocks, then features that fall under those syntenic k-mer links are flagged as candidate ortholog pairs. The candidate pair graph is then clustered into orthogroups.

**Inputs / outputs.** Inputs are DECIPHER SQLite sequence databases plus gene/feature annotations and a k-mer matching threshold. Outputs are synteny maps across genomes, scored ortholog pair predictions, and orthogroup cluster assignments; EvoWeaver layers gene-functional-association predictions on top.

**Key innovation.** **ExoLabel** — a disk-backed, linear-time community-detection algorithm for the ortholog graph, which keeps memory bounded as the genome count grows. Together with EvoWeaver (Lakshman & Wright, *Nat. Commun.* 2025), this is what lets the DECIPHER ecosystem scale orthology detection past the size where MCL / OrthoFinder run out of RAM.

**Parameters worth knowing.**
- `FindSynteny()` — detects k-mer matches and assembles syntenic blocks.
- `NucleotideOverlap()` — computes sequence-similarity metrics over the synteny links.
- `PairSummaries()` — aggregates per-pair statistics for ortholog candidates.
- `ExoLabel()` — disk-backed clustering of the resulting orthology network.

**Canonical example.** The vignette loads the bundled `Endosymbionts_v05a.sqlite` (three endosymbiont genomes with distant evolutionary relationships) and runs `Syn <- FindSynteny(dbFile = DBPATH)` to produce a synteny summary across the three genomes, which then feeds into the pair-scoring and ExoLabel-clustering stages.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo / AI methods; orthology at scale matters for pan-cancer comparative-genomics and tumor-evolution dossiers
- **EuroBioC 2025:** no direct counterpart; comparative-genomics infrastructure is GBCC-side
- **ISMB 2026:** scaffold; expect overlap on scalable orthology methods
- **Nextflow Summit 2026:** not mentioned

## Notes

ExoLabel's linear-time-on-disk approach is the load-bearing claim. The package sits in the DECIPHER ecosystem (Wright lab at Pitt) — credibility comes from how heavily DECIPHER itself is used for ribosomal-RNA alignment and microbial-genome work across Bioconductor.
