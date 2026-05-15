# Efficient Fine-Tuning of Single-Cell FMs for Zero-Shot Perturbation Prediction — Maleki et al. (Genentech)

**One-line description** — A drug-conditional adapter for pretrained single-cell foundation models that adds <1 % trainable parameters yet enables zero-shot prediction of cellular responses to *novel* drugs and generalisation to *unseen* cell lines.

- **Authors:** Sepideh Maleki, Jan-Christian Huetter, Kangway V. Chuang, Gabriele Scalia, Tommaso Biancalani
- **Affiliation(s):** Prescient Design / Genentech (Roche)
- **Track / workshop:** ICLR 2026 LMRL workshop — paper continuation of the ICLR 2025 main-track submission
- **OpenReview:** [forum?id=tKn6gpvlUX](https://openreview.net/forum?id=tKn6gpvlUX)
- **arXiv:** [2412.13478v2](https://arxiv.org/html/2412.13478v2)
- **Code:** TBD — Prescient Design typically releases on github.com/genentech post-camera-ready
- **Status at ICLR 2026:** workshop continuation (originally accepted ICLR 2025; LMRL 2026 re-presentation with extended ablations)

## What it does

This paper attacks the single-cell perturbation-prediction problem by *re-using* large pretrained single-cell foundation models (scGPT, Geneformer, scFoundation, scMulan-class) rather than training new architectures from scratch. The contribution is a parameter-efficient drug-conditioning adapter that lets the foundation model respond to molecular perturbations it never saw at pretraining, while preserving the broad cellular knowledge encoded in the base weights.

## How it works

**Core idea.** Freeze a pretrained single-cell foundation model (scGPT / Geneformer / scFoundation / scMulan-class) and insert a small drug-conditional adapter (<1 % of base parameters) that modulates cell-token representations conditional on a query drug — preserving pretrained cell knowledge while learning the perturbation map.

**Inputs / outputs.** Inputs are (a) a control single-cell expression profile / token sequence and (b) a query drug representation (SMILES or molecular graph — TBD-verify against camera-ready); output is the predicted perturbed expression profile.

**Key innovation.** Prior perturbation predictors fall into two camps: train-from-scratch supervised models (scGen, CPA, GEARS, ChemCPA) that don't leverage the cell-knowledge encoded in foundation-model pretraining, and full-fine-tune approaches that overfit on small perturbation datasets. The adapter-based approach gives zero-shot generalisation to *unseen* drugs and *unseen* cell lines at <1 % trainable-parameter cost — the key gap closed.

**Parameters / training details.** Adapter size: <1 % of base FM parameters. Base FMs: scGPT, Geneformer, scFoundation, scMulan-class (multiple base models swept). Training data: limited perturbation datasets (Perturb-seq / drug-screen-class). The adapter projects molecular structure into the FM's cell-token modulation space.

**Canonical experiment.** Across multiple zero-shot evaluation scenarios — held-out drugs and held-out cell lines — the adapter reports state-of-the-art performance vs scGen / CPA / GEARS baselines, with the headline gains concentrated in *few-shot and zero-shot generalisation to new cell types* (TBD — exact per-task PCC / MMD from camera-ready). The Nature Methods 2025 Csendes et al. linear-baseline caveat applies: any deep-perturbation claim should be checked against the simple baselines.

## Headline benchmarks

The paper reports **state-of-the-art performance across multiple evaluation scenarios**, with the headline gains in **few-shot and zero-shot generalisation to new cell types compared to existing baselines** (scGen, CPA, GEARS-class). Exact per-task PCC and MMD numbers are in the camera-ready tables (TBD — parse from PDF).

## Where it fits in the corpus

- **AACR 2026 virtual-cells axis:** primary cross-link — perturbation prediction is the load-bearing downstream task for virtual-cells claims. Pair with any cell-state-engineering AACR dossier.
- **GBCC 2025 / EuroBioC 2025:** no direct R/Bioconductor implementation, but conceptually adjacent to perturbation-modelling sessions.
- **NeurIPS 2026 LMRL:** likely follow-on with extended molecular conditioning.
- **AACR Pancreatic 2026 / SITC 2026:** primary translational hook — drug-response prediction over pancreatic / immuno-onc cell lines.

## Notes

Prescient Design / Genentech is the same group that ships LBSTER and related single-cell tooling; the lineage here is "use the pretrained scFoundation-class model + a thin adapter" rather than "train a new bigger model" — the parameter-efficiency framing matters because it is the pattern most likely to be adopted by smaller oncology-focused groups that cannot afford fresh pretraining runs. Note the **Nature Methods 2025 caveat**: linear baselines remain competitive with deep methods on this task, so any 2026 perturbation-prediction claim should be checked against the Csendes et al. simple-baseline analysis.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** This is an **adapter layer**, not a foundation model — a <1% trainable-parameter projection that conditions a frozen scGPT / Geneformer / scFoundation / scMulan-class backbone on a drug input. It is therefore not a peer to scGPT itself; it is a peer to other parameter-efficient perturbation-conditioning methods (LoRA / IA³ / prefix-tuning variants) and to perturbation-prediction architectures that have a *drug* input alongside the *cell* input. The closest direct competitors are the train-from-scratch supervised predictors (CPA, GEARS, scGen, ChemCPA) and the explicit adapter / decoupled-encoder lines in PerturBench's reference implementations.

**Direct peers — drug-conditional / perturbation-prediction models.**

| Model | Architecture | Trainable params (relative) | Zero-shot to unseen drugs? | Released |
|---|---|---|---|---|
| **Maleki et al. adapter** (this paper) | frozen scGPT / Geneformer / scFoundation + thin drug-conditional adapter | <1% of base FM | yes | ICLR 2025 main + ICLR 2026 LMRL |
| **CPA** (Lotfollahi et al. 2023) | compositional perturbation autoencoder | trained from scratch | no — needs drug seen at train | 2023 |
| **GEARS** (Roohani et al. 2023) | GNN over gene-perturbation graph | trained from scratch | partial — needs gene-pair graph node | *Nat Biotech* 2023 |
| **scGen** (Lotfollahi et al. 2019) | VAE + arithmetic latent shift | trained from scratch | no | 2019 |
| **ChemCPA** (Hetzel et al. 2022) | CPA + chemical encoder | trained from scratch | partial | 2022 |
| **PerturBench LA + scGPT embeddings** ([arXiv 2408.10609](https://arxiv.org/abs/2408.10609)) | latent additive over scGPT cell embeddings | linear head only | benchmark reference | 2024–2025 |

The PerturBench result is the load-bearing comparator here — PerturBench's strongest reference baseline is *latent-additive on scGPT embeddings*, which is conceptually adjacent to (and a more minimal version of) the Maleki et al. adapter. Any claim of "state-of-the-art" therefore has to clear both the linear baseline (Ahlmann-Eltze & Huber) and the latent-additive baseline (PerturBench LA + scGPT).

**What changed in 2025–2026.**

- **Linear-baseline reckoning (load-bearing critique).** Ahlmann-Eltze & Huber, *Nature Methods* 2025, showed that across CRISPRi Perturb-seq datasets, scGPT, UCE, scBERT, GEARS, and scFoundation do not consistently beat a mean-of-training-perturbations baseline ([Nature Methods article](https://www.nature.com/articles/s41592-025-02772-6)). Any 2026 perturbation-prediction claim — including this adapter's — must be re-stated against this baseline.
- **scPerturBench (2025).** Independent benchmark replication: [github.com/bm2-lab/scPerturBench](https://github.com/bm2-lab/scPerturBench) confirms the linear-baseline result and gives a clean re-runnable harness.
- **Tahoe-100M (Feb 2025).** 100M cells × 1,200 drugs × 50 cancer lines is the natural training and evaluation substrate this adapter would have benefited from; the original ICLR 2025 submission predates Tahoe-100M and the LMRL 2026 continuation does not yet integrate it (TBD-confirm from camera-ready).
- **Diversity-by-design / mode collapse critique** ([arXiv 2506.22641](https://arxiv.org/html/2506.22641v1)) — single-cell perturbation predictors including scGPT, UCE, and scBERT show *mode collapse*: predictions barely vary across perturbations. Adapter approaches inherit this risk and should be re-evaluated under rank metrics, not just RMSE.
- **No retraction events**, but the field has effectively retired pre-2025 perturbation-prediction leaderboard numbers as primary evidence.

**Cross-AACR relevance.** Primary cross-link to the [AACR 2026 ED03 virtual-cells session](../../aacr-2026/topics/virtual-cells/landscape.md), specifically the perturbation-prediction-and-in-silico-screens family (6 posters including #1464 CELLama-Perturb, #4181 Turbine Virtual Lab, #1467 mechanism-aware therapy planning). The [AACR scGPT dossier](../../aacr-2026/topics/bioinfo-tools/tools/scgpt.md) and [Geneformer dossier](../../aacr-2026/topics/bioinfo-tools/tools/geneformer.md) are the direct backbone references. The AACR virtual-cells landscape audit notes that "scGPT, Geneformer, and Universal Cell Embeddings do not appear in any title in this slice — they show up only as comparators in abstract bodies" — meaning the adapter-on-frozen-FM pattern Maleki et al. demonstrate is *exactly* what most AACR perturbation posters are implicitly doing (using a pretrained FM as an encoder + a thin head) without naming the recipe. Pair with the [synthesis-ed03-vs-corpus.md](../../aacr-2026/topics/virtual-cells/synthesis-ed03-vs-corpus.md) cross-synthesis when writing the perturbation-prediction methods stack-up.
