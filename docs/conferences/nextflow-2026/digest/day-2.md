# Day 2 — Community, multi-agent demos, enterprise stacks, AI panel

**Date:** 2026-05-01
**Source transcript:** [`2026-05-01-nextflow-summit-day-2`](../sessions/2026-05-01-nextflow-summit-day-2.md)

Day 2 was lower-key on product launches and heavier on community structure (training, ambassadors, hackathons), enterprise architecture (Pfizer iFox on Lamin, Microsoft Foundry agent demo, Azure storage tiering), and a closing panel on what AI is doing to the bioinformatician role.

---

## 1. Community training update
**Geraldine "GiGi"** (Seqera Community team)

The Nextflow training portal: free, Creative Commons, GitHub-Codespaces-based, available in **11 languages**. Two tracks:

- **Newcomers:** Hello Nextflow, Nextflow Run
- **Experienced:** nf-core training + advanced "side quests"

Heavy use of **Claude (Anthropic) skills** to update code snippets across courses. Phil's AI-driven translation harness diffs changed sections and re-translates only those — fixes are made in the **prompt, not the file**, so style and pronoun choices propagate to all 11 languages on the next run. Inspired by FastAPI docs community.

Upcoming: Nextflow Training Week (~2 weeks out).

---

## 2. Nextflow Ambassador Program
**Marcel Ribeiro-Dantas** (Seqera Community team)

History and stats: started late 2023, grew from 5 → **143 ambassadors**, 16 → **40 countries**, ~700 activities in 2.5 years. Rolling six-month cohorts (Jan / July intake). Incentives: travel/swag/event funding, early access to Seqera releases (Seqera AI, VS Code extension), private channel.

**Top 10 Certificates of Excellence** — James, Julia, Matias, Jose, Firas, Evangelos, Maxim, Cubra, Antoine, plus Fides (Tunisia).

**Hybrid Hackathon (March):** ~70% of local sites hosted by ambassadors.

**Why it matters:** The deliberate non-monetary recognition model is the program's stated load-bearing design choice (keeps it non-competitive).

---

## 3. *(Skipped)* — Vipava (Grail) cancelled live; recorded talk to be posted on YouTube.

---

## 4. Downstream RNA-seq analysis pipeline
**Reema** (Northeastern University; work begun at Novo Nordisk)

Custom DSL2 pipeline that *starts* from the count matrices that nf-core/rnaseq emits.

**Sub-workflows:** gene filtering → optional **ComBat-seq** batch correction → **DESeq2** *or* **limma-voom** differential expression → optional **FGSEA / MSigDB** pathway analysis. Plus **RNASeqPower** for power analysis, YAML-driven config, optional API ingestion of metadata/counts.

**Live ecosystem moment:** Q&A surfaced overlap with **nf-core/differentialabundance** (already has a built-in Shiny app) — maintainers publicly invited her to merge efforts.

---

## 5. Hackathon recap
**Marcel** (returning)

Pitches nf-core hackathons as fun / collaborative / flexible (not competitive). Recap:

- **March hybrid hackathon** — 41 projects, 29 local sites, 600 participants, 19 time zones
- **Boston in-person** — ~30–40 participants

**Highlighted projects:**

- **Topic-channels migration** — ~30–40 PRs converting nf-core modules to the `versions` topic
- **GPU variant callers in nf-core/sarek** (Gary, Joe)
- **nf-core/cellpainting** (Ken)
- **DuckDB integration for Nextflow** — "Eider" h5ad reader (Michael, Edmond, Ben)
- **Harrison's AI-agent project** — Antigravity orchestrating multiple agents to auto-fix ~2,000 modules
- **Single-cell perturbation pipeline** ("Cosmic AI")

A ~30-page "host-your-own hackathon" handbook is now available.

---

## 6. Lightning talks

- **Marcus Sujanski** (MDI Biological Lab, Bar Harbor ME) — `sc-samap`: Nextflow wrapper around the **SAMap** algorithm (Tarashansky / Wang, Stanford) for cross-species single-cell comparison (axolotl, turquoise killifish, zebrafish). Adds homolog detection, cross-species DE, cell-type-to-cell-type mapping.
- **CUNY PhD student** — Two pipelines: Nextflow port of an older Galaxy-based lab pipeline + a downstream analysis pipeline that integrates outputs and produces transcript lists for phylogenetic analysis.
- **Unnamed** — Pipeline for circular / non-canonical-splicing RNA quantification; claims top-tier speed and accuracy vs. CD3 benchmark.

