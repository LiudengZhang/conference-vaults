# CellPLM

**Family:** sc-fm
**Modality:** Single-cell + spatially-resolved transcriptomics (cell-as-token; tissue-as-sentence)
**Released:** 2024 (ICLR)
**License:** BSD-2-Clause
**Code/checkpoint:** [github.com/OmicsML/CellPLM](https://github.com/OmicsML/CellPLM) (checkpoint `20230926_85M` via Dropbox link in repo)

> CellPLM is a single-cell pretrained language model from Jiliang
> Tang's group at Michigan State University that inverts the
> dominant single-cell-FM design: instead of treating *genes* as
> tokens and a single cell as a sentence, CellPLM treats *cells* as
> tokens and a *tissue* as the sentence. This lets a transformer
> attend across neighboring cells in a tissue context — the first
> single-cell FM to encode cell–cell relations explicitly. It is
> pretrained on ~9M scRNA-seq cells plus ~2M spatially-resolved
> transcriptomic (SRT) cells with a Gaussian-mixture prior over the
> cell-embedding space, and is reported to be ~100× faster at
> inference than gene-as-token FMs.

## What it does

CellPLM produces cell embeddings that incorporate not only the
focal cell's expression profile but also the gene-expression context
of its neighbors in a tissue (or its cohort within a batch for plain
scRNA-seq). The model is fine-tuned for cell-type annotation, gene
expression imputation (including imputing scRNA from spatial slices
and vice versa), and perturbation response — and the entire
pretrained model can be used zero-shot for spatial imputation.

## How it works

**Architecture.** CellPLM is a transformer encoder where each input
token is a *cell embedding* derived from its gene-expression vector,
not an individual gene. Many cells (sampled from a tissue / dataset)
are concatenated into one input sequence so the model attends across
cells. A Gaussian-mixture prior is imposed on the cell-embedding
latent space as an inductive bias to overcome the relative scarcity
of single-cell data vs. text ([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf); [OpenReview](https://openreview.net/forum?id=BKXvPDekud)).
For SRT inputs, 2D spatial coordinates are added through a positional
encoding, so the model can use physical neighborhood structure.

**Tokenization.** Cell-as-token. A cell's gene-expression vector
(masked positions filled with 0) is encoded by a gene-embedding
front-end into a single cell-level token vector; the transformer
then operates over a sequence of such cell tokens. Masked
positions are reconstructed at output — the masked-language-modeling
objective is over *gene-expression entries inside cells*, not over
held-out cell tokens ([Liu et al., *Advanced Science* 2025](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)).

**Pretraining corpus + objective.** Over 9 million scRNA-seq cells
plus over 2 million SRT cells, all human, are used for masked-language-modeling
pretraining ([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf)).
Including spatial cells with their (x, y) coordinates is what makes
the cell-cell attention biologically meaningful: neighbor cells in a
tissue genuinely share signaling context, so cross-token attention
has a substrate to learn from.

**Scale.** Approximately 80M+ parameters (the released checkpoint is
named `20230926_85M`) ([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf); [OmicsML/CellPLM README](https://github.com/OmicsML/CellPLM)).
Pretraining completed in under 24 hours on a single GPU server
([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf)).
The repo distributes weights via Dropbox under the BSD-2 license
([OmicsML/CellPLM README](https://github.com/OmicsML/CellPLM)).

**Fine-tuning recipe.** Standard pretrained-init + task-specific
loss: the pretrained encoder is initialized and either a
classification head (cell-type annotation), an imputation decoder
(scRNA / SRT imputation), or a perturbation head is added. For
spatial-transcriptomic imputation, the *entire pretrained model* can
be used zero-shot — no task-specific fine-tuning is required
([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf)).

**Downstream tasks evaluated.** Cell-type annotation on PBMC12K,
Pancreas, HLCA, Immune, Brain, and Liver datasets; scRNA-seq
expression imputation; spatial-transcriptomic imputation
(MERFISH-style, zero-shot); perturbation prediction
([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf); [OmicsML/CellPLM README](https://github.com/OmicsML/CellPLM)).

## Headline benchmarks

- **Cell-type annotation (intra-dataset).** CellPLM, scGPT, and
  Geneformer show comparable performance; CellPLM is among the
  top-three single-cell FMs by combined usability and accuracy in a
  systematic benchmark across nine open-source FMs and 29 datasets
  ([Liu et al., *Advanced Science* 2025](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)).
- **Cell-type annotation (inter-dataset transfer).** CellPLM, scGPT,
  Geneformer, tGPT, and UCE all outperform scBERT
  ([Liu et al., *Advanced Science* 2025](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)).
- **Inference speed.** CellPLM reports ~100× faster inference for
  generating cell embeddings than prior gene-as-token FMs
  ([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf); [ICLR poster page](https://iclr.cc/virtual/2024/poster/19221)).
- **Spatial imputation.** Pretrained CellPLM zero-shot beats published
  baselines on cross-modality SRT imputation; specific numerical
  margins are reported per dataset in the ICLR paper rather than as a
  single headline figure (unverified single-number summary — paper
  reports per-dataset MAE/Pearson rather than a single benchmark).

## Why it matters for AACR / virtual cells

CellPLM is the most credible single-cell FM positioned for *spatial
oncology* analyses, because (a) it explicitly models cell-cell
relations rather than treating each cell as i.i.d., and (b) its
zero-shot spatial-imputation capability fills in genes not measured
on commercial spatial platforms (Xenium, MERSCOPE) from a paired
scRNA reference. For AACR audiences building tumor-microenvironment
analyses, that is closer to a usable virtual-cell pipeline than the
gene-as-token FMs that ignore spatial context. CellPLM's
~100× inference speedup also lowers the barrier to embedding patient
cohorts on commodity hardware ([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf)).

## Known limitations / open questions

- **Smaller pretraining corpus than its peers.** ~9M scRNA-seq + ~2M
  SRT cells is well below scFoundation (50M+), Geneformer V2
  (~104M), or UCE's IMA (~36M) ([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf)).
  The Gaussian-prior inductive bias is positioned as a remedy, but
  scaling-law comparisons at fixed corpus are not reported.
- **Human-only.** Pretraining is human; mouse / PDX work is out of
  scope without retraining ([Wen et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf)).
- **Cell-as-token framing depends on batch composition.** Because the
  transformer attends across cells in an input sequence, embeddings
  for the same cell can drift when the surrounding cohort changes —
  a property the paper presents as a feature (context-awareness) but
  which complicates reproducibility of per-cell embeddings across
  pipelines (unverified quantification — paper does not benchmark
  embedding stability across input batches).
- **No tumor-pretrained variant.** Like scFoundation, CellPLM ships
  one pan-tissue checkpoint; no cancer-domain-tuned weights are
  released ([OmicsML/CellPLM README](https://github.com/OmicsML/CellPLM)).
- **Cell-type-annotation lead is narrow.** Head-to-head, CellPLM is
  not consistently #1 — it is consistently competitive with scGPT
  and Geneformer rather than dominant
  ([Liu et al., *Advanced Science* 2025](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)).

## Sources

- Paper: [Wen, Tang, Dai, Ding, Jin, Xie, Tang, "CellPLM: Pre-training of Cell Language Model Beyond Single Cells," ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/173bcdbd820edbe43284e0941109ada9-Paper-Conference.pdf)
- Preprint: [bioRxiv 2023.10.03.560734](https://www.biorxiv.org/content/10.1101/2023.10.03.560734v1)
- OpenReview record: [openreview.net/forum?id=BKXvPDekud](https://openreview.net/forum?id=BKXvPDekud)
- ICLR poster: [iclr.cc/virtual/2024/poster/19221](https://iclr.cc/virtual/2024/poster/19221)
- Code + weights: [github.com/OmicsML/CellPLM](https://github.com/OmicsML/CellPLM)
- PyPI package: [pypi.org/project/cellplm](https://pypi.org/project/cellplm/)
- External benchmark: [Liu et al., *Advanced Science* 2025 — single-cell FM utility evaluation](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202514490)
