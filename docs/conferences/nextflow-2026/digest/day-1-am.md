# Day 1 AM — Keynote, AI rewrites, Nextflow 26.04

**Date:** 2026-04-30 (morning)
**Source transcript:** [`2026-04-30-nextflow-summit-day-1-am`](../sessions/2026-04-30-nextflow-summit-day-1-am.md)

The opening session framed Nextflow as the substrate for "AI-era science": agentic pipeline authoring, machine-readable modules, and a closed-loop optimization layer above the workflow engine. Anchored by Evan Floden's keynote, then a string of practitioner talks that show what AI-driven pipeline development actually looks like in 2026.

---

## 1. Opening keynote — *The AI era of science*
**Evan Floden** (CEO/co-founder, Seqera)

State-of-the-union framed around three pillars: **Context** (data + lineage), **Execution** (compute), **Co-Scientist** (agents). Opens with a tribute to Craig Venter. Announces a long slate of platform features and positions Nextflow as the integration layer for agent-driven, closed-loop science.

**What was launched:**

- **Benchling AI ↔ Seqera MCP** — launch RNA-seq runs from a Benchling chat
- **Data lineage** as a first-class entity, surfaced in the Data Explorer UI
- **In-browser IGV** for BAMs/BEDs/VCFs straight from cloud buckets
- **Studios SSH** — connect via VS Code Remote SSH or Cursor
- **Seqera GxP packages** — validation docs aligned to FDA/EMA, GLP/GCP/GMP
- **IDP-to-Teams mapping** (Okta, Entra), audit logs, fine-grained authz
- **Community module registry** + `nextflow module run` (any module standalone)
- **GPU metrics first-class** (NVIDIA partnership; Sarek GPU acceleration)
- **Seqera Intelligent Compute** — new scheduler replacing the AWS Batch model: spot optimization, right-sizing, bin-packing. Live demo: $5/sample → $2/sample.
- **Co-Scientist** — three modes (assist / build / automate), model-agnostic (BYO key)
- **Seqera for Sciences (Launchpad)** — self-serve scientist UI with "Explain failure" debugging
- **Event-driven pipeline chaining** — bucket events trigger downstream pipelines
- **Closed-loop optimization layer** — autonomous hill-climbing across params, tools, even model architectures (RNA-seq quant + model-training pipeline demos)

**Why it matters:** Floden is explicit that the bet is on context + agents + a re-architected scheduler. Modules become agent-callable tools; lineage becomes the audit trail; Intelligent Compute admits AWS Batch was the wrong primitive.

---

## 2. Building a pipeline factory with AI
**Lorena** (clinical-hospital postdoc, Boston → returning to Barcelona)

Personal talk on doing everything (sysadmin / dev / analyst) at a clinical lab. Ran the same pipeline-build task three ways: **Claude Code**, **Grok + skills**, **Seqera AI**. Seqera AI won — 5 min plan / 4 min build — primarily on context, not model quality.

**Key concepts:** Claude Code skills, sub-agents, XML prompting, the Docker registry as agent context, "context is king."

**Why it matters:** The headline lesson is that the pipeline factory is built from skills and registries, not from a smarter model. Also doubles as a job-search announcement.

---

## 3. Rust-QC — AI-driven rewrites of legacy bioinformatics
**Phil Ewels** (co-founder MultiQC; nf-core veteran)

Origin story of **Rust-QC**: a Rust rewrite of the nf-core/rnaseq QC sub-workflow, generated in a Slack experiment with Phil + Seqera AI. Consolidates 16 bioinformatics commands into one tool — file reads drop from ~18× to 1×, disk usage from 2.5 TB to <0.1 TB. Verification target: **nf-test snapshots** (deterministic, byte-comparable). Cited cost: ~$10K in Anthropic API spend.

**The reusable pattern:** *emulate-then-rewrite*. Don't ask AI to invent a novel tool; ask it to reproduce a verifiable target. nf-test snapshot diffs are the agent harness. Phil predicts a "gold rush" of AI-driven legacy rewrites.

