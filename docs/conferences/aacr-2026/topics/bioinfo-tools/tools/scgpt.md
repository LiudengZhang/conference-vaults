# scGPT

**Family:** sc-fm
**Modality:** Single-cell RNA-seq (gene-expression value tokens)
**Released:** 2024 (Nature Methods)
**License:** MIT (code); checkpoints distributed via Google Drive under the same terms
**Code/checkpoint:** [github.com/bowang-lab/scGPT](https://github.com/bowang-lab/scGPT) (whole-human, organ-specific, and pan-cancer checkpoints)
**Also surfaced in:** agentic-ai, single-cell-spatial-omics, virtual-cells

> scGPT is a generative single-cell foundation model from the Bo Wang
> Lab at the University of Toronto that treats each cell as a sequence
> of gene–value tokens and pretrains a transformer to reconstruct
> masked expression values. It is trained on more than 33 million
> human cells from CELLxGENE and supports cell-type annotation,
> integration, perturbation prediction, and gene-regulatory inference
> after lightweight fine-tuning. Organ-specific (brain, blood, lung,
> heart, kidney) and pan-cancer (5.7M cells) checkpoints are released
> alongside the whole-human default.

## Architecture & training

scGPT uses a transformer encoder with a custom generative attention
mask: gene tokens are paired with binned expression-value tokens and
condition tokens (batch, modality), and the model is trained to
predict masked expression values given the unmasked context. The
flagship "whole-human" checkpoint is pretrained on ~33M normal human
cells aggregated from CELLxGENE; organ-specific variants range from
~0.8M to ~13M cells, and a pan-cancer variant is trained on ~5.7M
tumor cells. Fine-tuning uses a small task head for cell-type
classification, batch integration, or perturbation response, and the
paper reports competitive or improved performance over scBERT,
Geneformer, and scVI baselines across these tasks.

## Use in the AACR 2026 corpus

<!-- mentions:start -->

**Posters mentioning scGPT (n=2):**

- **4212** — *Baseline peripheral blood scRNA-seq AI estimator framework predicts solid-tumor response and adverse events via molecular foundation models and cell-to-patient learning*
  …e PBMC scRNA-seq counts (with optional cell-type annotations), pre-trained molecular foundation models (FMs) (scGPT v1.0 [1], scFoundation [2]), cell-to-patient Multi-Instance Learning (MIL) [3] with RECIST labels (CR/PR Resp…
- **5478** — *Benchmarking gene expression foundation models on bulk RNA-Seq data*
  …ble models with released weights, including six single-cell models (CellFM, GeneFormer, scBERT, scFoundation, scGPT, and scLong) and BulkFormer, a model trained on bulk RNA-seq data. Embeddings were extracted following each m…

**Sessions mentioning scGPT (n=1):**

- [2026-04-20-am-ai-revolution-in-cancer-research](../../../sessions/2026-04-20-am-ai-revolution-in-cancer-research.md)
  …k and send us any feedbacks you may have. All right, so what's next? I talk about virtual cell models such as scGPT and ExCell. I talk about bioreason models, particularly bioreasons through DNA sequences, bioreasons through…

<!-- mentions:end -->

## What's missing / where evidence is weak

- **The pan-cancer checkpoint is absent.** Despite a 5.7M tumor-cell pan-cancer variant being released alongside the whole-human default, no corpus mention uses or evaluates it. Both poster mentions reach for the v1.0 whole-human checkpoint or a generic "scGPT" baseline.
- **No fine-tuning protocol detail in the corpus.** Poster 4212 (PBMC peripheral-blood AI estimator) calls out scGPT v1.0 as a feature extractor, and poster 5478 benchmarks it, but neither describes fine-tuning hyperparameters, organ-specific checkpoint choice, or perturbation evaluation.
- **The session mention is a name-check.** The April-20 AI Revolution session lists scGPT alongside ExCell as "virtual cell models" without methodological detail; it adds no evidence beyond the posters.
- **No tumor-microenvironment or perturbation work.** scGPT's headline capabilities (perturbation prediction, GRN inference) do not appear in any corpus mention.

## Takeaway

scGPT is present in AACR 2026 as a representative single-cell foundation model — invoked in two posters and one session — but always as a context entry in a foundation-model lineup (typically alongside scFoundation or Geneformer) rather than as the primary engine of an analysis. The corpus pattern mirrors Geneformer's: scGPT is widely *known* and consistently *named*, but no AACR 2026 contribution leans on its generative or perturbation capabilities to drive a finding.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** scGPT is a generative, decoder-style transformer in the single-cell FM family — distinguished from Geneformer (encoder-only, rank-based) and Cell2Location (Bayesian, not an FM at all) by a gene-value tokenization that lets it run masked expression *regression* rather than just rank-token masking. The flagship whole-human checkpoint is ~51M parameters, with a 53M-parameter pan-cancer variant and several organ-specific releases; this puts scGPT at the smaller end of the modern single-cell FM cohort (UCE: 650M; scFoundation: 100M; CellPLM: 80M; Geneformer-V2-Deep: 316M).

**Direct peers.**

| Model | Architecture | Pretraining corpus | Public weights | Headline benchmark |
| --- | --- | --- | --- | --- |
| scGPT v1.0 | Decoder transformer, gene-value tokens, ~51M params | 33M human cells (CELLxGENE) + 5.7M pan-cancer variant | MIT, Google Drive | Cell-type annotation, integration, perturbation (Nature Methods 2024) |
| UCE (Universal Cell Embeddings) | Encoder transformer, protein-sequence-conditioned gene embeddings, 650M params | 36M cells, 8 species | MIT, GitHub + HF | Strongest cross-dataset zero-shot embedding in 2025 scFM benchmarks |
| scFoundation | xTrimoGene encoder, continuous-value embedding, 100M params | 50M human cells | Code MIT, weights gated | Tumor-tissue tasks (best in pooled-data eval) |
| GET | Sequence + chromatin-accessibility transformer | 213 fetal/adult cell types (multi-omics) | MIT, GitHub | Cross-cell-type expression prediction (Nature 2025) |
| CellPLM | Cell-as-token encoder, ~80M params | 11M cells with spatial context | MIT, GitHub | Spatial-context cell-state inference |

**What changed in 2025-2026.** Three things matter. First, the Bo Wang lab released **scGPT-spatial** (bioRxiv Feb 2025), a continually pretrained variant on SpatialHuman30M (~30M spatial profiles) with a Mixture-of-Experts decoder for protocol-aware deconvolution and imputation — the spatial successor that AACR 2026 has not yet caught up to. Second, **a series of 2025 benchmark papers** (Kedzierska et al., *Genome Biology* 2025; Wenkel et al., *Nature Methods* 2025) showed that scGPT, Geneformer, and scFoundation **do not outperform simple linear baselines on perturbation prediction** and have weak zero-shot embedding quality — a credibility hit that has not surfaced in any AACR 2026 poster framing. Third, the scGPT-cancer (pan-cancer) checkpoint has been reported to *underperform* the generic whole-human checkpoint on several non-cancer tasks, raising the question of whether domain-specific continual pretraining was worth the 5.7M-cell investment. No formal retraction or concern flag has been issued on the published paper.

**AACR-relevant use cases.** Three live use modes appear in the 2026 corpus or are visible immediately adjacent to it: (1) **PBMC response prediction** — poster 4212 uses scGPT v1.0 + scFoundation embeddings as MIL features to predict RECIST response from peripheral-blood scRNA-seq, the only "primary engine" usage in the corpus; (2) **Bulk-RNA-seq benchmarking** — poster 5478 evaluates scGPT alongside five other scFMs on bulk-RNA-seq embeddings, an off-label use that the recent zero-shot critique literature would predict to fail; (3) **Virtual-cell scaffolding** — the [April 20 AI Revolution session](../../../sessions/2026-04-20-am-ai-revolution-in-cancer-research.md) name-checks scGPT alongside ExCell as a virtual-cell substrate, framing it as a building block for cell-simulation agents rather than an end-user analysis tool. The pan-cancer 5.7M-cell checkpoint and scGPT-spatial are absent from both posters and sessions — a substantive gap given that scGPT-spatial would directly compete with Cell2Location on spot-resolution deconvolution.
