# ICLR 2026 — Program Notes (post-meeting prep)

> Internal working file. Today is **May 11, 2026** — the meeting concluded Apr 27, 2026 (~2 weeks ago). Accepted-paper lists and the 40-workshop roster are public on OpenReview; camera-ready PDFs and SlidesLive recordings are landing on a rolling basis. **Bulk `tools/` extraction starts this month.** This file holds the scaffolding and filter for the screening pass.

## Verified facts

| Field | Value | Source |
|---|---|---|
| Conference | Fourteenth International Conference on Learning Representations | iclr.cc |
| City | Rio de Janeiro, Brazil | iclr.cc/Conferences/2026 |
| Venue | Riocentro Convention and Event Center | iclr.cc/Conferences/2026 |
| Main conference | Apr 23–25, 2026 | iclr.cc/Conferences/2026/Dates |
| Workshops | Apr 26–27, 2026 | iclr.cc/Conferences/2026/Dates |
| Abstract deadline | Sep 19, 2025 (AoE) — past | Dates |
| Paper deadline | Sep 24, 2025 (AoE) — past | Dates |
| Reviews released | Nov 11, 2025 — past | Dates |
| Discussion period ends | Dec 3, 2025 — past | Dates |
| Decision notification | Jan 25, 2026 (AoE) — past | Dates |
| Workshop accept notification | Feb 28, 2026 — past | Dates |
| Early registration deadline | Mar 14, 2026 — past | Dates |
| Workshops accepted | 40 | blog.iclr.cc/2026/01/13/iclr2026-workshops/ |
| Paper format | 9 pages main + unlimited references/appendix; +1 page for camera-ready | Call for Papers |
| License | CC-BY default via OpenReview; ~90% of accepted papers permissive | OpenReview |

## Sources we will rely on

