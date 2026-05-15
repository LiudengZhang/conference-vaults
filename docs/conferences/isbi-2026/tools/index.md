# ISBI 2026 — Tools

ISBI 2026 delivered ~400–600 peer-reviewed 4-page papers (final IEEE Xplore count pending post-meeting indexing), 8 challenges with public datasets and leaderboards, 6 workshops, 4 special sessions, and 5 tutorials over four days at ExCeL London (April 8–11, 2026). The subset that yields tool pages is the intersection of (a) main-proceedings papers that release a named model / method / package with a maintained repo and a cancer or pathology / radiology FM tie-in, (b) workshop papers in the cancer-adjacent tracks (FAIBI, Exploring Foundation Models in Medical Image Analysis, Large Models Meet Surgical Data Science), (c) challenge winners with public code / weights from the cancer-relevant challenges (RIVA cervical cytology, WBCBench2026 leukemia, MPI Low Concentration with oncology translation), and (d) any update to an FM already in the AACR / RSNA / MICCAI corpus (CHIEF / UNI / Prov-GigaPath line via the Mahmood keynote).

> **Status:** Scaffold (post-meeting) — ready for retrospective bulk extraction. Per-tool format proposed here for review *before* bulk extraction runs once IEEE Xplore proceedings index lands (~early May 2026, T+3 weeks post-meeting). Estimated ~10–25 entries — narrower than [MICCAI 2026](../../miccai-2026/tools/index.md)'s ~25–50 because of the smaller paper count and tighter scope filter, similar in scope to [CVPR 2026](../../cvpr-2026/index.md)'s filtered medical-imaging subset.

## Per-tool entry template

Each tool gets its own page (`tools/<package-slug>.md`) following this structure. The shape mirrors [MICCAI 2026's tool template](../../miccai-2026/tools/index.md) with two ISBI-specific adaptations (IEEE Xplore DOI instead of Springer LNCS DOI; Track field uses ISBI's structure: Main proceedings / Workshop / Challenge / Special Session / Tutorial / Clinical Day):

````markdown
# <ToolName>

**One-line description** — what the tool does in plain language.

- **Maintainer:** <name> (<institution>)
- **Domain:** pathology / cytology / radiology (CT / MR / PET / mammography / US / MPI) / microscopy / hematopathology / surgical / multimodal
- **Ecosystem:** PyTorch / MONAI / nnU-Net / HuggingFace / standalone-Python / web-service / IEEE SPS reference codebase / other
- **Package / source:** [GitHub link]
- **Model weights / checkpoint:** [HuggingFace / Zenodo / Grand Challenge / lab site link, with license]
- **Docs / tutorial:** [link]
- **Status at ISBI 2026:** new release / major update / methods paper / challenge winner / workshop talk / tutorial / Clinical Day demo / keynote-adjacent
- **Proceedings:** [IEEE Xplore DOI if applicable — null for workshop-only or non-paper talks; flag if pending IEEE Xplore indexing]
- **arXiv preprint:** [arXiv link if mirrored — partial coverage for ISBI authors]
- **TBME Special Section:** [link if selected for the proposed TBME ISBI 2026 Special Section]

## Talk at ISBI 2026

- **Speaker:** ...
- **Day / Track:** Wed Apr 8 / Tutorial · Thu Apr 9 / Main Proceedings · Fri Apr 10 / FAIBI workshop · Sat Apr 11 / Challenge results · etc.
- **Session slot:** oral / poster / spotlight / challenge-results / keynote / special-session-invited
- **Slides:** [Zenodo DOI or lab site if deposited]
- **Video:** [conference replay link if posted]
- **Abstract / paper page:** [ISBI program link or IEEE Xplore link]

## What it does

2–3 sentences: the clinical or methodological problem it solves, the key architectural / training idea, what it consumes (modality, resolution, label type) and produces, what it's benchmarked against (which challenge / public dataset).

## Where it fits in the corpus

- AACR 2026: [link if mentioned — pathology FM dossiers especially]
- MICCAI 2026: [link if cousin paper exists — same lab, Sep version typical]
- RSNA 2026: [link if mentioned — radiology-side clinical-deployment counterpart]
- CVPR 2026: [link if mentioned — architecture-feeder upstream]
- NeurIPS 2026: [link if mentioned — general ML / FM counterpart]

## Notes

Free-form impressions: benchmarks claimed, comparisons to baselines (nnU-Net, SAM, prior FM checkpoints), reproducibility (license, weights availability, training-data access), and AACR/MICCAI/RSNA-axis fit notes. For ISBI specifically: flag (a) whether the paper is part of the TBME Special Section pipeline, (b) whether the work extends a Mahmood-lab / CHIEF / UNI line, (c) whether the modality is ISBI-overweighted (MRI reconstruction, MPI, ultrasound, microscopy) vs MICCAI-overweighted.
````

