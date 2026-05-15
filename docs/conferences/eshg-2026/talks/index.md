# Talks — ESHG 2026

The primary artifact of this vault: **one Markdown file per talk**. ESHG 2026 is a hybrid meeting — some talks are tool / pipeline / package debuts, others are clinical-genetics / cohort readouts, others are pure-methods papers, others are Award Lectures. The per-talk schema accommodates all four with one Anchor field and adds a **European-cohort tag** because cohort-anchored talks at ESHG cluster around a small set of named biobanks.

> **Status:** Template + master index. Per-talk pages will be populated once the EJHG abstract supplement lands (typically week of the meeting, ~early June 2026) and the speaker list reconciles against session assignments. Pre-meeting stubs flagged `*expected per Programme-at-a-Glance + speaker list*` are sourced from the public Programme-at-a-Glance, the confirmed-speakers page, lab websites, and consortium dashboards (FinnGen, UK Biobank, Generation R, GeneRISK); titles and assignments will be reconciled with the EJHG supplement.

## Per-talk template

Each talk file (e.g., `mendel-lecture-2026.md`, `finngen-r13-cancer.md`, `ukb-cancer-prs.md`) follows this schema. Copy and fill:

```markdown
# <Talk title — short>

> **Session:** <session ID (PL/E/I/S/C) + name + date + time CEST + room> · **Track:** <track / theme> · **Abstract:** <EJHG abstract #, if assigned>

## At a glance

- **Speaker:** <name, degrees>
- **Affiliation:** <institution, department, lab, country>
- **Day / session / track:** <Sun Jun 14 / S07 Cancer Mechanisms / Cancer Genetics>
- **Talk title:** <full title as in programme>
- **Anchor type:** <tool / package / pipeline | study / cohort / readout | methods paper | award lecture>
- **Anchor:** <package name + Bioconductor/CRAN/PyPI link | study acronym + NCT or cohort | manuscript citation + DOI | award name>
- **European cohort tag:** <FinnGen R13 / UK Biobank / Generation R / GeneRISK / Estonian Biobank / deCODE / SweBCG / HEBON / GC-HBOC / CanRisk / EBMT / N/A>
- **Co-authors / consortium:** <if applicable — e.g., FinnGen, UK Biobank, GBMI>
- **Preprint / paper:** <medRxiv / bioRxiv / EJHG / HGG Advances / Nature Genetics DOI, if accompanying>

## Key result

<One paragraph. Numbers + cohort size + effect size if known. If pre-program,
mark `*expected per <lab page / cohort dashboard / prior-year talk>*` or
`*pre-supplement speculation*`.>

## Methods / approach

<2–4 sentences. What cohort, what assay, what statistical / computational
method, what comparator. For tool talks: what it consumes / produces, key
methodological idea, language / framework. For award lectures: career
retrospective vs landmark contribution framing.>

## Why it matters for the corpus

<1–2 sentences. The cancer-genomics relevance specifically — does it inform
hereditary-cancer panel design, cancer-PRS stratification, somatic-mosaicism
detection, pharmacogenomics-guided oncology, or methods used in AACR / ASCO /
ASH / ASHG talks?>

## Cross-links to corpus

- **ASHG 2026:** <related Oct talk, if applicable — ESHG-first / ASHG-update pattern>
- **AACR 2026:** <related session / poster>
- **ASCO 2026:** <trial / biomarker that uses the method / cohort / panel>
- **EHA 2026:** <same-week heme-genomics tie-in (June 11–14, Stockholm)>
- **ASH 2026:** <CHIP / MN-predisposition tie-in>
- **ISMB 2026 / RECOMB 2026 / ECCB 2026:** <methods-paper sibling>
- **AGBT 2026:** <upstream platform if this talk applies a new sequencing modality>
- **EuroBioC 2025 tools:** <Bioconductor package used / extended>
- **Other ESHG 2026 talks:** <session-mates, same-cohort, same-method>

## Sources

- EJHG abstract: <DOI / URL or "pending supplement">
- Preprint / paper: <medRxiv / bioRxiv / journal DOI>
- Lab page / cohort dashboard: <URL>
- Recording (post-meeting): <ESHG virtual platform link or YouTube>
- Trade-press recap: <GenomeWeb / Bio-IT URL>
```

## Master talk index

The shortlist below is for **stub creation only** — most entries are `*expected per Programme-at-a-Glance + speaker list*` and will be reconciled with the EJHG abstract supplement when released. Stubs prioritize the **cancer-genomics-relevant subset** of the programme (hereditary cancer, cancer-PRS, somatic mosaicism, clonal hematopoiesis, large-cohort pan-cancer readouts, pharmacogenomics in oncology) plus the **load-bearing award lectures + cohort plenaries** that we'd want to cite from cancer-talks downstream.

