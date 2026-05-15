# Trials — EHA 2026

The primary artifact of this vault: **one Markdown file per trial / readout**. EHA 2026 is a clinical-readout meeting, so the unit of analysis is the trial — not the speaker, not the tool, not the company. Same per-trial schema as [ASH 2026](../../ash-2026/trials/index.md) and [ASCO 2026](../../asco-2026/trials/index.md); EHA adds an explicit **European cooperative-group** sub-axis (HOVON, GIMEMA, GELTAMO, GMLL, IFM, LYSA, NCRI) and an **EBMT registry** sub-axis on transplant / cellular therapy.

> **Status:** Template + master index. Per-trial pages will be populated in two waves: (1) regular abstracts upon *HemaSphere*-supplement release on **May 12, 2026, 15:30 CEST** (tomorrow); (2) Late-Breaking Abstracts on **June 2, 2026, 15:30 CEST**. Pre-meeting stubs flagged `*expected, subject to embargo*` are sourced from company toplines, ASCO 2026 heme subset (May 29 – Jun 2), and analyst preview pieces; numbers can shift on the actual abstract reveal.

## Per-trial template

Each trial file (e.g., `epcore-nhl-2-update.md`) follows this schema. Copy and fill:

```markdown
# <Trial acronym / name> — <Drug regimen, indication, line>

> **Abstract:** <abstract #, e.g., LB1234 / Presidential Symposium S100 / Oral S567> · **Session:** <session name, date, time CEST, hall> · **Embargo:** <date>

## At a glance

- **Sponsor:** <pharma / cooperative group (HOVON, GIMEMA, GELTAMO, GMLL, IFM, LYSA, NCRI, etc.)>
- **PI / presenter:** <name, institution>
- **NCT ID:** <NCTxxxxxxxx>
- **Phase:** <1 / 1b / 2 / 2-3 / 3 / pivotal / registry>
- **Design:** <arms, randomization, blinding>
- **N:** <enrolled / analyzed>
- **Primary endpoint(s):** <PFS / OS / EFS / CR rate / MRD-neg / VOC-free / FVIII expression>
- **Comparator:** <SOC / placebo / active comparator / historical>
- **Indication:** <heme disease, subtype, biomarker / cytogenetic selection>
- **Line:** <frontline / 1L / 2L / 3L+ / maintenance / post-transplant / post-CAR-T>

## Headline result

<One paragraph. Numbers + HR + p-value if known. If pre-embargo, mark
`*expected per <company> topline <date>*` or `*pre-embargo per <analyst source>*`
or `*ASCO 2026 readout, EHA 2026 update expected*`.>

## Mechanism / class

<Drug class, target, prior approvals (FDA + EMA). For CAR-T: construct details
(costim domain, CD-target, manufacturing). For bispecifics: format (IgG-like, BiTE,
DART). For gene therapy: vector + payload. Cross-link to related AACR mechanism
sessions.>

## Discussant takeaway

<Named discussant + key framing once known. EHA discussant identity is itself
a signal — senior figures in the relevant European disease group set the
post-meeting narrative.>

## Practice-changing?

<Yes / no / pending, with rationale: ESMO / EHA guideline implications, EMA / CHMP
filing path, unmet need, prior SOC. For non-malignant heme: ESH / EHA guideline
path. Flag any EU-only or EU-first approval angles.>

## Cross-links

- **AACR 2026:** <related mechanism / poster / session, if applicable>
- **AACR 2025:** <prior-year mechanism work>
- **ASCO 2026:** <heme readout earlier in the year, if applicable>
- **ASH 2026:** <December update expected, if applicable — flag "EHA-first, ASH-update">
- **ESMO 2026:** <if heme readout was presented there>
- **Other EHA 2026 trials:** <same class, same disease>
- **JPM 2026 / 2027:** <sponsor presentation / deal>

## Sources

- EHA abstract (HemaSphere supplement): <URL or "pending May 12 release">
- Company press release: <URL>
- Trade-press recap: <OncLive / Healio / ASCO Post URL>
- ClinicalTrials.gov: <NCT URL>
- EU CTR (EudraCT) / CTIS: <URL, if applicable>
```

## Master trial index (pre-meeting watch list)

Pre-meeting shortlist for stub creation. All entries below are **pre-abstract-release, sourced from company pipelines + AACR 2026 mechanism sessions + ASCO 2026 heme subset + EHA 2025 / ASH 2025 prior-year readouts + analyst preview pieces** — to be reconciled with the **May 12, 2026** abstract drop and the **June 2** LBA release. **`Result` column entries marked italic are speculative / not yet disclosed.**

### Lymphoma — DLBCL + bispecifics

