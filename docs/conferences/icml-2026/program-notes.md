# ICML 2026 — Program Notes (pre-meeting prep)

> Internal working file. Today is **May 11, 2026** — the meeting is ~2 months out. Main-paper submissions closed Jan 28, 2026; workshop final-notification deadline is May 15, 2026 (this week); accepted-paper lists post on OpenReview around the same window through camera-ready in June. **Limited accepted-paper data exists yet.** This file holds the scaffolding so we can move fast once the lists drop.

## Verified facts

| Field | Value | Source |
|---|---|---|
| Conference | Forty-Third International Conference on Machine Learning | icml.cc |
| City | Seoul, South Korea | icml.cc/Conferences/2026 |
| Venue | COEX Convention & Exhibition Center | icml.cc/Conferences/2026 |
| Expo / Tutorial Day | Jul 6, 2026 | icml.cc |
| Main conference | Jul 7–9, 2026 | icml.cc |
| Workshops | Jul 10–11, 2026 | icml.cc |
| Submission site opened | Jan 8, 2026 — past | CallForPapers |
| Abstract submission deadline | Jan 23, 2026 (AoE) — past | CallForPapers |
| Full paper submission deadline | Jan 28, 2026 (AoE) — past | CallForPapers |
| Workshop application deadline | Feb 13, 2026 (AoE) — past | CallForWorkshops |
| Workshop acceptance notifications | Mar 20, 2026 — past | CallForWorkshops |
| Workshop contributions deadline | Apr 24, 2026 (AoE) — past | CallForWorkshops |
| Workshop final notification | May 15, 2026 (AoE) — **this week** | CallForWorkshops |
| Early registration deadline | May 24, 2026 (AoE) | icml.cc |
| Registration cancellation deadline | Jun 15, 2026 (8:59 PM KST) | icml.cc |
| Paper format | 8 pages main + unlimited references / impact / appendix; +1 page for camera-ready | CallForPapers |
| License | PMLR open-access (proceedings) + OpenReview hosting | PMLR / OpenReview |

## Sources we will rely on

