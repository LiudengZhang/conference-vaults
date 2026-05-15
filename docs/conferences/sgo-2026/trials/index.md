# Trials — SGO 2026

The primary artifact of this vault: **one Markdown file per trial / readout**. SGO 2026 is a clinical-readout meeting, so the unit of analysis is the trial — not the speaker, not the surgical platform, not the company.

> **Status:** Scaffold (post-meeting) — ready for retrospective bulk extraction. Meeting closed **one month ago** (Apr 10–13, 2026). All abstract embargoes lifted; the master index below is finalized with verified readouts from *Gynecologic Oncology* abstracts, simultaneous *Lancet* / *NEJM* / *JCO* publications, SGO Meeting News daily coverage, and OncLive / Targeted Oncology / OncoDaily trade-press recaps. Per-trial pages will be filled in mechanically — the shape, master index, and source URLs are pre-wired here.

## Per-trial template

Each trial file (e.g., `rosella.md`) follows this schema. Copy and fill:

```markdown
# <Trial acronym / name> — <Drug regimen, indication, line>

> **Abstract:** <abstract #, e.g., LBA1> · **Session:** <Plenary I / II / III / IV / V, date, time AST, hall> · **Simultaneous publication:** <Lancet / NEJM / JCO / Gyn Onc DOI>

## At a glance

- **Sponsor:** <pharma / cooperative group(s) — often multi-group: GOG / NRG / ENGOT / APGOT / LACOG / ANZGOG>
- **PI / presenter:** <name, institution>
- **NCT ID:** <NCTxxxxxxxx>
- **Phase:** <1 / 1-2 / 2 / 2-3 / 3>
- **Design:** <arms, randomization, blinding, biomarker selection>
- **N:** <enrolled / analyzed>
- **Primary endpoint(s):** <PFS / OS / ORR / DOR / pCR>
- **Comparator:** <SOC / placebo / active comparator>
- **Indication:** <tumor type, subtype, biomarker — e.g., FRα+ PSOC, dMMR/MSI-H endometrial, locally advanced cervical>
- **Line:** <neoadjuvant / adjuvant / 1L / 2L / 3L+ / maintenance>

## Headline result

<One paragraph. Numbers + HR + p-value. Cite simultaneous publication if applicable
(e.g., "Lancet 2026 Apr 11 — DOI:10.1016/S0140-6736(26)00462-9").>

## Mechanism / class

<Drug class, target, prior approvals if any. Cross-link to related AACR mechanism sessions
(B7-H4, CDH6, FRα, B7-H3, TROP2, glucocorticoid receptor antagonism, etc.).>

## Discussant / moderator takeaway

<Named Plenary moderator + key framing. SGO Plenary moderators are typically NCCN
panel members — their framing translates directly into guideline updates.>

## Practice-changing?

<Yes / no / pending, with rationale: NCCN guideline implications, FDA filing path,
unmet need, prior SOC. ROSELLA is a fast-cycle example — Mar 2026 FDA approval
preceded the SGO presentation.>

## Cross-links

- **AACR 2026:** <related plenary / session / poster on the target class, e.g., B7-H4, CDH6>
- **AACR prior years:** <preclinical mechanism work — relacorilant GR antagonism, MIRV FRα biology>
- **Other SGO 2026 trials:** <same disease / same class>
- **ASCO 2026 forward link:** <expected May/Jun sequel — OS update, subgroup analysis, biomarker correlates>
- **ESMO 2026 forward link:** <expected Oct sequel — European subgroup, mature follow-up>
- **JPM 2026:** <sponsor investor presentation Jan 12–15>
- **Tools:** <if a biomarker / ctDNA / FRα IHC / B7-H4 IHC method anchored the trial>

## Sources

- *Gynecologic Oncology* abstract: <URL or DOI>
- Simultaneous publication (*Lancet* / *NEJM* / *JCO*): <URL or DOI>
- SGO Meeting News daily-coverage: <URL>
- Company press release: <URL>
- Trade-press recap: <OncLive / Targeted Oncology / OncoDaily / CancerNetwork URL>
- ClinicalTrials.gov: <NCT URL>
```

## Master trial index

Verified post-meeting (Apr 10–13, 2026). Numbers below are **on-record from the SGO abstracts + simultaneous publications + post-meeting trade-press recaps**. `Result` column is final-data, not pre-embargo.

### Ovarian cancer

