# Talks — AACR Pancreatic Cancer 2026

The primary artifact of this vault: **one Markdown file per talk**, hybrid-anchored. AACR Pancreatic 2026 is a mixed clinical-readout + basic-biology + translational meeting, so a single anchor type does not fit — each talk resolves to **trial** (clinical readout / interventional study), **tool** (model system / platform / assay), or **study** (mechanism paper / dataset / hypothesis-generating cohort).

> **Status:** Template + master index. Per-talk pages will be populated as the AACR Pancreatic 2026 program is released (August–September 2026) and abstracts publish (~2 weeks pre-meeting). Pre-meeting stubs flagged `*expected, subject to embargo*` are sourced from prior-year AACR Pancreatic programs, AACR 2026 Annual pancreatic-track content, sponsor pipeline guidance (JPM 2026, Q1 2026 earnings), and ASCO 2026 preview material. Talk titles, session assignments, and named-lecture lineups are speculative until program release.

## Per-talk template (hybrid)

Each talk file (e.g., `daraxonrasib-rascolt-1.md`, `tuveson-organoid-platform.md`, `mcallister-microbiome-prevention.md`) follows one of three anchored schemas depending on what the talk is centered on. The shared header is uniform; the body block differs.

### Shared header (all anchor types)

```markdown
# <Talk title> — <one-line framing>

> **Anchor:** trial | tool | study · **Session:** <session name, date, time PT, room> · **Embargo:** <date>

## At a glance

- **Speaker / presenter:** <name, institution>
- **Senior author / lab:** <name, institution> (if different)
- **Talk type:** keynote / plenary / major-symposium invited / mini-symposium proffered / poster spotlight
- **Co-authors highlighted:** <if cross-institution collaboration is the story>
```

### Body — trial anchor (clinical readout / interventional)

For talks centered on a clinical trial or interventional study. Use when the headline is a Phase 1/2/3 readout.

```markdown
## Trial

- **Trial name / acronym:** <e.g., RASolute-302, IMcode-004>
- **NCT ID:** <NCTxxxxxxxx>
- **Sponsor:** <pharma / cooperative group / academic IIT>
- **Phase:** <1 / 1b/2 / 2 / 2/3 / 3>
- **Design:** <arms, randomization, blinding, biomarker selection>
- **N:** <enrolled / analyzed at this readout>
- **Primary endpoint(s):** <ORR / PFS / OS / RFS / DLT / pharmacodynamic>
- **Comparator:** <SOC / placebo / single-arm>
- **Population:** <line of therapy; KRAS-mut subset; resectable vs metastatic; biomarker-selected>

## Headline result

<One paragraph. Numbers + HR + p-value if known. If pre-embargo, mark
`*expected per <company> topline <date>*` or `*pre-embargo per <analyst source>*`.>

## Mechanism / class

<Drug class, target. Cross-link to AACR Annual mechanism sessions or prior AACR Pancreatic readouts.>

## Practice-changing?

<Yes / no / pending, with rationale: FDA filing path, NCCN PDAC guideline implications, unmet need.>
```

### Body — tool anchor (model system / platform / assay)

For talks introducing or updating a research tool — organoid platform, GEMM, spatial assay, computational pipeline, biomarker assay.

```markdown
## Tool

- **Tool name:** <e.g., PancOrg-Plus, KPCY mouse cohort, MS-PSP assay>
- **Type:** organoid platform / GEMM / PDX / spatial assay / sequencing pipeline / liquid biopsy / imaging
- **Status at AACR Pancreatic 2026:** new release / major update / methods talk / case study
- **Open / closed:** open-source / restricted / commercial
- **Repository / accession:** <GitHub / Bioconductor / GEO / dbGaP / Synapse link>
- **Reference publication:** <DOI; preprint or peer-reviewed>

## What it does

<2–3 sentences: the problem it solves, key methodological idea, what it consumes / produces.
What's new since the last AACR Pancreatic / AACR Annual presentation.>

## Where it fits in the corpus

- AACR 2026 Annual: <link if mentioned>
- Prior AACR Pancreatic (2022/2024/2025): <link if mentioned>
- ASCO / ASCO GI: <link>
- SITC / ESMO: <link>

## Notes

<Free-form: benchmarks claimed, comparisons to alternatives, validation cohorts.>
```

