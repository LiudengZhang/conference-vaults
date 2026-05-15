# Landscape — 642 CT posters by phase bucket

The clinical-trials slice of AACR 2026 was harvested via a hybrid strategy: a keyword union over the Abstracts Online search plus a direct session-endpoint pull for 25 CT-track session IDs. Of the resulting records, 642 survived filtering on `Activity` (keeping both `Abstract Submission` and `Late Breaking and Clinical Trials`) plus `PlayerUrl`. This page buckets those 642 along two orthogonal dimensions:

- **Primary — phase stratification** (inferred from `Title`, `SessionTitle`, and `Abstract`): first-in-human/Phase 0/Phase 1a, Phase 1 dose-escalation/expansion, Phase 1/2, Phase 2, Phase 3 and Phase 3/4, biomarker-correlative, trial-design methodology.
- **Secondary — track**: *In-Progress* (trial-in-progress posters, study-design/rationale posters), *Results-reporting* (preliminary or final efficacy/safety data), *Biomarker-correlative* (Biomarkers Predictive of Therapeutic Benefit sessions), *Methodology* (Biostatistics in CT / Mathematical Modeling / Quantitative Pharmacology sessions).

**LBR tier:** 282 of 642 posters (~44%) are `Late Breaking and Clinical Trials`. LBR is the highest-signal subset because it is where most first-in-human and late-phase readouts are reported. Flagged in-line as **[LBR]** below.

All PresentationNumbers cited are from the JSONL; counts are exact.

## Phase-bucket tally

| Bucket | Count | LBR | Track mix |
|---|---:|---:|---|
| Phase 1 dose-escalation / expansion | 127 | 52 | 99 Results, 28 In-Progress |
| Phase 1/2 and Phase 2 (Phase II) | 71 | 31 | 71 Results |
| Biomarker-correlative | 70 | 4 | 46 Results, 24 Biomarker-correlative |
| First-in-human / Phase 0 / Phase 1a | 66 | 48 | 66 Results |
| Phase 3 and Phase 3/4 | 66 | 49 | 45 Results, 21 In-Progress |
| Late-Breaking Research: Clinical Research (unphased) | 65 | 65 | 65 Results |
| Phase 1/2 (combined-phase) | 49 | 27 | 23 Results, 26 In-Progress |
| Trial-design methodology | 21 | 3 | 15 Methodology, 4 Results, 2 In-Progress |
| Unclassified (no phase signal in title or session) | 107 | 3 | 107 Results |
| **Total** | **642** | **282** | — |

The *Unclassified* bucket is mechanism-focused preclinical/translational posters harvested because their abstracts mention "clinical trial" or a specific NCT number, but whose phase is not explicit; they are CT-adjacent rather than trial posters per se. The *LBR Clinical Research (unphased)* bucket is the four `Late-Breaking Research: Clinical Research 1-4` sessions — these are typically translational and biomarker papers, not dose-escalation readouts, so phase tagging was inconsistent.

---

## First-in-human / Phase 0 / Phase 1a (66 posters, 48 LBR)

The FIH layer at AACR 2026 is dominated by two sessions — `First-in-Human Phase I Clinical Trials` (23 posters) and `Phase 0 and First-in-Human Phase I Clinical Trials` (21 posters) — plus FIH-flagged posters scattered across LBR Experimental/Molecular Therapeutics and LBR Immunology tracks. Approximately 73% are LBR, reflecting the "fresh readout" tier. Modality mix skews heavily to novel ADCs, bispecific T-cell engagers, targeted radiopharmaceuticals, molecular glues, and CAR-NK/CAR-T — first-cycle safety and preliminary RP2D signals.

