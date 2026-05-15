# Landscape — 1,015 posters by platform / modality

The 1,015 posters in this corpus were harvested from the AACR 2026 Abstracts Online system with a single-cell / spatial / multiplex-imaging phrase-quoted keyword union (`"single cell"`, `"scRNA-seq"`, `"snRNA-seq"`, `"spatial transcriptomics"`, `"spatial proteomics"`, `"multiplex immunofluorescence"`, `"CODEX"`, `"Xenium"`, `"Visium"`, `"MERFISH"`, `"PhenoCycler"`, `"imaging mass cytometry"`, and siblings). Every record kept here has `Activity ∈ {Abstract Submission, Late Breaking and Clinical Trials}` and a resolvable `PlayerUrl`.

Below, each poster has been assigned to exactly one **primary** platform / modality bucket by regex match on title + abstract. The priority order is: imaging-based spatial transcriptomics → sequencing-based spatial transcriptomics → spatial proteomics / multiplex imaging → single-cell multiomics → single-cell RNA-seq → other / hybrid. A single poster can touch multiple platforms (236 of 1,015 do); this page counts each poster once, toward its highest-priority bucket, so the primary counts sum to 994. The 21 unclassified posters are ones whose titles / abstracts do not use any platform keyword — typically loose-harvest wet-lab papers that slipped through.

| Bucket | Primary | Any match |
|---|---:|---:|
| Spatial transcriptomics — imaging-based | 141 | 141 |
| Spatial transcriptomics — sequencing-based | 79 | 106 |
| Spatial proteomics / multiplex imaging | 125 | 181 |
| Single-cell multiomics | 50 | 56 |
| Single-cell RNA-seq | 500 | 629 |
| Other / hybrid | 99 | 173 |
| Unclassified | 21 | — |

Tables below list up to 15 representative posters per bucket — not the full list. **Selection rule (all tables):** roughly one-third late-breaking (`LB*`), the rest drawn from method-oriented sessions (Spatial Proteomics & Transcriptomics 1-3; Spatial Niches; Application of Bioinformatics to Cancer Biology; New Algorithms / New Software Tools; Digital Pathology; Integrative Computational Approaches; Machine Learning for Image Analysis), ranked by abstract depth, with at most two posters per session to avoid over-representing any one session's cohort.

## Spatial transcriptomics — imaging-based (141 posters)

Imaging-based spatial transcriptomics — every assay where transcripts are localized in intact tissue by fluorescent / hybridization imaging rather than by positional barcodes on a sequencer. **Xenium** (10x Genomics, ~85 keyword hits across titles and abstracts) and **CosMx** (NanoString / Bruker, ~38 hits) dominate this bucket in the 2026 corpus; MERFISH / MERSCOPE (Vizgen, ~8), seqFISH, STARmap, smFISH, and RNAscope appear less often but do appear. Several posters that claim "subcellular" or "single-cell-resolution" spatial transcriptomics are here rather than in sequencing-based, because resolution is the imaging regime's distinguishing feature.

