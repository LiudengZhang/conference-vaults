# Day 1 PM — Co-Scientist demos, MLOps, GPUs, reproducibility

**Date:** 2026-04-30 (afternoon)
**Source transcript:** [`2026-04-30-nextflow-summit-day-1-pm`](../sessions/2026-04-30-nextflow-summit-day-1-pm.md)

The afternoon swung between vendor demos (Seqera Co-Scientist on protein design, GSK's MCP-per-pipeline architecture) and grounded counter-takes (GPU economics, Bactopia's failed-LLM-rewrite story, Tommy Tang's reproducibility keynote). The honest takeaway: agents work, but only on top of typed pipelines, machine-readable contexts, and human-gated promotion.

---

## 1. From Stack Overflow to Co-Scientist — agentic protein design
**Tycho** (Seqera; collaborator: Rashni)

Walks through a Nipah-virus protein-G binder design competition (hosted by ProteinBased) on Nebius GPU cloud. Contrasts the manual six-tool pipeline of a year ago with today's **Seqera Co-Scientist** flow:

- **Infrastructure** — agent spins up a Kubernetes/compute env
- **Pipeline development** — a colleague extended an existing pipeline with **RFdiffusion 3** end-to-end in 44 min
- **Interpretation** — auto-ranks top 5 binders from run outputs at `ai.seqera.io`

**Tools shown:** BoltzGen, ProteinMPNN, RFdiffusion (v3), Nebius GPU cloud, BYOK enterprise deploy, token-scoped guardrails, full lineage/audit context.

**Q&A highlights:** BYOK so prompts never leave your AI provider (pharma data-egress fear); continuous evals with ground truth; foundation-model knowledge plus paper-fetch tools for biological context.

**Why it matters:** The 44-min RFdiffusion-3 module-add is the most concrete "agents shipping pipelines" data point of the conference.

---

## 2. ADMET property prediction — Nextflow as MLOps engine
**Anthony Reyes** (background: NASA/JPL ML platforms, SMS scheduling NLP)

ML pipeline that predicts ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity) from SMILES strings for a bench chemist's CADD tool.

**Architecture:** internal assay extraction → RDKit feature/descriptor expansion → parallel model training (sklearn classical models on ECS CPU; deep nets on AWS Batch GPU) → MLflow autologging → containerized inference API.

**Backstory:** SageMaker tried first; team fell back to Nextflow due to familiarity. Human-gated promotion (no auto-deploy to prod).

**Why it matters:** Nextflow used as a general-purpose MLOps engine on a non-bioinformatics problem (cheminformatics). Useful counterexample to "Nextflow is for genomics."

---

## 3. Three GPU case studies in genomics
**Jason Warner** (Principal Scientific Consultant, Diamond Age Data Science)

Anti-hype GPU talk:

1. **NVIDIA Parabricks as drop-in for GATK** — minimal Nextflow changes (`accelerator` directive + AWS Batch GPU queue), 10× speed/cost only worth it above ~10–20 samples
2. **Custom gene-editing workflow** — only the mapping step was GPU-friendly; switching back to CPU Python downstream killed the gains
3. **Single-cell QC** — moving to GPU via RAPIDS / scVI

**Reusable rule:** profile first, refactor only if the whole pipeline can stay on the GPU (FUSE / file-staging overhead eats hybrid pipelines).

**Why it matters:** A useful counter to the keynote's GPU enthusiasm — for small batch sizes or hybrid Python downstream, GPUs can be a net loss.

---

## 4. Lightning round

- **Alejandro** (Sanford / Stowers) — regulatory potential analysis across thousands of TFBS in NCBI + newly assembled TOGA genomes; oxygen-sensing pathway shows distinct circuits in marsupials and monotremes; metabolism genes cluster by lifestyle (diving, high metabolic rate).
- **Pediatric leukemia long-read speaker** — updates to **nf-core/longread** for PacBio HiFi: adds **Sawfish** (SV caller), **HiFiCNV** (CNV caller), variant annotation, per-CpG methylation in pb-CpG-tools, and **fibertools** for fiber-seq adenine methylation.
- **Aditi** — short pitch on autonomous-lab / microscope vision (mostly garbled in transcript).

