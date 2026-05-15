# RSNA 2026 — Tools

The RSNA 2026 AI track is dominated by **medical-imaging foundation models** — self-supervised models pretrained on millions of radiology images (or radiology + radiology-report pairs, or radiology + pathology jointly) that can be fine-tuned or prompted for downstream tasks: detection, segmentation, report generation, triage, risk-stratification, opportunistic screening. This directory captures one page per model / method that surfaces at RSNA 2026 with new checkpoints, clinical-deployment data, or named-trial readouts.

> **Status:** Template stub — meeting is ~7 months out. The per-tool format below is the proposal; tool entries get populated as the program goes live (late summer) and during / after the meeting. Pathology FMs already covered at AACR 2026 (CHIEF, Prov-GigaPath, UNI/UNI2) are **cross-linked, not duplicated** — see "Cross-vault links" below.

## Per-tool entry template

Each tool gets its own page (`tools/<model-slug>.md`) following this structure:

````markdown
# <ModelName>

**Family:** radiology-fm / pathology-fm / multimodal-fm / segmentation-fm / report-generation / vendor-product
**Modality:** CT / MR / X-ray / mammography / US / multimodal — be specific (e.g., "CT chest only", "whole-slide H&E + CT")
**Released:** YYYY (venue, e.g., "2025 (NEJM AI)", "2024 (Nature)")
**License:** OSI license or proprietary; note non-commercial-academic gating
**Code / checkpoint:** [repo link] + checkpoint availability (open, gated, none public)
**Vendor / sponsor:** academic group, company, or consortium
**Also surfaced in:** AACR 2026 / NeurIPS 2026 / ISMB 2026 / ASCO 2026 — short list of cross-vault hits

> One-paragraph plain-language summary: what the model does, what data it was pretrained on, what tasks it's evaluated for, what's novel about it. ~120 words.

## Architecture & training

