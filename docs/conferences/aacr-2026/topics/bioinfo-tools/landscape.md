# Landscape — 536 posters by method family

The bioinfo-tools slice of AACR 2026 was harvested via the AACR Abstracts Online **Session endpoint** (`/Session/<sid>/Presentations`) rather than a keyword union, so 536 records map tightly onto 24 methods-oriented poster sessions (Digital Pathology 1-3, Application of Bioinformatics to Cancer Biology 1-5, Integrative Computational Approaches 1-2, New Software Tools for Data Analysis, New Algorithms and Computational Methods, Network Biology and Precision Medicine, Computational/Technological/Mechanistic Advances, Radiomics and AI in Medical Imaging, Machine Learning Approaches for Cancer Prediction, Machine Learning for Image Analysis, Deep Learning in Cancer, Large Language Models in the Clinic, Agentic AI in Cancer, Late-Breaking Bioinformatics 1-2, Molecular Pathology, Innovative Therapeutic Modalities and Translational Platforms).

The seven buckets below were assigned by regex over title + abstract, then manually reviewed for false positives (e.g., "PRISM" for Graphpad or DepMap PRISM is dropped; "Atlas" as a resource vs. a model name is disambiguated). A poster can appear in more than one bucket — the tallies are per-bucket memberships, not mutually exclusive counts.

## Digital pathology foundation models

