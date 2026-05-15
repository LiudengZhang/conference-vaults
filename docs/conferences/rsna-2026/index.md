# RSNA 2026

**112th Scientific Assembly and Annual Meeting of the Radiological Society of North America** — McCormick Place, Chicago, IL · Nov 29 – Dec 3, 2026. ~50,000 attendees, the largest medical-imaging meeting in the world. 2026 theme: **"At the Center of Care"** (president-elect cycle; full leadership confirmed closer to the meeting).

> **Status:** Scaffold — meeting is **~7 months out** as of today. Abstract submission closed earlier in the spring; acceptance notifications are rolling out now (RSNA in Brief April 2026). Registration opens late July. This vault stands up the per-tool template and the program-notes prep page now so the live-coverage scaffold is ready when the AI Showcase exhibitor list and program grid go public (typically late summer / early fall).

## Why this is in the vault

RSNA is the **medical-imaging counterpart** to [AACR 2026](../aacr-2026/index.md). The convergence point is **imaging foundation models**: the same self-supervised whole-slide / multimodal architectures that AACR 2026 tracks for histopathology (CHIEF, Prov-GigaPath, UNI/UNI2) extend at RSNA to radiology — CT, MR, mammography, and emerging cross-modality FMs that read pathology + radiology + radiology-text jointly. RSNA is also where **clinical-deployment data** for those models lands (prospective screening trials, real-world readouts, FDA-cleared product announcements), which AACR almost never carries.

The AACR vault already has standalone dossiers for [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md), [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md), and [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md). The RSNA vault extends that index with the **radiology-native** FMs and methods (RadFM, Med-PaLM-M, Merlin, RadDino, MAIRA, CheXagent, MedSAM, plus whatever debuts in the 2026 cycle) and the **clinical-trial readouts** that depend on them.

