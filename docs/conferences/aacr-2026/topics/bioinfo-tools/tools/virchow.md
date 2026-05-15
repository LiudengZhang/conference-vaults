# Virchow / Virchow-2

**Family:** path-fm
**Modality:** H&E whole-slide image tiles (224×224 at 0.5 µm/px for Virchow; mixed magnifications 5×/10×/20×/40× plus IHC for Virchow-2)
**Released:** Virchow: Nature Medicine, October 2024 (Vorontsov et al.); Virchow-2: arXiv August 2024 (Zimmermann et al., updated 2025)
**License:** Virchow: Apache-2.0 weights (academic, non-clinical use). Virchow-2: CC-BY-NC-ND-4.0, non-commercial academic research only; institutional email required
**Code/checkpoint:** [huggingface.co/paige-ai/Virchow](https://huggingface.co/paige-ai/Virchow); [huggingface.co/paige-ai/Virchow2](https://huggingface.co/paige-ai/Virchow2)
**Also surfaced in:** single-cell-spatial-omics, virtual-cells

> Virchow is a tile-level pathology foundation model from Paige and
> Memorial Sloan Kettering Cancer Center, designed as a general-purpose
> H&E feature extractor that supports cancer detection, subtyping,
> biomarker prediction, and rare-cancer triage with a single frozen
> backbone. Virchow-2 keeps the same 632M-parameter ViT-H/14 backbone
> but doubles the training corpus to 3.1 million slides, adds IHC and
> mixed magnifications, and retrains with a pathology-tuned DINOv2
> recipe. The line is one of the three pathology FMs (with UNI and
> Prov-GigaPath) most often used as a drop-in patch encoder in 2025-2026
> translational pathology pipelines.

## Architecture & training

Both Virchow and Virchow-2 use a **ViT-H/14** backbone: 632M parameters,
32 layers, 1280-dim embeddings, 16 attention heads, SwiGLU activation,
LayerScale enabled, 224×224 input. The final tile embedding is a
2560-dim vector formed by concatenating the class token (1280-d) with
the mean-pooled patch tokens (1280-d). Virchow-2 adds 4 register
tokens.

**Virchow (v1)** was pretrained with standard DINOv2 self-supervision
on 1.5 million H&E whole-slide images from Memorial Sloan Kettering
spanning ~100,000 patients, sampled at 0.5 µm/px (20× magnification).
The model is released under Apache-2.0 (with a non-clinical-use
disclaimer).

**Virchow-2** scales the training corpus to **3.1 million WSIs covering
~225,000 patients and nearly 200 tissue types**, drawn from MSK plus
external consult cases — ~15% of slides and ~57% of patients come from
non-MSK institutions submitting challenging cases worldwide. The
recipe is a **pathology-modified DINOv2**: the KoLeo regularizer is
replaced with a kernel density estimator (more stable on
near-duplicate histology tiles), the standard crop-and-resize
augmentation is replaced with an "extended context translation" that
preserves magnification semantics, and tiles are sampled at 5×, 10×,
20×, and 40× to make the encoder magnification-aware. Virchow-2 ships
as three variants: Virchow-2 (632M), Virchow-2G (1.9B), and Virchow-2G
Mini (22M, distilled). The Virchow-2 weights carry the more
restrictive CC-BY-NC-ND-4.0 license.

Neither model includes a slide-level head — both are tile encoders
intended to be paired with attention MIL (abMIL/ABMIL), TransMIL, or a
linear probe downstream.

## Headline benchmarks

**Pan-cancer detection (Virchow Nature Medicine 2024).** A
weakly-supervised aggregator on top of Virchow tile features reached
**0.949 specimen-level AUC across 17 cancer types** and 0.937 AUC on 7
rare cancer subtypes. On the same evaluation, Virchow embeddings beat
UNI (0.940), Phikon (0.932), and CTransPath (0.907) on overall
pan-cancer AUC.

**Tile-level tasks (Virchow-2, arXiv 2024).** Across 12 tile-level
benchmarks, Virchow-2 lifts the weighted average F1 from **0.944
(Virchow) to 0.966**, with the pathology-tuned DINOv2 recipe
contributing most of the gain. Virchow-2G (1.9B) is reported as
state-of-the-art across the same suite.

**Independent comparisons.** Public clinical benchmarks of pathology
FMs (e.g. the 2025 ArteraAI evaluation and the PMC clinical benchmark
PMC12003829) consistently place Virchow / Virchow-2 in the top tier
alongside UNI2-h and Prov-GigaPath, with model ordering shifting by
task — Virchow-2 tends to win on rare-cancer detection and IHC-aware
tasks where mixed magnifications matter.

## Why it matters for AACR / clinical pathology

- **Rare-cancer triage.** Virchow is the first pathology FM whose
  flagship paper foregrounds rare-cancer detection (7 rare tumors at
  0.937 AUC), directly relevant to AACR streams on under-served
  cancers and pediatric oncology.
- **Magnification-aware features.** Virchow-2's mixed-magnification
  training is the closest current answer to the spatial-pathology
  question of how to share features across 10×/20×/40× tiles without
  retraining — useful for pipelines that combine tile-level cell
  morphology with slide-level architecture.
- **Industrial provenance.** Both Virchow checkpoints come from Paige,
  whose Paige Prostate Detect is FDA-cleared, so the backbone has a
  clearer regulatory lineage than purely academic FMs.

## Known limitations

- **License asymmetry.** Virchow-2 (the better model) is CC-BY-NC-ND-4.0
  and gated, so commercial / translational groups face a real
  adoption barrier and often default to Virchow-1 or UNI2-h.
- **No slide-level encoder.** Unlike Prov-GigaPath, neither Virchow
  release includes a slide-level transformer — downstream MIL
  aggregation is the user's problem.
- **Training data concentration.** Despite Virchow-2's global consult
  cases, the majority of slides still originate from a single
  institution (MSK), and the paper does not release fairness analyses
  by site or demographic.
- **No vision-language head.** Virchow is vision-only; it does not
  support text queries or report generation natively (cf. PathChat,
  CONCH).

## Sources

- Vorontsov E. et al. (2024). *A foundation model for clinical-grade
  computational pathology and rare cancers detection.* Nature Medicine
  30:2924-2935. [doi:10.1038/s41591-024-03141-0](https://doi.org/10.1038/s41591-024-03141-0)
- Vorontsov E. et al. (2023). *Virchow: A Million-Slide Digital
  Pathology Foundation Model.* [arXiv:2309.07778](https://arxiv.org/abs/2309.07778) (preprint).
- Zimmermann E. et al. (2024). *Virchow2: Scaling Self-Supervised Mixed
  Magnification Models in Pathology.* [arXiv:2408.00738](https://arxiv.org/abs/2408.00738).
- HuggingFace: [paige-ai/Virchow](https://huggingface.co/paige-ai/Virchow)
  (Apache-2.0), [paige-ai/Virchow2](https://huggingface.co/paige-ai/Virchow2)
  (CC-BY-NC-ND-4.0).
- Paige.ai. *The Virchow Foundation Model, Explained.*
  [paige.ai/blog](https://www.paige.ai/blog/the-virchow-foundation-model-explained-a-qa-with-an-ai-scientist).

## Use in the AACR 2026 corpus

<!-- mentions:start -->

_Mention scan pending — populated by the alias-matching pipeline used
for UNI, CHIEF, and Prov-GigaPath._

<!-- mentions:end -->
