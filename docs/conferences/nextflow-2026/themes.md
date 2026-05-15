# Themes & takeaways — Nextflow Summit 2026

Cross-day synthesis of the recurring threads, surprising bits, and named entities across [Day 1 AM](digest/day-1-am.md), [Day 1 PM](digest/day-1-pm.md), and [Day 2](digest/day-2.md).

---

## The five threads

### 1. Agentic AI on top of Nextflow

Almost every talk touched this. Three concrete patterns emerged:

- **Co-Scientist (Seqera)** — model-agnostic, BYO-key agent across infra, pipeline development, and result interpretation. Demoed via Tycho's 44-min RFdiffusion-3 module-add and the closing keynote's autonomous closed-loop optimizer.
- **MCP-per-pipeline (GSK)** — expose a curated catalog through Model Context Protocol so an LLM can only invoke vetted pipelines. Quietly underway since 2022. Echoed in Microsoft's Foundry demo (a "Seqera coding agent" connected via MCP autonomously identified a plasmodium dataset).
- **Template orchestrator (Tommy Tang)** — opposite end of the spectrum: AI fills in a Quarto template, humans own the analysis. Justified by his on-stage demo of LLM output drift even at temperature 0.

**The honest counter-takes:**

- Phil Ewels' Rust-QC succeeded only because **nf-test snapshots** acted as a deterministic verification target ("emulate-then-rewrite," not "invent").
- Robert Petit (Bactopia v4) tried wholesale LLM auto-port and **abandoned it** — the win came from custom linters + machine-readable indices + Claude Code skills, not a smarter agent.
- Lorena's bake-off picked Seqera AI over Claude and Grok primarily on **context, not model quality**.

### 2. Pipeline as data product / contract

The recurring engineering pattern: typed inputs, typed outputs, typed channels, schemas, versioning, machine-readable metadata. Specific instances:

- **Nextflow 26.04** — typed `params`, typed channels, typed process I/O, new `output {}` syntax (Paolo)
- **Nextflow Modules** as the packaging primitive above containers, with `nextflow model` CLI and semantic search (Paolo)
- **Bactopia v4** — strict syntax, record types, ~250 modules / 70 standalone workflows (Petit)
- **GSK Omics Workbench** — standardized pipeline template that ~100 teams interoperate against (Adams)

The throughline: pipelines must be machine-readable before agents can call them safely.

### 3. Cloud cost & compute reform

Three independent talks landed on the same insight: **the cloud-batch model is the wrong abstraction.**

- **Seqera Intelligent Compute** (Floden, Paolo) — new scheduler replacing AWS Batch: spot optimization, right-sizing, bin-packing. Demos: $5/sample → $2/sample, $34 → $15 on the same workload.
- **Azure storage tiering** — POSIX hot tier (Lustre / NetApp / NFS) in front of object cold tier; reframe "cores per dollar" as "**science per dollar**."
- **Jason Warner's GPU realism** — Parabricks 10× only above ~10–20 samples; hybrid CPU/GPU pipelines lose to FUSE/staging overhead.

### 4. Community & training as the moat

- Training portal in **11 languages** with an open-source AI translation harness (fixes are made in the prompt, not the file)
- Ambassador program: 5 → 143 ambassadors, 16 → 40 countries in 2.5 years; deliberately non-monetary recognition
- Hackathons framed as fun / collaborative / non-competitive: 600 participants across 19 time zones in March
- Internal patterns echoed at GSK (weekly Nextflow office hours, internal "core developer" cohort)

### 5. Real scientific applications

A useful counterweight to the AI talk track:

- **Vaccinology** — `prodvac-seq` for proactive pandemic preparedness (multiplexed barcoded pseudovirus + DMS)
- **Microbial genotyping** — MGTree where Kraken2 fails on closely-related references; caught a co-infection Sanger missed
- **Spatial omics** — nf-spatial standardized Xenium preprocessing
- **Cheminformatics** — Anthony Reyes' ADMET pipeline (Nextflow as MLOps engine, not bioinformatics)
- **Long-read pediatric leukemia** — nf-core/longread additions for PacBio HiFi (Sawfish, HiFiCNV, fibertools)
- **Cross-species single-cell** — `sc-samap` (axolotl, killifish, zebrafish)
- **Downstream RNA-seq** — Reema's pipeline starting from count matrices (overlaps with nf-core/differentialabundance)
- **Pfizer iFox** — enterprise OMICs unification on Lamin

---

## Surprises worth flagging

