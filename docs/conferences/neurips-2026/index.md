# NeurIPS 2026

**40th Conference on Neural Information Processing Systems** — three-city satellite model:

- **Sydney, Australia** · Dec 6–12, 2026
- **Atlanta, Georgia, USA** · Dec 9–13, 2026
- **Paris, France** · Dec 9–13, 2026

> **Status:** Scaffold — meeting ~7 months out (today is May 11, 2026). Paper notifications go out Sep 24, 2026; workshop accept/reject Sep 29, 2026; accepted-paper list and workshop roster are not yet public. This is a **light build**, not full coverage — see "Scope" below.

## Why this is in the vault

NeurIPS is the largest ML venue worldwide (~15,000 attendees across the three satellite hubs in 2026, by ISCB-comparable estimates), and the overwhelming majority of its program is general-purpose ML with no direct cancer-research relevance. We are **not** trying to cover it like ISMB or EuroBioC. Instead, NeurIPS lives in this vault for one specific reason: it is the upstream methods source for the AACR vault's **agentic-AI** and **virtual-cells / foundation-model** axes. Almost every general-purpose architecture that later gets adapted to oncology (Transformer, diffusion model, RLHF, scaling-laws results, agentic-LLM scaffolds, equivariant GNN, flow matching for molecules) is first peer-reviewed here.

Two further reasons to keep a scoped presence:

- **Foundation models for biology cross-pollination.** scGPT, Geneformer, ESM-class protein models, RFdiffusion, Boltz / AlphaFold descendants, and Evo / NT-class genomic LMs all have NeurIPS papers in their lineage. The annual workshop circuit (LMRL, MLSB, AI4D3, GenAI for Health, AIM-FM) is where the next generation of these is unveiled.
- **Agentic AI for science.** Through 2025 NeurIPS became the canonical venue for LLM-agent / tool-use / scientific-reasoning work that the AACR agentic-AI axis tracks. The pattern: an agent paper presented here in December shows up as a TissueAgent / OncoAgent-class demo at AACR / ASCO the following spring.

## Scope (what this vault covers — and what it does not)

**In scope (light build):**

- The five recurring **bio / health / drug-discovery / structural-biology workshops** (see roster below).
- Main-track papers that match a **cancer / genomics / single-cell / spatial / drug-discovery / clinical-NLP keyword filter** (anticipate a few dozen, not thousands).
- The **agentic-AI / LLM-for-science** subset of the main track, regardless of explicit bio framing (these get adapted to oncology within ~6 months).

**Out of scope:**

- General-purpose ML methods papers (vision-only, NLP-only, RL-only, theory, optimization, fairness, robotics, etc.) with no plausible bio downstream — the >95% bulk.
- The full ~2,000-paper main proceedings; bulk extraction is explicitly **not** planned.
- Tutorials and competitions outside the bio / health niches.

## Anticipated bio / health-relevant workshops

NeurIPS announces its workshop roster late September. Based on the 2023, 2024, and 2025 cycles, we expect roughly this set to recur (acronyms in parentheses are NeurIPS-canonical; some merge or rebrand year-on-year):

| Workshop | Theme | Canonical short name | Last seen |
|---|---|---|---|
| Machine Learning in Structural Biology | protein structure, RFdiffusion-class, equivariant GNN | **MLSB** | 2024, 2025 |
| AI for New Drug Modalities / AI for Drug Discovery | small molecule + biologics generation, ADMET, target ID | **AI4NewDrugs / AI4D3** | 2024, 2025 |
| Learning Meaningful Representations of Life | foundation models for genomics, single-cell, spatial; cross-modal bio | **LMRL** | 2024, 2025 |
| GenAI for Health | clinical NLP, EHR, medical imaging, regulatory and trust | **GenAI4Health** | 2024, 2025 |
| Advancements in Medical Foundation Models | medical FMs, explainability, robustness, safety | **AIM-FM** | 2024, 2025 |
| AI for Science (catch-all) | physics / chem / bio crossover; sometimes splits into AI4Mat | **AI4Science** | recurring |

