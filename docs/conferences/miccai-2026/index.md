# MICCAI 2026

**29th International Conference on Medical Image Computing and Computer Assisted Intervention** — Strasbourg Convention Center, Strasbourg, France · September 27 – October 1, 2026. ~3,000 attendees. Hosted by the [MICCAI Society](https://miccai.org/); peer-reviewed proceedings published in Springer Lecture Notes in Computer Science (LNCS) ~1 week before the meeting.

> **Status:** Scaffold — meeting is **~20 weeks out** as of May 11, 2026. Early acceptance notifications went out May 7; rebuttal window runs May 8–14; final decisions land June 12. Proceedings post no earlier than September 21. This vault stands up the per-tool template and program-notes prep page now so the live-coverage scaffold is ready when (a) the early-accept list is public, (b) the workshop/challenge slate is finalized (acceptance March 13, 2026, so already known but not yet centrally listed on the 2026 site), and (c) the proceedings PDFs drop in late September.
>
> **One factual note up front:** MICCAI 2026 was originally awarded to Abu Dhabi, UAE. The MICCAI Board relocated the meeting to Strasbourg due to regional uncertainty; Abu Dhabi is now slated for 2029. References to "MICCAI 2026 Abu Dhabi" in older calls / press materials are stale.

## Why this is in the vault

MICCAI is the **methods-and-models counterpart to [RSNA 2026](../rsna-2026/index.md)** in the medical-imaging-AI axis, and the **radiology-side methods feeder to [AACR 2026](../aacr-2026/index.md)** in the foundation-model axis. The convergence points:

- **Pathology foundation models.** The AACR vault already carries standalone dossiers for [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md), [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md), and [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md). Their **methodology papers** (and the next-cycle updates — UNI2, new tile encoders, slide-level aggregation methods) are MICCAI / MICCAI-workshop work. When CHIEF cites "self-supervised pretraining at tile-level," that loss / sampling / curation work lives in MICCAI proceedings or COMPAY / MILEX workshop papers, not in *Nature Medicine*.
- **Radiology AI methods.** Segmentation (nnU-Net-class), registration (deformable, learning-based), generative medical imaging (diffusion priors for MRI/CT reconstruction, synthetic data for fairness), and multimodal vision-language models (report generation, radiology-text alignment) are MICCAI-native. These feed the imaging-AI tool entries in the RSNA vault.
- **Oncology-specific challenges.** MICCAI hosts the long-running cancer-imaging challenges that anchor public benchmarks: **BraTS** (brain tumor), **HECKTOR** (head-and-neck PET/CT), **KiTS** (kidney tumor), **AutoPET** (whole-body lesion segmentation), **PANORAMA** (pancreas), plus rotating skin / mammography / prostate efforts. Any oncology imaging AI claim at AACR or RSNA likely benchmarks against one of these.
- **Computer-assisted intervention.** The "CAI" half of MICCAI carries surgical AI (laparoscopic navigation, surgical phase recognition, intra-op imaging) — relevant to rad-onc dose planning, IGRT (image-guided radiotherapy), and emerging surgical-oncology AI.
- **Peer-reviewed, proceedings-backed.** Unlike RSNA (clinical-trial / vendor-heavy, journal-paired but not proceedings-driven), MICCAI has a **two-round peer review** (rebuttal window built into the timeline) and full LNCS proceedings. Tool entries here can cite a Springer DOI alongside the talk metadata — same shape as ISMB / RECOMB, not RSNA.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **MICCAI 2026 home** | venue, dates, key dates, calls | [conferences.miccai.org/2026](https://conferences.miccai.org/2026) |
| **Important Dates** | full timeline through final decisions | [conferences.miccai.org/2026/en/IMPORTANT-DATES.html](https://conferences.miccai.org/2026/en/IMPORTANT-DATES.html) — abstract Feb 12, papers Feb 26, early accept May 7, rebuttal May 8–14, final decision Jun 12 |
| **Call for Papers** | topic areas, formatting | [conferences.miccai.org/2026/en/CALL-FOR-PAPERS.html](https://conferences.miccai.org/2026/en/CALL-FOR-PAPERS.html) |
| **Call for Workshops** | workshop slate, dates Sep 27 + Oct 1 | [conferences.miccai.org/2026/en/CALL-FOR-WORKSHOPS.html](https://conferences.miccai.org/2026/en/CALL-FOR-WORKSHOPS.html) — LOI Dec 15 2025, full proposal Jan 15 2026, accept Mar 13 2026 |
| **Call for Challenges** | challenge slate, ESR-collaboration oncology track | [conferences.miccai.org/2026/en/CALL-FOR-CHALLENGES.html](https://conferences.miccai.org/2026/en/CALL-FOR-CHALLENGES.html) — three ESR-flagged oncology topics (colorectal liver mets CT, PET oncology assessment, RECIST on thorax-abdomen CT); top 3 also present at ECR 2027 |
| **Springer LNCS proceedings** | peer-reviewed full papers + DOIs | Springer publishes multi-volume LNCS set ~Sep 21–26; each paper has a DOI before the talk. Open-access option (gold OA) for authors who pay APC; otherwise paywalled but author-uploaded preprints typical on arXiv. |
| **MICCAI Society challenges registry** | historical + 2026-registered challenges | [miccai.org/index.php/special-interest-groups/challenges/miccai-registered-challenges/](https://miccai.org/index.php/special-interest-groups/challenges/miccai-registered-challenges/) |
| **arXiv mirrors** | preprints flagged "to appear in MICCAI 2026" | the dominant preprint channel for MICCAI work; expect a wave of postings May–Aug 2026 as accept notifications go out |
| **CliniCAI (Clinical Day)** | clinical-translation track | listed on 2026 program nav; clinician-facing companion to the main proceedings |
| **Open Data initiative** | open-data submissions tied to the conference | dedicated call on the 2026 site |
| **Virtual Startup Village** | pitch competition; deadline Jun 1, 2026 | application window open as of May 2026 |
| **Social / press** | #MICCAI2026 on Bluesky, X, Mastodon | useful for real-time talk reactions; not a primary source |

## Program shape

MICCAI 2026 runs **Sunday Sep 27 through Thursday Oct 1**, five days at the Strasbourg Convention Center. The canonical MICCAI structure (carried over from the 2024 Marrakesh / 2025 Daejeon cycles):

- **Sunday Sep 27** — Satellite Events day 1: tutorials (half- and full-day), workshops (start), challenges (kickoff / on-site phase). No main proceedings sessions.
- **Monday Sep 28 – Wednesday Sep 30** — Main conference. Each day opens with a keynote (typically 3 keynotes across the three main days), followed by 3–4 parallel oral sessions and large poster sessions. Awards (Best Paper, Young Scientist, MICCAI Society Fellow) announced at the closing plenary Wednesday.
- **Thursday Oct 1** — Satellite Events day 2: remaining workshops, tutorials, challenge result sessions. CliniCAI (Clinical Day) typically lands on one of the satellite days.
- **Workshops** — ~35–60 typically, split across the two satellite days. Cancer-relevant recurring ones (subject to 2026 acceptance, finalized Mar 13, 2026):
  - **BrainLes / BraTS** — brain tumor segmentation, the largest and longest-running MICCAI challenge-plus-workshop
  - **COMPAY** — Computational Pathology (pathology-FM home; pairs with AACR pathology-FM dossiers)
  - **MILEX / MILLanD** — medical image labels, low-supervision learning
  - **DGM4MICCAI** — Deep Generative Models for MICCAI (diffusion, GANs for medical imaging)
  - **CaPTion** — Cancer Prevention through Image-based Technologies (when running)
  - **MMMI / Multi-Modal** — multimodal learning across modalities
  - **PIPPI** — perinatal, preterm, paediatric imaging (sometimes carries paediatric oncology)
- **Challenges** — historically ~25–40 registered per year. Oncology-relevant recurring slate (subject to 2026 registration):
  - **BraTS** — brain tumor (Adult Glioma, Meningioma, Pediatrics, Africa, MET, Inpainting sub-tasks)
  - **HECKTOR** — head-and-neck PET/CT tumor + outcome
  - **KiTS** — kidney tumor / surgical AI
  - **AutoPET** — whole-body FDG PET/CT lesion segmentation
  - **PANORAMA** — pancreatic cancer detection (PDAC)
  - **ISIC-style** skin lesion challenges (sometimes co-located)
  - **2026 ESR oncology track** — three ESR-flagged proposals (colorectal liver mets CT, PET oncology, RECIST thorax-abdomen CT); winners co-present at ECR 2027
- **Keynotes** — 3 plenary speakers across Mon–Wed (slate not yet announced as of May 11, 2026)
- **Posters** — typically >1,500 across the main 3 days, two daily blocks
- **Startup Village** — applications close Jun 1, 2026

## Organization

```
conferences/miccai-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep: dates, venue, workshop/challenge slate,
│                        # anticipated oncology-relevant work, cross-links to AACR/RSNA dossiers
├── themes.md            # cross-day synthesis (deferred until post-meeting)
├── digest/              # day-by-day recap (deferred until post-meeting)
│   ├── day-0-sunday.md      # tutorials + workshops day 1 + challenge kickoff
│   ├── day-1-monday.md      # keynote 1 + main proceedings sessions
│   ├── day-2-tuesday.md     # keynote 2 + main proceedings sessions
│   ├── day-3-wednesday.md   # keynote 3 + closing plenary + awards
│   └── day-4-thursday.md    # workshops day 2 + CliniCAI + challenge results
├── keynotes/            # one entry per plenary keynote (deferred until speakers announced)
├── topics/              # cross-cutting bins (deferred)
│   ├── pathology-fm/        # COMPAY + main-proceedings pathology FMs (CHIEF / GigaPath / UNI updates)
│   ├── segmentation/        # nnU-Net descendants, SAM-medical adapters
│   ├── generative-imaging/  # DGM4MICCAI + main-proceedings diffusion / synthesis
│   ├── radiotherapy-ai/     # dose planning, IGRT, auto-contouring
│   ├── multimodal-vlm/      # report generation, radiology-text, multimodal FMs
│   ├── surgical-ai/         # CAI side — phase recognition, intra-op imaging
│   └── oncology-challenges/ # BraTS / HECKTOR / KiTS / AutoPET / PANORAMA results
├── tools/               # PRIMARY artifact — one entry per model / method / package
│   └── index.md
└── sessions/            # full session index (post-meeting, after proceedings drop)
    └── index.md
```

The `tools/` directory is the load-bearing artifact, same shape as [ISMB 2026](../ismb-2026/tools/index.md) and [RECOMB 2026](../recomb-2026/index.md). MICCAI-specific additions to the per-tool template (see [`tools/index.md`](tools/)): a **Proceedings** row pointing to the Springer LNCS DOI when applicable (versus *Bioinformatics* DOI for ISMB), and a **Track** field (Main proceedings / Workshop / Challenge / CliniCAI / Tutorial) to keep the satellite-vs-main signal legible.

## What's different from RSNA 2026

- **Peer-reviewed proceedings, not vendor-driven.** RSNA's AI Showcase is 100+ vendors with booths; MICCAI is academic-led, with full peer-reviewed LNCS proceedings. Tool entries here will be unusually complete pre-meeting (DOI + GitHub + benchmarks) — same depth as ISMB.
- **Methods, not deployment.** RSNA carries the prospective screening trial and the FDA-clearance press release; MICCAI carries the loss function, the architecture, the benchmark. The same pathology FM (e.g., UNI) gets a methods paper at MICCAI and a clinical-readout poster at RSNA / AACR.
- **Challenges as first-class artifact.** Unlike RSNA (one annual RSNA AI Challenge), MICCAI runs ~25–40 challenges per year. Many oncology AI benchmarks (BraTS, HECKTOR, KiTS, AutoPET, PANORAMA) live here and have been running 5–15+ years.
- **Surgical AI / CAI half.** RSNA is diagnostic imaging only. MICCAI's "CAI" track covers surgical phase recognition, laparoscopic navigation, intra-op imaging — orthogonal axis not present at RSNA.
- **Scale.** RSNA ~50,000 attendees (mostly clinicians); MICCAI ~3,000 (mostly engineers / methodologists / clinicians-in-method-track). MICCAI is closer in scale to ISMB / NeurIPS than to RSNA.

## Cross-vault links

- **[AACR 2026](../aacr-2026/index.md)** — pathology-FM and translational-cancer side. Direct dossier links from MICCAI tool pages back to:
  - [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) — pathology FM, Mahmood Lab
  - [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) — pathology FM, Microsoft / Providence
  - [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md) — pathology FM, Mahmood Lab
- **[RSNA 2026](../rsna-2026/index.md)** — clinical-deployment / vendor side of medical-imaging AI. Many MICCAI 2026 method papers will resurface at RSNA Nov 29–Dec 3 as clinical-deployment readouts.
- **[ISMB 2026](../ismb-2026/index.md)** — methodologically nearest sibling (peer-reviewed proceedings, methods-heavy, similar scale). Shape of the per-tool template is shared.
- **[NeurIPS 2026](../neurips-2026/index.md)** — general ML / FM side; cross-pollinates with MICCAI on medical-image FMs and diffusion methods.
- **[Conferences timeline](../../timeline.md)** — MICCAI's position in the year (AACR Apr → ASCO May/Jun → RECOMB May → ISMB Jul → ESMO Oct (overlaps) → MICCAI late Sep / early Oct → RSNA late Nov / early Dec).

## Sources

- [MICCAI 2026 home (conferences.miccai.org/2026)](https://conferences.miccai.org/2026)
- [MICCAI 2026 Important Dates](https://conferences.miccai.org/2026/en/IMPORTANT-DATES.html)
- [MICCAI 2026 Call for Papers](https://conferences.miccai.org/2026/en/CALL-FOR-PAPERS.html)
- [MICCAI 2026 Call for Workshops](https://conferences.miccai.org/2026/en/CALL-FOR-WORKSHOPS.html)
- [MICCAI 2026 Call for Challenges](https://conferences.miccai.org/2026/en/CALL-FOR-CHALLENGES.html)
- [MICCAI Society home](https://miccai.org/)
- [MICCAI Registered Challenges](https://miccai.org/index.php/special-interest-groups/challenges/miccai-registered-challenges/)
- [Springer LNCS (proceedings publisher)](https://www.springer.com/series/558)
- [MICCAI 2025 Daejeon (prior year, for shape reference)](https://conferences.miccai.org/2025/en/)

## Next step

- **Now (May 2026, T-20 weeks):** stand up template + program-notes (this commit). Track the early-accept list (notifications May 7) and the workshop/challenge slate (already accepted Mar 13; populated as workshop sites go live through summer).
- **Summer 2026 (T-8 to T-16 weeks):** final paper decisions Jun 12 — full accepted-paper list public mid-June via OpenReview / arXiv mirrors. Pre-build stub pages for high-signal entries: any paper updating CHIEF / GigaPath / UNI / RadFM / Merlin-class FMs; any BraTS / HECKTOR / KiTS / AutoPET / PANORAMA challenge writeup; any DGM4MICCAI / COMPAY workshop standout.
- **Pre-meeting (T-1 to T-4 weeks):** Springer LNCS proceedings drop ~Sep 21–26. Pull DOIs into stub pages; populate the `tools/` index table.
- **Live meeting (Sep 27 – Oct 1):** real-time capture of slide deposits, GitHub repos, demo links from social. CliniCAI clinical-translation talks pair to RSNA preview.
- **Post-meeting (Oct 2026):** bulk tool-page extraction. Estimated ~25–50 tool entries — narrower than ISMB (proceedings filter is stricter) but deeper per-entry (full Springer DOI + arXiv + benchmark + code from the start). Cross-check against AACR 2026 pathology-FM mentions and stage radiology-side cross-links for RSNA 2026 (Nov 29).
