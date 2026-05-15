# Prov-GigaPath

**Family:** path-fm
**Modality:** H&E whole-slide image tiles (256×256 at 20×, resized to 224 for the ViT) plus a slide-level encoder
**Released:** 2024 (Nature)
**License:** Code Apache-2.0; model weights gated, non-commercial research only (Microsoft Research / Providence terms)
**Code/checkpoint:** [github.com/prov-gigapath/prov-gigapath](https://github.com/prov-gigapath/prov-gigapath); checkpoint on HuggingFace ([prov-gigapath/prov-gigapath](https://huggingface.co/prov-gigapath/prov-gigapath))
**Also surfaced in:** single-cell-spatial-omics, virtual-cells

> Prov-GigaPath is a whole-slide pathology foundation model from
> Microsoft Research and Providence Health that pairs a tile-level
> encoder with a slide-level aggregator, so a single forward pass can
> turn an entire gigapixel slide into a fixed-length representation.
> It is pretrained on more than 1.3 billion tiles from over 170,000
> real-world H&E slides drawn from 31 Providence-affiliated hospitals,
> making it one of the largest published pathology corpora to date.
> The Nature 2024 paper claims state-of-the-art results across cancer
> subtyping, mutation prediction, and pathology-genomics retrieval.

## Architecture & training

The tile encoder is a ViT-style backbone trained with DINOv2-style
self-supervision on roughly 1.3 billion 256×256 H&E patches sampled
from 171,189 whole-slide images. The slide-level encoder uses a
LongNet-based dilated-attention transformer that ingests the full
sequence of tile tokens for a slide (tens of thousands per WSI) and
is pretrained with a masked tile-modeling objective, producing a
single slide embedding without needing weakly supervised MIL. The
public checkpoint comprises both the tile and slide encoders; the
authors report improved performance over UNI, CTransPath, and other
pathology backbones across 26 downstream clinical and biomarker
tasks.

## Use in the AACR 2026 corpus

<!-- mentions:start -->

**Posters mentioning Prov-GigaPath (n=2):**

- **1457** — *Prediction of gene expression and molecular pathway activity from H&E whole slide images in non-small cell lung cancer*
  …ted internal dataset of 67 commercial non-small cell lung cancer (NSCLC) patient samples with matched RNA-seq.Gigapath, a large-scale pathology foundation model pre-trained on over 170,000 WSIs, was used to extract patch and pat…
- **1470** — *Selecting representative histologic sections for cost-efficient 3D spatial transcriptomics and tumor microenvironment reconstruction*
  …mune aggregates, and mucosa&#8212;were segmented using a graph neural network. For each section, we extracted Prov-GigaPath embeddings and tissue class area proportions. Pairwise similarities, incorporating histology features and z-d…

**Sessions mentioning Prov-GigaPath (n=1):**

- [2026-04-20-am-decoding-cancer-ecosystem-pathology-tme-heterogeneity](../../../sessions/2026-04-20-am-decoding-cancer-ecosystem-pathology-tme-heterogeneity.md)
  …get a lot of those related image. For example, that's how, for example, Gabriele and team build on using the gigapath to actually model sort of pathology slide. They are using in just specific kind of scenario that are very dif…

<!-- mentions:end -->

## What's missing / where evidence is weak

- **Only the tile encoder is being used.** Both poster mentions (1457 NSCLC gene expression; 1470 3D spatial-transcriptomics tile selection) extract patch / tile embeddings — neither exercises the LongNet slide-level encoder that is Prov-GigaPath's actual architectural contribution.
- **No head-to-head benchmark in the corpus.** None of the posters compare Prov-GigaPath against UNI / UNI2-h or CONCH on a shared task; the choice of backbone reads as convenience, not the result of evaluation.
- **The session mention is glancing.** The April-20 session reference is a name-drop ("using gigapath to … model pathology slide") with no method detail, so it adds no evidence beyond the posters.
- **No discussion of the gated weights or non-commercial terms** in any corpus mention, despite this being a real adoption barrier for industry-adjacent work.

## Takeaway

Prov-GigaPath shows up as a working tile-feature backbone in two specialized methods posters — gene-expression prediction from H&E in NSCLC, and tile-similarity-based section selection for 3D spatial transcriptomics — plus one passing session reference. The AACR 2026 corpus thus uses Prov-GigaPath the same way it uses UNI: as a frozen patch encoder feeding a downstream model. The slide-level LongNet encoder, which is the paper's main novelty, never appears in the corpus, suggesting that even where Prov-GigaPath is preferred over UNI, it is not yet preferred *because of* its slide-level capability.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** Prov-GigaPath is the **two-stage (tile + slide) encoder** in the pathology FM family — a ViT-style DINOv2 tile encoder paired with a LongNet dilated-attention slide encoder, which is its architectural differentiator from the encoder-only UNI / UNI2-h / Virchow line. At ~1.1B parameters total (the LongNet slide encoder adds substantial weight on top of the ViT tile backbone) it sits between UNI2-h (681M) and Virchow2G (1.85B). The 1.3B-tile / 171K-WSI Providence corpus is one of the three largest pathology pretraining datasets, alongside Paige's 3.1M-WSI Virchow2 corpus and the Mahmood Lab's 350K-WSI UNI2 corpus.

**Direct peers.**

| Model | Architecture | Pretraining corpus | Public weights | Headline benchmark |
| --- | --- | --- | --- | --- |
| Prov-GigaPath | DINOv2 ViT tile + LongNet slide encoder | 1.3B tiles, 171K WSIs (Providence) | Apache-2.0 code, gated HF weights, non-commercial | 26-task SOTA over UNI/CTransPath (Nature 2024); top tumor-type classification (2026 benchmark) |
| Virchow | DINOv2 ViT-H, 632M params | 1.5M WSIs (Paige real-world) | CC-BY-NC, HF gated | Pan-cancer detection, rare cancers (Nature Medicine 2024) |
| Virchow2 / Virchow2G | DINOv2 ViT-H (632M) / ViT-G (1.85B) | 3.1B / 1.9B tiles, 3.1M WSIs | CC-BY-NC, HF gated | Highest overall CPTAC 7-task average (2026 clinical benchmark) |
| Hibou-B / Hibou-L | DINOv2 ViT-B (85.7M) / ViT-L | 1M+ WSIs (HistAI) | Apache-2.0 open | Patch classification + batch-effect correction |
| PathChat / PathChat+ | Vision-language LLM (UNI/CONCH-based encoder + LLM) | 1M+ visual-language instructions | Demo only, non-commercial | Diagnostic Q&A across pathology specialties (Nature 2024 + arXiv 2025) |

**What changed in 2025-2026.** Prov-GigaPath itself has not had a v2 release — the model card on `prov-gigapath/prov-gigapath` retained the original Nature 2024 weights through 2025-2026, gated behind a HuggingFace contact-information form. Two things shifted in 2025-2026: (1) the clinical benchmark frontier moved — Campanella et al. (*Nat Commun* 2025) and follow-up CPTAC-based studies put **Virchow2 first, Prov-GigaPath and UNI tied for second**, reordering the 2024 Nature paper's "SOTA" claim; (2) Virchow2G at 1.85B parameters demonstrated that **further scaling beats Prov-GigaPath** on tile-level tasks, putting pressure on the LongNet slide-level architecture to justify its compute cost. The non-commercial / Microsoft-Providence terms remained an adoption barrier for industry-adjacent groups, more restrictive than Hibou's Apache-2.0 and comparable to UNI2-h's CC-BY-NC-ND.

**AACR-relevant use cases.** The corpus shows three live use modes: (1) **H&E-to-RNA prediction in NSCLC** — poster 1457 uses Gigapath embeddings as the tile-feature backbone for predicting matched RNA-seq gene expression and pathway activity from H&E in commercial NSCLC samples, the most "biomarker-discovery" use case in the corpus; (2) **3D-ST section selection** — poster 1470 uses Prov-GigaPath embeddings + tissue-class area proportions to compute pairwise WSI similarity for cost-efficient 3D spatial transcriptomics, a methodologically novel application that exercises tile-level features at scale; (3) **Pathology TME modeling** — the [April 20 AM Decoding Cancer Ecosystem session](../../../sessions/2026-04-20-am-decoding-cancer-ecosystem-pathology-tme-heterogeneity.md) name-checks "gigapath" in the context of modeling pathology slides for tumor microenvironment heterogeneity, though without methodological detail. Conspicuously **absent**: no AACR 2026 poster exercises the **LongNet slide-level encoder**, which is Prov-GigaPath's actual architectural novelty over UNI — every corpus use is a tile-feature extraction that UNI2-h could equally serve. The "virtual cell" framing (the topic the dossier is also surfaced in) does not yet connect Prov-GigaPath to single-cell or spatial transcriptomic FMs in any 2026 abstract.