**Why it matters:** The first concrete recipe at the summit for getting trustworthy AI-generated tools — and the cost transparency ($10K) is rare and useful.

---

## 4. What's new in Nextflow 26.04
**Paolo Di Tommaso** (co-founder / chief architect, Seqera)

Two themes: **language** and **engine**.

**Language:**
- New Syntax Parser v2 — own grammar, no Groovy dependency
- Stronger static type system
- Typed `params` block, typed channels, typed process inputs/outputs

**Engine:**
- **Nextflow Modules** as first-class registry (evolution of plug-ins)
- `nextflow model` CLI — search / view / run / create / publish
- Semantic search over modules
- Wave-built containers on the fly
- **Intelligent Compute** in preview on AWS — comparison shown: 230 vs ~280 CPU-h, $15 vs $34

**Why it matters:** Modules — not Docker containers — are pitched as the right packaging primitive, and the typed-everything direction makes pipelines machine-readable for agents.

---

## 5. Nextflow for proactive vaccinology
**Suriya Ghose** (Imperial College London; Kelly / Barclay group)

Building **`prodvac-seq`** for *proactive* (rather than reactive) pandemic preparedness. Replaces single-virus reporter assays with multiplexed barcoded pseudovirus NGS panels (Jesse Bloom-lab paradigm). Pipeline does barcode counting → neutralization curves / IC50 → deep mutational scanning across COVID and flu variants. Validated against Bloom-lab data; collaborators at Cambridge and the Crick.

**Why it matters:** A subfield going NGS-native. The reporter-assay → barcoded-pseudovirus shift is the kind of methodological pivot Nextflow is well-positioned to standardize.

---

## 6. MGTree — microbial genotyping with Nextflow
**Scott Norton** (Senior Bioinformatics Scientist, Merck, Cambridge MA)

**MGTree** does viral genotyping (norovirus, HPV) where Kraken2's k-mer approach fails on closely-related references. Pipeline: Bowtie2 with `-a` (all alignments) → custom dynamic alignment-score filter → reads placed on a Muscle-aligned phylogenetic tree → custom MultiQC report. Validated against PCR/Sanger; in one case caught a co-infection that Sanger missed.

**Caveat:** Doesn't handle recombination.

**Why it matters:** A clean example of where the off-the-shelf tool (Kraken2) is the wrong abstraction, and the Nextflow community's MultiQC tooling makes a custom replacement shippable.

---

## 7. nf-spatial — reproducible Xenium preprocessing
**Lara Ianov** (Co-Director, Biological Data Science Core, UAB)

An nf-core-adjacent pipeline for 10x **Xenium** spatial transcriptomics. Defines a "Tier 1" automated workflow: annotation → multi-stage QC (raw / filtered / normalized / clustered) → cell-shape classification (circular / non-circular / polygonal) as a segmentation-quality proxy → area-based normalization → PCA + spatial clustering with parameter sweeps → consolidated R / RDS outputs and report (UMAP videos, violin plots).

**Out of scope:** Segmentation (use nf-core/spatialvi), cell-type label transfer (bias concerns), CosMx.

**Runtime:** 300–500-panel Xenium = ~day for dozens of samples; 5K panel is much heavier.

**Why it matters:** Core-facility scaling problem solved by treating spatial preprocessing as a standardized pipeline rather than per-project R notebooks.

---

## Cross-cutting threads

- **Context > model** — repeated by Floden, Lorena, and Ewels: skills, lineage, and registries matter more than the LLM choice.
- **Modules as the packaging primitive** — registry, semantic search, agent-callable; pitched as the layer above containers.
- **Verification harnesses for AI rewrites** — nf-test snapshots are Phil's "zero-pass referral" rule.
- **Cloud-scheduler reform** — Intelligent Compute openly replacing the HPC-mimicking Batch model.
- **nf-core as default sharing channel** — every academic and industry talk in this session targeted it.

See [Themes & takeaways](../themes.md) for cross-day synthesis.
