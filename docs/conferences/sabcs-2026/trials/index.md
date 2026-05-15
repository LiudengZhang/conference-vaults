# Trials — SABCS 2026

The primary artifact of this vault: **one Markdown file per trial / readout**. SABCS 2026 is a breast-cancer clinical-readout meeting, so the unit of analysis is the trial — not the speaker, not the tool, not the company.

> **Status:** Template + master index. Per-trial pages will be populated as the SABCS 2026 program is released (Oct–Nov 2026) and embargoes lift (day of presentation, Dec 8–11). Pre-meeting stubs flagged `*expected, subject to embargo*` are sourced from company toplines, prior-year readouts, JPM 2026 sponsor guidance, and analyst preview pieces; trial identities and numbers can shift on the actual abstract reveal.

## Per-trial template

Each trial file (e.g., `monarche-7yr.md`, `destiny-breast09.md`) follows this schema. Copy and fill:

```markdown
# <Trial acronym / name> — <Drug regimen, indication, line>

> **Abstract:** <abstract #, e.g., GS1-01> · **Session:** <session name, date, time CT, hall> · **Embargo:** <date>

## At a glance

- **Sponsor:** <pharma / cooperative group>
- **PI / presenter:** <name, institution>
- **NCT ID:** <NCTxxxxxxxx>
- **Phase:** <1 / 2 / 3 / 2-3>
- **Design:** <arms, randomization, blinding>
- **N:** <enrolled / analyzed>
- **Primary endpoint(s):** <iDFS / EFS / PFS / OS / pCR / ORR>
- **Comparator:** <SOC / placebo / active comparator>
- **Indication:** <HR+/HER2-, HER2+, TNBC; biomarker selection: HER2-low/ultralow, ESR1-mut, BRCA, PD-L1>
- **Line:** <neoadjuvant / adjuvant / 1L MBC / 2L MBC / 3L+ MBC>

## Headline result

<One paragraph. Numbers + HR + p-value if known. If pre-embargo, mark
`*expected per <company> topline <date>*` or `*pre-embargo per <analyst source>*`.>

## Mechanism / class

<Drug class, target, prior approvals if any. Cross-link to related AACR mechanism sessions
or prior SABCS readouts in the same series (e.g., DESTINY-Breast lineage).>

## Discussant takeaway

<Named discussant / session chair + key framing once known. SABCS uses session-level
discussants rather than per-abstract — capture the GS session chair framing.>

## Practice-changing?

<Yes / no / pending, with rationale: NCCN breast guideline implications, FDA filing path,
unmet need, prior SOC. SABCS is the venue where most NCCN breast updates originate.>

## Cross-links

- **SABCS prior years:** <e.g., monarchE original GS5 2020; KEYNOTE-756 GS01 2023>
- **AACR 2026:** <related mechanism / biomarker session>
- **ASCO 2026:** <e.g., ASCENT-04 PFS1 LBA1000, SERENA-6 PFS1 Plenary>
- **ESMO 2026:** <prior interim readouts>
- **JPM 2026:** <sponsor presentation / pipeline framing>
- **Other SABCS 2026 trials:** <same class, same target>

## Sources

- *Cancer Research* SABCS abstract: <DOI or "pending day of presentation">
- Company press release: <URL>
- Trade-press recap: <OncLive / ASCO Post / Targeted Oncology / CancerNetwork URL>
- ClinicalTrials.gov: <NCT URL>
```

## Master trial index

The shortlist for pre-meeting stub creation. All entries below are **anticipated** — sourced from prior-year SABCS slots, JPM 2026 sponsor guidance, ongoing-trial timelines, and analyst preview material. **Trial slot assignments (GS numbers) are unknown until program release (Oct–Nov 2026); all numbers are speculative until then.** Italicized `Result` entries are pre-embargo / topline-only.