| # | Title | Presenter | Session |
|---|---|---|---|
| LB302 | Investigation of the immune microenvironment of breast cancer brain metastasis using single-cell spatial transcriptomics | Eva Zhao | Late-Breaking Research: Tumor Biology 2 |
| LB123 | Spatial immune architecture at single-cell resolution predicts response to atezolizumab plus bevacizumab | Anna Vila-Escoda | Late-Breaking Research: Clinical Research 2 |
| LB427 | Humanized PDX models uncover drug-reversible epigenetic immune exclusion governing T-cell therapy response | Giovanni Medico | Late-Breaking Research: Clinical Research 4 |
| LB199 | High-plex spatial transcriptomics reveals triplatin-induced DNA damage signaling and tumor-fibroblast rewiring | Praveen Bhoopathi | Late-Breaking Research: Experimental and Molecular Therapeutics |
| LB237 | High-resolution spatial transcriptomics identifies unique spatial programs in lung adenocarcinoma | Wei Zhao | Late-Breaking Research: Tumor Biology 1 |
| 4945 | Distinct colorectal cancer tumor cell subtypes revealed by single-cell and spatial transcriptomics | Ji Hye Choi | Spatial Niches and Functional Boundaries within the TME 2 |
| 3974 | Decoding cancer hallmarks through single-cell whole transcriptome imaging in invasive ductal carcinoma | Patrick Danaher | Spatial Proteomics and Transcriptomics 2 |
| 3967 | Spatial whole transcriptomic profiling of breast cancer tissue with CosMx Spatial Molecular Imager | Megan Hopkins | Spatial Proteomics and Transcriptomics 2 |
| 1210 | Integrated spatial and single-cell profiling uncovers a pre-existing, treatment-resistant subclone | Kazutaka Otsuji | Spatial Proteomics and Transcriptomics 1 |
| 4129 | Spatial single-cell transcriptomic profiling reveals distinct immune and stromal landscapes | Kyungsoo Kim | Application of Bioinformatics to Cancer Biology 4 |
| 6858 | Single-cell elucidation of molecularly distinct states and therapeutic vulnerabilities in IDH-mutant glioma | Luca Zanella | Network Biology and Precision Medicine |
| 6914 | STCS: Spatial transcriptomics cell segmentation outperforms existing methods on multiple slides | Xinyu Hu | New Algorithms and Computational Methods |
| 6909 | Dimensionless, null-calibrated spatial indices from Xenium RNA and protein in breast IDC | Jinghao Tian Tian | New Algorithms and Computational Methods |
| 6195 | Spatial transcriptomics analysis reveals tumor cell plasticity and diverse tumor microenvironments | Heng Luo | Spatial Niches and Functional Boundaries within the TME 2 |
| 5491 | AI foundation model for single-cell annotation from conventional histopathology images | Xiangqi Bai | Machine Learning for Image Analysis |

## Spatial transcriptomics — sequencing-based (79 posters)

Sequencing-based spatial transcriptomics — platforms where positional barcodes on a substrate are read out by NGS. **Visium** and **Visium HD** (10x Genomics, ~84 keyword hits) dominate; **GeoMx DSP** (NanoString / Bruker, ~19 hits) is the second-largest platform in this bucket. Stereo-seq (BGI, ~4 hits) and Slide-seq (~1) appear, but rarely. Several posters that integrate Visium with single-cell RNA-seq or GeoMx with H&E are here because their spatial readout is sequencing-backed; the resolution ceiling (~55 µm for standard Visium, ~2 µm for Visium HD) is the practical axis on which the sequencing regime still trails the imaging regime.

| # | Title | Presenter | Session |
|---|---|---|---|
| LB175 | Weakly supervised deep learning enables spatially resolved cell type inference from H&E histopathology | Eldad Shulman | Late-Breaking Research: Bioinformatics, Computational Biology |
| LB238 | Spatial transcriptomics identifies distinct molecular and immune pathways in endometrial cancer | Danyelle Hill | Late-Breaking Research: Tumor Biology 1 |
| LB306 | Spatial transcriptomics reveals primary-site endothelial EMT reprogramming that drives immunosuppression | Gurdeep Singh | Late-Breaking Research: Tumor Biology 2 |
| LB122 | Dynamic interactions of spatially organized tumor, stromal and immune cellular niches predict outcome | Grégoire Marret | Late-Breaking Research: Clinical Research 2 |
| 6664 | Single-cell spatial proteomics of 1200+ protein targets in tumor microenvironments from diverse cancers | Terence Theisen | Spatial Proteomics and Transcriptomics 3 |
| 1217 | Multi-omics integration of bulk, single-cell, and spatial transcriptomics identifies robust prognostics | Viswanathan Palanisamy | Spatial Proteomics and Transcriptomics 1 |
| 3963 | Spatially resolved cell-cell communication reveals intra-tumoral heterogeneity in small-cell lung cancer | Benjamin Lok | Spatial Proteomics and Transcriptomics 2 |
| 1442 | Spatial transcriptomics informed tumor purity estimation from histology slides for triple-negative breast cancer | Vivek Pujara | Digital Pathology 2 |
| 5505 | A unified framework for cross-platform spatial omics analysis and deep spatial profiling | Yunhe Liu | New Software Tools for Data Analysis |
| 4949 | High-resolution spatial transcriptomics reveals dynamic remodeling of the tumor microenvironment | Jiayi Zhou | Spatial Niches and Functional Boundaries within the TME 2 |
| 3957 | Spatially derived transcriptomic predictors of immune checkpoint blockade outcome in advanced gastric cancer | Changjin Hong | Spatial Proteomics and Transcriptomics 2 |
| 815 | Simultaneous spatial transcriptome and epigenome profiling in fresh-frozen and FFPE tissues | Katelyn Noronha | Spatial Protein Profiling and Multi-Modal Mapping |
| 1212 | Spatial transcriptomics reveals distinct SPP1-CD44 signaling networks in neoadjuvant osimertinib-treated NSCLC | Whitney Tamaki | Spatial Proteomics and Transcriptomics 1 |

