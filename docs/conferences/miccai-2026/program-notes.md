# MICCAI 2026 — Program Notes (Pre-Meeting Prep)

Internal working file. Updated incrementally as the proceedings list, workshop sites, and challenge leaderboards go public through summer 2026. Today's state: **T-20 weeks**, early-accept notifications just went out (May 7), rebuttal window open through May 14, final decisions land Jun 12.

## Verified core facts

| Field | Value |
|---|---|
| **Edition** | 29th MICCAI |
| **Dates** | Sunday September 27 – Thursday October 1, 2026 |
| **Venue** | Strasbourg Convention Center, Strasbourg, France |
| **Organizing society** | [MICCAI Society](https://miccai.org/) |
| **Proceedings publisher** | Springer Lecture Notes in Computer Science (LNCS), multi-volume set posted no earlier than Sep 21, 2026 |
| **Local representative** | Caroline Essert (Université de Strasbourg) |
| **Expected attendance** | ~3,000 |
| **Theme** | not announced as of May 11, 2026 |
| **Relocation note** | Originally awarded to Abu Dhabi; relocated by MICCAI Board due to regional uncertainty. Abu Dhabi rescheduled to 2029. |

## Key dates (verified from Important Dates page)

| Milestone | Date |
|---|---|
| Abstract registration | Thursday February 12, 2026, 23:59 PT |
| Paper submission | Thursday February 26, 2026, 23:59 PT |
| Early acceptance notification | EOD May 7, 2026 PT |
| Rebuttal period | May 8 – 14, 2026 |
| Final decision | EOD June 12, 2026 PT |
| Camera-ready (early-accepted) | Monday May 25, 2026 |
| Camera-ready (all other) | Friday June 26, 2026 |
| Author registration deadline | Friday June 26, 2026 |
| Proceedings available | No earlier than September 21, 2026 |
| Workshop LOI deadline | December 15, 2025 |
| Workshop full proposal | January 15, 2026 |
| Workshop final acceptance | March 13, 2026 |
| Registration Grant deadline | May 17, 2026 |
| Travel Grant deadline | July 1, 2026 |
| Startup Village applications | June 1, 2026 |

## Day-by-day shape (working hypothesis from prior-year patterns)

Final program goes live mid-summer. Working from the standard MICCAI structure (carried over from 2024 Marrakesh and 2025 Daejeon):

- **Sunday Sep 27 — Satellite Events Day 1**
  - Half-day and full-day **tutorials** (~8–12 tutorials, all day, parallel)
  - **Workshops** day 1 (subset of the ~35–60 workshop slate)
  - **Challenges** on-site phase begins (live submissions, leaderboard sessions)
- **Monday Sep 28 — Main Conference Day 1**
  - Opening + Keynote 1 (TBA)
  - Main proceedings oral sessions (3–4 parallel)
  - Poster Session 1 (afternoon)
- **Tuesday Sep 29 — Main Conference Day 2**
  - Keynote 2 (TBA)
  - Main proceedings oral sessions
  - Poster Session 2
  - MICCAI Society business meeting (typical)
- **Wednesday Sep 30 — Main Conference Day 3**
  - Keynote 3 (TBA)
  - Main proceedings oral sessions
  - Poster Session 3
  - **Closing plenary + Awards** (Best Paper, Young Scientist, MICCAI Fellow inductions)
- **Thursday Oct 1 — Satellite Events Day 2**
  - **Workshops** day 2 (remaining workshops)
  - **CliniCAI / Clinical Day** (often lands here; clinician-facing)
  - **Challenge result sessions** (final leaderboards, prize ceremonies)
  - Wrap-up

## Anticipated cancer-relevant work — watch list

**Forward-looking; subject to final-accept list Jun 12 and workshop-program publication. Conservative — only items with prior-year precedent or already-public 2026 signals.**

### Pathology foundation models (COMPAY workshop + main proceedings)

The pathology-FM cycle (CHIEF, Prov-GigaPath, UNI / UNI2) has been a dominant axis at MICCAI 2023–2025 and is highly likely to extend. Watch:

- **Updated tile-encoder pretraining** — larger curated WSI cohorts, multi-magnification, multi-stain. The Mahmood Lab (UNI), Microsoft Research / Providence (Prov-GigaPath), and the broader DINOv2 / iBOT pathology adaptations have all been incrementally publishing methods papers at MICCAI.
- **Slide-level aggregation methods** — TITAN, PRISM, ABMIL extensions, attention-MIL variants. The "tile-to-slide" step is the active methodology frontier post-FM.
- **Pathology-radiology multimodal** — bridges between pathology FMs and radiology FMs (Merlin-style). The 2026 cycle is when these typically debut.
- **Multimodal pathology-text** — PathChat / pathology VLM extensions; report generation from WSI.
- **Hyperion / spatial-omics integration** — pathology FM features feeding into spatial transcriptomics / spatial proteomics analysis.

### Radiology FMs (main proceedings + DGM4MICCAI workshop)

- **RadFM / Med-PaLM-M / MAIRA-class** updates — report generation, multimodal radiology VLMs
- **MedSAM / SegVol** evolutions — promptable medical segmentation, follow-ups to the 2024–2025 cohort
- **CT / MR foundation models** — self-supervised pretraining on large unlabeled scan cohorts
- **Diffusion priors for medical reconstruction** — undersampled MR, low-dose CT denoising

### Generative medical imaging (DGM4MICCAI workshop)

- **Synthetic-data fairness** — diffusion-generated data for rare-disease / underrepresented-population augmentation (echoes the 2026 Call for Papers' equity emphasis)
- **Counterfactual medical imaging** — disease / no-disease counterfactuals for explainability
- **Cross-modality synthesis** — CT-from-MR, PET-from-CT for surrogate imaging when one modality is unavailable

### Radiotherapy planning / IGRT (main proceedings, occasional workshops)

- **Auto-contouring** — deep-learning OAR (organs-at-risk) and GTV (gross tumor volume) segmentation for treatment planning
- **Dose prediction** — image-to-dose models, especially for proton therapy
- **Adaptive radiotherapy** — daily / weekly replanning driven by CBCT or MR-linac imaging

### Oncology challenge slate (Thursday Oct 1 results)

Subject to 2026 challenge acceptance (deadline Jan 9, full results announced Mar 13). Likely recurring:

- **BraTS 2026** — brain tumor segmentation; expected sub-tasks Adult Glioma, Meningioma, Pediatrics, BraTS-Africa, BraTS-MET (metastases), Inpainting
- **HECKTOR 2026** — head-and-neck PET/CT tumor segmentation + outcome prediction
- **KiTS 2026** — kidney tumor segmentation / surgical AI (if running)
- **AutoPET 2026** — whole-body FDG PET/CT lesion segmentation; the 2024–2025 cycle introduced PSMA tracer
- **PANORAMA** — pancreatic cancer detection on CT (PDAC)
- **ESR oncology track (new 2026)** — three flagged proposals
  - Detection / quantification of colorectal liver metastases on CT
  - AI-based assessment of PET imaging for oncology
  - Automated RECIST assessment on baseline and follow-up Thorax-Abdomen CT
  - Top 3 winners co-present at ECR 2027

### Surgical AI (CAI half — main proceedings + workshops)

- **Surgical phase recognition** — workflow understanding during oncology surgery (colorectal, hepatobiliary, gynecologic)
- **Endoscopic / laparoscopic AI** — polyp detection, tumor margin assessment
- **Intra-op imaging fusion** — pre-op planning to intra-op navigation (ultrasound, fluoroscopy)

## Cross-link map (AACR / RSNA / ISMB / NeurIPS)

### To AACR 2026

| AACR dossier | MICCAI 2026 cross-link |
|---|---|
| [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) — pathology FM, Mahmood Lab | Watch COMPAY 2026 workshop + main-proceedings for tile-encoder updates, slide-aggregation methods, multimodal extensions |
| [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) — pathology FM, MSR / Providence | Watch main proceedings for any GigaPath-v2 or downstream-task papers; Microsoft/Providence are MICCAI regulars |
| [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md) — pathology FM, Mahmood Lab | Watch main proceedings for UNI2 or task-specific UNI adapters |
| AACR bioinfo-tools index | Any new pathology FM at MICCAI 2026 → mirror into AACR vault as a dossier if it's clinically referenced |

### To RSNA 2026

The MICCAI → RSNA pipeline runs Sep 27 → Nov 29 (8 weeks). Many MICCAI 2026 methods papers will resurface at RSNA 2026 as clinical-deployment readouts. Tracking:

- **Imaging FMs in clinical pipelines** — MedSAM, SegVol, RadFM-class deployments
- **Screening AI** — lung-screening AI (NLST / NELSON-derivative), mammography AI-CAD, prostate MRI AI
- **Vendor partnerships** — any MICCAI tool that lands a commercial deployment shows up in RSNA's AI Showcase
- **Radiology-pathology bridges** — Merlin-style cross-modality FMs span both vaults

### To ISMB 2026 / RECOMB 2026

Less direct, but relevant for:

- **Computational pathology with multi-omics** — pathology FM features cross-referenced with spatial transcriptomics / scRNA-seq (overlaps ISMB MLCSB COSI)
- **Foundation models theory** — self-supervised pretraining methods cross-cited between MICCAI and ISMB MLCSB / NeurIPS

### To NeurIPS 2026

- **General ML methods** (diffusion, transformers, MoE) feed MICCAI medical-imaging applications. Watch DGM4MICCAI workshop especially.
- **Medical-imaging tracks at NeurIPS** — increasingly significant; cross-citations both ways.

## Sources

- [MICCAI 2026 home](https://conferences.miccai.org/2026)
- [MICCAI 2026 Important Dates](https://conferences.miccai.org/2026/en/IMPORTANT-DATES.html)
- [MICCAI 2026 Call for Papers](https://conferences.miccai.org/2026/en/CALL-FOR-PAPERS.html)
- [MICCAI 2026 Call for Workshops](https://conferences.miccai.org/2026/en/CALL-FOR-WORKSHOPS.html)
- [MICCAI 2026 Call for Challenges](https://conferences.miccai.org/2026/en/CALL-FOR-CHALLENGES.html)
- [MICCAI Society challenges registry](https://miccai.org/index.php/special-interest-groups/challenges/miccai-registered-challenges/)
- [MICCAI Society home](https://miccai.org/)
- [Springer LNCS](https://www.springer.com/series/558)
- [MICCAI 2025 Daejeon (prior-year shape reference)](https://conferences.miccai.org/2025/en/)
- [MICCAI 2026 Foundation Model for Ultrasound Biometry challenge (Springer Communities)](https://communities.springernature.com/posts/miccai-2026-challenge-on-foundation-model-for-ultrasound-biometry)

## Working notes

- The workshop-date confusion in some web copy ("Oct 4 and Oct 8") is a stale artifact from the original Abu Dhabi schedule; under the relocated Strasbourg schedule, workshops/satellites are on Sep 27 and Oct 1, with main proceedings Sep 28–30. To be reconfirmed when the program-overview page populates.
- Keynote speakers not yet announced as of T-20 weeks (May 11, 2026). Typical announcement window is T-12 to T-8 weeks.
- The early-accept track (notifications May 7) is a MICCAI mechanism that fast-tracks a subset of clearly-strong submissions; final-decision track for the bulk lands Jun 12.
- Bulk extraction of tool pages should target the **week after Oct 1** — proceedings DOIs are live, GitHub READMEs have post-meeting updates, and the challenge leaderboards are final.