| Trial | Sponsor | Indication | Phase | Endpoint | Status (pre-abstract-release) |
|---|---|---|---|---|---|
| **EPCORE NHL-2 / -3 / -5 interim** | Genmab / AbbVie | r/r DLBCL + 1L combinations | 1b/2 / 3 | PFS / CR / durability | *2-yr interim of epco mono; 1L combination signal* |
| **GO29781 / glofit + Pola-R-CHP (SKYGLO)** | Roche | 1L DLBCL high-IPI | 3 | PFS / EFS | *Interim topline tracking; ASH 2026 update expected* |
| **SUNMO / STARGLO follow-up** | Roche | r/r DLBCL glofit + GemOx | 3 | OS | *EHA tends to host SUNMO/STARGLO long-term* |
| **frontMIND interim** | Incyte / MorphoSys | 1L DLBCL high-IPI (tafa+lena+R-CHOP) | 3 | PFS interim | *ASCO 2026 LBA7000 PFS+; EHA reconcile + ASH update* |
| **POLARIX 5-yr follow-up** | Roche | 1L DLBCL (pola-R-CHP) | 3 | OS update | *Long-term durability* |

### Lymphoma — CLL + indolent

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **BRUIN CLL-321 European subset / pirtobrutinib** | Lilly | covalent-BTKi-resistant CLL | 3 | PFS | *Pivotal interim — Presidential Symposium candidate* |
| **GAIA / CLL13 follow-up** | German CLL Study Group | frontline fit CLL | 3 | MRD-neg / PFS | *Fixed-duration ven combos long-term* |
| **FLAIR long-term follow-up** | UK NCRI | frontline CLL | 3 | PFS / MRD | *Ibrutinib+ven vs FCR; ibr+ven vs ibr* |
| **MAJIC** | AbbVie / academic | frontline CLL | 3 | MRD-neg / PFS | *Acalabrutinib + ven fixed-duration* |
| **TRANSCEND CLL 004 follow-up** | BMS | r/r CLL liso-cel | 1/2 | DOR / OS | *2-3 yr durability European cohort* |
| **Mosunetuzumab FL long-term** | Roche | r/r FL | 2 | DOR | *5-yr durability* |

### Myeloma — CAR-T + bispecifics

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **CARTITUDE-4 long-term + CARTITUDE-5 interim** | J&J / Legend | r/r MM / NDMM | 3 | PFS / OS | *European-cohort durability + frontline pivot interim* |
| **KarMMa-3 long-term + KarMMa-9 interim** | BMS / 2seventy | r/r MM / NDMM | 3 | PFS | *Frontline ide-cel pivot interim* |
| **MajesTEC-3 / -5 interim teclistamab** | J&J | r/r MM + 1L combos | 3 | PFS | *ASCO 2026 readout, EHA interim, ASH long-term* |
| **MonumenTAL-3 interim talquetamab** | J&J | r/r MM 1–3L | 3 | PFS | *Pivotal interim* |
| **RedirecTT-1 / -2 update** | J&J | EMD MM dual bispecific | 1b/2 | ORR | *Dual bispecific (BCMA + GPRC5D)* |
| **IFM 2020-02 / HOVON-MM frontline** | IFM / HOVON | NDMM | 3 | PFS / MRD | *European cooperative-group frontline* |
| **Allogeneic BCMA CAR-T** | Allogene / Caribou / others | r/r MM | 1 | safety + ORR | *Class watch* |

### Acute leukemias — AML + ALL

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **Revumenib AUGMENT-101 + combos (European)** | Syndax | r/r KMT2A-r / NPM1-mut AML | 1/2 + combos | CR / MRD | *Post-approval European real-world + combos with ven/aza* |
| **Ziftomenib KOMET-001 / -007 / -008 European** | Kura | r/r NPM1-mut AML + frontline combos | 2 / 3 | CR / OS | *Post-approval European cohort + frontline pivot interim* |
| **HOVON-AML / GMLL frontline maintenance** | HOVON / GMLL | post-induction AML | 3 | RFS / OS | *European cooperative-group venetoclax maintenance* |
| **FLT3 inhibitors evolution** | various | FLT3-mut AML | 3 | OS | *Gilteritinib, quizartinib follow-up; new TKIs European cohorts* |
| **Frontline IDH inhibitors (European)** | Servier / others | IDH1/2-mut AML | 3 | EFS / OS | *Ivosidenib, enasidenib, olutasidenib frontline — EMA-relevant* |
| **GRAALL / ALL CAR-T European** | GRAALL / academic | r/r B-ALL | 3 + registry | EFS / OS | *Adult ALL European pivot + brexu-cel real-world* |

### MDS / MPN

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **Imetelstat post-approval European** | Geron | lower-risk MDS, transfusion-dependent | reg / 4 | TI rate | *Post-IMerge European real-world; Nordic MDS Group cohort* |
| **COMMANDS European follow-up** | BMS / Acceleron | lower-risk MDS ESA-naive luspatercept | 3 | TI rate | *Long-term durability European subset* |
| **IDH inhibitors in MDS** | Servier | IDH-mut MDS | 2/3 | response | *Frontline + post-HMA European cohorts* |
| **Momelotinib / pacritinib MF European** | GSK / Sobi | myelofibrosis | 3 / 4 | symptom + anemia | *Post-approval European real-world* |
| **IPSS-M-guided transplant (EBMT)** | EBMT | MDS frontline transplant decision | registry | OS | *EBMT registry IPSS-M cohort* |