| # | Title | Presenter | Session |
|---|---|---|---|
| CT041 [LBR] | Investigator-initiated phase I trial of an oligonucleotide therapeutic targeting long noncoding RNA TUG1 for recurrent glioblastoma | Keiko Shinjo | First-in-Human Phase I Clinical Trials |
| CT046 [LBR] | A first-in-class HER2-targeted radiopharmaceutical therapy: Initial findings from the Phase 0/1 HEAT trial of 177Lu-RAD202 | Dimitris Voliotis | First-in-Human Phase I Clinical Trials |
| CT060 [LBR] | First-in-human phase 1 study of D3S-002, a purposely designed ERK1/2 inhibitor, in advanced solid tumors with MAPK pathway mutations | Shaonan Wang | First-in-Human Phase I Clinical Trials |
| CT061 [LBR] | A phase I study of the type II ROS1 TRK inhibitor ANS03 in ROS1 fusion-positive lung cancers | Shengxiang Ren | First-in-Human Phase I Clinical Trials |
| CT065 [LBR] | Preliminary safety, PK, and PD of SGR-3515, a Wee1/Myt1 dual inhibitor, from an ongoing Phase 1 study | Stephanie Lheureux | First-in-Human Phase I Clinical Trials |
| CT097 [LBR] | A Phase 1, first-in-human study of the SMARCA2 degrader PLX-61639 in SMARCA4-mutated advanced solid tumors | Jorge F. DiMartino | Phase I Clinical Trials in Progress |
| CT109 [LBR] | A phase 0/1 study of PRMT5 inhibitor BMS-986504 in recurrent glioblastoma with MTAP deletion | An-Chi Tien | Phase 0 and First-in-Human Phase I Clinical Trials |
| CT114 [LBR] | Phase 1a/1b results of GIGA-564, a novel intratumoral Treg-depleting anti-CTLA-4 antibody | James Gulley | Phase 0 and First-in-Human Phase I Clinical Trials |
| CT126 [LBR] | Phase 1 first-in-human results of HMBD-002, an IgG4 anti-VISTA mAb | Eugene Kennedy | Phase 0 and First-in-Human Phase I Clinical Trials |
| CT127 [LBR] | First-in-human study of ES014, a bispecific antibody targeting CD39 and TGF-β | Yehua Zhu | Phase 0 and First-in-Human Phase I Clinical Trials |
| CT129 [LBR] | First-in-human Phase 1a/b of pan-RAF-MEK molecular glue NST-628 | Ahmad Tarhini | Phase 0 and First-in-Human Phase I Clinical Trials |
| CT131 [LBR] | Global FiH dose escalation of BAY2862789, a DGKα inhibitor (keyboard design) | Shirish Gadgeel | Phase 0 and First-in-Human Phase I Clinical Trials |
| CT133 [LBR] | First-in-human trial of 225Ac-DOTA-daratumumab alpha radioimmunotherapy | Scott Goldsmith | Phase 0 and First-in-Human Phase I Clinical Trials |
| LB269 [LBR] | Mechanistic insights into the pharmacology of CDR609 targeted immunotherapy | Athanasia Dasargyri | Late-Breaking Research: Immunology 3 |
| LB441 [LBR] | Platform PBPK-QSP model for first-in-human dose selection of GenSci139 | Yehua Xie | Late-Breaking Research: Bioinformatics |

## Phase 1 dose-escalation / expansion (127 posters, 52 LBR)

The single largest bucket. Most are dose-escalation readouts or Phase I trials-in-progress for targeted therapies, ADCs, radioligands, cell therapies, and immunomodulators. The session-driven subset comprises `Phase I Clinical Trials` (19), `Phase I Clinical Trials in Progress` (28), and a large CT-adjacent tail drawn from subject-specific sessions (ADC Linker Engineering, Adoptive Cell Therapy, Immune Checkpoints) where the title or abstract explicitly references Phase 1. 41% are LBR.

