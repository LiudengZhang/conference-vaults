# CVPR 2026

**IEEE/CVF Conference on Computer Vision and Pattern Recognition** — Colorado Convention Center, **Denver, Colorado, USA**, **June 3–7, 2026** (Workshops + Tutorials Jun 3–4; main conference Jun 5–7). Expected attendance ~10,000.

> **Status:** Scaffold — meeting is ~3.5 weeks out as of May 11, 2026. Final paper decisions landed Feb 20, 2026; the accepted-paper list and per-paper OpenReview pages are public; camera-ready and the full virtual program are in flight through May. The workshop slate is finalized (Wed Jun 3 / Thu Jun 4 / split half- and full-day formats). This is a **light build**, not full coverage — see "Scope" below.

## Why this is in the vault

CVPR is the premier computer-vision venue worldwide (~10,000 attendees, sibling in scale to NeurIPS / ICML) and like those two the overwhelming majority of its program is general-purpose vision — scene understanding, 3D reconstruction, autonomous-driving perception, generative image / video, robotics — with **no direct cancer-research relevance**. We are **not** trying to cover it like ISMB or MICCAI. CVPR lives in this vault for one specific reason: it is the **largest single feeder of methodology** for medical-imaging and pathology foundation models that later appear in AACR / RSNA / MICCAI translational dossiers.

The convergence points:

- **Pathology foundation models.** The AACR vault carries standalone dossiers for [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md), [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md), and [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md). The **base architectures** (DINOv2 / DINOv3-class tile encoders, slide-level aggregation transformers, multimodal CLIP-style alignment) are CVPR / ICCV / ECCV-native work. When a pathology FM cites "DINOv2-pretrained ViT-L," that ViT-L paper lived at CVPR or NeurIPS, not in *Nature Medicine*.
- **Medical vision-language models.** Radiology report generation (CXR-LLaVA, MAIRA, Merlin, RadFM-class), pathology VLMs (CONCH, PathChat, MUSK), and the broader CLIP / SigLIP / LLaVA stack all surface their core architectures at CVPR before clinical translation at RSNA / MICCAI.
- **Generative medical imaging.** Diffusion priors for MRI/CT reconstruction, synthetic data for fairness audits, and counterfactual generation for explainability all build on CVPR-mainstream diffusion (latent diffusion, ControlNet, DiT, flow matching) work.
- **Segmentation methods.** SAM / SAM-2 / EfficientSAM / SAM-Med-class adapters dominate medical segmentation downstream, and the parent SAM line is CVPR / Meta work that MICCAI workshops adapt.
- **Major feeder for AACR / MICCAI / RSNA.** A CVPR June paper on a new ViT pretraining recipe typically appears as a MICCAI September methods paper on pathology-FM v2 and an AACR April translational poster in the following spring — the 10-month adapt-to-oncology arc.

## Scope (what this vault covers — and what it does not)

**In scope (light build):**

- The **medical-imaging / biomedicine / clinical-translation workshops** at CVPR 2026 (six identified; see roster below).
- Main-track papers that match a **medical-imaging / pathology / radiology / biomedical-VLM / generative-medical-imaging / segmentation-for-medicine keyword filter** (anticipate a few dozen out of ~2,500 main-track papers).
- **Architectural building blocks** that are *known feeders* to pathology / radiology FMs even when the parent paper has no medical framing — DINOv3-class self-supervised pretraining recipes, slide-level / multi-instance aggregation transformers, SAM-line segmentation foundation models, frontier multimodal alignment methods (next-gen CLIP / SigLIP).

**Out of scope:**

- General scene understanding, 3D reconstruction, NeRF / Gaussian splatting (unless explicit medical use), autonomous-driving perception, robotics, video generation for entertainment, face / person reID, AR/VR — the >90% bulk.
- The full ~2,500-paper main proceedings; bulk extraction is explicitly **not** planned.
- Tutorials and demos outside the medical niches.
- Pure efficiency / inference-acceleration work without a medical downstream.

## Anticipated bio / health-relevant workshops

The CVPR 2026 workshop slate is finalized; six identified medical / biomedical / clinical workshops (subject to room and schedule changes through May):