| Talk | Speaker (expected) | Affiliation | Day / Session | Track | Anchor type | European cohort tag | Cancer-genomics relevance |
|---|---|---|---|---|---|---|---|
| **Opening Plenary (PL1)** | *TBA* | *TBA* | Sat Jun 13 / PL1 14:00 | Society | award lecture | N/A | Variable — depends on opening speakers |
| **Mendel Lecture** | *TBA* | *TBA (international keynote)* | Plenary (PL2–PL6) | Award | award lecture | N/A | Variable — Mendel often goes to landmark genetics investigators |
| **ESHG Award Lecture** | *TBA* | *TBA (European mid-career to senior)* | Plenary (PL2–PL6) | Award | award lecture | N/A | Variable |
| **ELPAG Award Lecture** | *TBA* | *TBA (Ethics / Public Policy)* | Plenary (PL2–PL6) | ELSI | award lecture | N/A | Indirect — clinical-implementation ethics |
| **Young Investigator Awards** | *TBA (winners announced ~April)* | Multiple | Plenary slots | Trainee plenary | mixed | Variable | Variable but often high-signal |
| **FinnGen R13 update** | *FinnGen leadership / scientific team* | Univ. of Helsinki / FinnGen | TBD (likely S-track) | Cohort / GWAS | study / cohort / readout | FinnGen R13 | High — cancer-PRS, Finnish hereditary-cancer prevalence, drug-target validation |
| **UK Biobank WGS + proteomics cancer overlay** | *UKB scientific team* | UK Biobank | TBD (likely S-track) | Cohort / GWAS | study / cohort / readout | UK Biobank | High — cancer-PRS, hereditary-cancer prevalence, multi-omics integration |
| **Generation R cancer-genomics arm** | *Generation R PIs* | Erasmus MC, Rotterdam | TBD | Cohort | study / cohort | Generation R | Indirect — pediatric / early-life cohort |
| **GeneRISK polygenic-risk pilot update** | *Perola / Widén / Ripatti* | FIMM / Univ. of Helsinki | TBD (likely S Polygenic Scores) | Statistical Genetics | methods paper | GeneRISK / FinnGen | High — first-in-class polygenic-risk return-of-results to patients, including cancer-PRS |
| **Estonian Biobank cancer module** | *Mägi / Metspalu group* | Univ. of Tartu / EstBB | TBD | Cohort | study / cohort | Estonian Biobank | Medium — pan-cancer germline-somatic on national cohort |
| **deCODE pan-cancer germline update** | *Stefansson / deCODE team* | deCODE genetics | TBD | Cohort | study / cohort | deCODE | High — large-effect cancer-predisposition variants |
| **Cancer Mechanisms symposium (S-track)** | *multiple* | Multiple | TBD | Cancer Genetics | mixed | Multiple | Core — mechanistic cancer-genetics |
| **Rare Cancers symposium (S-track)** | *multiple* | Multiple | TBD | Cancer Genetics | study / cohort | Multiple | Core — rare cancer genetics overlap with AACR rare-cancer sessions |
| **Polygenic Scores symposium (S-track)** | *multiple* (Mavaddat / Pharoah / Wray / Khera-aligned EU labs) | Multiple | TBD | Statistical Genetics | methods paper | UKB / FinnGen / GBMI | Core — cancer-PRS trial-stratification relevance |
| **Extrachromosomal DNA (ecDNA) Educational (E-track)** | *Mischel / Verhaak / European collaborators* | Multiple | TBD (E-track) | Cancer Genetics | methods paper | N/A | Core — ecDNA crossing from AACR / ASHG into ESHG education programme |
| **Episignatures Interactive (I-track)** | *Sadikovic / European episignature labs* | LHSC London ON / European partners | TBD (I-track) | Clinical / Methylation | tool / pipeline | N/A | Medium — methylation-based tumor classification overlap |
| **Pharmacogenomics Interactive (I-track)** | *Swen / van der Wouden (Ubiquitous-PGx) / Karolinska* | LUMC / Karolinska | TBD (I-track) | Pharmacogenomics | study / cohort | Ubiquitous-PGx / Nordic registries | Medium — DPYD/UGT1A1/TPMT/CYP2D6 oncology-drug dosing |
| **Long-read sequencing Educational (E-track)** | *European clinical adopters (PacBio / ONT)* | Multiple | TBD (E-track) | Clinical / Diagnostics | tool / pipeline | N/A | Medium — clinical WGS programs using HiFi / ONT, AGBT crossover |
| **AI in Functional Genomics Educational (E-track)** | *DeepMind / EvolutionaryScale / European AI-genomics labs* | Multiple | TBD (E-track) | Computational / ML | methods paper | N/A | Core — foundation-model variant predictors used in AACR variant-classification |
| **ELSI in AI Genomics Educational (E-track)** | *multiple (EU AI Act framing)* | Multiple | TBD (E-track) | ELSI | discussion | N/A | Indirect — EU AI Act clinical deployment of cancer-AI |
| **Hereditary breast / ovarian cancer panel-design (S/C track)** | *Mavaddat / Pharoah / GC-HBOC / HEBON / SweBCG* | Multiple | TBD | Cancer Genetics | study / cohort | GC-HBOC / HEBON / SweBCG / CanRisk | Core — pan-European panel harmonization |
| **Lynch syndrome / colorectal cancer (S/C track)** | *Mecklin / European Lynch Consortium* | Multiple | TBD | Cancer Genetics | study / cohort | InSiGHT / European registries | Core |
| **Clonal hematopoiesis at European population scale (S/C track)** | *multiple (UKB / FinnGen CHIP-aligned)* | Multiple | TBD | Statistical Genetics / Cancer Genetics | study / cohort | UKB / FinnGen | Core — bridge to EHA 2026 (same week!) and ASH 2026 |
| **Gene Editing symposium (S-track)** | *multiple (CRISPR therapeutics + base editing)* | Multiple | TBD | Therapy | tool / pipeline | N/A | Indirect — gene-edited oncology cell therapies overlap |
| **Repeat Expansions symposium (S-track)** | *multiple* | Multiple | TBD | Mendelian | methods paper | N/A | Indirect — methods bleed into cancer microsatellite-instability work |
| **Chromosome X Genetics symposium (S-track)** | *multiple* | Multiple | TBD | Population Genetics | methods paper | N/A | Indirect |

