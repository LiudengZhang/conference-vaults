# Synthesis — Foundation-model pathology got traction in AACR 2026

**Thesis.** Pathology foundation models (FMs) — UNI / UNI2, Virchow, CONCH, TITAN, H-optimus, Prov-GigaPath, CTransPath, DINOv2, and smaller siblings — stopped being the subject of a talk in AACR 2026 and started being infrastructure. **18 of 536 posters** in the bioinfo-tools slice (3.4%) cite at least one named pathology FM by its model name, and almost all of them use it as a tile or slide encoder for a downstream clinical task (response prediction, subtyping, biomarker inference, retrieval). Traditional deep-learning pathology — CNN / U-Net / attention-MIL pipelines — is still larger in raw count (~30 posters in the same Digital Pathology / Radiomics / Machine Learning for Image Analysis sessions), but is being **outperformed** within the same abstracts when an FM baseline is reported (#5470, #5489, #1444). The shift is real on the methodological axis but shallow on the adoption axis: CHIEF and PathChat are absent from the 2026 poster corpus, and no AACR-submitted lab has yet fine-tuned an FM for a regulatory-grade endpoint in this slice.

*Name note: auto-caption renders Faisal Mahmood correctly, but session-chair Eytan Ruppin is never spelled out in captions — he is identified by audience address as "Eitan" and by his NIH Bethesda / Ken Aldape affiliations. Transcript quotes below are lightly cleaned (paragraphing, obvious filler removed) per `docs/notes/caveats.md`.*

---

## What's new vs prior years — which pathology FMs actually appear in 2026 posters

We scanned title + abstract for every named pathology FM we could enumerate (UNI, UNI2, Virchow, CONCH, TITAN, CHIEF, PathChat, PLIP, MUSK, Hibou, Phikon, Lunit-SCOPE, H-optimus, Prov-GigaPath, CTransPath, HIPT, BiomedCLIP, REMEDIS, Kaiko, MADELEINE, RudolfV, PanDerm, KRONOS, LOKI, CA-MAE, DINOv2) with case-sensitive regex and word boundaries, then manually filtered false positives (Graphpad PRISM in #5447; DepMap PRISM library in #1464). Tallies from actual JSONL parsing:

| FM | Mentions | Posters |
|---|---|---|
| UNI / UNI2 (Mahmood lab) | 6 | #1441, #5470, #2758, #71, #4163, #5505 |
| H-optimus (Owkin) | 3 | #1444, #LB174, #5489 |
| KRONOS (spatial-proteomics) | 2 | #4163, #5505 |
| CTransPath | 2 | #83, #4151 |
| Lunit-SCOPE | 2 | #80, #1465 |
| Virchow / Virchow 2 | 1 | #1442 |
| Prov-GigaPath | 1 | #1470 |
| CONCH | 1 | #5489 |
| TITAN (CONCHv1.5 + TITAN) | 1 | #4184 |
| MUSK | 1 | #5489 |
| DINOv2 (pathology-adapted) | 1 | #2778 |
| Hibou | 1 | #4164 |
| LOKI | 1 | #5505 |
| CHIEF | **0** | — |
| PathChat | **0** | — |
| PLIP / HIPT / Phikon / BiomedCLIP / REMEDIS / Kaiko / MADELEINE / RudolfV / PanDerm | **0 each** | — |

Unique posters citing a named pathology FM: **18**. The distribution is top-heavy: UNI / UNI2 alone is in one-third of them, and CHIEF — widely discussed in the 2024-2025 literature as a generalist pathology agent — has zero AACR 2026 poster hits in this corpus.

---

## Use cases — what pathology FMs are actually being applied to

### Biomarker prediction from H&E

Posters predicting molecular or proteomic readouts from routine H&E using an FM encoder. This is the single largest use case by volume.

- **#1438** — Generative AI improves breast cancer genomic subtype prediction from histology images.
- **#1442** — Virchow 2-backed VIDCellTyper predicts spot-level tumor proportions from H&E to estimate tumor purity in TNBC.
- **#1457** — Predicts gene expression and molecular pathway activity from H&E WSIs in NSCLC.
- **#2778** — DINOv2-based patch encoder jointly trained with a spatial-transcriptomics prediction head; learns "spatial transcriptomic patterns from WSIs with a cancer-scale foundation model."
- **#87** (Path2Prot) — AI-inferred proteomic biomarkers from H&E for breast tumor subtyping and treatment response.
- **#5470** — UNI2 compared to a new low-magnification model for HER2 status prediction from H&E (noted below under counter-evidence).
- **#75** — "From single H&E to virtual immunohistochemical biomarker staining in the lung tumor microenvironment."
- **#85** (Path2Marker) — Cell-level prediction of multiplex protein expression from routine H&E.

### Subtyping and tumor grading

- **#1444** — Lauren subtype classification in gastric cancer with H-optimus-0 tile embeddings + attention-MIL.
- **#1445** — Weakly supervised TCGA molecular subtypes of gastric cancer from H&E WSIs.
- **#2758** — PAX3/7::FOXO1 fusion detection and transcriptomic prediction from WSIs of rhabdomyosarcoma using UNI2-h tile embeddings + ABMIL.
- **#78** — OncoPredikt tumor detection and biomarker quantification in breast H&E.
- **#5491** — "AI foundation model for single cell annotation from conventional histopathology images."

### Clinical outcome / response prediction

- **#1441** — UNI2-h embeddings + CLAM-style MIL for prostate cancer risk stratification.
- **#4184** — CONCHv1.5 + TITAN image encoder in a multimodal prostate cancer phenotype predictor.
- **#1454** — AI framework for image-based digital biomarkers predictive of immunotherapy response.
- **#1465** — Expression-based model benchmarked against Lunit-SCOPE for ICI response in lung cancer.
- **#4170** — AI-driven multimodal workflow for late-phase clinical trial outcome prediction.
- **#82** — "AI-derived spatial transcriptomic signatures from H&E slides predict survival."
- **#84** — Deep-learning PFS prediction for EGFR inhibitors from H&E.

### Retrieval, search, and spatial biomarker discovery

- **#4163** (KRONOS) — General-purpose AI FM for spatial proteomics, explicitly "uses representations as a search engine to retrieve similar regions within spatial proteomic data, as well as for spatial biomarker discovery" (matching Mahmood's stage claim).
- **#5505** — Unified cross-platform spatial-omics framework exposing a "foundation-model hub (UNI, KRONOS, LOKI) for panel expansion, imputation, and cross-modality retrieval."
- **#89** (TissueTrek) — Interactive web platform for exploring spatial morphology-molecular links.
- **#1470** — Prov-GigaPath embeddings for selecting representative histologic sections in 3D spatial transcriptomics.
- **#72** — Unbiased AI detection of tertiary lymphoid structures from H&E WSIs using mRNA-derived labels. The FM is used to bootstrap weak labels from the transcriptomic side into the image side.

### Scanner / QC / deployment infrastructure

Posters that wrap an FM in the plumbing required to make it usable in the hospital.

- **#4151** — Phone-based portable slide digitization system feeding CTransPath tile features into a classifier (Telepath). FM inside a point-of-care stack.
- **#4164** — Diffusion-based color checker for histological image batch correction, using Hibou mean-pooled embeddings to detect scanner-of-origin.
- **#81** — Clinical-grade QC and stain harmonization for lung WSIs (no named FM in abstract, but structured as pre-FM plumbing).
- **#4170** — Multimodal workflow targeting late-phase clinical-trial outcome prediction, with the FM as one of several modalities.

### Building / training the FM itself

- **#LB174** — H-optimus-1, a new pathology FM from Owkin.
- **#4163** — KRONOS, a general-purpose FM for spatial proteomics (variable-panel). Outperforms UNI and CA-MAE baselines on downstream tasks per abstract.
- **#5489** — Uses three FMs (CONCH, H-optimus, MUSK) at multiple magnifications as descriptors for tumor localization in RCC.

---

## Evidence from sessions

### Jakob Nikolas Kather (chairing AI Revolution, 4/20 AM) — FMs are the third wave

> "These methods allow us to analyze structured data, tabular data, features that we extracted from images. But for complex data such as image data, we needed more capable methods. So in the 2010s, deep learning came along [...] And this was supercharged by the advent of another technology, foundation models, just a couple of years ago, whereby you have a large data set, you can train a big model one time on this large heterogeneous data set, and then you can use it for many downstream tasks."
> — Session chair, *AI Revolution in Cancer Research* (transcript offset ~1103)

This is the "periodization" framing the session chair uses to set up the afternoon. Pathology FMs are claimed as the third phase after tabular ML (2000s) and deep learning (2010s).

### Faisal Mahmood (Harvard) — adoption is already at the "4 million downloads" scale

> "[UNI and CONCH] were made publicly available and have been downloaded over four million times and have been used at this point in over 2,000 different studies. So this really accelerated the utility of these models [and] shows that how important self-supervision is and how important representing data into meaningful representations can be."
> — Faisal Mahmood, *AI Revolution in Cancer Research* (transcript offset ~81314)

> "So these studies were focusing on representing... regions of pathology slides, but we also wanted to scale this to the entire slide. So last year we published Titan, which is a foundation model that focuses on representing the entirety of a whole slide image into a singular vector [...] all of the problems that we were trying to target back in 2024, these models already perform almost perfectly on those tasks."
> — Faisal Mahmood, same session (offset ~81800, ~82461)

The "almost perfectly on those tasks" qualifier is doing a lot of work: it is simultaneously a claim that the 2024 benchmark set is saturated, and a claim that the next generation (TITAN, and spatial-proteomic extensions) is already the research frontier.

### Mingyao Li (UPenn) — the bridge is H&E → spatial omics via FM-style pretraining

> "So to scale up this biological insight to the broader field, we recently developed the Foundation model. So here, we utilized the rich dataset produced by Dr. Kadaris and Dr. Wong's labs. And we build our Foundation model using 36 million cells generated from 54 tissue sections. [...] So by building this Foundation model, now the research community can simply fit in your data into our Foundation model, and we are able to give you comprehensive multi-modal information at a single-cell resolution."
> — Mingyao Li, *AI Spatial Transcriptomics & Pathology* (transcript offset ~19488)

The same session's third speaker (session chair, identified from NIH/NCI context as Eytan Ruppin) made the adoption-economics claim:

> "You only generate this training data once in principle. Well, you generate two free training data sets because you want to test and validate it, but then you're good to go for eternity just from the H&E slides. That's the whole point. [...] I think it's a no-brainer. The value is tremendous. This is transformative."
> — Session chair (Eytan Ruppin, NCI), *AI Spatial Transcriptomics & Pathology* (transcript offset ~72419)

The three claims together: (1) FMs are the third wave; (2) they are already downloaded 4M times and in 2,000+ studies; (3) once trained, the downstream economics collapse to "just the H&E slide."

---

## Counter-evidence — where traditional DL is still winning

The corpus pushes back on the stage narrative in four concrete ways.

### Matched-head-to-head benchmarks where a custom model beats an FM

- **#5470** — A low-magnification deep-learning model for HER2 prediction from H&E achieves AUC comparable to "the state-of-the-art deep learning model UNI2" (AUC 0.7150 vs 0.715), but "despite comparable accuracy, our model demonstrated markedly" better runtime / accessibility. The custom model ties UNI2 without the FM's compute cost.
- **#1465** — Expression-based immune-phenotyping ML "outperformed image-based prediction methods such as Lunit-SCOPE and PD-L1 tumor proportion score (TPS), achieving AUCs of 0.933 [...] compared to 0.733 and 0.559." This is a head-to-head defeat of a named pathology AI product by a transcriptomics model.

### Small-data tasks where FM scale doesn't help

- **#1446** — Urine cytology for bladder cancer. The poster's load-bearing finding is about focal plane quality, not a better encoder. These non-monolayer cytology specimens are not what pathology FMs were trained on.
- **#1443** — Nuclear morphometric features (interpretable, hand-crafted) distinguish histologic subtypes — no FM used.
- **#2770** (astril), **#2786** (CorrectionNet), **#2788** (multi-site lesion classification) — radiology segmentation/classification tools in Radiomics that use standard U-Net / CNN pipelines. Radiology FMs barely appear in this session.

### Interpretability-first clinical biomarker papers

- **#1447** (DIANNE) — "Segmentation-free localization of histology differential attributes." The contribution is an interpretability method, not a bigger encoder.
- **#1458** — "Deep learning of H&E slides adds prognostic value beyond IASLC grading in non-mucinous lung adenocarcinoma" — frames the contribution as additive to a standard human grading system, not as an encoder-replacement.
- **#4167** — Virtual inference of collagen architecture from H&E. Mechanistic, not FM-centric.

### Benchmark posters that probe FM limitations

- **#5478** — "Benchmarking gene expression foundation models on bulk RNA-Seq data" — tests transfer, finds it imperfect.
- **#LB159** — "A practical guideline for benchmarking unimodal and multimodal foundation models on spatial transcriptomics" — the only pathology-adjacent FM guideline poster in the corpus.
- **#4160** — "Ensuring pathologist alignment to safeguard data integrity in multi-centre oncology IVD/CDx clinical trials" — treats human-expert alignment, not FM benchmark scores, as the regulatory-grade evaluation axis.
- **#LB169** (scCAP) — Ontology-aware single-cell LLM, explicitly argues that structured grounding beats raw scale for annotation.
- **#5476** (GLEAM) — "Democratizing high-quality machine learning for cancer research" — makes a dataset / tooling argument against FM-only pipelines.
- **#LB175** — "Weakly supervised deep learning enables spatially resolved cell type inference from H&E histopathology" — positions weak supervision, not FM scale, as the key ingredient.

---

---

## Thin-evidence flags

- **FMs-for-immunohistochemistry scoring** — Only #76 (IHCExplore, "AI-driven computational pathology platform for accurate and scalable IHC scoring") and #4162 (TROP2 IHC in NSCLC) frame themselves as FM-powered IHC scoring. Corpus is too thin to argue whether IHC FMs are distinct from H&E FMs.
- **Pan-cancer retrieval at scale** — Mahmood's "search engine to retrieve similar regions" claim is represented by #4163 and #5505 at the single-study scale; no poster in the corpus deploys an FM retrieval engine over a multi-institution tumor archive.
- **CHIEF vs UNI vs Virchow head-to-heads** — Zero posters run a cross-FM comparison on a matched clinical task in this corpus; the only cross-FM use is #5489 (CONCH + H-optimus + MUSK as descriptors), which pools rather than pits them.
- **Prospective / multi-site FM deployment** — Zero posters report prospective clinical deployment of a pathology FM under a registered protocol. The closest is #4160, which is an evaluation-methodology poster, not a deployment poster.

## Closing synthesis — real shift, shallow adoption

Is FM-pathology a real shift or hype inflation at AACR 2026? The honest answer is **both, and the axis matters**. Adoption **depth** — how many labs have built pathology FMs — is narrow: a half-dozen named models (UNI/UNI2, Virchow, CONCH, TITAN, H-optimus, Prov-GigaPath, CTransPath) cover almost all the 2026 uses, and CHIEF and PathChat are absent entirely. But adoption **breadth** — how many labs now use a pathology FM as a plug-in encoder rather than rolling their own CNN/ViT — is real: 18 posters across 8 different sessions cite one by name, and several more (#82, #85, #1454, #1457, #4170) describe architectures that are clearly FM-backed but don't name the backbone in the abstract.

What AACR 2026 actually confirms is an architectural consolidation: the encoder is now assumed to be someone else's pre-trained FM, and the interesting question is what sits on top of it (MIL aggregation in #1441, multimodal fusion in #4184 and #5505, spatial biomarker discovery in #4163). Where FMs lose — to simpler custom models (#5470), to transcriptomics signatures (#1465), or to interpretable morphometrics (#1443, #1447) — it's on tasks where the extra parameters buy nothing because the clinical signal is either small-data, tabular, or inherently structured. That pattern suggests the shift is real at the **level of the representation layer** and hype-inflated at the **level of headline biomarker-prediction accuracy**: one generation in, pathology FMs are infrastructure, not products.
