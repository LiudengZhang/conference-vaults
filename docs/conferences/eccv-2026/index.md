# ECCV 2026

**European Conference on Computer Vision** — Malmö Arena and Malmömässan, **Malmö, Sweden**, **September 8–12, 2026** (Workshops + Tutorials Sep 8–9; main conference Sep 10–12). Biennial (even years); 36th edition. Expected attendance ~6,700–7,500 (sibling in scale to CVPR / ICCV; building on ECCV 2024 Milan's 6,700+).

> **Status:** Scaffold — meeting is ~4 months out as of May 11, 2026. The submission cycle is still mid-flight: paper submissions closed Mar 5, 2026; the rebuttal period **closed today (May 11)**, and final decisions land **Jun 17, 2026** with camera-ready Jun 26. The workshop slate is **partially public** — workshop proposals were accepted Apr 12, 2026, and individual workshop sites are coming online through May–June. This is a **light build**, not full coverage — see "Scope" below.

## Why this is in the vault

ECCV is the European counterpart of CVPR and ICCV — together they form the top-3 computer-vision venue triumvirate that anchors essentially all modern vision foundation-model research. ECCV runs biennially (even years), so 2026 is an ECCV year (alternating with ICCV in odd years). Like [CVPR 2026](../cvpr-2026/index.md), the overwhelming majority of its program is general-purpose vision — 3D reconstruction, autonomous-driving perception, generative video, robotics — with **no direct cancer-research relevance**. We are **not** trying to cover it like ISMB or MICCAI. ECCV lives in this vault for one specific reason: it is the **European leg of the top-3 vision feeder pipeline** for medical-imaging and pathology foundation models that later appear in AACR / RSNA / MICCAI translational dossiers.

The convergence points (parallel to CVPR / ICCV):

- **Pathology foundation models.** The AACR vault carries standalone dossiers for [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md), [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md), and [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md). The **base architectures** (DINOv2 / DINOv3-class tile encoders, slide-level aggregation transformers, CLIP-style alignment) are CVPR / ICCV / ECCV-native work. ECCV is where the European labs (Inria, MPI, IST Austria, ETH Zurich, EPFL, Helmholtz Munich, Oxford VGG, Cambridge) flagship their tile-encoder and segmentation-FM work — and these are the **same labs** that ship pathology / radiology FMs to MICCAI and the Springer LNCS proceedings the following September.
- **Pathology and medical vision-language models.** CONCH / PathChat / MUSK / Virchow line; CXR-LLaVA / MAIRA / Merlin / RadFM line. Many of the parent CLIP / SigLIP / LLaVA architecture papers premiere at ECCV when the lead author is European. *Knowledge-enhanced Visual-Language Pretraining for Computational Pathology* (KEP, ECCV 2024) is the canonical example — direct upstream of pathology-VLM benchmarks.
- **Generative medical imaging.** Latent diffusion / DiT / flow-matching priors for MRI/CT reconstruction premiered at ECCV alongside CVPR; the European diffusion-research community (LMU Munich Compvis, EPFL, IST) is heavily represented.
- **Segmentation methods.** SAM-line successors, promptable segmentation, mask transformers — half the architectural innovation runs through ECCV (European authors) and the other half through CVPR (US authors). MICCAI consumes both.
- **Major feeder for AACR / MICCAI / RSNA.** An ECCV September paper on a new ViT pretraining recipe typically appears as a MICCAI (concurrent — same month!) methods paper on pathology-FM v2 and an AACR April translational poster the following spring. **The ECCV / MICCAI overlap is even tighter than CVPR / MICCAI** because the two meetings physically overlap in late September / early October.

## ECCV 2026 vs CVPR 2026 vs ICCV (positioning)

| Venue | When | Geography | Pathology-FM gravity | Medical-workshop footprint |
|---|---|---|---|---|
| CVPR 2026 | Jun 3–7, Denver | US-led | Heavy — six medical workshops in 2026 | High (6 workshops) |
| **ECCV 2026** | **Sep 8–12, Malmö** | **European-led** | **Heavy — European medical-imaging labs flagship here** | **Medium (workshop slate still posting; BioImage Computing recurring; medical FM workshop expected)** |
| ICCV (off-year) | n/a 2026 | Alternates US/Asia | Heavy — odd years | n/a |

The unique ECCV signal: European medical-imaging consortia (PHAROS, EuCAIM, EOSC-Life, OPTIMAL, GenomeUK, ELIXIR-DE) anchor papers here that **do not show up at CVPR**. EU regulation (EU AI Act, MDR for medical-AI deployment), federated learning across European hospital networks, and the EU-funded BraTS / KiTS / HECKTOR challenge ecosystem all run through ECCV and the co-located workshops in a way that the US venues do not replicate.

## Scope (what this vault covers — and what it does not)

**In scope (light build):**

- The **medical-imaging / biomedicine / clinical-translation workshops** at ECCV 2026 (the workshop slate is still going public — anticipated 2–4 medical / bio workshops based on ECCV 2022 + 2024 history; see roster below).
- Main-track papers that match a **medical-imaging / pathology / radiology / biomedical-VLM / generative-medical-imaging / segmentation-for-medicine keyword filter** (anticipate a few dozen out of ~2,500 main-track papers).
- **Architectural building blocks** that are *known feeders* to pathology / radiology FMs even when the parent paper has no medical framing — DINOv3-class self-supervised pretraining recipes, slide-level / multi-instance aggregation transformers, SAM-line segmentation foundation models, frontier multimodal alignment methods (next-gen CLIP / SigLIP).

**Out of scope:**

- General scene understanding, 3D reconstruction, NeRF / Gaussian splatting (unless explicit medical use), autonomous-driving perception, robotics, video generation for entertainment, face / person reID, AR/VR — the >90% bulk.
- The full ~2,500-paper main proceedings; bulk extraction is explicitly **not** planned.
- Tutorials and demos outside the medical niches.
- Pure efficiency / inference-acceleration work without a medical downstream.

## Anticipated bio / health-relevant workshops

Workshop proposal acceptance landed Apr 12, 2026; individual workshop pages are coming online through May and June. Based on recurring ECCV history (2018 / 2020 / 2022 / 2024) and the CVPR 2026 medical cluster, the following are anticipated; entries marked confirmed have public sites already.

| Workshop | Theme | Date | Status |
|---|---|---|---|
| **BioImage Computing (BIC)** | Recurring at ECCV since 2016 — bio-imaging computing for microscopy, segmentation of subcellular structures, cells, animals; deep learning for bio-imaging | Sep 8 or 9 (TBD) | Anticipated (recurring 2018 / 2020 / 2022 / 2024) |
| **Medical Computer Vision (MCV)** ECCV edition | Cross-pollinates with the CVPR MCV series; broad medical-imaging methods (last ECCV edition 2022) | Sep 8 or 9 (TBD) | Anticipated based on 2022 precedent |
| **Foundation Models for Medical Vision** ECCV variant | Could surface as ECCV-edition equivalent of the FMV CVPR series | Sep 8 or 9 (TBD) | Speculative — workshop slate not yet fully public |
| **CV4Good — Computer Vision for Humanitarian Action** | Confirmed: Good AI Lab + MSF collaboration; humanitarian-AI scope adjacent to global-health imaging | Sep 8–9 | **Confirmed** |
| **Multimodal Foundation Models for Biomedicine (ECCV variant)** | Possible ECCV companion to the CVPR MMFM-BIOMED workshop | Sep 8 or 9 (TBD) | Speculative |

This page will be revised once the official ECCV 2026 workshop list goes fully public on `eccv.ecva.net/Conferences/2026/Workshops`. The roster above is a planning placeholder, not a verified slate.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Main proceedings** | ~2,500 accepted papers (anticipated) | OpenReview venue `thecvf.com/ECCV/2026/Conference`; proceedings published by **Springer LNCS** (paywall layer, unlike CVPR's CVF Open Access) — though ECVA posts open-access PDFs at `ecva.net/papers/eccv_2026/` post-meeting. |
| **Workshop pages** | one per workshop, varying maturity | Workshop sites coming online May–August. |
| **ECVA Open Access** | post-meeting full-text repository | [ecva.net](https://www.ecva.net/) — full PDFs typically posted within ~1–2 weeks of meeting. |
| **Springer LNCS** | published proceedings | DOI-stable; sometimes paywalled before ECVA mirror. |
| **arXiv mirrors** | most accepted papers preprint | Title-search "ECCV 2026" on arXiv finds the bulk; widely cross-posted. |
| **bioRxiv / medRxiv mirrors** | medical-imaging subset | Pathology / radiology FM papers often dual-post; benchmark on TCGA / CPTAC / BraTS / HECKTOR cohorts. |
| **Social / press** | real-time reactions | `#ECCV2026` on Bluesky / X / Mastodon. |
| **Recorded talks** | YouTube + ECVA | Orals typically recorded; workshop recording is workshop-dependent. |
| **Cross-link with MICCAI 2026** | author + tool overlap is the rule | The same labs that ship a DINOv3-medical at ECCV September 8–12 will ship the pathology-FM v2 at MICCAI September 27–Oct 1 — single tool entry should consolidate. **The two meetings sit 2–3 weeks apart in 2026.** |

## Organization

```
conferences/eccv-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep — dates, filter criteria, expected themes, workshop slate
└── tools/               # per-paper / per-tool entries, populated post-meeting
    └── index.md         # template + scope-filter note
```

No `digest/`, no `themes.md`, no `keynotes/`, no `timeline.md`, no `mkdocs.yml`. The light-build pattern mirrors [CVPR 2026](../cvpr-2026/index.md), [ICML 2026](../icml-2026/index.md), and [NeurIPS 2026](../neurips-2026/index.md): only `tools/` gets populated, and only with the filtered subset.

## What's different from full-conference vaults

Compared to [MICCAI 2026](../miccai-2026/index.md) — the methodologically nearest medical-imaging sibling, with full proceedings coverage planned — ECCV 2026 is **scope-limited by design**:

- No per-session digests, no per-day digests, no themes synthesis. The general-vision bulk is irrelevant.
- No keynote / plenary coverage unless the speaker is a known medical-imaging / pathology-FM author.
- Tool entries are filtered down to a few dozen, not exhaustive. The filter is keyed on AACR axes + the pathology-FM dossier chain, not on ECCV's own taxonomy.
- Most ECCV 2026 tool entries should explicitly cross-link to a **MICCAI 2026 cousin paper** (same lab, two-to-three-week offset in Sept 2026) — the near-zero arc is uniquely tight for European medical-imaging labs.
- Architectural-building-block entries get an entry **only if** they have a documented or near-certain medical adoption path. Pure-vision flagship papers without a medical downstream stay out.

## Key dates

| Date | Event |
|---|---|
| Feb 15, 2026 | Tutorial proposals deadline — past |
| Feb 26, 2026 | Paper registration deadline — past |
| Feb 27, 2026 | Workshop proposals deadline (AoE) — past |
| Mar 5, 2026 | Full paper submission deadline (AoE) — past |
| Mar 12, 2026 | Supplemental materials deadline — past |
| Apr 12, 2026 | Workshop / tutorial acceptance notifications — past |
| **May 11, 2026** | **Rebuttal period closes (9:00 PM UTC) — today** |
| Jun 14, 2026 | AI Art submissions deadline |
| **Jun 17, 2026** | **Final paper decisions announced** |
| Jun 26, 2026 | Camera-ready deadline |
| Jun 29, 2026 | AI Art acceptance notifications |
| **Sep 8, 2026** | Workshops + Tutorials Day 1 |
| **Sep 9, 2026** | Workshops + Tutorials Day 2 |
| **Sep 10–12, 2026** | Main conference (Malmö Arena + Malmömässan) |

## Sources

- [ECCV 2026 home](https://eccv.ecva.net/)
- [ECCV 2026 Important Dates](https://eccv.ecva.net/Conferences/2026/Dates)
- [ECCV 2026 Call for Workshops](https://eccv.ecva.net/Conferences/2026/CallForWorkshops)
- [ECCV 2026 Expo / Sponsorship](https://eccv.ecva.net/Conferences/2026/Expo)
- [ECCV 2026 OpenReview venue](https://openreview.net/group?id=thecvf.com/ECCV/2026/Conference)
- [CV4GOOD — Computer Vision for Humanitarian Action (ECCV 2026)](https://cv4good.thegoodailab.org/)
- [BioImage Computing — community site](https://www.bioimagecomputing.com/) (workshop has run at ECCV 2018 / 2020 / 2022 / 2024)
- [ECVA Open Access](https://www.ecva.net/)
- [AI Lund — Preparing ECCV in Malmö Sep 2026](https://www.ai.lu.se/2025-10-15)

## Cross-vault links

- **[AACR 2026](../aacr-2026/index.md)** — pathology-FM and translational-cancer side. Direct dossier links from ECCV tool pages back to:
  - [CHIEF](../aacr-2026/topics/bioinfo-tools/tools/chief.md) — pathology FM, Mahmood Lab
  - [Prov-GigaPath](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) — pathology FM, Microsoft / Providence
  - [UNI](../aacr-2026/topics/bioinfo-tools/tools/uni.md) — pathology FM, Mahmood Lab
- **[CVPR 2026](../cvpr-2026/index.md)** — direct sibling vision conference; same scope-filter approach. Six-medical-workshop comparator. Many ECCV authors are the European complement of the CVPR US-led cohort.
- **[MICCAI 2026](../miccai-2026/index.md)** — direct methodological sibling; same labs, 2–3 week offset (MICCAI follows ECCV by ~2.5 weeks in 2026: Sep 27–Oct 1). **Most ECCV medical-imaging tool entries should cross-link to a MICCAI 2026 cousin.**
- **[RSNA 2026](../rsna-2026/index.md)** — clinical-deployment / vendor side of medical-imaging AI. ECCV architecture → MICCAI methods paper → RSNA clinical-trial readout is the canonical 12-month arc.
- **[NeurIPS 2026](../neurips-2026/index.md)** — general ML / FM side; cross-pollinates with ECCV on diffusion methods, multimodal alignment, and biomedicine workshops (LMRL).
- **[ICML 2026](../icml-2026/index.md)** — sibling light-build template; same scope-filter approach.

## Next step

- **Now (May 11, 2026, T-17 weeks):** stand up template + program-notes (this commit). The submission cycle is mid-flight — final decisions land Jun 17, so the accepted-paper list is **not yet public**. No keyword filtering possible against accepts until late June.
- **Pre-meeting (Jun 17 – Sep 7, T-12 weeks → T-1 day):** accept list goes public Jun 17; camera-ready Jun 26; arXiv mirrors land June–August. Begin keyword-scanning then. Workshop accepted-paper lists post on individual workshop sites through July–August. Cross-check authorship against the MICCAI 2026 accept list for cousin-paper pairing.
- **Live meeting (Sep 8–12):** opportunistic capture of slide deposits, GitHub repos, demo links from social. Sep 8–9 workshop cluster (BioImage Computing + medical workshops if confirmed + CV4Good) is the highest-signal pair of days for the vault filter.
- **Post-meeting (mid-Sep 2026 onward):** ECVA Open Access proceedings post ~1–2 weeks after meeting. Bulk-populate `tools/` with the filtered subset. Estimated ~20–40 tool entries. Cross-link into AACR 2026 pathology-FM dossiers and **immediately stage MICCAI 2026 (Sep 27–Oct 1) cousin pairings — the two meetings overlap in time, so dual-coverage capture is the day-of-meeting workflow.**