**Additional shortlist candidates** to stub post-supplement-release:

- **Cohort updates:** GBMI (Global Biobank Meta-analysis Initiative) cancer cross-biobank; Million Veteran Program European-equivalent partners; H3Africa cancer-genomics arm presentations at ESHG; Genomics England 100k follow-on / NHS GMS readouts; All of Us European-collaboration arm if presented.
- **Methods / tools:** DeepVariant / GLnexus EU clinical deployments; CADD v2; PRS-CSx / SBayesRC cross-ancestry methods; mosaic-variant callers; pangenome / HPRC + European pangenome-reference clinical applications; AlphaMissense follow-ons; ESM / EVO genomic foundation models.
- **Pre-conference courses to flag:** Clinical NGS Data Interpretation Course (Jun 11–12) — content overlap with cancer somatic / germline variant interpretation.
- **Dysmorphology sessions (I-track, two parallel):** ESHG signature format — face-recognition AI + variant-prioritization tools (Face2Gene / DeepGestalt successors); indirect cancer relevance through cancer-predisposition syndromes.

## Cross-cutting themes (for `themes.md`, deferred until post-meeting)

To synthesize across `talks/` once populated:

1. **FinnGen R13 + UK Biobank cancer-PRS convergence.** Two of the largest European cohorts with cancer modules co-presenting — readouts from both anchor the trial-stratification feasibility story carried forward to ASCO 2027.
2. **Pan-European hereditary-cancer panel harmonization.** GC-HBOC + HEBON + SweBCG + CanRisk + French / Italian registries — variant-classification standardization across single-payer systems.
3. **ecDNA crosses into ESHG.** A topic that has lived primarily at AACR / ASHG arrives in the ESHG educational track, signaling broader clinical-genetics awareness of focal-amplification biology.
4. **EU AI Act overlay on foundation-model variant predictors.** AlphaMissense follow-ons + ESM/EVO genomic models meet European clinical-deployment regulation — first major meeting where this overlay is explicit.
5. **Pharmacogenomics-guided oncology dosing in Nordic + Dutch systems.** Ubiquitous-PGx + Nordic PGx registries provide outcomes data on DPYD, UGT1A1, TPMT, CYP2D6 in oncology — bridge from ESHG into ASCO 2026 supportive-care sessions.
6. **CHIP at European population scale.** UKB + FinnGen CHIP overlays bridge to EHA 2026 (same week, Stockholm) clonal-hematopoiesis-to-MN risk sessions, and into ASH 2026 / SABCS 2026 (anthracycline-CHIP downstream).
7. **GeneRISK polygenic-risk return-of-results.** First multi-year cohort of return-of-PRS-to-patients including cancer-PRS — behavior change + clinical-pathway data.
