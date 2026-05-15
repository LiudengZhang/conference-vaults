# Trials — ASH 2026

The primary artifact of this vault: **one Markdown file per trial / readout**. ASH 2026 is a clinical-readout meeting, so the unit of analysis is the trial — not the speaker, not the tool, not the company. Same per-trial schema as [ASCO 2026](../../asco-2026/trials/index.md) and [ESMO 2026](../../esmo-2026/trials/index.md); ASH adds an explicit **cell-and-gene-therapy** sub-axis and a **non-malignant heme** sub-axis.

> **Status:** Template + master index. Per-trial pages will be populated in two waves: (1) regular abstracts upon *Blood*-supplement release on **Nov 4, 2026, 9:00 AM ET**; (2) Late-Breaking Abstracts on **~Nov 24, 2026, 12:00 noon ET**. Pre-meeting stubs flagged `*expected, subject to embargo*` are sourced from company toplines, EHA 2026 mid-year readouts, ASCO 2026 heme subset, and analyst preview pieces; numbers can shift on the actual abstract reveal.

## Per-trial template

Each trial file (e.g., `frontmind-update.md`) follows this schema. Copy and fill:

```markdown
# <Trial acronym / name> — <Drug regimen, indication, line>

> **Abstract:** <abstract #, e.g., LBA-1 / Plenary #6 / Abstract 234> · **Session:** <session name, date, time CT, hall> · **Embargo:** <date>

## At a glance

- **Sponsor:** <pharma / cooperative group>
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
or `*EHA 2026 readout, ASH 2026 update expected*`.>

## Mechanism / class

<Drug class, target, prior approvals if any. For CAR-T: construct details (costim
domain, CD-target, manufacturing). For bispecifics: format (IgG-like, BiTE,
DART). For gene therapy: vector + payload. Cross-link to related AACR
mechanism sessions.>

## Discussant takeaway

<Named discussant + key framing once known. ASH discussant identity is itself
a signal — senior figures in the relevant disease group set the post-meeting
narrative.>

## Practice-changing?

<Yes / no / pending, with rationale: NCCN guideline implications, FDA filing path,
unmet need, prior SOC. For non-malignant heme: NCCN-equivalent ASH guideline path.>

## Cross-links

- **AACR 2026:** <related mechanism / poster / session, if applicable>
- **AACR 2025:** <prior-year mechanism work>
- **ASCO 2026:** <heme readout earlier in the year, if applicable>
- **EHA 2026:** <mid-year European readout, if applicable>
- **ESMO 2026:** <if heme readout was presented there>
- **Other ASH 2026 trials:** <same class, same disease>
- **JPM 2026 / 2027:** <sponsor presentation / deal>

## Sources

- ASH abstract (Blood supplement): <URL or "pending Nov 4 release">
- Company press release: <URL>
- Trade-press recap: <OncLive / ASH Clinical News / Healio / ASCO Post URL>
- ClinicalTrials.gov: <NCT URL>
```

## Master trial index (pre-meeting watch list)

Pre-meeting shortlist for stub creation. All entries below are **pre-abstract-release, sourced from company pipelines + AACR 2026 mechanism sessions + EHA 2025 / ASH 2025 prior-year readouts + analyst preview pieces** — to be reconciled with the Nov 4, 2026 abstract drop and the late-November LBA release. **`Result` column entries marked italic are speculative / not yet disclosed.**

### Lymphoma — DLBCL + bispecifics