| Trial | Sponsor | Indication | Phase | Endpoint | Result (pre-embargo) | Expected status | Practice-changing? |
|---|---|---|---|---|---|---|---|
| **monarchE 7-yr** | Lilly | HR+/HER2- high-risk EBC adjuvant (abemaciclib + ET) | 3 | iDFS / OS | *Prior 5-yr iDFS HR 0.68; 7-yr OS the watched endpoint* | *expected, GS slot likely* | Strengthens / confirms adjuvant SOC if OS HR <0.85 |
| **NATALEE long-term** | Novartis | HR+/HER2- stage II–III EBC adjuvant (ribociclib + ET) | 3 | iDFS / OS | *Prior iDFS HR 0.749; OS pending* | *expected, GS slot likely* | Practice-changing — extends CDK4/6 adjuvant to stage II; competes with monarchE on tolerability |
| **DESTINY-Breast09** | Daiichi Sankyo / AZ | HER2+ 1L MBC (T-DXd ± pertuzumab vs THP) | 3 | PFS | *PFS positive per AZ/Daiichi topline; magnitude TBD* | *expected, GS01 / late-breaker* | Yes — would displace THP as 1L HER2+ SOC |
| **DESTINY-Breast05** | Daiichi Sankyo / AZ | HER2+ high-risk residual disease post-neoadj (T-DXd vs T-DM1) | 3 | iDFS | *expected, subject to embargo* | *anticipated* | Yes if positive — displaces T-DM1 in KATHERINE niche |
| **DESTINY-Breast11** | Daiichi Sankyo / AZ | HER2+ high-risk EBC neoadj (T-DXd → THP vs ddAC-THP) | 3 | pCR / EFS | *expected, subject to embargo* | *anticipated; may slip to 2027* | Practice-changing if pCR meaningfully higher |
| **DESTINY-Breast12 update** | Daiichi Sankyo / AZ | HER2+ MBC with active/stable brain mets (T-DXd) | 3b | CNS-PFS / OS | *Prior CNS-ORR ~80% at SABCS 2024 / ESMO 2025* | *expected update* | Confirmatory; brain-mets framing |
| **EMBER-3 update** | Lilly | 2L ER+/HER2- MBC, ESR1-mut and wild-type (imlunestrant ± abema) | 3 | PFS | *Prior PFS positive in ESR1-mut subgroup* | *expected mature OS* | Class-defining for next-gen oral SERDs |
| **persevERA OS** | Roche/Genentech | 1L ER+/HER2- MBC (giredestrant + palbo vs letrozole + palbo) | 3 | OS (sec) | *PFS missed primary per Roche Mar 2026; OS context-setting* | *expected secondary readout* | Preserves CDK4/6 + AI SOC; confirms SERD-monotherapy ceiling |
| **EMBER-4** | Lilly | HR+/HER2- EBC adjuvant (imlunestrant vs ET SOC, post-monarchE strata) | 3 | iDFS | *Enrolling; readout not expected at SABCS 2026* | *ongoing-trial poster only* | Future readout — 2027/28 |
| **VERITAC-2** | Arvinas / Pfizer | 2L/3L ER+/HER2- MBC, ESR1-mut (vepdegestrant PROTAC) | 3 | PFS | *PFS positive in ESR1-mut subgroup per AACR 2025 / SABCS 2024* | *expected mature data / OS update* | Class-validating for ER-targeted PROTAC |
| **postMONARCH update** | Lilly | 2L HR+/HER2- MBC post-CDK4/6 (abema + fulv vs fulv) | 3 | PFS | *Prior PFS HR 0.73; mature OS the watch* | *expected update* | Strengthens post-CDK4/6 sequencing |
| **KEYNOTE-756 follow-up** | MSD | HR+/HER2- high-risk EBC neoadj (pembro + chemo neoadj → pembro + ET adj) | 3 | EFS / OS | *pCR positive at SABCS 2023; EFS the practice-changing endpoint* | *expected, GS slot* | Yes if EFS positive — extends pembro to HR+ EBC |
| **CheckMate 7FL follow-up** | BMS | HR+/HER2- high-risk EBC neoadj (nivo + chemo) | 3 | EFS | *pCR positive at SABCS 2023* | *expected EFS update* | Confirmatory PD-1 + chemo neoadj in HR+ EBC |
| **A-BRAVE final** | Cooperative (Italy) | TNBC post-neoadj residual disease (avelumab adjuvant) | 3 | DFS | *Prior DFS marginal* | *expected mature data* | Marginal — likely subgroup-driven |
| **OptimICE-RD / NRG-BR009** | NRG / cooperative | TNBC residual disease post-neoadj (pembro + cape vs pembro alone) | 3 | iDFS | *enrolling/maturing; readout window plausible 2026–27* | *anticipated* | Post-KEYNOTE-522 adjuvant intensification question |
| **ASCENT-04 PFS2 / OS update** | Gilead | 1L PD-L1+ MBC TNBC (sacituzumab + pembro) | 3 | PFS2 / OS | *PFS1 positive at ASCO 2026 LBA1000* | *expected confirmatory* | Confirmatory TROP2-ADC durability |
| **ASCENT-03** | Gilead | 1L PD-L1- MBC TNBC (sacituzumab vs chemo) | 3 | PFS | *Sacituzumab + pembro precedent; PD-L1- subset* | *expected* | Potential 1L TNBC niche extension |
| **TROPiCS-02 long-term** | Gilead | 2L+ HR+/HER2- MBC (sacituzumab) | 3 | OS update | *Prior PFS / OS positive* | *expected mature data* | Strengthens TROP2-ADC in HR+ post-endocrine |
| **TROPION-Breast01 / -02** | Daiichi / AZ | HR+/HER2- and TNBC MBC (datopotamab deruxtecan) | 3 | PFS / OS | *Prior PFS positive HR+; TNBC data evolving* | *expected updates* | Class competition with sacituzumab |
| **CAPItello-291 follow-up** | AZ | 2L HR+/HER2- MBC (capivasertib + fulv, AKT pathway-altered subset) | 3 | OS | *PFS positive; OS the watched endpoint* | *expected mature data* | Confirms AKT-i in PIK3CA/AKT1/PTEN-altered subset |
| **INAVO120 / INAVO121** | Roche/Genentech | 1L/2L HR+/HER2- PIK3CA-mut MBC (inavolisib combos) | 3 | PFS / OS | *INAVO120 PFS HR 0.43 at SABCS 2023; OS now the watch* | *expected update* | Strengthens 1L PIK3CA-mut combo |
| **HER2CLIMB-05 / HER2CLIMB-02 update** | Pfizer / Seagen | HER2+ MBC and brain mets (tucatinib combinations) | 3 | PFS / CNS-PFS | *Prior HER2CLIMB positive* | *expected ongoing-trial or update* | Sequencing question vs T-DXd |
| **DARE / LEADER / c-TRAK-TN ctDNA updates** | Cooperative / academic | ctDNA-MRD-guided adjuvant decisions, HR+/HER2- and TNBC | 2/3 | RFS / intervention triggering | *Signal-finding; not practice-changing yet* | *expected updates* | Sets up ctDNA-MRD adjuvant guideline path |
| **POSITIVE follow-up** | IBCSG / cooperative | HR+ EBC fertility / pregnancy interruption of ET | observational/randomized | BCFI / disease events | *Original GS4 2022; 3-yr safety positive; longer follow-up the question* | *expected update* | Strengthens shared decision-making for young patients |
| **HER2-ultralow analyses** | Multiple | Assay standardization for HER2-low/-ultralow IHC; T-DXd eligibility | analytic / correlative | concordance / outcome | *Pathology standardization theme* | *expected mini-symposium* | Sets the eligible-population denominator for ADC SOC |

