# Genomic Next-Token Predictors are In-Context Learners — Breslow et al. (JHU)

**One-line description** — A controlled-experiment study showing that the Evo2 genomic foundation model exhibits *organically emergent* in-context learning on symbolic reasoning tasks in genomic form, with log-linear gains as in-context demonstrations scale — mirroring large language model ICL behaviour.

- **Authors:** Nathan Breslow, Aayush Mishra, Michael Schatz, Anqi Liu, Mahler Revsine, Daniel Khashabi
- **Affiliation(s):** Johns Hopkins University (Schatz, Khashabi groups)
- **Track / workshop:** ICLR 2026 — **Sci4DL workshop** (Science for Deep Learning)
- **OpenReview:** [forum?id=BJxPhTcrsr](https://openreview.net/forum?id=BJxPhTcrsr)
- **Code:** TBD — JHU groups typically release on github post-meeting
- **Status at ICLR 2026:** Sci4DL workshop accepted paper; March 2, 2026 acceptance

## What it does

The paper asks whether *in-context learning* — the well-known LLM phenomenon where models infer and apply patterns from a few in-context examples — emerges naturally in genomic foundation models trained on DNA next-token prediction. The answer is yes: Evo2 (Arc Institute's 40B-parameter, 1Mb-context DNA model) exhibits ICL on symbolic reasoning tasks framed in genomic form, with log-linear gains as the number of in-context demonstrations grows. The contribution is *the first systematic evidence of organically emergent ICL in genomic sequences*.

## How it works

**Core idea.** Use a paired controlled-experiment design: encode identical symbolic reasoning tasks in two forms — natural-language (fed to a language model) and genomic-sequence (fed to Evo2) — and test whether the genomic FM exhibits in-context learning as the number of in-context demonstrations grows.

**Inputs / outputs.** Inputs are k-shot demonstrations of a symbolic reasoning task plus a query, encoded either as natural-language tokens or as DNA bases; outputs are next-token predictions decoded back to task answers, scored against ground truth.

**Key innovation.** Prior genomic FM evaluations (Nucleotide Transformer, Caduceus, Hyena-DNA) probed *task-specific* downstream performance after fine-tuning; this paper is the first systematic evidence that genomic next-token predictors exhibit *organically emergent* in-context learning — the LLM-style scaling phenomenon — without any task-specific tuning. The comparison baseline is a modern LLM (Qwen3-class).

**Parameters / training details.** Evaluation target: Evo2 (Arc Institute, Hyena-based, 40B parameters, 1Mb context, pretrained on 9.3 trillion nucleotides — *Nature* March 2026). LLM baseline: Qwen3-class. Variable swept: number of in-context demonstrations. Metric: task accuracy vs demonstration count, log-linear fit.

**Canonical experiment.** On the symbolic-reasoning task suite encoded in both forms, Evo2 shows log-linear gains in pattern-induction accuracy as the number of in-context demonstrations grows — mirroring the canonical LLM ICL scaling curve. This is the load-bearing result: it argues Evo2's pretraining has induced general-purpose pattern-induction capabilities rather than only sequence-specific memorisation (TBD — exact accuracy curves from workshop PDF).

## Headline benchmarks

The paper reports **log-linear gains in pattern induction as the number of in-context demonstrations increases**, matching the canonical LLM ICL scaling behaviour. Specific accuracy curves and task-suite definitions are in the workshop PDF (TBD — full numbers).

## Where it fits in the corpus

- **AACR 2026 virtual-cells axis:** indirect — ICL in genomic LMs is the methodological precondition for using these models as zero-shot variant-effect predictors over patient genomes.
- **ICML 2026 LCFM (long-context FM workshop):** primary venue for follow-on work on context scaling and ICL in DNA LMs.
- **NeurIPS 2026:** Evo2 is the headline genomic-FM release of 2025–2026; expect a NeurIPS paper from Arc Institute itself.
- **AGBT 2026:** likely Evo2 application demos at the platform session.
- **ASHG 2026 / ESHG 2026:** clinical-genomics adaptation venues.

## Notes

Evo2 itself (Arc Institute, Hyena-based, 40B params, 1Mb context) was published in *Nature* March 2026; this ICLR 2026 Sci4DL paper is a methodological study *of* Evo2 rather than a new model release. It serves the AACR vault's "long-context genomic LM" slot as the canonical 2026-era reference point — and the JHU-led "Evo2 as in-context learner" framing is the bridge between the genomic-FM and LLM-reasoning communities that the AACR agentic-AI axis sits on top of. The Sci4DL workshop venue (not LMRL or MLGenX) is itself notable — this is methods-paper community, not bio community, signalling that genomic LMs are now methodologically interesting *on their own terms*.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** Breslow et al. is an **ICL benchmark study performed on Evo2**, not a new model and not a stand-alone benchmark suite. Evo2 (Arc Institute / NVIDIA / Stanford / UC Berkeley / UCSF, 40B parameters, 1Mb context, 9.3 trillion nucleotide pretraining; *Nature* 2026) is the underlying model whose capabilities are being probed — the paper's contribution is the *finding* that ICL emerges in genomic next-token predictors, not the Evo2 release itself. The competing object class is therefore the set of *genomic foundation models* that could in principle be re-evaluated with the same paired NL-vs-DNA protocol, plus the small handful of "genomic ICL"-style probing studies.

**Direct peers — long-context genomic foundation models.**

| Model | Backbone | Parameters | Context | Pretraining substrate | Released |
|---|---|---|---|---|---|
| **Evo2** (Arc Institute) | Hyena / StripedHyena | 40B | 1 Mb (single-nucleotide) | 9.3 T nucleotides, all-domains | *Nature* 2026 ([Arc Evo2](https://arcinstitute.org/tools/evo)) |
| **AlphaGenome** (Google DeepMind) | Transformer | TBD-disclosed | 1 Mb input → base-pair tracks | human + mouse genomes | *Nature* 2025 ([DeepMind AlphaGenome](https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/)) |
| **Nucleotide Transformer** (InstaDeep / NVIDIA) | Transformer | 50M – 2.5B | 6 kb – 12 kb | 850 species | *Nat Methods* 2024 |
| **HyenaDNA** (Stanford) | Hyena | 0.4M – 6.6M | up to 1 Mb | human reference | NeurIPS 2023 |
| **Caduceus** (Cornell / Stanford) | bidirectional Mamba / Hyena | tens of M | up to 131 kb | human reference | ICML 2024 |

Evo2 is unique in this peer set for combining 40B parameters, a 1 Mb context, and all-domains-of-life pretraining; AlphaGenome is its primary 2025 competitor and **outperforms or matches Evo2 in 25 of 26 regulatory-variant-effect evaluations** ([AlphaGenome Nature paper](https://www.nature.com/articles/s41586-025-10014-0)), though only on a human + mouse pretraining substrate and with a *different model class* (track-prediction transformer, not generative DNA LM). For the *ICL phenomenon Breslow et al. study*, none of AlphaGenome / Nucleotide Transformer / HyenaDNA has been shown to exhibit log-linear ICL scaling — Evo2 is the load-bearing positive case.

**What changed in 2025–2026.**

- **Evo2 *Nature* publication, March 2026.** Confirmed: 40B parameters, 1 Mb context, 9.3 trillion nucleotides, predicts BRCA1 variant pathogenicity zero-shot ([Arc Institute Evo2 release](https://arcinstitute.org/news/evo2); [Nature article](https://www.nature.com/articles/s41586-026-10176-5)).
- **AlphaGenome (Google DeepMind, June 2025).** Direct head-to-head competitor; outperforms or matches Evo2 in 25/26 regulatory-variant-effect benchmarks; available via API for non-commercial use ([github.com/google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome)). Crucially, AlphaGenome is a *track-prediction* model, not a generative LM, so it cannot be probed for ICL the same way Evo2 can.
- **BioReason (AACR 2026, surfaced via the AI Revolution in Cancer Research session, 2026-04-20).** Freezes Evo2 and aligns DNA-sequence tokens to language tokens with RL to teach DNA-in-context-of-language ([transcript line 619](../../aacr-2026/sessions/2026-04-20-am-ai-revolution-in-cancer-research.md)). This is the *clinical-genomics analogue* of Breslow et al.'s ICL claim — same backbone, different downstream framing.
- **Evo 2 "One Year Later"** ([Arc Institute retrospective](https://arcinstitute.org/news/evo-2-one-year-later)) — community traction, fine-tuning recipes, downstream applications.
- **No retraction events** affecting Evo2, AlphaGenome, or this Breslow et al. paper.

**Cross-AACR relevance.** Direct cross-link to the [AACR 2026 AI Revolution session](../../aacr-2026/sessions/2026-04-20-am-ai-revolution-in-cancer-research.md), which contains the only explicit Evo2 references in the AACR 2026 vault — specifically the BioReason talk (transcript lines 619 and 629) that freezes Evo2 and aligns it to language tokens. Breslow et al.'s ICL finding is the methodological substrate that makes that BioReason pipeline plausible: if Evo2 already exhibits ICL on genomic sequences, then aligning DNA tokens to NL tokens via a frozen-backbone RL recipe is asking the model to do something it has already learned to do natively. Indirect cross-link to the [AACR virtual-cells landscape](../../aacr-2026/topics/virtual-cells/landscape.md) — none of the 48 AACR virtual-cells posters cites Evo2 directly, which makes this dossier the *external anchor* for genomic-LM ICL at AACR 2026. The AACR vault has no Evo2 tool dossier; this ICLR 2026 entry is the de-facto placeholder until one is written.
