# CVPR 2026 — Program Notes (pre-meeting prep)

**Last updated:** May 11, 2026 — T-3.5 weeks. Final paper decisions landed Feb 20, 2026; accepted-paper list public on OpenReview; CVF Open Access PDFs post around the meeting. Workshop accepted-paper lists landing May–early June. Camera-ready in flight.

This page exists to lock the **scope filter**, **workshop slate**, **anticipated paper themes**, and **cross-vault pairings** before any tool extraction begins. It is intentionally explicit about what is *out of scope* — CVPR's bulk is general computer vision, and conflating that bulk with the medical-imaging / pathology-FM subset would destroy the vault's signal-to-noise.

## Verified meeting facts

- **Dates:** Wed June 3 – Sun June 7, 2026.
  - **Jun 3 (Wed):** Workshops + Tutorials Day 1 — the **medical cluster lives here** (MCV full day, FMV half day, MMFM-BIOMED half day, PHAROS half day).
  - **Jun 4 (Thu):** Workshops + Tutorials Day 2 — second medical sub-cluster (CV4Clinical half day, Med-Reasoner half day).
  - **Jun 5 (Fri) – Jun 7 (Sun):** Main conference, orals + highlights + poster sessions.
- **Venue:** Colorado Convention Center, Denver, Colorado, USA.
- **Scale:** ~10,000 attendees (sibling to NeurIPS / ICML in scale).
- **Proceedings:** CVF Open Access (full open-access PDFs, no paywall) — typically posts within ~1 week of meeting. OpenReview venue: `CVPR.thecvf.com/2026/Conference`.

## Scope filter (load-bearing — repeat from `tools/index.md`)

CVPR is **scope-limited by design** in this vault. The filter is:

1. **Medical / biomedical workshop** (one of six identified).
2. **Main-track keyword match** on medical / pathology / radiology / oncology / clinical / biomedical / segmentation-for-medicine vocabulary.
3. **Architectural building block** with a documented or near-certain medical adoption path — DINOv3-class SSL pretraining, SAM-3-class segmentation FM, next-gen CLIP / SigLIP multimodal alignment, slide-level aggregation, diffusion / flow-matching for medical synthesis.

Everything else stays out. The light-build pattern mirrors [ICML 2026](../icml-2026/program-notes.md) and [NeurIPS 2026](../neurips-2026/index.md).

## Medical / biomedical workshop slate (verified)

Six workshops identified from the CVPR 2026 workshops page. All run on Jun 3–4 alongside tutorials.

| Workshop | Acronym | Date | Format | Contact | Notes |
|---|---|---|---|---|---|
| Medical Computer Vision | **MCV** | Wed Jun 3 | Full day | Zongwei Zhou | 12th edition; the canonical CVPR medical-CV workshop; broad scope from segmentation through FMs |
| Foundation Models for Medical Vision | **FMV** | Wed Jun 3 | Half day | Jun Ma | 3rd edition; medical-imaging FMs, SAM-Med-class, RadFM-class; co-organized with the BraTS / nnU-Net network |
| Multimodal Foundation Models for Biomedicine | **MMFM-BIOMED** | Wed Jun 3 | Half day | Yuhui Zhang | 2nd edition; pathology + radiology VLMs; CLIP / LLaVA / SigLIP for biomedicine |
| PHAROS AI Factory for Medical Imaging & Healthcare | **PHAROS** | Wed Jun 3 | Half day | Stefanos Kollias | EU AI Factory project; healthcare deployment, regulatory, federated learning |
| Bridging AI and Medical Reality (CV4Clinical) | **CV4Clinical** | Thu Jun 4 | Half day | Yicheng Wu | Real-world clinical translation, reliability, reproducibility, deployment failure modes |
| Medical Reasoning with Vision Language Foundation Models | **Med-Reasoner** | Thu Jun 4 | Half day | Anas Zafar | New entrant for 2026; reasoning capabilities for medical VLMs; clinician × CV researcher cross |

Workshop accepted-paper lists are landing through May 2026; stub pages and per-paper tracking will populate as those lists go public.

## Anticipated paper themes (5 high-signal axes)

These are the patterns we expect to see repeatedly in both main-track and workshop accepts. We will not commit to a full theme synthesis page (that would be out of scope for a light build), but the per-tool entries will tag against these themes:

1. **Pathology foundation model successors and slide-level aggregators.** Next-generation tile encoders (DINOv3-class, scaling beyond UNI / GigaPath / Virchow), slide-level aggregation transformers (ABMIL / TransMIL successors), and multi-cohort pretraining at TCGA / CPTAC / Mass General Brigham + Providence + UCSF-scale. Direct upstream of [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) / [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) / [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md) updates.

2. **Pathology and radiology vision-language models.** CONCH / PathChat / MUSK successors on the pathology side; MAIRA / RadFM / Merlin / CXR-LLaVA successors on the radiology side. Pathology-report alignment, radiology-report generation, prompt-tunable report drafting. Expect MMFM-BIOMED + Med-Reasoner to be the workshop home for the bulk of these.

3. **Generative medical imaging and counterfactuals.** Latent diffusion / DiT / flow-matching priors for MRI / CT reconstruction; ControlNet-style anatomy-conditioned synthesis; counterfactual generation for fairness audits and explainability; synthetic-data augmentation for rare-cohort segmentation. Bridges to MICCAI 2026 DGM4MICCAI workshop.

