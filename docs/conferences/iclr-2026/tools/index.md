# ICLR 2026 — Tools / Methods (filtered)

> **Status:** Template stub. Meeting concluded Apr 27, 2026 (today is May 11, 2026); accepted-paper lists are fully public on OpenReview, camera-ready PDFs are landing rolling, SlidesLive recordings are posting now. **Bulk extraction starts this month.** No entries are populated yet — this page exists to lock the per-tool format and the **scope filter** before extraction begins.

## Scope filter (load-bearing — this is a light build)

ICLR 2026 accepted ~3,700 main-track papers + several hundred more across 40 workshops. We do **not** extract them all. An entry lands in this directory **only if** it satisfies one of:

1. **Workshop filter** — appears in one of the bio / health / drug-discovery / structural-biology workshops at ICLR 2026:
   - **LMRL** — Learning Meaningful Representations of Life
   - **MLGenX** — Machine Learning for Genomics Explorations (3rd edition; "AI Agents and the Biological Lab" theme)
   - **Gen² / Gen2** — Generative AI in Genomics: Barriers and Frontiers
   - **GEM** — Integrating Generative and Experimental Platforms for Biomolecular Design
   - **FM4Science** — Foundation Models for Science (bio subset only; skip pure climate / materials / physics contributions)
2. **Main-track keyword filter** — title or abstract contains any of: *cancer, oncology, tumor, genomics, single-cell, scRNA, spatial transcriptomics, perturbation, CRISPR, drug discovery, molecular property, protein structure, foundation model for biology, electronic health record, clinical NLP, pathology, histology, virtual cell*.
3. **Agentic-AI / LLM-for-science filter** — main-track or workshop paper on LLM agents, tool-use, scientific-reasoning benchmarks, or autonomous experimentation, regardless of explicit bio framing. These reliably adapt to oncology within 6 months and feed the AACR agentic-AI axis.

