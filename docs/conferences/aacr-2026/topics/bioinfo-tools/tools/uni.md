# UNI / UNI2

**Family:** path-fm
**Modality:** H&E (and IHC for UNI2) whole-slide image patches (224×224, 20×)
**Released:** UNI: 2024 (Nature Medicine); UNI2-h: 2025 (Mahmood Lab release)
**License:** CC-BY-NC-ND 4.0, non-commercial academic use; commercial use requires Mass General Brigham approval
**Code/checkpoint:** [github.com/mahmoodlab/UNI](https://github.com/mahmoodlab/UNI); checkpoints on HuggingFace ([MahmoodLab/uni](https://huggingface.co/MahmoodLab/uni), [MahmoodLab/UNI2-h](https://huggingface.co/MahmoodLab/UNI2-h))
**Also surfaced in:** clinical-trials, single-cell-spatial-omics, virtual-cells

> UNI is a self-supervised pathology foundation model from the Mahmood
> Lab that produces general-purpose tile embeddings for H&E whole-slide
> images, intended as a drop-in feature extractor for downstream tasks
> like tumor detection, subtyping, biomarker prediction, and survival
> analysis. UNI2-h is a larger 2025 successor trained on a substantially
> expanded corpus that adds IHC alongside H&E. The line is one of the
> most widely benchmarked pathology backbones, frequently used as the
> tile encoder feeding ABMIL or other slide-level aggregators.

## Architecture & training

UNI uses a ViT-L/16 backbone pretrained with DINOv2 self-supervision on
roughly 100 million tiles from ~100,000 diagnostic H&E slides spanning
20 major tissue types from Mass General Brigham. UNI2-h scales the
backbone to ViT-H/14 with register tokens and is trained on more than
200 million H&E and IHC tiles sampled from over 350,000 whole-slide
images. Both models are tile encoders (no slide-level head) returning
1024-dimensional embeddings (UNI) or 1536-dimensional embeddings (UNI2-h),
designed to be paired with attention MIL or similar aggregators downstream. Reported claims include
strong few-shot transfer and consistent gains over CTransPath and
generic ImageNet ViTs across more than 30 clinical histopathology
benchmarks.

## Use in the AACR 2026 corpus

<!-- mentions:start -->

**Posters mentioning UNI / UNI2 (n=9):**

- **1441** — *Whole-slide image and clinical feature integration for superior prostate cancer risk stratification*
  …notated and tiled at 224×224 pixels using QuPath (Bankhead Sci Rep 2017). Tile embeddings were extracted with UNI2-h (Mahmood Nat Med 2025). An end-to-end machine learning pipeline was developed to aggregate tile embeddings…
- **1448** — *Deep learning integration of molecular and histopathological data for prognostic stratification in non small cell lung cancer*
  …timus1 features highest. Co-mutation models produced AUROC scores of 0.69-0.77 with EGFR-TP53 prediction from Uni2 features the best. The KRAS-TP53 co-mutation model (AUROC 0.69, Uni2) showed significant separation in overal…
- **2758** — *PAX3/7::FOXO1 fusion detection and transcriptomic prediction from whole-slide images of rhabdomyosarcoma using attention-based deep learning frameworks: A multi-institutional study*
  …MCI) = 252] were used to train and evaluate an Attention-Based Multiple Instance Learning (ABMIL) model using UNI2-h foundation features for fusion classification. For gene expression prediction, 135 RMS WSIs paired with bul…
- **4163** — *A general-purpose AI foundation model for spatial proteomics*
  …, renal cell carcinoma, and skin cancer. Across these tasks, KRONOS consistently outperforms other pathology (UNI) and spatial proteomics foundation model (CA-MAE) baselines, underscoring the importance of a domain-specific…
- **5470** — *Low-magnification deep learning model for rapid HER2 status prediction from H&E whole-slide images*
  …d an AUC of 0.7280.029 and an F1-score of 0.6530.054. In comparison, the state-of-the-art deep learning model UNI2 achieved an AUC of 0.7150.010 and F1-score of 0.6270.036. Despite comparable accuracy, our model demonstrated…