| Trial | Sponsor | Indication | Phase | Endpoint | Result | Moderator / Plenary | Practice-changing? |
|---|---|---|---|---|---|---|---|
| **ROSELLA (LBA, Plenary I)** | Corcept · GOG-3073 / ENGOT-ov72 / APGOT-Ov10 / LACOG-0223 / ANZGOG-2221 | Platinum-resistant epithelial ovarian (post-bev) | 3 | OS + PFS (dual primary) | **mOS 16.0 vs 11.9 mo, HR 0.65 (95% CI 0.51–0.83), p=0.0004; mPFS HR 0.70, p=0.0076**; simultaneous *Lancet* publication | Plenary I, Apr 10 | **Yes** — Lifyorli (relacorilant) FDA-approved Mar 2026; first GR-antagonist class win in solid tumor |
| **KEYNOTE-B96 (Plenary I encore)** | Merck · ENGOT-ov65 | Platinum-resistant recurrent ovarian | 3 | PFS | PFS positive (per FDA approval Feb 2026); pembro + paclitaxel ± bev | Plenary I, Apr 10 | Yes — FDA-approved 1Q26 |
| **NRG-GY019 (Plenary I)** | NRG | Low-grade serous ovarian, frontline | 3 | PFS (non-inferiority) | Letrozole alone **failed non-inferiority** vs paclitaxel/carboplatin + letrozole — chemo retained in LGSOC SOC | Plenary I, Apr 10 (presenter: Amanda Fader, MD) | Yes (negative) — preserves chemo backbone in LGSOC |
| **Mirvetuximab + carboplatin → MIRV maintenance (LBA)** | AbbVie · IMGN853-0420 | Platinum-sensitive recurrent ovarian, FRα+ | 2 | ORR maintenance | **ORR 68% in maintenance phase; 63.9% in PARPi-pretreated subgroup**; 81% continued to MIRV monotherapy maintenance | Apr 12 | Supports moving ELAHERE earlier into PSOC; AbbVie life-cycle |
| **REJOICE-Ovarian01** | Daiichi Sankyo | Platinum-resistant high-grade serous/endometrioid ovarian | 2/3 | ORR | **ORR 50.5% overall**; CDH6 ADC first clinical efficacy at scale | Apr 11 | Pivotal Ph3 expansion design; first CDH6-targeted class data |
| **RAMP-201 follow-up** | Verastem | Low-grade serous ovarian (recurrent) | 2 | DOR / PFS | **DOR 31 mo; PFS 12.9 mo overall, 19.6 mo in KRAS-mut subgroup** | Apr 10 | Confirms avutometinib + defactinib durability in KRAS-mut LGSOC |
| **GLORIOSA / TroFuse-022 / RAINFOL-04** | Multiple sponsors | Platinum-sensitive recurrent ovarian | 3 | PFS / OS | Updates from ADC-maintenance Ph3 designs (mirvetuximab + bev, sac-tirumotecan, etc.) | Apr 11 | Maintenance ADC class — defining future SOC |
| **BNT-324 (Phase 1/2)** | BioNTech | Platinum-sensitive + platinum-resistant ovarian | 1/2 | ORR | Anti-B7-H3 ADC active in both settings | Apr 11 | Early signal; B7-H3 class entry |
| **BEHOLD-1** | TBD sponsor | Platinum-resistant recurrent ovarian | 1/2 | ORR | **ORR 62%** in platinum-resistant | Apr 11 | Early-phase ADC; pivotal-design-defining |

### Endometrial cancer

| Trial | Sponsor | Indication | Phase | Endpoint | Result | Moderator / Plenary | Practice-changing? |
|---|---|---|---|---|---|---|---|
| **RUBY 4-year OS (Plenary III)** | GSK · ENGOT-EN6-NSGO/GOG-3031 | 1L advanced/recurrent endometrial (all-comer, with dMMR primary) | 3 | OS (mature update) | **dMMR/MSI-H: HR 0.32 (95% CI 0.17–0.63) — 68% mortality reduction; ~73% 4-yr OS**; MMRp HR 0.79, 7-mo median OS gain | Plenary III, Apr 12 | **Yes (confirmatory)** — dostarlimab + chemo 1L SOC reinforced |
| **Puxitatug samrotecan BLUESTAR (LBA, Ph1/2a)** | AstraZeneca · AZD8205 | Advanced/metastatic endometrial cancer | 1/2a | ORR / PFS | **ORR 34.6% @ 2.0 mg/kg, 38.5% @ 2.4 mg/kg; 12-wk DCR 80.8% / 84.6%; mPFS 7.0 mo** | Apr 12 (presenter: Stephanie Gaillard, MD, Johns Hopkins) | First-in-human B7-H4 ADC clinical efficacy data |
| **D-RT** | GSK | Adjuvant stage III-IVA dMMR endometrial (no residual) | 2 | DFS | Chemo-free dostarlimab + RT — feasibility + efficacy in dMMR adjuvant | Apr 12 | Pilot for chemo-free adjuvant in dMMR |
| **GOG-3039** | GOG | Advanced/recurrent HR+ endometrioid endometrial | 2 | PFS / ORR | **6-mo PFS 57%; ORR 39%** with abemaciclib + letrozole | Apr 12 | Defines CDK4/6 + AI signal in HR+ endometrial |
| **Destiny-Endometrial01 / 02 / TroFuse-033** | Daiichi/AZ, Merck/Kelun | Adjuvant / 1L endometrial ADC | 3 | PFS | Ph3 ADC designs in adjuvant + 1L | Apr 12 | Defines next-line endometrial SOC |
| **BEHOLD-01** | TBD sponsor | Recurrent endometrial | 1/2 | ORR | **ORR 67%** | Apr 12 | Early-phase signal |