| # | Title | Presenter | Session |
|---|---|---|---|
| CT050 [LBR] | Preliminary results of TAVO412, an anti-EGFR/cMET/VEGF multispecific antibody | Mark Chiu | First-in-Human Phase I Clinical Trials |
| CT070 [LBR] | Dose escalation of autologous GD2-CAR-T cells | Michael Brown | Phase I Clinical Trials in Progress |
| CT074 [LBR] | Phase 1 of CAN2109, a long-acting tumor-retained immunogenic cell death inducer | Jiancheng Huang | Phase I Clinical Trials in Progress |
| CT082 [LBR] | Phase 1b/2 toripalimab + nadunolimab for MSS mCRC | Jacob Lowy | Phase I Clinical Trials in Progress |
| CT092 [LBR] | Phase 1a/1b first-in-human study of DB-1317, an ADC targeting ADAM9 | Charlotte Lemech | Phase I Clinical Trials in Progress |
| CT115 [LBR] | LYC001 IL-2 immunotherapy Phase Ia dose escalation | Wenfeng Zeng | Phase 0 and First-in-Human Phase I Clinical Trials |
| CT179 [LBR] | SON-1010 (IL12-FHAB) + trabectedin in advanced soft-tissue sarcoma | Richard Kenney | Phase I Clinical Trials |
| CT191 | Ruxolitinib + abemaciclib in myelofibrosis (Phase I) | Brian Chernak | Phase I Clinical Trials |
| CT192 [LBR] | First report: patients treated with LP-118, a novel Bcl-2/Bcl-xL dual inhibitor | Qing Zhou | Phase I Clinical Trials |
| CT200 [LBR] | Phase I dose-escalation of ENPP1 inhibitor vizenpistat | Mohan Kaadige | Phase I Clinical Trials |
| CT267 [LBR] | Phase 1 of RPT1G in R/R AML and high-risk MDS | Parisa Moghaddam-Taaheri | Phase I and Phase II Clinical Trials in Progress |
| CT292 [LBR] | CAN016, a HER2 dual-payload ADC, Phase 1 clinical development | Pengqi Xu | Phase I and Phase II Clinical Trials in Progress |
| CT295 [LBR] | Phase I of CRD3874-SI, a systemic 3rd-gen STING agonist | Ciara Kelly | Phase I and Phase II Clinical Trials in Progress |
| LB063 [LBR] | Novel oral G-quadruplex stabilizer for DNA-repair-deficient cancers | Hong Xu | Late-Breaking Research: Experimental and Molecular Therapeutics 1 |
| LB345 [LBR] | HZ-V055, an oral pan-Ras molecular glue in RasMut cancer | Yizhe Wu | Late-Breaking Research: Experimental and Molecular Therapeutics 3 |

## Phase 1/2 (combined-phase trials) (49 posters, 27 LBR)

Combined Phase 1/2 protocols — usually Phase 1 dose-escalation plus Phase 2 expansion in the same study — are heavily represented in the `Phase I and Phase II Clinical Trials in Progress` session (27 posters) plus LBR spillover. 55% are LBR. Mix tilts toward novel-modality ADCs (EGFR/HER3, TROP2, ITGA2), bispecific T-cell engagers, and radioligand therapies where sponsors have bundled dose-finding with expansion from the outset.

| # | Title | Presenter | Session |
|---|---|---|---|
| CT073 [LBR] | FiREBOLT: Phase 1 radioligand therapy LY4337713 in FAP+ solid tumors | Gary Ulaner | Phase I Clinical Trials in Progress |
| CT087 [LBR] | Phase I/II FIH of IPN60300, a first-in-class ITGA2 ADC | Elisabetta Leo | Phase I Clinical Trials in Progress |
| CT128 [LBR] | Phase I/II of JS212, an EGFR/HER3 bispecific ADC | Wei Su | Phase 0 and First-in-Human Phase I Clinical Trials |
| CT198 [LBR] | Phase 1 trial of a first-in-class antagomir therapeutic | Zdravka Medarova | Phase I Clinical Trials |
| CT213 [LBR] | Phase I/II of EP0031 (lunbotinib), a next-gen RET inhibitor | Jaime Rubio-Perez | Phase II and Phase III Clinical Trials in Progress |
| CT270 [LBR] | Phase I BCC020: DFMO + AMXT-1501 | Giselle Saulnier Sholler | Phase I and Phase II Clinical Trials in Progress |
| CT284 [LBR] | First-in-human Phase I/II of BPI-572270, a RAS(ON) multi-tri-complex inhibitor | Hong Lan | Phase I and Phase II Clinical Trials in Progress |
| CT285 [LBR] | DOMISOL: FIH Phase I/II of DT-7012 (CCR8 mAb) — adaptive Bayesian | Stephan Schann | Phase I and Phase II Clinical Trials in Progress |
| CT287 [LBR] | FIH Phase 1/2 dose-escalation of CNS-penetrant PARP1-selective agent | Meghal Gandhi | Phase I and Phase II Clinical Trials in Progress |
| CT288 [LBR] | FIH study of oral PARG inhibitor SYN608 | Xuzhen Tang | Phase I and Phase II Clinical Trials in Progress |
| CT289 [LBR] | Phase Ib of POLQ inhibitor SYN818 + olaparib | Xuzhen Tang | Phase I and Phase II Clinical Trials in Progress |
| CT290 [LBR] | NTS071-101: Phase 1/2a NTS071 in solid tumors | Qiancheng Shen | Phase I and Phase II Clinical Trials in Progress |
| CT291 [LBR] | FIH IL-12 Prodrug KGX101 | Lu Si | Phase I and Phase II Clinical Trials in Progress |
| CT294 [LBR] | TROPIKANA: TROP2 CAR IL-15 cord-blood NK (BOIN12 design) | Oriol Mirallas | Phase I and Phase II Clinical Trials in Progress |
| CT099 [LBR] | VBC101, EGFR/cMET bispecific ADC, Phase 1/2a | Nehal Lakhani | Phase I Clinical Trials in Progress |