---

## 7. Multi-agent workflows with Microsoft Foundry + Nextflow
**Computational biologist at Microsoft** (book on O'Reilly forthcoming)

Defines models vs. agents vs. multi-agent workflows (sequential, concurrent, group-chat, human-in-the-loop). Pitches **Microsoft Foundry** (announced Nov 2025):

- Governed model deployment (incl. Hugging Face's ~14k models)
- Agent builder, **Foundry IQ** (RAG over your data)
- **Foundry Tools** including a generic MCP connector
- **Foundry Local** — auto-quantizes models to local hardware

**Demo:** workflow with a "bioinformatics evaluator" agent + a "Seqera coding" agent connected to Seqera via **MCP**. Given a BioProject ID, the agents autonomously identified plasmodium RNA-seq, picked an nf-core pipeline, drafted and ran the Nextflow command. Cost note: ~$600 in GPT-4o tokens to run the book examples.

**Why it matters:** The autonomous BioProject demo is the conference's strongest "agents end-to-end" data point. The agent identified one of the speaker's own six-year-old datasets with no domain hints.

---

## 8. Pfizer's iFox — OMICs cross-functions infrastructure
**Joe** (Pfizer, Machine Learning & Computational Sciences in Medicine Design Research Unit)

**iFox** (Infrastructure for OMICs Cross-functions) — joint R&D + IT initiative to unify storage / compute / pipelines across Pfizer research units (oncology, immunology, vaccines, drug safety).

**Stack:**

- **AWS Batch + Seqera Platform** as the backbone
- **Lamin / LaminDB** for data lineage, ontology-aware search, artifact versioning (Pfizer's framing: "*LaminDB is to data as GitHub is to code*")
- Lamin-integrated metadata schema tool (Rebecca White)
- **Seqera Studios** for interactive compute
- **iFox reference-data ingestion pipeline** (Airflow)
- **Evidence** visual analytics platform (built with Austrian partner "David Vision")
- ML model registry + custom genome-manager pipeline
- **Bionty** ontologies

**Why it matters:** A relatively rare enterprise adoption story for Lamin. Recruiting note included.

---

## 9. Optimizing Nextflow cost & performance on Azure
**Azure Storage Engineering** (HPC storage products)

Covers Nextflow's five copy strategies, executor choice (**Azure Batch** vs. **AKS** via Azure CycleCloud), and storage tiering:

- **Azure Blob** (object) for cold/output
- **Azure Managed Lustre** / **Azure NetApp Files** / **Azure Files NFS** for hot working dirs
- Single-namespace tiered storage: POSIX hot tier in front, object cold tier behind

**Networking:** multi-region endpoints to avoid egress; co-locate compute with storage.

**Mindset shift:** optimize "**science per compute budget**" instead of cores/petabytes purchased.

Mentions **Seqera Fusion** as the abstraction layer; Azure MCP server can analyze runs and suggest optimizations.

---

## 10. Closing panel — AI in bioinformatics
**Maria Enrique** (Seqera, agentic AI), **Isha** (Seqera scientific engagement lead), a third panelist with microbiology background, **Evan** moderating.

**Themes discussed:**

- The bioinformatician's role is shifting from hands-on executor to **orchestrator/architect**
- Validating fuzzy biological "ground truth" is the open problem
- IT/governance burden of approving AI tools
- Need for guardrails + human-in-the-loop + sandboxes
- Ownership of AI-generated code (avoiding duplicate solutions)
- **Obsidian + Notion as "second brain"** repositories LLMs can search
- **MCP servers as the integration backbone**

**Closing prediction:** *systems* will beat *models* — long-term winners are agent harnesses with reasoning + domain context + tool/data access, not any single frontier model.

**Plugs:** upcoming Seqera Co-Scientist webinar, virtual Nextflow Summit in October, Boston subterranean hackathon.

---

## Cross-cutting threads

- **AI/agents everywhere** — training maintenance (Claude skills), code generation, autonomous workflow execution, hackathon project automation.
- **MCP as integration substrate** — Seqera, Azure, Foundry connectors all converging on it.
- **Governance + trust** — Lamin lineage, audit logs, human-in-the-loop, sandboxed adoption before enterprise rollout.
- **Cost-aware cloud architecture** — Azure tiered storage, AWS savings plans, GPT-4o token costs all called out explicitly.
- **Community as the moat** — non-competitive hackathons, ambassador recognition, multilingual training.

See [Themes & takeaways](../themes.md) for cross-day synthesis.
