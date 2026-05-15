# Talks — ASHG 2026

The primary artifact of this vault: **one Markdown file per talk**. ASHG 2026 is a hybrid meeting — some talks are tool / pipeline / package debuts, others are clinical-genetics / cohort readouts, others are pure-methods papers. The per-talk schema accommodates all three with one Anchor field.

> **Status:** Template + master index. Per-talk pages will be populated once the program-at-a-glance is public (typically early-September 2026) and the AJHG abstract supplement lands (~September 2026). Pre-meeting stubs flagged `*expected, program not yet public*` are sourced from ASHG 2025 program shape, lab websites, and cohort-consortium dashboards (All of Us, UK Biobank, gnomAD); titles and assignments will be reconciled with the official program.

## Per-talk template

Each talk file (e.g., `allan-award-2026.md`, `aou-cancer-prs.md`, `gnomad-v5.md`) follows this schema. Copy and fill:

```markdown
# <Talk title — short>

> **Session:** <session name, date, time ET, room> · **Track:** <track / theme> · **Abstract:** <AJHG / abstract #, if assigned>

## At a glance

- **Speaker:** <name, degrees>
- **Affiliation:** <institution, department, lab>
- **Day / session / track:** <Tue Oct 20 / Plenary 1 / Statistical Genetics>
- **Talk title:** <full title as in program>
- **Anchor type:** <tool / package / pipeline | study / cohort / readout | methods paper | award lecture>
- **Anchor:** <package name + Bioconductor/CRAN/PyPI link | study acronym + NCT or cohort | manuscript citation + DOI>
- **Co-authors / consortium:** <if applicable — e.g., All of Us, UK Biobank, GREGoR, gnomAD>
- **Preprint / paper:** <bioRxiv / medRxiv / Nature Genetics / AJHG / HGGA DOI, if accompanying>

## Key result

<One paragraph. Numbers + cohort size + effect size if known. If pre-program, mark
`*expected per <lab page / cohort dashboard / prior-year talk>*` or
`*pre-program speculation*`.>

## Methods / approach

<2–4 sentences. What cohort, what assay, what statistical / computational method,
what comparator. For tool talks: what it consumes / produces, key
methodological idea, language / framework.>

## Why it matters for the corpus

<1–2 sentences. The cancer-genomics relevance specifically — does it inform
hereditary-cancer panel design, cancer-PRS stratification, somatic-mosaicism
detection, or methods used in AACR / ASCO / ASH talks?>

## Cross-links to corpus

- **AACR 2026:** <related session / poster, if applicable>
- **ASCO 2026:** <trial that uses the method / cohort / panel>
- **ASH 2026:** <CHIP / MN-predisposition tie-in>
- **ISMB 2026 / RECOMB 2026:** <methods-paper sibling talk>
- **AGBT 2026:** <upstream platform if this talk applies a new sequencing modality>
- **EuroBioC 2025 tools:** <Bioconductor package used / extended>
- **Other ASHG 2026 talks:** <session-mates, same-cohort, same-method>

## Sources

- AJHG abstract: <DOI / URL or "pending program release">
- Preprint / paper: <bioRxiv / medRxiv / journal DOI>
- Lab page / cohort dashboard: <URL>
- Recording (post-meeting): <ASHG virtual link or YouTube>
- Trade-press recap: <GenomeWeb / Bio-IT URL>
```

## Master talk index

The shortlist below is for **stub creation only** — all entries are `*expected, program not yet public*` and will be reconciled with the official ASHG 2026 program when released. Stubs prioritize the **cancer-genomics-relevant subset** of the program (hereditary cancer, cancer-PRS, somatic mosaicism, clonal hematopoiesis, large-cohort pan-cancer readouts) plus the **load-bearing methods / platform talks** that we'd want to cite from cancer-talks downstream.