## Phase 1/2 and Phase 2 (Phase II readouts) (71 posters, 31 LBR)

`Phase II Clinical Trials` (25 posters) is the main session anchor, supplemented by subject-specific sessions where the title clearly indicates Phase II (Combination Immunotherapies, Clinical Correlates of Immunotherapy, ADC Linker Engineering 3, etc.). 44% LBR. Readouts here are efficacy-focused with preliminary translational correlatives.

| # | Title | Presenter | Session |
|---|---|---|---|
| CT236 [LBR] | NIBIT epigenetic immune reprogramming for PD-1-resistant melanoma (Phase II) | Alessia Covre | Phase II Clinical Trials |
| CT160 | Phase Ib/II surufatinib + sintilimab + capecitabine in small bowel ca | Xiaoyu Xie | Phase II and Phase III Clinical Trials |
| CT262 [LBR] | Elacestrant + everolimus or abemaciclib in ER+/HER2− mBC (umbrella ELEVATE) | Tomer Wasserman | Phase II Clinical Trials |
| LB032 [LBR] | KH617 reverses glioblastoma resistance to alkylators via MGMT modulation | Yun Feng | Late-Breaking Research: Chemistry |
| LB152 [LBR] | ACR-368 + PD-L1 coordinated innate/adaptive immunity | Amira Elbakry | Late-Breaking Research: Immunology 2 |
| LB234 [LBR] | Cabozantinib remodels pancreatic TME to potentiate immunotherapy | Yana Zavros | Late-Breaking Research: Tumor Biology 1 |
| 6453 | Serum PD biomarkers of IPI/NIVO/RELA + sarilumab in melanoma (Stage 1 Phase II) | Teruyuki Mizutani | Clinical Correlates of Immunotherapy |
| 6487 | Camrelizumab + chemo as 2L in advanced ESCC (Phase II) | Linlin Wang | Combination Targeted Therapy |
| 6547 | Phase II tremelimumab + durvalumab in advanced HCC | Sukeshi Arora | Immune Checkpoint Blockade |
| 3788 | Single-cell analysis of clinical benefit in PD-L1+ NSCLC (Phase II correlative) | Jii Bum Lee | Combination Immunotherapies |
| 2008 | Fasting-induced ferroptosis in breast cancer (Phase II correlative) | Claudio Vernieri | Metabolic Regulation in Breast and Gynecologic Cancers |
| 7071 | CRISPRi screen identifies ARID1A-PRC2 synthetic lethality | Yan-Jin Liu | Epigenetic Modulators 2 |
| 2933 | Itareparib selective non-trapper PARP1i for combination (Phase II) | Alessia Montagnoli | Cellular Responses to Anticancer Drugs |
| 1660 | NoNabody against GRP for SCLC (Phase II) | Pablo Garrido Rodriguez | Antibody Technologies and Platforms 1 |
| 5698 | Exploiting MYC oncogenic stress for therapeutic benefit in lymphoma | Smriti Kanangat | Mechanisms of Anticancer Drug Action |

## Phase 3 and Phase 3/4 (66 posters, 49 LBR)

Phase III readouts dominate `Phase II and Phase III Clinical Trials` (26), `Phase II and Phase III Clinical Trials in Progress` (22), and LBR Clinical Research cohorts. 74% LBR — the highest LBR fraction of any phase bucket, consistent with Phase 3 being the venue for conference-defining readouts. Multiple posters report exploratory translational analyses of completed pivotal trials (RATIONALE 305, DREAM3R, CHECKMATE-816).

