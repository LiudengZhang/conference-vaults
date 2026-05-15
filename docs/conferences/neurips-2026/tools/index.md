# NeurIPS 2026 — Tools / Methods (filtered)

> **Status:** Template stub. Meeting is ~7 months out; main-track accepted-paper list lands Sep 24, 2026; workshop accepted-paper lists land Oct–Nov 2026. No entries are populated yet — this page exists to lock the per-tool format and the **scope filter** before extraction begins.

## Scope filter (load-bearing — this is a light build)

NeurIPS 2026 accepts ~2,000 main-track papers + thousands more across workshops. We do **not** extract them all. An entry lands in this directory **only if** it satisfies one of:

1. **Workshop filter** — appears in one of the bio / health / drug-discovery / structural-biology workshops:
   - **MLSB** — Machine Learning in Structural Biology
   - **AI4NewDrugs / AI4D3** — AI for New Drug Modalities / AI for Drug Discovery
   - **LMRL** — Learning Meaningful Representations of Life
   - **GenAI4Health** — Generative AI for Health
   - **AIM-FM** — Advancements In Medical Foundation Models
   - **AI4Science** — AI for Science (only the bio / chem subset; skip physics-only and materials-only contributions)
2. **Main-track keyword filter** — title or abstract contains any of: *cancer, oncology, tumor, genomics, single-cell, scRNA, spatial transcriptomics, perturbation, CRISPR, drug discovery, molecular property, protein structure, foundation model for biology, electronic health record, clinical NLP, pathology, histology, virtual cell*.
3. **Agentic-AI / LLM-for-science filter** — main-track or workshop paper on LLM agents, tool-use, scientific-reasoning benchmarks, or autonomous experimentation, regardless of explicit bio framing. These reliably adapt to oncology within 6 months and feed the AACR agentic-AI axis.

Everything else — general vision / NLP / RL / theory / optimization / fairness / robotics — is **out of scope** and gets no entry here. Reviewer bandwidth is the binding constraint, not source availability.

## Per-entry template

Each in-scope paper gets a file (`tools/<paper-slug>.md`) following this structure:

````markdown
# <Method / Tool name>

**One-line description** — what the method does in plain language.

- **Authors:** <first author + lab + institution>
- **Track:** main-track / MLSB / LMRL / AI4D3 / GenAI4Health / AIM-FM / AI4Science
- **OpenReview:** [paper page]
- **arXiv / bioRxiv:** [preprint link]
- **Code:** [GitHub link]
- **Pretrained weights:** [HF Hub / Zenodo link if applicable]
- **Satellite hub:** Sydney / Atlanta / Paris (if presentation is hub-specific)

## Presentation at NeurIPS 2026

- **Format:** oral / spotlight / poster / workshop talk
- **Day / session:** ...
- **SlidesLive / YouTube:** [link, post-meeting]

## What it does

2–3 sentences: the problem it solves, the methodological idea, what it consumes and produces.

## Why it matters for cancer / biology

Explicit statement of the bridge to oncology — even for main-track papers that don't claim cancer relevance. Example: "Equivariant GNN for protein–ligand binding affinity; directly applicable to target-engagement prediction in oncology drug discovery."

## Where it fits in the corpus

- AACR 2026 agentic-AI axis: [link if relevant]
- AACR 2026 virtual-cells axis: [link if relevant]
- ISMB 2026: [link if benchmarked / cited]
- RECOMB 2026: [link if benchmarked / cited]
- ASCO 2026: [link if clinically translated]

## Notes

Free-form: benchmarks claimed, comparisons to scGPT / Geneformer / ESM / RFdiffusion / AlphaFold / Boltz / Evo / NT, scaling-law observations, agentic-AI capabilities, regulatory implications.
````

## Tool index

*Empty — populates from Sep 29, 2026 (workshop roster) onward. Anticipated final count: ~30–60 entries across the five bio workshops + main-track filter hits + agentic-AI subset.*

| Method / Tool | Track | Modality | Authors | Format | OpenReview | Code | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|

## Why this format

- **Track + satellite-hub fields** — NeurIPS spans three cities and a dozen+ venues per year; these two fields disambiguate where a result lived without polluting the page body.
- **"Why it matters for cancer / biology" is mandatory** — most NeurIPS work is not explicitly oncology, but the only reason it's in this vault is the cancer downstream. Forcing this field keeps the filter honest.
- **Pretrained weights row** — NeurIPS bio papers increasingly ship HF Hub / Zenodo weights; tracking these is the difference between a paper entry and a usable tool entry.
- **Cross-vault links to AACR axes** — the load-bearing purpose: a NeurIPS December result should be one click from the AACR April session where it gets demonstrated on a tumor dataset.

## Open questions

1. **Workshop-only papers without code or weights** — keep as entries anyway, or defer to "main proceedings only"? *Tentative: keep; workshop ideas often pre-stage code releases.*
2. **Agentic-AI subset granularity** — every LLM-agent paper, or only those with a science / bio benchmark? *Tentative: only those with a science / tool-use / SWE-bench-class benchmark; pure dialog-agent work is out.*
3. **Satellite-hub overlap** — if the same paper is presented at two hubs, one entry or two? *Tentative: one entry, both hubs noted.*
