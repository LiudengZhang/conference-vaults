# RIVA Cervical Cytology Challenge — ISBI 2026

**Pap smear precancer detection challenge with nucleus-level annotations across Bethesda categories — direct cervical-cancer-prevention axis with 959 FOVs and 26,158 nucleus annotations, scored on detection + multi-class classification with expert-agreement evaluation.**

- **Speaker(s) / Authors:** RIVA Challenge organizers (TBD — full author list pending challenge-results writeup)
- **Affiliation(s):** TBD (multi-institutional consortium typical for cytology challenges)
- **Anchor type:** challenge + dataset
- **Track / day:** ISBI 2026 challenge results session (Sat Apr 11)
- **IEEE Xplore:** TBD (challenge summary paper typically indexed within ~4 weeks post-meeting)
- **Status:** post-meeting

## What it does

RIVA targets the cervical-cancer prevention pipeline: from a Pap smear field of view, detect and classify cervical cells (nuclei) into Bethesda System categories (NILM, ASC-US, LSIL, HSIL, SCC, atypical glandular cells). The dataset — 959 fields of view with 26,158 nucleus-level annotations — is a direct downstream evaluation substrate for general pathology FMs and a focused training corpus for cytology-specific models.

## How it works / methodology

Two-task structure: (1) nuclei detection (bounding-box or centroid localization), (2) multi-class cell classification across Bethesda categories. Evaluation uses standard detection mAP plus class-balanced classification metrics, augmented with an **expert-agreement evaluation** — a fairness / inter-rater check that compares model predictions against multiple expert annotators to flag where model "errors" are within human inter-rater variance. Patient-level data splits prevent leakage.

## Headline benchmarks

- **Dataset:** 959 FOVs, 26,158 nucleus annotations, Bethesda category coverage
- Per-class F1, detection mAP, expert-agreement-normalized accuracy — specific top-1 winner numbers TBD pending challenge-results paper
- Top-1 and (if code released) top-3 winning models are candidate tool-page entries

## How it works

**Core idea.** RIVA frames cervical-cytology AI as a two-stage detection-then-classification task at the **nucleus** level (not cell or FOV level), with explicit Bethesda-system categorical structure and an expert-agreement-normalized fairness metric — a more clinically faithful evaluation than older slide-level cervical-AI benchmarks.

**Inputs / outputs.** Inputs: Pap smear fields of view (typically 1024x1024 to 2048x2048 pixel crops from whole-slide scans at 20x or 40x); outputs: per-nucleus bounding box / centroid + Bethesda-category class label (NILM, ASC-US, LSIL, HSIL, SCC, AGC).

**Key innovation.** Three load-bearing design choices: (1) nucleus-level annotation density (26,158 nuclei across 959 FOVs — roughly 27 nuclei per FOV, dense relative to other public cytology datasets), (2) Bethesda-faithful multi-class structure rather than binary normal/abnormal, (3) **expert-agreement evaluation** that compares model predictions against multiple annotators and penalizes only the model errors that fall outside human inter-rater variance — flagging where model confusion is genuinely human-disagreed.

**Parameters.** Submission-dependent; typical winning entries are likely Mask R-CNN / Cellpose / SAM-medical-adapted detectors paired with a tile-classifier head (ResNet / Swin / pathology-FM tile encoder). Per-class F1 + detection mAP are reported alongside expert-agreement-normalized accuracy.

**Canonical example.** Input a Pap-smear FOV containing ~30 cells of mixed Bethesda categories. The pipeline detects each nucleus, classifies into Bethesda category, and the leaderboard reports (a) detection mAP at IoU 0.5, (b) per-class F1 (NILM / ASC-US / LSIL / HSIL / SCC / AGC), (c) overall accuracy weighted by expert-agreement (predictions matching majority-expert vote score 1.0; predictions matching any expert vote score partial credit; predictions outside the expert-vote envelope score 0).

## Where it fits in the corpus

- **AACR 2026:** direct downstream-evaluation use case for [CHIEF](../../aacr-2026/topics/bioinfo-tools/tools/chief.md) and [UNI](../../aacr-2026/topics/bioinfo-tools/tools/uni.md) (zero-shot transfer to cytology); intersects with cancer-prevention / screening axis
- **MICCAI 2026:** likely COMPAY workshop cousin papers from challenge participants
- **RSNA 2026 / CVPR 2026:** less direct — cytology is pathology-side, but generalist medical-FM evaluations may include RIVA

## Notes

Cervical cytology is one of the rare cancer-screening modalities with a mature, label-rich, public benchmark — RIVA fills a gap MICCAI underweights. Expert-agreement evaluation is a methodologically interesting fairness flag worth highlighting. Watch challenge GitHub for dataset release license and winning-model code drops May–July 2026.