### Cell and gene therapy — durability + access

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **Exa-cel / Casgevy European real-world** | Vertex / CRISPR | sickle cell + beta-thalassemia | reg / 4 | VOC-free / TI | *Post-approval European treatment-center early experience; Karolinska data prominent* |
| **Lovo-cel / Lyfgenia European** | bluebird bio | sickle cell | reg / 4 | VOC-free | *EU access pathway; second-malignancy reporting* |
| **In-vivo base / prime editing for SCD** | Beam / Editas / Verve / Prime | sickle cell (early phase) | 1 | safety + edit efficiency | *Class watch — next gen* |
| **Roctavian (val-rox) European long-term** | BioMarin | hemophilia A | reg / 4 | FVIII expression curve | *2–4 yr durability European cohort* |
| **Hemgenix (etranadez) European long-term** | CSL | hemophilia B | reg / 4 | FIX expression curve | *2–4 yr durability European cohort* |
| **CAR-T 4–5-yr durability (axi-cel, liso-cel, cilta-cel, ide-cel)** | Kite / BMS / J&J | r/r LBCL + MM | reg / 4 | DOR / PFS / SPM | *EBMT registry European cohort durability + SPM* |
| **Beta-thalassemia gene therapy long-term** | Vertex / bluebird | TDT | reg / 4 | TI rate | *Casgevy + ex-betibeglogene post-approval European* |

### Non-malignant heme

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **Mim8 / next-gen FVIIIa-mimetic** | Novo Nordisk | hemophilia A (with / without inhibitors) | 3 | bleed rate | *Post-FRONTIER pivot data; European cohort* |
| **Concizumab / fitusiran European follow-up** | Novo / Sanofi | hemophilia A/B with inhibitors | 3 | bleed rate | *Real-world + long-term European* |
| **Mitapivat in SCD / thalassemia** | Agios | sickle cell / thalassemia | 2/3 | Hb / VOC | *RISE UP and ENERGIZE follow-up* |
| **Etavopivat follow-up** | Novo Nordisk (ex-Forma) | sickle cell | 3 | Hb / VOC | *HIBISCUS pivot update* |
| **PNH C5 vs C3 inhibitor head-to-heads** | Alexion / Novartis / Apellis | PNH | 3 | hemoglobin / TI | *Pegcetacoplan, iptacopan, danicopan combos* |
| **Caplacizumab / rituximab iTTP follow-up** | Sanofi / academic | iTTP | 3 / registry | exacerbation rate | *Long-term European cohort* |
| **Factor XI inhibitors heme implications** | various | thrombosis | 3 | bleed / VTE | *Abelacimab, milvexian, asundexian — cardiology spillover* |

## Cross-cutting themes (for `themes.md`)

To synthesize across `trials/` once populated:

1. **EHA-first → ASH-update lineage.** Many trials get a phase-2 mature / phase-3 interim at EHA and a longer-follow-up update at ASH six months later. Map this lineage in `themes.md` to identify which EHA 2026 readouts will set the ASH 2026 framing.
2. **European cooperative-group dominance.** HOVON, GIMEMA, GELTAMO, GMLL, IFM, LYSA, NCRI studies that don't always travel to ASH. The European-only investigator network and the EMA / CHMP regulatory read-through.
3. **The "CAR-T tail" in European registries.** EBMT registry data on axi-cel, liso-cel, cilta-cel, ide-cel European durability and SPM signal. Real-world vs pivotal-trial gap is the load-bearing curve.
4. **Bispecifics + CAR-T compete and combine — European edition.** Sequencing data from European real-world (DLBCL: bispecific-after-CAR-T; MM: same). Class read-through to solid-tumor T-cell engagers (DLL3, B7-H3 — cross-link to lung / SCLC at ESMO).
5. **Menin / IDH / FLT3 mature in AML — European cohorts.** Revumenib and ziftomenib post-approval European real-world; combinations with ven/aza, FLT3, IDH; frontline pivots. Cross-link to AACR 2026 menin / leukemia mechanism sessions.
6. **Gene therapy for SCD — European access + durability.** Casgevy / Lyfgenia 2–3 yr European post-approval data; EMA approval status; Stockholm / Karolinska treatment-center experience. Payer access bottlenecks distinct from US.
7. **Red cell biology / non-malignant heme — EHA strength.** Mitapivat, etavopivat, hemoglobinopathy gene therapy, PNH inhibitors — proportionally larger at EHA than at ASH.
8. **AACR ↔ EHA ↔ ASH mechanism-to-clinic continuity.** Each EHA practice-changing trial traces to a 1–3 year prior AACR mechanism session and forward-projects to an ASH long-term update. Map the lineage in `themes.md`.
