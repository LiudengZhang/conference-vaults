# ISBI 2026

**23rd IEEE International Symposium on Biomedical Imaging** — ExCeL London, London, UK · April 8–11, 2026. ~1,500 attendees. Joint initiative of the [IEEE Signal Processing Society (SPS)](https://signalprocessingsociety.org/) and the [IEEE Engineering in Medicine and Biology Society (EMBS)](https://www.embs.org/). Peer-reviewed proceedings published in **IEEE Xplore** (4-page papers) within ~4 weeks of the meeting. Theme: **"Translation to Impact!"**

> **Status:** Scaffold (post-meeting) — ready for retrospective bulk extraction. Meeting concluded April 11, 2026; the official program, keynote slate, special sessions, workshops, tutorials, and challenge roster are public. IEEE Xplore proceedings are expected to post by early May 2026. This vault stands up the per-tool template and program-notes prep page now so the post-meeting extraction can run against a stable schema once (a) the IEEE Xplore DOIs are indexed and (b) challenge-winner code releases land through May–June. **A proposed IEEE TBME Special Section** ("Selected Topics from ISBI 2026") will publish ~10 expanded papers from the most outstanding ISBI 2026 contributions — those become primary citation anchors for tool entries.

## Why this is in the vault

ISBI is the **signal-processing-and-algorithms counterpart to [MICCAI 2026](../miccai-2026/index.md)** in the medical-imaging-AI axis — smaller scale (~1,500 vs MICCAI's ~3,000), shorter-format papers (4-page IEEE conference papers vs MICCAI's full LNCS chapters), broader modality coverage (heavy on MRI reconstruction, microscopy, ultrasound, and signal-side methods that MICCAI underweights), and an explicit IEEE SPS / EMBS membership. The convergence points with the cancer-research axis:

- **Pathology and cytology AI.** Cancer-relevant ISBI 2026 work concentrates in cytology (RIVA Cervical Cytology Challenge — Pap smear precancer detection with nucleus-level annotations) and hematopathology (WBCBench2026 — leukemia diagnosis via white blood cell classification). These pair with [AACR 2026](../aacr-2026/index.md) pathology-FM dossiers ([CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md), [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md), [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md)) — Faisal Mahmood (CHIEF / UNI lead, Harvard Medical School) delivered an ISBI 2026 keynote.
- **Radiation oncology and treatment-response imaging.** ISBI's "Translation to Impact" theme foregrounded predictive treatment response modeling and oncology-imaging biomarkers — feeds the [RSNA 2026](../rsna-2026/index.md) clinical-deployment axis.
- **Foundation models for medical imaging.** The 2nd FAIBI workshop (Foundation AI models in Biomedical Imaging) and the "Exploring Foundation Models in Medical Image Analysis" workshop both ran at ISBI 2026 — same author pool as MICCAI's COMPAY / DGM4MICCAI and CVPR's FMV / MMFM-BIOMED.
- **Ultrasound and low-field imaging.** ISBI 2026 ran an ultrasound foundation-model challenge (50,000+ annotated images) and a POCUS-AI workshop — modalities underrepresented at MICCAI / CVPR.
- **MRI reconstruction.** Keynote-level emphasis on rapid MRI reconstruction (a long-standing ISBI strength via Polina Golland, MIT, and the broader inverse-problems community) — methods that downstream into cancer-specific MRI workflows.
- **Magnetic Particle Imaging (MPI).** ISBI is the home venue for MPI methods — the 2026 Low Concentration Reconstruction Challenge explicitly targeted oncology and cardiovascular clinical translation.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **ISBI 2026 home** | venue, dates, program nav | [biomedicalimaging.org/2026](https://biomedicalimaging.org/2026/) |
| **Program / Full Program** | session-by-session schedule | [biomedicalimaging.org/2026/program](https://biomedicalimaging.org/2026/program/) |
| **Keynote slate** | 5 confirmed plenaries | Faisal Mahmood (Harvard), Polina Golland (MIT), Bram van Ginneken (Radboud), Mauricio Reyes (Bern), Greg Slabaugh (QMUL) — all delivered |
| **Special sessions** | 4 ran (2 cancelled) | foundation-model data prep · safety/reliability · digital twins + multi-omics · privacy-aware federated learning |
| **Workshops** | 6 confirmed | Medical Video AI · Pediatric Brain Data · Large Models for Surgical Data · Foundation Models in Medical Image Analysis · POCUS-AI · FAIBI (2nd ed.) |
| **Tutorials** | 5 ran (1 cancelled) | Generative modelling (flows/diffusions) · multiresolution analysis · sequence diagrams → MR images · covariance neural networks · modern data cleaning |
| **Challenges** | 8 confirmed | see below — cancer-relevant: RIVA (cervical cytology), WBCBench2026 (leukemia), MPI Low Concentration (oncology imaging) |
| **IEEE Xplore proceedings** | peer-reviewed 4-page papers + DOIs | accepted papers indexed in IEEE Xplore; usually appears within ~4 weeks post-meeting |
| **IEEE TBME Special Section (proposed)** | top ~10 ISBI 2026 contributions as full TBME papers | [embs.org/tbme/research-highlights/isbi-2026](https://www.embs.org/tbme/research-highlights/isbi-2026/) — extended versions are the durable citation anchor |
| **Call for Papers PDF** | scope, topics, formatting | [isbi26 CfP PDF](https://confcats-event-sessions.s3.us-east-1.amazonaws.com/isbi26/uploads/isbi26-cfp_web-03.pdf) |
| **arXiv mirrors** | preprints flagged "to appear in ISBI 2026" | partial coverage — ISBI authors mirror less consistently than MICCAI / CVPR but coverage is rising |
| **Social / press** | reactions | [@IeeeIsbi on X](https://x.com/IeeeIsbi); IEEE SPS newsletter writeup [here](https://signalprocessingsociety.org/newsletter/2025/11/isbi-2026-london-where-machines-learn-see-body-and-humans-learn-what-comes-next) |
| **Clinical Day** | clinician-facing translational track | runs alongside main proceedings |

## Program shape

ISBI 2026 ran **Wednesday April 8 through Saturday April 11**, four days at ExCeL London.

- **Wednesday April 8** — Tutorials day (5 full- and half-day tutorials), workshop / satellite kickoff.
- **Thursday April 9** — Main proceedings + workshops: keynotes, oral sessions, poster sessions; "Preparing Large-Scale Medical Imaging Data for Foundation Model Development" (Martin Willemink, Segmed) and "Safety and Reliability in Medical Imaging" special sessions ran this day. Medical Video AI workshop and Pediatric Brain Data Analysis workshop ran full-day.
- **Friday April 10** — Main proceedings continued + workshops: "Digital Twins and Multi-Omics Integration" and "Privacy-Aware Federated Learning in Healthcare" special sessions; "Large Models Meet Surgical Data Science" (AM) and "Exploring Foundation Models in Medical Image Analysis" (PM) workshops.
- **Saturday April 11** — Satellite day 2: POCUS-AI workshop (AM), FAIBI 2nd edition workshop (PM), challenge result sessions, closing.

### Keynotes (5 confirmed)

| Speaker | Affiliation | Likely focus (oncology / FM crosswalk) |
|---|---|---|
| **Faisal Mahmood** | Harvard Medical School / Brigham & Women's | Pathology FMs — CHIEF, UNI, multimodal pathology agents; direct AACR pathology-FM dossier crosswalk |
| **Polina Golland** | MIT CSAIL | MRI reconstruction, image registration, statistical methods for medical imaging |
| **Bram van Ginneken** | Radboud University Medical Center | Diagnostic radiology AI (lung CT, mammography); Grand Challenge platform; clinical translation |
| **Mauricio Reyes** | University of Bern | Trustworthy / explainable medical AI; BraTS history |
| **Greg Slabaugh** | Queen Mary University of London | Medical computer vision; local host |

### Challenges (8 confirmed, post-meeting)

| Challenge | Modality | Cancer-relevance | Dataset size |
|---|---|---|---|
| **Foundation Model Challenge for Ultrasound Image Analysis** | Ultrasound | indirect (general FM) | 50,000+ annotated images |
| **CXR-LT 2026** | Chest X-ray | indirect (long-tail dx incl. lung CA) | 300,000+ X-rays (MIMIC + MIDRC) |
| **Low Concentration Reconstruction Challenge in MPI** | Magnetic Particle Imaging | **direct** — explicit oncology translation goal | FFL-MPI |
| **CSV 2026** | Carotid ultrasound | indirect (stroke prevention) | 1,500 paired transverse-longitudinal, 7 hospitals |
| **Multi-modal Ulcerative Colitis Grading in Endoscopy** | Endoscopy video | indirect (colon cancer screening axis) | multi-center |
| **FETUS 2026** | Fetal ultrasound | not cancer | — |
| **RIVA Cervical Cytology Challenge** | Pap smear cytology | **direct** — cervical cancer precancer detection | 959 FOVs, 26,158 nucleus-level annotations |
| **WBCBench2026** | Hematopathology | **direct** — leukemia diagnosis | patient-level held-out |

### Workshops (6)

- **Medical Video AI Assessment and Uncertainty Quantification: Bridging Research and Practice** — Yang (FDA) / Ngo Din (Cosmo IMD) / Hüllermeier (LMU); Thu Apr 9, full day.
- **Pediatric Brain Data Analysis** — Grant / Ou / Bao (Harvard / BCH); Thu Apr 9, full day.
- **Large Models Meet Surgical Data Science** — Ali (Leeds) / Godau (DKFZ) / Lam (Imperial) / Shi (Tongji) / Bhattarai (Aberdeen); Fri Apr 10 AM.
- **Exploring Foundation Models in Medical Image Analysis: Applications, Challenges, and Uncertainties** — Gu (Tohoku) / Chen (Sheffield) / Yang (Emory/GT) / Zheng (Liverpool) / Zhou (UCL) / Shen (ShanghaiTech); Fri Apr 10 PM.
- **POCUS–AI: Point-of-care Ultrasound Powered by AI** — Brattain (UCF) / Panicker (NTU Singapore) / Hareendranathan (Alberta); Sat Apr 11 AM.
- **FAIBI 2nd ed. — Foundation AI models in Biomedical Imaging** — Ali (Stirling) / Qureshi (Salim Habib) / Rekik (Imperial) / **Wu (MD Anderson Cancer Center)** / Bilal (Birmingham City); Sat Apr 11 PM.

### Special sessions (4 ran, 2 cancelled)

- **Preparing Large-Scale Medical Imaging Data for Foundation Model Development** — Martin J. Willemink (Segmed); Thu Apr 9 15:00–16:00.
- **Safety and Reliability in Medical Imaging** — Voiculescu (Oxford) / Pastore (Genoa); Gori (Télécom Paris) and Zuluaga (EURECOM) featured. Thu Apr 9 16:30–17:30.
- **Digital Twins and Multi-Omics Integration: Methodological Advances for Personalized Biomedical Modeling** — Giannini / Rosati / Nicoletti (Turin / Politecnico Turin); Fri Apr 10 8:00–9:00.
- **Privacy-Aware, Data-Efficient AI via Personalized Incremental and Federated Learning in Healthcare** — Mineo / Palazzo / Bellitto / Sorrenti / Proietto Salanitri / Spampinato (Catania); featured Xiaofeng Liu (Yale). Fri Apr 10 10:30–11:30.
- *Cancelled:* "NIH Session: Funding Opportunities and Grant Writing Tips"; "Data Crimes in Medical Imaging: Pitfalls, Biases, and Mitigation Strategies".

### Tutorials (5 ran)

- **Introduction to Generative Modelling with Flows and Diffusions** — Galassi (Rennes) / Roy / Solal (Sorbonne / Brain Institute) / Baghai-Wadji (UCT); includes AnoDDPM unsupervised brain-tumor detection lab. Wed Apr 8 full-day.
- **Customized Multiresolution Analysis and Learning Algorithms in Biomedical Imaging** — Baghai-Wadji (UCT); Wed Apr 8 full-day.
- **From Sequence Diagrams to Medical Images** — Huber / Neisser (Fraunhofer MEVIS); MR sequence + image formation via gammaSTAR. Wed Apr 8 AM.
- **Learning with Covariance Matrices: Foundations and Applications to Network Neuroscience** — Sihag (Albany) / Mateos (Rochester) / Isufi (TU Delft) / Ribeiro (Penn); coVariance Neural Networks (VNNs). Wed Apr 8 AM.
- **Modern Data Cleaning** — Gröger (Basel) / Lionetti (Lucerne) / Varela (City St George's / Imperial); Wed Apr 8 PM.
- *Cancelled:* BioMedPINNs (Physics-Informed Neural Networks).

## Organization

```
conferences/isbi-2026/
├── index.md             # this page
├── program-notes.md     # post-meeting prep: keynote roster, challenge winners shortlist,
│                        # cancer-relevant filter, AACR/MICCAI/RSNA crosslinks
└── tools/               # PRIMARY artifact — one entry per model / method / package
    └── index.md         # template + scope filter; populated post-IEEE-Xplore-indexing
```

No `digest/`, no `themes.md`, no `keynotes/` subdir — same scope-limited shape as [CVPR 2026](../cvpr-2026/index.md) and [ICML 2026](../icml-2026/index.md), narrower in scope than [MICCAI 2026](../miccai-2026/index.md). ISBI is a focused-scope conference; only `tools/` gets populated, filtered to the cancer-imaging / pathology / radiology-FM intersection.

## What's different from MICCAI 2026

- **Scale.** ISBI ~1,500 attendees vs MICCAI ~3,000. Single-track-heavy main program with parallel oral sessions; fewer workshops (6 vs 35–60); fewer challenges (8 vs 25–40).
- **Paper format.** 4-page IEEE conference papers vs MICCAI's full LNCS chapters. Methods are tighter, less reproducibility detail in-paper, often more concentrated demonstration of a single idea — code/data release is the load-bearing artifact, which is why we anchor tool entries to GitHub/HuggingFace and use IEEE Xplore DOIs as the citation hook.
- **Publisher.** IEEE Xplore (paywalled, but IEEE member access is common; arXiv mirroring rising but not universal) vs Springer LNCS.
- **Modality breadth.** ISBI overweights MRI reconstruction, microscopy, ultrasound, MPI — modalities where signal-processing methods dominate. MICCAI overweights segmentation, registration, pathology FMs, surgical AI.
- **Society backing.** Joint IEEE SPS + IEEE EMBS (engineering / signals society); MICCAI is its own society (MICCAI Society).
- **TBME pipeline.** Top ISBI papers can extend into a TBME Special Section — a clear journal-version-of-record path that MICCAI doesn't have (MICCAI's journal pair is *Medical Image Analysis*, less formal).

## Cross-vault links

- **[AACR 2026](../aacr-2026/index.md)** — Faisal Mahmood keynote bridges directly to the pathology-FM dossier chain:
  - [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) — pathology FM, Mahmood Lab
  - [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md) — pathology FM, Mahmood Lab
  - [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) — pathology FM, Microsoft / Providence
- **[MICCAI 2026](../miccai-2026/index.md)** — methodologically nearest sibling. Same author pool largely; the half-year offset (ISBI Apr → MICCAI Sep) means an ISBI 4-page paper often becomes a MICCAI full LNCS chapter. Cross-link tool entries.
- **[CVPR 2026](../cvpr-2026/index.md)** — architecture-feeder upstream. CVPR Jun → ISBI/MICCAI medical adaptation later in year.
- **[RSNA 2026](../rsna-2026/index.md)** — clinical-deployment / vendor side. Bram van Ginneken's Grand Challenge platform crosswalks here.
- **[Conferences timeline](../../timeline.md)** — ISBI position in the year: AACR Apr 17–22 (overlaps tail end with ISBI Apr 8–11).

## Sources

- [ISBI 2026 home (biomedicalimaging.org/2026)](https://biomedicalimaging.org/2026/)
- [ISBI 2026 Challenges](https://biomedicalimaging.org/2026/challenges/)
- [ISBI 2026 Special Sessions](https://biomedicalimaging.org/2026/special-sessions/)
- [ISBI 2026 Tutorials](https://biomedicalimaging.org/2026/tutorials-2/)
- [ISBI 2026 Workshops](https://biomedicalimaging.org/2026/workshops-2/)
- [ISBI 2026 Call for Papers PDF](https://confcats-event-sessions.s3.us-east-1.amazonaws.com/isbi26/uploads/isbi26-cfp_web-03.pdf)
- [IEEE SPS newsletter on ISBI 2026](https://signalprocessingsociety.org/newsletter/2025/11/isbi-2026-london-where-machines-learn-see-body-and-humans-learn-what-comes-next)
- [IEEE TBME Special Section on ISBI 2026](https://www.embs.org/tbme/research-highlights/isbi-2026/)
- [IEEE Signal Processing Society event page](https://signalprocessingsociety.org/events/2026-ieee-23rd-international-symposium-biomedical-imaging-isbi)
- [@IeeeIsbi on X](https://x.com/IeeeIsbi)
- [ISBI 2027 (Lausanne) — next edition](https://biomedicalimaging.org/)

## Next step

- **Now (May 11, 2026, T+1 month post-meeting):** stand up template + program-notes (this commit). Begin watching IEEE Xplore for the proceedings index drop (typically ~4 weeks post-meeting).
- **Late May / June 2026:** IEEE Xplore indexes the full 4-page paper set. Pull DOIs into stub pages for the cancer-relevant cluster (RIVA, WBCBench2026, MPI Low Concentration, Mahmood keynote-adjacent pathology FM work).
- **Summer 2026:** TBME Special Section authors invited; track the ~10 selected papers as primary tool-entry anchors. Challenge winner code releases land May–July.
- **Post-extraction (Q3 2026):** estimated ~10–25 tool entries — narrower than MICCAI (smaller paper count, scope filter) but deeper per-entry where the cancer-relevance is direct. Cross-check against AACR 2026 pathology-FM dossiers (Mahmood line) and the MICCAI 2026 early-accept list (Sep) for cousin pairings.
