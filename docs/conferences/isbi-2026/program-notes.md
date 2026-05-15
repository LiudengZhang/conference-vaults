# ISBI 2026 — Program Notes (post-meeting prep)

**Status:** Scaffold (post-meeting) — meeting concluded April 11, 2026. This page is the **candidate shortlist** for retrospective bulk extraction into [`tools/`](tools/index.md) once IEEE Xplore indexes the 2026 proceedings (expected early May 2026, ~T+3 weeks). Companion to [`index.md`](index.md).

## Verified meeting metadata

- **Dates:** Wednesday April 8 – Saturday April 11, 2026 (4 days)
- **Venue:** ExCeL London, London, UK
- **Scale:** ~1,500 attendees
- **Theme:** "Translation to Impact!"
- **Tagline:** "Where machines learn to see the body — and humans learn what comes next"
- **Organizers:** Joint IEEE Signal Processing Society (SPS) + IEEE Engineering in Medicine and Biology Society (EMBS)
- **Proceedings:** IEEE Xplore (4-page peer-reviewed conference papers); subset extended to **IEEE Transactions on Biomedical Engineering Special Section** ("Selected Topics from ISBI 2026") — ~10 invited expanded papers
- **Next edition:** ISBI 2027 — Lausanne, Switzerland

## Why we wait for retrospective extraction (vs live coverage)

ISBI 2026 ran April 8–11, **overlapping the tail end of AACR 2026** (Apr 17–22 starts ~1 week after ISBI ends, but planning overlap was significant in March–April 2026). Live coverage was deprioritized in favor of AACR + RECOMB + ISMB live builds. ISBI's compact size and post-meeting IEEE Xplore indexing pattern (proceedings drop ~3–4 weeks after the meeting) makes a retrospective extraction tractable and complete — no advantage to a pre-meeting scaffold.

## Cancer-relevance filter (the load-bearing axis)

Of ISBI 2026's ~400–600 papers, the cancer-relevant subset for this vault is concentrated in **four anchor clusters** (in descending priority):

### 1. Pathology / cytology FMs — anchored on the Faisal Mahmood keynote (Harvard Medical School)

Mahmood is the lead author / corresponding author on the AACR-corpus pathology FMs [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) and [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md). The ISBI 2026 keynote is the **likely venue for any methods-side update** to that line (UNI2, new tile-encoder pretraining recipe, slide-level aggregation variant). Watch the Mahmood Lab GitHub and HuggingFace through Q2 2026 for the actual artifact drop — the keynote announcement is the signal but the code release is the citable hook.

**Crosswalk:** any new model goes either (a) as an in-place update to the AACR dossier (incremental work) or (b) as a new ISBI tool page (fundamentally new model). Mirror with the MICCAI 2026 (Sep 27–Oct 1) cousin paper when it lands.

### 2. RIVA Cervical Cytology Challenge — direct cancer-relevance

- **Modality:** Pap smear cytology (a.k.a. liquid-based cytology slides for cervical cancer precancer detection)
- **Dataset:** 959 fields of view, 26,158 nucleus-level annotations across Bethesda categories
- **Tasks:** Nuclei detection + multi-class cell classification (with expert-agreement evaluation as a fairness/inter-rater check)
- **Anchor:** Direct line to AACR cancer-prevention axis; intersects with [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) / [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md) as a downstream evaluation use case
- **Tool extraction:** Top-1 (top-3 if code released) — one page per winning model; the challenge itself is summarized here, not as a separate tool page

### 3. WBCBench2026 — direct cancer-relevance (hematopathology)

- **Modality:** Peripheral-blood / bone-marrow smear hematopathology
- **Tasks:** Robust white blood cell classification, with severe class imbalance and fine-grained morphological discrimination — leukemia diagnosis axis
- **Evaluation:** Patient-level separation enforced to prevent information leakage in test sets (a methodological best-practice flag worth highlighting)
- **Anchor:** Connects to AACR / ASH hematologic-malignancies dossiers; ASH 2026 (Dec 12–15) clinical-deployment counterpart possible
- **Tool extraction:** Top-1 winning model + any baseline-beating workshop paper

### 4. MPI Low Concentration Reconstruction Challenge — direct oncology imaging translation