Posters that either train a new pathology / spatial-imaging foundation model (FM) or use a named, pre-trained pathology FM (UNI/UNI2, Virchow, CONCH, TITAN, H-optimus, Prov-GigaPath, CTransPath, Hibou, MUSK, DINOv2, Lunit-SCOPE, KRONOS, LOKI, MADELEINE, CA-MAE) as a tile or slide encoder. **18 posters** cite at least one of these FMs by name; one of them (#LB174) trains a new pathology FM from scratch. #4163 (KRONOS) is the corpus analog of the "general-purpose AI FM for spatial proteomics" shown from stage by Faisal Mahmood.

| # | Title | Presenter | Session |
|---|---|---|---|
| LB174 | H-optimus-1: A foundation model for computational histopathology | Marin Scalbert | Late-Breaking Research: Bioinformatics 1 |
| 4163 | A general-purpose AI foundation model for spatial proteomics | Andrew Song | Digital Pathology 3 |
| 5491 | AI foundation model for single cell annotation from conventional histopathology images of cancer | Xiangqi Bai | Machine Learning for Image Analysis |
| 5489 | Multi-scale foundational AI descriptors enable accurate tumor localization in digitized renal cell carcinoma pathology | Brennan Flannery | Machine Learning for Image Analysis |
| 2778 | Learning spatial transcriptomic patterns from whole-slide images with a cancer-scale foundation model | Minsoo Lee | Radiomics and AI in Medical Imaging |
| 5505 | A unified framework for cross-platform spatial omics analysis and deep spatial profiling | Yunhe Liu | New Software Tools for Data Analysis |
| 71 | Bridging histopathology and spatial transcriptomics for comprehensive tumor microenvironment profiling | Xiaohan Xing | Digital Pathology 1 |
| 1441 | Whole-slide image and clinical feature integration for superior prostate cancer risk stratification | Piotr Bakalarski | Digital Pathology 2 |
| 1442 | Spatial transcriptomics informed tumor purity estimation from histology slides for triple negative breast cancer | (VIDCellTyper team) | Digital Pathology 2 |
| 1444 | Lauren subtype classification in gastric cancer using deep learning on real-world H&E images | Akul Singhania | Digital Pathology 2 |
| 2758 | PAX3/7::FOXO1 fusion detection and transcriptomic prediction from whole-slide images of rhabdomyosarcoma | (ABMIL + UNI2-h team) | Large Language Models in the Clinic |
| 5470 | Low-magnification deep learning model for rapid HER2 status prediction from H&E whole-slide images | (UNI2 comparison team) | Deep Learning in Cancer |
| 4184 | Multimodal deep learning framework for predicting clinically significant phenotypes in prostate cancer | Priyanka Vasanthakumari | Integrative Computational Approaches 2 |
| 4164 | Implementation of a diffusion-based color checker for histological image batch correction | (Hibou team) | Digital Pathology 3 |
| 1470 | Selecting representative histologic sections for cost-efficient 3D spatial transcriptomics and tumor context modeling | (Prov-GigaPath team) | Integrative Computational Approaches 1 |
| 83 | AI-powered analysis of pancreatic ductal adenocarcinoma tissues to study the tumor immune ecosystem | Rebecca Polidori | Digital Pathology 1 |
| 80 | Quantitative assessment of tumor-infiltrating lymphocytes using AI in non-small cell lung cancer (SCOPE IO platform) | (Lunit team) | Digital Pathology 1 |
| 1465 | Expression-based immune-phenotyping ML model predict ICI response and long-term clinic benefit in lung cancer (vs Lunit-SCOPE) | (benchmark team) | Integrative Computational Approaches 1 |
| LB159 | A practical guideline for benchmarking unimodal and multimodal foundation models on spatial transcriptomics | (benchmark team) | Late-Breaking Research: Bioinformatics 1 |

## Traditional deep-learning pathology

Posters that use CNN / U-Net / ResNet / MIL / attention-MIL / ViT pipelines on WSI or other imaging modalities without a named pathology FM. This family remains larger than the FM-pathology family by raw poster count (~30 posters across Digital Pathology 1-3, Machine Learning for Image Analysis, and Radiomics), and includes several strong clinical biomarker works.

| # | Title | Presenter | Session |
|---|---|---|---|
| 73 | Accurate prediction of microsatellite instability-high gastric cancer from H&E-stained whole slide images | Shima Nofallah | Digital Pathology 1 |
| 78 | OncoPredikt: A deep-learning framework for tumor detection and biomarker quantification in breast H&E | (OncoPredikt team) | Digital Pathology 1 |
| 82 | Artificial intelligence derived spatial transcriptomic signatures from H&E slides predict survival | (signature team) | Digital Pathology 1 |
| 84 | Deep-learning prediction of progression-free survival to EGFR inhibitors from H&E tissue slides | (EGFR team) | Digital Pathology 1 |
| 1440 | FLEXMIL: A flexible multimodal multiple instance learning framework for clinical and translational pathology | (FLEXMIL team) | Digital Pathology 2 |
| 1445 | Predicting TCGA molecular subtypes of gastric cancer from H&E whole-slide images using a weakly supervised model | (weakly-sup team) | Digital Pathology 2 |
| 1446 | Accurate focal plane is crucial for AI assessment of non-monolayer urine cytology specimens | (cytology team) | Digital Pathology 2 |
| 1447 | DIANNE: Segmentation-free localization of histology differential attributes | Sergii Domanskyi | Digital Pathology 2 |
| 1448 | Deep learning integration of molecular and histopathological data for prognostic stratification in NSCLC | Sanddhya Jayabalan | Digital Pathology 2 |
| 1458 | Deep learning of H&E slides adds prognostic value beyond IASLC grading in non-mucinous lung adenocarcinoma | (IASLC team) | Digital Pathology 2 |
| 2770 | astril: Automated segmentation toolkit for radiology image libraries | (astril team) | Radiomics and AI in Medical Imaging |
| 2783 | Lung cancer intelligent detection (LUCID) using a universally accessible, cross-platform, AI-powered tool | (LUCID team) | Radiomics and AI in Medical Imaging |
| 2786 | CorrectionNet: A lightweight residual refinement framework for improving medical image segmentation | (CorrectionNet team) | Radiomics and AI in Medical Imaging |
| 2788 | Multi-site development of automated lesion classification for comprehensive tumor burden assessment | (lesion team) | Radiomics and AI in Medical Imaging |
| 5490 | Scalable and interpretable multimodal AI: Integrating imaging and genomics via image-based encoding | (SIM-AI team) | Machine Learning for Image Analysis |

## Benchmarking / evaluation frameworks

Formal benchmarks, evaluator frameworks, and reference-dataset construction papers. The FM-evaluation axis is notably stronger here than in the sibling virtual-cells slice: #5478 is a direct gene-expression-FM benchmark, #LB159 is explicitly framed as a practical guideline for spatial-transcriptomics FMs, and #4160 treats *pathologist alignment itself* as the evaluation layer for regulated IVD/CDx trials.

| # | Title | Presenter | Session |
|---|---|---|---|
| 5478 | Benchmarking gene expression foundation models on bulk RNA-Seq data | Jong Hyun Kim | Deep Learning in Cancer |
| LB159 | A practical guideline for benchmarking unimodal and multimodal foundation models on spatial transcriptomics | (SpaTxBench team) | Late-Breaking Research: Bioinformatics 1 |
| 4160 | Ensuring pathologist alignment to safeguard data integrity in multi-centre oncology IVD/CDx clinical trials | (alignment team) | Digital Pathology 3 |
| LB169 | scCAP: An ontology-aware large language model framework for hierarchical and standardized single-cell type annotation | Seok-Won Jang | Late-Breaking Research: Bioinformatics 1 |
| 5476 | GLEAM: Democratizing high-quality machine learning for cancer research | (GLEAM team) | Deep Learning in Cancer |
| 2739 | Evaluation of large language models for automated clinical trial matching in oncology | (trial-matching team) | Large Language Models in the Clinic |
| 2747 | Source discipline matters: Guideline anchored large language model outperforms Open Evidence for decision support | (guideline team) | Large Language Models in the Clinic |
| 5496 | From transcripts to cells: Dissecting sensitivity, signal contamination, and specificity in Xenium segmentation | (Xenium benchmark team) | New Software Tools for Data Analysis |
| 6906 | Test-time compute for subtype classification in pediatric T-cell acute lymphoblastic leukemia | (test-time team) | New Algorithms and Computational Methods |
| 981 | MTA-DTA: A multi-token attention framework for drug-target binding affinity prediction | (MTA-DTA team) | Computational, Technological, and Mechanistic Advances |

## Data infrastructure / atlases / resources

Posters that ship a queryable resource, knowledge graph, atlas, public database, or harmonization pipeline rather than a novel model per se. This includes COSMIC and the UCSC Xena / TCGA / CCDI / Human Tumor Atlas Network records — long-running community infrastructure that anchors almost every downstream method.

| # | Title | Presenter | Session |
|---|---|---|---|
| 56 | COSMIC: Advancing the cancer genomics knowledgebase of somatic mutations | (COSMIC team) | Application of Bioinformatics 1 |
| 2704 | NCI's childhood cancer data initiative: Advancing pediatric cancer research | (CCDI team) | Application of Bioinformatics 3 |
| 4169 | Reading the map: An invitation to the resources of the Human Tumor Atlas Network | (HTAN team) | Digital Pathology 3 |
| 5524 | Visualization and analysis of cancer genomics data using UCSC Xena | (UCSC Xena team) | New Software Tools for Data Analysis |
| 4147 | CEDAR: A comprehensive database of curated cancer epitopes and receptors | (CEDAR team) | Application of Bioinformatics 5 |
| 5501 | A quantum-enabled atlas-scale resource to study metabolic landscapes and heterogeneity in cancer TME | (quantum-atlas team) | New Software Tools for Data Analysis |
| 5521 | MeDOC-KB: Knowledge base for unraveling the metabolic links between obesity-related cancers | (MeDOC-KB team) | New Software Tools for Data Analysis |
| 2688 | A unified prostate cancer single-cell atlas reveals molecular subtypes and lineage plasticity | (prostate atlas team) | Application of Bioinformatics 2 |
| 4195 | OncoGraphDB: Rapid projections of patient-level multimodal graph database | (OncoGraphDB team) | Integrative Computational Approaches 2 |
| 6892 | A pan-cancer atlas of telomere length in tissues and plasma cell-free DNA | (telomere atlas team) | New Algorithms and Computational Methods |
| 5451 | Omicology: A comprehensive AI/LLM/NLP-based web resource for the ontology, phylogeny, and practical annotation | (Omicology team) | Application of Bioinformatics 4 |
| 4174 | hla2vec: Developing a HLA embedding space using probabilistic cross-reactive groups | (hla2vec team) | Integrative Computational Approaches 2 |
| 6865 | A knowledge graph screen of innovative versus incremental lung cancer trials for need-aligned design | (KG-trial team) | Network Biology and Precision Medicine |
| 1426 | A single-cell tumor atlas defines robust pathway and gene signatures enabling cancer cell-line fidelity | (atlas team) | Application of Bioinformatics 1 |

## Clinical decision support / prediction models

Posters whose primary output is a patient-level prediction — survival, recurrence, treatment response, ICI response, prognosis — grounded in at least one model trained on clinical endpoints. This is the **largest** bucket in the corpus (~45 posters by keyword, and a plurality of Digital Pathology 2 + Machine Learning Approaches for Cancer Prediction sessions). Representative posters selected across tissue types.

| # | Title | Presenter | Session |
|---|---|---|---|
| 87 | Path2Prot offers a new way for breast tumor subtyping and treatment response prediction from AI-inferred proteomic biomarkers | Saugato Rahman Dhruba | Digital Pathology 1 |
| 1441 | Whole-slide image and clinical feature integration for superior prostate cancer risk stratification | Piotr Bakalarski | Digital Pathology 2 |
| 1454 | Development of an AI framework for identifying image based digital biomarkers predictive of immunotherapy response | (IO-biomarker team) | Digital Pathology 2 |
| 1482 | A deep learning-based multimodal integration framework for clinical outcome prediction | (clinical-integration team) | Integrative Computational Approaches 1 |
| 1485 | Multimodal AI for patient subtype discovery in LUSC using real-world data | (LUSC team) | Integrative Computational Approaches 1 |
| 4206 | The ancestry-transcriptome link: Machine learning predicts chemotherapy response in breast cancer | (ancestry team) | Machine Learning Approaches for Cancer Prediction |
| 4212 | Baseline peripheral blood scRNA-seq AI estimator framework predicts solid-tumor response and adverse events | Marta Milo | Machine Learning Approaches for Cancer Prediction |
| 4217 | Multi-modal modeling of genomic, histopathologic, and lab data predicts survival after hepatectomy | (hepatectomy team) | Machine Learning Approaches for Cancer Prediction |
| 1432 | Single-cell-derived gene-pair classifiers for prostate cancer prognostication | (gene-pair team) | Application of Bioinformatics 1 |
| 1484 | p-EMT transitional hub and its DC2-macrophage niche define recurrence in oral squamous cell carcinoma | (p-EMT team) | Integrative Computational Approaches 1 |
| 2744 | Automating clinical and pathological staging for breast cancer patients | (staging team) | Large Language Models in the Clinic |
| 4210 | Transformer and pretraining on external EHR cohort boosts infection risk prediction in hematologic malignancy | (EHR-pretrain team) | Machine Learning Approaches for Cancer Prediction |
| 6883 | An RNA-based survival model predicting real-world response to trastuzumab deruxtecan | Josh Wheeler | Network Biology and Precision Medicine |
| 6884 | Quantum mechanics-based multi-tensor AI/ML correctly predicts glioblastoma patients' overall survival | (quantum-GBM team) | Network Biology and Precision Medicine |
| LB175 | Weakly supervised deep learning enables spatially resolved cell type inference from H&E histopathology | (weak-sup team) | Late-Breaking Research: Bioinformatics 2 |

## Multi-omics integration methods

Posters whose methodological contribution is joint modeling / fusion / cross-modal bridging across ≥2 omics modalities (typically transcriptomics + imaging, or transcriptomics + proteomics, or transcriptomics + genomics). This family overlaps heavily with FM-pathology (#4184, #5505, #2754) but is listed separately because the architectural focus is fusion rather than the encoder itself.

| # | Title | Presenter | Session |
|---|---|---|---|
| 2754 | VGL: Vision-Gene-Language multimodal LLM integrating histopathology and gene expression for cell type classification | Haenara Shin | Large Language Models in the Clinic |
| 2752 | CancerSTFormer enables multi-scale analysis of spot-resolution spatial transcriptomes | Qian Zhu | Large Language Models in the Clinic |
| 4184 | Multimodal deep learning framework for predicting clinically significant phenotypes in prostate cancer | Priyanka Vasanthakumari | Integrative Computational Approaches 2 |
| 5505 | A unified framework for cross-platform spatial omics analysis and deep spatial profiling | Yunhe Liu | New Software Tools for Data Analysis |
| 5519 | SOMaC: An interpretable and generalizable framework for integrating and clustering multimodal spatial data | (SOMaC team) | New Software Tools for Data Analysis |
| 5520 | Multi-modal integration in the NetFlow framework for comprehensive exploratory data analysis | (NetFlow team) | New Software Tools for Data Analysis |
| 6904 | OTTER: Optimal transport-based transcriptomics and genomics representation fusion for T-ALL subtyping | (OTTER team) | New Algorithms and Computational Methods |
| 4207 | Omics-aware patch aggregation via multimodal co-training with a scalable multi-omics encoder for slide-level tasks | (Omics-aware team) | Machine Learning Approaches for Cancer Prediction |
| 1469 | Multi-omics profiling of neuroblastoma identifies immunological biomarkers associated with higher risk | (neuroblastoma team) | Integrative Computational Approaches 1 |
| 2687 | First single slide spatially resolved multiomic integration of pancreatic cancer: High-plex proteomics | (PDAC-multiomic team) | Application of Bioinformatics 2 |
| 6908 | Large-scale patient cohorts integration via a novel Bayesian transfer learning framework | (Bayesian-TL team) | New Algorithms and Computational Methods |
| 1478 | Unifying molecular structure and cellular morphology to enhance drug-target interaction modeling | (DTI team) | Integrative Computational Approaches 1 |

## Other (CRISPR screens, variant interpretation, pipelines)

Posters that don't fit the above buckets but represent important workhorse bioinformatics — variant callers, neoantigen pipelines, functional-screen analysis, signature extraction. Grouped here because each sub-family is too small for its own bucket (~5-8 posters each).

| # | Title | Presenter | Session |
|---|---|---|---|
| LB160 | SMURFS: A comprehensive Nextflow pipeline for consensus somatic variant detection | (SMURFS team) | Late-Breaking Research: Bioinformatics 1 |
| LB162 | Twistcgp pipeline: A portable, open-source workflow for comprehensive genomic profiling in translational studies | (twistcgp team) | Late-Breaking Research: Bioinformatics 1 |
| LB446 | Improved mutation detection in duplex sequencing data with sample-specific error profiles | (duplex team) | Late-Breaking Research: Bioinformatics 2 |
| LB170 | scVarID: Linking somatic variants to single-cell transcriptomes to reveal early cancer-associated cells | (scVarID team) | Late-Breaking Research: Bioinformatics 1 |
| 6860 | Ensemble somatic variant calling and transcript reconstruction for high-fidelity neoantigen discovery | (neoantigen team) | Network Biology and Precision Medicine |
| 6861 | NeonDisco: A Nextflow orchestration framework for in silico discovery and prioritization of recurrent neoantigens | (NeonDisco team) | Network Biology and Precision Medicine |
| 6878 | AI-driven structural variant annotation expands therapeutic stratification in breast cancer | (SV annotation team) | Network Biology and Precision Medicine |
| 6872 | Assessing the Impact of Variant Calling Pipelines on De Novo SBS Mutational Signature Extraction | (SBS team) | Network Biology and Precision Medicine |
| 6893 | MambaSV: Accurate germline and somatic structural variant calling from long-reads | (MambaSV team) | New Algorithms and Computational Methods |
| 6900 | Wakhan: Reconstruction of chromosome-scale copy number profiles of tumor genomes with long-read sequencing | (Wakhan team) | New Algorithms and Computational Methods |
| 5511 | Exacto: Accurate identification of mutant proteoforms and neoantigens using integrative long-read sequencing | (Exacto team) | New Software Tools for Data Analysis |
| 4186 | A novel integrated AI ML and COSMIC signature profiling approach resolving blast crisis CML heterogeneity | (CML team) | Integrative Computational Approaches 2 |

## Tally

Bucket memberships (a poster can be counted in more than one bucket):

- Digital pathology foundation models: **18 posters cite a named pathology FM**; ~50 posters hit the looser "foundation model" keyword pattern (including cell/gene/transcriptome FMs in sessions like Large Language Models in the Clinic).
- Traditional deep-learning pathology: **~30** posters across Digital Pathology 1-3 + Machine Learning for Image Analysis + Radiomics that use CNN / U-Net / ViT / MIL without a named pathology FM.
- Benchmarking / evaluation frameworks: **23** (of which 3 are explicit FM benchmarks: #5478, #LB159, #LB174).
- Data infrastructure / atlases / resources: **~40** touching at least one of atlas / knowledge graph / database / harmonization / curation keywords.
- Clinical decision support / prediction models: **45** by survival-or-response-prediction keywords — the largest single family.
- Multi-omics integration methods: **45** touching multi-omics fusion / cross-modal / joint-embedding keywords.
- Other (CRISPR / variants / pipelines): **13** variant- or screen-analysis posters across the Late-Breaking Bioinformatics sessions and New Algorithms and Computational Methods.

Total records: **536** across 24 poster sessions (Digital Pathology 1-3 = 59 posters, Application of Bioinformatics to Cancer Biology 1-5 = 137, Integrative Computational Approaches 1-2 = 50, New Software Tools = 29, New Algorithms = 26, Network Biology and Precision Medicine = 25, Computational/Technological/Mechanistic Advances = 27, Radiomics = 21, ML Approaches for Cancer Prediction = 23, ML for Image Analysis = 8, Deep Learning in Cancer = 18, LLMs in the Clinic = 25, Agentic AI = 18, Late-Breaking Bioinformatics 1-2 = 31, Molecular Pathology = 12, Innovative Therapeutic Modalities = 27).

Name-level FM tallies from the poster corpus (title + abstract, case-sensitive regex, false positives like Graphpad-PRISM and DepMap-PRISM removed):

- **UNI / UNI2**: 6 (#1441, #5470, #2758, #71, #4163, #5505)
- **H-optimus**: 3 (#1444, #LB174, #5489)
- **CTransPath**: 2 (#83, #4151)
- **Lunit-SCOPE**: 2 (#80, #1465)
- **Virchow**: 1 (#1442, "Virchow 2" backbone)
- **Prov-GigaPath**: 1 (#1470)
- **DINOv2**: 1 (#2778)
- **CONCH**: 1 (#5489)
- **TITAN**: 1 (#4184, as CONCHv1.5 + TITAN)
- **MUSK**: 1 (#5489)
- **Hibou**: 1 (#4164)
- **KRONOS**: 2 (#4163, #5505)
- **LOKI**: 1 (#5505)
- **CHIEF**: 0
- **PathChat**: 0
- **PLIP / HIPT / Phikon / BiomedCLIP / REMEDIS / Kaiko / MADELEINE / RudolfV / PanDerm**: 0 each

Eighteen posters cite at least one named pathology FM. The strongest AACR 2026 pathology FM, by mentions, is the **UNI / UNI2 family** (Mahmood lab, Harvard), followed by **H-optimus** (Owkin); **CHIEF** and **PathChat** — both active in the broader literature — do not appear in any 2026 poster title or abstract in this corpus.
