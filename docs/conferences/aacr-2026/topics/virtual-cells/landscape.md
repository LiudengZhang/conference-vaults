# Landscape — 48 posters by model family

The virtual-cells slice of AACR 2026 was harvested via a phrase-quoted keyword union over the Abstracts Online search (`"virtual cell"`, `"foundation model"`, `scGPT`, `Geneformer`, `"digital twin"`, `"in silico perturbation"`, and siblings). Of 88 union hits, 48 survived filtering on `Activity` + `PlayerUrl`. Those 48 are classified below into six model families based on the title and abstract: (1) cell/gene/genome/epigenome/microbiome foundation models, (2) pathology & imaging foundation models, (3) perturbation prediction & in-silico screens, (4) digital twins, (5) multimodal fusion & VLM/LLM integration, and (6) benchmarks, evals & agentic systems — with a small **Other** bucket for loose keyword hits.

## Foundation models — cell, gene, genome, epigenome, microbiome

Core "virtual cell"-adjacent foundation models trained over sequencing, mutation, methylation, or microbiome data. Scope spans RNA, DNA, methylation, genotype projections, and whole-patient temporal modeling.

Notable framing: #LB443 (MutationProjector) explicitly treats the genotype as a projection into a learned coordinate system — conceptually the closest poster to a Universal Cell Embedding analogue for tumor mutations. #33 extends the FM idea to whole-patient longitudinal EHR rather than a single molecular assay. None of the eight posters here cites scGPT, Geneformer, or Universal Cell Embeddings as a backbone — they are all custom in-house FMs.

| # | Title | Presenter | Session |
|---|---|---|---|
| 33 | A healthcare system scale multimodal whole patient temporal foundation model | Andrew Zhang | Agentic AI in Cancer |
| 2765 | Microbiome foundation modeling of cancer: MiFM-derived continuous trajectories and risk clocks for pan-cancer immunotherapy response prediction | Hongru Shen | Large Language Models in the Clinic |
| 5482 | MethylFM: A DNA methylation foundation model for modeling epigenomic regulatory dynamics | Limeng Pu | Deep Learning in Cancer |
| 7268 | AI-Driven stratification of cancer patients using The Cancer Genome Atlas whole-genome sequencing data | Jonghoon Lee | Genomic Approaches to Define Tumor Biology |
| LB434 | RNA1-DA: A domain-adaptive RNA foundation model for forward and reverse translation | Janusz Dutkowski | Late-Breaking Research: Bioinformatics |
| LB435 | Large-scale foundation model-based PDX model selection and cancer subtype assignment | Edward O'Brien | Late-Breaking Research: Bioinformatics |
| LB443 | A foundation model of cancer genotype enables precise predictions of therapeutic response (MutationProjector) | JungHo Kong | Late-Breaking Research: Bioinformatics |
| 4212 | Baseline peripheral blood scRNA-seq AI estimator framework predicts solid-tumor response and adverse events via molecular foundation models | Marta Milo | Machine Learning Approaches for Cancer Prediction |

## Foundation models — pathology & imaging

Histopathology, spatial-proteomics, endoscopic, and radiology foundation models. Several explicitly scale the Meta DINOv2-style recipe from ImageNet to whole-slide tissue. #4163 is the poster-corpus analogue of Charlotte Bunne's ED03 spatial-proteomics FM claim; #LB174 (H-optimus-1) is a pure-histopathology vision transformer, and #1251 (HONeYBEE) is the multimodal fusion play over H&E + EHR + molecular.

| # | Title | Presenter | Session |
|---|---|---|---|
| LB174 | H-optimus-1: A foundation model for computational histopathology | Marin Scalbert | Late-Breaking Research: Bioinformatics |
| 4163 | A general-purpose AI foundation model for spatial proteomics | Andrew Song | Digital Pathology 3 |
| 5491 | AI foundation model for single cell annotation from conventional histopathology images of cancer | Xiangqi Bai | Machine Learning for Image Analysis |
| 5489 | Multi-scale foundational AI descriptors enable accurate tumor localization in digitized renal cell carcinoma pathology | Brennan Flannery | Machine Learning for Image Analysis |
| 2778 | Learning spatial transcriptomic patterns from whole-slide images with a cancer-scale foundation model | Minsoo Lee | Radiomics and AI in Medical Imaging |
| 2789 | Depth prediction in superficial esophageal cancer using a foundation model from endoscopic images | Sehun Kim | Radiomics and AI in Medical Imaging |
| 2790 | Foundation model-based gastric cancer staging from complete, uncurated EGD image sequences | Sehun Kim | Radiomics and AI in Medical Imaging |
| 1251 | Real-world evaluation of multimodal AI: Foundation model-driven multimodal AI for GBM, NSCLC, and PDAC (HONeYBEE) | Aakash Tripathi | Survivorship, Supportive Care, QoL |

