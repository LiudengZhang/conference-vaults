# RECOMB 2026 — Program Notes (working file)

**Internal-use working file.** Source for the bulk tool-page generation pass that will run immediately after the meeting closes May 29, 2026. Not for end-reader consumption — formatting is utilitarian. Compiled from the public RECOMB 2026 web pages, fetched 2026-05-11 (~15 days pre-meeting).

**Tag legend:**
- `[METHOD]` — methods paper that ships a software artifact; tool-page candidate
- `[BIOC]` — paper with biological-data application as the headline contribution (single-cell, spatial, cancer evolution, protein function)
- `[SOFTWARE]` — paper whose contribution is primarily an engineering artifact (scalability, index structure, framework)
- `[THEORY]` — proof / complexity / minimax / minimizer-density result; **not** a tool-page candidate (one-paragraph entry in `topics/sequence-phylogeny/` instead)
- `[PRIVACY]` — papers in the privacy / differential-privacy / federated-learning bin
- `[?]` — placeholder; populated post-meeting

A paper can carry multiple tags. The intersection that gets a tool page is `[METHOD]` + (`[BIOC]` ∪ `[SOFTWARE]`).

**Sparse-coverage flags:**

- **Keynote titles not yet public.** All 4 keynote speakers announced (Medvedev / Myers / Stamatakis / Mostafavi) but talk titles are not on the public site as of May 11. Likely posted day-of or via #RECOMB2026 social. Recheck May 26.
- **Satellite-workshop programs uneven.** RECOMB-CG and RECOMB-Seq sites are populated; RECOMB-Privacy / RECOMB-Arch / RECOMB-CCB / RECOMB-Genetics / RECOMB-RSG schedules are sparser as of May 11. Recheck the satellite sites May 20–24.
- **Partnering-journal venue per paper not yet announced.** The 3-way split between *Cell Systems* / *Genome Research* / *JCB* is decided on a per-paper basis; selections are announced at the closing session or shortly after. JCB special-issue DOIs typically take 3–6 months to materialize.
- **No central RECOMB Zenodo community.** Slide deposits are ad-hoc — Berger lab, Klau lab, Mirarab lab historically deposit; most others don't. Manual sweep of speaker labs / Bluesky needed post-meeting.
- **Recordings.** RECOMB main program traditionally not recorded. Some sessions occasionally posted to [RECOMB YouTube](https://www.youtube.com/@recombseries) 6–10 weeks late. Assume no recordings until proven otherwise.

---

## Verified high-level facts (2026-05-11)

- **Conference:** RECOMB 2026 — 30th Annual International Conference on Research in Computational Molecular Biology
- **Dates:** Tue May 26 – Fri May 29, 2026 (main program). Satellites + H.bioinfo'17 on Sun May 24 + Mon May 25.
- **Venue:** Thessaloniki Concert Hall, Thessaloniki, Greece. In-person only.
- **Hosting:** Aristotle University of Thessaloniki, under the Hellenic Bioinformatics Society, in affiliation with ISCB.
- **PC Chair:** Rayan Chikhi (Institut Pasteur)
- **Steering Committee:** Bonnie Berger (chair, MIT), Vineet Bafna (UCSD), Eleazar Eskin (UCLA), Jian Ma (CMU), Teresa Przytycka (NCBI/NIH), Cenk Sahinalp (NCI/NIH), Roded Sharan (Tel Aviv), Martin Vingron (Max Planck)
- **Organizing Co-chairs:** Christos Ouzounis (Aristotle Univ. Thessaloniki), Ezgi Ebren (Bilkent)
- **Operations:** Ilias Kappas + Asimina Kournoutou (both Aristotle Univ.)
- **Publicity Chair:** Can Alkan (Bilkent)
- **Industry Chair:** Mohammed Alser (Georgia State)
- **Posters Chair:** Kaiyuan Zhu (Shanghai Jiao Tong)
- **Travel Fellowships Chair:** Gurkan Bebek (Case Western Reserve)
- **Accepted papers:** **65 main-program papers**
- **Keynotes:** **4** — Paul Medvedev (Tue), Gene Myers (Wed), Alexandros Stamatakis (Thu), Sara Mostafavi (Fri)
- **Proceedings venue:** **No Springer LNBI this year.** Papers route to partnering journals: **Cell Systems**, **Genome Research**, or **Journal of Computational Biology** (default JCB special issue). Some papers may be invited to submit expanded versions to Cell Systems / Genome Research for expedited review.
- **Satellites:** 7 — RECOMB-Seq, RECOMB-CCB, RECOMB-CG, RECOMB-Genetics, RECOMB-Privacy, RECOMB-Arch, RECOMB-RSG. Plus H.bioinfo'17 (Hellenic Bioinformatics Society) on May 25.

---

## Keynotes (4)

| Day | Speaker | Affiliation | Field | Title |
|---|---|---|---|---|
| Tue May 26 | **Paul Medvedev** | Penn State University, USA | sequence algorithms, genome assembly, k-mer indexing | TBD — not yet public |
| Wed May 27 | **Gene Myers** | Max Planck Institute of Molecular Cell Biology & Genetics, Dresden (and CSHL) | sequence assembly (BLAST co-author; DAZZLER assembler) | TBD — not yet public |
| Thu May 28 | **Alexandros Stamatakis** | Heidelberg Institute for Theoretical Studies / KIT | phylogenetics (RAxML, ExaML) | TBD — not yet public |
| Fri May 29 | **Sara Mostafavi** | University of Washington / Allen School | machine learning for genomics, allele-specific measurements, regulatory genomics | TBD — not yet public — note: Mostafavi is also senior author on paper #19 ("Deep genomic models of allele-specific measurements") in Session 7 |

All 4 keynotes are in the main hall (Thessaloniki Concert Hall). One per day, scheduled at the start of the program day. Talk titles will likely be posted to keynotes.html closer to the date or announced at the opening; #RECOMB2026 on Bluesky / X is the fastest source.

---

## Day-by-day skeleton (from the program schedule page)

### Sunday May 24 + Monday May 25, 2026 — Satellites + H.bioinfo'17

Parallel-track satellite workshops at Thessaloniki Concert Hall (same venue, different rooms). Each satellite runs its own program; not detailed here. Tool pages from satellite talks get `Status: satellite-workshop` + `Satellite: <name>`.

- **RECOMB-Seq** ([site](https://recomb-seq.github.io/)) — sequence-analysis methods
- **RECOMB-CCB** — Cancer Computational Biology (closest to AACR axis fit)
- **RECOMB-CG** ([site](https://recomb-cg.org/)) — Comparative Genomics
- **RECOMB-Genetics** — statistical / population genetics
- **RECOMB-Privacy** — privacy-preserving comp-bio (overlaps Session 13)
- **RECOMB-Arch** — ancient DNA / paleogenomics
- **RECOMB-RSG** — Regulatory and Systems Genomics
- **H.bioinfo'17** — Hellenic Bioinformatics Society meeting, May 25 only

### Tuesday May 26, 2026 — Day 1

- **Keynote 1: Paul Medvedev** (Penn State)
- **Session 1: Sequence I** — 6 talks
  - Minimizer Density revisited: Models and Multiminimizers `[THEORY][METHOD]` (Ingels, Robidou, Martayan, Marchet, Limasset)
  - MaxGeomHash: An Algorithm for Variable-Size Random Sampling of Distinct Elements `[METHOD]` (Hera, Koslicki, Martínez)
  - Faster and Scalable Parallel External-Memory Construction of Colored Compacted de Bruijn Graphs with Cuttlefish 3 `[SOFTWARE][METHOD]` (Khan, Dhulipala, Pandey, **Patro**)
  - Sequence-to-graph alignment based copy number calling using a network flow formulation `[METHOD]` (Magalhães, Weber, Klau, Marschall, Prodanov)
  - Privacy-Preserving Pangenome Graphs `[METHOD][PRIVACY]` (Blindenbach, Soni, Gursoy)
  - bronko: ultrarapid, alignment-free detection of viral genome variation `[SOFTWARE][METHOD]` (Doughty, Tisza, Treangen)
- **Session 2: Protein/ML I** — 6 talks
  - Predicting interaction-specific protein–protein interaction perturbations by missense variants with MutPred-PPI `[METHOD][BIOC]` (Stewart, Laval, Calderwood, Mort, Cooper, Vidal, Radivojac)
  - Bacterial protein function prediction via multimodal deep learning `[METHOD]` (Muzio, Adamer, Fernandez, Miklautz, Borgwardt, Avican)
  - Evolutionary profile enhancement improves protein function annotation `[METHOD]` (Dai, Luo, Luo)
  - Integrative Multi-Scale Sequence–Structure Modeling for Antimicrobial Peptide Prediction and Design `[METHOD]` (Li, Shao, Li, Yu)
  - ProtFlow: Flow Matching-based Protein Sequence Design with Comprehensive Protein Semantic Distribution Learning `[METHOD]` (Kong, Zhu, Xu, Yin, Hou, Wu, Xu, Hsieh)
  - Transforming Biological Foundation Model Representations for Out-of-Distribution Data `[METHOD]` (Pratapa, Singh, Tata)
- **Session 3: Single-Cell I** — 4 talks
  - Random Matrix Theory-guided sparse PCA for single-cell RNA-seq data `[METHOD][THEORY]` (Chardès)
  - Gene-First Identity Construction for Robust Cell Identification in Single-Cell Transcriptomics `[METHOD][BIOC]` (Yang, Huang, Xin, Cai)
  - Error Correction Algorithms for Efficient Gene Quantification in Single Cell Transcriptomics `[METHOD]` (Zentgraf, Schmitz, Keller, **Rahmann**)
  - Nullstrap-DE: A General Framework for Calibrating FDR and Preserving Power in Differential Expression Methods, with Applications to DESeq2 and edgeR `[METHOD][BIOC]` (Jiang, Wang, **J.J. Li**) — **direct cross-vault overlap with EuroBioC2025 (edgeR/DESeq2)**

### Wednesday May 27, 2026 — Day 2

- **Keynote 2: Gene Myers** (Max Planck Dresden / CSHL)
- **Session 4: Sequence II** — 6 talks
  - KuPID: Kmer-based Upstream Preprocessing of Long Reads for Isoform Discovery `[SOFTWARE][METHOD]` (Borowiak, Yu)
  - SLAB: A Sweep Line Algorithm in PBWT for Finding Haplotype Block Cores `[METHOD]` (Naseri, Sanaullah, Zhang, Zhi)
  - pHapCompass: Probabilistic Assembly and Uncertainty Quantification of Polyploid Haplotype Phase `[METHOD]` (Hosseini, Veiner, Bergendahl, Yasenpoor, Smith, Staton, Aguiar)
  - On Deriving Synteny Blocks by Compacting Elements `[METHOD]` (Bohnenkämper, Parmigiani, Chauve, Stoye)
  - Compressed inverted indexes for scalable sequence similarity `[SOFTWARE][METHOD]` (Ingels, Vandamme, Girard, Agret, Cazaux, Limasset)
  - Fast and Flexible Flow Decompositions in General Graphs via Dominators `[THEORY][METHOD]` (Sena, Tomescu)
- **Session 5: Multi-Omics** — 4 talks
  - Multimodal spatial alignment and morphology mapping with MOSAICField `[METHOD][BIOC]` (Liu, Zheng, Halmos, Gold, Storrs, Ding, **B. Raphael**) — spatial omics flagship
  - Multi-modal tissue-aware graph neural network for in silico genetic discovery `[METHOD][BIOC]` (Aggarwal, Sokolova, **O. Troyanskaya**) — Troyanskaya overlap with ISMB 2026 Mon keynote
  - Modeling Multi-Modal Brain Connectomes for Brain Disorder Diagnosis via Graph Diffusion Optimal Transport Network `[METHOD][BIOC]` (Sheng, Liu, Liang, Zhang, Mondal, Li, Zhang, Liu, Song, Cai)
  - Achieving spatial multi-omics integration from unaligned serial sections with DIME `[METHOD][BIOC]` (Sun, Mou, Zheng, Huang)
- **Session 6: Small Molecules** — 2 talks
  - SpecLig: Energy-Guided Hierarchical Model for Target-Specific 3D Ligand Design `[METHOD]` (Zhang, Han, Kong, Chen, Ma)
  - Joint Learning of Drug-Drug Combination and Drug-Drug Interaction via Coupled Tensor-Tensor Factorization with Side Information `[METHOD]` (Zhang, Fang, Tang, Chen, Li)
- **Session 7: Transcriptomics** — 4 talks
  - Summarizing RNA Structural Ensembles via Maximum Agreement Secondary Structures `[METHOD][THEORY]` (Gu, Ivanovic, Feng, **El-Kebir**)
  - CLADES — Contrastive Learning Augmented DifferEntial Splicing with Orthologous Positive Pairs `[METHOD]` (Talukder, Keung, Pe'Er, Knowles)
  - Alternet: Alternative splicing-aware gene regulatory network inference `[METHOD]` (Hoffmann, Wallnig, Dai, Tsoy, Blumenthal, Hartebrodt)
  - Deep genomic models of allele-specific measurements `[METHOD]` (Tu, Sasse, Chowdhary, Spiro, Yang, Chikina, Benoist, **Mostafavi**) — **Mostafavi is also the Fri keynote**

### Thursday May 28, 2026 — Day 3

- **Session 8: Phylogeny I** — 3 talks
  - Constrained diffusion as a paradigm for evolution `[METHOD][THEORY]` (Lazarev, Sappington, Chau, Zhang, **B. Berger**)
  - Deconvolving Phylogenetic Distance Mixtures `[METHOD]` (Arasti, Şapcı, Rachtman, El-Kebir, **Mirarab**)
  - A Cophylogenetic Approach for Virus-Host Interaction Prediction `[METHOD][BIOC]` (Chowdhury, Murali, **Sashittal**)
- **Session 9: Single-Cell II** — 6 talks
  - scDesignPop generates population-scale single-cell RNA-seq data for power analysis, method benchmarking, and privacy protection `[METHOD][BIOC]` (Dong, Cen, Song, **J.J. Li**)
  - scProfiterole: Clustering of Single-Cell Proteomic Data Using Graph Contrastive Learning via Spectral Filters `[METHOD][BIOC]` (Coşkun, Lopes, Tolunay, Chance, Koyutürk)
  - Integrating morphology and gene expression in unpaired single-cell data using GeoAdvAE `[METHOD][BIOC]` (Du, Lin)
  - MOSAIC: A Spectral Framework for Integrative Phenotypic Characterization Using Population-Level Single-Cell Multi-Omics `[METHOD][BIOC]` (Lu, Kluger, Ma)
  - Integrative Inference of Spatially Informed Cell Lineage Trees using LineageMap `[METHOD][BIOC]` (Pan, Chen, Zhang)
  - Causal gene regulatory network inference from Perturb-seq via adaptive instrumental variable modeling `[METHOD][BIOC]` (Sun, Kang, Keles)
- **Keynote 3: Alexandros Stamatakis** (HITS / KIT)
- **Session 10: Phylogeny II** — 3 talks
  - Quartet-based species tree methods enable fast and consistent tree of blobs reconstruction under the network multispecies coalescent `[METHOD][THEORY]` (Dai, Han, Molloy)
  - STELAR-X: Scaling Coalescent-Based Species Tree Inference to 100,000 Species and Beyond `[SOFTWARE][METHOD]` (Saha, Bayzid)
  - PaNDA: Efficient Optimization of Phylogenetic Diversity in Networks `[METHOD]` (Holtgrefe, van Iersel, Meuwese, Murakami, Schestag)
- **Session 11: Cancer & Evolution** — 4 talks **(highest AACR axis fit of any session)**
  - Arborist: Prioritizing Bulk DNA Inferred Tumor Phylogenies via Low-pass Single-cell DNA Sequencing Data `[METHOD][BIOC]` (Weber, Ching, Ly, Cheng, Gao, **Van Loo**)
  - Identifying Robust Subclonal Structures Through Tumor Progression Tree Alignment `[METHOD][BIOC]` (Wu, Gilbert, Malikić, **Sahinalp**)
  - Fast and accurate resolution of ecDNA sequence using Cycle-Extractor `[METHOD][BIOC]` (Faizrahnemoon, Luebeck, Hung, Rao, Jones, Mischel, Chang, Zhu, **Bafna**) — ecDNA is a top AACR 2026 theme
  - POTTR: Identifying Recurrent Trajectories in Evolutionary and Developmental Processes using Posets `[METHOD][BIOC]` (Käufler, Schmidt, Jürgens, Klau, Sashittal, **B. Raphael**)

### Friday May 29, 2026 — Day 4 (close)

- **Keynote 4: Sara Mostafavi** (Univ. of Washington / Allen School)
- **Session 12: Protein/ML II** — 6 talks
  - Fast, accurate construction of multiple sequence alignments from protein language embeddings `[METHOD]` (Hoang, Armour-Garb, **Singh**)
  - Generating Hybrid Proteins with the MSA-Transformer `[METHOD]` (Tule, Davis, Koludarov, Mora, Boden)
  - Deconvolving mutation effects on protein stability and function with disentangled protein language models `[METHOD][BIOC]` (Ding, Li, Tu, Luo, Luo)
  - Quantum and Temporal Graph Neural Networks Reveal New Accuracy Limits in Predicting Protein–Ligand Dissociation Kinetics `[METHOD]` (Salamatov, Bai, Atluri, Guan)
  - Protein Compositional Ratio Representation (PCRR) Systematically Improves Human Disease Prediction `[METHOD][BIOC]` (Madduri, Ellis, Patel)
  - Uncertainty-aware synthetic lethality prediction with pretrained foundation models `[METHOD][BIOC]` (Hua, Haber, **J. Ma**) — synthetic lethality has direct cancer-target-discovery relevance
- **Session 13: Statistical Genetics** — 6 talks
  - Prediction of lifetime disease liability from EHR features `[METHOD][BIOC]` (Di, Cai)
  - Private Information Leakage from Polygenic Risk Scores `[METHOD][PRIVACY]` (Nikitin, Gursoy)
  - A biobank-scale method for learning environmental modulators of gene–environment interaction underlying complex traits `[METHOD][BIOC]` (Liu, Ramteke, Anand, Gorla, Jeong, **Sankararaman**)
  - Bias in genome-wide association test statistics due to omitted interactions `[METHOD][THEORY]` (Yelmen, Güler, Kollo, Möls, Charpiat, Jay)
  - GOPHER: Optimization-based Phenotype Randomization for Genome-Wide Association Studies with Differential Privacy `[METHOD][PRIVACY]` (Nandi, Neel, **Cho**)
  - Evolutionary dynamics under phenotypic uncertainty `[METHOD][THEORY]` (Mohanty, Sappington, Shakhnovich, **B. Berger**)
- **Session 14: Single-Cell III** — 5 talks
  - CAMP: Coreset Accelerated Metacell Partitioning enables scalable analysis of single-cell data `[METHOD][BIOC]` (Li, Ko, **Canzar**)
  - DeltaNMF: A Two-Stage Neural NMF for Differential Gene Program Discovery `[METHOD][BIOC]` (Karpurapu, Gersbach, **Singh**)
  - Information Geometry Reconciles Discrete and Continuous Variation in Single-Cell and Spatial Transcriptomic Analysis `[METHOD][THEORY]` (Cai, Wang, Qiao, Wang, Rong, Zhou, Liu, Jiang, Shen, **J.J. Li**, Xin)
  - DiCoLo: Integration-free and cluster-free detection of localized differential gene co-expression in single-cell data `[METHOD][BIOC]` (Li, Yang, Su, Jaffe, Lindenbaum, **Kluger**)
  - CycleGRN: Inferring Gene Regulatory Networks from Cyclic Flow Dynamics in Single-Cell RNA-seq `[METHOD][BIOC]` (Zhao, **Fertig**, Stein-O'Brien) — Fertig overlap with AACR / JHU cancer-systems-biology axis
- **Closing session** — best-paper + best-student-paper announcements (TBD, announced from stage)

---

## Accepted-paper bins by AACR-axis fit

**Direct AACR axis (high-priority for bulk extraction):**

| Bin | Sessions | Count | Notes |
|---|---|---|---|
| **Cancer & Evolution** | Session 11 | 4 | Arborist (Van Loo), tumor-progression-tree alignment (Sahinalp), Cycle-Extractor for ecDNA (Bafna), POTTR (Raphael). All four are direct AACR-axis tools. ecDNA paper especially relevant — ecDNA is a top AACR 2026 theme. |
| **Single-Cell methods** | Sessions 3, 9, 14 | 15 | CAMP, DiCoLo, scDesignPop, MOSAIC, scProfiterole, GeoAdvAE, Gene-First, CycleGRN, DeltaNMF, error-correction, Nullstrap-DE, Information-Geometry, sparse-PCA, LineageMap, Perturb-seq causal GRN. Heaviest tool-page yield of any bin. |
| **Spatial Omics** | Sessions 5, 9 | 4 | MOSAICField (Raphael), DIME, LineageMap, GeoAdvAE. Overlaps EuroBioC2025 SpatialData / GBCC2025 sosta themes. |
| **Protein/ML & drug design** | Sessions 2, 6, 12 | 14 | MutPred-PPI, ProtFlow, foundation-model OOD, SpecLig, drug-drug interactions, MSA-from-PLM, MSA-Transformer hybrids, synthetic-lethality, quantum-GNN, PCRR, AMP design, bacterial function, evolutionary-profile-enhanced annotation, mutation-effect disentanglement. AACR oncology drug-discovery relevance high. |

**Adjacent AACR axis (medium-priority):**

| Bin | Sessions | Count | Notes |
|---|---|---|---|
| **Transcriptomics** | Session 7 | 4 | CLADES, Alternet, RNA-structure ensembles, allele-specific measurements (Mostafavi). Splicing + RNA structure + regulatory genomics. |
| **Statistical / Privacy genetics** | Session 13 | 6 | Disease-liability prediction, PRS leakage, GOPHER, biobank G×E, GWAS bias, evolutionary dynamics. PRS privacy directly relevant to clinical AACR translational work. |
| **Multi-Omics integration** | Session 5 | 4 | Tissue-aware GNN (Troyanskaya), brain-connectome diffusion-OT, MOSAICField, DIME. |

**Upstream infrastructure (low AACR fit, treated as topic entries):**

| Bin | Sessions | Count | Notes |
|---|---|---|---|
| **Sequence algorithms** | Sessions 1, 4 | 12 | Minimizers, MaxGeomHash, Cuttlefish 3, sequence-to-graph CN, pangenome privacy, bronko, KuPID, SLAB, pHapCompass, synteny, compressed inverted indexes, flow decompositions. Mostly `[SOFTWARE]` + `[THEORY]`; only Cuttlefish 3, KuPID, bronko, SLAB, compressed indexes likely warrant full tool pages. |
| **Phylogeny** | Sessions 8, 10 | 6 | Constrained diffusion, distance mixtures, virus-host cophylogeny, quartet-trees, STELAR-X, PaNDA. STELAR-X (100k-species scaling) is the standout tool-page candidate. |

---

## Cross-vault speaker overlap watch

Confirmed RECOMB 2026 authors with corpus presence elsewhere. **All confirmed via the public accepted-paper list** (not predicted, unlike the ISMB 2026 watch).

| Person | Lab / institution | RECOMB 2026 paper(s) | Where they appear elsewhere | Likely overlap topic |
|---|---|---|---|---|
| **Bonnie Berger** | MIT (RECOMB Steering chair) | "Constrained diffusion as a paradigm for evolution" (S8), "Evolutionary dynamics under phenotypic uncertainty" (S13) | ISMB 2026 MLCSB likely; cross-AACR cited | ML for evolution / generative models |
| **Olga Troyanskaya** | Princeton | "Multi-modal tissue-aware GNN for in silico genetic discovery" (S5) | **ISMB 2026 Mon Jul 13 distinguished keynote (Innovator Award)** | foundation models / multi-modal tissue ML — **RECOMB → ISMB direct cross-link** |
| **Sara Mostafavi** | Univ. Washington / Allen | "Deep genomic models of allele-specific measurements" (S7) + **RECOMB Fri keynote** | ISMB 2026 RegSys likely | allele-specific regulatory genomics |
| **Ben Raphael** | Princeton | MOSAICField (S5), POTTR (S11) | EuroBioC2025 SpatialData adjacency; AACR cited | spatial alignment + cancer-evolution posets |
| **Rob Patro** | Univ. Maryland | Cuttlefish 3 (S1) | GBCC2025 tximeta / fishpond cycle; ISMB 2026 BOSC | k-mer indexing / quantification — **RECOMB → ISMB-BOSC + GBCC cross-link** |
| **Jingyi Jessica Li** | UCLA | Nullstrap-DE (S3), scDesignPop (S9), Information-Geometry (S14) | EuroBioC / GBCC adjacency via DESeq2/edgeR mention; ISMB MLCSB likely | single-cell statistical methods / FDR calibration — **3 RECOMB papers; biggest single-author cluster** |
| **Siavash Mirarab** | UCSD | "Deconvolving Phylogenetic Distance Mixtures" (S8) | ISMB EvolCompGen likely | phylogenetics |
| **Mohammed El-Kebir** | Univ. Illinois | "Maximum Agreement Secondary Structures" (S7), Phylogenetic distance mixtures (S8) | ISMB MLCSB / VarI possible | structure ensembles + phylogeny |
| **Vineet Bafna** | UCSD (Steering) | Cycle-Extractor for ecDNA (S11) | **AACR 2026 direct — ecDNA is a top AACR session theme** | ecDNA cancer biology — **RECOMB → AACR direct cross-link** |
| **Cenk Sahinalp** | NCI/NIH (Steering) | Subclonal structures via tumor tree alignment (S11) | AACR translational | tumor-evolution / subclonal phylogeny |
| **Peter Van Loo** | MD Anderson | Arborist (S11) | AACR direct (cancer-genomics PI) | tumor phylogeny — **RECOMB → AACR direct cross-link** |
| **Sven Rahmann** | Saarland | Error-correction for single-cell quantification (S3) | EuroBioC / GBCC adjacency possible | scRNA-seq quantification |
| **Jian Ma** | CMU (Steering) | Uncertainty-aware synthetic-lethality (S12) | ISMB MLCSB likely | synthetic-lethality + foundation models |
| **Elana Fertig + Genevieve Stein-O'Brien** | JHU | CycleGRN (S14) | AACR / JHU systems-bio adjacency | GRN dynamics — possible AACR cross-link |
| **Sushmita Roy / Sunduz Keles** | UW-Madison | Causal GRN from Perturb-seq (S9 — Keles) | ISMB RegSys / MLCSB | Perturb-seq causal inference |
| **Carl Kingsford / Rob Patro / Prashant Pandey** | UMd / CMU | Cuttlefish 3 (S1) | GBCC / BioC / ISMB BOSC | k-mer indexing infrastructure |
| **Sriram Sankararaman** | UCLA | Biobank-scale G×E (S13) | ISMB RegSys / TransMed | population genetics |
| **Hyunghoon Cho** | Yale | GOPHER differential-privacy GWAS (S13) | ISMB MLCSB / TransMed | privacy-preserving genomics |
| **Gamze Gursoy** | Columbia | Pangenome privacy (S1), PRS leakage (S13) | ISMB TransMed / VarI | privacy across the genomics pipeline |

**Keynote-level overlap:** Sara Mostafavi (RECOMB keynote Fri) is also senior author on a Session 7 paper — uncommon dual role. Olga Troyanskaya (RECOMB co-author Session 5) is ISMB 2026's Monday distinguished keynote — clean RECOMB → ISMB MLCSB cross-link 6 weeks later. Carlos Bustamante is ISMB 2026's closing keynote; not on RECOMB 2026 but Gamze Gursoy and Hyunghoon Cho (RECOMB privacy track) work the same privacy-PRS axis. RECOMB's Vineet Bafna ecDNA paper (S11) is the cleanest RECOMB → AACR direct hit.

---

## Tool/package shortlist for the bulk extraction pass

Highest-priority tool-page candidates after filtering. The full filter is: `[METHOD]` + (`[BIOC]` ∪ `[SOFTWARE]`), excluding pure-theory papers, retaining anything with a maintained code repo and AACR-corpus relevance. Estimated ~50–60 entries total; the top tier is listed here.

**Tier 1 — Direct AACR-axis tools (highest priority, build first):**

1. **Cycle-Extractor** (Faizrahnemoon, ..., **Bafna**, S11 Cancer & Evolution) — fast/accurate ecDNA sequence resolution. **Direct AACR 2026 ecDNA cross-link.**
2. **Arborist** (Weber, ..., **Van Loo**, S11) — tumor phylogeny from low-pass scDNA-seq. AACR-CCB axis.
3. **POTTR** (Käufler, ..., **B. Raphael**, S11) — recurrent evolutionary/developmental trajectories via posets.
4. **MOSAICField** (Liu, ..., **B. Raphael**, S5 Multi-Omics) — multimodal spatial alignment + morphology mapping; spatial-omics flagship.
5. **DIME** (Sun, Mou, Zheng, Huang, S5) — spatial multi-omics integration from unaligned serial sections.
6. **LineageMap** (Pan, Chen, Zhang, S9) — spatially informed cell lineage trees.
7. **CAMP** (Li, Ko, **Canzar**, S14 Single-Cell III) — coreset metacell partitioning; scales single-cell analysis.
8. **scDesignPop** (Dong, Cen, Song, **J.J. Li**, S9) — population-scale scRNA-seq simulator for benchmarking + privacy.
9. **Nullstrap-DE** (Jiang, Wang, **J.J. Li**, S3) — calibrated-FDR framework on top of DESeq2 + edgeR. **EuroBioC 2025 cross-link via edgeR/DESeq2.**
10. **MutPred-PPI** (Stewart, ..., **Radivojac**, S2) — interaction-specific PPI perturbation prediction by missense variants. Variant-interpretation axis.

**Tier 2 — Single-cell + spatial + transcriptomics (build second):**

11. **DiCoLo** (Li, Yang, ..., **Kluger**, S14) — localized differential gene co-expression, integration-free.
12. **CycleGRN** (Zhao, **Fertig**, Stein-O'Brien, S14) — GRN inference from cyclic-flow dynamics.
13. **DeltaNMF** (Karpurapu, Gersbach, **Singh**, S14) — neural NMF for differential gene programs.
14. **MOSAIC** (Lu, Kluger, Ma, S9) — spectral integrative phenotypic characterization.
15. **scProfiterole** (Coşkun, ..., Koyutürk, S9) — clustering for single-cell proteomic data; graph contrastive learning.
16. **GeoAdvAE** (Du, Lin, S9) — unpaired morphology + gene expression integration.
17. **Causal Perturb-seq GRN** (Z. Sun, Kang, **Keles**, S9) — IV-based causal GRN from Perturb-seq.
18. **CLADES** (Talukder, ..., Knowles, S7) — contrastive learning for differential splicing.
19. **Alternet** (Hoffmann, ..., Hartebrodt, S7) — splicing-aware GRN inference.
20. **Allele-specific deep models** (Tu, ..., **Mostafavi**, S7) — allele-specific measurement prediction; Mostafavi-keynote-adjacent.
21. **Information-Geometry** (Cai, ..., **J.J. Li**, Xin, S14) — discrete-continuous reconciliation for single-cell + spatial.
22. **Gene-First** (Yang, Huang, Xin, Cai, S3) — robust cell identification.

**Tier 3 — Protein/ML, drug design, synthetic lethality (build third):**

23. **ProtFlow** (Kong, ..., Hsieh, S2) — flow-matching protein sequence design.
24. **SpecLig** (Zhang, ..., **J. Ma**, S6) — energy-guided 3D ligand design.
25. **Synthetic-lethality foundation-model predictor** (Hua, Haber, **J. Ma**, S12) — direct cancer-target-discovery relevance.
26. **MSA-from-PLM** (Hoang, Armour-Garb, **M. Singh**, S12) — fast accurate MSA construction from protein language embeddings.
27. **MSA-Transformer hybrid proteins** (Tule, ..., Boden, S12) — generative hybrid-protein design.
28. **PLM mutation-effect disentanglement** (Ding, ..., Y. Luo, S12) — protein stability + function effect deconvolution.
29. **PCRR** (Madduri, Ellis, **Patel**, S12) — protein-compositional-ratio disease prediction.
30. **OOD foundation-model transform** (Pratapa, R. Singh, Tata, S2) — foundation-model out-of-distribution adapter.
31. **Bacterial protein function multimodal DL** (Muzio, ..., **Borgwardt**, S2).
32. **Evolutionary-profile-enhanced annotation** (S. Dai, ..., **Y. Luo**, S2).

**Tier 4 — Sequence/phylogeny infrastructure (build selectively):**

33. **Cuttlefish 3** (Khan, Dhulipala, Pandey, **Patro**, S1) — parallel external-memory colored compacted de Bruijn graph construction. Patro cross-link to GBCC/ISMB-BOSC.
34. **STELAR-X** (Saha, Bayzid, S10) — coalescent species-tree inference at 100k+ species scale.
35. **KuPID** (Borowiak, Yu, S4) — k-mer preprocessing for long-read isoform discovery.
36. **bronko** (Doughty, Tisza, **Treangen**, S1) — alignment-free viral genome variation detection.
37. **SLAB** (Naseri, ..., Zhi, S4) — PBWT haplotype block cores.
38. **Compressed inverted indexes** (Ingels, ..., Limasset, S4).
39. **Sequence-to-graph CNV via flow** (Magalhães, ..., **Marschall**, S1).
40. **pHapCompass** (Hosseini, ..., Aguiar, S4) — polyploid haplotype phase assembly.
41. **PaNDA** (Holtgrefe, ..., Schestag, S10) — phylogenetic diversity optimization in networks.

**Tier 5 — Privacy + statistical genetics (build selectively):**

42. **Privacy-preserving pangenome graphs** (Blindenbach, Soni, **Gursoy**, S1).
43. **PRS leakage** (Nikitin, **Gursoy**, S13).
44. **GOPHER** (Nandi, Neel, **Cho**, S13) — differential-privacy GWAS phenotype randomization.
45. **Biobank G×E** (Z. Liu, ..., **Sankararaman**, S13).
46. **EHR disease-liability** (Di, Cai, S13).

**Tier 6 — Theory-only (NOT tool pages; topic entries only):**

- Minimizer Density theoretical results (Ingels et al., S1)
- Flow Decompositions via Dominators (Sena, Tomescu, S4)
- Quartet-based tree-of-blobs consistency (J. Dai, Han, Molloy, S10)
- GWAS bias due to omitted interactions (Yelmen et al., S13)
- Evolutionary dynamics under phenotypic uncertainty (Mohanty, ..., **Berger**, S13)
- Random Matrix Theory sparse PCA (Chardès, S3) — borderline; has code, may upgrade to tool page
- Constrained diffusion as evolution paradigm (Lazarev, ..., **Berger**, S8) — borderline

**Satellite-workshop tool pages (deferred until satellite programs publish):**

- RECOMB-Seq, RECOMB-CCB (closest to AACR cancer-comp-bio axis), RECOMB-CG, RECOMB-Genetics, RECOMB-Privacy, RECOMB-Arch, RECOMB-RSG. Expect ~30–50 satellite talks total across the 7 satellites; estimated ~15–25 will yield tool pages with `Status: satellite-workshop`.

---

## Open follow-ups before bulk extraction

1. **Watch keynote titles.** All 4 keynote speakers public, titles not. Likely posted to [keynotes.html](http://recomb.org/recomb2026/keynotes.html) closer to the date or announced at the opening. Recheck May 24–26.
2. **Satellite-workshop programs.** RECOMB-CG and RECOMB-Seq sites are populated; RECOMB-CCB / RECOMB-Privacy / RECOMB-Arch / RECOMB-Genetics / RECOMB-RSG schedules are sparser. Recheck May 20–24. URLs:
   - [recomb-seq.github.io](https://recomb-seq.github.io/)
   - [recomb-cg.org](https://recomb-cg.org/)
   - The other 5 — check [recomb.org/satellites/](https://recomb.org/satellites/) for current links
3. **Best-paper announcements.** Announced from stage at the closing session Fri May 29 PM. Same-day update to the tool-page index + RECOMB-2026 vault to flag winners.
4. **Partnering-journal venue per paper.** Selections for *Cell Systems* / *Genome Research* fast-track may be announced at the closing or in a post-meeting email; remainder route to *JCB* special issue. Track per-paper venue assignment over May–Sep 2026; backfill into Proceedings rows in tool pages.
5. **bioRxiv preprint sweep.** Most RECOMB 2026 papers have a bioRxiv / arXiv preprint already (the [proceedings hub](https://recomb.org/proceedings/proceedings/2030-2026/2026/) lists them). Build the title → bioRxiv DOI table before the meeting so tool-page Preprint rows can be filled in pre-meeting.
6. **Slide deposits (post-meeting).** No central RECOMB Zenodo community. Sweep speaker labs / Bluesky #RECOMB2026 the week of May 30 – Jun 6 for slide deposits. Berger lab, Klau lab, Mirarab lab, Patro lab, J.J. Li lab historically deposit; most others don't.
7. **Recordings.** Default assumption is no recordings. If RECOMB YouTube posts sessions, recheck 6–10 weeks post-meeting (Jul–Aug 2026).
8. **RECOMB → ISMB cross-link map.** Build the RECOMB 2026 ↔ ISMB 2026 cross-link table once ISMB MLCSB rosters firm in mid-June 2026. Expected hits: Troyanskaya (RECOMB S5 paper + ISMB Mon keynote), Mostafavi (RECOMB keynote + S7 paper + likely ISMB RegSys), Berger (RECOMB S8+S13 + likely ISMB MLCSB), J.J. Li (3 RECOMB papers + likely ISMB MLCSB).
9. **RECOMB → AACR cross-link map.** Confirm the 3 most likely direct hits: Cycle-Extractor (Bafna) for ecDNA, Arborist (Van Loo) for tumor phylogeny, POTTR / subclonal-trees (Raphael / Sahinalp) for tumor evolution. All three are leading candidates for AACR 2026 / 2027 poster citations.