The 2026 roster won't be confirmed until Jul 11 (accept notifications) → Sep 29 (final). The above is our planning anchor; we'll reconcile against the official list when it drops.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Main proceedings** | ~2,000 accepted papers | OpenReview group `NeurIPS.cc/2026/Conference`; posted progressively from Sep 24 (notifications) through Dec (camera-ready). CC-BY. |
| **Workshop pages** | one OpenReview venue per workshop | Roster public Sep 29; each workshop posts its own accepted-paper list typically Oct–Nov. |
| **bioRxiv mirrors** | most bio-relevant NeurIPS papers have a preprint | Filter `bioRxiv` for "NeurIPS 2026" mentions; typical lag of weeks. |
| **Twitter/Bluesky/Mastodon** | real-time talk reactions | `#NeurIPS2026`; useful for noting which agentic-AI / FM-bio papers get traction. |
| **Recorded talks** | SlidesLive + YouTube | NeurIPS records all main-track orals + most workshop talks; posts on SlidesLive ~1 week post-meeting, then mirrors on YouTube. |
| **Three-city satellite schedules** | Sydney, Atlanta, Paris | Sydney runs Dec 6–12 (starts 3 days earlier); Atlanta and Paris overlap Dec 9–13. Workshop programs may differ slightly across satellites — TBD. |

## Three-city satellite model — what it means for us

NeurIPS 2026 is the **first three-hub year** (2025 had two-hub Vancouver + Mexico City pilot; 2026 expands to Sydney + Atlanta + Paris). For our purposes this matters in three ways:

- **Workshops may not all run at all three sites.** Bio / health workshops historically cluster at the "main" hub; in 2026 it's not yet clear which of Sydney / Atlanta / Paris is anchor. We track all three rosters when they drop.
- **Recordings reconcile across hubs.** SlidesLive + YouTube post a unified set, so a single Vault entry per paper is fine.
- **Time-zone bias for live attendance.** Not actionable for the vault, but the meeting-week digest (if we run one) should pick the hub whose program is densest for bio.

## Organization

```
conferences/neurips-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep — dates, filter criteria, expected themes
└── tools/               # per-paper / per-tool entries, populated post-meeting
    └── index.md         # template + scope-filter note
```

No `digest/`, no `themes.md`, no `keynotes/`. The light-build pattern is: only `tools/` gets populated, and only with the filtered subset. Anything more is a re-scope decision.

## Key dates

| Date | Event |
|---|---|
| May 6, 2026 | Main paper submission deadline (AoE) — **past** |
| Jun 6, 2026 | Workshop application deadline (AoE) |
| Jul 11, 2026 | Workshop acceptance notifications |
| Sep 24, 2026 | Paper author notifications |
| Sep 29, 2026 | Workshop accept/reject finalized |
| Oct–Nov 2026 | Workshop paper lists post on OpenReview |
| **Dec 6–12, 2026** | **Sydney hub** |
| **Dec 9–13, 2026** | **Atlanta + Paris hubs** |

## Sources

- [NeurIPS 2026 home](https://neurips.cc/Conferences/2026)
- [NeurIPS 2026 Call for Workshops](https://neurips.cc/Conferences/2026/CallForWorkshops)
- [OpenReview NeurIPS group](https://openreview.net/group?id=NeurIPS.cc)
- [SlidesLive (NeurIPS recorded talks archive)](https://slideslive.com/neurips)
- [LMRL workshop (recurring)](https://www.lmrl.org/)
- [MLSB workshop (recurring)](https://www.mlsb.io/)
- [GenAI for Health workshop (2024 reference)](https://genai4health.github.io/)

## Next step

- **Now → Sep 24, 2026:** monitor for accepted-paper list and final workshop roster. No content extraction until either drops.
- **Sep 29 – Dec 5, 2026:** scaffold likely workshop pages and run keyword filter against the main-track accepted list to identify the ~few-dozen bio-relevant papers.
- **Dec 6–13, 2026 (during the meeting):** opportunistic capture of social reactions, especially for agentic-AI / FM-for-biology orals.
- **Post-meeting (mid-Dec 2026 onward):** populate `tools/` with the filtered subset; cross-link into AACR 2026 agentic-AI and virtual-cells axes; flag candidates for adaptation to oncology benchmarks.
