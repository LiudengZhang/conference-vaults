# ECCV 2026 — Program Notes (pre-meeting prep)

**Last updated:** May 11, 2026 — T-17 weeks. Submission cycle is mid-flight: paper submissions closed Mar 5; rebuttal **closed today (May 11)**; final decisions land **Jun 17, 2026**; camera-ready Jun 26. Workshop proposals were accepted Apr 12, with individual workshop sites coming online through May–August. Accepted-paper list **not yet public** — meaningful keyword scanning of accepts cannot begin until late June.

This page exists to lock the **scope filter**, **workshop slate**, **anticipated paper themes**, and **cross-vault pairings** before any tool extraction begins. It is intentionally explicit about what is *out of scope* — ECCV's bulk is general computer vision, and conflating that bulk with the medical-imaging / pathology-FM subset would destroy the vault's signal-to-noise.

## Verified meeting facts

- **Dates:** Tue September 8 – Sat September 12, 2026.
  - **Sep 8 (Tue):** Workshops + Tutorials Day 1 — anticipated medical / bio cluster here.
  - **Sep 9 (Wed):** Workshops + Tutorials Day 2 — second day of workshop / bio cluster.
  - **Sep 10 (Thu) – Sep 12 (Sat):** Main conference, orals + poster sessions + Expo.
- **Venue:** Malmö Arena and Malmömässan, Malmö, Sweden. (Malmö is the southern Swedish city across the Öresund Bridge from Copenhagen; easy travel pairing with Copenhagen Airport CPH.)
- **Scale:** Anticipated ~6,700–7,500 attendees, building on ECCV 2024 Milan's 6,700+ (smaller than CVPR's ~10,000 but the same overall venue tier).
- **Proceedings:** **Springer LNCS** (paywalled at the DOI, but mirrored open-access via ECVA at `ecva.net/papers/eccv_2026/`) — typically posts within ~1–2 weeks of meeting. OpenReview venue: `thecvf.com/ECCV/2026/Conference`.
- **Biennial cadence:** ECCV runs even years; alternates with ICCV (odd years). 36th edition (the "European" cycle dating back to 1990 with two-year gaps).

## Scope filter (load-bearing — repeat from `tools/index.md`)

ECCV is **scope-limited by design** in this vault. The filter is:

1. **Medical / biomedical workshop** (slate still being announced through May–August; anticipated 2–4 medical / bio workshops based on ECCV 2022 + 2024 history).
2. **Main-track keyword match** on medical / pathology / radiology / oncology / clinical / biomedical / bio-imaging / segmentation-for-medicine vocabulary.
3. **Architectural building block** with a documented or near-certain medical adoption path — DINOv3-class SSL pretraining, SAM-3-class segmentation FM, next-gen CLIP / SigLIP multimodal alignment, slide-level aggregation, diffusion / flow-matching for medical synthesis.

Everything else stays out. The light-build pattern mirrors [CVPR 2026](../cvpr-2026/program-notes.md), [ICML 2026](../icml-2026/program-notes.md), and [NeurIPS 2026](../neurips-2026/index.md).

## Medical / biomedical workshop slate (partial — being announced)

Workshop proposals were accepted **Apr 12, 2026**; individual workshop sites are coming online through May–August. The slate below is partial and based on **anticipation from ECCV 2018 / 2020 / 2022 / 2024 history + the CVPR 2026 medical workshop pattern**; expect revision as the official slate populates.

| Workshop | Acronym | Likely date | Format | Notes |
|---|---|---|---|---|
| BioImage Computing | **BIC** | Sep 8 or 9 (TBD) | Half / full day | Recurring at ECCV 2018 / 2020 / 2022 / 2024; bio-imaging methods, microscopy, cell segmentation, deep learning for bio-imaging — anticipated for 2026 |
| Medical Computer Vision (ECCV edition) | **MCV** | Sep 8 or 9 (TBD) | Half / full day | ECCV-edition ran at 2022; cross-pollinates with CVPR MCV — anticipated |
| Foundation Models for Medical Vision (ECCV variant) | **FMV-ECCV** | Sep 8 or 9 (TBD) | Half day | Speculative — possible ECCV companion to the CVPR FMV series |
| Multimodal Foundation Models for Biomedicine (ECCV variant) | **MMFM-BIOMED-ECCV** | Sep 8 or 9 (TBD) | Half day | Speculative — possible ECCV companion to CVPR MMFM-BIOMED |
| CV4Good — Computer Vision for Humanitarian Action | **CV4Good** | Sep 8–9 | TBD | **Confirmed**; Good AI Lab + MSF; humanitarian / global-health imaging — partial vault relevance |

Workshop slate revision will land when `eccv.ecva.net/Conferences/2026/Workshops` is fully populated (anticipated June–July, in line with prior ECCV cycles).