| Surprise | Speaker | Why it stood out |
|---|---|---|
| **$10K Anthropic spend** for Rust-QC | Phil Ewels | Rare cost transparency — gives a concrete dollar figure for AI-driven legacy rewrites |
| **Seqera explicitly rebuilds the cloud scheduler** | Floden | Public admission that AWS Batch's HPC-mimicking model is the wrong primitive |
| **MCP server per pipeline** | GSK / Janae Adams | Concrete blueprint for regulated pharma agent deployment, quietly in progress since 2022 |
| **LLM output drift at temperature 0** | Tommy Tang | Same prompt, same model, different reports — the on-stage demo justifying "humans own the analysis" |
| **Microsoft Foundry agent identifies a 6-year-old BioProject** | Microsoft demo | Strongest end-to-end agent demo at the conference |
| **44-minute RFdiffusion-3 pipeline extension** | Tycho (Seqera) | Most concrete "agents shipping pipelines" data point |
| **Closed-loop optimization can mutate model architecture** | Floden | Hill-climbing across params + tools + model architectures inside a training pipeline |
| **MGTree caught a co-infection Sanger missed** | Scott Norton (Merck) | Concrete real-world validation of replacing the off-the-shelf tool |
| **Tamagotchi pixel-art contest** | (closing) | Conference whimsy worth noting |
| **Phil's "$10K" + Lorena's "5 min plan"** | Day 1 AM | Two contrasting cost framings on the same day — both real |
| **Antigravity-orchestrated agents at the hackathon** | Harrison | Auto-cleaned ~2,000 nf-core modules; punchline that agents now outnumber humans at the hackathon |
| **Lamin = "GitHub for data"** | Pfizer / Joe | Rare enterprise-scale Lamin adoption, with a memorable framing |

---

## Tools & entities — quick index

**Where each tool/entity surfaced:**

| Tool / entity | Day 1 AM | Day 1 PM | Day 2 |
|---|:-:|:-:|:-:|
| Seqera Co-Scientist | ✓ | ✓ | ✓ |
| Seqera Intelligent Compute | ✓ | | |
| Seqera Studios | ✓ | | ✓ |
| Seqera Fusion | | | ✓ |
| Nextflow 26.04 (strict syntax, modules) | ✓ | ✓ | |
| nf-core/rnaseq | ✓ | | ✓ |
| nf-core/sarek (GPU) | ✓ | | ✓ |
| nf-core/longread | | ✓ | |
| nf-core/differentialabundance | | | ✓ |
| nf-core/cellpainting | | | ✓ |
| Rust-QC | ✓ | | |
| MultiQC | ✓ | | |
| Bactopia v4 | | ✓ | |
| MGTree | ✓ | | |
| nf-spatial | ✓ | | |
| prodvac-seq | ✓ | | |
| sc-samap (SAMap) | | | ✓ |
| Eider (DuckDB h5ad reader) | | | ✓ |
| RFdiffusion / BoltzGen / ProteinMPNN | | ✓ | |
| RDKit / sklearn / MLflow | | ✓ | |
| NVIDIA Parabricks | | ✓ | |
| RAPIDS / scVI | | ✓ | |
| MCP servers | ✓ | ✓ | ✓ |
| Lamin / LaminDB / Bionty | | | ✓ |
| Microsoft Foundry / Foundry Local / Foundry IQ | | | ✓ |
| Benchling AI integration | ✓ | | |
| Wave (containers) | ✓ | | |
| Claude Code (skills) | ✓ | ✓ | ✓ |
| Antigravity | | | ✓ |
| Quarto / RMarkdown / Marimo | | ✓ | |
| mamba / uv / renv / pixi | | ✓ | |
| Snakemake / WDL | | ✓ | |
| nf-test (snapshots as agent harness) | ✓ | | |
| GxP packages (FDA/EMA/GLP/GCP/GMP) | ✓ | | |
| AWS Batch | ✓ | ✓ | ✓ |
| Azure Batch / AKS / CycleCloud / Lustre / NetApp | | | ✓ |
| GCP Batch / BigQuery | | ✓ | |
| Nebius GPU cloud | | ✓ | |
| Obsidian / Notion (LLM second brain) | | | ✓ |

**Companies / institutions named:** Seqera, NVIDIA, Anthropic, AWS, Azure, GCP, Nebius, Benchling, GSK, AstraZeneca, Pfizer, Merck, Sanofi(?), Novo Nordisk, Diamond Age Data Science, Wyoming Public Health Lab, Imperial College London, UAB, MDI Biological Lab, Northeastern, CUNY, Grail, MD Anderson, UC Davis (Titus Brown), Fred Hutch (Bloom lab), Francis Crick, Cambridge, Microsoft, "David Vision" (Pfizer Austria partner).

**Standards / frameworks named:** GxP, GLP, GCP, GMP, GAMP, FDA/EMA guidelines, Okta, Entra (Azure AD), MCP (Model Context Protocol).

---

## Predictions to watch

From the closing panel and threaded across the keynotes:

1. **Systems beat models.** The long-term winners are agent harnesses with reasoning + domain context + tool/data access — not any specific frontier model.
2. **The bioinformatician shifts from executor to orchestrator/architect.** Hands-on data wrangling becomes agent-mediated; human attention moves to evaluation, governance, and biology.
3. **Verification harnesses (nf-test snapshots, schemas, lineage) become the load-bearing primitive** — without them, AI rewrites and agent-driven pipelines aren't trustable.
4. **Modules — not containers — are the right packaging primitive.** Agent-discoverable via semantic search, runnable standalone with `nextflow module run`.
5. **The cloud-batch model is being replaced.** Intelligent Compute on AWS, tiered storage on Azure — the economics of "science per dollar" win out over "cores per dollar."

---

## Caveat

All transcripts are auto-generated English captions, with significant noise — "Vicksville Summit" for "Nextflow Summit," "Seqera" mistranscribed as "Sigara / secura / Sequeira / Securitas," "Heng Li" as "Helen Lee," etc. Speaker names and affiliations are best-effort inferences. Treat names and exact quotes as approximations until confirmed against the recordings on Goldcast.