| Source | When usable | Coverage |
|---|---|---|
| [ICML 2026 home](https://icml.cc/Conferences/2026) | now | dates, venue, organizers, registration |
| [Call for Papers](https://icml.cc/Conferences/2026/CallForPapers) | now | submission rules, paper-format spec |
| [Call for Workshops](https://icml.cc/Conferences/2026/CallForWorkshops) | now | workshop timeline |
| [OpenReview ICML group](https://openreview.net/group?id=ICML.cc) | from late May 2026 | accepted main-track papers + per-workshop venues |
| [PMLR proceedings](https://proceedings.mlr.press/) | from ~Jul 2026 | camera-ready, citeable |
| [SlidesLive (ICML)](https://slideslive.com/icml) | from ~Jul 15 onward | recorded orals + workshop talks |
| bioRxiv / arXiv | continuous | preprints, filterable by "to appear at ICML 2026" / "accepted at ICML 2026" |
| `#ICML2026` on Bluesky / Mastodon / X | Jul 6–11 | real-time talk reactions |
| Lab blogs (DeepMind, Anthropic, Insitro, Recursion, Genentech prescient design, Isomorphic Labs, Profluent, Cradle, Latent Labs) | rolling | preprints + summary posts of ICML papers from these labs |

## Filter criteria (locked — mirrors `tools/index.md`)

A paper enters this vault only if it matches **one** of three filters. Reproduced here for the pre-meeting screening pass.

### Filter 1 — workshop track

Accept anything in these workshops (canonical short names; 2026 roster finalizes May 15):

- **FM4LS / ML4LMS** — Multi-modal Foundation Models and LLMs for Life Sciences
- **GenBio** — Generative AI for Biology (3rd edition anticipated)
- **AI4Science** — AI for Science (bio / chem subset only)
- **FM4Health** — Foundation Models for Health (anticipated entrant; may surface under a different rebrand)
- **LCFM** — Long-Context Foundation Models (genomic-LM contributions only)

### Filter 2 — main-track keyword

Run this regex over titles + abstracts once the main-track accept list publishes:

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
- Scientific-reasoning benchmarks (SWE-bench-class, sci-agent-class, lab-task benchmarks)
- Autonomous research / hypothesis-generation systems
- Multi-agent scientific workflows

Rationale: these adapt to oncology within ~6 months (the empirical pattern from 2024 → AACR 2025 and 2025 → AACR 2026) and feed the AACR agentic-AI axis directly.

## Expected paper themes (5 anchors)

Pre-meeting predictions, to be reconciled against the actual list in late May / June. These are the buckets we expect `tools/` entries to cluster into.

### Theme 1 — Foundation models for biology, second generation

scGPT, Geneformer, and ESM are 2022–2024 vintage. ICML 2026 should feature the next-gen models: cross-modal (DNA + RNA + protein + tissue + clinical), multi-million-cell training corpora, instruction-tuned for downstream tasks (perturbation prediction, virtual-screen rerank), and benchmarked on virtual-cell tasks rather than embedding-quality proxies. Workshop home: **FM4LS / ML4LMS**, with main-track spillover. Expect heavy overlap with the NeurIPS 2026 LMRL roster six months later.

### Theme 2 — Agentic AI for science

Tool-use LLMs that drive bioinformatics pipelines, design wet-lab experiments, or autonomously navigate clinical-decision trees. 2025 surfaced ChemCrow / Coscientist-class systems; 2026 should bring oncology-specific agents (tumor-board agents, trial-matching agents, multi-omics interpretation agents). Workshop home: main-track + **FM4Health** (if it runs); also AI4Science.

### Theme 3 — Single-cell + spatial ML methods

Cell-state representation learning, perturbation-response prediction (Replogle-class, sci-Plex-class benchmarks), spatial-transcriptomics imputation, cell-cell communication inference, virtual-tissue generation. Workshop home: **FM4LS / ML4LMS**; main-track for the methods-heavy contributions. The 2025 FM4LS roster anchored this theme strongly; 2026 should extend it.

### Theme 4 — Generative biology: de novo protein, antibody, and molecule design

De novo small-molecule generation conditioned on oncology targets, antibody / TCR / peptide design, equivariant diffusion models for protein–ligand co-design, RFdiffusion descendants, Boltz / AlphaFold3-class structure models, flow-matching applied to molecular design. Workshop home: **GenBio** (3rd edition anticipated); main-track for the headline releases.

### Theme 5 — Long-context genomic and clinical language models

Evo / NT-class genomic LMs scaling to whole-chromosome / whole-genome context windows; clinical-trajectory LMs over multi-year EHR sequences; long-context FMs for whole-slide pathology / whole-trajectory radiology. Workshop home: **LCFM** (genomic-LM subset) + **FM4LS / FM4Health** spillover; main-track for the architecture papers.

## Pre-meeting timeline (action items)

| Date | Action |
|---|---|
| Now → May 15, 2026 | passive monitoring; await workshop final-notification list |
| **May 15, 2026** | workshop roster finalized — confirm which bio/health workshops actually run, identify any new entrants |
| Late May – Jun 2026 | main-track accepted-paper list publishes via OpenReview — run keyword regex, build candidate list |
| Jun 2026 | per-workshop accepted-paper lists drop — extend candidate list; cross-check author overlap with NeurIPS 2026 expected roster |
| Late Jun 2026 | scaffold likely `tools/` pages from titles + bioRxiv mirrors |
| **Jul 6–11, 2026** | meeting week — opportunistic real-time capture from social, especially agentic-AI and GenBio orals |
| Mid-Jul 2026 → Aug 2026 | bulk `tools/` population from SlidesLive recordings + camera-ready / PMLR papers |

## Caveats

- **Partial accepted-paper data.** Workshop accept lists and the main-track list publish on a rolling basis through May–Jun. Past-year patterns anchor the planning; the keyword filter is the safety net.
- **2026 workshop roster could shift.** FM4LS appeared in 2025; the committee favors novel workshops over long-running iterations, so the same theme may rebrand. The keyword filter and theme anchors mitigate this.
- **ICML / NeurIPS author overlap.** Many tools and authors appear at both venues within a calendar year. Tool-entry consolidation policy is in `tools/index.md` open question 3.
- **Agentic-AI scope creep risk.** Filter 3 is broader than Filters 1–2 by design, but it can swell if applied loosely. Keep the "science / tool-use benchmark required" caveat enforced.
- **Seoul-venue logistics.** No bearing on the vault, but the meeting-week digest (if we run one) needs to account for KST time-zone offsets when capturing social reactions.