## Anticipated paper themes (5 high-signal axes)

These are the patterns we expect to see repeatedly in both main-track and workshop accepts. We will not commit to a full theme synthesis page (that would be out of scope for a light build), but the per-tool entries will tag against these themes:

1. **Pathology foundation model successors and slide-level aggregators.** Next-generation tile encoders (DINOv3-class, scaling beyond UNI / GigaPath / Virchow), slide-level aggregation transformers (ABMIL / TransMIL successors), multi-cohort pretraining at TCGA / CPTAC / European-hospital-network scale (Charité, Karolinska, Erasmus MC, Institut Curie, IEO Milan, NKI). Direct upstream of [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) / [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) / [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md) updates. European pathology consortia (BIGPICTURE, EOSC4Cancer, EuCAIM) anchor papers here that don't appear at CVPR.

2. **Pathology and radiology vision-language models.** CONCH / PathChat / MUSK / Virchow successors on the pathology side; MAIRA / RadFM / Merlin / CXR-LLaVA successors on the radiology side. Pathology-report alignment, radiology-report generation, prompt-tunable report drafting. Knowledge-enhanced visual-language pretraining (KEP-line, ECCV 2024) is the canonical anchor. Expect the speculative MMFM-BIOMED-ECCV (if it materializes) to be the workshop home for the bulk of these.

3. **Generative medical imaging and counterfactuals.** Latent diffusion / DiT / flow-matching priors for MRI / CT reconstruction; ControlNet-style anatomy-conditioned synthesis; counterfactual generation for fairness audits and explainability; synthetic-data augmentation for rare-cohort segmentation. Bridges to MICCAI 2026 DGM4MICCAI workshop (2–3 weeks later). European diffusion-research community (LMU Compvis, EPFL, IST Austria) anchors many of these papers.

4. **Segmentation foundation models — SAM line and successors, plus bio-imaging segmentation.** SAM-3 / EfficientSAM-2 / MedSAM-class adapters; promptable segmentation for tumor / lesion / organ tasks; few-shot and zero-shot transfer to BraTS / HECKTOR / KiTS / AutoPET / PANORAMA. **Plus** the BioImage Computing axis: 2D/3D cell segmentation, subcellular structure segmentation, microscopy super-resolution, instance segmentation for high-content screens — directly relevant to cancer biology pipelines (IHC quantification, tumor microenvironment imaging).

5. **Multimodal medical reasoning, federated learning, and EU regulatory-grade clinical VLMs.** Chain-of-thought reasoning over chest X-rays / pathology slides, agentic clinical workflows, retrieval-augmented diagnosis, multimodal alignment between text reports + imaging + structured EHR. **The ECCV-distinctive thread:** federated learning across European hospital networks (PHAROS, EuCAIM, OPTIMAL, EOSC4Cancer) and EU AI Act / MDR-compliant deployment frameworks — work that doesn't surface at CVPR. Cross-link to [AACR 2026 agentic-AI axis](../aacr-2026/index.md) and [ICML 2026 agentic-AI subset](../icml-2026/index.md).

## Out-of-scope themes (explicitly skipped)

To keep the filter honest, the following ECCV 2026 themes get **no coverage** in this vault even when they are technically impressive:

- General scene understanding, depth estimation, optical flow, monocular 3D — no medical thread.
- Autonomous driving perception (KITTI / Waymo / nuScenes-class) — no medical thread.
- Robotics manipulation, embodied AI, simulation-to-real — no medical thread (surgical robotics is MICCAI's CAI track, not ECCV's general robotics track).
- General video generation (Sora / Veo / Movie Gen class) — no medical thread unless medical-imaging-specific.
- Face recognition, person re-identification, biometrics — no medical thread.
- AR / VR / NeRF / Gaussian splatting (general) — no medical thread.
- Adversarial robustness and watermarking for general images — out of scope.
- General efficiency / quantization / pruning — out of scope unless the paper benchmarks on a medical FM.
- General-purpose CV4Good humanitarian-imaging entries that aren't health / medical — partial CV4Good relevance only.

## Cross-vault pairings (the load-bearing chains)

The point of carrying ECCV in this vault is the cross-conference arcs. **The ECCV–MICCAI overlap is the tightest of any conference pair in the vault** — 2–3 weeks separates them in 2026, both in Europe (Malmö → Daejeon for MICCAI, but European lab authorship dominates both). Four canonical chains to track:

1. **ECCV pretraining recipe → MICCAI methods (2–3 weeks later) → AACR translational poster.** A new SSL recipe at ECCV Sep 8–12 → pathology-FM v2 paper at [MICCAI 2026](../miccai-2026/index.md) Sep 27–Oct 1 → translational poster at AACR 2027 April. The ECCV entry should explicitly link forward to the MICCAI cousin and the eventual AACR poster.

