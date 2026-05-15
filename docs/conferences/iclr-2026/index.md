# ICLR 2026

**Fourteenth International Conference on Learning Representations** — Riocentro Convention and Event Center, **Rio de Janeiro, Brazil**, **April 23–27, 2026** (main conference Apr 23–25; workshops Apr 26–27).

> **Status:** Scaffold — meeting concluded ~2 weeks ago (today is May 11, 2026). Accepted-paper list and workshop rosters are public on OpenReview; SlidesLive recordings and camera-ready PDFs are rolling out now. This is a **light build**, not full coverage — see "Scope" below. Bulk `tools/` extraction starts this month.

## Why this is in the vault

ICLR is the third of the "big three" general-purpose ML conferences (alongside NeurIPS and ICML) and is the canonical venue for **representation learning** — the methodological substrate underneath every foundation model that later gets adapted to cancer biology. Like NeurIPS and ICML, the overwhelming majority of its program is general-purpose ML with no direct oncology relevance, so we are **not** trying to cover it like ISMB or EuroBioC. ICLR lives in this vault for the same reason its siblings do: it is an upstream methods source for the AACR vault's **agentic-AI** and **virtual-cells / foundation-model** axes.

Three reasons to keep a scoped presence:

- **Representation learning is the bottleneck for virtual cells.** scGPT, Geneformer, UCE, and the next-generation cross-modal cell models all are *representation-learning* contributions before they are biology contributions; ICLR is where their methodological cousins (contrastive objectives, masked modeling regimes, equivariant architectures, multimodal alignment) first land.
- **Bio-FM cross-pollination is heavier than at NeurIPS / ICML.** ICLR 2025 hosted MLGenX and GEM; ICLR 2026 hosts four bio-themed workshops (LMRL, MLGenX 3rd ed., Gen², GEM) — a denser bio footprint than ICML's. Many authors and tools overlap directly with the NeurIPS LMRL / MLSB and ICML FM4LS / GenBio circuits.
- **Agentic AI for science.** ICLR 2026 features explicit MLGenX framing of "AI Agents and the Biological Lab" plus a Foundation Models for Science workshop; the same ~6-month adapt-to-oncology pattern applies — an ICLR April result tends to surface as a TissueAgent / OncoAgent-class demo at SITC, ASH, or AACR within the same calendar year.

## Scope (what this vault covers — and what it does not)

**In scope (light build):**

- The recurring **bio / health / drug-discovery / structural-biology workshops** at ICLR 2026 (see roster below).
- Main-track papers that match a **cancer / genomics / single-cell / spatial / drug-discovery / clinical-NLP keyword filter** (anticipate a few dozen out of ~3,700 main-track papers).
- The **agentic-AI / LLM-for-science** subset of the main track, regardless of explicit bio framing.

**Out of scope:**

- General-purpose ML methods papers (vision-only, NLP-only, RL-only, theory, optimization, fairness, robotics, etc.) with no plausible bio downstream — the >95% bulk.
- The full ~3,700-paper main proceedings; bulk extraction is explicitly **not** planned.
- Tutorials, expo events, and socials outside the bio / health niches.

## Bio / health-relevant workshops (verified, 2026 roster)

ICLR 2026 accepted 40 workshops; four are directly bio-themed plus a fifth science-FM workshop with a substantial bio subset. Workshop dates are **Apr 26–27, 2026** at Riocentro.

| Workshop | Theme | Canonical short name | Edition |
|---|---|---|---|
| Learning Meaningful Representations of Life | foundation models for genomics, single-cell, spatial; virtual cells as the headline framing | **LMRL** | recurring (ICLR + NeurIPS) |
| Machine Learning for Genomics Explorations | "From Reasoning to Experimentation: Closing the Loop Between AI Agents and the Biological Lab" — target ID, perturbation reasoning, BRChallenge agent benchmark | **MLGenX** | 3rd edition |
| Generative AI in Genomics: Barriers and Frontiers | directed evolution in protein science; engineering cellular and tissue states | **Gen² / Gen2** | 1st edition |
| Integrating Generative and Experimental Platforms for Biomolecular Design | proteins, ligands, nucleic acids, cells; bridging computational and experimental biology | **GEM** | recurring |
| Foundation Models for Science: Real-World Impact and Science-First Design | problem-driven FMs for climate, materials, biology — bio subset only is in scope | **FM4Science** | 2nd edition |

This is a denser bio footprint than ICML 2026's (2–3 bio workshops) and comparable to NeurIPS 2026's expected 5–6 bio workshops — partly because OpenReview's transparent acceptance lifecycle gives ICLR a small advantage for bio-FM submissions that prefer public review.

## OpenReview advantage — bulk extraction is easier here

ICLR's review process is fully public on OpenReview from submission through camera-ready: every accepted paper has a public review thread, author-reviewer discussion, and (for ~90% of papers) a permissive license on the PDF itself. This makes ICLR **the easiest of the big-three to bulk-extract**, compared to CVPR (camera-ready only) or NeurIPS (OpenReview-public but with later workshop posting cadence). Practical implications:

