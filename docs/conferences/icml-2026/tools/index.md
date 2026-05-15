# ICML 2026 — Tools / Methods (filtered)

> **Status:** Template stub. Meeting is ~2 months out (Jul 6–11, 2026, Seoul); main-track accepted-paper list expected to drop on OpenReview around the workshop final-notification window (May 15, 2026) through camera-ready in June. Workshop accepted-paper lists land May–Jun. No entries are populated yet — this page exists to lock the per-tool format and the **scope filter** before extraction begins.

## Scope filter (load-bearing — this is a light build)

ICML 2026 accepts ~2,000 main-track papers + thousands more across workshops. We do **not** extract them all. An entry lands in this directory **only if** it satisfies one of:

1. **Workshop filter** — appears in one of the bio / health / drug-discovery / structural-biology workshops at ICML 2026:
   - **FM4LS / ML4LMS** — Multi-modal Foundation Models and LLMs for Life Sciences
   - **GenBio** — Generative AI for Biology (3rd edition anticipated)
   - **AI4Science** — AI for Science (bio / chem subset only; skip physics-only and materials-only contributions)
   - **FM4Health** — Foundation Models for Health (anticipated 2026 entrant)
   - **LCFM** — Long-Context Foundation Models (genomic-LM subset only; skip generic long-context theory)
2. **Main-track keyword filter** — title or abstract contains any of: *cancer, oncology, tumor, genomics, single-cell, scRNA, spatial transcriptomics, perturbation, CRISPR, drug discovery, molecular property, protein structure, foundation model for biology, electronic health record, clinical NLP, pathology, histology, virtual cell*.
3. **Agentic-AI / LLM-for-science filter** — main-track or workshop paper on LLM agents, tool-use, scientific-reasoning benchmarks, or autonomous experimentation, regardless of explicit bio framing. These reliably adapt to oncology within 6 months and feed the AACR agentic-AI axis.

Everything else — general vision / NLP / RL / theory / optimization / fairness / robotics — is **out of scope** and gets no entry here. Reviewer bandwidth is the binding constraint, not source availability.

## Per-entry template

Each in-scope paper gets a file (`tools/<paper-slug>.md`) following this structure:

````markdown
# <Method / Tool name>

**One-line description** — what the method does in plain language.

- **Authors:** <first author + lab + institution>
- **Track:** main-track / FM4LS / GenBio / AI4Science / FM4Health / LCFM
- **OpenReview:** [paper page]
- **PMLR proceedings:** [final paper link, once camera-ready posts]
- **arXiv / bioRxiv:** [preprint link]
- **Code:** [GitHub link]
- **Pretrained weights:** [HF Hub / Zenodo link if applicable]

## Presentation at ICML 2026

- **Format:** oral / spotlight / poster / workshop talk
- **Day / session:** Jul 7–9 (main) or Jul 10–11 (workshop)
- **SlidesLive / YouTube:** [link, post-meeting]

## What it does

2–3 sentences: the problem it solves, the methodological idea, what it consumes and produces.

## Why it matters for cancer / biology

Explicit statement of the bridge to oncology — even for main-track papers that don't claim cancer relevance. Example: "Equivariant diffusion model for protein–ligand co-design; directly applicable to target-engagement prediction in oncology drug discovery."

## Where it fits in the corpus

- AACR 2026 agentic-AI axis: [link if relevant]
- AACR 2026 virtual-cells axis: [link if relevant]
- **NeurIPS 2026 cousin paper / author overlap:** [link — ICML / NeurIPS author overlap is the rule]
- ISMB 2026: [link if benchmarked / cited]
- RECOMB 2026: [link if benchmarked / cited]
- ASCO 2026: [link if clinically translated]

## Notes

Free-form: benchmarks claimed, comparisons to scGPT / Geneformer / ESM / RFdiffusion / AlphaFold / Boltz / Evo / NT, scaling-law observations, agentic-AI capabilities, regulatory implications.
````

## Tool index

*Empty — populates from late May 2026 (workshop final-notification window) onward. Anticipated final count: ~20–40 entries across the bio workshops + main-track filter hits + agentic-AI subset. Smaller than NeurIPS 2026 expected total because ICML's bio-workshop footprint is narrower (2–3 recurring bio workshops vs. NeurIPS's 5–6).*

| Method / Tool | Track | Modality | Authors | Format | OpenReview | Code | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|

## Why this format

- **Track field** — ICML hosts ~10 workshops and a sprawling main track; this field disambiguates where a result lived without polluting the page body.
- **"Why it matters for cancer / biology" is mandatory** — most ICML work is not explicitly oncology, but the only reason it's in this vault is the cancer downstream. Forcing this field keeps the filter honest.
- **NeurIPS cousin field** — the load-bearing cross-link. ICML (July) and NeurIPS (December) split the same author community across two cycles per calendar year; tracking the overlap prevents duplicated tool entries and surfaces method-evolution arcs.
- **Pretrained weights row** — ICML bio papers increasingly ship HF Hub / Zenodo weights; tracking these is the difference between a paper entry and a usable tool entry.
- **Cross-vault links to AACR axes** — the load-bearing purpose: an ICML July result should be one click from the AACR April session where it gets demonstrated on a tumor dataset (the following spring).

## Open questions

1. **Workshop-only papers without code or weights** — keep as entries anyway, or defer to "main proceedings only"? *Tentative: keep; workshop ideas often pre-stage code releases.*
2. **Agentic-AI subset granularity** — every LLM-agent paper, or only those with a science / bio benchmark? *Tentative: only those with a science / tool-use / SWE-bench-class benchmark; pure dialog-agent work is out.*
3. **Consolidating ICML + NeurIPS cousin papers** — one entry or two when the same lab ships an evolved version six months later? *Tentative: two entries, with explicit version / delta notes; the half-year arc is informative.*
