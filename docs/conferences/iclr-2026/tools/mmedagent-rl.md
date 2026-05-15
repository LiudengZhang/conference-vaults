# MMedAgent-RL — Multi-Agent RL for Multimodal Medical Reasoning

**One-line description** — A reinforcement-learning–trained multi-agent collaboration framework for multimodal medical reasoning over images and clinical text, where specialist agents (radiology, pathology, EHR) are coordinated by a planner agent and tuned end-to-end with RL.

- **Authors:** TBD — author roster not surfaced in scrape; "MMedAgent-RL" team at a Chinese-academia / industry consortium per ICLR 2026 papers digest
- **Affiliation(s):** TBD
- **Track / workshop:** ICLR 2026 main track — poster (designation TBD-verify against virtual schedule)
- **OpenReview:** TBD — to be linked once forum ID is parsed
- **Code:** TBD
- **Status at ICLR 2026:** main-track accept (per Paper Copilot / Bohrium digest)

## What it does

MMedAgent-RL coordinates a team of specialist LLM-based agents — each pinned to a different medical modality (CT/MRI, whole-slide pathology, structured EHR, free-text clinical notes) — and trains the *coordination policy* between them with reinforcement learning. The framework targets the multi-hop medical-reasoning regime where no single modality is sufficient (e.g. radiology + pathology + history to triage a tumour case).

## How it works

**Core idea.** Coordinate a team of modality-specialist LLM agents (radiology VLM, pathology VLM, EHR-tuned LLM, free-text clinical-note LLM) via a planner agent, and use reinforcement learning to optimise the *coordination policy* — when each specialist is invoked and how their evidence is aggregated.

**Inputs / outputs.** Inputs are multi-modal clinical cases (CT/MRI volumes, whole-slide pathology, structured EHR, free-text notes); outputs are the planner's final diagnosis or recommendation plus the agent dialogue trace explaining the reasoning chain.

**Key innovation.** Single-agent medical VLMs (Med-PaLM-M, LLaVA-Med, RadFM) collapse all modalities into one backbone; prior multi-agent medical systems (AgentClinic, MedAgent) hard-code the coordination policy. MMedAgent-RL learns the coordination policy via RL on verifiable medical reasoning rewards — the recipe shared with the 2026 AgentFlow / GLM-Agent wave, ported into the clinical-imaging multi-agent setting (TBD-verify against camera-ready for the exact RL algorithm — likely GRPO / PPO-class).

**Parameters / training details.** Specialist agents initialised from domain-tuned VLMs / LLMs (TBD — specific backbones from camera-ready). RL reward: verifiable multi-modal medical-reasoning task accuracy. Training environment: multi-modal MedQA-class benchmarks (TBD-verify).

**Canonical experiment.** The paper benchmarks MMedAgent-RL against single-agent VLM baselines and rule-coordinated multi-agent baselines on multi-modal medical reasoning suites; Paper Copilot / Bohrium ICLR 2026 digests cluster it with MedAgentGym, M3CoTBench, MedVLSynther, and CARE as the main-track medical-AI cohort, with the headline accuracy numbers in the camera-ready (TBD — full parse).

## Headline benchmarks

Bohrium / Paper Copilot ICLR 2026 highlights flag MMedAgent-RL alongside MedAgentGym, M3CoTBench, MedVLSynther, and CARE as the main-track medical-AI cohort. Specific accuracy numbers across MedQA / multi-modal benchmarks are in the camera-ready (TBD — parse).

## Where it fits in the corpus

- **AACR 2026 agentic-AI axis:** secondary cross-link — pair with the AACR tumour-board agent demos and the RSNA-style radiology-pathology integration sessions.
- **MedAgentGym (this vault):** sibling submission; MedAgentGym is the *training environment*, MMedAgent-RL is a *trained multi-agent policy* using a similar paradigm.
- **MICCAI 2026 / RSNA 2026:** primary clinical-imaging cross-link — expect adapted versions at RSNA's AI plenary.
- **SITC 2026:** if extended to immuno-oncology multi-modal trial-matching, plausible adapt.

## Notes

This entry is **lightly verified** — title and accept status are confirmed via two third-party ICLR 2026 highlights digests (Paper Copilot, Bohrium), but the author roster and OpenReview forum ID need a second pass once camera-ready PDFs are fully indexed. Hold this entry as a placeholder for the multi-agent medical-reasoning slot until the metadata pass completes. The 2026 main-track medical-AI cohort (MedAgentGym + MMedAgent-RL + M3CoTBench + MedVLSynther + CARE) collectively is the strongest single-conference clustering of clinical agentic-AI to date — the AACR vault's "agentic AI for oncology" axis should treat this cohort as the methodological substrate for SITC 2026 / AACR 2027 demos.