| Source | Status | Coverage |
|---|---|---|
| [ICLR 2026 home](https://iclr.cc/Conferences/2026) | live | dates, venue, organizers |
| [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates) | live | full date list |
| [ICLR 2026 Workshops blog post](https://blog.iclr.cc/2026/01/13/iclr2026-workshops/) | live | full 40-workshop roster |
| [Virtual workshops page](https://iclr.cc/virtual/2026/events/workshop) | live | per-workshop landing pages |
| [OpenReview ICLR group](https://openreview.net/group?id=ICLR.cc) | live | accepted main-track papers + per-workshop venues + review threads |
| [LMRL workshop](https://www.lmrl.org/) | live | LMRL accept list (recurring across ICLR + NeurIPS) |
| [MLGenX workshop](https://mlgenx.github.io/) | live | MLGenX 3rd-ed accept list + BRChallenge submissions |
| [GEM workshop](https://www.gembio.ai/) | live | GEM accept list |
| [FM4Science workshop](https://fm-science.github.io/) | live | FM4Science accept list (bio subset filter required) |
| [SlidesLive (ICLR)](https://slideslive.com/iclr) | rolling | recorded orals + workshop talks, posting through May–Jun 2026 |
| bioRxiv / arXiv | continuous | preprints, filterable by "to appear at ICLR 2026" / "accepted at ICLR 2026" |
| `#ICLR2026` on Bluesky / Mastodon / X | post-meeting | reaction archives — most useful for Apr 23–28 window |
| Lab blogs (DeepMind, Anthropic, Insitro, Recursion, Genentech prescient design, Isomorphic Labs, Profluent, Cradle, Latent Labs, NVIDIA BioNeMo, Arc Institute) | rolling | preprints + summary posts of ICLR papers from these labs |

## Filter criteria (locked — mirrors `tools/index.md`)

A paper enters this vault only if it matches **one** of three filters. Reproduced here for the screening pass.

### Filter 1 — workshop track

Accept anything in these five bio-themed workshops (verified, 2026 roster):

- **LMRL** — Learning Meaningful Representations of Life (recurring; co-runs at NeurIPS)
- **MLGenX** — Machine Learning for Genomics Explorations (3rd ed.; theme: "From Reasoning to Experimentation: Closing the Loop Between AI Agents and the Biological Lab"; includes BRChallenge agent benchmark)
- **Gen² / Gen2** — Generative AI in Genomics: Barriers and Frontiers (1st ed.; directed evolution, engineering cellular/tissue states)
- **GEM** — Integrating Generative and Experimental Platforms for Biomolecular Design (proteins, ligands, nucleic acids, cells)
- **FM4Science** — Foundation Models for Science (2nd ed.; **bio subset only** — skip pure climate, materials, physics)

### Filter 2 — main-track keyword

Run this regex over titles + abstracts of the ~3,700 accepted main-track papers:

```
(cancer|oncolog|tumor|metasta|carcinom|melanoma|leukemi|lymphoma)
| (genomic|epigenom|transcriptom|proteom|metabolom|methyl)
| (single[- ]cell|scRNA|scATAC|spatial transcriptom|spatial omic)
| (perturbation|CRISPR|knockout|knockdown|sgRNA)
| (drug discover|target ident|molecular property|ADMET|small molecul|biologic|de novo design|generative chemistry)
| (protein structur|protein function|protein language|equivariant|RFdiffusion|AlphaFold|Boltz|ESM)
| (foundation model.*(biolog|cell|genom|tissue|pathol|clinical|medical))
| (electronic health record|EHR|clinical NLP|medical imaging|pathology|histolog|radiolog|diagnos)
| (virtual cell|cell atlas|cellular state)
```

### Filter 3 — agentic-AI / LLM-for-science subset

Independent of bio framing, accept any main-track or workshop paper on:

- LLM agents with tool-use, code-execution, or experiment-design loops
- Scientific-reasoning benchmarks (SWE-bench-class, sci-agent-class, lab-task benchmarks, MLGenX BRChallenge)
- Autonomous research / hypothesis-generation systems
- Multi-agent scientific workflows

Rationale: these adapt to oncology within ~6 months (the empirical pattern from 2024 → AACR 2025 and 2025 → AACR 2026) and feed the AACR agentic-AI axis directly. The MLGenX 2026 theme explicitly centers this pattern.

## Expected paper themes (5 anchors)

Post-meeting predictions, to be reconciled against the actual extraction in May–Jun. These are the buckets we expect `tools/` entries to cluster into.

### Theme 1 — Representation learning for biology: next-generation virtual-cell embeddings

scGPT, Geneformer, and UCE are 2022–2024 vintage. ICLR 2026's LMRL workshop is positioned as the "virtual cells" venue, with explicit framing around in silico representations of cell behaviour in health and disease. Expect next-gen contributions: cross-modal (DNA + RNA + protein + spatial + clinical), multi-million-cell training corpora, instruction-tuned for downstream tasks (perturbation prediction, virtual-screen rerank), and benchmarked on virtual-cell tasks rather than embedding-quality proxies. Workshop home: **LMRL**, with main-track spillover. Expect heavy overlap with the NeurIPS 2026 LMRL roster eight months later.

### Theme 2 — Agentic AI for biological labs (MLGenX flagship theme)

The MLGenX 3rd-ed workshop theme is explicitly "AI Agents and the Biological Lab" — adaptive, interpretable, experiment-aware AI systems that learn from feedback and drive biological insight. The inaugural **BRChallenge** benchmarks biological AI agents on sequence design, perturbation reasoning, and multimodal evidence synthesis for target identification. Expect a wave of tumor-board agents, trial-matching agents, multi-omics interpretation agents, and oncology-specific tool-use systems. Workshop home: **MLGenX**, main-track agentic-AI spillover, **FM4Science** bio subset.

### Theme 3 — Generative AI for genomics and cellular state engineering

The Gen² workshop is a new entrant framed around "engineering cellular and tissue states" as the next frontier after directed protein evolution. Expect diffusion / flow-matching models conditioned on cell-state targets, programmable perturbation generation, sequence-design models for synthetic regulatory elements, and generative single-cell models for in silico hypothesis generation. Workshop home: **Gen²**; spillover into LMRL and MLGenX. Direct relevance to AACR's virtual-cells axis.

### Theme 4 — Generative biomolecular design: proteins, antibodies, ligands, nucleic acids

GEM is the established venue for de novo small-molecule generation conditioned on oncology targets, antibody / TCR / peptide design, equivariant diffusion for protein–ligand co-design, RFdiffusion descendants, Boltz / AlphaFold3-class structure models, and flow-matching for molecular design. ICLR 2026 GEM has explicit framing around bridging computational and experimental biology — expect benchmark contributions tied to wet-lab assays. Workshop home: **GEM**; main-track for the headline architectural releases.

### Theme 5 — Multimodal medical-imaging and clinical-language foundation models

Less workshop-anchored at ICLR 2026 (no dedicated medical-imaging workshop ran), but FM4Science and main-track keyword hits should surface contributions on whole-slide pathology FMs, radiology-report co-trained models, EHR-trajectory LMs, and clinical-NLP foundation models. The "Foundation Models for Science: Real-World Impact and Science-First Design" framing aligns directly with this. Workshop home: **FM4Science** bio subset + main-track filter hits.

## Post-meeting timeline (action items)

| Date | Action |
|---|---|
| **Now → mid-May 2026** | run keyword regex over OpenReview main-track accept list (~3,700 papers); build candidate list of ~50–80 main-track hits |
| Mid-May 2026 | pull accept lists from LMRL / MLGenX / Gen² / GEM / FM4Science OpenReview venues; merge with main-track hits; expected ~150 raw candidates |
| Late May 2026 | de-duplicate (papers often live in workshop AND main-track), apply Filter 3 (agentic-AI), drop out-of-scope FM4Science contributions (climate / materials / physics); target final ~30–50 entries |
| Jun 2026 | bulk `tools/` population from camera-ready PDFs + SlidesLive recordings; pull bioRxiv mirrors; tag each entry with AACR cross-link |
| **Jul 6–11, 2026** | ICML 2026 — identify cousin papers from same labs; cross-link ICLR entries to ICML cousins |
| **Dec 6–13, 2026** | NeurIPS 2026 — same cousin-paper pass; complete the full-year ML-for-biology arc |

## Caveats

- **40-workshop roster, only 5 in-scope.** Confirm-positive on the workshop filter is straightforward; the risk is missing a non-bio workshop that hosts a sneaky bio contribution (e.g., a representation-learning theory workshop that admits a scGPT-class paper). The main-track keyword filter is the safety net.
- **OpenReview review-thread mining is optional, not load-bearing.** Resist the urge to scrape every review thread for sentiment; one sentence per entry only when contention is unusual.
- **ICLR + ICML + NeurIPS author overlap is the rule, not the exception.** Tool-entry consolidation policy is in `tools/index.md` open question 3: separate entries per venue with explicit delta notes. The full-year arc is the value-add.
- **Agentic-AI scope creep risk.** Filter 3 is broader than Filters 1–2 by design, but it can swell if applied loosely. Keep the "science / tool-use benchmark required" caveat enforced. MLGenX BRChallenge submissions are auto-include.
- **Rio venue logistics.** No bearing on the vault. Post-meeting social-reaction harvesting is BRT-timezone (UTC−3); roughly aligns with North American working hours.
- **~90% CC-BY license rate.** A small minority of accepted ICLR 2026 papers retain restrictive licenses; check each before quoting at length. PDFs themselves are always public-readable via OpenReview.