## Spatial proteomics / multiplex imaging (125 posters)

Spatial proteomics — multiplexed antibody-based imaging that reads 20-100+ protein markers at single-cell or subcellular resolution in intact tissue. **CODEX** / **PhenoCycler** (Akoya, now Bruker, ~23 keyword hits), **imaging mass cytometry / IMC** (Hyperion / Standard BioTools, ~21 hits), **CyCIF** (Harvard / Lin lab, ~11 hits) and **Opal multiplex immunofluorescence** (Akoya Vectra) are the dominant platforms; **MIBI-TOF** (Ionpath, ~3 hits) and **MACSima** (Miltenyi) appear less often. Mass-cytometry-in-suspension (**CyTOF**) posters that are not imaging-based but still multiplex-protein are included here because their analytical framing (clustering, phenotyping) overlaps. This bucket has the largest gap between primary count (125) and "any-match" count (181) — many posters combine spatial proteomics with a spatial-transcriptomics readout and land in the higher-priority transcriptomics buckets.

| # | Title | Presenter | Session |
|---|---|---|---|
| LB221 | Early macrophage reprogramming drives BRCA1-associated breast cancer initiation | Angela Lincy Prem Antony Samy | Late-Breaking Research: Prevention, Early Detection |
| 6851 | Multi-cell-type model for analyzing spatial single-cell protein imaging data with application to ovarian cancer | Chase Sakitis | Mathematical Modeling and Statistical Methods |
| 6200 | Single-cell spatial CRISPR screen for tumor microenvironment | Boyoung Jeong | Spatial Niches and Functional Boundaries within the TME 2 |
| 4133 | Single-cell multi-omics enables molecular dissection of gastric cancer subtypes | Junha Cha | Application of Bioinformatics to Cancer Biology 4 |
| 55 | Differentiation state and immune interaction contribute to drug response in AML | Natasha Black | Application of Bioinformatics to Cancer Biology 1 |
| 6192 | Multi-omics reveals the diversity of CAF in ESCC lymph node metastasis | Licheng Tan | Spatial Niches and Functional Boundaries within the TME 2 |
| 61 | Defining spatial biomarkers of survival across solid tumors using a pan-cancer proteomics atlas | Khoa Huynh | Application of Bioinformatics to Cancer Biology 1 |
| 789 | PaintScape enables in situ, single-cell spatial multiomic visualization of 3D genome organization | Shyamtanu Chattoraj | Spatial Protein Profiling and Multi-Modal Mapping |
| 4966 | A single-cell spatial proteomic analysis of the TNBC microenvironment defines genotype-specific features | Dana Pueschl | Spatial Niches and Functional Boundaries within the TME 1 |
| 697 | Label-free spatial profiling of the melanoma tumor microenvironment using metasurface-enhanced Raman | Kai Chang | Methods to Measure Tumor Evolution and Heterogeneity |
| 85 | Path2Marker: Cell-level prediction of multiplex protein expression from routine H&E slides | Amos Stemmer | Digital Pathology 1 |
| 804 | Distinct cellular phenotypes and spatial neighborhoods constitute the heterogeneous microenvironment | Kevin Murgas | Spatial Protein Profiling and Multi-Modal Mapping |
| 3968 | Spatial transcriptomic features associated with response to neoadjuvant therapy in triple-negative breast cancer | Shiqing Liao | Spatial Proteomics and Transcriptomics 2 |
| 5500 | Morphology-aware profiling of highly multiplexed tissue images using variational autoencoders | Gregory Baker | New Software Tools for Data Analysis |

