# SEMPLR

**SNP Effect Matrix Pipeline in R** — a Bioconductor package for predicting transcription-factor-binding effects of genetic variants using pre-computed SNP Effect Matrices (SEMs); ships 223 built-in matrices and supports custom matrices, with enrichment and variant-comparison utilities on top.

- **Maintainer:** Grace E Kenney (Boyle / Phanstiel labs, University of Michigan) — `kenney.grace6@gmail.com`
- **Bioconductor:** [SEMPLR v1.0.0](https://bioconductor.org/packages/release/bioc/html/SEMPLR.html)
- **Source:** [github.com/grkenney/SEMPLR](https://github.com/grkenney/SEMPLR) · [project site](https://grkenney.github.io/SEMPLR)
- **Vignettes:** [SEMPLR intro](https://bioconductor.org/packages/release/bioc/vignettes/SEMPLR/inst/doc/SEMPLR.html)
- **License:** MIT
- **Status at GBCC2025:** methods talk on TF-binding variant effects (first major release — Bioc 3.23, v1.0.0)

## Talk at GBCC2025

- **Speakers:** Grace E Kenney, Rintsen N Sherpa, Alan P Boyle, Douglas H Phanstiel (University of Michigan)
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2B, Grace Auditorium (chair: Vincent Carey)
- **Talk title:** "SEMplR: An R package for predicting the effects of genetic variation on transcription factor binding"
- **Slides (Zenodo DOI):** *TBD — Zenodo deposits typically 2–4 weeks post-conference*
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

SEMPLR scores genomic locations and SNPs against SNP Effect Matrices — a per-TF representation of binding affinity that captures position-specific tolerance for substitutions. With 223 pre-computed SEMs in the box, a user can take a list of variants (GWAS hits, somatic mutations, eQTL fine-mapping outputs) and ask which TFs lose or gain binding at each site, plus look at TF-specific enrichment. The companion data package `SEMplR_data` ([github.com/rnsherpa/SEMplR_data](https://github.com/rnsherpa/SEMplR_data)) hosts the raw matrices.

## How it works

**Core idea.** A SNP Effect Matrix is a position-by-nucleotide table of *binding-affinity* scores rather than the frequency-derived probabilities used in a PWM/PFM. Each cell encodes the relative binding energetics for a nucleotide at that position, so SEMPLR slides the SEM across both strands of a variant's flanking sequence and reports the best-scoring window per TF.

**Inputs / outputs.** Input is a set of genomic coordinates (e.g. a `GRanges` of variants) plus a reference genome (`BSgenome.Hsapiens`). Output for each variant × TF pair is a raw `score`, a baseline-normalized `scoreNorm` (the binding vs. non-binding signal), and the `index` of the best-matching subsequence. Enrichment outputs are TF-level p-values across a query set.

**Key innovation.** Energy-based affinity scoring rather than frequency-based probability — SEMs are derived from experimental binding measurements, so they distinguish "frequent" from "preferred" nucleotides, which matters when scoring single-base substitutions that PWMs treat as roughly equivalent. Shipping 223 pre-computed SEMs makes it usable out of the box.

**Parameters worth knowing.**
- `nFlank` — nucleotides of flanking sequence around each query position (defaults to the minimum needed for the longest SEM).
- `seqId` — metadata column for unique variant identification.
- `threshold` — adjusted p-value cutoff (~0.05) for enrichment calls.
- `method` — clustering metric (e.g. `"WPCC"`) for SEM dendrogram visualizations.

**Canonical example.** The vignette scores chr12:94136009 by building `gr <- GRanges(seqnames="chr12", ranges=94136009)` and calling `scoreBinding(x=gr, sem=SEMC, genome=Hsapiens)`, yielding 446 predictions (223 TFs × 2 orientations). A downstream enrichment example mixes 200 JUN-derived sequences with 800 random ones and recovers JUN as significantly enriched (p<1e-167) — a positive-control validation of the matrix-scoring approach.

## Where it fits in the corpus

- **AACR 2026:** axis bioinfo-tools — regulatory variant interpretation is an upstream step for many cancer-genomics dossiers
- **EuroBioC2025:** ties into the TF-binding-prediction theme — Koen Van den Berge's *transfactor* talk on Day 1 PM is the deep-learning counterpart; SEMPLR is the classical-ML / matrix-scoring counterpart
- **ISMB 2026:** scaffold; gene regulation / TF-binding overlap
- **RECOMB 2026:** scaffold

## Notes

Boyle and Phanstiel labs are well-known for chromatin and 3D-genome work — SEMPLR is the variant-effect prediction surface of that program, packaged as classical-ML matrix scoring rather than a deep-learning model. First Bioconductor release (v1.0.0) — the GBCC talk is effectively the launch presentation.