2. **CVPR (Jun) → ECCV (Sep) → MICCAI (Sep–Oct) European mirror arc.** A US-led CVPR pretraining recipe in June 2026 → European-lab response / variant at ECCV three months later → MICCAI methods application within 2–3 weeks. Tracking the CVPR–ECCV–MICCAI triple is informative for understanding the US / European division of method labor in medical-imaging FM development.

3. **ECCV medical-VLM → RSNA clinical-deployment readout.** A new radiology VLM at ECCV → vendor demonstration or prospective-study readout at [RSNA 2026](../rsna-2026/index.md) Nov 29–Dec 3. The 11-week arc is reliable for diagnostic-imaging VLMs.

4. **ECCV SAM successor → MICCAI challenge winner.** A SAM-3-class segmentation FM at ECCV → adoption in BraTS / HECKTOR / KiTS / AutoPET / PANORAMA winning entry at [MICCAI 2026](../miccai-2026/index.md) within the same month. Track which ECCV segmentation paper anchors each MICCAI challenge result.

## What is NOT being built

To be explicit (light-build hygiene):

- **No `digest/` directory.** No per-day digests. The general-vision bulk dominates per-day proceedings and would dilute signal.
- **No `themes.md`.** The five themes above are scoped here in `program-notes.md` and tagged per tool entry; a separate synthesis page is not warranted.
- **No `keynotes/`.** ECCV plenaries are general-vision; we cover them only if a known medical-imaging / pathology-FM author is on stage.
- **No `mkdocs.yml`.** This vault piggybacks on the parent site config (per repo convention for sibling conference vaults).
- **No `timeline.md`.** Conference timeline lives at [`../../timeline.md`](../../timeline.md); no per-vault duplication.

## Next actions

- **May 11 – Jun 17, 2026 (now → final decisions, T-17 → T-12 weeks):** workshop sites continue posting; track accepted workshops as they post (especially confirm/deny BIC, MCV-ECCV, FMV-ECCV, MMFM-BIOMED-ECCV anticipation). **No main-track filtering possible until Jun 17.**
- **Jun 17 – Jul 31, 2026 (T-12 → T-6 weeks):** accept list goes public Jun 17. Begin scanning with keyword filter; pre-stub the ~20–40 high-signal entries. Camera-ready Jun 26; arXiv mirrors land through July. Cross-check authorship against the MICCAI 2026 accept list (already posted May 7) for cousin-paper pairing — this is the **single most important cross-link operation** for this vault given the 2–3 week ECCV–MICCAI gap.
- **Aug 2026 (T-5 → T-2 weeks):** workshop accept lists post on individual workshop sites. Pull DOIs and arXiv IDs into stub pages.
- **Sep 8–12, 2026 (during the meeting):** opportunistic capture of slide deposits, GitHub repos, demo links, social reactions. Sep 8–9 workshop cluster is the densest pair of days for vault filter. **Plan for dual-coverage workflow** — MICCAI 2026 (Sep 27–Oct 1) starts 15 days after ECCV ends; the same labs will be at both meetings.
- **Sep 13 – Sep 30, 2026 (post-meeting):** ECVA Open Access proceedings post ~1–2 weeks after meeting. Bulk-populate `tools/` with the filtered subset, consolidating ECCV–MICCAI cousin pairs as MICCAI runs concurrently. Cross-link into AACR pathology-FM dossiers.

## Sources

- [ECCV 2026 home](https://eccv.ecva.net/)
- [ECCV 2026 Important Dates](https://eccv.ecva.net/Conferences/2026/Dates)
- [ECCV 2026 Call for Workshops](https://eccv.ecva.net/Conferences/2026/CallForWorkshops)
- [ECCV 2026 OpenReview venue](https://openreview.net/group?id=thecvf.com/ECCV/2026/Conference)
- [CV4GOOD — Computer Vision for Humanitarian Action (ECCV 2026)](https://cv4good.thegoodailab.org/)
- [ECCV 2024 Workshops list (precedent)](https://eccv.ecva.net/Conferences/2024/Workshops)
- [BioImage Computing community site](https://www.bioimagecomputing.com/) (ECCV 2018 / 2020 / 2022 / 2024 history)
- [ECCV 2022 Medical Computer Vision workshop (precedent)](https://mcv-workshop.github.io/previous/eccv2022.html)
- [Knowledge-enhanced Visual-Language Pretraining for Computational Pathology (KEP, ECCV 2024)](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06901.pdf)
- [ECVA Open Access](https://www.ecva.net/)
- [AI Lund — Preparing ECCV in Malmö Sep 2026](https://www.ai.lu.se/2025-10-15)
