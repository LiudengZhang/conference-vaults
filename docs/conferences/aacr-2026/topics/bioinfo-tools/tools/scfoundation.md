# scFoundation

**Family:** sc-fm
**Modality:** Single-cell RNA-seq (continuous-valued, ~20K-gene vocabulary, human)
**Released:** 2024 (Nature Methods)
**License:** Apache-2.0 (code); separate model-weight license
**Code/checkpoint:** [github.com/biomap-research/scFoundation](https://github.com/biomap-research/scFoundation)
**Also surfaced in:** agentic-ai, single-cell-spatial-omics, virtual-cells

> scFoundation (xTrimoscFoundationα) is a 100M-parameter single-cell
> foundation model from BioMap / Tencent AI Lab and Tsinghua
> University, built on the xTrimoGene asymmetric encoder–decoder
> transformer. It is the first single-cell FM at the 100M scale that
> jointly models ~20,000 genes in a continuous-valued (non-binned)
> representation, and it introduces a Read-Depth-Aware (RDA)
> pretraining task that lets the model project low-quality cells onto
> the manifold of high-depth cells. Pretrained on 50M+ human single-cell
> transcriptomes, it claims state-of-the-art transfer to perturbation
> prediction, drug-response prediction, and read-depth enhancement.

## What it does

scFoundation produces cell- and gene-context embeddings from raw
single-cell expression vectors and is designed to be plugged into
downstream architectures — GEARS for perturbation, DeepCDR / SCAD for
drug response — as a frozen or lightly fine-tuned feature extractor.
The RDA pretraining task means the model has been explicitly trained
to map a downsampled (low-read-depth) cell to the same embedding as
its high-depth counterpart, which is useful when shallow scRNA-seq is
all that's available.

## How it works

**Architecture.** scFoundation uses the *xTrimoGene* backbone: an
asymmetric encoder–decoder transformer where the encoder is a
vanilla-transformer block that processes only nonzero, nonmasked
genes (a small, information-dense subset), and the decoder is a
Performer (linear-attention) block that operates over all ~20K genes
([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7); [xTrimoGene preprint](https://arxiv.org/html/2311.15156v2)).
This asymmetry keeps the heavy compute on the sparse input while
still producing a full-length output. An embedding module converts
continuous gene-expression scalars into learnable high-dimensional
vectors so the model can ingest raw counts rather than binned tokens
([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7)).

**Tokenization.** Genes are addressed by a fixed 19,264-gene index
(`OS_scRNA_gene_index.19264.tsv`) — a continuous-valued vocabulary
where each cell is a (gene, scalar-expression) pair list, not a
ranked or binned sequence ([biomap-research/scFoundation README](https://github.com/biomap-research/scFoundation)).

**Pretraining corpus + objective.** Pretraining uses over 50 million
human single-cell transcriptomic profiles ([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7)).
The novel objective is Read-Depth-Aware (RDA) pretraining: each
training pair consists of a masked expression vector plus two
total-count indicators T and S (target depth and source depth). The
model is asked to recover the masked expression at the target depth
T given an input downsampled to depth S — so RDA simultaneously
performs (a) traditional masked-token reconstruction and (b) a
denoising / depth-enhancement task that maps shallow profiles to
deep ones ([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7); [HyperAI commentary](https://hyper.ai/en/news/32623)).

**Scale.** The authors trained scFoundation at three sizes — 3M, 10M,
and 100M parameters — and report that masked-expression-prediction
quality scales monotonically with parameter count ([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7)).
The flagship 100M-parameter checkpoint covers ~20,000 genes.
Pretraining wall-clock GPU-hours are not stated in the manuscript
(unverified — paper does not report total training cost).

**Fine-tuning recipe.** scFoundation is positioned as a *plug-in
embedding service* for task-specific models. For perturbation, the
recipe is GEARS-with-scFoundation-embeddings (the scFoundation
encoder produces 19,264 × 512 gene-context embeddings that are fed
into GEARS as the gene-relation graph). For drug response, embeddings
are inserted into DeepCDR (bulk RNA-seq → drug IC50) or SCAD
(single-cell drug sensitivity). The repository ships scripts for each
of these stacks ([biomap-research/scFoundation README](https://github.com/biomap-research/scFoundation)).

**Downstream tasks evaluated.** Read-depth enhancement, drug response
prediction (DeepCDR, SCAD), perturbation prediction (GEARS), gene
module inference, cell mapping / integration, and cell-type
annotation ([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7); [biomap-research/scFoundation README](https://github.com/biomap-research/scFoundation)).

## Headline benchmarks

- **Perturbation prediction (GEARS + scFoundation).** scFoundation
  embeddings reportedly improve GEARS Pearson-Delta on the
  Adamson/Norman/Replogle benchmarks vs. the GEARS baseline alone
  ([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7)).
  Third-party re-evaluation, however, finds that scFoundation reaches
  only 0.552 / 0.459 / 0.269 / 0.471 Pearson-Delta on
  Adamson / Norman / Replogle-K562 / Replogle-RPE1 respectively —
  *worse* than a Train-Mean baseline (0.711 / 0.557 / 0.373 / 0.628)
  and worse than scGPT on most splits (0.641 / 0.554 / 0.327 / 0.596)
  ([Ahlmann-Eltze et al., *Nature Methods* 2025](https://www.nature.com/articles/s41592-025-02772-6)).
- **Cell-type annotation.** In a head-to-head benchmark, the top
  three single-cell FMs by combined usability + accuracy are scGPT,
  CellPLM, and Geneformer — with scFoundation reported as competitive
  but not dominant on intra-dataset annotation
  ([Liu et al., *Advanced Science* 2025](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)).
- **Scale law.** Within the scFoundation family, the 100M variant
  outperforms 10M and 3M variants on masked-expression prediction
  monotonically ([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7)).

## Why it matters for AACR / virtual cells

scFoundation is the most-cited single-cell FM at the 100M-parameter
scale that ships drug-response stacks (DeepCDR, SCAD) out of the box,
which is directly aligned with the AACR audience's interest in
translating cell-state models into IC50 or RECIST predictors. The RDA
pretraining task is also a practical fit for clinical scRNA-seq,
which is often shallower than research-grade cell atlases — RDA
embeddings should, in principle, be more robust to PBMC samples
generated under hospital-throughput conditions. Both
features explain why AACR 2026 posters pair scFoundation with scGPT
when building patient-response classifiers.

## Known limitations / open questions

- **Perturbation gains contested.** Independent benchmarks find that
  scFoundation underperforms a Train-Mean baseline on standard
  Perturb-seq splits ([Ahlmann-Eltze et al., *Nature Methods* 2025](https://www.nature.com/articles/s41592-025-02772-6)).
- **Pretraining cost not reported.** The Nature Methods paper does
  not state pretraining GPU-hours or hardware
  (unverified — paper does not report).
- **Human-only.** Unlike UCE, scFoundation is trained on human
  transcriptomes only; mouse / PDX work requires separate handling
  ([Hao et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7)).
- **Model-weight license is separate from code.** The Apache-2.0
  license covers code; the model checkpoint is distributed under its
  own "Model License" agreement, which users must accept before
  commercial use ([biomap-research/scFoundation README](https://github.com/biomap-research/scFoundation)).
- **No tumor-pretrained variant.** Unlike scGPT (which ships a 5.7M-cell
  pan-cancer checkpoint), scFoundation's released weights are a single
  pan-tissue model — there is no cancer-domain-tuned variant to
  benchmark against (unverified — repository lists only the 100M
  pan-tissue checkpoint at the time of writing).

## Sources

- Paper: [Hao, Gong, Zeng, et al., "Large-scale foundation model on single-cell transcriptomics," *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02305-7)
- Preprint (full PDF): [bioRxiv 2023.05.29.542705](https://www.biorxiv.org/content/10.1101/2023.05.29.542705v4.full.pdf)
- Backbone paper: [xTrimoGene preprint, arXiv 2311.15156](https://arxiv.org/html/2311.15156v2)
- Code: [github.com/biomap-research/scFoundation](https://github.com/biomap-research/scFoundation)
- External benchmark: [Ahlmann-Eltze et al., *Nature Methods* 2025 — perturbation-prediction FM evaluation](https://www.nature.com/articles/s41592-025-02772-6)
- External benchmark: [Liu et al., *Advanced Science* 2025 — single-cell FM utility evaluation](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)
