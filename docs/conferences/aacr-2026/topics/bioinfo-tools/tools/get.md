# GET

**Family:** regulatory-fm
**Modality:** Single-cell ATAC-seq peaks (motif × peak matrix) + DNA sequence; cell-type-resolved
**Released:** 2025 (Nature)
**License:** open-source via GET-Foundation GitHub organization
**Code/checkpoint:** [github.com/GET-Foundation](https://github.com/GET-Foundation)

> GET (General Expression Transformer) is a foundation model for
> transcriptional regulation from Xi Fu in the Rabadan lab at
> Columbia, with Shentong Mo from Eric Xing's group at CMU / MBZUAI.
> It learns cell-type-specific regulatory grammar from chromatin
> accessibility (scATAC-seq) and DNA sequence alone, and predicts
> gene expression — even in held-out cell types — with reported
> experimental-level accuracy. Unlike scGPT / Geneformer /
> scFoundation, GET does *not* take an RNA-expression cell as input;
> it takes the *regulatory state* of a cell and reads out what that
> cell should be transcribing.

## What it does

Given a cell type's scATAC-seq accessibility profile, GET predicts
which genes that cell type will express, in a sequence-aware way:
each gene's prediction is computed from the model's view of the
~2 Mbp region around its locus. The model also enables in-silico
perturbation of transcription-factor (TF) motifs to identify causal
regulators, and it generalizes zero-shot to cell types not in the
pretraining set, including held-out fetal lineages and disease
states.

## How it works

**Architecture.** GET is a 12-layer transformer encoder. The input
is a (regions × motifs) tensor — for each of R accessible peaks in a
~2 Mbp window, a motif-presence vector of length M (the quantitative
ATAC signal can optionally be appended to M). A `RegionEmb` layer
projects this into a D-dimensional latent (shape: B × R × D); 12
transformer encoder layers then mix information across regions; a
linear projection plus SoftPlus activation produces the per-region
output (B × R × O), which is summed/aggregated to a gene-level
expression prediction ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z); [Fu et al., PMC PMC11244937](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244937/)).

**Tokenization.** Each token is an *accessible region* (an
scATAC-seq peak), not a gene. The token's content is the offline
motif-matching vector for that peak's DNA sequence (B, R, L\*, 4 → B,
R, M after motif convolution), optionally augmented with the peak's
quantitative accessibility signal ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z)).
Switching cell types means swapping the accessibility vector at
input time — the model itself is shared across all cell types.

**Pretraining corpus + objective.** GET is pretrained on a human
single-cell ATAC-seq atlas covering 213 fetal and adult cell types
([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z); [Carnegie Mellon press release](https://www.cs.cmu.edu/news/2025/gene-expression)).
The self-supervised objective is *random masked-region pretraining*:
mask out the motif vectors for a subset of accessible peaks and have
the model reconstruct them from the surrounding peaks. After
pretraining, the model is fine-tuned on paired scATAC + scRNA data
to map regulatory syntax to expression, with the gene-expression head
trained on held-in cell types and evaluated on held-out ones.

**Scale.** 12 transformer encoder layers over a ~2 Mbp locus window.
The paper does not report a single headline parameter count
(unverified — exact parameter count not stated in the main text);
inputs span more than 2 megabases of genomic context per locus.

**Fine-tuning recipe.** Two-stage: (1) masked-region pretraining
across all 213 cell types using ATAC peaks alone, (2) supervised
fine-tuning on paired scATAC + scRNA-seq for gene-expression
prediction, with leave-one-cell-type-out evaluation for
generalization. For zero-shot reporter-assay prediction, GET is run
without further fine-tuning ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z)).