| # | Title | Presenter | Session |
|---|---|---|---|
| CT137 [LBR] | QoL outcomes in Bria-ABC late-stage metastatic Phase 3 trial | Blaise Bayer | Phase II and Phase III Clinical Trials |
| CT206 [LBR] | Larotrectinib in NTRK1/2/3-amp solid tumors — TAPUR Phase II basket | Jordi Rodon | Phase II and Phase III Clinical Trials in Progress |
| CT211 [LBR] | Palbociclib in CCND1-amp lung cancer — TAPUR Phase II basket | Evan Pisick | Phase II and Phase III Clinical Trials in Progress |
| CT212 [LBR] | Neratinib in EGFR exon-18 NSCLC — SUMMIT Phase 2 basket | Steve Shen | Phase II and Phase III Clinical Trials in Progress |
| CT223 [LBR] | AACR-ADOPT-GEA: adaptive biomarker-driven organ-preservation platform trial | Ronan McLaughlin | Phase II and Phase III Clinical Trials in Progress |
| CT224 [LBR] | Adaptive Phase 2/3 of EIK1001 (TLR7/8) + pembrolizumab (TeLuRide-006) | Diwakar Davar | Phase II and Phase III Clinical Trials in Progress |
| LB011 [LBR] | RATIONALE 305 biomarker analysis (tislelizumab + chemo 1L gastric) | Ciji Cabrera | Late-Breaking Research: Clinical Research 1 |
| LB105 [LBR] | DREAM3R Phase 3 translational analysis (durvalumab + chemo mesothelioma) | Valsamo Anagnostou | Late-Breaking Research: Molecular/Cellular Biology and Genetics 1 |
| 4237 | IF-based adaptive immune subtypes in CHECKMATE-816 | Qichen Wang | Adaptive Immunity in Cancer |
| 2507 | Causal ML personalizes endocrine therapy in DCIS (Phase 3 follow-on) | Emma Graham Linck | Data-Driven Approaches to Precision Oncology |
| 4170 | AI multimodal workflow for late-phase trial outcome prediction | Inbal Gazy | Digital Pathology 3 |
| 2280 | AR promotes survival of endocrine-therapy-responsive ER+ breast cancer | Patrick Aouad | Hormone Receptor Signaling and Therapeutic Targeting |
| 4221 | CAPTYN ML model for atezo-bev benefit in HCC | Gaehoon Jo | Machine Learning Approaches for Cancer Prediction |
| 5546 | Rilvegostomig vs anti-PD-1 monotherapy — immune activation | Jun Ren | Bi- and Tri-Specific Antibody Therapies |
| 2950 | Palazestrant recruits NCoR1 for complete ER antagonism (Phase III) | Susanna Barratt | Cellular Responses to Anticancer Drugs |

## Late-Breaking Research: Clinical Research (unphased) (65 posters, 65 LBR)

The four `Late-Breaking Research: Clinical Research 1-4` sessions are entirely LBR and entirely unphased by construction — these are translational/biomarker readouts, novel diagnostics, access/outcome analyses, and correlative studies. I did not force a phase tag on a poster that did not advertise one. Representative depth:

| # | Title | Presenter | Session |
|---|---|---|---|
| LB002 [LBR] | Nutrigenomic stratification of EO-CRC (HMGCS2-low, stress-response targetable) | Chia-Wei Cheng | Late-Breaking Research: Clinical Research 1 |
| LB014 [LBR] | HSPBP1 9-bp insertion predicts immunotherapy response | Marianne Hannisdal | Late-Breaking Research: Clinical Research 1 |
| LB114 [LBR] | Raman-spectroscopy liquid biopsy (clinical feasibility) | Seungwook Kim | Late-Breaking Research: Clinical Research 2 |
| LB118 [LBR] | TP53-alteration real-world evidence linking mutation class to genomic instability | Atul Bharde | Late-Breaking Research: Clinical Research 2 |
| LB128 [LBR] | Adaptive genomically-classified molecular clusters in pan-Indian lung cohort | Vidya Veldore | Late-Breaking Research: Clinical Research 2 |
| LB320 [LBR] | Cancer vs Alzheimer inverse relationship — autophagy/apoptosis | Jagadeesh Narasimhappagari | Late-Breaking Research: Clinical Research 3 |
| LB322 [LBR] | Targeting senescence for chemo-induced muscle aging (Phase Ib ancillary) | Yuliya Zektser | Late-Breaking Research: Clinical Research 3 |
| LB324 [LBR] | Community Living Lab learning health system for prostate cancer | Opeyemi Bolajoko | Late-Breaking Research: Clinical Research 3 |
| LB326 [LBR] | Point-of-care PRAME-specific TCR-T induces remission in ALL | Christian Seitz | Late-Breaking Research: Clinical Research 3 |
| LB327 [LBR] | Adaptive fludarabine dosing in pediatric CAR-T | Emma Barlow | Late-Breaking Research: Clinical Research 3 |
| LB412 [LBR] | Personalized T-cell approaches in gastric cancer | Giulia Milardi | Late-Breaking Research: Clinical Research 4 |
| LB414 [LBR] | TIL therapy (LM103) updated efficacy + translational biomarker | Li Zhou | Late-Breaking Research: Clinical Research 4 |
| LB424 [LBR] | GZMA+ CD8+ T cells and pCR of BRCA-mutated breast cancer | Songhan Li | Late-Breaking Research: Clinical Research 4 |
| LB426 [LBR] | Tumor-intrinsic TGF-β drives hyperprogression in SCLC | Anish Thomas | Late-Breaking Research: Clinical Research 4 |
| LB429 [LBR] | Severe liver metastases impact immunotherapy response | Aung Naing | Late-Breaking Research: Clinical Research 4 |