Everything else — general vision / NLP / RL / theory / optimization / fairness / robotics — is **out of scope** and gets no entry here. Reviewer bandwidth is the binding constraint, not source availability (ICLR's full OpenReview transparency means we could grab everything; we choose not to).

## Per-entry template

Each in-scope paper gets a file (`tools/<paper-slug>.md`) following this structure:

````markdown
# <Method / Tool name>

**One-line description** — what the method does in plain language.

- **Authors:** <first author + lab + institution>
- **Track:** main-track (oral / spotlight / poster) / LMRL / MLGenX / Gen² / GEM / FM4Science
- **OpenReview:** [paper page with public reviews]
- **arXiv / bioRxiv:** [preprint link]
- **Code:** [GitHub link]
- **Pretrained weights:** [HF Hub / Zenodo link if applicable]

## Presentation at ICLR 2026

- **Format:** oral / spotlight / poster / workshop talk
- **Day / session:** Apr 23–25 (main) or Apr 26–27 (workshop)
- **SlidesLive / YouTube:** [link, post-meeting]
- **Review thread sentiment:** brief note on review-thread contention, if notable (ICLR's public reviews are a useful signal)

## What it does

2–3 sentences: the problem it solves, the methodological idea, what it consumes and produces.

## Why it matters for cancer / biology

Explicit statement of the bridge to oncology — even for main-track papers that don't claim cancer relevance. Example: "Multi-modal contrastive objective aligning single-cell RNA with spatial-protein readouts; directly applicable to tumor microenvironment characterization."

## Where it fits in the corpus

- AACR 2026 agentic-AI axis: [link if relevant]
- AACR 2026 virtual-cells axis: [link if relevant]
- **ICML 2026 cousin paper / author overlap:** [link — Jul 2026, same calendar year]
- **NeurIPS 2026 cousin paper / author overlap:** [link — Dec 2026, same calendar year]
- ISMB 2026: [link if benchmarked / cited]
- RECOMB 2026: [link if benchmarked / cited]
- ASCO 2026: [link if clinically translated]

## Notes

Free-form: benchmarks claimed, comparisons to scGPT / Geneformer / UCE / ESM / RFdiffusion / AlphaFold / Boltz / Evo / NT, scaling-law observations, agentic-AI capabilities, regulatory implications, OpenReview review-thread highlights.
````

## Tool index

*Empty — populates from May 2026 onward. Anticipated final count: ~30–50 entries across the five bio workshops + main-track filter hits + agentic-AI subset. Likely slightly larger than ICML 2026's expected ~20–40 because ICLR's bio-workshop footprint is denser (5 workshops vs. ICML's 2–3).*

| Method / Tool | Track | Modality | Authors | Format | OpenReview | Code | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|
| [ESM-3](esm-3.md) | Foundation-model dependency | Protein sequence + structure + function | Hayes et al. (EvolutionaryScale) | *Science* 2025 (not ICLR) | n/a | [evolutionaryscale/esm](https://github.com/evolutionaryscale/esm) | Backbone for Proteina-Complexa, TEA-alphabet, GEM workshop binder pipelines |
| [BioMedCLIP](biomedclip.md) | Foundation-model dependency | Biomedical image-text (CLIP) | Zhang, Xu et al. (Microsoft Research) | *NEJM AI* 2024 (not ICLR) | n/a | [microsoft/BiomedCLIP_data_pipeline](https://github.com/microsoft/BiomedCLIP_data_pipeline) | Default baseline for ICLR 2026 imaging tracks; AACR 2026 pathology axis |
| [Nucleotide Transformer](nucleotide-transformer.md) | Foundation-model dependency | DNA / genomic FM (encoder, MLM, 6-mer; 50M–2.5B params) | Dalla-Torre et al. (InstaDeep + NVIDIA + TU Munich) | *Nature Methods* 2025 (not ICLR) | n/a | [instadeepai/nucleotide-transformer](https://github.com/instadeepai/nucleotide-transformer) | Canonical 2.5B baseline cited across MLGenX / Gen² / FM4Science |
| [DNABERT-2](dnabert-2.md) | Foundation-model dependency | DNA / genomic FM (encoder, MLM, BPE + ALiBi; 117M params) | Zhou et al. (Northwestern MAGICS Lab) | ICLR 2024 poster (not ICLR 2026) | [oMLQB4EZE1](https://openreview.net/forum?id=oMLQB4EZE1) | [MAGICS-LAB/DNABERT_2](https://github.com/MAGICS-LAB/DNABERT_2) | GUE benchmark canonical across MLGenX / Gen² submissions |
| [HyenaDNA](hyenadna.md) | Foundation-model dependency | DNA / genomic FM (causal LM, Hyena operators, single-nt; 1 Mb context) | Nguyen et al. (Stanford Hazy Research + Harvard + Mila) | NeurIPS 2023 poster (not ICLR) | [ubzNoJjOKj](https://openreview.net/forum?id=ubzNoJjOKj) | [HazyResearch/hyena-dna](https://github.com/HazyResearch/hyena-dna) | Hyena lineage → Evo / Evo2 (Sci4DL ICLR 2026) |
| [AlphaGenome](alphagenome.md) | Foundation-model dependency | DNA → multi-modal functional tracks (U-Net + transformer; 1 Mb, ~450M params) | Avsec et al. (Google DeepMind) | *Nature* 2026 (not ICLR) | n/a | [google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome) | Variant-effect benchmark referenced by Gen² / LMRL clinical-genomics submissions |

## Why this format

- **Track field** — ICLR runs 40 workshops + a sprawling main track; this field disambiguates where a result lived without polluting the page body. Bio-workshop names are short enough to use as plain track labels.
- **"Why it matters for cancer / biology" is mandatory** — most ICLR work is not explicitly oncology, but the only reason it's in this vault is the cancer downstream. Forcing this field keeps the filter honest.
- **Review thread sentiment** — ICLR-specific. OpenReview review threads are public and a useful signal for which method claims hold up under scrutiny vs. which got accepted on novelty alone. Optional but encouraged.
- **ICML + NeurIPS cousin fields** — load-bearing cross-links. ICLR (Apr), ICML (Jul), NeurIPS (Dec) split the same author community across three cycles per calendar year; tracking the overlap prevents duplicated tool entries and surfaces the full-year method-evolution arc.
- **Pretrained weights row** — ICLR bio papers very reliably ship HF Hub / Zenodo weights (OpenReview reviewer pressure for reproducibility is the highest of the big-three); tracking these is the difference between a paper entry and a usable tool entry.
- **Cross-vault links to AACR axes** — the load-bearing purpose: an ICLR April result should be one click from the AACR April session (same month, by the way) where it gets demonstrated on a tumor dataset.

## Open questions

1. **Workshop-only papers without code or weights** — keep as entries anyway, or defer to "main proceedings only"? *Tentative: keep; MLGenX and GEM workshop papers often pre-stage code releases.*
2. **Agentic-AI subset granularity** — every LLM-agent paper, or only those with a science / bio benchmark? *Tentative: only those with a science / tool-use / SWE-bench-class benchmark; pure dialog-agent work is out. MLGenX BRChallenge submissions are auto-include.*
3. **Consolidating ICLR + ICML + NeurIPS cousin papers** — one entry or three when the same lab ships an evolved version twice in the same year? *Tentative: separate entries per venue with explicit version / delta notes; the full-year arc across three venues is informative.*
4. **OpenReview review-thread mining** — how much sentiment / contention signal to extract per entry? *Tentative: one sentence on contention only if the review thread is unusually divided (e.g., reject → accept after rebuttal, or strong-accept oral with a vocal dissent).*