| Trial | Sponsor | Indication | Phase | Endpoint | Status (pre-abstract-release) |
|---|---|---|---|---|---|
| **EPCORE NHL-2 / NHL-3 follow-up** | Genmab / AbbVie | r/r DLBCL + 1L combinations | 1b/2 / 3 | PFS / CR / durability | *3+ yr durability of epco mono; 1L combination signal* |
| **GO29781 / glofit + Pola-R-CHP** | Roche | 1L DLBCL high-IPI | 3 | PFS / EFS | *Topline tracking; possible practice-changing* |
| **MajesTEC analog in DLBCL** | various | r/r DLBCL post-CAR-T | 2 | ORR / CR | *Sequencing question — bispecific after CAR-T failure* |
| **frontMIND long-term follow-up** | Incyte / MorphoSys | 1L DLBCL high-IPI (tafa+lena+R-CHOP) | 3 | OS / PFS update | *ASCO 2026 LBA7000 PFS+; ASH update expected* |
| **CD20×CD3 head-to-head registry data** | multi-sponsor | r/r DLBCL real-world | obs | OS / ORR by class | *CIBMTR + ASH-flow registries* |

### Lymphoma — CLL + indolent

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **BRUIN CLL-321 / pirtobrutinib** | Lilly | covalent-BTKi-resistant CLL | 3 | PFS | *Pivotal update; possibly Plenary candidate* |
| **TRANSCEND CLL 004 follow-up** | BMS | r/r CLL liso-cel | 1/2 | DOR / OS | *2-3 yr durability* |
| **Venetoclax fixed-duration combos** | AbbVie | frontline CLL | 3 | MRD-neg / PFS | *MAJIC, CLL17, others* |

### Myeloma — CAR-T + bispecifics

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **CARTITUDE-5 / -6 cilta-cel** | J&J / Legend | NDMM / 1L MM | 3 | PFS / MRD | *Pivotal frontline data expected* |
| **KarMMa-9 ide-cel** | BMS / 2seventy | NDMM | 3 | PFS | *Frontline ide-cel pivot* |
| **MajesTEC-3 / -5 teclistamab** | J&J | r/r MM + 1L combos | 3 | PFS | *ASCO 2026 follow-up; ASH long-term* |
| **MonumenTAL-3 talquetamab** | J&J | r/r MM 1–3L | 3 | PFS | *Pivotal* |
| **RedirecTT-1 / -2** | J&J | EMD MM dual bispecific | 1b/2 | ORR | *Dual bispecific (BCMA + GPRC5D)* |
| **Allogeneic BCMA CAR-T** | Allogene / Caribou / others | r/r MM | 1 | safety + ORR | *Class watch* |

### Acute leukemias — AML + ALL

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **Revumenib AUGMENT-101 follow-up + combos** | Syndax | r/r KMT2A-r / NPM1-mut AML | 1/2 + combos | CR / MRD | *Post-approval real-world + combos with ven/aza* |
| **Ziftomenib KOMET-001 / -007 / -008** | Kura | r/r NPM1-mut AML + frontline combos | 2 / 3 | CR / OS | *Post-approval + frontline pivot* |
| **Venetoclax maintenance** | AbbVie | post-induction AML | 3 | RFS / OS | *VIALE-M, others* |
| **FLT3 inhibitors evolution** | various | FLT3-mut AML | 3 | OS | *Gilteritinib, quizartinib follow-up; new TKIs* |
| **Frontline IDH inhibitors** | Servier / others | IDH1/2-mut AML | 3 | EFS / OS | *Ivosidenib, enasidenib, olutasidenib frontline* |
| **CD19 / CD22 CAR-T in ALL** | Kite / Novartis / academic | r/r B-ALL | 3 + registry | EFS / OS | *Adult ALL pivots + pediatric updates* |

### MDS / MPN

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **Imetelstat post-approval** | Geron | lower-risk MDS, transfusion-dependent | reg / 4 | TI rate | *Post-IMerge real-world* |
| **COMMANDS follow-up** | BMS / Acceleron | lower-risk MDS ESA-naive luspatercept | 3 | TI rate | *Long-term durability* |
| **IDH inhibitors in MDS** | Servier | IDH-mut MDS | 2/3 | response | *Frontline + post-HMA* |
| **Momelotinib / pacritinib MF** | GSK / Sobi | myelofibrosis | 3 / 4 | symptom + anemia | *Post-approval real-world* |

