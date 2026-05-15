# Toward Generative Virtual Cells — Lewis & Zueco (AIXC Research)

**One-line description** — A co-evolutionary framework where a virtual-cell *world model* (predicts experimental outcomes) and a *perturbation planner* (chooses which experiments to run) jointly adapt on inner and outer timescales, with validation-gated architecture search closing the loop.

- **Authors:** David Scott Lewis, Enrique Zueco
- **Affiliation(s):** AIXC Research
- **Track / workshop:** ICLR 2026 — **Gen² workshop** (Generative AI in Genomics)
- **OpenReview:** [openreview.net Gen2 ICLR 2026 PDF](https://openreview.net/pdf/58c616e58a32446ea386695fcf2a9f5caa4f5ab1.pdf)
- **Code:** TBD — not released at workshop time
- **Status at ICLR 2026:** Gen² workshop accepted paper (Apr 27, 2026)

## What it does

The paper argues that "virtual cell" research treats the world model and the experimental planner as separable, when in practice they are tightly coupled: a planner only proposes informative perturbations if the world model is calibrated, and a world model only improves on perturbations the planner actually selects. The contribution is a *co-evolutionary* training loop that updates both jointly, with a validation-gated mechanism for safely changing the world-model architecture mid-loop.

## How it works

**Core idea.** Treat the virtual-cell world model and the experimental planner as a *co-evolutionary* system updated on two timescales — fast joint adaptation in response to each experiment, and slower validation-gated changes to the world-model architecture itself.

**Inputs / outputs.** Inputs are a current world-model checkpoint, a candidate perturbation library (Perturb-seq-style genetic or small-molecule), and a held-out validation set; outputs are (a) selected next perturbations to run, (b) updated world-model weights, and (c) accepted/rejected architecture proposals.

**Key innovation.** Prior virtual-cell pipelines (scGen, CPA, GEARS, and the broader Arc / Recursion virtual-cell wave) train the world model on fixed perturbation datasets and treat experimental design as a downstream step; this paper argues the two should be jointly adapted, with the planner's exploration strategy conditioned on world-model uncertainty and recent error patterns, and architecture moves gated by a validation criterion to prevent catastrophic regression.

**Parameters / training details.** Proof-of-concept uses a synthetic Perturb-seq simulator and a small MLP / transformer world model; planner exploration is uncertainty-weighted; the outer-loop architecture-change criterion compares validation loss + capacity constraints before commit (TBD — exact thresholds in workshop PDF).

**Canonical experiment.** On the toy Perturb-seq simulator, the co-evolutionary loop is compared against a fixed-world-model baseline and a fixed-planner baseline; the paper reports that joint adaptation under validation gating outperforms both, with the architecture-change mechanism preventing the runaway drift that plagues naive joint training (TBD — exact numbers behind workshop PDF).

## Headline benchmarks

This is a **position + proof-of-concept paper**, not a benchmark paper. The Gen² accept frames the contribution as a paradigm for "safe model adaptation" coupled with experimental design. Quantitative comparisons against fixed-world-model baselines are reported in the workshop PDF on toy Perturb-seq simulators (TBD — exact numbers behind PDF parsing).

## Where it fits in the corpus

- **AACR 2026 virtual-cells axis:** direct match — pair with the AACR virtual-cell session and with any cell-state-engineering pharma demos.
- **NeurIPS 2026 LMRL:** the natural next venue for the diffusion-based + real-Perturb-seq version this paper telegraphs.
- **ICML 2026 GenBio:** workshop-level cousin contributions on perturbation planners likely.
- **AACR Pancreatic / Brain Tumors 2026:** longer-term — perturbation planning over tissue-specific cell atlases is the obvious oncology adapt.

## Notes

The paper is workshop-stage and explicitly speculative — it is included as the *concept* anchor for the Gen² "engineering cellular states" theme more than as a method release. The Lewis/Zueco framing — "world model + planner, jointly adapted under validation gating" — is the architecture pattern that AACR-vault agentic-AI dossiers should expect to start emerging from labs like Cradle, Recursion, and Insitro within 6–12 months.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** Lewis & Zueco propose a **generative virtual-cell model** plus joint planner — not a benchmark, not an adapter, and not a pre-trained encoder. It belongs to the small cohort of *systems* papers that try to close the loop from world model to next experiment, alongside Arc Institute's STATE virtual-cell model release ([Arc Institute, 2025](https://arcinstitute.org/news/virtual-cell-model-state)) and the Cradle / Recursion in-house planners. Concretely, the world-model side is in the same architectural family as scGPT-perturbation modes, GEARS, and CPA; the planner side is in the active-learning / Bayesian-optimization-over-Perturb-seq tradition.

**Direct peers — generative virtual-cell models / perturbation generators.**

| System | World model | Planner / loop | Substrate | Release |
|---|---|---|---|---|
| **Lewis & Zueco (this paper)** | small MLP / transformer + validation-gated architecture search | uncertainty-weighted, jointly adapted | toy Perturb-seq simulator | ICLR 2026 Gen² workshop |
| **STATE** (Arc Institute) | transformer pretrained on Tahoe-100M + scBaseCount | offline (model only) | 600M-cell Arc Virtual Cell Atlas | Arc Institute, 2025 |
| **scGPT generation mode** | masked-token autoregressive over scRNA-seq | none — open-loop | CELLxGENE corpus | Cui et al., *Nature Methods* 2024 |
| **GEARS** | GNN over gene-perturbation graph | open-loop | Perturb-seq screens | Roohani, Huang, Leskovec *Nature Biotech* 2023 |
| **scFoundation generation modes** | 100M-cell pretrained autoregressive | open-loop | scFoundation pretraining mix | Hao et al. 2024 |
| **scBaseCamp / scBaseCount** | n/a — *atlas* used as training substrate | AI agent-curated metadata | 500M cells, 21 organisms | Arc Institute scBaseCount, 2025 |

The differentiator vs. STATE (the closest 2025–2026 production-scale analogue) is the *joint adaptation under validation gating* — STATE is trained offline on a frozen Tahoe-100M snapshot, while Lewis & Zueco argue the planner and world model must be updated together as new experiments come in. This is the paper's load-bearing methodological claim.

**What changed in 2025–2026.**

- **STATE release (Arc Institute, 2025).** First production-grade virtual-cell model trained on the Arc Virtual Cell Atlas; Lewis & Zueco's contribution is now legible as "the loop closure STATE doesn't (yet) implement" ([Arc Institute STATE announcement](https://arcinstitute.org/news/virtual-cell-model-state)).
- **Tahoe-100M (Feb 2025).** 100M cells × 1,200 drugs × 50 cancer lines — the substrate any future co-evolutionary loop would target ([Vevo Tahoe-100M release](https://www.prnewswire.com/news-releases/vevo-therapeutics-open-sources-tahoe-100m-the-worlds-largest-single-cell-dataset-as-the-inaugural-contribution-to-arc-institutes-new-virtual-cell-atlas-302384677.html)).
- **Virtual Cell Atlas launch (Feb 2025).** Combined ≥300M cells (now ≥600M) across Tahoe-100M + scBaseCount, the natural deployment substrate for any planner / world-model loop.
- **Linear-baseline reckoning (Ahlmann-Eltze & Huber, *Nature Methods* 2025).** Casts a long shadow on any 2026 generative-virtual-cell paper that does not include the mean-of-training-perturbations baseline as a control ([Nature Methods article](https://www.nature.com/articles/s41592-025-02772-6)).
- **No retraction events,** but the field-wide critique narrows what "outperforms baseline" can mean — Lewis & Zueco's toy-simulator result must be read against this caveat.

**Cross-AACR relevance.** Direct match to the [AACR 2026 ED03 virtual-cells session](../../aacr-2026/topics/virtual-cells/landscape.md), particularly the perturbation-prediction-and-in-silico-screens family (6 posters including #1464 CELLama-Perturb and #4181 Turbine Virtual Lab) and the digital-twins family (3 posters). The [AACR scGPT dossier](../../aacr-2026/topics/bioinfo-tools/tools/scgpt.md) and [Geneformer dossier](../../aacr-2026/topics/bioinfo-tools/tools/geneformer.md) are the comparator world-model entries. The "planner" framing maps directly onto AACR's [AT02 agentic-AI session](../../aacr-2026/sessions/2026-04-21-at02-agentic-ai-cancer-researcher.md), which discussed AI-as-experimentalist autonomy — Lewis & Zueco's validation-gated architecture move is the methods-side answer to AT02's open question about how agents should propose their own next experiments without runaway drift.
