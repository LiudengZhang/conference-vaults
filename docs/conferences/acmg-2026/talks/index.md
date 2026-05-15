# Talks — ACMG 2026

The primary artifact of this vault: **one Markdown file per talk**. ACMG 2026 is a hybrid clinical-lab meeting — some talks are clinical case readouts, some are cohort / cohort-classification readouts, some are standards-document updates (ACMG/AMP, ClinGen VCEPs), some are AI/ML methods talks, some are TED-style perspectives, and the named-award lectures are their own slot type. The per-talk schema accommodates all of these with one Anchor field.

> **Status:** Template + master index, populated retrospectively. Stubs are pulled from the ACMG 2026 meeting site, pre-meeting press release, and the ACMG Foundation award announcement; entries tagged `*per pre-meeting press, GIM abstract supplement pending*` will be reconciled with DOIs and full abstract text once the *Genetics in Medicine* abstract supplement publishes (typically ~April–May post-meeting) and the ACMG Digital Edition on-demand recordings are accessible (~April–May 2026, partially live now).

## Per-talk template

Each talk file (e.g., `rimoin-2026-carey.md`, `nifs-symposium.md`, `llm-acmg-amp-classification.md`) follows this schema. Copy and fill:

```markdown
# <Talk title — short>

> **Session:** <session name, date, time ET, room> · **Track:** <track / theme> · **Abstract:** <GIM abstract # or platform/poster #>

## At a glance

- **Speaker:** <name, degrees (MD, PhD, MS, FACMG, CGC, etc.)>
- **Affiliation:** <institution, department, clinical lab>
- **Day / session / track:** <Wed Mar 11 / Platform 1 / Hereditary Cancer and Adult Genetics>
- **Talk title:** <full title as in program>
- **Anchor type:** <clinical-lab cohort / case readout | standards / guideline update | tool / pipeline / ML method | award lecture | TED-style / perspective | symposium discussion>
- **Anchor:** <cohort name + size + lab | guideline document + version + GIM DOI | tool name + GitHub/PyPI | manuscript citation + DOI>
- **Co-authors / consortium:** <if applicable — e.g., ClinGen VCEP, UDN, AoU, CSER, eMERGE>
- **Preprint / paper:** <bioRxiv / medRxiv / GIM / GIM Open / NEJM / AJHG DOI, if accompanying>

## Key result

<One paragraph. Numbers + cohort size + diagnostic yield / classification-change rate / effect
size if known. For retrospective stubs, mark `*per pre-meeting press`*` or
`*per session description, GIM abstract supplement pending*` if not yet reconciled.>

## Methods / approach

<2–4 sentences. What clinical cohort, what assay, what classification framework
(ACMG/AMP 2015 + which evidence-code recalibrations), what comparator. For tool
talks: what it consumes / produces, key methodological idea, integration with
lab LIMS / variant-curation workflow. For standards-update talks: scope, what
changed vs prior version, implementation timeline.>

## Why it matters for the corpus

<1–2 sentences. The cancer-genomics / clinical-trials / methods relevance specifically
— does it inform hereditary-cancer panel design, ACMG/AMP variant classification
for cancer variants, CHIP / mosaicism detection in cancer testing, AI / LLM
validation in clinical labs, or methods used in AACR / ASCO / ASH downstream?>

## Cross-links to corpus

- **AACR 2026:** <related session / poster, if applicable>
- **ASCO 2026:** <trial that uses the testing framework / cohort / panel>
- **ASH 2026:** <CHIP / MN-predisposition / germline-MN tie-in>
- **ASHG 2026:** <methods-paper sibling talk later in the year>
- **ISMB 2026 / RECOMB 2026:** <upstream variant-effect-predictor or LLM methods talk>
- **AGBT 2026:** <upstream platform if this talk applies a new sequencing modality>
- **ESHG 2026:** <European sibling talk if same investigator / cohort>
- **Other ACMG 2026 talks:** <session-mates, same-cohort, same-method>

## Sources