- **Modality:** Magnetic Particle Imaging (MPI), specifically field-free-line MPI (FFL-MPI) setups
- **Tasks:** Reconstruction at low tracer concentrations — the bottleneck for clinical translation, with **explicit oncology and cardiovascular imaging applications** flagged in the challenge description
- **Anchor:** ISBI is the home venue for MPI methods (MICCAI underweights this modality). MPI is an emerging molecular-imaging modality with potential for tumor-specific tracer visualization
- **Tool extraction:** Top-1 winning reconstruction algorithm + any methods-paper introducing a new MPI deep-learning prior

### 5. (Secondary) Foundation models for medical imaging — FAIBI workshop + "Exploring FM in Medical Image Analysis" workshop

Both 2026 workshops ran on the closing day (Sat Apr 11). FAIBI 2nd edition co-organized by **Jia Wu (MD Anderson Cancer Center)** — direct cancer-center authorship signal. Watch for: any oncology-imaging FM update, any pathology FM evaluation paper, any radiology FM with a cancer subgroup analysis.

## Keynote roster — full annotation

| Speaker | Affiliation | Likely talk axis | Cancer-relevance | Cross-vault link |
|---|---|---|---|---|
| **Faisal Mahmood** | Harvard Medical School / Brigham & Women's | Pathology FMs; multimodal pathology agents | **Direct** — CHIEF / UNI line | [AACR pathology FMs](../aacr-2026/topics/bioinfo-tools/) |
| **Polina Golland** | MIT CSAIL | MRI reconstruction; image registration; statistical methods | Indirect — methods feed cancer MRI workflows | [MICCAI 2026](../miccai-2026/index.md) |
| **Bram van Ginneken** | Radboud University Medical Center | Diagnostic radiology AI (lung CT, mammography); Grand Challenge platform; clinical translation | **Direct** — lung cancer screening, breast cancer mammography AI | [RSNA 2026](../rsna-2026/index.md) |
| **Mauricio Reyes** | University of Bern | Trustworthy / explainable medical AI; long-time BraTS organizer | Indirect — brain tumor segmentation legacy | [MICCAI 2026 BraTS](../miccai-2026/index.md) |
| **Greg Slabaugh** | Queen Mary University of London | Medical computer vision; local host | Indirect — general medical AI | — |

## Challenge slate — full annotation

| # | Challenge | Modality | Cancer-direct? | Extract? |
|---|---|---|---|---|
| 1 | Foundation Model Challenge for Ultrasound Image Analysis | Ultrasound (general / fetal-maternal) | No | Only if winner releases a generalist medical-US FM |
| 2 | CXR-LT 2026 | Chest X-ray (long-tail, multi-label) | Indirect (lung cancer in long tail) | If winner addresses oncology-specific subset |
| 3 | Low Concentration Reconstruction in MPI | Magnetic Particle Imaging | **Yes** — explicit oncology translation | **Yes** — top-1 + any methods paper |
| 4 | CSV 2026 — Carotid Plaque Segmentation | Carotid ultrasound | No (stroke prevention) | No |
| 5 | Multi-modal Ulcerative Colitis Grading in Endoscopy | Colonoscopy video | Indirect (colon cancer screening axis) | Only if model generalizes to neoplasia detection |
| 6 | FETUS 2026 | Fetal echocardiography | No | No |
| 7 | **RIVA Cervical Cytology** | Pap smear cytology | **Yes** — cervical precancer | **Yes** — top-1 + top-3 if code released |
| 8 | **WBCBench2026** | Hematopathology (WBC) | **Yes** — leukemia | **Yes** — top-1 + any baseline-beating paper |

## Workshop slate — full annotation

| Workshop | Day | Cancer-direct? | Extract pages? |
|---|---|---|---|
| Medical Video AI Assessment + UQ | Thu Apr 9 | Indirect (endoscopy generalizes) | Sample only if a named tool released |
| Pediatric Brain Data Analysis | Thu Apr 9 | Indirect (pediatric brain tumors possible) | Sample only |
| Large Models Meet Surgical Data Science | Fri Apr 10 AM | Indirect (surgical-oncology axis) | Sample only |
| **Exploring FM in Medical Image Analysis** | Fri Apr 10 PM | **Yes** — explicit FM axis | Yes — extract named-tool papers |
| POCUS-AI | Sat Apr 11 AM | No | No |
| **FAIBI 2nd ed.** (co-org Jia Wu, MD Anderson) | Sat Apr 11 PM | **Yes** — cancer-center co-organizer | Yes — extract named-tool papers |

## Special-session slate — full annotation