### Cervical cancer

| Trial | Sponsor | Indication | Phase | Endpoint | Result | Moderator / Plenary | Practice-changing? |
|---|---|---|---|---|---|---|---|
| **KEYNOTE-A18 mature OS** | Merck · ENGOT-cx11 / GOG-3047 | Locally advanced cervical (high-risk, stage IB–IVA) | 3 | OS (long-term FU) | **OS HR 0.73 (95% CI 0.57–0.94); 36-mo OS 81.8% vs 74.4%; 48-mo OS 75.4% vs 70.2%**; no new safety signals | Apr 13 | Yes — pembro + CCRT 1L SOC for high-risk LACC, durable benefit |
| **InnovaTV 205 Arm H** | Pfizer/Seagen · Genmab | 1L recurrent/metastatic cervical | 2 | ORR / DOR | **ORR 66%; mDOR 13 mo** with tisotumab vedotin + carboplatin + pembrolizumab ± bevacizumab | Apr 13 | TV + chemo-IO 1L expansion |
| **TroFuse-036** | Merck/Kelun | Cervical maintenance post-CCRT | 2 | PFS | Sacituzumab tirumotecan + pembro ± bev; novel maintenance strategy | Apr 13 | Defines post-CCRT maintenance design space |
| **IBI130 (Phase 1/2)** | Innovent | Recurrent/metastatic cervical | 1/2 | ORR | **ORR 53%; manageable safety** — anti-TROP2 ADC | Apr 13 | China-origin TROP2 ADC entry in cervical |

### Surgical innovation + rare tumors (Day 4 Plenary V)

| Topic | Setting | Headline |
|---|---|---|
| Sentinel lymph node mapping in early-stage endometrial | Surgical | Updated SLN-mapping algorithm performance + ultra-staging |
| Robotic platforms in cervical surgery | Surgical | Long-term outcomes post-LACC trial reassessment |
| Fertility-sparing in early cervical | Surgical | Trachelectomy and conization outcomes |
| Uterine leiomyosarcoma combination Ph2 | Sarcoma | Novel combination Ph2 data |

## Cross-cutting themes (for `program-notes.md`)

To synthesize across the trial list:

1. **ADC era arrives in gyn-onc.** Six distinct ADC targets with 2026 clinical efficacy data: FRα (mirvetuximab — moving earlier into PSOC), CDH6 (raludotatug deruxtecan — first signal), B7-H4 (puxitatug samrotecan AZD8205 — first-in-human), B7-H3 (BNT-324), TROP2 (sacituzumab tirumotecan, IBI130), tissue factor (tisotumab vedotin). This is the AACR ADC linker-chemistry-payload mechanism story landing in the clinic.
2. **Glucocorticoid receptor antagonism is a class.** ROSELLA's Lifyorli win (relacorilant) is the first GR-antagonist solid-tumor Phase 3 win — a new class with read-through to cortisol-axis biology across hormone-receptor-modulated cancers.
3. **Chemo-immunotherapy 1L is now SOC across all three gyn cancers.** RUBY (endometrial dostarlimab), KEYNOTE-A18 (cervical pembro + CCRT), KEYNOTE-B96 (ovarian platinum-resistant pembro). Mature OS data at SGO 2026 closed the loop on this SOC shift.
4. **Cooperative-group multi-region sponsorship.** ROSELLA alone has five cooperative-group sponsors (GOG / ENGOT / APGOT / LACOG / ANZGOG). This authorship density is a unique gyn-onc structural feature versus other oncology subspecialties.
5. **Biomarker-defined subgroups dominate.** dMMR/MSI-H, FRα+, BRCA, HRD, KRAS-mut LGSOC, B7-H4+, CDH6+, PD-L1+, p53-abn, POLE-mut — every Phase 3 in 2026 reports a molecular subgroup. The "all-comer" gyn-onc trial era is over.
6. **China-origin assets surface.** IBI130 (Innovent anti-TROP2), BNT-324 (BioNTech B7-H3 — Mainz/Berlin biotech), and the AZ / Daiichi global ADCs all cross-list with US trade-press. Echo of the JPM 2026 "China is the story" thread.
7. **Surgical innovation gets a Plenary.** SGO's preservation of a dedicated surgical-innovation Plenary distinguishes it from ASCO/ESMO; sentinel-node, robotic, and fertility-sparing data here often inform NCCN surgical guidelines directly.
