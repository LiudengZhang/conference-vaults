# Trials — ASCO 2026

The primary artifact of this vault: **one Markdown file per trial / readout**. ASCO 2026 is a clinical-readout meeting, so the unit of analysis is the trial — not the speaker, not the tool, not the company.

> **Status:** Template + master index. Per-trial pages will be populated as embargoes lift (regular abstracts May 21, 5pm ET; LBAs the morning of presentation). Pre-meeting stubs flagged `*expected, subject to embargo*` are sourced from company toplines, abstract titles (released Apr 21), and analyst preview pieces; numbers can shift on the actual abstract reveal.

## Per-trial template

Each trial file (e.g., `libretto-432.md`) follows this schema. Copy and fill:

```markdown
# <Trial acronym / name> — <Drug regimen, indication, line>

> **Abstract:** <abstract #, e.g., LBA3> · **Session:** <session name, date, time CT, hall> · **Embargo:** <date>

## At a glance

- **Sponsor:** <pharma / cooperative group>
- **PI / presenter:** <name, institution>
- **NCT ID:** <NCTxxxxxxxx>
- **Phase:** <1 / 2 / 3 / 2-3>
- **Design:** <arms, randomization, blinding>
- **N:** <enrolled / analyzed>
- **Primary endpoint(s):** <PFS / OS / EFS / DFS / ORR / pCR>
- **Comparator:** <SOC / placebo / active comparator>
- **Indication:** <tumor type, subtype, biomarker selection>
- **Line:** <neoadjuvant / adjuvant / 1L / 2L / 3L+ / perioperative>

## Headline result

<One paragraph. Numbers + HR + p-value if known. If pre-embargo, mark
`*expected per <company> topline <date>*` or `*pre-embargo per <analyst source>*`.>

## Mechanism / class

<Drug class, target, prior approvals if any. Cross-link to related AACR mechanism sessions.>

## Discussant takeaway

<Named discussant + key framing once known. Discussant identity is itself a
signal — ASCO assigns senior figures to practice-changing trials.>

## Practice-changing?

<Yes / no / pending, with rationale: NCCN guideline implications, FDA filing path,
unmet need, prior SOC.>

## Cross-links

- **AACR 2026:** <related plenary / session / poster, if applicable>
- **AACR 2025:** <prior-year mechanism work>
- **Other ASCO 2026 trials:** <same class, same indication>
- **JPM 2026:** <sponsor presentation / deal>
- **Tools:** <if a biomarker / ctDNA / spatial method anchored the trial>

## Sources

- ASCO Meeting Library abstract: <URL or "pending embargo">
- Company press release: <URL>
- Trade-press recap: <OncLive / ASCO Post / Targeted Oncology URL>
- ClinicalTrials.gov: <NCT URL>
```

## Master trial index

The shortlist for pre-meeting stub creation. All numbers below are **pre-embargo, sourced from company toplines + OncLive / ApexOnco previews + ASCO press releases** — to be reconciled with the official abstract / presentation. **`Result` column entries marked italic are speculative / company topline only.**