### Body — study anchor (mechanism / dataset / hypothesis)

For talks centered on a mechanism paper, dataset reveal, or hypothesis-generating cohort study without a single trial or tool as the unit.

```markdown
## Study

- **Type:** mechanism / dataset / cohort / functional genomics screen / computational analysis
- **System(s):** <human cohort / GEMM / organoid / cell line / PDX / multi-modal>
- **N (samples / mice / patients):** <…>
- **Key dataset(s):** <accession + brief description>
- **Reference publication / preprint:** <DOI>

## Key finding

<One paragraph. The headline biological / clinical insight.>

## Mechanism / model

<2–3 sentences: the pathway / cell-state / interaction posited.>

## Translational implication

<Would this nominate a target, a patient-selection biomarker, a new model system,
or a clinical-trial design? What's the next step?>

## Cross-links

- AACR 2026 Annual: <link if presented in preview form>
- Prior AACR Pancreatic: <link>
- Related trials in this vault: <links to trial-anchored talks downstream>
```

### Shared footer (all anchor types)

```markdown
## Sources

- AACR abstract / *Cancer Research* proceedings: <DOI or "pending day of presentation">
- Company press release (if applicable): <URL>
- Trade-press recap: <OncLive / Let's Win / PanCAN / ASCO Post / STAT URL>
- Preprint / peer-reviewed paper (if applicable): <DOI>
- ClinicalTrials.gov (if trial-anchored): <NCT URL>
```

## Master talk index

Shortlist for pre-meeting stub creation. All entries are **anticipated** — sourced from prior-year AACR Pancreatic slots, the 2024 / 2025 program patterns, AACR 2026 Annual pancreatic-track content, sponsor pipeline guidance, and ASCO 2026 preview material. **Session assignments are unknown until program release (August 2026); all numbers are speculative until then.** Italicized entries are pre-embargo / topline-only.

### Trial-anchored (clinical / interventional readouts)

