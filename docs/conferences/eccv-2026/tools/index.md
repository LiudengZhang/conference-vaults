# ECCV 2026 — Tools / Methods (filtered)

> **Status:** Template stub. Meeting is ~17 weeks out (Sep 8–12, 2026, Malmö, Sweden). Submission cycle is mid-flight: rebuttal period **closed today (May 11)**, final decisions land **Jun 17, 2026**, camera-ready Jun 26. The accepted-paper list is **not yet public** — the workshop slate is being finalized (proposals accepted Apr 12). No entries are populated yet — this page exists to lock the per-tool format and the **scope filter** before extraction begins post-Jun-17.

## Scope filter (load-bearing — this is a light build)

ECCV 2026 will accept ~2,500 main-track papers + thousands more across workshops. We do **not** extract them all. An entry lands in this directory **only if** it satisfies one of:

1. **Medical / biomedical workshop filter** — appears in one of the medical / biomedical / clinical / bio-imaging workshops at ECCV 2026:
   - **BioImage Computing (BIC)** — recurring since 2016; bio-imaging methods (anticipated)
   - **Medical Computer Vision (MCV)** ECCV edition — anticipated based on 2022 precedent
   - **Foundation Models for Medical Vision** ECCV variant — speculative
   - **Multimodal Foundation Models for Biomedicine** ECCV variant — speculative
   - **CV4Good** — Computer Vision for Humanitarian Action (confirmed); humanitarian / global-health adjacent
   - *(Workshop slate is still posting through May–August 2026; this list will be revised once `eccv.ecva.net/Conferences/2026/Workshops` goes fully public.)*
2. **Main-track keyword filter** — title or abstract contains any of: *medical imaging, radiology, pathology, histology, histopathology, whole-slide image, WSI, CT, MRI, PET, X-ray, mammography, ultrasound, dermatology, endoscopy, ophthalmology, retinal, tumor, lesion, segmentation for medicine, radiotherapy, surgical, clinical, electronic health record, biomedical, cancer, oncology, foundation model for medicine, vision-language for healthcare, report generation, microscopy, cell segmentation, bio-imaging, fluorescence, single-cell imaging*.
3. **Architectural-building-block filter** — main-track paper on a self-supervised pretraining recipe (DINOv3-class), segmentation FM (SAM-3-class), multimodal alignment (next-gen CLIP / SigLIP), slide- or volume-level aggregation, diffusion / flow-matching for image synthesis, **with a documented or near-certain medical adoption path** within 12 months. Pure-vision flagship papers without a medical downstream stay out.

Everything else — general scene understanding, 3D reconstruction, NeRF / Gaussian splatting (non-medical), autonomous-driving perception, robotics, face / person reID, video generation for entertainment, AR/VR — is **out of scope** and gets no entry here. Reviewer bandwidth is the binding constraint, not source availability.

## Per-entry template

Each in-scope paper gets a file (`tools/<paper-slug>.md`) following this structure:

````markdown
# <Method / Tool name>

**One-line description** — what the method does in plain language.

- **Authors:** <first author + lab + institution>
- **Track:** main-track (oral / poster) / BIC / MCV / FMV-ECCV / MMFM-BIOMED-ECCV / CV4Good / [workshop slug]
- **OpenReview:** [paper page]
- **ECVA Open Access:** [final paper link, posted ~1–2 weeks post-meeting]
- **Springer LNCS:** [DOI link]
- **arXiv / bioRxiv / medRxiv:** [preprint link]
- **Code:** [GitHub link]
- **Pretrained weights:** [HF Hub / Zenodo link if applicable]
- **Demo:** [HF Space / Replicate / project page if applicable]

## Presentation at ECCV 2026

- **Format:** oral / poster / workshop talk
- **Day / session:** Sep 8–9 (workshops) or Sep 10–12 (main)
- **Room / time:** [pulled from program]
- **Video:** [YouTube / ECVA link, post-meeting]

## What it does

2–3 sentences: the problem it solves, the methodological idea, what it consumes and produces (modality, scale, output type).

## Why it matters for cancer / biology

Explicit statement of the bridge to oncology — especially for main-track papers that don't claim cancer relevance. Example: "DINOv3-class self-supervised pretraining at 1B-parameter ViT-G from European labs; direct upgrade path for pathology FMs (CHIEF / UNI / GigaPath next-gen tile encoders) and radiology FMs (RadFM / Merlin)." Without this paragraph, the entry doesn't belong here.

## Where it fits in the corpus

