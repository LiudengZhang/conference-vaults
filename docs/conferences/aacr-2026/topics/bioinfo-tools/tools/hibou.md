# Hibou-B / Hibou-L

**Family:** path-fm
**Modality:** H&E and non-H&E whole-slide image tiles (224×224, patch size 14); cytology slides included in pretraining
**Released:** 2024 (Nechaev, Pchelnikov, Ivanova — HistAI; arXiv June 2024)
**License:** Apache-2.0 for both Hibou-B and Hibou-L — commercial use permitted (one of the only major pathology FMs with this property)
**Code/checkpoint:** [github.com/HistAI/hibou](https://github.com/HistAI/hibou); HuggingFace [histai/hibou-b](https://huggingface.co/histai/hibou-b), [histai/hibou-L](https://huggingface.co/histai/hibou-L)
**Also surfaced in:** single-cell-spatial-omics

> Hibou is a family of two self-supervised pathology foundation models
> from HistAI (Hibou-B, 86M parameters; Hibou-L, 307M parameters) that
> uses a register-augmented DINOv2 recipe to produce general-purpose
> tile embeddings for H&E and non-H&E histology. Unlike most other
> pathology FMs at this scale, both Hibou variants ship under
> Apache-2.0 with no commercial restriction, which has made them a
> common backbone for industry-adjacent and startup pipelines that
> cannot adopt UNI / Virchow-2 / Prov-GigaPath under their respective
> non-commercial terms.

## Architecture & training

**Hibou-B** is a **ViT-B/14** with ~86M parameters; **Hibou-L** is a
**ViT-L/14** with ~307M parameters. Both use a customized DINOv2
implementation that adds **register tokens** (Darcet et al. 2024) on
top of the original Facebook Research code — register tokens stabilize
self-supervised ViTs at scale by absorbing the "high-norm artifact"
tokens that otherwise pollute attention maps. The implementation
requires `trust_remote_code=True` to load from HuggingFace.

**Pretraining corpus.** The training set comprises **1,138,905 whole
slides**: 936,441 H&E-stained slides, 202,464 non-H&E (mostly IHC and
special stains), plus 2,676 cytology slides, drawn from 306,400 unique
cases. The corpus is multi-institutional and includes veterinary
biopsies alongside human tissue — the authors frame this as one of the
most stain- and species-diverse pathology pretraining sets to date.

**Compute and recipe.** Hibou-B was trained on 512M curated patches
using 8× A100-80G GPUs with batch size 1024 for 500k iterations.
Hibou-L was trained on 1.2B curated patches using 32× A100-40G GPUs,
batch size 1024, for 1.175M iterations. Augmentations included
random rotation, horizontal/vertical flips, RandStainNA stain
normalization, and color jittering. The training objective is
standard DINOv2 (DINO + iBOT + KoLeo) with register tokens.

Hibou is a tile encoder only — no slide-level head — and is intended
to feed attention-MIL or linear probes for downstream tasks.

## Headline benchmarks

**Patch-level linear probing (Hibou paper, average top-1 across 6
public datasets: CRC-100K, PCAM, MHIST, MSI-CRC, MSI-STAD, TIL-DET).**

| Model       | Avg. top-1 |
|-------------|------------|
| Phikon      | 0.846      |
| Virchow     | 0.871      |
| RudolfV     | 0.871      |
| Hibou-B     | 0.872      |
| **Hibou-L** | **0.887**  |

Hibou-L is the top average performer in this comparison and beats
Virchow by ~1.6 absolute points, despite Virchow having roughly 2×
the parameters.

**Slide-level AUC (Hibou paper, weakly-supervised aggregation).**
Hibou-L reaches 0.946 on TCGA-BRCA subtyping, 0.969 on TCGA-NSCLC,
and 0.996 on TCGA-RCC. Notably, **Hibou-B (86M) surpasses
Prov-GigaPath (1.1B tile encoder) on 2 of the 3 slide-level
benchmarks despite having ~13× fewer parameters** — the authors cite
this as evidence that pretraining-data diversity (non-H&E + cytology)
contributes meaningfully alongside scale.

**Independent benchmarks.** Public ranking suites of pathology FMs
(e.g. the 2025 ArteraAI clinical readiness review) typically place
Hibou-L mid-tier on H&E-only tasks — below UNI2-h and Virchow-2 on
average accuracy, but the only model in that tier with a permissive
commercial license.

## Why it matters for AACR / clinical pathology

- **Apache-2.0 is the differentiator.** UNI / UNI2-h, CHIEF, and
  Virchow-2 all gate weights under CC-BY-NC or AGPL non-commercial
  terms; Prov-GigaPath weights are gated under Microsoft Research /
  Providence terms. Hibou is the only top-tier pathology FM with
  unrestricted commercial weights, so it is disproportionately
  represented in startup and pharma-adjacent pipelines that need a
  clean license trail.
- **Non-H&E coverage.** The 200K+ IHC and special-stain slides in
  pretraining make Hibou competitive on multi-stain tasks where
  UNI / Virchow-1 (H&E-only) underperform. This matters at AACR for
  posters combining H&E with companion-diagnostic IHC (HER2, PD-L1,
  Ki-67).
- **Lightweight option.** Hibou-B at 86M parameters is the most
  inference-cheap of the headline pathology FMs, useful for whole-cohort
  scale-out and on-prem deployment.

## Known limitations

- **No slide-level encoder.** Like Virchow and UNI, Hibou is a tile
  encoder; users must add their own MIL aggregator.
- **Smaller training corpus than Virchow-2 / Prov-GigaPath.** 1.1M
  slides is below Virchow-2 (3.1M) and Prov-GigaPath (171K slides but
  1.3B tiles); on pure H&E tasks the larger models still lead.
- **Closed pretraining data.** The dataset is proprietary to HistAI;
  no slide-level provenance, demographic breakdown, or fairness
  audit is published.
- **Smaller benchmark suite in the paper.** Hibou's headline
  comparisons cover 6 patch datasets and 3 TCGA slide tasks — less
  exhaustive than the 26+ tasks in Prov-GigaPath or the 30+ in UNI.

## Sources

- Nechaev D., Pchelnikov A., Ivanova E. (2024). *Hibou: A Family of
  Foundational Vision Transformers for Pathology.* [arXiv:2406.05074](https://arxiv.org/abs/2406.05074).
- HuggingFace: [histai/hibou-b](https://huggingface.co/histai/hibou-b)
  (Apache-2.0), [histai/hibou-L](https://huggingface.co/histai/hibou-L)
  (Apache-2.0).
- GitHub: [HistAI/hibou](https://github.com/HistAI/hibou) — reference
  code, training notes, and downstream examples.
- Darcet T. et al. (2024). *Vision Transformers Need Registers.* ICLR
  2024 — methodological basis for Hibou's register-augmented DINOv2.

## Use in the AACR 2026 corpus

<!-- mentions:start -->

_Mention scan pending — populated by the alias-matching pipeline used
for UNI, CHIEF, and Prov-GigaPath._

<!-- mentions:end -->