| Talk | Anchor | Sponsor / lead | Population / line | Phase | Endpoint | Expected status |
|---|---|---|---|---|---|---|
| **RASolute-302** | trial | Revolution Medicines | 2L+ KRAS-mut metastatic PDAC (daraxonrasib monotherapy / + chemo) | 3 | PFS / OS | *expected interim or supportive Phase 2 maturation; pivotal Phase 3 likely ESMO/ASCO GI* |
| **Daraxonrasib + chemo Ph1b/2 expansion** | trial | Revolution Medicines | 1L metastatic PDAC (daraxonrasib + mFOLFIRINOX or gem/nab-paclitaxel) | 1b/2 | ORR / DLT / PFS | *expected; ASCO 2025 / AACR 2026 Annual lineage* |
| **Zoldonrasib (RMC-9805) Ph1 PDAC** | trial | Revolution Medicines | KRAS-G12D metastatic PDAC; mono and combo | 1 | DLT / ORR / PK-PD | *expected first-in-human PDAC-specific update* |
| **RMC-6291 (G12C(ON)) PDAC subset** | trial | Revolution Medicines | KRAS-G12C metastatic PDAC | 1/2 | ORR | *expected subset readout* |
| **MRTX1133 / next-gen Mirati G12D** | trial | BMS (Mirati) | KRAS-G12D metastatic PDAC | 1 | DLT / ORR | *expected program update post-clinical-pause history* |
| **Astellas / Boundless pan-RAS Ph1** | trial | Astellas / Boundless Bio | KRAS-mut PDAC | 1 | DLT / PK | *expected if datacut available* |
| **BNT122 / autogene cevumeran follow-up** | trial | BioNTech / Genentech | Resected PDAC (adjuvant mRNA neoantigen vaccine + atezo + mFOLFIRINOX) | 2 | RFS / immunogenicity | *expected Phase 2 randomized update post-ASCO 2024 Phase 1 RFS signal* |
| **mRNA-4157 PDAC arm (if launched)** | trial | Moderna / Merck | Resected PDAC (mRNA individualized + pembro) | 2 | RFS / immunogenicity | *anticipated if PDAC arm reads; primary signal is melanoma KEYNOTE-942 lineage* |
| **AltCAP** | trial | Academic IIT | 1L metastatic PDAC (alternating NALIRIFOX / gem-nab) | 2 | PFS / tolerability | *expected mature data per AACR Pancreatic 2025 first reveal* |
| **CD40 agonist (sotigalimab) follow-up** | trial | Apexigen / cooperative | 1L metastatic PDAC + chemo + checkpoint | 1b/2 | ORR / OS / immune correlates | *expected if PRINCE / follow-up cohorts mature* |
| **KRAS-G12D TCR-T (NCI / Rosenberg lineage)** | trial | NCI / cooperative | HLA-C*08:02 KRAS-G12D-mut PDAC | 1 | safety / ORR / persistence | *expected per Tran/Rosenberg lineage; case-series scale* |
| **Claudin 18.2 ADC / CAR-T in PDAC** | trial | Multiple (AstraZeneca, Lilly, others) | CLDN18.2+ PDAC subset | 1/2 | ORR / DLT | *expected expansion talks; zolbetuximab class extending* |
| **PRECISION-Promise platform update** | trial | PanCAN-led adaptive platform | Metastatic PDAC | 2 platform | platform-level | *expected annual update* |
| **PRECISION-Panc update** | trial | UK adaptive platform | Metastatic / advanced PDAC | 2 platform | platform-level | *expected; cross-Atlantic counterpart to Precision Promise* |
| **BRCA / HRD-targeted PARP inhibitor maintenance** | trial | Multiple | gBRCA / HRD-positive metastatic PDAC | 2/3 | PFS / OS | *expected updates; POLO follow-on context* |

### Tool-anchored (models / platforms / assays)

| Talk | Anchor | Lead | Type | Status |
|---|---|---|---|---|
| **PDAC organoid biobank / Tuveson platform** | tool | Tuveson / Tiriac (CSHL) | organoid biobank | *expected major update; long-running franchise* |
| **HumanPancFun (or successor cohort)** | tool | Multi-institutional | living biobank / functional screen | *expected; AACR 2026 Annual lineage* |
| **KPC / KPCY GEMM cohorts** | tool | Stanger / Vonderheide / Olive lineage | GEMM platform | *expected drug-development applications* |
| **Spatial PDAC atlas** | tool | Multi-institutional | Visium / Xenium / CODEX / MERFISH atlas | *expected; AACR 2026 Annual spatial-omics overlap* |
| **PDAC single-cell atlas update** | tool | Multi-lab | scRNA / scATAC atlas | *expected* |
| **CA19-9 successor multi-analyte panel** | tool | Multiple (Wolpin / Hingorani / academic + industry) | serum / blood-based detection assay | *expected; early-detection major-symposium centerpiece* |
| **Microbiome (oral / stool) detection signature** | tool | McAllister (MD Anderson) and collaborators | microbiome assay | *expected; McAllister co-chair lineage* |
| **AI-CT / AI-MRI early-lesion detection** | tool | Multi-institutional + industry | imaging-AI pipeline | *expected; <2cm lesion miss-rate framing per AACR 2025* |
| **Pancreas-cyst risk-stratification assay** | tool | Multi-institutional | molecular cyst-fluid panel | *expected; interception strategy* |
| **Methylation-based MRD assay for PDAC** | tool | Industry (Guardant / Natera / GRAIL / Exact) | ctDNA-MRD assay | *expected* |

### Study-anchored (mechanism / cohort / dataset)