- AACR 2026 pathology-FM dossiers: [CHIEF / Prov-GigaPath / UNI links if relevant]
- **MICCAI 2026 cousin paper / author overlap:** [link — ECCV / MICCAI author overlap is the rule, 2–3 week offset in 2026]
- CVPR 2026 cousin paper (June 2026): [link — for US-led labs the CVPR-ECCV pair may exist]
- RSNA 2026 clinical-deployment cousin: [link if a trial or vendor adopts]
- NeurIPS 2026 LMRL / cousin: [link if cross-listed at NeurIPS bio workshops]
- ISMB 2026 / RECOMB 2026: [link if benchmarked / cited from bioinformatics side]

## Notes

Free-form: benchmarks claimed (TCGA / CPTAC / MIMIC-CXR / BraTS / HECKTOR / KiTS / PANORAMA / Camelyon / PANDA / cell-segmentation benchmarks), comparisons to CHIEF / Prov-GigaPath / UNI / CONCH / PathChat / MUSK / Virchow / RadFM / Merlin / SAM-Med, scaling-law observations, data-curation methodology, EU AI Act / MDR regulatory implications, federated-learning provenance (PHAROS / EuCAIM / OPTIMAL cohorts), license terms (often more restrictive than CVPR — Springer LNCS layer + ECVA mirror).
````

## Tool index

*Empty — populates from mid-June 2026 onward (post final decisions Jun 17), with bulk fill in mid-to-late September 2026 after the meeting and ECVA Open Access posting. Anticipated final count: ~20–40 entries across medical / bio workshops + main-track filter hits + architectural-building-block subset.*

| Method / Tool | Track | Modality | Authors | Format | OpenReview / ECVA | Code | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|

## Why this format

- **Track field** — ECCV runs many workshops alongside a sprawling main track; this field disambiguates where a result lived without polluting the page body. Medical / bio workshops are flagged explicitly.
- **"Why it matters for cancer / biology" is mandatory** — most ECCV work is not explicitly medical, and a lot of the medical work isn't explicitly oncology. The only reason a paper is in this vault is the cancer downstream. Forcing this field keeps the filter honest, especially for architectural-building-block entries.
- **MICCAI cousin field** — the load-bearing cross-link. ECCV (Sep 8–12) and MICCAI (Sep 27–Oct 1) sit **2–3 weeks apart** in 2026, with heavy author overlap (more so than CVPR/MICCAI's 4-month gap). Tracking the overlap prevents duplicated tool entries and surfaces method-evolution arcs (sometimes a paper is the *same paper* in different framing).
- **Pretrained weights + demo rows** — ECCV medical-FM papers from European labs are increasingly shipping HF Hub weights and HF Space demos; tracking these is the difference between a paper entry and a usable tool entry.
- **Springer LNCS row** — ECCV proceedings carry both an ECVA open-access PDF and a Springer LNCS DOI. The DOI is the citation-stable identifier; the ECVA PDF is the unpaywalled artifact. Tracking both is necessary.
- **Cross-vault links to AACR pathology-FM dossiers** — the load-bearing purpose: an ECCV September pretraining recipe should be one click from the AACR April session where its descendant pathology FM gets demonstrated on TCGA the following spring.

## Open questions

1. **Workshop-only papers without code or weights** — keep as entries anyway, or defer to "main proceedings only"? *Tentative: keep workshop entries; medical-FM workshops at ECCV pre-stage code releases reliably given the European open-science emphasis (Horizon Europe, EOSC mandates).*
2. **Architectural-building-block subset** — every new self-supervised pretraining paper, or only those with a documented medical adoption path? *Tentative: only those where the paper itself names a medical benchmark, or where author overlap with a known pathology / radiology FM lab is documented. Pure-vision flagship without a medical thread stays out.*
3. **SAM-line entries** — every SAM-Med adapter, or only the parent SAM-3 / EfficientSAM update? *Tentative: parent SAM update gets one entry; SAM-Med adapters get an entry only if they introduce a new architecture beyond prompt-tuning.*
4. **Consolidating ECCV + MICCAI cousin papers (2–3 week gap)** — one entry or two when the same lab ships an evolved version 2–3 weeks later? *Tentative: usually one entry with cousin-link annotation, given the near-zero time gap; only split into two entries when the MICCAI version is clearly a different paper rather than an extended-abstract / methods-paper companion to ECCV.*
5. **BioImage Computing scope** — the BIC workshop covers microscopy and bio-imaging broadly (cell segmentation, single-cell imaging, fluorescence). Include the full BIC paper accept list, or filter to cancer-relevant only (tumor microenvironment imaging, IHC quantification, pathology-adjacent microscopy)? *Tentative: filter to cancer-relevant; the cell-biology-foundational subset belongs in a separate bio-imaging vault if and when one is built.*
6. **Springer LNCS paywall window** — entries posted before ECVA mirror lags ~1–2 weeks. *Tentative: stub entries on arXiv ID alone, fill ECVA / LNCS URLs in a second pass once `ecva.net/papers/eccv_2026/` is live.*