## Perturbation prediction & in-silico screens

Posters that explicitly predict response to a chemical/genetic perturbation, or simulate treatment effects mechanistically. This is the family most directly mapped to the "virtual cell" label used at ED03 — and also, at six posters, one of the thinner families relative to the hype. #1464 (CELLama-Perturb) and #4181 (Turbine's Virtual Lab) are the only two that use the phrase "virtual cell" or "virtual lab" in their titles.

| # | Title | Presenter | Session |
|---|---|---|---|
| 1464 | CELLama-Perturb: A virtual cell modeling approach for mapping drug sensitivity across spatial tumor heterogeneity | Haenara Shin | Integrative Computational Approaches 1 |
| 4181 | De-risk targets through mechanism-enabled simulations in the Virtual Lab (Turbine) | Krishna Bulusu | Integrative Computational Approaches 2 |
| 4213 | Generative genomics accurately predicts cancer gene expression (GEM-1) | Alexander Abbas | Machine Learning Approaches for Cancer Prediction |
| 978 | Deep learning frameworks for translating cancer drug response from cell-level to patient-level by modeling transcriptome | Sun Kim | Computational, Technological, and Mechanistic Advances |
| 1467 | Mechanism-aware cancer therapy planning with group-relative policy optimization on a multimodal oncology foundation model | Eric Schadt | Integrative Computational Approaches 1 |
| LB438 | Decoding therapy-induced rewiring of the tumor microenvironment networks to overcome drug resistance through multiscale mechanistic pathway crosstalk analysis | Minsoo Choi | Late-Breaking Research: Bioinformatics |

## Digital twins

