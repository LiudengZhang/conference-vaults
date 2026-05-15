# CHIEF

**Family:** path-fm
**Modality:** H&E whole-slide image patches (256×256 at 10×) and slide-level aggregation
**Released:** 2024 (Nature)
**License:** AGPL-3.0, non-commercial academic use only
**Code/checkpoint:** [github.com/hms-dbmi/CHIEF](https://github.com/hms-dbmi/CHIEF) (weights gated via repo request form)
**Also surfaced in:** agentic-ai, single-cell-spatial-omics, virtual-cells

> CHIEF (Clinical Histopathology Imaging Evaluation Foundation) is a
> two-stage pathology foundation model from the Mahmood Lab that maps
> H&E whole-slide images to patch- and slide-level embeddings for
> cancer detection, subtyping, biomarker prediction, and outcome
> stratification. It is trained on a multi-cancer cohort spanning 19
> anatomical sites and is positioned as a generalist model whose
> embeddings can be reused across downstream histology tasks without
> task-specific retraining.

## Architecture & training

CHIEF is built in two stages: a CTransPath-based patch encoder
(CHIEF-CTransPath) producing 768-dimensional tile embeddings, and a
weakly supervised attention-based aggregator that pools tile features
into a slide-level representation. Patch-level pretraining uses
self-supervised contrastive learning over ~15 million tiles drawn from
~60,530 whole-slide images spanning 19 anatomical sites (~44 TB of
pixel data); the slide-level head is then trained with anatomic-site
conditioning so embeddings carry organ context. The released
checkpoints are evaluated across 19,491 WSIs from 32 independent
cohorts at 24 hospitals, with reported gains on cancer detection,
genomic biomarker prediction, and survival prediction relative to
prior pathology backbones.

## Use in the AACR 2026 corpus

<!-- mentions:start -->

**Posters mentioning CHIEF (n=0):**

_No posters in the AACR 2026 corpus mention this tool._

**Sessions mentioning CHIEF (n=6):**

- [2026-04-18-ai-in-biomarker-discovery-and-drug-development](../../../sessions/2026-04-18-ai-in-biomarker-discovery-and-drug-development.md)
  …wever, that he was able to send his recorded talk. So we'll get there in a second. I'm George Visilo. I'm the Chief AI for Science Innovation at AstraZeneca, and I'm going to pass here to my impromptu co-chair. Hi. Very nice…
- [2026-04-19-gastric-gastroesophageal-cancer-dynamics](../../../sessions/2026-04-19-gastric-gastroesophageal-cancer-dynamics.md)
  …cling tuft cell into the secretory progenitor. And at the opposite end of the spectrum, these are the gastric chief stem cells. Whereas in metaplastic organoid, you can see they are more complex. So from the cycling isthmus s…
- [2026-04-20-am-plasticity-cancer-progression-clarkson-symposium](../../../sessions/2026-04-20-am-plasticity-cancer-progression-clarkson-symposium.md)
  Morning, everybody. My name is Bill Heit, and I'm honored to serve currently as the AACR Chief Scientific Advisor, but it's really my even greater honor to introduce today's symposium in honor of my frien…
- [2026-04-20-pm-ai-spatial-transcriptomics-pathology](../../../sessions/2026-04-20-pm-ai-spatial-transcriptomics-pathology.md)
  …ry and development. In this virtual biotech, it's a team of tens of thousands of AI agents, which is led by a chief scientist officer, or CSO agent, and working under the CSO agent, we have these different divisions, which co…
- [2026-04-20-pm-late-microenvironmental-determinants-tumor-evolution-immune-escape](../../../sessions/2026-04-20-pm-late-microenvironmental-determinants-tumor-evolution-immune-escape.md)
  …For gastric regeneration, we primarily use a high-dose tamoxifen model, which induces parietal cell loss and chief cell loss, and triggers PEN, a kind of metaplastic response, and normally resolve back to histological baseli…
- [2026-04-22-agentic-ai-as-the-oncologist](../../../sessions/2026-04-22-agentic-ai-as-the-oncologist.md)
  …ion Support and Human AI Collaboration. My name is Renato Umeton. I'm the Vice President of Data Sciences and Chief of AI for St. Jude Children's Research Hospital. And today we're going to explore this session with two giant…

<!-- mentions:end -->

## What's missing / where evidence is weak

- **Every corpus hit above is a false positive.** "Chief AI for Science", "Chief Scientific Advisor", "Chief of AI", "chief scientist officer", and the gastric-biology references to "chief stem cells" / "chief cell loss" all share the substring "chief" but none refer to the CHIEF pathology foundation model. The tool cleared the inclusion gate purely on alias collision.
- **No posters in the AACR 2026 corpus mention the actual model.** This is the cleanest signal that despite CHIEF being a flagship 2024 pathology FM, it did not surface in the abstracts harvested for this meeting.
- **No head-to-head benchmark against UNI or Prov-GigaPath in the corpus** — the posters that do compare pathology FMs (e.g., 4163, 5478, LB159) name UNI / UNI2 / GigaPath but not CHIEF.
- **No discussion of the AGPL-3.0 + non-commercial-academic gating** in any corpus mention; the licensing constraint is invisible here even though it likely shapes adoption.

## Takeaway

CHIEF is the textbook case for why an alias-based mention scanner needs a human pass: it scored highest of any tool by raw session count, yet none of those hits is real. The genuine signal AACR 2026 carries about CHIEF is its absence — a widely cited pathology FM that simply did not appear in the harvested abstracts or transcripts, while UNI and Prov-GigaPath did. That absence, not the false-positive count, is the data point.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** CHIEF is a two-stage pathology FM (tile encoder + weakly-supervised attention aggregator) from the Yu Lab at HMS-DBMI — distinct from the Mahmood Lab line (UNI/UNI2, CONCH, TITAN, PathChat) and from the Microsoft / Providence Prov-GigaPath line. Its CTransPath-based tile encoder is ~28M parameters, smaller than UNI (ViT-L, 307M), UNI2-h (ViT-H, 681M), Virchow (632M), and Virchow2 (632M); its distinguishing feature is the **slide-level aggregator with anatomic-site conditioning**, an architectural choice that the dominant Mahmood Lab and Microsoft alternatives handle either via separate MIL heads (UNI) or a LongNet slide encoder (Prov-GigaPath).

**Direct peers.**

| Model | Architecture | Pretraining corpus | Public weights | Headline benchmark |
| --- | --- | --- | --- | --- |
| CHIEF | CTransPath tile encoder + attention-MIL slide head, anatomic-site-conditioned | ~15M tiles, 60K WSIs, 19 anatomic sites | AGPL-3.0, gated via request form | 32-cohort eval, 19,491 WSIs (Nature 2024) |
| Virchow / Virchow2 | DINOv2 ViT-H (632M) / ViT-G (1.85B for Virchow2G) | 1.5M / 3.1M WSIs (Paige real-world) | CC-BY-NC, HF gated | 12 tile-task SOTA, biomarker prediction (Nature Medicine 2024 / arXiv 2024) |
| Hibou-B / Hibou-L | DINOv2 ViT-B (85.7M) / ViT-L | 1M+ WSIs (HistAI proprietary) | Apache-2.0, HF open | Patch-level classification, batch-correction tasks |
| PathChat / PathChat+ | Vision-language LLM, multimodal | 1M+ visual-language instructions | Mahmood Lab terms, demo-only | Diagnostic Q&A (Nature 2024); PathChat+ multi-image (arXiv 2025) |
| Prov-GigaPath | ViT tile encoder + LongNet slide encoder | 1.3B tiles, 171K WSIs | Apache-2.0, HF gated | Mutation prediction, retrieval (Nature 2024) |

**What changed in 2025-2026.** CHIEF itself has not had a new major release in 2025; the github.com/hms-dbmi/CHIEF repository remained at its initial Nature 2024 release through the year, and weights stayed gated behind a request form under AGPL-3.0 with non-commercial-academic restrictions. The landscape shifted *around* it: Virchow2 / Virchow2G (Paige, 2024-2025), UNI2-h (Mahmood, Jan 2025), CONCHv1.5 + TITAN (Mahmood, 2025), PathChat+ and SlideSeek (Mahmood, 2025) all released larger or vision-language-extended successors, while the 2025 Nat Comms clinical benchmark (Campanella et al.) put **Virchow2, Prov-GigaPath, and UNI** at the top across CPTAC tasks with CHIEF either absent from the lineup or trailing. The AGPL-3.0 + gated-weights combination has become a real adoption tax versus Apache-2.0 alternatives (Prov-GigaPath, Hibou).

**AACR-relevant use cases.** The AACR 2026 corpus contains **zero real CHIEF mentions** (all six "session hits" are alias collisions on the word "chief" — Chief Scientific Advisor, gastric chief cells, Chief of AI, etc.; see the "What's missing" section above). The relevant AACR 2026 sessions where CHIEF *could* have surfaced but did not include the [April 20 AM Decoding Cancer Ecosystem](../../../sessions/2026-04-20-am-decoding-cancer-ecosystem-pathology-tme-heterogeneity.md) (which name-checked Prov-GigaPath), the [April 20 PM AI Spatial Transcriptomics Pathology](../../../sessions/2026-04-20-pm-ai-spatial-transcriptomics-pathology.md) session, and the [April 21 Agentic AI Cancer Researcher](../../../sessions/2026-04-21-at02-agentic-ai-cancer-researcher.md) talk that explicitly featured Mahmood Lab's competing PathChat+ and SlideSeek. The honest CHIEF use-case story for AACR 2026 is that the model is **deployable in principle** for clinical pathology workflows — cancer detection, anatomic-site-aware biomarker prediction, survival stratification — but is **not deployed in this corpus**, with adoption likely capped by the AGPL-3.0 license and the rise of Apache-2.0 / CC-BY-NC competitors with comparable or stronger benchmark numbers.