| Talk | Anchor | Lead | System | Status |
|---|---|---|---|---|
| **CAF heterogeneity update — iCAF / myCAF / apCAF resolution** | study | Tuveson / Öhlund / Olive lineage | scRNA + functional | *expected; field-defining franchise* |
| **Stromal mechanical tension and ECM remodeling** | study | Olive / Hingorani lineage | GEMM + imaging | *expected; co-chair Olive franchise* |
| **PDAC immune evasion — MHC-I downregulation, autophagy** | study | Perez-Mancera / Tuveson / Aguirre | functional genomics | *expected per AACR Annual 2026 lineage* |
| **Tumor-microbiome cross-talk** | study | McAllister / Riquelme lineage | microbiome + immune | *expected; co-chair franchise* |
| **Neoantigen landscape — KRAS-mut shared neoantigens, cryptic ORFs** | study | Freed-Pastor (DFCI) / Wu / Hacohen | proteogenomics + immunopeptidomics | *expected per AACR 2025 cryptic-antigen talks* |
| **Metabolic vulnerabilities — autophagy, glutamine, pyrimidine** | study | Kimmelman / Commisso / Cantley lineage | metabolomics + functional | *expected; established AACR Pancreatic franchise* |
| **PDAC heterogeneity — classical / basal-like subtypes, plasticity** | study | Bailey / Aguirre / Maitra | bulk + single-cell + spatial | *expected; subtype-and-plasticity update* |
| **Lineage tracing — PDAC origin, acinar-to-ductal metaplasia** | study | Stanger / Pasca di Magliano / Crawford | GEMM lineage tracing | *expected* |
| **PDAC functional genomics — CRISPR screens for combination targets** | study | Aguirre (co-chair) / Hahn / Boehm | DepMap / pooled CRISPR | *expected; AACR 2026 Annual lineage* |
| **High-risk surveillance cohorts — familial / new-onset diabetes** | study | Brand / Chari / Goggins lineage | clinical cohort | *expected; interception framing* |
| **Health disparities in PDAC** | study | Multi-institutional | epidemiology + biology | *expected; AACR Special Conference programmatic priority* |

### Late-breaker / wildcard slots

Reserve 3–5 slots for late-breaker abstracts (typically announced August 2026). High-probability fillers:

- Phase 2 RASolute or daraxonrasib combination interim with definitive numbers.
- BNT122 randomized Phase 2 RFS readout (if August toplines).
- A first-in-class KRAS-G12V or pan-KRAS(ON) selective Ph1 first-cohort.
- A claudin 18.2 PDAC-subset expansion (if zolbetuximab class data matures).

## Cross-cutting themes (for the program-notes synthesis)

To trace across `talks/` once populated:

1. **The KRAS-targeting class question.** Pan-RAS (daraxonrasib) vs allele-selective (zoldonrasib G12D, RMC-6291 G12C(ON), Mirati G12D) vs combination backbones (with chemo, with checkpoint, with SHP2 / mTORC1 / autophagy partners). The 2026 question: does pan-RAS Phase 3 win on raw efficacy, or does allele-selectivity win on tolerability for the chronic-dosing window?
2. **mRNA neoantigen vaccines — durability and generalizability.** Phase 1 BNT122 RFS signal needs Phase 2 randomized validation; the question is whether the result extends beyond a single-center Memorial Sloan Kettering / BioNTech / Genentech axis and into multi-site adjuvant SOC.
3. **Stroma — is it druggable yet, or is the answer still "model it better"?** A decade of stromal-targeting clinical failures (hedgehog, hyaluronidase, FAK) sit against a decade of refined biology (iCAF/myCAF/apCAF, mechanical tension, exosomal cross-talk). 2026's slate will likely lean basic with a few combo-trial signals.
4. **Early detection moving from biomarker discovery to interception.** CA19-9 successor assays + microbiome + AI imaging are converging — but high-risk cohort enrollment, screening-trial economics, and overdiagnosis questions are unresolved.
5. **PDX / organoid platforms maturing into co-clinical-trial infrastructure.** The Tuveson / Tiriac and successor organoid platforms have been "almost ready" for several AACR Pancreatic cycles; 2026 may be the year where one of them is the formal SOC arm of an adaptive trial.
