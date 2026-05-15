# ICML 2026

**Forty-Third International Conference on Machine Learning** — COEX Convention & Exhibition Center, **Seoul, South Korea**, **July 6–11, 2026** (Expo/tutorials Jul 6; main conference Jul 7–9; workshops Jul 10–11).

> **Status:** Scaffold — meeting ~2 months out (today is May 11, 2026). Author notifications and the workshop roster are not yet public; main-paper submissions closed Jan 28, 2026 and workshop final notifications are due May 15, 2026. This is a **light build**, not full coverage — see "Scope" below.

## Why this is in the vault

ICML is one of the two largest general-purpose ML venues worldwide (sibling to NeurIPS, comparable ~10,000-attendee scale), and like NeurIPS the overwhelming majority of its program is general-purpose ML with no direct cancer-research relevance. We are **not** trying to cover it like ISMB or EuroBioC. ICML lives in this vault for the same reason NeurIPS does: it is an upstream methods source for the AACR vault's **agentic-AI** and **virtual-cells / foundation-model** axes. ICML and NeurIPS together host most of the canonical method papers (Transformer, diffusion, RLHF, flow matching, equivariant GNN, agentic-LLM scaffolds) that later get adapted to oncology.

Two further reasons to keep a scoped presence:

- **Foundation models for biology cross-pollination.** ICML 2024 and 2025 hosted the *Generative AI for Biology* (GenBio) and *Multi-modal Foundation Models and LLMs for Life Sciences* (FM4LS / ML4LMS-class) workshops, which surface scGPT / Geneformer / ESM / RFdiffusion / Boltz / Evo descendants alongside their NeurIPS LMRL / MLSB cousins. Many authors and tools overlap directly with the NeurIPS bio circuit.
- **Agentic AI for science.** ICML's main track is increasingly the venue for LLM-agent and tool-use papers (alongside NeurIPS); the same 6-month adapt-to-oncology pattern applies — an ICML July result tends to surface as a TissueAgent / OncoAgent-class demo at SITC or ASH in the same calendar year.

## Scope (what this vault covers — and what it does not)

**In scope (light build):**

- The recurring **bio / health / drug-discovery / structural-biology workshops** at ICML 2026 (see roster below).
- Main-track papers that match a **cancer / genomics / single-cell / spatial / drug-discovery / clinical-NLP keyword filter** (anticipate a few dozen out of ~2,000 main-track papers).
- The **agentic-AI / LLM-for-science** subset of the main track, regardless of explicit bio framing.

**Out of scope:**

- General-purpose ML methods papers (vision-only, NLP-only, RL-only, theory, optimization, fairness, robotics, etc.) with no plausible bio downstream — the >95% bulk.
- The full ~2,000-paper main proceedings; bulk extraction is explicitly **not** planned.
- Tutorials, expo days, and competitions outside the bio / health niches.

## Anticipated bio / health-relevant workshops

ICML announces workshop notifications on Mar 20, 2026 with final notification May 15, 2026 — the 2026 roster lands inside our planning window but may not be fully public until contributions deadlines pass. Based on the 2024 and 2025 cycles, we expect roughly this set to recur (acronyms in parentheses are ICML-canonical; year-on-year rebranding is common):

| Workshop | Theme | Canonical short name | Last seen |
|---|---|---|---|
| Multi-modal Foundation Models and LLMs for Life Sciences | foundation models for genomics, protein, transcriptomic, multi-omic; cross-modal bio | **FM4LS / ML4LMS** | 2025 |
| Generative AI for Biology | de novo protein / molecule design, RFdiffusion-class, generative chemistry for therapeutics | **GenBio** | 2024, 2025 (2nd ed.) |
| AI for Science (bio / chem subset) | physics / chem / bio crossover; bio-relevant contributions only | **AI4Science** | recurring across ICML + NeurIPS |
| Foundation Models for Health / FM4Health (anticipated) | clinical NLP, EHR, medical imaging, regulatory and trust | **FM4Health** | anticipated 2026 |
| Long-Context Foundation Models (genomic-LM subset) | genomic LMs (Evo / NT-class), long-context scientific corpora | **LCFM** | 2025 (2nd ed.) |

