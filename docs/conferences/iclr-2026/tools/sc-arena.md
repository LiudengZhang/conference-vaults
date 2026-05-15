# SC-Arena — Jiahao Zhao et al.

**One-line description** — A natural-language benchmark for single-cell reasoning that formalises a "virtual cell" abstraction and evaluates LLMs / single-cell foundation models with knowledge-augmented metrics across five biological tasks.

- **Authors:** Jiahao Zhao, Feng Jiang, Shaowei Qin, Zhonghui Zhang, Junhao Liu, Guibing Guo, Hamid Alinejad-Rokny, Min Yang
- **Affiliation(s):** Shenzhen Institute of Advanced Technology (Chinese Academy of Sciences); Northeastern University (Shenyang); UNSW Sydney — affiliations inferred from co-author roster, TBD-verify
- **Track / workshop:** ICLR 2026 main track — Poster
- **OpenReview:** [forum?id=5RcoUe1tA1](https://openreview.net/forum?id=5RcoUe1tA1)
- **arXiv:** [2602.23199](https://arxiv.org/abs/2602.23199)
- **Code:** TBD — not surfaced in OpenReview camera-ready
- **Status at ICLR 2026:** Poster, Sat Apr 25 (Pavilion 3); license CC-BY 4.0

## What it does

SC-Arena reframes the evaluation problem for single-cell foundation models (scGPT, Geneformer, UCE, CellFM and their LLM-conditioned cousins) as a *natural-language reasoning* benchmark. Instead of measuring embedding quality with proxy metrics, it formalises a "virtual cell" abstraction unifying intrinsic cell attributes and gene-level interactions, then probes models with five free-form tasks: cell-type annotation, captioning, generation, perturbation prediction, and scientific QA.

## How it works

**Core idea.** SC-Arena reformulates single-cell foundation-model evaluation as natural-language reasoning over a "virtual cell" abstraction that unifies intrinsic cell attributes with gene-level interaction context, replacing brittle string-match metrics with a knowledge-augmented scoring pipeline.

**Inputs / outputs.** Inputs are single-cell expression profiles (or their tokenised foundation-model embeddings) plus a free-form natural-language probe; outputs are model responses for five tasks — cell-type annotation, captioning, generation, perturbation prediction, and scientific QA — each scored against ontology- and literature-grounded ground truth.

**Key innovation.** Prior benchmarks (Geneformer / scGPT / UCE / CellFM evaluations) lean on exact-match cell-type F1 or embedding probing; SC-Arena instead uses evidence-grounded knowledge-augmented metrics that consult Cell Ontology, GO, curated marker databases, and the scientific literature to score biological faithfulness with interpretable rationales.

**Parameters / training details.** SC-Arena is an evaluation benchmark (no new model training). Evaluated systems span general-purpose LLMs (GPT-4o-class) and domain-specialised single-cell LMs; scoring weights across the five tasks and the per-task knowledge-base lookups are released as configurable benchmark assets (TBD — exact weighting from camera-ready).

**Canonical experiment.** The paper benchmarks scGPT, Geneformer, UCE, CellFM, and LLM-conditioned cousins side-by-side across the five tasks. Knowledge-augmented metrics consistently re-rank models versus string-matching baselines, and the authors report "uneven performance on biologically complex tasks, particularly those demanding mechanistic or causal understanding" — the load-bearing methodological finding.

## Headline benchmarks

The paper reports "uneven performance on biologically complex tasks, particularly those demanding mechanistic or causal understanding." Specific per-model numbers are reported in the camera-ready tables (TBD — full PDF behind login). Knowledge-augmented metrics consistently rank models differently from string-matching baselines, supporting the methodological argument.

## Where it fits in the corpus

- **AACR 2026:** virtual-cells axis anchor — pair with the AACR virtual-cell methodology session and any TissueAgent / pan-tumor cell-atlas tool entries.
- **NeurIPS 2026:** likely cousin contribution at the NeurIPS LMRL re-run (Dec 2026) — same evaluation framework, expanded benchmark suite expected.
- **ICML 2026:** GenBio / FM4LS workshop submissions in July may target this benchmark directly.
- **ISMB 2026:** scaffold — cell-type-annotation benchmarks overlap.

## Notes

This is the LMRL community's explicit answer to "how do you actually score a virtual cell?" — the 2024–2025 scGPT/Geneformer wave was evaluated mostly on cell-typing F1; SC-Arena's task suite (especially scientific QA + perturbation prediction) reframes virtual-cell quality as scientific-reasoning quality. Mark TBD on exact per-model leaderboard ranks until camera-ready PDF is parsed in full.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** SC-Arena is a **benchmark / evaluator**, not a model — it competes with other virtual-cell evaluation harnesses, not with scGPT or Geneformer themselves. The argument the paper makes (knowledge-augmented metrics over string-match F1) is methodological infrastructure: SC-Arena is the *scorecard*, and any single-cell foundation model is a *contestant*. This positioning matters because the 2025–2026 wave of single-cell-FM critique papers (Ahlmann-Eltze & Huber in *Nature Methods* 2025; Csendes et al.; the scPerturBench follow-on) all pointed at the same gap SC-Arena is trying to close: the field had no agreed-upon evaluation harness that distinguished mechanistic understanding from surface pattern-matching.

**Direct peers — single-cell evaluation benchmarks.**

| Benchmark | Scope | Task count | Knowledge-grounding | Released |
|---|---|---|---|---|
| **SC-Arena** (this paper) | virtual-cell reasoning | 5 NL tasks | Cell Ontology + GO + literature | ICLR 2026 |
| **Open Problems in Single Cell Analysis** | scaling community benchmarks across cell-typing, integration, perturbation | ~10 task tracks | manual ground truth | live since 2024, *Nature Biotech* 2024 |
| **Tahoe-100M** | single-cell drug-perturbation atlas — *training and evaluation* substrate, 100 M cells × 1,200 drugs × 50 cell lines | n/a (atlas) | wet-lab Mosaic platform | Vevo / Tahoe Bio, open-sourced Feb 25 2025 |
| **PerturBench / scPerturBench** | perturbation prediction only | 5 datasets + rank metrics | Perturb-seq held-outs | ICLR 2025 / GitHub 2025 |
| **CellBench-LS** | low-supervision single-cell FM probing | 4 transfer tasks | scRNA-seq held-outs | bioRxiv April 2026 |

The differentiator is the NL-reasoning framing — Open Problems and PerturBench measure embedding / prediction quality; SC-Arena scores natural-language outputs, which is the slice that determines how LLM-conditioned single-cell models (scMulan, GenePT, C2S-Scale) get ranked.

**What changed in 2025–2026.**

- **Linear-baseline reckoning (load-bearing).** Ahlmann-Eltze & Huber, *Nature Methods* 2025 ([article](https://www.nature.com/articles/s41592-025-02772-6)), showed scGPT, UCE, scBERT, GEARS, and scFoundation fail to outperform "mean of training perturbations" baselines on Perturb-seq prediction. SC-Arena's perturbation-prediction task suite inherits this critique — any benchmark that does not include the linear baseline as a contestant is rightly suspect after 2025.
- **scPerturBench (BM2 Lab GitHub, 2025).** Independent re-benchmark of single-cell perturbation predictors confirming the linear-baseline result; treated as the de-facto replication.
- **Tahoe-100M release (Feb 25 2025).** 50× larger than all prior open drug-perturbed single-cell data combined ([Vevo press release](https://www.prnewswire.com/news-releases/vevo-therapeutics-open-sources-tahoe-100m-the-worlds-largest-single-cell-dataset-as-the-inaugural-contribution-to-arc-institutes-new-virtual-cell-atlas-302384677.html)). SC-Arena does not yet integrate Tahoe-100M as a perturbation-task source; this is the obvious 2026-Q3 extension.
- **No retraction events** affecting SC-Arena itself, but the linear-baseline finding implicitly retired the headline cell-typing-F1 numbers from the original scGPT / Geneformer / UCE preprints as the sole evaluation axis.

**Cross-AACR relevance.** SC-Arena's *named contestants* (scGPT, Geneformer, UCE, CellFM) are all discussed at the [AACR 2026 ED03 virtual-cells session](../../aacr-2026/topics/virtual-cells/landscape.md) — the ED03 corpus harvest explicitly used `scGPT`, `Geneformer`, and "foundation model" as harvest keywords, with 48 surviving posters. The [AACR scGPT tool dossier](../../aacr-2026/topics/bioinfo-tools/tools/scgpt.md) and [Geneformer dossier](../../aacr-2026/topics/bioinfo-tools/tools/geneformer.md) are the matching corpus entries. Notably, the ED03 landscape audit found "scGPT, Geneformer, and Universal Cell Embeddings do not appear in any title in this slice — they show up only as comparators in abstract bodies" — so SC-Arena is the *methods-side* anchor for what is otherwise an evaluation gap in the AACR virtual-cells slice. Pair with the [virtual-cells landscape](../../aacr-2026/topics/virtual-cells/landscape.md) when writing the cross-meeting synthesis.