## Tool index

Placeholder table. ~10–25 entries expected after bulk extraction; the populated table will be sortable by Domain, Track, or Cancer-relevance.

| Tool | Domain | Ecosystem | Maintainer | Day / Track | Proceedings (IEEE Xplore DOI) | arXiv | Code | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|---|
| *(populated post-meeting once IEEE Xplore indexes the proceedings ~early May 2026; see [`../program-notes.md`](../program-notes.md) for the candidate shortlist anchored on the 3 cancer-direct challenges + the Mahmood keynote axis + the FAIBI workshop slate)* | | | | | | | | |

## Why this format

- **IEEE Xplore DOI is the anchor for ISBI.** Like Springer LNCS for MICCAI, the IEEE Xplore conference-paper DOI is the citable artifact even when slide decks vanish. Putting it on the same row as the talk metadata keeps the citation chain intact. **Caveat:** ISBI 4-page papers are paywalled in Xplore (IEEE member access typical); when authors mirror to arXiv that becomes the practical reading link, but the Xplore DOI is the version-of-record.
- **TBME Special Section field is ISBI-specific.** A subset of the strongest ISBI 2026 papers will be invited to extend into the TBME Special Section ("Selected Topics from ISBI 2026"). The extended TBME version becomes the durable citation anchor for those papers — worth flagging.
- **Track field replaces COSI / MICCAI Track.** ISBI's structure: Main proceedings / Workshop / Challenge / Special Session / Tutorial / Clinical Day. Smaller set than MICCAI's (no separate Satellite Events day formalism); each track signals a different peer-review bar.
- **Model weights + license are first-class.** ISBI tools are often model checkpoints + reference implementations (frequent IEEE SPS reference-codebase pattern, separate from typical academic GitHub). License clarity matters for downstream cancer-clinical deployment at RSNA / AACR.
- **arXiv row separate from IEEE Xplore row.** ISBI authors mirror to arXiv less consistently than MICCAI / CVPR (estimated 40–60% vs MICCAI's >80%), so the arXiv field will be sparser. Both rows are still tracked because when the arXiv mirror exists it's typically the more-read link.
- **Cross-vault "Mentioned elsewhere"** specifically watches: AACR pathology-FM dossiers (CHIEF / UNI / GigaPath) for the Mahmood-line work, MICCAI 2026 (Sep 27–Oct 1) for the cousin-paper pairing pattern (same lab, fuller methods paper 5 months later), RSNA 2026 (Nov 29–Dec 3) for clinical-deployment counterparts.

## Open questions

1. **Granularity** — locked: **one page per tool / model**, same as ISMB / RECOMB / MICCAI / AACR bioinfo-tools.
2. **Challenge writeups vs methods papers** — proposed: **one page per winning model** (top-1, top-3 if all release code) for the cancer-relevant challenges (RIVA, WBCBench2026, MPI Low Concentration). The challenge itself (history, dataset, leaderboard) is summarized in `../program-notes.md` rather than as a separate tool page — ISBI doesn't have a long enough challenge-history-per-challenge to warrant the MICCAI-style separate challenge page in most cases.
3. **TBME Special Section pairing** — open: when an ISBI 2026 paper extends to a TBME 2026/2027 paper, do we (a) keep one tool page anchored on the ISBI version with a "TBME extension" cross-link, or (b) update the page when the TBME version drops? Proposed: **(a)** — single page, TBME pointer updated as available.
4. **Mahmood keynote** — proposed: the keynote itself doesn't become a tool page, but **any new tool announced or updated in the keynote talk** (likely a CHIEF / UNI variant or a multimodal pathology-agent successor) gets either an update to the AACR dossier in-place or a new MICCAI-style page if it's a fundamentally new model. Watch the Mahmood Lab GitHub through Q2 2026 for the artifact drop.
5. **Coverage budget** — open: ~400–600 papers + 8 challenges + 6 workshops × ~5–10 papers. We don't expand a tool page for every paper. Filter: (a) any main-proceedings paper with code + maintained repo + clear oncology / pathology-FM / radiology-AI tie-in, (b) any FAIBI / Exploring-FM-in-Medical-Image-Analysis workshop paper that introduces a named model, (c) winners of the 3 cancer-relevant challenges, (d) any update to an existing-in-corpus AACR / MICCAI / RSNA tool. Estimated ~10–25 after filtering.
