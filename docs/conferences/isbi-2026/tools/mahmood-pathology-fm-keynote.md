# Pathology Foundation Models — Faisal Mahmood (Harvard / Mahmood Lab)

**ISBI 2026 plenary keynote on pathology foundation models, slide-level aggregation, and multimodal pathology agents — the methods-side bridge from the AACR pathology-FM dossier line (CHIEF / UNI / Prov-GigaPath) into the IEEE imaging community.**

- **Speaker(s) / Authors:** Faisal Mahmood
- **Affiliation(s):** Harvard Medical School / Brigham & Women's Hospital / Broad Institute (Mahmood Lab)
- **Anchor type:** keynote
- **Track / day:** ISBI 2026 main plenary (Thu Apr 9 or Fri Apr 10, ExCeL London)
- **IEEE Xplore:** TBD (keynote — no IEEE Xplore paper; any new artifact tracked via Mahmood Lab GitHub / HuggingFace through Q2 2026)
- **Status:** post-meeting

## What it does

Mahmood's keynote framed the current pathology-FM landscape — CHIEF (slide-level diagnostic + prognostic FM), UNI / UNI2 (tile-level encoder pretrained on >100M H&E patches), and the broader CONCH / multimodal pathology agent line — and outlined where the field is going: larger tile encoders, multimodal (H&E + IHC + report + molecular) pretraining, agentic workflow composition, and clinical deployment. The talk is the direct methods-side complement to the AACR 2026 pathology-FM clinical-deployment readouts.

## How it works / methodology

Pathology FMs share a three-tier stack: (1) self-supervised tile encoders (DINOv2-class) trained on tens-to-hundreds of millions of H&E patches; (2) slide-level aggregation (attention-based MIL, transformers over tile embeddings, set-transformer variants); (3) task heads for subtyping, biomarker prediction, survival, and weakly-supervised molecular regression. Mahmood-line models (UNI, CHIEF) emphasize generalization across cancer types via task-agnostic pretraining plus zero-shot / few-shot evaluation.

## Headline benchmarks

TBD — keynote-level synthesis; specific benchmark deltas not in program-notes. CHIEF and UNI baselines remain the published anchors (CHIEF: 19 cancer types, 60K+ slides; UNI: >100M tiles).

## How it works

**Core idea.** A pathology foundation model is a large image (and increasingly multimodal) encoder pretrained self-supervised on H&E whole-slide tiles at internet scale (tens-to-hundreds of millions of patches), producing a generic slide / tile embedding that transfers to dozens of downstream pathology tasks with minimal task-specific data.

**Inputs / outputs.** Inputs: H&E whole-slide images (typically 20x or 40x magnification); for multimodal extensions, paired IHC, molecular labels, or pathology reports. Outputs: tile-level embeddings (UNI, UNI2), slide-level embeddings or task predictions (CHIEF), or report / answer generation (multimodal pathology agents in the CONCH / PathChat line).

**Key innovation.** Three-tier stack with task-agnostic pretraining: (1) DINOv2-class self-supervised tile encoder pretrained on >100M unlabeled patches, (2) attention-MIL or transformer-over-tiles aggregator that lifts tile embeddings to slide-level representations, (3) light task heads or zero-shot evaluation. Generalization-by-scale rather than task-by-task model design is the field-shaping move; CHIEF added the agentic / multitask synthesis layer.

**Parameters.** UNI: ViT-L/16, ~300M parameters, ~100M H&E tiles. UNI2 / CHIEF v2: scale TBD (likely ViT-H/G, hundreds-of-millions to low-billions parameters, internet-scale tile counts). Slide-aggregation models: transformer over up to ~10K tiles per slide.

**Canonical example.** Zero-shot or few-shot lung-cancer subtyping from H&E: tile a WSI, encode all tiles with UNI, aggregate with attention-MIL, predict LUAD vs LUSC. CHIEF extends this to a single model covering 19 cancer types and 60K+ slides with prognostic outputs alongside diagnostic ones — the headline cross-cancer-type generalist pathology FM result that anchored the keynote.

## Where it fits in the corpus

- **AACR 2026:** direct line to [CHIEF](../../aacr-2026/topics/bioinfo-tools/tools/chief.md), [UNI](../../aacr-2026/topics/bioinfo-tools/tools/uni.md), and [Prov-GigaPath](../../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) dossiers
- **MICCAI 2026:** anticipated COMPAY workshop cousin paper (Sep 27–Oct 1) — likely UNI2 or CHIEF v2 methods write-up
- **RSNA 2026 / CVPR 2026:** RSNA radiology-pathology fusion track; CVPR FMV / MMFM-BIOMED workshops likely surface the same author pool

## Notes

