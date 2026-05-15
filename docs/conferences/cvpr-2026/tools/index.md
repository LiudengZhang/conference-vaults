# CVPR 2026 — Tools / Methods (filtered)

> **Status:** Template stub. Meeting is ~3.5 weeks out (Jun 3–7, 2026, Denver). Final decisions landed Feb 20, 2026; the accepted-paper list is public on OpenReview, with camera-ready PDFs and CVF Open Access full text posting around the meeting. Workshop accepted-paper lists land May–early June. No entries are populated yet — this page exists to lock the per-tool format and the **scope filter** before extraction begins.

## Scope filter (load-bearing — this is a light build)

CVPR 2026 accepts ~2,500 main-track papers + thousands more across workshops. We do **not** extract them all. An entry lands in this directory **only if** it satisfies one of:

1. **Medical / biomedical workshop filter** — appears in one of the six CVPR 2026 medical / biomedical / clinical workshops:
   - **MCV** — Medical Computer Vision (12th edition; full day Wed Jun 3)
   - **FMV** — Foundation Models for Medical Vision (3rd edition; half day Wed Jun 3)
   - **MMFM-BIOMED** — Multimodal Foundation Models for Biomedicine (2nd edition; half day Wed Jun 3)
   - **PHAROS** — AI Factory for Medical Imaging & Healthcare (half day Wed Jun 3)
   - **CV4Clinical** — Bridging AI and Medical Reality (half day Thu Jun 4)
   - **Med-Reasoner** — Medical Reasoning with Vision Language Foundation Models (half day Thu Jun 4)
2. **Main-track keyword filter** — title or abstract contains any of: *medical imaging, radiology, pathology, histology, histopathology, whole-slide image, WSI, CT, MRI, PET, X-ray, mammography, ultrasound, dermatology, endoscopy, ophthalmology, retinal, tumor, lesion, segmentation for medicine, radiotherapy, surgical, clinical, electronic health record, biomedical, cancer, oncology, foundation model for medicine, vision-language for healthcare, report generation*.
3. **Architectural-building-block filter** — main-track paper on a self-supervised pretraining recipe (DINOv3-class), segmentation FM (SAM-3-class), multimodal alignment (next-gen CLIP / SigLIP), slide- or volume-level aggregation, diffusion / flow-matching for image synthesis, **with a documented or near-certain medical adoption path** within 12 months. Pure-vision flagship papers without a medical downstream stay out.

Everything else — general scene understanding, 3D reconstruction, NeRF / Gaussian splatting (non-medical), autonomous-driving perception, robotics, face / person reID, video generation for entertainment, AR/VR — is **out of scope** and gets no entry here. Reviewer bandwidth is the binding constraint, not source availability.

## Per-entry template

Each in-scope paper gets a file (`tools/<paper-slug>.md`) following this structure:

````markdown
# <Method / Tool name>

**One-line description** — what the method does in plain language.

- **Authors:** <first author + lab + institution>
- **Track:** main-track (oral / highlight / poster) / MCV / FMV / MMFM-BIOMED / PHAROS / CV4Clinical / Med-Reasoner
- **OpenReview:** [paper page]
- **CVF Open Access:** [final paper link, once camera-ready posts]
- **arXiv / bioRxiv / medRxiv:** [preprint link]
- **Code:** [GitHub link]
- **Pretrained weights:** [HF Hub / Zenodo link if applicable]
- **Demo:** [HF Space / Replicate / project page if applicable]

## Presentation at CVPR 2026

- **Format:** oral / highlight / poster / workshop talk
- **Day / session:** Jun 3–4 (workshops) or Jun 5–7 (main)
- **Room / time:** [pulled from virtual program]
- **Video:** [YouTube / CVF link, post-meeting]

## What it does

2–3 sentences: the problem it solves, the methodological idea, what it consumes and produces (modality, scale, output type).

## Why it matters for cancer / biology

