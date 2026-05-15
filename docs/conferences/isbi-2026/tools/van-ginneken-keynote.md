# Diagnostic Radiology AI — Bram van Ginneken (Radboud)

**ISBI 2026 plenary keynote on diagnostic radiology AI — lung CT, mammography, and the Grand Challenge platform — directly bridging into the RSNA 2026 clinical-deployment axis with concrete cancer-screening applications.**

- **Speaker(s) / Authors:** Bram van Ginneken
- **Affiliation(s):** Radboud University Medical Center (Diagnostic Image Analysis Group, Nijmegen)
- **Anchor type:** keynote
- **Track / day:** ISBI 2026 main plenary (day TBD — Thu Apr 9 or Fri Apr 10)
- **IEEE Xplore:** TBD (keynote — no Xplore paper)
- **Status:** post-meeting

## What it does

Van Ginneken's keynote covers the Radboud DIAG group's two-decade-long line of work on diagnostic radiology AI, anchored on lung CT (nodule detection, COPD, lung cancer screening) and mammography (breast cancer detection AI, the LUNA / DREAM challenge legacy). The talk is the most cancer-direct keynote on the ISBI 2026 slate after Mahmood — both lung cancer screening and breast cancer mammography AI are core RSNA / clinical-deployment topics.

## How it works / methodology

The DIAG-group pattern emphasizes (a) large-scale curated datasets (LIDC-IDRI, NLST-derived, OPTIMAM mammography), (b) benchmark challenges hosted via the Grand Challenge platform (grand-challenge.org — van Ginneken co-founded), (c) clinical-validation studies with reader-study designs that compare AI to radiologist performance, (d) regulatory-facing translation toward CE-mark / FDA-cleared products. Methods themselves are typically CNN / transformer hybrids tuned for clinical-deployment metrics (sensitivity at fixed FP rate, AUC vs reader panels).

## Headline benchmarks

TBD — keynote-level synthesis. Anchor numbers from the DIAG-group published line: lung nodule detection on LIDC-IDRI (FROC sensitivity), mammography AI vs reader-panel AUC. Specific ISBI 2026 keynote deltas not in program-notes.

## How it works

**Core idea.** Diagnostic radiology AI succeeds clinically when it is built on large curated public datasets, benchmarked against radiologist readers via challenge platforms, and validated for the specific operating points clinical workflows demand (sensitivity at a fixed false-positive rate, not just AUC). Van Ginneken's two-decade DIAG-group line operationalizes this end-to-end.

**Inputs / outputs.** Lung CT inputs: full chest CT volumes (typically 0.5–1.0mm slice thickness); outputs: nodule candidate locations with malignancy probabilities, plus lung-cancer-screening LDCT triage scores. Mammography inputs: 4-view digital mammograms (CC + MLO, bilateral) and/or DBT volumes; outputs: lesion locations, BI-RADS-aligned probability scores, and case-level malignancy probability.

**Key innovation.** The Grand Challenge platform (grand-challenge.org — van Ginneken co-founded) institutionalized fair reader-study-grade comparison across teams: hidden test sets, standardized evaluation, multi-reader multi-case (MRMC) study designs, and regulatory-grade audit trails. The methodological gain isn't a single architecture — it's an infrastructure layer that made medical AI benchmarking reproducible.

**Parameters.** Tool-specific; the DIAG-group line spans 3D CNNs for nodule detection (tens of millions of parameters typical), DenseNet / EfficientNet-class mammography classifiers, and increasingly transformer hybrids. Operating-point selection is parameter-equivalent in importance to architecture.

**Canonical example.** Lung-nodule CAD on LIDC-IDRI: sliding-window 3D CNN over a chest CT volume produces candidate locations, false-positive reduction stage filters, FROC sensitivity reported at fixed FP-per-scan rates (1, 4, 8 FP/scan). Mammography canonical pipeline: per-view CNN feature maps fused across CC + MLO via attention, case-level malignancy score benchmarked against reader-panel AUC on MRMC datasets like OPTIMAM.

## Where it fits in the corpus

- **AACR 2026:** indirect — lung cancer screening and breast cancer prevention axes overlap with AACR clinical sessions
- **MICCAI 2026:** strong sibling — DIAG-group work appears across MICCAI main proceedings and challenge tracks
- **RSNA 2026:** **direct crosswalk** — Grand Challenge platform, lung CT and mammography AI are core RSNA deployment topics; van Ginneken keynote bridges ISBI methods → RSNA clinical translation
- **CVPR 2026:** indirect — architecture upstream

## Notes

Of the five ISBI 2026 keynotes, van Ginneken's is second only to Mahmood's in direct cancer-screening relevance (lung + breast). The Grand Challenge platform itself is a vault-relevant infrastructure asset — many of the challenges referenced across the MICCAI / ISBI tools index are hosted there. Keynote does not yield a separate tool page; any named tool announced in the talk would warrant either an RSNA tool entry (clinical deployment) or a MICCAI cousin-paper entry.