---

## 5. Avoiding AI slop — Bactopia v4 with strict syntax + custom linters
**Robert Petit** (Wyoming Public Health Lab)

History of bacterial genomic surveillance post-COVID and the under-resourced public-health-lab user. Tried a wholesale LLM rewrite of Bactopia — failed. Ended up doing it by hand, but with a tight feedback loop on top:

- Small machine-readable context indices
- **Custom linters** for Nextflow code patterns
- Inline **Groovy doc** replacing meta YAML
- Dev-side Claude Code skills (e.g., "add a Bactopia tool")
- AI-aided migration to **Nextflow 26.04 strict syntax** + record types

**Bactopia v4 stats:** fully rewritten, strict syntax, static types, ~250 modules / 70 standalone workflows, plus a Python package and plugin.

**Why it matters:** Most honest "we tried full LLM auto-port and it didn't work" story at the summit. The win came from building agent guardrails (linters + indices + skills), not from a smarter agent.

---

## 6. Pipelines as infrastructure — GSK's Omics Workbench
**Janae Adams** (GSK Data Automation & Computational Sciences; with Francine Mira & Mike Gonzalez)

GSK's **Omics Workbench** wraps Nextflow with a standardized pipeline template (params, error handling, Docker catalog, reference configs) so ~100 teams interoperate. Pipelines are versioned, typed, queryable, modular — i.e. machine-readable.

**The vision:** one **MCP server per pipeline**, so an LLM agent can only invoke catalog pipelines (no hallucinated ones), bridging to GSK's "**Lab in a Loop**" automated experiment cycle.

**Stack:** GCP Batch + BigQuery + Seqera Platform + GCP artifact registry. Project began ~2022.

**Org pattern:** centralized reference-genome workspace, weekly Nextflow office hours, internal "core developer" cohort.

**Why it matters:** Concrete blueprint for how a regulated pharma exposes a curated Nextflow catalog to LLMs without hallucination risk — quietly underway since 2022, only now being talked about.

---

## 7. Closing keynote — Reproducibility in the age of AI
**Tommy Tang** (AstraZeneca)

Cites Titus Brown's "95% of bioinformatics analyses can't be reproduced" and the **Anil Potti / Keith Baggerly** MD Anderson scandal (a row-shifted spreadsheet that halted clinical trials) as motivation.

**Six pillars of "good enough" practice:**

1. Tidy data + spreadsheet hygiene (Karl Broman & Karl Woo)
2. Project organization & file naming (Jenny Bryan)
3. Git — six commands suffice
4. Environment management — mamba / uv / renv + Docker / Singularity, Rocker
5. Literate programming (RMarkdown, Quarto, Marimo) + automation (shell → Snakemake / Nextflow / WDL)
6. Clean code & functions (purrr, tidyverse, packaging)

**LLM caveat (closing):** outputs drift even at temperature 0. Use AI as an **orchestrator that fills a Quarto template**, not as the analysis itself. Live demo: identical prompt to AstraZeneca's internal agent produced different reports/figures across runs.

**Q&A:** tertiary analysis remains hard to reproduce; suggests journals should require peer reproduction as a submission gate.

**Why it matters:** The conference's most pointed pushback on agent maximalism — and the LLM-drift demo gives a concrete reason to keep humans in the loop.

---

## Cross-cutting threads

- **Agentic AI on Nextflow** converges on three patterns: Co-Scientist (Seqera), MCP-per-pipeline (GSK), template-orchestrator (Tang).
- **Pipeline as data product** — typed I/O, versioning, schemas (Nextflow 26.04 `output {}` syntax came up in Q&A).
- **Guardrails and evals** — token-scoped permissions, BYOK, regression eval suites, human-gated promotion.
- **GPU strategy** — only worth it at scale; profile bottlenecks first; watch CPU↔GPU transitions.
- **Standardization** — pipeline templates, shared Docker registries, central reference genomes, internal core-dev cohorts.

See [Themes & takeaways](../themes.md) for cross-day synthesis.