**Format note:** RSNA is **half tools / half trials** — closer in shape to the JPM / ASCO vaults than to AACR. Per-tool pages anchor the AI track; per-trial pages anchor the screening-AI and imaging-driven oncology readouts (lung-cancer screening AI, mammography AI-CAD, prostate MRI PI-RADS AI). No standalone `trials/` subdirectory yet — the imaging-trial coverage is folded into the per-tool pages where a model has named trial data, with a light cross-link table in `program-notes.md`. If the post-meeting corpus warrants it, a separate `trials/` directory gets carved out.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **RSNA Daily Bulletin** | per-day session recaps written by RSNA editorial | [dailybulletin.rsna.org](https://dailybulletin.rsna.org/) — first-pass primary source during the meeting |
| **RSNA Meeting Program** | session grid, refresher courses, scientific sessions, AI track | [meeting.rsna.org](https://meeting.rsna.org/) — searchable program goes live late summer |
| **Radiology / Radiology: AI** journals | embargoed companion publications timed to the meeting | [pubs.rsna.org](https://pubs.rsna.org/) — many headline trial readouts publish simultaneously with the meeting talk |
| **AI Showcase exhibitor list** | 100+ AI vendors in South Hall A | [rsna.org/ai-showcase](https://www.rsna.org/annual-meeting/exhibitors-and-sponsors/exhibit-spaces/ai-showcase) — booth-level demo programming |
| **RSNAI Monthly press releases** | RSNA's own AI-track preview series | [rsna.org/media/press](https://www.rsna.org/media/press) — monthly cadence Sep–Dec |
| **Aunt Minnie / RadAI / AuntMinnie Europe** | trade-press editorial, sponsor stand-ups | [auntminnie.com](https://www.auntminnie.com/), [radai.com](https://www.radai.com/) |
| **STAT / HealthTechHotspot** | post-meeting analyst framing, infrastructure narrative | sub-required for some |
| **Vendor press releases** | RSNA 2026 product announcements, FDA-cleared offerings | wire-service syndication |
| **Plenary livestreams + replay** | named lectures, presidential address | RSNA Virtual Meeting (separate registration; on-demand for ~12 months) |

The **Radiology / Radiology: AI** companion-publication pattern is the analogue to ASCO's Meeting Library: every load-bearing claim from a podium talk should be backed by a journal DOI when one exists, not just the Daily Bulletin recap.

## Program shape

RSNA 2026 runs **Sunday Nov 29 through Thursday Dec 3**, five days, McCormick Place. The structure:

- **Sunday Nov 29** — opening day. President's Address + Annual Oration (named lecture). First scientific sessions. Technical Exhibits open 10:00–17:00 CT.
- **Monday Nov 30 – Wednesday Dec 2** — full program days. Scientific sessions, refresher courses, hot-topic / controversy sessions, plenaries, AI Theater programming.
- **Thursday Dec 3** — closing day, lighter program. Some refresher courses, AI Showcase closed.
- **AI Showcase (South Hall A, Booth ~4700-block)** — 100+ AI vendors, demo programming, AI Theater (20-minute vendor talks Sun–Wed), runs Nov 29 – Dec 2.
- **"Radiology Reimagined: AI, innovation and interoperability in practice"** demonstration — live every half hour Mon–Wed in the AI Showcase. Showcases standards-based AI integration into the diagnostic workflow (the IAIP successor demo).
- **Deep-learning lecture series** — refresher-course track on AI/ML fundamentals, governance, validation. Recurring multi-day series.
- **2026 RSNA AI Challenge — Knee MRI** (announced; first MSK challenge in the series). Winners announced at the meeting.
- **~1,500+ scientific paper sessions, ~1,800+ scientific posters, ~700 refresher courses** (typical scale; 2026-specific counts available after the program goes live).
- **Tracks dominating the AI corpus:** Breast (AI-CAD, density / risk models), Chest (lung-nodule detection, screening AI), Neuro (stroke triage, tumor segmentation), MSK (this year's challenge focus), Cardiac (CCTA AI), Abdominal (opportunistic-screening AI, body composition), Informatics (foundation models, multimodal LLMs, governance / regulation / reimbursement).

## Organization

```
conferences/rsna-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep: dates, venue, AI track structure, expected FM updates,
│                        # cross-links to AACR pathology-FM dossiers, anticipated imaging-trial readouts
└── tools/               # PRIMARY artifact — per-tool template for imaging FMs + AI methods
    └── index.md         # template + master tool index table, cross-linked to AACR dossiers
```

The `tools/` directory is the load-bearing artifact, mirroring the [EuroBioC 2025 per-tool template](../eurobioc-2025/tools/index.md) but adapted for medical-imaging FMs and methods (where "Bioconductor package page" becomes "model weights + checkpoint + license"). Imaging-driven clinical trials are folded in as a "Named trials using this model" sub-section on each tool page rather than getting their own directory — most trials at RSNA are about evaluating a model, so the model is the natural index.

Expected ~15–25 tool entries by post-meeting close, depending on how many radiology-native FMs surface new checkpoints / clinical-deployment data at the 2026 cycle. The AACR pathology-FM dossiers are **not duplicated** here — they're cross-linked, with an RSNA-specific addendum on each tool page noting any radiology-extension work or cross-modality variants surfaced at RSNA.

## What's different from AACR 2026

- **Imaging-FM is the convergence point, not the periphery.** At AACR, pathology FMs are one topic among many; at RSNA, foundation models for radiology are the dominant axis of the AI track. The tool template is identical to AACR's bioinfo-tools index in structure; the population differs.
- **Clinical-deployment data is first-class.** Where AACR mostly carries the model paper and a few benchmark posters, RSNA carries the prospective screening trial, the real-world readout, the FDA-clearance press release, and the post-deployment audit (drift, fairness, generalization).
- **Vendor presence dominates the exhibit floor.** Unlike AACR (academic-led), RSNA's AI Showcase is vendor-led — 100+ companies, named booths, AI Theater demo programming. The vault treats vendor announcements as second-tier sources (linked in tool pages but always paired with a peer-reviewed reference or named talk).
- **Cross-modality FMs are the 2026 watch.** The 2024–2025 cycle was about pathology FMs (CHIEF, GigaPath, UNI). 2026 will likely surface more radiology-pathology bridges (Merlin-style; multimodal report-generation models). These are tracked here, not at AACR.

## Cross-vault links

- **[AACR 2026](../aacr-2026/index.md)** — the pathology-FM and biology side. Direct dossier links from the RSNA tool pages back to:
  - [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) — pathology FM, Mahmood Lab, Nature 2024
  - [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) — pathology FM, Microsoft / Providence
  - [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md) — pathology FM, Mahmood Lab, Nature Medicine 2024
- **[JPM 2026](../jpm-2026/index.md)** — financing / commercial layer. Many RSNA 2026 vendors had JPM presentations in January (imaging-AI startups, large vendors like GE / Siemens / Philips).
- **[ASCO 2026](../asco-2026/index.md)** — clinical-trial counterpart for imaging-driven oncology readouts (lung-screening AI, breast-density / risk models tied to chemoprevention).
- **[Conferences timeline](../../timeline.md)** — RSNA's position in the year's cycle (AACR Apr → ASCO May/Jun → ESMO Oct → ASH Dec → RSNA late Nov / early Dec → JPM Jan).

## Next step

- **Now (May 2026, T-7 months):** stand up the per-tool template and program-notes prep file (this commit). Identify the candidate FM list — pathology FMs (cross-link to AACR), radiology-native FMs (RadFM, Med-PaLM-M, Merlin, RadDino, MAIRA, CheXagent), and segmentation FMs (MedSAM, SegVol). Track the AACR 2026 talks where radiology-pathology cross-modality work surfaced.
- **Summer 2026 (T-3 to T-5 months):** registration opens late July; full program goes live late summer. At that point, populate the tool index with confirmed talks / sessions and pull the AI Showcase exhibitor list once published.
- **Fall 2026 (T-1 to T-2 months):** RSNAI Monthly Sep / Oct / Nov press releases preview the AI track. Pull the highlighted FMs / trials and pre-build stub pages.
- **Live meeting (Nov 29 – Dec 3):** Daily Bulletin recaps + Radiology / Radiology: AI companion-publication dropouts feed the tool pages and the embedded trial cross-links.
- **Post-meeting (Dec 2026 – Jan 2027):** finalize tool corpus. Cross-check against AACR 2026 pathology-FM mentions for the model-overlap audit.

## Sources

- [RSNA Annual Meeting home](https://www.rsna.org/annual-meeting)
- [RSNA AI Showcase](https://www.rsna.org/annual-meeting/exhibitors-and-sponsors/exhibit-spaces/ai-showcase)
- [AI at the Annual Meeting](https://www.rsna.org/artificial-intelligence/at-the-meeting)
- [Radiology Reimagined: AI, innovation and interoperability in practice](https://www.rsna.org/artificial-intelligence/radiology-reimagined-ai)
- [RSNA 2026 abstract-submission status note (RSNA in Brief, Apr 2026)](https://www.rsna.org/media/press/2026/2652)
- [Radiology journal](https://pubs.rsna.org/journal/radiology)
- [Radiology: Artificial Intelligence journal](https://pubs.rsna.org/journal/ai)
- [RSNA Daily Bulletin](https://dailybulletin.rsna.org/)
- [Future & past meetings](https://www.rsna.org/annual-meeting/future-and-past-meetings)