## Biomarker-correlative (70 posters, 4 LBR)

`Biomarkers Predictive of Therapeutic Benefit 1-6` plus `Pharmacogenomics and Translational Biomarkers for Precision Cancer Therapy` anchor this bucket. Only 6% LBR — predictive-biomarker work is mostly Abstract-Submission-tier, not late-breaking. Most posters are retrospective correlative analyses that run across a set of trials rather than a single Phase X study; several develop ML/DL scoring models over existing trial cohorts.

| # | Title | Presenter | Session |
|---|---|---|---|
| 1009 | Landscape of homozygous CN losses across 400K tumors — clinical actionability | Timothy Yap | Biomarkers Predictive of Therapeutic Benefit 1 |
| 1046 | DL prediction of HRD in breast cancer from transcriptomics | Yashwin Madakamutil | Biomarkers Predictive of Therapeutic Benefit 2 |
| 2435 | TLS induction predicts and enhances famitinib + PD-L1 response | Wei Kou | Biomarkers Predictive of Therapeutic Benefit 3 |
| 3731 | Gene-expression predictor of bevacizumab response | Joshua Tay | Biomarkers Predictive of Therapeutic Benefit 4 |
| 5239 | Phase I DT-9081 biomarker dynamics (ex vivo cytokine, urinary) | Stephan Schann | Biomarkers Predictive of Therapeutic Benefit 5 |
| 7722 | Nelmastobart biomarker dynamics (BTN1A1) in CRC | Stephen Yoo | Biomarkers Predictive of Therapeutic Benefit 6 |
| 6942 | Validation of HER2/TROP2/NECTIN4 IHC for ADC MATCH trial | Kyle Beauchamp | Antibody-Drug Conjugates 2 |
| 2438 | Circulating proteomic biomarkers for HRR-driven solid tumors (IMAGENE basket) | Yuehan Feng | Biomarkers Predictive of Therapeutic Benefit 3 |
| LB455 [LBR] | AT-108 in-situ tumor-to-dendritic-cell conversion — biomarker characterization | Fabio Rosa | Late-Breaking Research: Experimental and Molecular Therapeutics 4 |
| 3775 | Integrated CTC analysis for multi-omics biomarker platforms | Kangwon Jang | Circulating Tumor Cells, Metastasis, and Dissemination Biology 2 |
| 2498 | OncoKB 2025 updates — precision-oncology knowledge base | Moriah Nissan | Data-Driven Approaches to Precision Oncology |
| 5444 | HLA class I allele typing in a liquid-biopsy platform | Adrian Bubie | Application of Bioinformatics to Cancer Biology |
| 33 | Whole-patient temporal multimodal foundation model | Andrew Zhang | Agentic AI in Cancer |
| 6303 | Predicting endocrine toxicity in large prospective cohort | Hala Awad | Advances in Survivorship |
| 7722 | BTN1A1 expression and TME dynamics in CRC (nelmastobart) | Stephen Yoo | Biomarkers Predictive of Therapeutic Benefit 6 |

## Trial-design methodology (21 posters, 3 LBR)

The `Biostatistics in Clinical Trials / Surgical Oncology` session (13 posters), `Mathematical Modeling and Statistical Methods`, and `Quantitative Pharmacology and Translational Modeling` sessions anchor this bucket, plus three CT-numbered trial-in-progress posters whose titles explicitly advertise a design innovation (FORTE master protocol, ADOPT-GEA adaptive platform, TeLuRide-006 Phase 2/3 adaptive). 71% are classical statistical methods or meta-analyses; the remainder are the higher-signal design-innovation posters that the synthesis page dissects.

