# MedAgentGym — Ran Xu et al. (Emory + UT Southwestern + collaborators)

**One-line description** — A scalable agentic training environment for code-centric biomedical reasoning, with 72,413 task instances across 129 categories drawn from 12 real-world biomedical scenarios, plus an open-sourced 7B "Med-Copilot" agent that competes with GPT-4o after RL fine-tuning.

- **Authors:** Ran Xu, Yuchen Zhuang, Yishan Zhong, Yue Yu, Zifeng Wang, Xiangru Tang, Hang Wu, May D. Wang, Peifeng Ruan, Donghan Yang, Tao Wang, Guanghua Xiao, Xin Liu, Carl Yang, Yang Xie, Wenqi Shi
- **Affiliation(s):** Emory University; UT Southwestern Medical Center; Georgia Tech; Yale — full affiliation map inferred from author roster, TBD-verify against camera-ready
- **Track / workshop:** ICLR 2026 main track — **Oral**
- **OpenReview:** [forum?id=jHDZEUgS4r](https://openreview.net/forum?id=jHDZEUgS4r)
- **arXiv:** [2506.04405](https://arxiv.org/abs/2506.04405)
- **Code:** [github.com/wshi83/MedAgentGym](https://github.com/wshi83/MedAgentGym)
- **Status at ICLR 2026:** Main-track Oral, Jan 26 2026 acceptance; CC-BY 4.0

## What it does

MedAgentGym is an interactive training-and-evaluation environment for LLM agents that write executable code over biomedical datasets. It bundles 72,413 task instances spanning 129 categories — pulled from 12 authentic biomedical scenarios (EHR cohort analytics, biostats over clinical trials, single-cell / bulk omics processing, medical-imaging analysis, etc.) — each wrapped in a sandboxed executable environment with verifiable ground-truth annotations and multi-turn feedback.

## How it works

**Core idea.** MedAgentGym wraps 72,413 biomedical task instances in sandboxed, executable environments with verifiable ground-truth checkers, then uses the same environment as both an evaluation benchmark and a training loop — supervised fine-tuning plus online RL on multi-turn agent trajectories yields the Med-Copilot-7B model.

**Inputs / outputs.** Inputs are natural-language biomedical task specs (e.g. "compute Kaplan-Meier survival for the high-mutational-burden cohort in this EHR slice") plus optional dataset handles; outputs are executable code, intermediate execution traces, and final answers checked against ground-truth annotations.

**Key innovation.** Versus AgentClinic (NeurIPS 2025, bedside dialogue) and prior medical LLM benchmarks (MedQA, MedMCQA — single-turn QA), MedAgentGym is broader (129 categories across 12 scenarios — EHR cohort analytics, biostats, single-cell / bulk omics, medical imaging), code-centric, and explicitly trains agents — not just evaluates them.

**Parameters / training details.** Base model: Qwen-2.5-7B-class for Med-Copilot-7B (TBD-verify backbone). Training: multi-threaded multi-turn trajectory sampling, SFT on filtered successful trajectories, then offline + online RL. 29 commercial + open-source LLMs benchmarked at zero-shot.

**Canonical experiment.** Across the full 72k-task suite, Med-Copilot-7B reports +43.02 % gain from offline RL and +45.28 % from online RL over the SFT baseline, ultimately performing competitively with GPT-4o despite the 7B parameter budget — the headline result the paper uses to argue for the privacy-preserving open-source code-agent recipe.

## Headline benchmarks

- Med-Copilot reports **+43.02 % (offline RL) and +45.28 % (online RL) performance gains** over the SFT baseline across the full task suite.
- After tuning, Med-Copilot-7B is **competitive with GPT-4o** as a privacy-preserving, cost-efficient alternative for code-based biomedical reasoning.
- A substantial gap between commercial and open-source models is reported across all 29 LLMs at the zero-shot evaluation tier (numbers in camera-ready tables, TBD-parse).

## Where it fits in the corpus

- **AACR 2026 agentic-AI axis:** primary cross-link — this is the closest 2026-vintage analogue to TissueAgent / TumorBoard agents from the AACR program, but with a public training environment and a released 7B model.
- **ICML 2026:** likely follow-on submissions to GenBio / FM4LS workshops; Med-Copilot agent is the natural baseline for future SITC / RSNA agentic-AI demos.
- **NeurIPS 2026:** expect an extended benchmark + leaderboard track.
- **Nextflow Summit 2026:** workflow-execution overlap — MedAgentGym sandboxes have similar reproducibility framing to Nextflow's compute-aware execution.

## Notes

The release strategy (full Gym + Med-Copilot-7B weights + 72k task instances) is unusually generous for an ICLR oral and is what makes this the load-bearing agentic-AI entry from ICLR 2026. The closest sibling at NeurIPS 2025 was AgentClinic; MedAgentGym is broader (data-science, not bedside dialogue) and explicitly code-centric, which is the right scope for the AACR vault's "agent that writes a CCLE re-analysis" downstream use case.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** MedAgentGym is an **agentic-AI gym / sandbox** — sandboxed executable environment plus verifiable ground-truth checkers, doubling as a benchmark and a training substrate. It is not a model (though it releases Med-Copilot-7B as a worked example), not a knowledge graph, and not a workflow orchestrator. The competing object class is the *biomedical agent benchmark / arena*: BixBench, ScienceAgentBench, BioMedArena, BioDSA-1K, BioML-bench. Med-Copilot-7B itself is in the same model family as AgentClinic's training-loop baselines and the Qwen-2.5-7B Med-X derivatives, distinguished by its code-centric, multi-turn RL recipe.

**Direct peers — agentic biomedical benchmarks / sandboxes.**

| Sandbox / arena | Task count | Domain breadth | Trains agents? | Released |
|---|---|---|---|---|
| **MedAgentGym** (this paper) | 72,413 instances / 129 categories | 12 biomedical scenarios (EHR, biostats, omics, imaging) | yes — SFT + offline + online RL | ICLR 2026 oral |
| **BioMedArena** ([arXiv 2605.06177](https://arxiv.org/abs/2605.06177)) | 147 benchmarks + 75 tools / 9 families | biomedical deep-research | evaluation only | 2026 |
| **ScienceAgentBench** ([OSU-NLP-Group/ScienceAgentBench](https://github.com/OSU-NLP-Group/ScienceAgentBench)) | per-task atomic scientific-workflow steps | data-driven science (broader than biomedical) | evaluation only | ICLR 2025 |
| **BixBench** ([arXiv 2503.00096](https://arxiv.org/abs/2503.00096)) | ~50 real-world scenarios / ~300 open-answer Qs | bioinformatics data exploration | evaluation only | 2025 |
| **BioML-bench** ([bioRxiv 2025.09.01.673319](https://www.biorxiv.org/content/10.1101/2025.09.01.673319v3.full)) | end-to-end biomedical ML pipelines | biomedical ML modeling | evaluation only | Sept 2025 |
| **AgentClinic** (NeurIPS 2025) | bedside dialogue scenarios | doctor–patient simulation | evaluation only | 2025 |

The differentiator is scale (72k vs ~50–300 tasks elsewhere), the *training* leg of the loop (online RL on multi-turn trajectories, not just zero-shot evaluation), and code-centric scoping (executable code over real biomedical datasets, not multiple-choice or open-ended generation). No other 2025–2026 biomedical agent benchmark releases a tuned 7B model with weights.

**What changed in 2025–2026.**

- **Critical mass of biomedical agent benchmarks.** BioMedArena (2026), BioDSA-1K (2025), BixBench (2025), BioML-bench (Sept 2025), BioProBench (2025) all landed inside a 12-month window — MedAgentGym entered an arena that did not really exist when it was first drafted in mid-2025.
- **The "linear-baseline" critique** from the single-cell space ([Ahlmann-Eltze & Huber, *Nature Methods* 2025](https://www.nature.com/articles/s41592-025-02772-6)) has its agentic-AI analogue: several 2025 biomedical-agent papers were re-benchmarked against minimal-tool-use baselines and found wanting. MedAgentGym's reported **+43.02% offline RL / +45.28% online RL gains over SFT** are the headline numbers that should be checked against this skepticism — the relative gains are large, but absolute task-completion ceilings remain modest on the hardest categories (camera-ready tables, parse pending).
- **Med-Copilot-7B competitive with GPT-4o.** The headline finding from the paper. With GPT-4o now superseded by Claude Sonnet 4.6 / GPT-5-class models in 2026-Q1, the comparison frame is already aging — a re-run against frontier 2026 models is the expected ICML 2026 / NeurIPS 2026 follow-on.
- **No retraction events** affecting MedAgentGym itself or AgentClinic.

**Cross-AACR relevance.** Primary cross-link to the [AACR 2026 AT02 agentic-AI session](../../aacr-2026/sessions/2026-04-21-at02-agentic-ai-cancer-researcher.md), the central oncology-side agentic-AI anchor at AACR. The [AACR agentic-AI landscape](../../aacr-2026/topics/agentic-ai/landscape.md) classifies the AACR corpus into 6 agent archetypes — copilots, workflow agents, multi-agent systems, LLM-as-classifier, multimodal specialty, and other — across 57 posters; MedAgentGym is the *training-and-evaluation infrastructure* missing from that AACR corpus, where every poster ships its own bespoke evaluation harness. Pair specifically with AACR posters #18 (GP CoPilot), #22 (multi-agent CAR-T), #4 (multi-agent CRC ecosystem), and #21 (MERSCOPE analysis agent) when writing the cross-meeting synthesis — these are the AACR analogues that would benchmark naturally inside a MedAgentGym EHR / omics / imaging slot. The [synthesis-at02-vs-corpus.md](../../aacr-2026/topics/agentic-ai/synthesis-at02-vs-corpus.md) is the existing AACR synthesis page that should be updated to cite Med-Copilot-7B as the public-weights baseline.