4. **Segmentation foundation models — SAM line and successors.** SAM-3 / EfficientSAM-2 / MedSAM-class adapters; promptable segmentation for tumor / lesion / organ tasks; few-shot and zero-shot transfer to BraTS / HECKTOR / KiTS / AutoPET / PANORAMA. Direct upstream of MICCAI challenge entries.

5. **Multimodal medical reasoning and clinical-grade VLMs.** Med-Reasoner is the named workshop; the main track will carry the architecture papers. Chain-of-thought reasoning over chest X-rays / pathology slides, agentic clinical workflows, retrieval-augmented diagnosis, multimodal alignment between text reports + imaging + structured EHR. Cross-link to [AACR 2026 agentic-AI axis](../aacr-2026/index.md) and [ICML 2026 agentic-AI subset](../icml-2026/index.md).

## Out-of-scope themes (explicitly skipped)

To keep the filter honest, the following CVPR 2026 themes get **no coverage** in this vault even when they are technically impressive:

- General scene understanding, depth estimation, optical flow, monocular 3D — no medical thread.
- Autonomous driving perception (KITTI / Waymo / nuScenes-class) — no medical thread.
- Robotics manipulation, embodied AI, simulation-to-real — no medical thread (surgical robotics is MICCAI's CAI track, not CVPR's general robotics track).
- General video generation (Sora / Veo / Movie Gen class) — no medical thread unless medical-imaging-specific.
- Face recognition, person re-identification, biometrics — no medical thread.
- AR / VR / NeRF / Gaussian splatting (general) — no medical thread.
- Adversarial robustness and watermarking for general images — out of scope.
- General efficiency / quantization / pruning — out of scope unless the paper benchmarks on a medical FM.

## Cross-vault pairings (the load-bearing chains)

The point of carrying CVPR in this vault is the cross-conference arcs. Three canonical chains to track:

1. **CVPR pretraining recipe → MICCAI methods → AACR translational poster.** A new SSL recipe at CVPR June 2026 → pathology-FM v2 paper at [MICCAI 2026](../miccai-2026/index.md) Sep 27–Oct 1 → translational poster at AACR 2027 April. The CVPR entry should explicitly link forward to the MICCAI cousin and the eventual AACR poster.

2. **CVPR medical-VLM → RSNA clinical-deployment readout.** A new radiology VLM at CVPR / MMFM-BIOMED → vendor demonstration or prospective-study readout at [RSNA 2026](../rsna-2026/index.md) Nov 29–Dec 3. The half-year arc is reliable for diagnostic-imaging VLMs.

3. **CVPR SAM successor → MICCAI challenge winner.** A SAM-3-class segmentation FM at CVPR → adoption in BraTS / HECKTOR / KiTS / AutoPET / PANORAMA winning entry at [MICCAI 2026](../miccai-2026/index.md) within the same calendar year. Track which CVPR segmentation paper anchors each MICCAI challenge result.

## What is NOT being built

To be explicit (light-build hygiene):

- **No `digest/` directory.** No per-day digests. The general-vision bulk dominates per-day proceedings and would dilute signal.
- **No `themes.md`.** The five themes above are scoped here in `program-notes.md` and tagged per tool entry; a separate synthesis page is not warranted.
- **No `keynotes/`.** CVPR plenaries are general-vision; we cover them only if a known medical-imaging / pathology-FM author is on stage.
- **No `mkdocs.yml`.** This vault piggybacks on the parent site config (per repo convention for sibling conference vaults).
- **No `timeline.md`.** Conference timeline lives at [`../../timeline.md`](../../timeline.md); no per-vault duplication.

## Next actions

- **May 11–31, 2026 (now → T-1 week):** scan accepted-paper list with keyword filter; pre-stub the ~25–50 high-signal entries. Pull workshop accept lists as they post. Cross-check against the MICCAI 2026 early-accept list (already posted May 7) for cousin-paper pairing.
- **Jun 3–7, 2026 (during the meeting):** opportunistic capture of slide deposits, GitHub repos, demo links, social reactions. The Wed Jun 3 medical-workshop cluster (MCV / FMV / MMFM-BIOMED / PHAROS) is the densest day; Thu Jun 4 carries the clinical-translation pair (CV4Clinical + Med-Reasoner).
- **Jun 8 – Jun 30, 2026 (post-meeting):** CVF Open Access proceedings post ~1 week after meeting. Bulk-populate `tools/` with the filtered subset. Cross-link into AACR pathology-FM dossiers and stage MICCAI 2026 (Sep 27–Oct 1) cousin pairings.

## Sources

- [CVPR 2026 home](https://cvpr.thecvf.com/Conferences/2026)
- [CVPR 2026 Important Dates](https://cvpr.thecvf.com/Conferences/2026/Dates)
- [CVPR 2026 Workshops list](https://cvpr.thecvf.com/Conferences/2026/Workshops)
- [FMV — Foundation Models for Medical Vision (CVPR 2026)](https://fmv-cvpr26workshop.github.io/)
- [Med-Reasoner workshop (CVPR 2026)](https://med-reasoner.github.io/cvpr2026/)
- [CV4Clinical 2026 — Bridging AI and Medical Reality](https://cv4clinical.github.io/cv4clinical_2026/)
- [MMFM-BIOMED workshop](https://mmfm-biomed.github.io/)
- [CVPR-MIA paper tracker (community-maintained)](https://github.com/MedAIerHHL/CVPR-MIA)
- [CVF Open Access](https://openaccess.thecvf.com/)