| # | Title | Presenter | Session |
|---|---|---|---|
| CT273 [LBR] | FORTE: Phase 2 master protocol for BRAF-altered cancers | Catherine Rachfalski | Phase I and Phase II Clinical Trials in Progress |
| CT212 [LBR] | Neratinib in EGFR exon-18 NSCLC — SUMMIT global basket (Phase 2) | Steve Shen | Phase II and Phase III Clinical Trials in Progress |
| CT128 [LBR] | JS212 Phase I/II (Bayesian Optimal Interval design) | Wei Su | Phase 0 and First-in-Human Phase I Clinical Trials |
| 6435 | Dose optimization in multi-indication basket trials — Bayesian borrowing for OBD | Danny Lu | Biostatistics in Clinical Trials / Surgical Oncology |
| 6437 | Adjuvant CDK4/6 inhibitors — HR-based network meta-analysis (NetMetaEasy) | Balazs Gyorffy | Biostatistics in Clinical Trials / Surgical Oncology |
| 6439 | Fastest-growing-lesion growth rate vs RECIST SoD — real-world NSCLC | Dean Bottino | Biostatistics in Clinical Trials / Surgical Oncology |
| 6441 | Post-CDK4/6 safety network meta-analysis HR+/HER2− mBC | Martina Pagliuca | Biostatistics in Clinical Trials / Surgical Oncology |
| 6444 | ctDNA + multi-site disease burden prognostic model | Justin Bader | Biostatistics in Clinical Trials / Surgical Oncology |
| 6434 | Affective trajectories in adaptive pharmacotherapy (EMA data) | Hadeel Al-Sahli | Biostatistics in Clinical Trials / Surgical Oncology |
| 6838 | Combination therapy severe-AE rates consistent with independent action | Kunhee Kim | Mathematical Modeling and Statistical Methods |
| 6832 | Virtual-trial framework for rotational multi-agent therapies (PDAC mice) | Krithik Vishwanath | Mathematical Modeling and Statistical Methods |
| 1818 | OBI-902 TROP2 ADC — preclinical PBPK modeling for resistance | Chi-Huan Lu | Quantitative Pharmacology and Translational Modeling |
| 1830 | SP09253 RAS(ON) molecular glue — translational PKPD modeling | Zherong Zhang | Quantitative Pharmacology and Translational Modeling |
| 2602 | STING master-protocol — TMB-high liquid biopsy cohort | Adrien Mouren | Liquid Biopsies: Circulating Nucleic Acids 2 |
| 6436 | 25-year ClinicalTrials.gov landscape of adjuvant immunotherapy in PDAC | Carmel Awadallah | Biostatistics in Clinical Trials / Surgical Oncology |

---

## Reading guide

Three starting points, depending on what you want:

- **"Show me what is actually being read out"** — the 127-poster **Phase 1 dose-escalation/expansion** and the 66-poster **Phase 3** buckets are where fresh efficacy/safety data lives. Filter `Activity = Late Breaking and Clinical Trials` on the poster browser.
- **"Show me what is being launched"** — the **Phase 1/2 (combined-phase) in-progress** and **Phase 3 in-progress** rows together amount to 47 trial-in-progress study-design posters. Representative of sponsor pipelines at AACR 2026.
- **"Show me the methodology shift"** — the 21-poster **Trial-design methodology** bucket, plus Bayesian/BOIN-design posters in the Phase 1 and Phase 1/2 buckets, feed the [synthesis-trial-design-methodology](./synthesis-trial-design-methodology.md) page.

**Per-bucket totals** (for cross-reference with the full poster browser on the [overview page](./index.md)):

- FIH / Phase 0 / Phase 1a: **66**
- Phase 1 dose-escalation / expansion: **127**
- Phase 1/2 (combined-phase): **49**
- Phase 1/2 and Phase 2: **71**
- Phase 3 and Phase 3/4: **66**
- LBR Clinical Research (unphased): **65**
- Biomarker-correlative: **70**
- Trial-design methodology: **21**
- Unclassified: **107**
- **Total: 642**

LBR tier cumulative: **282 / 642** (43.9%). The LBR:Abstract ratio is highest in the phase buckets closest to a readout (FIH 73%, Phase 3 74%, LBR Clinical Research 100%) and lowest in correlative/methodology tiers (Biomarker 6%, Methodology 14%), which matches the intent of the Late-Breaking tier.