## Single-cell RNA-seq (500 posters)

By far the largest bucket, and by far the most diverse in session-assignment: scRNA-seq and snRNA-seq work spans every biology session in this corpus (Clonal Hematopoiesis, DTCs, Senescence, Plasticity, Neural-Immune, Macrophages, Fibroblasts, gastric / gastroesophageal, hematologic malignancies). Chromium-family 10x Genomics workflows are the default (~389 scRNA-seq keyword hits, ~24 snRNA-seq). Parse Biosciences and BD Rhapsody appear rarely. This bucket also includes the long tail of posters where "single-cell" appears in the abstract but no specific platform vendor is named — typically because the authors used 10x Chromium without saying so. Note that there is **no dedicated single-cell RNA-seq poster session** at AACR 2026 (compare to seven dedicated spatial-named sessions, see [index.md](index.md) and the [synthesis](synthesis-spatial-eating-sc.md#claim-2-growth-signal-in-session-titles)).

| # | Title | Presenter | Session |
|---|---|---|---|
| LB170 | scVarID: Linking somatic variants to single-cell transcriptomes to reveal early cancer-associated cells | Juyeon Cho | Late-Breaking Research: Bioinformatics, Computational Biology |
| LB169 | scCAP: An ontology-aware LLM framework for hierarchical standardized single-cell type annotation | Seok-Won Jang | Late-Breaking Research: Bioinformatics, Computational Biology |
| LB171 | AI-based B2SC identifies pre-existing TOP2A/E2F-active populations driving resistance to T-DXd | Se-eun Han | Late-Breaking Research: Bioinformatics, Computational Biology |
| LB309 | Y chromosome loss drives cellular plasticity through single-cell epigenetic and transcriptional heterogeneity | Kathleen Schlueter | Late-Breaking Research: Tumor Biology 2 |
| LB316 | FOXA2-associated chemoresistance in gastroesophageal adenocarcinoma: a single-cell transcriptomic examination | Sanjima Pal | Late-Breaking Research: Tumor Biology 2 |
| 1426 | A single-cell tumor atlas defines robust pathway and gene signatures enabling cancer cell-line characterization | Rosyli Reveron-Thornton | Application of Bioinformatics to Cancer Biology 2 |
| 5522 | scSurvival: Single-cell survival analysis of clinical cancer cohort data at cellular resolution | Tao Ren | New Software Tools for Data Analysis |
| 1515 | Doublet removal enhances single-cell resolution and uncovers malignant transcriptional programs | Qian Wang | Sequence Analysis |
| 4959 | Trekker enables high-sensitivity single-cell spatial profiling of the FFPE lung SCC tumor microenvironment | Cedric Uytingco | Spatial Niches and Functional Boundaries within the TME 1 |
| 40 | Integrated transcriptomic and immune-clonal evolution defines stepwise molecular progression | Kang Qin | Application of Bioinformatics to Cancer Biology 1 |
| 1462 | Cell-type-specific somatic variants captured from single-cell RNA sequencing underlie transcriptional heterogeneity | Jasmine Ryu Won Kang | Integrative Computational Approaches 1 |
| 1513 | Gene signatures and infiltration patterns of mast cells in breast cancer revealed by integrated scRNA-seq | Qian Wang | Sequence Analysis |
| 44 | scSubtype2.0: Predictor of breast cancer molecular subtypes at single-cell resolution | Alexander Lobanov | Application of Bioinformatics to Cancer Biology 1 |
| 1407 | Single-cell long-read transcriptomics reveals isoform-centric molecular features of rare pseudogenes | Kyungtae Lee | Application of Bioinformatics to Cancer Biology 2 |
| 2679 | Integrated bulk and single-cell transcriptomics reveal hepatocyte-like reprogramming in metastasis | James Madigan | Application of Bioinformatics to Cancer Biology 3 |

## Single-cell multiomics (50 posters)

Assays that read ≥2 molecular modalities per cell: scATAC-seq (~13 keyword hits), CITE-seq (~8), Perturb-seq / ECCITE-seq (~4), 10x Multiome (RNA + ATAC), TEA-seq, ASAP-seq, SHARE-seq, single-cell DNA methylation, and single-cell long-read transcriptomics. Conceptually the most technology-dense bucket but also the smallest single-cell bucket — single-cell multiomics has not yet scaled into biology posters the way plain scRNA-seq has. The dedicated *Single-Cell Multi-omic Technologies* session (Mon 4/20, see [index.md](index.md)) focuses heavily on DNA-side modalities (methylation, chromatin, ecDNA) rather than the RNA-plus-protein CITE-seq direction.

| # | Title | Presenter | Session |
|---|---|---|---|
| 1503 | Single-cell multiomics analysis reveals cell-type-specific genetic regulatory programs underlying immune cell aging | Siyuan Huang | Sequence Analysis |
| 4141 | Multimodal single-cell analysis of systemic immune remodeling induced by cytoreductive nephrectomy | Suebin Park | Application of Bioinformatics to Cancer Biology 4 |
| 4130 | Single-cell multi-omic characterization of gastric intestinal metaplasia reveals potential genetic drivers | Dongin Lee | Application of Bioinformatics to Cancer Biology 4 |
| 2689 | Single-cell multiome sequencing reveals distinct transcriptional programs associated with ecDNA amplification | Ashley Hui | Application of Bioinformatics to Cancer Biology 3 |
| 703 | Tracking tumor evolution and heterogeneity in fusion-driven sarcomas through cell-free DNA analysis | Tom Fischer | Methods to Measure Tumor Evolution and Heterogeneity |
| 692 | Novel single-cell and bulk NGS assays for improved assessment of MRD in hematologic malignancies | Crystal Zhou | Methods to Measure Tumor Evolution and Heterogeneity |
| 6888 | scDeBussy: Cohort-level pseudotime alignment reveals recurrent dynamic gene programs in histologies | Meng Wang | New Algorithms and Computational Methods |
| 3498 | Improving the utility of the single-cell pediatric cancer atlas through updated cell-type annotation | Ally Hawkins | Pediatric Cancer Genomics and Epigenomics |
| 495 | Single-cell multiomic drug response profiling of PRISM-multiplexed cancer cell lines | Houlin Yu | Genomic Dissection to Define Novel Therapeutic Strategies |
| 2073 | In vivo single-cell CRISPR screens identify targets to restore T cell function in aged tumors | Alex Chang-Yu Chen | Aging and Host Determinants of Tumor Progression |
| 3544 | Single-cell multi-omics uncovers coordinated epigenetic and transcriptomic evolution in IDH-mutant glioma | Masashi Nomura | Tumor Evolution |
| 5964 | Single-cell multi-omics profiling unveils regulatory mechanisms of small-cell lung cancer | Charny Park | Mechanisms and Dynamics of Gene Expression |

## Other / hybrid (99 posters)

The catch-all bucket — posters whose platform signature is explicitly hybrid (3D spatial multi-omics, pseudo-spatial deconvolution of bulk RNA-seq, light-sheet / tissue-clearing, multimodal-integration method papers, and benchmark-framework posters). Also includes posters that use "spatial" language but no specific platform keyword survives the priority-ordered classifier (they are here rather than being double-counted as imaging or sequencing spatial). Methodologically this is where most of the explicitly-spatial-and-single-cell integration posters land.

| # | Title | Presenter | Session |
|---|---|---|---|
| LB229 | Single-cell and spatially resolved transcriptomics identifies clinically targetable myeloid niches | Jason Carter | Late-Breaking Research: Tumor Biology 1 |
| LB041 | Decoding single-cell protein interactomes of CAR T cells with the Proximity Network Assay | Michael Forster | Late-Breaking Research: Chemistry |
| LB246 | Neoadjuvant androgen signaling inhibition promotes mixed basal/club-like prostate cancer identities | Antti Kiviaho | Late-Breaking Research: Tumor Biology 1 |
| LB159 | A practical guideline for benchmarking unimodal and multimodal foundation models on spatial transcriptomics | Anna Wahl-Schaar | Late-Breaking Research: Bioinformatics, Computational Biology |
| 1466 | CellNeighbor: A transcriptional atlas of patient tumors and cell-line models to inform preclinical modeling | Caitlin Simopoulos | Integrative Computational Approaches 1 |
| 1200 | Spatially resolved tumor-cell MHC class II shapes adaptive immunity and therapeutic response in TNBC | Saranya Chumsri | Spatial Proteomics and Transcriptomics 1 |
| 4179 | Three-dimensional spatial multi-omics of gastric tumor sections reveal hidden features beyond 2D analysis | Inyeop Jang | Integrative Computational Approaches 2 |
| 1214 | SPACE: Spatially resolved multiomic analysis for high-throughput CRISPR screening in 3D models | Mengwei Hu | Spatial Proteomics and Transcriptomics 1 |
| 2692 | EpiGuide: Tracking epigenetic plasticity in circulating tumor DNA to monitor tumor progression | Edoardo Giuili | Application of Bioinformatics to Cancer Biology 3 |
| 6685 | Integrated high-throughput multimodal spatial profiling of RNA, protein, and morphology in FFPE sections | Michael Lawson | Spatial Proteomics and Transcriptomics 3 |
| 6848 | HPlot: A quantitative framework for spatial profiling of immune heterogeneity in the tumor microenvironment | Chao Hui Huang | Mathematical Modeling and Statistical Methods |
| 1464 | CELLama-Perturb: A virtual cell modeling approach for mapping drug sensitivity across spatial tumor heterogeneity | Haenara Shin | Integrative Computational Approaches 1 |

## Tally

| Bucket | Count | Share of classified |
|---|---:|---:|
| Spatial transcriptomics — imaging-based | 141 | 14% |
| Spatial transcriptomics — sequencing-based | 79 | 8% |
| Spatial proteomics / multiplex imaging | 125 | 13% |
| **Spatial subtotal** | **345** | **35%** |
| Single-cell RNA-seq | 500 | 50% |
| Single-cell multiomics | 50 | 5% |
| **Single-cell subtotal** | **550** | **55%** |
| Other / hybrid | 99 | 10% |
| **Classified total** | **994** | **100%** |
| Unclassified (no platform keyword) | 21 | — |

At first glance the aggregate reads as "scRNA-seq still dominates, 50% to 35%." That picture is too flat: it treats a biology-session scRNA-seq poster ("we ran 10x on 12 patient samples") and a method-development scRNA-seq poster ("scCAP ontology-aware LLM annotation") as equivalent, and it hides the fact that the single-cell share is inflated by hundreds of biology-framed posters where scRNA-seq is a workhorse rather than the point. The [synthesis page](synthesis-spatial-eating-sc.md) unpacks why, on the **methods** axis, the corpus looks quite different — seven dedicated spatial poster sessions to zero dedicated single-cell-named sessions, and a growing class of "integrated spatial + single-cell" posters that treat scRNA-seq as the annotation substrate for what is fundamentally a spatial-biology paper.