**Downstream tasks evaluated.** Cell-type-specific gene expression
prediction (held-in and held-out cell types); cis-regulatory element
identification; transcription-factor interaction inference; in-silico
perturbation of TF motifs; lentivirus-based massively parallel
reporter assay (MPRA) readout prediction (zero-shot); upstream
regulator identification for fetal haemoglobin; identification of
leukemia-risk TF interactions in B cells ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z); [GEN news coverage](https://www.genengnews.com/topics/artificial-intelligence/ai-foundation-model-predicts-gene-activity-in-human-cells/)).

## Headline benchmarks

- **Cell-type-specific gene expression.** GET achieves
  experimental-level accuracy in predicting gene expression in both
  seen and held-out cell types using only chromatin accessibility +
  sequence ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z); [PMC PMC11244937](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244937/)).
- **Cis-regulatory element identification.** GET outperforms prior
  state-of-the-art on identifying cis-regulatory elements, including
  distal regulatory regions missed by earlier models in fetal
  erythroblasts ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z)).
- **Zero-shot MPRA readout.** GET outperforms current models in
  predicting lentivirus-based massively parallel reporter assay
  results without any task-specific training ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z)).
- **Disease application.** In B cells, GET identifies a
  lymphocyte-specific TF interaction that explains the functional
  significance of a leukemia-risk germline mutation
  ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z); [Columbia CUIMC press release](https://www.cuimc.columbia.edu/news/new-ai-predicts-inner-workings-cells)).

Note: GET is not directly comparable to scGPT / Geneformer on cell-
type annotation because it does not take an expression vector as
input. Comparisons in the literature instead pit GET against
Enformer-class sequence-to-expression models on the regulatory-element
side, where GET reports state-of-the-art ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z)).

## Why it matters for AACR / virtual cells

GET is the cleanest published bridge between the *epigenomic* virtual-
cell agenda (cell-type-specific chromatin landscapes) and downstream
*expression* predictions, which makes it uniquely useful for cancer
risk-variant interpretation. The B-cell leukemia example in the
Nature paper is a template AACR-relevant workflow: take a GWAS
variant of unknown significance, ask GET to score its effect on
TF-motif accessibility in the relevant cell type, and read out the
predicted downstream-expression change in silico. For solid tumors,
GET's generalization to held-out cell types is a route to scoring
regulatory variants in cell types that lack scRNA reference atlases
but do have ATAC data.

## Known limitations / open questions

- **Requires scATAC-seq input.** GET cannot operate on bulk RNA-seq
  or scRNA-seq alone — applications without matched accessibility
  data are out of scope ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z)).
- **Human-only.** The pretraining atlas covers 213 *human* fetal and
  adult cell types; cross-species transfer is not reported
  ([Fu et al., *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z)).
- **Cancer cell-type coverage is uneven.** The pretraining atlas
  emphasizes fetal and normal adult tissues; tumor-derived ATAC
  cell types are likely underrepresented (unverified — paper does
  not report a tumor-specific subset).
- **Parameter count is not headline-reported.** The main text does
  not surface a single parameter number, which makes
  apples-to-apples scaling-law comparison with scGPT / scFoundation
  difficult (unverified — only architectural shape, 12 layers, is
  stated).
- **Resolution is at the peak, not the base.** Tokens are accessible
  regions, so single-base-pair regulatory effects (e.g. fine-grained
  variant interpretation inside a single motif) must be re-encoded
  through motif-presence features.

## Sources

- Paper: [Fu, Mo, Buendia, et al., "A foundation model of transcription across human cell types," *Nature* 2025](https://www.nature.com/articles/s41586-024-08391-z)
- Open-access PMC version: [Fu et al., PMC PMC11244937](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244937/)
- Preprint: [bioRxiv 2023.09.24.559168](https://www.biorxiv.org/content/10.1101/2023.09.24.559168v2.full)
- Code: [github.com/GET-Foundation](https://github.com/GET-Foundation)
- Press: [Columbia CUIMC — "New AI Predicts Inner Workings of Cells"](https://www.cuimc.columbia.edu/news/new-ai-predicts-inner-workings-cells)
- Press: [Carnegie Mellon — "Using AI To Predict Gene Expression"](https://www.cs.cmu.edu/news/2025/gene-expression)
