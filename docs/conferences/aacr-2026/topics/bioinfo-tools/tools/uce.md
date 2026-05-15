# UCE

**Family:** sc-fm
**Modality:** Single-cell RNA-seq (cross-species; ESM2 protein-embedding gene tokens)
**Released:** 2023 (bioRxiv)
**License:** MIT (code)
**Code/checkpoint:** [github.com/snap-stanford/UCE](https://github.com/snap-stanford/UCE) (4-layer default auto-downloads; 33-layer flagship via Figshare); model card on the [CZI Virtual Cells Platform](https://virtualcellmodels.cziscience.com/model/uce)

> UCE (Universal Cell Embedding) is a single-cell foundation model from
> the Leskovec and Quake groups at Stanford (with collaborators at
> Genentech) that learns a species-agnostic embedding space by
> tokenizing genes through their ESM2 protein representations rather
> than as integer IDs. Trained self-supervised on cell atlas data
> spanning eight species, UCE produces zero-shot cell embeddings that
> transfer across tissues and to previously unseen species, and is the
> engine behind the Integrated Mega-scale Atlas (IMA) of ~36M cells.

## What it does

UCE turns any single-cell transcriptome — human, mouse, or a species
the model has never seen — into a fixed-dimensional embedding without
any task-specific fine-tuning. Because gene tokens are derived from
the underlying protein sequence via ESM2, orthologs across species map
to similar positions in the input space, so cell-type structure
transfers zero-shot from well-studied to under-sampled organisms.
The released checkpoints are typically used as a frozen feature
extractor for clustering, label transfer, and atlas integration.

## How it works

**Architecture.** UCE is a transformer encoder. The flagship paper
checkpoint has 33 layers and over 650 million parameters; a smaller
4-layer variant ships as the GitHub default for users without
multi-GPU resources ([Rosen et al., bioRxiv 2023](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2); [snap-stanford/UCE README](https://github.com/snap-stanford/UCE)).

**Tokenization.** Each gene is represented by the ESM2 protein
language-model embedding of the protein it encodes (ESM2 is a 15B-parameter
protein LM operating on amino-acid sequences), with a chromosome
positional token and a species token concatenated. A cell is
then encoded as a *sampled bag of expressed genes* — UCE draws genes
with replacement, weighted by their expression value — rather than as
a ranked list or fixed-length vector ([Rosen et al., bioRxiv 2023](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2)).
This design lets the model accept any gene set from any species
without retraining the vocabulary.

**Pretraining corpus + objective.** UCE is trained self-supervised,
without any cell-type labels, on cell atlases from human and seven
other species (eight species total) ([Rosen et al., bioRxiv 2023](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2)).
The objective is a binary masked-gene-presence task: given a sampled
subset of a cell's expressed genes, predict which other genes from a
candidate set are also expressed in that cell. This contrastive-style
objective avoids quantitative reconstruction of expression values and
emphasizes which genes co-occur in a cellular context.

**Scale.** 33 layers, ~650M parameters for the flagship; pretraining
GPU-hours are not stated in the preprint (unverified — paper does not
report wall-clock training cost). Inference of the 33-layer model
requires a multi-GPU node; the 4-layer model fits on a single GPU
([snap-stanford/UCE README](https://github.com/snap-stanford/UCE)).

**Fine-tuning recipe.** UCE is positioned as a *zero-shot* model:
the standard workflow is to run a single forward pass over a query
AnnData and use the cell embeddings directly for downstream
clustering, label transfer (e.g. k-NN against a labeled reference),
or visualization. No fine-tuning code is provided in the official
repository, and the paper's headline results are zero-shot.

**Downstream tasks evaluated.** Cell-type annotation by label transfer,
cross-species cell-type matching, batch integration on the scIB
benchmark, and construction of the Integrated Mega-scale Atlas — a
joint embedding of ~36M cells, >1,000 named cell types, spanning
dozens of tissues and eight species ([Rosen et al., bioRxiv 2023](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2)).

## Headline benchmarks

- **scIB cell-embedding benchmark (zero-shot).** UCE reportedly
  outperforms the next-best foundation model (Geneformer) by 13.9%
  on overall score, 16.2% on biological-conservation score, and 10.1%
  on batch-correction score ([Rosen et al., bioRxiv 2023](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2)).
- **Per-cell-type win rate (zero-shot).** UCE beats Geneformer on
  80% of cell types, tGPT on 73%, and scGPT on 83% in the original
  paper's evaluation ([Rosen et al., bioRxiv 2023](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2)).
- **Perturbation prediction (third-party).** When evaluated outside
  its design envelope on the Adamson/Norman/Replogle perturbation
  benchmarks, UCE — like scGPT (0.641/0.554/0.327/0.596 Pearson-Delta)
  and scFoundation (0.552/0.459/0.269/0.471) — fails to beat a simple
  "predict the training-set mean" baseline that scores 0.711/0.557/0.373/0.628
  ([Ahlmann-Eltze et al., *Nature Methods* 2025](https://www.nature.com/articles/s41592-025-02772-6)).
  This is a class-wide limitation of single-cell FMs, not unique to UCE,
  but worth flagging for cancer-perturbation use cases.

## Why it matters for AACR / virtual cells

UCE's species-agnostic tokenization is the cleanest published answer
to a problem AACR audiences face every day: mouse models do not share
gene IDs with human tumors, and PDX or syngeneic-model scRNA-seq is
hard to project into a human reference. UCE's ESM2-grounded gene
embeddings sidestep ortholog-mapping pipelines entirely, making it a
natural backbone for cross-species cancer cell-of-origin questions
and for harmonizing mouse perturbation screens with human atlases. It
is also one of two published single-cell FMs (with scGPT) that the
CZI Virtual Cells Platform packages as a hosted model card for the
"virtual cell" research program ([CZI Virtual Cells Platform](https://virtualcellmodels.cziscience.com/model/uce)).

## Known limitations / open questions

- **No native fine-tuning workflow.** The model is designed for
  zero-shot use; users who want task-specific adaptation must wire up
  their own head and risk catastrophic forgetting of the
  cross-species embedding geometry.
- **Inference cost.** The 33-layer flagship requires multi-GPU
  inference and is impractical for sample-level workflows without
  caching embeddings ([snap-stanford/UCE README](https://github.com/snap-stanford/UCE)).
- **Perturbation prediction is out of scope.** Third-party benchmarks
  show UCE (alongside scGPT, scFoundation, Geneformer) loses to
  linear baselines on perturb-seq response prediction
  ([Ahlmann-Eltze et al., *Nature Methods* 2025](https://www.nature.com/articles/s41592-025-02772-6)).
- **Tumor-cell coverage is underrepresented.** IMA is biased toward
  normal cell atlases; the paper does not report a dedicated cancer
  evaluation (unverified — paper claims general transfer, but no
  pan-cancer benchmark is reported).
- **Still a preprint at time of writing.** The work has circulated as
  a bioRxiv preprint since November 2023; a peer-reviewed venue is
  not confirmed in the public record we surveyed (unverified — paper
  remains on bioRxiv).

## Sources

- Paper: [Rosen, Roohani, Agarwal, et al., "Universal Cell Embeddings: A Foundation Model for Cell Biology," bioRxiv 2023.11.28.568918](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v2)
- Code: [github.com/snap-stanford/UCE](https://github.com/snap-stanford/UCE)
- Hosted model card / weights: [CZI Virtual Cells Platform — UCE v1.0](https://virtualcellmodels.cziscience.com/model/uce)
- External benchmark: [Ahlmann-Eltze et al., *Nature Methods* 2025 — perturbation-prediction FM evaluation](https://www.nature.com/articles/s41592-025-02772-6)