**Additional shortlist candidates** to stub once the program drops:

- **Brain metastases:** intrathecal T-DXd / tucatinib early-phase, leptomeningeal disease trials, novel BBB-penetrant HER2 / TROP2 conjugates.
- **HER2+ de-escalation:** PHERGain follow-up (chemo-free neoadj), CompassHER2 series.
- **Early-phase / novel:** CDK2-selective inhibitors, KAT6 / SMARCA2 degraders, AR-targeted in TNBC, oral GnRH antagonists (relugolix combinations).
- **Health disparities / survivorship:** GLP-1 in breast cancer obesity, racial disparities in ADC outcomes, cardiotoxicity in HER2 long-term survivors.
- **Prevention:** anastrozole / tamoxifen chemoprevention long-term follow-up, denosumab fracture / DFS follow-up.

## Cross-cutting themes (for `themes.md`)

To synthesize across `trials/` once populated:

1. **HER2+ 1L SOC reset.** DESTINY-Breast09 vs THP — if PFS magnitude is large, the entire HER2+ 1L paradigm shifts to T-DXd-first. Echoes the DESTINY-Breast03 2L reset of 2021.
2. **CDK4/6 adjuvant battle: monarchE vs NATALEE.** 7-yr OS for abemaciclib + the maturing NATALEE OS define which agent (and which patient subset, II vs III high-risk) wins the adjuvant niche.
3. **Next-gen oral SERDs — class definition.** EMBER-3, persevERA, VERITAC-2, plus ELAINE/ARV-471 — does any oral SERD beat the CDK4/6 + AI 1L SOC, or do they stay 2L+/ESR1-mut?
4. **Post-CDK4/6 sequencing.** postMONARCH, INAVO121, CAPItello-291 OS — the field has multiple second-line options; SABCS 2026 will start to rank them by subset (PIK3CA, AKT, ESR1, wild-type).
5. **TROP2-ADC class.** Sacituzumab govitecan vs datopotamab deruxtecan — cross-trial PFS / OS / tolerability comparisons in HR+ and TNBC.
6. **ctDNA-MRD adjuvant decision-making.** DARE / LEADER / c-TRAK-TN — moving from signal-finding to randomized intervention. The FDA / NCCN posture watch.
7. **Brain-metastasis activity as a class differentiator.** T-DXd (DB-12), tucatinib (HER2CLIMB), intrathecal regimens — the ADC + small-molecule brain-mets data is becoming a category for label / guideline differentiation.
8. **Neoadjuvant IO in HR+ EBC.** KEYNOTE-756 EFS, CheckMate 7FL EFS — does pembro / nivo extend from TNBC (KEYNOTE-522 SOC) into HR+ high-risk EBC?
9. **Pregnancy / fertility / survivorship.** POSITIVE long-term — the practice-changing data that made it OK to pause ET; longer follow-up tests durability.