2–4 paragraphs:
- Backbone (ViT-L, Swin, hybrid CNN-Transformer, etc.) and parameter count
- Pretraining objective (DINO, MAE, CLIP-style image-text contrastive, MoCo, etc.)
- Pretraining corpus size and composition (#images, #institutions, modalities, anatomies)
- Slide-level / volume-level / report-level aggregation if applicable
- Released checkpoint variants and what differs

## Use at RSNA 2026

<!-- For populated tools: pulled from program / Daily Bulletin / Radiology journal. -->

**Sessions / talks at RSNA 2026 (n=X):**
- Date — session — talk title — speaker — link

**Named clinical trials presenting data at RSNA 2026 (n=X):**
- Trial ID / acronym — sponsor — endpoint — readout (PFS / sensitivity / AUROC / etc.)

**AI Showcase exhibitors using this model (n=X):**
- Company — booth — product

## Cross-vault links

- AACR 2026: [link to the AACR dossier if one exists] — short note on what the AACR side covers
- ASCO 2026: [link if an imaging-driven trial readout appears at ASCO]
- JPM 2026: [link if the sponsor company presented at JPM]
- NeurIPS 2026: [link if a methods paper landed at NeurIPS]
- ISMB / RECOMB 2026: [link if a benchmark paper landed there]

## What's missing / where evidence is weak

Bullet list — honest about gaps: no head-to-head benchmark, license unclear, single-institution evaluation, no prospective deployment data, etc.

## Takeaway

1–2 sentences: what RSNA 2026 actually told us about this model beyond the paper.
````

## Tool index — candidate roster (pre-meeting)

Candidate models / methods to watch, grouped by family. Populated entries link out; unpopulated ones are tracked here for the program-notes triage pass. The roster is conservative — only models with a credible RSNA 2026 footprint (named talk, AI Showcase product, companion-publication submission) get individual pages. Otherwise they live in a roll-up paragraph in `../program-notes.md`.

### Pathology FMs (cross-linked to AACR 2026)

These are already covered in the AACR vault — the RSNA page is an extension addendum, not a duplicate.

| Model | AACR dossier | RSNA-side notes |
|---|---|---|
| CHIEF | [aacr-2026/topics/bioinfo-tools/tools/chief.md](../../aacr-2026/topics/bioinfo-tools/tools/chief.md) | Watch for radiology-pathology bridges / multimodal extensions at RSNA |
| Prov-GigaPath | [aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md](../../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) | Microsoft + Providence — sponsor may demo at AI Showcase |
| UNI / UNI2 | [aacr-2026/topics/bioinfo-tools/tools/uni.md](../../aacr-2026/topics/bioinfo-tools/tools/uni.md) | Mahmood Lab — same lab has CHIEF; watch for joint H&E + radiology presentation |

### Radiology-native FMs

| Model | Modality | Sponsor | Status at RSNA 2026 | Page |
|---|---|---|---|---|
| RadFM | multimodal (2D + 3D radiology + text) | Shanghai Jiao Tong + others | candidate — refresher-course material | TBD |
| Med-PaLM-M | multimodal (radiology + report) | Google DeepMind | candidate — informatics track | TBD |
| Merlin | abdominal CT + EHR | Stanford | candidate — opportunistic-screening sessions | TBD |
| RadDino | chest X-ray FM (DINOv2-based) | Microsoft Research | candidate — chest AI sessions | TBD |
| MAIRA-2 | chest X-ray report generation | Microsoft Research | candidate — informatics / governance | TBD |
| CheXagent | chest X-ray (multimodal LLM) | Stanford AIMI | candidate — informatics | TBD |
| LLaVA-Med / LLaVA-Rad | vision-language radiology | Microsoft + Stanford | candidate — informatics | TBD |

### Segmentation FMs

| Model | Modality | Sponsor | Status at RSNA 2026 | Page |
|---|---|---|---|---|
| MedSAM | universal medical segmentation | Wang lab (UToronto) | candidate — segmentation refresher | TBD |
| SegVol | 3D volumetric segmentation | BAAI / Tsinghua | candidate — segmentation refresher | TBD |
| Universal-MedSeg variants | various | various | placeholder | TBD |

### Screening / clinical-deployment AI (named-trial entries)

These are models with a credible RSNA 2026 trial readout — entry per model, trial cross-linked in the page.

| Model / vendor | Modality | Trial / readout | Page |
|---|---|---|---|
| Mammography AI-CAD (Lunit INSIGHT MMG, ScreenPoint Transpara, Hologic Genius AI, etc.) | mammography | AI-STREAM follow-up, BreastScreen Norway, prospective deployment audits | TBD |
| Mirai / Mirai-MRI | mammography risk + MR triage | MIRAI-MRI (NCT05968157) — supplemental MRI triggered by AI risk | TBD |
| Lung-nodule AI (various — Aidoc, Riverain ClearRead, RadAI, etc.) | chest CT | NLST-replay readouts, USPSTF-aligned screening cohorts | TBD |
| PI-RADS AI (prostate MRI) | prostate MRI | PI-RADS Steering Committee AI-development reporting standards (Radiology v1.0) | TBD |
| Body-composition / opportunistic-screening AI | abdominal CT / whole-body MRI | RSNA 2026 whole-body MRI body-composition study (May 2026 press release) | TBD |

### Methods / governance (not models)

| Topic | Why it matters | Page |
|---|---|---|
| AI bias auditing / fairness frameworks | governance refresher courses | TBD |
| FDA-cleared AI device list / regulatory snapshots | reimbursement + governance | TBD |
| ACR DSI (Data Science Institute) standards | tied to "Radiology Reimagined" IAIP demo | TBD |

## Why this format

- **One model per page, AACR-style** — the AACR `topics/bioinfo-tools/tools/` index uses the same shape. Borrowing it lets a reader hop AACR ↔ RSNA in one click without learning a second schema.
- **Cross-vault links are first-class** — pathology FMs that already have an AACR dossier don't get re-typed; they get a row in the table above plus a back-link in any RSNA addendum.
- **Trials fold into model pages** — at RSNA, most trials are evaluating a model. Indexing by model keeps trial coverage attached to its evidence base.
- **"Status" tells the reader whether they're looking at a paper-only candidate or a model with named-session footprint** — same convention as EuroBioC 2025 tools.

## Open questions for the pilot

1. **Where do vendor products go?** — *open*: an FDA-cleared AI device that's a wrapper around a public FM should probably link to both (the FM gets the model page; the vendor product gets a row in the "AI Showcase exhibitors" section of that page). Need to validate this against the actual exhibitor list when it goes public.
2. **How granular for screening AI?** — *open*: every major mammography vendor has an AI-CAD product, but lumping them into one "mammography AI-CAD" page hides head-to-head differences. Likely split if any one product has a load-bearing RSNA 2026 readout (e.g., a single-product prospective trial); otherwise stay rolled up.
3. **Cross-modality FMs (radiology + pathology)** — *open*: these straddle AACR and RSNA. Default: page lives in whichever vault hosts the named talk; the other vault gets a back-link. If the model debuts at NeurIPS / arxiv with no conference home, the page goes wherever the first deployment cohort lives.

## See also

- [RSNA 2026 program notes](../program-notes.md) — pre-meeting prep, expected FM updates, anticipated trial readouts
- [AACR 2026 bioinfo-tools index](../../aacr-2026/topics/bioinfo-tools/tools/index.md) — the pathology-FM dossier collection this directory cross-links into
- [EuroBioC 2025 tools template](../../eurobioc-2025/tools/index.md) — the per-tool format this is adapted from