- **5505** — *A unified framework for cross-platform spatial omics analysis and deep spatial profiling*
  …HD single-cell transformation using registered H&#38;E), multimodal registration, and a foundation-model hub (UNI, KRONOS, LOKI) for panel expansion, imputation, and cross-modality retrieval. With harmonized data and z-axis…
- **6446** — *Molecular profiling to predict the first site of recurrence in pancreatic cancer patients receiving neoadjuvant therapy followed by surgery*
  …nt neoadjuvant therapy followed by surgery at Cedars Sinai Medical Center between May 2013 and November 2024. Uni- and multivariable binary logistic regression including clinicopathologic variables and NGS-based molecular f…
- **71** — *Bridging histopathology and spatial transcriptomics for comprehensive tumor microenvironment profiling*
  …thods: We introduce a multi-scale multimodal learning strategy that aligns two large-scale foundation models: UNI (trained on 100,000 pathology slides) [1] and Visiumformer (trained on 3.94 million ST profiles) [2]. Rather…
- **LB159** — *A practical guideline for benchmarking unimodal and multimodal foundation models on spatial transcriptomics data in oncology*
  …in this work provide a crucial toolset to researchers seeking to accurately assess the evolving landscape of uni- and multimodal foundation models for spatial omics.

**Sessions mentioning UNI / UNI2 (n=1):**

- [2026-04-18-pm-3d-tissue-imaging-and-cancer](../../../sessions/2026-04-18-pm-3d-tissue-imaging-and-cancer.md)
  …eemed to be sitting in some landscape. That actually was similar to what Ashley described. It was actually an UNI model embedding. And what's interesting is these things are just visually totally different. These machine le…

<!-- mentions:end -->

## What's missing / where evidence is weak

- **Two of the nine "poster" hits are alias collisions, not the model.** Poster 6446 ("Uni- and multivariable binary logistic regression") and LB159 ("uni- and multimodal foundation models") match on the prefix "uni" but refer to univariate analysis and unimodal models, not UNI / UNI2-h. The true-positive poster count is closer to 7.
- **No outcome / external-validation data in the corpus.** Posters use UNI(2) as a frozen feature extractor feeding ABMIL or similar aggregators, but none report prospective clinical validation, calibration, or fairness analyses.
- **Almost no head-to-head benchmarking against other pathology FMs.** Poster 4163 (KRONOS) and 5470 (low-mag HER2) are the only entries that compare UNI(2) directly to an alternative; there is no poster systematically evaluating UNI vs. Prov-GigaPath vs. CONCH on identical tasks.
- **The CC-BY-NC-ND license is invisible in the corpus** — no poster discusses commercial-use constraints despite many appearing to come from translational / industry-adjacent groups.

## Takeaway

UNI / UNI2-h is the most-evidenced pathology foundation model in AACR 2026: nine poster mentions (≈7 true-positive) plus one session, almost all using it as a drop-in tile encoder feeding attention-MIL pipelines for tumor subtyping, biomarker prediction, mutation prediction, or fusion calling. The corpus pattern is striking — UNI shows up as the default backbone the way ResNet-50 once did, beating CTransPath but matched or modestly beaten by domain-specific successors (KRONOS for spatial proteomics, a custom low-magnification model for HER2). What is conspicuously missing is any prospective clinical evaluation; UNI is being used as feature plumbing, not yet as a deployed decision-support component.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** UNI / UNI2-h is the **encoder-only tile-level FM** anchor of the pathology FM landscape — a vanilla DINOv2-pretrained ViT backbone (ViT-L/16, 307M params for UNI; ViT-H/14, 681M params for UNI2-h) returning a flat 1024- or 1536-dim tile embedding with no built-in slide aggregator. This makes it the most "plug-in" of the pathology FMs: where Prov-GigaPath ships with a LongNet slide head and CHIEF ships with an anatomic-site-conditioned attention-MIL head, UNI requires the user to bring their own aggregator (typically ABMIL). UNI2-h is the **biggest pure tile encoder in active 2026 use**, sized between Virchow (632M) and Virchow2G (1.85B), and the only major pathology FM trained on a mix of H&E *and* IHC tiles.