| Workshop | Theme | Date | Format |
|---|---|---|---|
| **MCV** — Medical Computer Vision | 12th iteration; broad medical-imaging methods + applications | Wed Jun 3 | Full day |
| **FMV** — Foundation Models for Medical Vision | 3rd iteration; medical-imaging FMs, SAM-Med-class, RadFM-class | Wed Jun 3 | Half day |
| **MMFM-BIOMED** — Multimodal Foundation Models for Biomedicine | 2nd iteration; cross-modal medical FMs, pathology + radiology VLMs | Wed Jun 3 | Half day |
| **PHAROS AI Factory for Medical Imaging & Healthcare** | EU AI Factory project; medical imaging + healthcare deployment | Wed Jun 3 | Half day |
| **Bridging AI and Medical Reality** (CV4Clinical) | Real-world clinical translation, reliability, reproducibility | Thu Jun 4 | Half day |
| **Med-Reasoner** — Medical Reasoning with Vision Language Foundation Models | Reasoning capabilities for medical VLMs; clinician + CV researcher cross | Thu Jun 4 | Half day |

This is a notably **heavier medical workshop footprint than ICML** (which has 2–3 bio workshops out of ~10) — CVPR's pathology / radiology FM gravity is the explanation.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Main proceedings** | ~2,500 accepted papers | OpenReview venue `CVPR.thecvf.com/2026/Conference`; CVF Open Access posts camera-ready PDFs around the meeting. Full open-access proceedings (no paywall, unlike Springer LNCS for MICCAI). |
| **Workshop pages** | one per workshop, varying maturity | Six medical workshops with public sites; accepted-paper lists drop May–early June. |
| **CVF Open Access** | post-meeting full-text repository | [openaccess.thecvf.com](https://openaccess.thecvf.com/) — full PDFs typically up within ~1 week of meeting. |
| **arXiv mirrors** | most accepted papers preprint | Title-search "CVPR 2026" on arXiv finds the bulk of accepted work; widely cross-posted. |
| **bioRxiv / medRxiv mirrors** | medical-imaging subset | Pathology / radiology FM papers often dual-post; benchmark on TCGA / CPTAC / MIMIC-CXR cohorts. |
| **Social / press** | real-time reactions | `#CVPR2026` on Bluesky / X / Mastodon; useful for catching which medical workshop talks get traction. |
| **Recorded talks** | YouTube + CVF | Orals are typically recorded; workshop recording is workshop-dependent. |
| **Cross-link with MICCAI 2026** | author + tool overlap is the rule | The same lab that ships a DINOv3-medical at CVPR June will ship a pathology-FM v2 at MICCAI September — single tool entry should consolidate. |

## Organization

```
conferences/cvpr-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep — dates, filter criteria, expected themes, workshop slate
└── tools/               # per-paper / per-tool entries, populated post-meeting
    └── index.md         # template + scope-filter note
```

No `digest/`, no `themes.md`, no `keynotes/`, no `timeline.md`, no `mkdocs.yml`. The light-build pattern mirrors [ICML 2026](../icml-2026/index.md) and [NeurIPS 2026](../neurips-2026/index.md): only `tools/` gets populated, and only with the filtered subset.

## What's different from full-conference vaults

Compared to [MICCAI 2026](../miccai-2026/index.md) — the methodologically nearest medical-imaging sibling, with full proceedings coverage planned — CVPR 2026 is **scope-limited by design**:

- No per-session digests, no per-day digests, no themes synthesis. The general-vision bulk is irrelevant.
- No keynote / plenary coverage unless the speaker is a known medical-imaging / pathology-FM author.
- Tool entries are filtered down to a few dozen, not exhaustive. The filter is keyed on AACR axes + the pathology-FM dossier chain, not on CVPR's own taxonomy.
- Most CVPR 2026 tool entries should explicitly cross-link to a **MICCAI 2026 cousin paper** (same lab, September version) — the half-year arc is informative.
- Architectural-building-block entries (DINOv3 successor, SAM-3, next-gen CLIP) get an entry **only if** they have a documented or near-certain medical adoption path. Pure-vision flagship papers without a medical downstream stay out.

## Key dates

| Date | Event |
|---|---|
| Nov 3, 2025 | Workshop submission deadline — past |
| Nov 7, 2025 | Abstract submission deadline (AoE) — past |
| Nov 13, 2025 | Full paper submission deadline (AoE) — past |
| Nov 20, 2025 | Supplementary materials deadline — past |
| Dec 15, 2025 | Tutorial submission deadline — past |
| Jan 22, 2026 | Reviews released; rebuttal period opens — past |
| Jan 29, 2026 | Rebuttal period closes — past |
| **Feb 20, 2026** | Final paper decisions announced — past |
| Mar 8, 2026 | Art submissions deadline — past |
| Mar 20, 2026 | Demo submissions deadline — past |
| Mar 31, 2026 | Broadening Participation deadline — past |
| **Apr 23, 2026** | Early registration deadline — past |
| **May 13, 2026** | Cancellation deadline — **this week** |
| **Jun 3, 2026** | Workshops + Tutorials Day 1 |
| **Jun 4, 2026** | Workshops + Tutorials Day 2 |
| **Jun 5–7, 2026** | Main conference (Denver, Colorado Convention Center) |

## Sources

- [CVPR 2026 home](https://cvpr.thecvf.com/Conferences/2026)
- [CVPR 2026 Important Dates](https://cvpr.thecvf.com/Conferences/2026/Dates)
- [CVPR 2026 Workshops list](https://cvpr.thecvf.com/Conferences/2026/Workshops)
- [CVPR 2026 Call for Workshops](https://cvpr.thecvf.com/Conferences/2026/CallForWorkshops)
- [FMV — Foundation Models for Medical Vision (CVPR 2026)](https://fmv-cvpr26workshop.github.io/)
- [Med-Reasoner workshop (CVPR 2026)](https://med-reasoner.github.io/cvpr2026/)
- [CV4Clinical 2026 — Bridging AI and Medical Reality](https://cv4clinical.github.io/cv4clinical_2026/)
- [MMFM-BIOMED workshop](https://mmfm-biomed.github.io/)
- [CVF Open Access](https://openaccess.thecvf.com/)
- [CVPR-MIA paper tracker (community-maintained)](https://github.com/MedAIerHHL/CVPR-MIA)

## Cross-vault links

- **[AACR 2026](../aacr-2026/index.md)** — pathology-FM and translational-cancer side. Direct dossier links from CVPR tool pages back to:
  - [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) — pathology FM, Mahmood Lab
  - [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) — pathology FM, Microsoft / Providence
  - [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md) — pathology FM, Mahmood Lab
- **[MICCAI 2026](../miccai-2026/index.md)** — direct methodological sibling; same labs, half-year offset. Most CVPR medical-imaging tool entries here should cross-link to a MICCAI 2026 cousin.
- **[RSNA 2026](../rsna-2026/index.md)** — clinical-deployment / vendor side of medical-imaging AI. CVPR architecture → MICCAI methods paper → RSNA clinical-trial readout is the canonical 18-month arc.
- **[NeurIPS 2026](../neurips-2026/index.md)** — general ML / FM side; cross-pollinates with CVPR on diffusion methods, multimodal alignment, and biomedicine workshops (LMRL).
- **[ICML 2026](../icml-2026/index.md)** — sibling light-build template; same scope-filter approach.

## Next step

- **Now (May 11, 2026, T-3.5 weeks):** stand up template + program-notes (this commit). Begin scanning the accepted-paper list with the keyword filter; pre-stub the highest-signal entries (pathology FM updates, SAM-line medical adapters, radiology VLM new entrants).
- **Pre-meeting (T-1 to T-3 weeks):** workshop accepted-paper lists post; pull DOIs and arXiv IDs into stub pages. Cross-check authorship against the MICCAI 2026 early-accept list (which posted May 7) for cousin-paper pairing.
- **Live meeting (Jun 3–7):** opportunistic capture of slide deposits, GitHub repos, demo links from social. The Wed Jun 3 medical-workshop cluster (MCV / FMV / MMFM-BIOMED / PHAROS) is the highest-signal day.
- **Post-meeting (mid-Jun 2026 onward):** CVF Open Access proceedings post ~1 week after meeting. Bulk-populate `tools/` with the filtered subset. Estimated ~25–50 tool entries. Cross-link into AACR 2026 pathology-FM dossiers and stage MICCAI 2026 (Sep 27–Oct 1) cousin pairings.