- Accepted-paper list for ICLR 2026 was public from Jan 25, 2026 (notifications) onward; full camera-ready PDFs are public now.
- Each workshop runs its own OpenReview venue with accepted papers posted ahead of the meeting (Mar–Apr 2026) — most are already public.
- Author–reviewer review threads are scrapable for sentiment / contention signals.
- bioRxiv mirrors exist for the majority of bio-themed contributions; the lag is typically 1–4 weeks behind OpenReview.

## What we have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Main proceedings** | ~3,700 accepted papers | OpenReview group `ICLR.cc/2026/Conference`; all camera-ready PDFs are public. CC-BY for ~90% of submissions. |
| **Workshop pages** | one OpenReview venue per workshop | All 40 workshops have their accept lists public; bio-themed five already finalized. |
| **bioRxiv mirrors** | most bio-relevant ICLR papers have a preprint | Filter bioRxiv for "ICLR 2026" mentions; lag of 1–4 weeks behind OpenReview. |
| **SlidesLive + YouTube** | recorded talks | ICLR records orals + most workshop talks; posts rolling, typically within 1–3 weeks of the meeting. Most are landing on SlidesLive now. |
| **Twitter/Bluesky/Mastodon** | post-meeting reactions | `#ICLR2026`; useful for catching which agentic-AI / FM-bio papers got traction. |
| **Cross-link with NeurIPS / ICML** | author + tool overlap | Many ICLR bio papers reappear at ICML (Jul) or NeurIPS (Dec) within the same year — single tool entry should consolidate or explicitly cross-link. |

## Organization

```
conferences/iclr-2026/
├── index.md             # this page
├── program-notes.md     # post-meeting prep — verified facts, filter criteria, expected themes
└── tools/               # per-paper / per-tool entries, populated from May 2026 onward
    └── index.md         # template + scope-filter note
```

No `digest/`, no `themes.md`, no `keynotes/`. The light-build pattern mirrors ICML 2026 and NeurIPS 2026: only `tools/` gets populated, and only with the filtered subset.

## What's different from full-conference vaults

Compared to ISMB 2026, RECOMB 2026, AACR 2026, ASCO 2026, or EuroBioC 2025 — which aim at near-complete program coverage — ICLR 2026 is **scope-limited by design**:

- No per-session digests, no per-day digests, no themes synthesis. The general-purpose ML bulk is irrelevant.
- No keynote / plenary coverage unless the speaker is a known bio-FM author.
- Tool entries are filtered down to a few dozen, not exhaustive. The filter is keyed on the AACR axes, not on ICLR's own taxonomy.
- Most ICLR 2026 tool entries should explicitly cross-link to an ICML 2026 (Jul) or NeurIPS 2026 (Dec) cousin paper — author and method overlap is the rule, not the exception across the big-three ML venues within a calendar year.

## Key dates

| Date | Event |
|---|---|
| Sep 19, 2025 | Abstract submission deadline (AoE) — past |
| Sep 24, 2025 | Paper submission deadline (AoE) — past |
| Nov 11, 2025 | Reviews released — past |
| Dec 3, 2025 | Discussion period ends — past |
| Jan 25, 2026 | Decision notification (AoE) — past |
| Feb 28, 2026 | Workshop acceptance notification — past |
| Mar 14, 2026 | Early registration deadline — past |
| Apr 2, 2026 | Registration cancellation deadline — past |
| **Apr 23–25, 2026** | **Main conference** (Riocentro, Rio de Janeiro) — past |
| **Apr 26–27, 2026** | **Workshops** — past |
| May 2026 → ongoing | SlidesLive recordings + camera-ready PDFs posting |

## Sources

- [ICLR 2026 home](https://iclr.cc/Conferences/2026)
- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)
- [ICLR 2026 Workshops blog post](https://blog.iclr.cc/2026/01/13/iclr2026-workshops/)
- [ICLR 2026 virtual workshops](https://iclr.cc/virtual/2026/events/workshop)
- [OpenReview ICLR group](https://openreview.net/group?id=ICLR.cc)
- [LMRL workshop (recurring)](https://www.lmrl.org/)
- [MLGenX workshop (3rd ed.)](https://mlgenx.github.io/)
- [GEM workshop](https://www.gembio.ai/)
- [FM4Science (2nd ed.)](https://fm-science.github.io/)

## Next step

- **May 2026:** run the keyword filter against the public main-track accept list; identify the ~few-dozen bio-relevant papers; cross-check against the five bio workshop rosters.
- **May–Jun 2026:** populate `tools/` with the filtered subset; pull bioRxiv mirrors and SlidesLive recordings as they post; tag each entry with its cross-link to AACR 2026 agentic-AI or virtual-cells axes.
- **Jul 2026 (ICML overlap):** cross-link ICLR 2026 bio tools to their ICML 2026 cousins where the same lab ships an evolved version.
- **Dec 2026 (NeurIPS overlap):** repeat for NeurIPS LMRL / MLSB / AI4D3 cousin papers; consolidate the full-year ML-for-biology arc across the big-three venues.