Keynote itself is not a tool page — any new model announced gets either (a) in-place update to the AACR dossier (incremental work) or (b) a new ISBI tool page if fundamentally new. Watch Mahmood Lab GitHub / HuggingFace through May–July 2026 for the artifact drop. Likely TBME Special Section pipeline if a methods companion paper exists.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** Mahmood's keynote is a **survey / synthesis** of the pathology foundation-model field, not a model release. The artifacts it discusses (UNI, UNI2, CHIEF, CONCH, KRONOS for spatial proteomics, the multimodal PathChat / CONCH agent line) are the underlying objects; the keynote's value is the landscape framing, the cross-model comparison, and the forward-look on multimodal pretraining + agentic deployment. Direct peers are therefore *other pathology FM landscape surveys* and *individual pathology FMs* — the keynote sits methodologically next to bioRxiv landscape reviews like ["Understanding Foundation Models in Digital Pathology"](https://www.biorxiv.org/content/10.1101/2025.09.12.675923v1.full.pdf) (Sep 2025) and the EUCAIM / community clinical-benchmark efforts ([clinical benchmark of public self-supervised pathology FMs, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003829/)).

**Direct peers — pathology foundation models the keynote anchored.**

| Model | Lab / Vendor | Backbone | Parameters | Pretraining tiles / slides | Released |
|---|---|---|---|---|---|
| **UNI** | Mahmood Lab (Harvard / BWH) | ViT-L/16 (DINOv2) | ~300M | ~100M H&E tiles | *Nature Medicine* 2024 |
| **UNI2** | Mahmood Lab | ViT-H (DINOv2) | larger than UNI | 200M+ H&E + IHC tiles / 350K+ WSIs | **Jan 14 2025 release** ([UNI GitHub](https://github.com/mahmoodlab/UNI)) |
| **Virchow / Virchow2** | Paige.ai | ViT-H | 632M (Virchow2) | 1.7B tiles / 3.1M WSIs / 225K patients / 45 countries | [Virchow2 arXiv 2408.00738](https://arxiv.org/pdf/2408.00738), 2024 |
| **CHIEF** | Mahmood Lab | tile encoder + slide-level aggregator | TBD | 19 cancer types, 60K+ slides | *Nature* 2024 |
| **Prov-GigaPath** | Microsoft Research / Providence | ViT + LongNet slide-aggregator | ~1B | 1.3B tiles / 171K WSIs | *Nature* 2024 |
| **Hibou** | HistAI | ViT (DINOv2) | tile encoder | ~1B tiles | 2024 |

UNI2 (Jan 2025) and Virchow2 (2024) are the most recent generation; UNI2 reports a perfect Balanced Accuracy (1.0) on BACH breast-cancer histology and 79.7 on pan-cancer tissue classification, while Virchow2 leads on CRC polyp classification (52.1) ([UNI2 release notes](https://github.com/mahmoodlab/UNI)). The keynote framed these as complementary rather than ranked — different backbones suit different downstream task families.

**What changed in 2025–2026.**

- **UNI2 release (Jan 14 2025)** — 200M+ H&E and IHC tiles across 350K+ WSIs; 25K+ pre-extracted WSI embeddings released for TCGA, CPTAC, PANDA ([Mahmood Lab GitHub](https://github.com/mahmoodlab/UNI)).
- **Virchow2 (Paige.ai, 2024–2025)** — scaling to 1.7B tiles and 3.1M WSIs from 225K patients; state-of-the-art on 12 tile-level tasks ([Virchow2 paper](https://arxiv.org/pdf/2408.00738)).
- **CHIEF v2 / agentic-CHIEF (signposted in keynote).** Methods companion paper expected through MICCAI 2026 / TBME pipeline — not yet released as of May 2026.
- **Clinical-benchmark traction.** [A clinical benchmark of public self-supervised pathology FMs](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003829/) (2025) is the first published head-to-head clinical comparison; complements but does not replace lab-internal benchmarks.
- **No retraction events** affecting any of the named pathology FMs as of May 12 2026.

**Cross-AACR relevance.** Mahmood's keynote anchors a dense AACR 2026 cross-link cluster. The [AACR bioinfo-tools landscape](../../aacr-2026/topics/bioinfo-tools/landscape.md) audit found **18 AACR 2026 posters citing pathology FMs by name** — UNI / UNI2 (6 posters: #1441, #5470, #2758, #71, #4163, #5505), Lunit-SCOPE (2: #80, #1465), Virchow2 (1: #1442), Prov-GigaPath (1: #1470), plus CONCH, TITAN, H-optimus, CTransPath, Hibou, MUSK, DINOv2, KRONOS, LOKI, MADELEINE, CA-MAE as named encoders. Direct dossier links: [AACR CHIEF](../../aacr-2026/topics/bioinfo-tools/tools/chief.md), [AACR UNI](../../aacr-2026/topics/bioinfo-tools/tools/uni.md), [AACR Prov-GigaPath](../../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md). The relevant AACR 2026 sessions are [Foundation Models & Multimodal AI in Cancer Research (Apr 17 PM)](../../aacr-2026/sessions/2026-04-17-pm-foundation-models-multimodal-ai-cancer-research.md), [Decoding the Cancer Ecosystem: Pathology + TME Heterogeneity (Apr 20 AM)](../../aacr-2026/sessions/2026-04-20-am-decoding-cancer-ecosystem-pathology-tme-heterogeneity.md), [AI + Spatial Transcriptomics + Pathology (Apr 20 PM)](../../aacr-2026/sessions/2026-04-20-pm-ai-spatial-transcriptomics-pathology.md), and [3D Tissue Imaging and Cancer (Apr 18 PM)](../../aacr-2026/sessions/2026-04-18-pm-3d-tissue-imaging-and-cancer.md). The existing AACR cross-synthesis [synthesis-fm-pathology-traction.md](../../aacr-2026/topics/bioinfo-tools/synthesis-fm-pathology-traction.md) is the page where Mahmood's ISBI keynote should be cited as the ground-truth landscape framing.