**Direct peers.**

| Model | Architecture | Pretraining corpus | Public weights | Headline benchmark |
| --- | --- | --- | --- | --- |
| UNI2-h | DINOv2 ViT-H/14, 681M params, SwiGLU FFN, register tokens | 200M+ tiles, 350K+ H&E+IHC WSIs (MGB) | CC-BY-NC-ND 4.0, HF gated (institutional email required) | Second-generation PFM tier, top-3 across CPTAC tasks (2026 clinical benchmark) |
| Virchow / Virchow2 | DINOv2 ViT-H (632M) / ViT-G (1.85B for V2G) | 1.5M WSIs / 3.1M WSIs (Paige real-world) | CC-BY-NC, HF gated | Virchow2 ranks first overall on CPTAC 7-task average (2026 benchmark) |
| Hibou-B / Hibou-L | DINOv2 ViT-B (85.7M) / ViT-L | 1M+ WSIs (HistAI) | Apache-2.0 open | Strong on patch classification, batch-effect correction |
| PathChat / PathChat+ | Vision-language LLM stacking UNI/CONCH encoders + LLM | 1M+ visual-language instructions | Demo only, non-commercial | Pathology Q&A across specialties (Nature 2024 + arXiv 2025) |
| Prov-GigaPath | DINOv2 ViT tile + LongNet slide encoder | 1.3B tiles, 171K WSIs (Providence) | Apache-2.0 code, HF gated weights | Top mutation prediction and tumor-type classification (Nature 2024) |

**What changed in 2025-2026.** UNI2-h released **January 14, 2025** as the Mahmood Lab's second-generation tile FM, scaling from ViT-L to ViT-H/14, doubling tile count to 200M+, and crucially adding IHC alongside H&E for the first time. Companion releases that hit in 2025 included **CONCHv1.5 + TITAN** (multimodal whole-slide FM, *Nat Med* 2025), **PathChat+** (multi-image vision-language pathology copilot, arXiv 2025), and **SlideSeek** (reasoning-enabled multi-agent system, arXiv 2025). License remained CC-BY-NC-ND 4.0 across the line — non-commercial academic only, with Mass General Brigham approval required for commercial use, and HF access gated behind institutional-email verification (no gmail/hotmail/qq). The 2025 *Nat Commun* clinical benchmark (Campanella et al.) confirmed **consistent generational improvements** — UNI2-h outperforms UNI, Virchow2 outperforms Virchow, H-optimus-1 outperforms H-optimus-0 — and put UNI2-h in the top tier alongside Virchow2 and Prov-GigaPath on CPTAC tasks.

**AACR-relevant use cases.** Three live AACR 2026 use modes: (1) **Risk stratification from frozen tile features** — poster 1441 uses UNI2-h embeddings + ABMIL for prostate cancer risk stratification, integrating with clinical features; poster 1448 uses Uni2 features for NSCLC prognostic stratification with co-mutation models (EGFR-TP53 AUROC 0.69-0.77); (2) **Fusion / mutation / biomarker prediction** — poster 2758 uses UNI2-h + ABMIL for PAX3/7::FOXO1 fusion detection in rhabdomyosarcoma across a multi-institutional cohort, the cleanest "rare-disease translational" application in the corpus; poster 5470 reports a low-magnification model that *matches* UNI2 on HER2 prediction (AUC 0.728 vs 0.715); (3) **Multimodal foundation-model hubs** — poster 5505 combines UNI, KRONOS, and LOKI in a cross-platform spatial-omics framework for panel expansion and imputation; poster 71 aligns UNI with Visiumformer to bridge histopathology and spatial transcriptomics. The [April 18 PM 3D Tissue Imaging session](../../../sessions/2026-04-18-pm-3d-tissue-imaging-and-cancer.md) is the only session that name-checks the UNI embedding directly. Across all nine poster hits, UNI2-h is used as **frozen feature plumbing for ABMIL pipelines** — never fine-tuned, never prospectively validated, and never explicitly compared head-to-head with Prov-GigaPath or Virchow2 on a matched task within a single AACR 2026 abstract.