- GIM abstract: <DOI / URL or "pending supplement publication">
- Preprint / paper: <bioRxiv / medRxiv / journal DOI>
- Lab / institutional page: <URL>
- Recording (post-meeting): <ACMG Digital Edition URL>
- Trade-press recap: <GenomeWeb / 360Dx URL>
- Sponsor release (if applicable): <vendor press URL>
```

## Master talk index

The shortlist below is pulled **retrospectively** from the ACMG 2026 meeting site and pre-meeting press. Stubs prioritize the **cancer-genetics-relevant subset** of the program (hereditary cancer, ACMG Secondary Findings cancer subset, CHIP / mosaicism in cancer testing, germline-somatic integration) plus the **load-bearing standards / AI-in-clinical-genomics talks** that we'd want to cite from cancer-talks downstream. Reconciliation with the GIM abstract supplement is pending.

| Talk | Speaker | Affiliation | Day | Track | Anchor type | Anchor | Cancer-genomics relevance |
|---|---|---|---|---|---|---|---|
| **David L. Rimoin Lifetime Achievement Award Lecture** | John C. Carey, MD, MPH, FACMG, FAAP | University of Utah (Emeritus) | Wed Mar 11 — Presidential Plenary | Award | award lecture | *career retrospective in clinical genetics, dysmorphology, trisomy 13/18 advocacy* | Indirect — clinical-genetics framing of cancer-predisposition syndromes |
| **Presidential Plenary: The Future of Expanded Newborn Genomic Screening** | *Presidential Plenary panel* | Multiple | Wed Mar 11 — Presidential Plenary | Society / Plenary | symposium discussion | *NBS expansion to genomic sequencing — BabySeq, GUARDIAN, NBSeq, EarlyCheck* | Core — pediatric cancer-predisposition reporting from newborn WGS is the cancer-relevant axis |
| **Non-Invasive Fetal Sequencing (NIFS) Is Coming: Are You Ready?** | *symposium panel* | Multiple (incl. Natera, Illumina, academic prenatal centers) | TBD | Prenatal / Reproductive | symposium discussion | *NIFS clinical-readiness debate* | Indirect — fetal cancer-predisposition variant detection is a downstream question |
| **Clonal Hematopoiesis, Somatic and Post-Zygotic Mosaicism in Multigene Cancer Testing for Geneticists** | *symposium panel* | Multiple (incl. Bick-aligned, Natarajan-aligned, clinical-lab CHIP working groups) | TBD | Cancer Genetics | symposium discussion | *CHIP / mosaicism findings in multigene panel testing — incidental finding handling* | Core — clinical-lab translation of population-CHIP work; bridge to ASH MDS/AML |
| **Beyond The List — Scope and Implementation of ACMG Secondary Findings** | *ACMG SF Working Group* | ACMG SF WG | TBD | Standards / Policy | standards / guideline update | *ACMG SF v3.3 implementation + future expansion debate* | Core — cancer-predisposition genes dominate the SF list (TP53, BRCA1/2, MLH1, MSH2, MSH6, PMS2, APC, MUTYH, PTEN, RB1, RET, VHL, WT1) |
| **Demystifying Base Large Language Model Reproducibility and Accuracy in ACMG/AMP Variant Classification** | *platform speaker, TBC from program* | TBD | TBD | AI / Informatics | tool / pipeline / ML method | *LLM benchmark for ACMG/AMP classification reproducibility* | Core — every cancer-variant classification rests on ACMG/AMP framework; LLM-validation is the gating question for clinical-lab adoption |
| **Platform 1 — Hereditary Cancer and Adult Genetics** | *multiple platform speakers* | Multiple | TBD | Cancer Genetics | mixed (clinical-lab cohort + classification + outcomes) | *hereditary-cancer panel updates, VUS reclassification, universal-testing implementations* | Core — primary cancer-genetics platform session |
| **AI-assisted genome interpretation and networked data sharing** | *platform speaker, TBC* | TBD | TBD | AI / Informatics | tool / pipeline / ML method | *AI-assisted clinical-lab genome interpretation pipeline* | Methods used in clinical cancer-variant interpretation downstream |
| **Diagnostic challenges from the Undiagnosed Diseases Network** | *UDN clinical sites* | UDN / NHGRI | TBD | Rare Disease | clinical-lab cohort / case readout | *UDN diagnostic-yield updates + complex-case readouts* | Indirect — UDN cancer-predisposition cases inform pan-cancer germline panel design |
| **Genomic Oncology track** | *multiple* | Multiple | TBD | Cancer Genetics | mixed | *germline-somatic integration, pharmacogenomics in oncology, tumor-only vs paired testing* | Core — cancer-genomics overlap with AACR / ASCO |
| **Gene Therapy implementation (clinical-lab perspective)** | *multiple* | Multiple (incl. gene-therapy clinical sites) | TBD | Therapeutics | symposium discussion | *clinical-lab role in AAV / CRISPR / ASO gene-therapy patient selection + monitoring* | Indirect — RB1 / TP53 gene-therapy and cancer-predisposition crossovers |
| **Washington policy: payer / FDA / LDT implications** | *policy panel* | ACMG advocacy + payer / FDA reps | TBD | Health Services / Policy | symposium discussion | *FDA LDT final rule, CMS coverage, prior-auth for clinical genetics* | Indirect — same regulatory framework gates somatic cancer-LDT operations |
| **ClinGen VCEP updates (cancer-predisposition expert panels)** | *ClinGen Cancer VCEPs* | ClinGen | TBD | Standards / Curation | standards / guideline update | *ClinGen Hereditary Cancer / TP53 / Lynch / BRCA VCEP curation updates* | Core — every clinical-lab cancer-variant classification consults ClinGen VCEP decisions |
| **Cardiovascular genetics — cardiomyopathy / arrhythmia panel updates** | *multiple* | Multiple (incl. Mayo, Stanford, MGB) | TBD | Cardiovascular Genetics | clinical-lab cohort / case readout | *HCM / DCM / LQTS panel-design updates, ClinGen Cardio VCEP* | Indirect — non-cancer, but methods overlap |
| **Long-read clinical sequencing case readouts** | *multiple* (PacBio / ONT clinical adopters) | Multiple | TBD | Clinical / Diagnostics | tool / pipeline | *clinical WGS programs using HiFi / ONT for structural-variant + repeat-expansion resolution* | Methods bleed into AGBT 2026 platform talks and AACR / ASHG cancer-SV detection |
| **RNA-seq for variant interpretation** | *multiple* | Multiple (incl. clinical-RNA programs) | TBD | Clinical / Diagnostics | tool / pipeline | *RNA-seq for splice-variant / RNA-level evidence in ACMG/AMP PVS1 / PS3* | Core methods — clinical-lab cancer-splice-variant interpretation |
| **TED-style talks (perspective slot)** | *multiple* | Multiple | TBD | Plenary perspective | TED-style / perspective | *5–10 minute big-idea talks on field-shaping topics* | Variable — past TED-style talks have included AI ethics, equity, return of results |
| **Trainee Awards platform session (Richard King Awards)** | *Trainee awardees* | Multiple | TBD | Trainee plenary | award lecture | *winning trainee abstracts across categories* | Variable but often high-signal |

**Additional shortlist candidates** to stub from the Digital Edition on-demand catalog:

- **Prenatal / NBS:** GUARDIAN study readout; BabySeq2 update; cfDNA expansion to monogenic disorders; expanded carrier-screening panel composition.
- **Cancer genetics:** universal Lynch / HBOC testing implementation studies; CHARM / MAGENTA / WISDOM-style population-screening cohorts; germline reanalysis cohorts; pediatric-cancer-predisposition referral pathways.
- **AI / Informatics:** AlphaMissense in clinical workflows; ESM-3 / EVO benchmark on clinical variants; LLM-drafted reports + clinician oversight; ML-assisted curation queues.
- **Therapeutics:** Casgevy (exa-cel) / Lyfgenia post-launch clinical-lab perspective; n-of-1 antisense oligonucleotide programs (n-Lorem, Stoke); AAV redosing / immunogenicity from a genetics-clinic perspective.
- **ELSI / equity:** ancestry / population-database representation in classification; return of results in pediatrics; secondary-findings in prenatal contexts.
- **Pre-meeting Short Courses to flag:** clinical laboratory genetics primer; cancer genetics for the practicing clinician; coding / reimbursement; long-read clinical implementation.

## Cross-cutting themes (for `themes.md`, deferred until post-meeting digest completes)

To synthesize across `talks/` once populated:

1. **LLM / foundation-model entry into ACMG/AMP variant classification.** The Demystifying-LLM-Reproducibility platform plus AI-assisted genome interpretation talks suggest 2026 is the validation year for clinical-lab LLM workflows. Cross-link to ISMB 2026 / RECOMB 2026 methods papers and ASHG 2026 foundation-model-variant-effect-predictor talks.
2. **Newborn-genomic-screening expansion: the cancer-predisposition wedge.** Presidential Plenary theme. Reporting cancer-predisposition variants (RB1, TP53, RET, APC, BRCA, Lynch) from newborn WGS sits at the policy-debate edge. Cross-link to AACR 2026 hereditary-cancer / pediatric-cancer-predisposition sessions.
3. **ACMG Secondary Findings list growth + scope debate.** *Beyond The List* session. Cancer-genes dominate; pediatric-onset cancer-predisposition reporting is the load-bearing question.
4. **CHIP / somatic mosaicism in clinical cancer testing.** Clinical-lab framing of the population-CHIP body of work. Bridge to ASH 2026 MDS/AML and ASHG 2026 statistical-genetics CHIP talks.
5. **NIFS clinical readiness.** Non-invasive fetal sequencing as the next-generation prenatal modality beyond NIPT — clinical-lab-validation and ELSI questions both live here.
6. **UDN diagnostic-yield maturation + complex-case framing.** The diagnostic-odyssey case-based session — clinical-lab and clinician collaboration patterns that scale.
7. **Long-read clinical sequencing inflection.** Same theme as ASHG 2026 + AGBT 2026, with clinical-lab implementation framing (LIMS integration, variant calling, reporting).
8. **Cancer pharmacogenomics + germline-somatic integration.** Bridge between clinical-lab cancer testing and AACR / ASCO trial eligibility.