| Trial | Sponsor | Indication | Phase | Endpoint | Result (pre-embargo) | Discussant | Practice-changing? |
|---|---|---|---|---|---|---|---|
| **LBA1 PROTEUS** | J&J / Janssen | High-risk localized prostate (perioperative) | 3 | MFS | *expected, subject to embargo* | TBD | TBD |
| **LBA2 SARC041** | Lilly | Advanced dedifferentiated liposarcoma | 3 | PFS | *expected, subject to embargo* | TBD | TBD |
| **LBA3 LIBRETTO-432** | Lilly (Loxo) | Stage IB–IIIA RET-fusion+ NSCLC (adjuvant) | 3 | EFS | *EFS positive per Lilly topline Feb 2026* | TBD | Likely yes — first adjuvant RET TKI |
| **LBA4 HARMONi-6** | Akeso / Summit | 1L advanced squamous NSCLC | 3 | OS | *PFS positive ESMO 2025; OS pending* | TBD | Class-defining if OS positive (PD-1×VEGF) |
| **LBA5 Rasolute-302** | Revolution Medicines | 2L pancreatic PDAC (RAS-mut) | 3 | OS / PFS | *mOS 13.2 vs 6.7 mo (HR 0.40, p<0.0001), per April 13 topline* | TBD | Yes — first pan-RAS Ph3 win in PDAC |
| **LBA8500 WU-KONG28** | Dizal | 1L EGFR exon 20 ins+ NSCLC | 3 | PFS | *expected, subject to embargo* | TBD | Possibly — vs platinum chemo SOC |
| **LBA8005 TRIPLEX** | French cooperative / AZ | 1L ES-SCLC | 3 | OS | *expected, subject to embargo* | TBD | TBD — TRT + chemo-IO combination |
| **LBA9503 OptimUM-02** | IDEAYA / Servier | 1L HLA-A2-neg metastatic uveal melanoma | 2/3 | PFS | *mPFS 6.9 vs 3.1 mo (HR 0.42, p<0.0001); ORR 37% vs 6%* | TBD | Yes — first effective 1L mUM regimen |
| **LBA7000 frontMIND** | Incyte / MorphoSys | 1L DLBCL (high IPI) | 3 | PFS | *PFS positive (HR 0.75, 95% CI 0.59–0.96, p=0.019) per Incyte topline Jan 2026* | TBD | Possibly — first R-CHOP+X PFS win in years |
| **LBA660 KN026-004** | Akeso / Hansoh | HER2+ early/locally advanced breast (neoadj) | 3 | pCR | *expected, subject to embargo* | TBD | Class read-through for anbenitamab vs THP |
| **Abstract 8000 ALCHEMIST EA5142** | NCI / ECOG-ACRIN | Stage IB–IIIA NSCLC (adjuvant) | 3 | DFS / OS | *expected, subject to embargo* | TBD | Adjuvant nivolumab post-chemo — possible SOC shift |
| **Abstract 8502 CROWN** | Pfizer | 1L ALK+ advanced NSCLC | 3 | PFS (7-yr update) | *expected — extended follow-up of prior PFS HR 0.27* | TBD | Confirmatory; CNS protection signal |
| **Abstract 8515 TRITON** | AZ | 1L STK11/KEAP1/KRAS-mut metastatic nonsquamous NSCLC | 2b | ORR / PFS | *expected, subject to embargo* | TBD | TBD — dual checkpoint in IO-cold subset |
| **LBA1000 ASCENT-04 PFS2** | Gilead | 1L PD-L1+ metastatic TNBC | 3 | PFS2 | *expected (PFS1 positive AACR/SABCS 2025)* | TBD | Confirmatory of TROP2-ADC durability |
| **LBA1006 persevERA BC** | Roche | 1L ER+/HER2- locally advanced/metastatic BC | 3 | PFS | *Missed primary per Roche topline Mar 2026* | TBD | Negative — preserves CDK4/6 + AI SOC |
| **LBA1007 SERENA-6 PFS2** | AZ | 1L ER+/HER2- ESR1-mut BC (switch design) | 3 | PFS2 / TT2P | *expected (PFS1 positive ASCO 2025 Plenary)* | TBD | Confirmatory — strengthens ctDNA switch |

**Additional shortlist candidates** to stub post-embargo (regular abstracts, not LBA):

- **GI:** Pancreatic KRAS-G12D early-phase combos; COMMIT update; CRC ctDNA-guided trials; gastric HERIZON-GEA-01 follow-up; amivantamab OrigAMI mCRC durability
- **GU:** KEYNOTE-B15 EV+pembro MIBC perioperative; LITESPARK-022 belzutifan adjuvant RCC; LITESPARK-011 belzutifan+lenva RCC 2L; PEACE-3 enza+Ra-223 mCRPC; actinium-225 PSMA
- **Heme:** MajesTEC-3 teclistamab+dara MM 1–3L; RedirecTT-1 dual bispecific MM EMD; Carvykti / anito-cel updates
- **Other:** DAREON-5 obrixtamig DLL3 bispecific (SCLC / NEC); CAR-T solid tumor early phase

## Cross-cutting themes (for `themes.md`)

To synthesize across `trials/` once populated:

1. **RAS-class drugs become real.** Daraxonrasib Plenary readout + KRAS-G12D early-phase combos. Cross-link to AACR 2025/2026 RAS mechanism sessions.
2. **PD-1 × VEGF bispecific class.** Ivonescimab HARMONi-6 OS readout is the class-defining moment. Echoes AbbVie RC148 ($5.6B JPM Day 1 deal), Summit JPM presence, BMS pumitamig.
3. **Perioperative IO expands.** PROTEUS (prostate), KEYNOTE-B15 (bladder), LIBRETTO-432 + ALCHEMIST (lung) — IO/TKIs moving earlier in disease.
4. **ADC durability story.** ASCENT-04 PFS2 (TROP2-ADC), trastuzumab deruxtecan continued read-through, novel ADC targets.
5. **Endocrine backbone resistance.** persevERA miss + SERENA-6 PFS2 — the limits of next-gen oral SERDs vs CDK4/6 + AI.
6. **China-origin assets dominate the LBA slate.** HARMONi-6 (Akeso), Rasolute-302 partner activity, anbenitamab (KN026-004), WU-KONG28 (Dizal). Continuity from JPM 2026 "China is the story" thread.
7. **Radioligands move to randomized data.** PEACE-3 enza+Ra-223, actinium-225 PSMA dose-escalation.