| Special Session | Day | Featured | Extract? |
|---|---|---|---|
| Preparing Large-Scale Medical Imaging Data for FM Development | Thu Apr 9 PM | Martin Willemink (Segmed) | If named data-prep tool released |
| Safety and Reliability in Medical Imaging | Thu Apr 9 PM | Gori (Télécom Paris), Zuluaga (EURECOM) | If named uncertainty / safety tool released |
| Digital Twins and Multi-Omics Integration | Fri Apr 10 AM | Valentina Giannini (Turin) | Yes — overlaps AACR multimodal axis |
| Privacy-Aware Federated Learning in Healthcare | Fri Apr 10 AM | Xiaofeng Liu (Yale) | If named federated framework released |

## Bulk-extraction plan

1. **Wait for IEEE Xplore indexing** (~T+3–4 weeks, early–mid May 2026) — pull the conference paper DOI list. Filter by title/abstract keywords: *pathology*, *cytology*, *cancer*, *tumor*, *oncology*, *leukemia*, *lymphoma*, *carcinoma*, *MRI reconstruction* (selected papers only), *MPI*, *foundation model*, *multiple instance learning*, *whole slide*, *Pap smear*, *bone marrow*, *mammography*.
2. **Cross-check against the 4 anchor clusters** above. Each cluster yields 2–8 candidate tool pages.
3. **Verify code/weights availability** for each candidate. Skip papers with no released artifact (ISBI 4-page papers without code are weak tool-page candidates).
4. **Stub tool pages** following [`tools/index.md`](tools/index.md) template. Populate the index table.
5. **Cross-link to MICCAI 2026 cousin pages** as the September meeting accept-list (already public for early-accept May 7) reveals same-lab follow-ups.
6. **Track TBME Special Section** invitations through Q3 2026; update tool pages with the TBME DOI as the extended version-of-record becomes available.

## Estimated yield

~10–25 tool pages after the filter. Distribution estimate:

- 3–5 from RIVA + WBCBench2026 + MPI challenges (winners + close runners-up)
- 2–4 from the Mahmood keynote axis (pathology FM updates, if a new artifact drops)
- 3–7 from FAIBI + Exploring-FM-in-Medical-Image-Analysis workshops (named-tool papers)
- 2–5 from main-proceedings oncology-imaging papers (segmentation / MRI / mammography / pathology)
- 0–3 from special-session-announced tools (digital twins, federated learning frameworks)

## Cross-vault dependencies

- **AACR 2026** ([dossier index](../aacr-2026/topics/bioinfo-tools/)) — Mahmood keynote work crosswalks here first. Update CHIEF / UNI / GigaPath dossiers in-place for incremental work.
- **MICCAI 2026** ([index](../miccai-2026/index.md)) — same author pool largely; ISBI April → MICCAI September cousin pairing is the rule. Wait for the MICCAI early-accept list (already posted May 7, 2026) and the final-accept list (Jun 12) to identify cousin papers.
- **RSNA 2026** ([index](../rsna-2026/index.md)) — Bram van Ginneken keynote work crosswalks to RSNA's clinical-deployment side. Lung CT and mammography AI specifically.
- **ASH 2026** (Dec 12–15) — WBCBench2026 leukemia-classification winners may resurface as ASH clinical-deployment readouts.
- **Conferences timeline** ([timeline.md](../../timeline.md)) — ISBI sits in early April, ~1 week before AACR.

## Sources

- [ISBI 2026 home](https://biomedicalimaging.org/2026/)
- [ISBI 2026 Challenges](https://biomedicalimaging.org/2026/challenges/)
- [ISBI 2026 Special Sessions](https://biomedicalimaging.org/2026/special-sessions/)
- [ISBI 2026 Workshops](https://biomedicalimaging.org/2026/workshops-2/)
- [ISBI 2026 Tutorials](https://biomedicalimaging.org/2026/tutorials-2/)
- [IEEE TBME Special Section on ISBI 2026](https://www.embs.org/tbme/research-highlights/isbi-2026/)
- [IEEE SPS newsletter — "ISBI 2026 in London"](https://signalprocessingsociety.org/newsletter/2025/11/isbi-2026-london-where-machines-learn-see-body-and-humans-learn-what-comes-next)
- [ISBI 2026 Call for Papers PDF](https://confcats-event-sessions.s3.us-east-1.amazonaws.com/isbi26/uploads/isbi26-cfp_web-03.pdf)
