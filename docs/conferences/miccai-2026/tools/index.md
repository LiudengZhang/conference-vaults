# MICCAI 2026 — Tools

MICCAI 2026 will deliver peer-reviewed Springer LNCS proceedings (~700–900 accepted papers across main + early-accept tracks; final count after Jun 12 notifications) plus ~35–60 workshops, ~25–40 challenges, and a tutorials slate across two satellite days. The subset that yields tool pages is the intersection of (a) main-proceedings papers that release a named model / method / package with a maintained repo, (b) workshop papers in the cancer-adjacent tracks (COMPAY, BrainLes/BraTS, DGM4MICCAI, MILEX, MMMI, CaPTion), (c) challenge winners with public code / weights, and (d) any update to an FM already in the AACR or RSNA corpus (CHIEF, Prov-GigaPath, UNI/UNI2, RadFM, MedSAM, Merlin, MAIRA-class).

> **Status:** Template stub. Per-tool format proposed here for review *before* bulk extraction runs after the meeting closes (Oct 1, 2026). Estimated ~25–50 entries once the proceedings list + challenge results are public.

## Per-tool entry template

Each tool gets its own page (`tools/<package-slug>.md`) following this structure. The shape mirrors [ISMB 2026's tool template](../../ismb-2026/tools/index.md) with two MICCAI-specific adaptations (Springer LNCS DOI instead of *Bioinformatics* DOI; Track field instead of COSI field):

````markdown
# <ToolName>

**One-line description** — what the tool does in plain language.

- **Maintainer:** <name> (<institution>)
- **Domain:** pathology / radiology (CT / MR / PET / mammography / US) / surgical / multimodal
- **Ecosystem:** PyTorch / MONAI / nnU-Net / HuggingFace / standalone-Python / web-service / other
- **Package / source:** [GitHub link]
- **Model weights / checkpoint:** [HuggingFace / Zenodo / lab site link, with license]
- **Docs / tutorial:** [link]
- **Status at MICCAI 2026:** new release / major update / methods paper / challenge winner / workshop talk / tutorial / CliniCAI demo
- **Proceedings:** [Springer LNCS DOI if applicable — null for workshop-only or non-paper talks]
- **arXiv preprint:** [arXiv link if mirrored — typical for MICCAI methods papers]

## Talk at MICCAI 2026

- **Speaker:** ...
- **Day / Track:** Sun Sep 27 / Tutorial · Mon Sep 28 / Main Proceedings · Wed Sep 30 / COMPAY workshop · Thu Oct 1 / BraTS challenge results · etc.
- **Session slot:** oral / poster / spotlight / challenge-results / keynote
- **Slides:** [Zenodo DOI or lab site if deposited]
- **Video:** [conference replay link if posted]
- **Abstract / paper page:** [MICCAI program link or Springer link]

## What it does

2–3 sentences: the clinical or methodological problem it solves, the key architectural / training idea, what it consumes (modality, resolution, label type) and produces, what it's benchmarked against (which challenge / public dataset).

## Where it fits in the corpus

- AACR 2026: [link if mentioned — pathology FM dossiers especially]
- RSNA 2026: [link if mentioned — radiology-side clinical-deployment counterpart]
- ISMB 2026: [link if mentioned — methodologically adjacent]
- NeurIPS 2026: [link if mentioned — general ML / FM counterpart]
- ESMO 2026 / ASCO 2026: [link if a clinical readout uses this tool]

## Notes

Free-form impressions: benchmarks claimed, comparisons to baselines (nnU-Net, SAM, prior FM checkpoints), reproducibility (license, weights availability, training-data access), and AACR/RSNA-axis fit notes (does this surface at RSNA as a clinical-deployment story? does it cite an AACR pathology-FM dossier?).
````

## Tool index

Placeholder table. ~25–50 entries expected after bulk extraction; the populated table will be sortable by Domain, Track, or Ecosystem.

| Tool | Domain | Ecosystem | Maintainer | Day / Track | Proceedings (LNCS DOI) | arXiv | Code | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|---|
| *(populated post-meeting from the Jun 12 final-accept list + workshop programs + challenge result writeups; see [`../program-notes.md`](../program-notes.md) for the candidate shortlist)* | | | | | | | | |

## Why this format

- **Springer LNCS DOI is the anchor for MICCAI.** Like ISMB's *Bioinformatics* DOI, the LNCS chapter DOI is what survives — it's the citable artifact even when slide decks vanish. Putting it on the same row as the talk metadata keeps the citation chain intact.
- **Track field replaces COSI.** MICCAI has fewer parallel tracks than ISMB (no 22-COSI structure), but it has a meaningful Main / Workshop / Challenge / CliniCAI / Tutorial split that drives reader expectations: a Main-proceedings paper is full peer-reviewed; a workshop paper is lighter peer review (typically 1–2 reviewers); a challenge writeup is more of a benchmark report than a methods paper.
- **Model weights + license are first-class.** MICCAI tools are mostly model checkpoints (not Bioconductor packages). License clarity (CC-BY, OpenRAIL, research-only) matters as much as code availability — clinical-deployment downstream at RSNA / AACR depends on it.
- **arXiv row separate from LNCS row.** Almost every MICCAI methods paper has an arXiv mirror filed 2–6 months before the meeting. The arXiv version is what most readers cite, but the LNCS version is the version-of-record. Both rows.
- **Cross-vault "Mentioned elsewhere"** specifically watches: AACR pathology-FM dossiers (CHIEF / GigaPath / UNI) for pathology-FM updates, RSNA tool index for radiology-side clinical-deployment counterparts, ESMO / ASCO trial readouts for any imaging-AI-driven oncology study.

## Open questions

1. **Granularity** — locked: **one page per tool / model**, same as ISMB / RECOMB / AACR bioinfo-tools.
2. **Challenge writeups vs methods papers** — open: a BraTS-2026 winning submission is "a tool" (the winning model) but the BraTS challenge itself is also "a benchmark." Proposed: **one page per winning model** (top-1, top-3 if all release code), plus **one page for the challenge as a benchmark** (history, dataset, leaderboard pointer). The challenge page lives under `topics/oncology-challenges/` rather than `tools/`.
3. **Pathology FM updates vs new entries** — open: if CHIEF's authors release a v2 or a new sub-method at MICCAI 2026 (likely), do we (a) update the AACR CHIEF dossier in-place with a "MICCAI 2026 update" section, or (b) create a parallel MICCAI tool page that cross-links to the AACR dossier? Proposed default: **(a) update in-place for incremental work, (b) new MICCAI page only for a fundamentally new model**. Symmetric to the ISMB-AACR cross-link convention.
4. **CliniCAI talks** — open: the Clinical Day track is typically clinician-facing and rarely names a new tool, but occasionally introduces a deployment-ready system. Proposed: **only if the talk names a specific tool with public artifact** — otherwise the talk is summarized in the day's digest, not in `tools/`.
5. **Coverage budget** — open: ~700–900 papers + ~50 workshops × ~10 papers each + ~30 challenges. We don't expand a tool page for every paper. Filter: (a) any main-proceedings paper with code + maintained repo + clear oncology / FM tie-in, (b) any COMPAY / BrainLes / DGM4MICCAI workshop paper that introduces a named model, (c) any challenge winner with released checkpoints, (d) any update to an existing-in-corpus AACR or RSNA tool. Estimated ~25–50 after filtering — narrower than ISMB's ~60–120 because the methods filter is sharper.