The 2026 roster won't be confirmed until late May; the above is our planning anchor. The keyword filter is the safety net if a recurring workshop drops or a new entrant appears.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Main proceedings** | ~2,000 accepted papers | PMLR proceedings; OpenReview group `ICML.cc/2026/Conference` posts accept list mid-year. Camera-ready papers under PMLR-style open license. |
| **Workshop pages** | one OpenReview venue per workshop | Roster finalizes May 15; each workshop posts accepted papers May–June. |
| **bioRxiv mirrors** | most bio-relevant ICML papers have a preprint | Filter bioRxiv for "ICML 2026" mentions; lag of weeks. |
| **Twitter/Bluesky/Mastodon** | real-time talk reactions | `#ICML2026`; useful for catching which agentic-AI / FM-bio papers get traction. |
| **Recorded talks** | SlidesLive + YouTube | ICML records orals + most workshop talks; posts within ~1–2 weeks of the meeting. |
| **Cross-link with NeurIPS** | author + tool overlap | Many ICML bio papers reappear at NeurIPS LMRL / MLSB six months later — single tool entry should consolidate both. |

## Organization

```
conferences/icml-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep — dates, filter criteria, expected themes
└── tools/               # per-paper / per-tool entries, populated post-notification
    └── index.md         # template + scope-filter note
```

No `digest/`, no `themes.md`, no `keynotes/`. The light-build pattern mirrors NeurIPS 2026: only `tools/` gets populated, and only with the filtered subset.

## What's different from full-conference vaults

Compared to ISMB 2026, RECOMB 2026, AACR 2026, ASCO 2026, or EuroBioC 2025 — which aim at near-complete program coverage — ICML 2026 is **scope-limited by design**:

- No per-session digests, no per-day digests, no themes synthesis. The general-purpose ML bulk is irrelevant.
- No keynote / plenary coverage unless the speaker is a known bio-FM author (e.g., a Demis Hassabis / John Jumper / Regina Barzilay-class talk).
- Tool entries are filtered down to a few dozen, not exhaustive. The filter is keyed on the AACR axes, not on ICML's own taxonomy.
- Most ICML 2026 tool entries should explicitly cross-link to a NeurIPS 2026 cousin paper (LMRL / MLSB / AI4D3) — author and method overlap is the rule, not the exception.

## Key dates

| Date | Event |
|---|---|
| Jan 8, 2026 | Submission site + OpenReview accounts opened — past |
| Jan 23, 2026 | Abstract submission deadline (AoE) — past |
| Jan 28, 2026 | Full paper submission deadline (AoE) — past |
| Jan 21, 2026 | Workshop proposal submissions open — past |
| Feb 13, 2026 | Workshop application deadline (AoE) — past |
| **Mar 20, 2026** | Workshop acceptance notifications — past |
| Apr 24, 2026 | Workshop contributions deadline (AoE) — past |
| **May 15, 2026** | Workshop final notification (AoE) — **this week** |
| May 24, 2026 | Early registration pricing deadline |
| Jun 3, 2026 | Dietary preference deadline |
| Jun 15, 2026 | Registration cancellation deadline (8:59 PM KST) |
| **Jul 6, 2026** | Expo / Tutorial Day |
| **Jul 7–9, 2026** | Main conference (Seoul, COEX) |
| **Jul 10–11, 2026** | Workshops |

## Sources

- [ICML 2026 home](https://icml.cc/Conferences/2026)
- [ICML 2026 Call for Papers](https://icml.cc/Conferences/2026/CallForPapers)
- [ICML 2026 Call for Workshops](https://icml.cc/Conferences/2026/CallForWorkshops)
- [OpenReview ICML group](https://openreview.net/group?id=ICML.cc)
- [PMLR ICML proceedings archive](https://proceedings.mlr.press/)
- [ICML 2025 workshop page (FM4LS reference)](https://icml.cc/virtual/2025/events/workshop)
- [GenBio workshop (recurring)](https://genbio-workshop.github.io/)

## Next step

- **Now → late May 2026:** monitor for workshop final-notification list (May 15) and main-track accepted-paper list announcement. No content extraction until either drops.
- **Late May – Jun 2026:** scaffold likely workshop pages and run the keyword filter against the main-track accepted list to identify the ~few-dozen bio-relevant papers; cross-check author lists against NeurIPS 2026 expectations.
- **Jul 6–11, 2026 (during the meeting):** opportunistic capture of social reactions, especially for GenBio / FM4LS orals and any agentic-AI main-track talks.
- **Post-meeting (mid-Jul 2026 onward):** populate `tools/` with the filtered subset; cross-link into AACR 2026 agentic-AI and virtual-cells axes, plus the NeurIPS 2026 cousins.