### Cell and gene therapy — durability + access

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **Exa-cel / Casgevy 3+ yr follow-up** | Vertex / CRISPR | sickle cell + beta-thalassemia | reg / 4 | VOC-free / TI | *Post-approval durability + pediatric* |
| **Lovo-cel / Lyfgenia 3+ yr follow-up** | bluebird bio | sickle cell | reg / 4 | VOC-free | *Post-approval; second-malignancy reporting* |
| **In-vivo base / prime editing for SCD** | Beam / Editas / others | sickle cell (early phase) | 1 | safety + edit efficiency | *Class watch — next gen* |
| **Roctavian (val-rox) long-term** | BioMarin | hemophilia A | reg / 4 | FVIII expression curve | *2–4 yr durability* |
| **Hemgenix (etranadez) long-term** | CSL | hemophilia B | reg / 4 | FIX expression curve | *2–4 yr durability* |
| **CAR-T 5-yr durability (axi-cel, liso-cel, cilta-cel, ide-cel)** | Kite / BMS / J&J | r/r LBCL + MM | reg / 4 | DOR / PFS / SPM | *The "CAR-T tail" — long-term curves + second-primary-malignancy* |

### Non-malignant heme

| Trial | Sponsor | Indication | Phase | Endpoint | Status |
|---|---|---|---|---|---|
| **Mim8 / next-gen FVIIIa-mimetic** | Novo Nordisk | hemophilia A (with / without inhibitors) | 3 | bleed rate | *Post-FRONTIER pivot data* |
| **Concizumab / fitusiran follow-up** | Novo / Sanofi | hemophilia A/B with inhibitors | 3 | bleed rate | *Real-world + long-term* |
| **TTP / iTTP cap / rituximab combos** | Sanofi / academic | iTTP | 3 / registry | exacerbation rate | *Caplacizumab follow-up* |
| **Aplastic anemia frontline horse-ATG + eltrombopag** | NIH / academic | severe AA | 3 | response | *Long-term + transplant comparison* |
| **PNH C5 vs C3 inhibitor head-to-heads** | Alexion / Novartis / Apellis | PNH | 3 | hemoglobin / TI | *Pegcetacoplan, iptacopan, danicopan combos* |

## Cross-cutting themes (for `themes.md`)

To synthesize across `trials/` once populated:

1. **The "CAR-T tail" hardens.** 5-yr durability curves for axi-cel, liso-cel, cilta-cel, ide-cel; SPM signal in FDA reporting; real-world vs pivotal-trial gap; sequencing after CAR-T failure.
2. **Bispecifics + CAR-T compete and combine.** DLBCL: bispecific-after-CAR-T as standard salvage. MM: bispecific-after-CAR-T vs CAR-T-after-bispecific sequencing data. Class read-through to solid-tumor T-cell engagers (DLL3, B7-H3 — cross-link to lung / SCLC at ASCO).
3. **Menin / IDH / FLT3 mature in AML.** Revumenib and ziftomenib post-approval; combinations with ven/aza, FLT3, IDH; frontline pivots beginning. Cross-link to AACR 2026 menin / leukemia mechanism sessions.
4. **Gene therapy for SCD — durability + access.** Casgevy / Lyfgenia 3+ yr data; pediatric pivots; in-vivo next-gen approaches; payer access bottlenecks become the practical-care narrative.
5. **Hemophilia gene therapy — long-term FVIII / FIX expression decay.** Roctavian and Hemgenix 2–4 yr curves define the durability ceiling; non-factor competitor data (Mim8, fitusiran) frame the alternative.
6. **MDS / lower-risk MDS becomes a structured space.** Imetelstat + luspatercept + IDH inhibitors carve up frontline; IPSS-M-guided transplant decisions mature.
7. **AACR ↔ ASH mechanism-to-clinic continuity.** Each ASH practice-changing trial traces to a 1–3 year prior AACR mechanism session (menin biology, CAR-T construct engineering, bispecific format, base-editing platform). Map the lineage in `themes.md`.