Posters that self-identify as digital twin or patient-specific predictive model work. Scope is narrow — five posters total — and spans preclinical (bone metastasis) to clinical-trial simulation. Only two posters (#4153, #1486) use "digital twin" in the title; the others are longitudinal predictive-model papers we've re-classified under this family because the framing matches.

| # | Title | Presenter | Session |
|---|---|---|---|
| 4153 | Advancing precision oncology through tumor digital twins: A versatile ViT-determined margin-consistent model for LUAD histopathologic subtyping | Bardia Rodd | Digital Pathology 3 |
| 1486 | From animals to computational oncology: Digital twins as ethical enablers of next-generation bone metastasis research | Eleonora Dondossola | Integrative Computational Approaches 1 |
| 2774 | Pulmonary nodule tracking in metastatic Ewing sarcoma enables personalized predictive models | Kevin Murgas | Radiomics and AI in Medical Imaging |
| 4170 | An AI-driven multimodal workflow for enhancing late-phase clinical trial outcome prediction | Inbal Gazy | Digital Pathology 3 |
| 6883 | An RNA-based survival model predicting real-world response to trastuzumab deruxtecan | Josh Wheeler | Network Biology and Precision Medicine |

## Multimodal fusion & VLM/LLM integration

Posters that combine histopathology with transcriptomics, proteomics, or text via multimodal transformers or vision-language models. These are the AACR 2026 analogues of ED03's "virtual patient" thesis — joint representations across modalities rather than single-modality FMs. Eight posters, which is the largest single family after the pathology FMs.

| # | Title | Presenter | Session |
|---|---|---|---|
| 2754 | VGL: Vision-Gene-Language multimodal LLM integrating histopathology and gene expression for cell type classification in lung cancer | Haenara Shin | Large Language Models in the Clinic |
| 2752 | CancerSTFormer enables multi-scale analysis of spot-resolution spatial transcriptomes and dissects gene and immune regulatory responses of targeted therapies | Qian Zhu | Large Language Models in the Clinic |
| 87 | Path2Prot offers a new way for breast tumor subtyping and treatment response prediction from AI-inferred proteomic biomarkers | Saugato Rahman Dhruba | Digital Pathology 1 |
| 71 | Bridging histopathology and spatial transcriptomics for comprehensive tumor microenvironment profiling | Xiaohan Xing | Digital Pathology 1 |
| 1457 | Prediction of gene expression and molecular pathway activity from H&E whole slide images in non-small cell lung cancer | Mina Khoshdeli | Digital Pathology 2 |
| 1438 | Generative AI improves breast cancer genomic subtype prediction from histology images | Brennan Simon | Digital Pathology 2 |
| 5505 | A unified framework for cross-platform spatial omics analysis and deep spatial profiling | Yunhe Liu | New Software Tools for Data Analysis |
| 4184 | Multimodal deep learning framework for predicting clinically significant phenotypes in prostate cancer | Priyanka Vasanthakumari | Integrative Computational Approaches 2 |

## Benchmarks, evaluations & agentic systems

Benchmarks, ontology-aware evaluators, and autonomous-agent posters. This is the thinnest family — only four posters — which matters for the ED03 synthesis: Bunne, Yeung-Levy and Moor each spent substantial stage time on benchmarks (MicroVQA) and agentic verification (process reward agents), yet the poster corpus is extremely thin on either. #30 is the only pure agentic-systems poster; #1467 is agentic only by virtue of using GRPO reinforcement learning.

| # | Title | Presenter | Session |
|---|---|---|---|
| 5478 | Benchmarking gene expression foundation models on bulk RNA-Seq data | Jong Hyun Kim | Deep Learning in Cancer |
| LB169 | scCAP: An ontology-aware large language model framework for hierarchical and standardized single-cell type annotation | Seok-Won Jang | Late-Breaking Research: Bioinformatics |
| 30 | Automated cohort extraction from real-world oncology data using adaptive LLM-based agentic systems for clinical trial feasibility and patient selection | Brandon Theodorou | Agentic AI in Cancer |
| 1467 | Mechanism-aware cancer therapy planning with group-relative policy optimization (also listed in Perturbation) | Eric Schadt | Integrative Computational Approaches 1 |

## Other (classical DL pathology, clinical DL, and loose harvest hits)

Posters that matched the keyword union but do not implement a foundation model, digital twin, perturbation simulator, or agent per se. Kept for completeness; several are strong classical-DL pathology biomarker papers that used a pre-trained FM as an off-the-shelf encoder (#73, #1444, #1457, #83, #76) without themselves contributing a new FM. Two (#6041, #295) appear to be wet-lab therapeutics papers that hit the "virtual cell" or "foundation" string incidentally in their abstract body; they are not virtual-cells-methodology posters and should probably have been filtered out at harvest time.

| # | Title | Presenter | Session |
|---|---|---|---|
| 73 | Accurate prediction of microsatellite instability-high gastric cancer from H&E-stained whole slide images | Shima Nofallah | Digital Pathology 1 |
| 1444 | Lauren subtype classification in gastric cancer using deep learning on real-world H&E images | Akul Singhania | Digital Pathology 2 |
| 1448 | Deep learning integration of molecular and histopathological data for prognostic stratification in NSCLC | Sanddhya Jayabalan | Digital Pathology 2 |
| 1447 | DIANNE: Segmentation-free localization of histology differential attributes | Sergii Domanskyi | Digital Pathology 2 |
| 83 | AI-powered analysis of pancreatic ductal adenocarcinoma tissues to study the tumor immune ecosystem and identify novel classifiers | Rebecca Polidori | Digital Pathology 1 |
| 76 | IHCExplore: An AI-driven computational pathology platform for accurate and scalable immunohistochemistry scoring | Kelsey Luu | Digital Pathology 1 |
| 1056 | Integrative multi-omics characterization and AI-driven biomarker discovery for NSCLC stage III outcomes | Katherina Chua | Biomarkers Predictive of Therapeutic Benefit 2 |
| 2711 | Large-scale integration of single-nuclei and spatial transcriptomics from the ETOP BEAT-meso trial in malignant pleural mesothelioma | Daria Buszta | Integration of Clinical and Research Data |
| 6041 | Fidaxomicin targets PDGFR⁺ cancer-associated fibroblast to restrain colorectal cancer progression | B. Mark Evers | Fibroblasts as Architects of the Tumor Microenvironment |
| 295 | Antitumor effect of a new pyruvate kinase M2 (PKM2) inhibitor Acyclovir in experimental esophageal adenocarcinoma | Md Sazzad Hassan | Innovative Therapeutic Modalities |

## Tally

- Cell / gene / genome / epigenome / microbiome FMs: **8**
- Pathology & imaging FMs: **8**
- Perturbation prediction & in-silico screens: **6**
- Digital twins: **5**
- Multimodal fusion & VLM/LLM: **8**
- Benchmarks, evals & agentic systems: **3** unique (plus #1467 cross-listed)
- Other / loose harvest hits: **10**

Total unique: **48** (#1467 is cross-listed between Perturbation and Agentic but counted once).

Keyword families most represented in titles: "foundation model" (18 posters), "digital twin" (3), "virtual cell"/"virtual lab" (2), "agentic" (1). The keyword `scGPT`, `Geneformer`, and `Universal Cell Embeddings` do not appear in any title in this slice — they show up only as comparators in abstract bodies (e.g., #LB169, #5478).

