# Geneformer

**Family:** sc-fm
**Modality:** Single-cell RNA-seq (rank-encoded gene expression, human)
**Released:** 2023 (Nature); V2 update 2024
**License:** Apache-2.0
**Code/checkpoint:** [huggingface.co/ctheodoris/Geneformer](https://huggingface.co/ctheodoris/Geneformer)
**Also surfaced in:** agentic-ai, single-cell-spatial-omics, virtual-cells

> Geneformer is a transformer foundation model for single-cell
> transcriptomics from Christina Theodoris's group at Gladstone/UCSF
> that represents each cell as a rank-ordered list of its most
> distinctively expressed genes and learns gene-context relationships
> via masked language modeling. It is pretrained on Genecorpus-30M, a
> ~30 million-cell corpus assembled from public human scRNA-seq, and
> was the first widely adopted single-cell FM. Standout claims center
> on zero- and few-shot transfer to disease modeling, in-silico
> perturbation, and identifying candidate gene targets in
> data-limited settings such as cardiomyopathy.

## Architecture & training

Geneformer encodes a cell as the ranked list of its top expressed
genes (rank-value encoding, deprioritizing housekeeping genes) and
runs a BERT-style transformer encoder over that sequence. The
original V1 model (2023) is ~10M parameters with a 2,048-token input
and ~25K-gene vocabulary, pretrained with 15% masked-gene-prediction
on Genecorpus-30M (~30M human single-cell transcriptomes). V2 (2024)
scales to 104M and 316M parameter variants with a 4,096-token input,
restricts the vocabulary to ~20K protein-coding genes, and is
pretrained on a ~104M-cell expanded corpus, with a separate
14M-cell cancer-domain-tuned variant. Pretraining is fully
self-supervised and the released models are typically used either
zero-shot for embeddings/perturbation or fine-tuned on small labeled
sets.

## Use in the AACR 2026 corpus

<!-- mentions:start -->

**Posters mentioning Geneformer (n=4):**

- **2752** — *CancerSTFormer enables multi-scale analysis of spot-resolution spatial transcriptomes and dissects the gene and immune regulatory responses of targeted therapies*
  …results using the PD1-sensitive/resistant gene sets of the Holdout group. When compared against a fine-tuned Geneformer and a norefinement control, both Local and Extended CancerSTFormer variants consistently achieved higher accu…
- **5478** — *Benchmarking gene expression foundation models on bulk RNA-Seq data*
  …thods: We compared publicly available models with released weights, including six single-cell models (CellFM, GeneFormer, scBERT, scFoundation, scGPT, and scLong) and BulkFormer, a model trained on bulk RNA-seq data. Embeddings we…
- **978** — *Deep learning frameworks for translating cancer drug response from cell-level to patient-level by modeling transcriptome*
  …e can be also seen as transcriptomic cellular state change, we used an existing pre-trained rank-based model (Geneformer, Nature 2024). Given these models of transcriptomic changes, we model the cancer patient in two different app…
- **LB169** — *scCAP: An ontology-aware large language model framework for hierarchical and standardized single-cell type annotation*
  …remains challenging in single-cell RNA sequencing analysis. Existing tools (CellTypist, SCimilarity, SingleR, Geneformer) exhibit distinct biases and lack standardized nomenclature, hindering cross-study comparability. Furthermore…

**Sessions mentioning Geneformer (n=0):**

_No session transcripts in the AACR 2026 corpus mention this tool._

<!-- mentions:end -->

## What's missing / where evidence is weak

- **No primary application** — every poster mention treats Geneformer as a baseline to beat (poster 2752 CancerSTFormer outperforms a fine-tuned Geneformer; poster 5478 benchmarks it alongside five other single-cell FMs on bulk RNA-seq), as a generic rank-based reference (poster 978), or as a comparator that "exhibits distinct biases" (poster LB169 scCAP). The corpus contains no poster that uses Geneformer as the primary tool driving a discovery.
- **Zero session mentions.** Despite being one of the earliest single-cell FMs and frequently named alongside scGPT, Geneformer is absent from all 12 bioinfo-tools session transcripts.
- **No explicit V1-vs-V2 comparison.** The released 104M / 316M-parameter V2 variants and the 14M-cell cancer-domain-tuned model are not differentiated in any corpus mention; posters refer to "Geneformer" generically.
- **No in-silico perturbation or drug-target discovery work** — Geneformer's headline use case from the original Nature paper does not appear in any corpus entry.

## Takeaway

In AACR 2026, Geneformer is the canonical "previous-generation" single-cell foundation model: cited in four posters, but always as a benchmark baseline that newer methods (CancerSTFormer, scCAP, BulkFormer, custom rank-based pipelines) measure themselves against — never as the primary engine of a result. The corpus thus tells a consistent story across single-cell FMs: Geneformer set the template, and the field has moved on to larger or more domain-specific successors without abandoning it as a reference point.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** Geneformer is the encoder-only, rank-token branch of the single-cell FM family — distinguished from scGPT's decoder-style gene-value generation by discarding magnitude and learning only relative gene ordering. V1 (2023) was ~10M parameters; V2 (Dec 2024) released **104M and 316M parameter variants** under the names Geneformer-V2-104M and Geneformer-V2-316M, with a separate **Geneformer-V2-104M_CLcancer** continually pretrained on ~14M cancer cells. At 316M parameters, V2-Deep is the largest published rank-encoded scFM, and one of the two largest single-cell FMs of any kind (UCE at 650M is the only larger commonly cited model).

**Direct peers.**

| Model | Architecture | Pretraining corpus | Public weights | Headline benchmark |
| --- | --- | --- | --- | --- |
| Geneformer V2-316M | BERT encoder, rank-value tokens, 4,096-token input | 104M cells, ~20K protein-coding genes | Apache-2.0, HF | Top AUPRC on cancer-task suite (Helical Bio 2025 benchmark) |
| scGPT v1.0 | Decoder, gene-value tokens, ~51M params | 33M cells + 5.7M pan-cancer | MIT, Google Drive | Cell-type annotation + perturbation (Nature Methods 2024) |
| UCE | Encoder, protein-sequence-conditioned, 650M params | 36M cells, 8 species | MIT, GitHub | Strongest cross-dataset zero-shot embedding (Liu et al. 2025) |
| scFoundation | xTrimoGene encoder, continuous-value, 100M params | 50M human cells | Code MIT, weights gated | Tumor-tissue pooled-data benchmarks |
| CellPLM | Cell-as-token encoder, ~80M params | 11M cells with spatial context | MIT, GitHub | Spatial-aware cell-state inference |

**What changed in 2025-2026.** Three things. First, the V2 family is now the default — the HuggingFace `main` branch was retargeted to V2-316M, and V1 is preserved only as a legacy directory. Geneformer-V2-104M_CLcancer (the cancer continual-learning variant) **matched or exceeded the 316M deep model** on cancer benchmarks at one-third the parameter count, which inverted the "scale wins" narrative the field had assumed in 2024. Second, the same 2025 critique wave that hit scGPT (Kedzierska et al., *Genome Biology* 2025; Wenkel et al., *Nature Methods* 2025) hit Geneformer harder — its rank-encoding deliberately throws away expression magnitude, and benchmark studies show this leaves it behind UCE and scFoundation on most embedding-quality and zero-shot classification tasks. Third, no retraction or formal concern has been issued, and the license remains permissive (Apache-2.0).

**AACR-relevant use cases.** The corpus shows Geneformer in three distinct AACR-relevant modes: (1) **As a baseline to beat** — poster 2752 (CancerSTFormer) explicitly fine-tunes Geneformer as the comparator and reports their spatial transformer wins, the cleanest "old-FM-vs-new-method" framing in the meeting; (2) **As a rank-based feature extractor** — poster 978 cites Geneformer as the rank-based model anchoring their cell-to-patient drug-response framework; (3) **As a single-cell annotator under critique** — poster LB169 (scCAP) names Geneformer among tools that "exhibit distinct biases" in cell-type annotation. Notably absent: Geneformer's headline **in-silico perturbation / drug-target discovery** use case from the original Theodoris *Nature* 2023 paper does not appear in any 2026 abstract, despite this being the workflow most directly relevant to AACR's translational audience. No session transcripts mention Geneformer at all (n=0) — strikingly low for a model with 4 poster hits.