Explicit statement of the bridge to oncology — especially for main-track papers that don't claim cancer relevance. Example: "DINOv3-class self-supervised pretraining at 1B-parameter ViT-G; direct upgrade path for pathology FMs (CHIEF / UNI / GigaPath next-gen tile encoders) and radiology FMs (RadFM / Merlin)." Without this paragraph, the entry doesn't belong here.

## Where it fits in the corpus

- AACR 2026 pathology-FM dossiers: [CHIEF / Prov-GigaPath / UNI links if relevant]
- **MICCAI 2026 cousin paper / author overlap:** [link — CVPR / MICCAI author overlap is the rule, half-year offset]
- RSNA 2026 clinical-deployment cousin: [link if a trial or vendor adopts]
- NeurIPS 2026 LMRL / cousin: [link if cross-listed at NeurIPS bio workshops]
- ISMB 2026 / RECOMB 2026: [link if benchmarked / cited from bioinformatics side]

## Notes

Free-form: benchmarks claimed (TCGA / CPTAC / MIMIC-CXR / BraTS / HECKTOR / PANORAMA), comparisons to CHIEF / Prov-GigaPath / UNI / CONCH / PathChat / MUSK / RadFM / Merlin / SAM-Med, scaling-law observations, data-curation methodology, regulatory implications (FDA 510(k) path), license terms.
````

## Tool index

*Empty — populates from late May 2026 (workshop accepted-paper window) onward, with bulk fill in mid-June after the meeting and CVF Open Access posting. Anticipated final count: ~25–50 entries across the six medical workshops + main-track filter hits + architectural-building-block subset.*

| Method / Tool | Track | Modality | Authors | Format | OpenReview / CVF | Code | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|

## Why this format

- **Track field** — CVPR runs ~120 workshops and a sprawling main track; this field disambiguates where a result lived without polluting the page body. Six medical workshops are flagged explicitly.
- **"Why it matters for cancer / biology" is mandatory** — most CVPR work is not explicitly medical, and a lot of the medical work isn't explicitly oncology. The only reason a paper is in this vault is the cancer downstream. Forcing this field keeps the filter honest, especially for architectural-building-block entries.
- **MICCAI cousin field** — the load-bearing cross-link. CVPR (June) and MICCAI (late Sep / early Oct) split the same medical-imaging-methods author community across two cycles per calendar year; tracking the overlap prevents duplicated tool entries and surfaces method-evolution arcs (CVPR v1 → MICCAI v2 within 3–4 months is common).
- **Pretrained weights + demo rows** — CVPR medical-FM papers increasingly ship HF Hub weights and HF Space demos; tracking these is the difference between a paper entry and a usable tool entry.
- **Cross-vault links to AACR pathology-FM dossiers** — the load-bearing purpose: a CVPR June pretraining recipe should be one click from the AACR April session where its descendant pathology FM gets demonstrated on TCGA the following spring.

## Open questions

1. **Workshop-only papers without code or weights** — keep as entries anyway, or defer to "main proceedings only"? *Tentative: keep workshop entries; medical-FM workshops at CVPR pre-stage code releases more reliably than general-vision workshops.*
2. **Architectural-building-block subset** — every new self-supervised pretraining paper, or only those with a documented medical adoption path? *Tentative: only those where the paper itself names a medical benchmark, or where author overlap with a known pathology / radiology FM lab is documented. Pure-vision flagship without a medical thread stays out.*
3. **SAM-line entries** — every SAM-Med adapter, or only the parent SAM-3 / EfficientSAM update? *Tentative: parent SAM update gets one entry; SAM-Med adapters get an entry only if they introduce a new architecture beyond prompt-tuning. The 50+ SAM-tuning papers per CVPR cycle would otherwise drown the index.*
4. **Consolidating CVPR + MICCAI cousin papers** — one entry or two when the same lab ships an evolved version 3–4 months later? *Tentative: two entries with explicit version / delta notes; the short arc is informative for tracking pathology-FM v2 / v3 evolution.*