| Talk | Speaker (expected) | Affiliation | Day | Track | Anchor type | Anchor (expected) | Cancer-genomics relevance |
|---|---|---|---|---|---|---|---|
| **William Allan Award Lecture** | *TBA* | *TBA* | Plenary (Wed Oct 21) | Award | award lecture | *career retrospective* | Variable — depends on awardee field |
| **Curt Stern Award Lecture** | *TBA* | *TBA* | Plenary (Thu Oct 22) | Award | award lecture | *landmark contribution* | Variable — Stern often goes to methods or rare-disease investigators with cancer-overlay relevance |
| **Mendel Lecture** | *TBA (international)* | *TBA* | Plenary (Fri Oct 23) | Award | award lecture | *international keynote* | Variable |
| **Presidential Address / Symposium** | Susan A. Slaugenhaupt | MGH / Harvard | Plenary (Tue Oct 20 evening) | Society | award lecture | *Communicating Science in an Uncertain World* | Indirect — public-trust framing |
| **All of Us Research Program update** | *AoU leadership / scientific team* | NIH / AoU consortium | TBD | Cohort plenary | study / cohort / readout | *AoU v8 release, expected cancer-cohort overlay* | High — pan-cancer germline-somatic on >800k participants expected |
| **UK Biobank WGS / proteomics update** | *UKB scientific team* | UK Biobank | TBD | Cohort plenary | study / cohort / readout | *500k WGS, expected cancer-PRS update* | High — cancer-PRS, hereditary-cancer prevalence |
| **gnomAD v5 release** | Konrad Karczewski or team | Broad Institute | TBD | Population genetics | tool / pipeline | *gnomAD v5 dataset + browser* | High — variant-classification backbone for hereditary cancer |
| **GREGoR Consortium update** | *GREGoR PIs* | NHGRI / GREGoR | TBD | Mendelian / rare | study / cohort / readout | *unsolved-rare-disease cohort* | Indirect — cancer-predisposition rare variants |
| **Cancer Genetics platform session** | *multiple* | Multiple | TBD | Cancer Genetics | mixed | *hereditary cancer panel updates* | Core track |
| **Hereditary cancer panel-design / VUS-resolution talks** | *multiple* | Multiple (incl. Color, Invitae successor labs, academic VUS programs) | TBD | Cancer Genetics | study / cohort | *ClinVar / VUS reclassification cohorts* | Core — panel-classification accuracy |
| **Clonal hematopoiesis (CHIP) population-scale talks** | *multiple* (Bick / Natarajan / Jaiswal-aligned labs) | Multiple | TBD | Cancer Genetics / Statistical Genetics | study / cohort | *CHIP prevalence + cancer-MN risk in UKB/AoU* | Core — bridge to ASH MDS/AML talks |
| **Cancer polygenic risk score (PRS) sessions** | *multiple* (Mavaddat / Pharoah / Khera-aligned labs) | Multiple | TBD | Statistical Genetics | methods paper | *breast / prostate / colorectal PRS cross-ancestry transferability* | Core — trial-stratification relevance |
| **Somatic mosaicism in non-cancer phenotypes** | *multiple* | Multiple | TBD | Mosaicism | methods paper | *somatic mosaicism callers + cohort applications* | Methods bleed into cancer ctDNA / clonal-evolution work |
| **Foundation-model variant-effect predictors** | *multiple* (DeepMind / EvolutionaryScale / Calico) | Multiple | TBD | Computational / ML | methods paper | *AlphaMissense follow-ons, ESM / EVO genomic models* | Methods used in AACR variant-classification talks |
| **Long-read clinical sequencing readouts** | *multiple* (PacBio / ONT clinical adopters) | Multiple | TBD | Clinical / Diagnostics | tool / pipeline | *clinical WGS programs using HiFi / ONT* | Methods bleed into AGBT 2026 platform talks |
| **Pan-cancer germline analysis (large cohort)** | *multiple* | Multiple | TBD | Cancer Genetics | study / cohort | *germline-pathogenic-variant prevalence across cancers* | Core — informs panel composition + universal-testing debates |
| **ELSI: AI ethics in genomics** | *multiple* | Multiple | TBD | ELSI | discussion | *responsible use of foundation models in clinical genomics* | Indirect — cancer-AI return-of-results overlap |
| **Trainee Research Excellence Award winners** | *Trainee awardees (announced ~July)* | Multiple | TBD | Trainee plenary | mixed | *to be announced* | Variable but often high-signal |

**Additional shortlist candidates** to stub post-program-release:

- **Cohort updates:** MVP (Million Veteran Program) cancer-genomics module; FinnGen R12/R13; GBMI cross-biobank meta-analyses; H3Africa cancer-genomics arm; GenomeAsia 100K cancer-PRS transferability.
- **Methods / tools:** DeepVariant / GLnexus updates; CADD v2; PRS-CSx / SBayesRC cross-ancestry methods; mosaic-variant callers (MosaicHunter, deepMosaic); pangenome / HPRC clinical applications.
- **Pre-meeting workshops to flag:** statistical-genetics primers; clinical-sequencing pipelines; PRS construction hands-on; foundation-models-for-genomics tutorials.

## Cross-cutting themes (for `themes.md`, deferred until post-meeting)

To synthesize across `talks/` once populated:

1. **Cancer-PRS clinical utility moment.** Cross-ancestry PRS transferability + biobank-scale validation may finally cross the threshold for trial-stratification adoption. Cross-link to AACR 2026 PRS sessions and ASCO 2026 breast / prostate biomarker-eligible trials.
2. **gnomAD v5 + ClinVar baseline.** New population reference may re-classify a meaningful fraction of variants in hereditary-cancer panels. Cross-link to AACR 2026 variant-classification posters.
3. **Long-read clinical sequencing inflection.** PacBio HiFi + ONT R10 quality at clinical scale — cross-link to AGBT 2026 platform talks.
4. **Foundation models for variant effect.** AlphaMissense follow-ons + protein-language-model + DNA-LM successors. Cross-link to AACR 2026 ML-bio sessions and ISMB 2026.
5. **Somatic mosaicism beyond cancer.** Methods sharing with cancer-ctDNA / clonal-evolution methodology.
6. **CHIP / CCUS at population scale.** Bridge to ASH 2026 MDS / AML clinical talks.
7. **AoU + UK Biobank coordinated cancer readouts.** Two cohorts both with ~mature cancer-genomics modules; pan-cancer germline-somatic at population scale is now feasible.
