# Trials — ASCO GI 2026

The primary artifact of this vault: **one Markdown file per trial / readout**. ASCO GI 2026 is a clinical-readout meeting (Jan 8–10, 2026, Moscone West, San Francisco), so the unit of analysis is the trial — not the speaker, not the tool, not the company. Mirrors the [ASCO 2026 trials template](../../asco-2026/trials/index.md).

> **Status:** Template + retrospective master index. Per-trial pages are **deferred** in May 2026 — priority is the ASCO main-meeting vault (`asco-2026/`) running live May 29 – Jun 2. The master index below captures the January readouts so forward cross-links from the May meeting (e.g., Rasolute-302 Plenary LBA5 builds on daraxonrasib Phase 1/2 here) resolve cleanly. Full per-trial pages can be backfilled from the ASCO Meeting Library on demand.

## Per-trial template

Each trial file (e.g., `breakwater-cohort3.md`) follows the same schema as ASCO 2026. Copy and fill:

```markdown
# <Trial acronym / name> — <Drug regimen, indication, line>

> **Abstract:** <abstract #, e.g., LBA438> · **Session:** <session name, date, time PT, hall> · **JCO 4_suppl DOI:** <10.1200/JCO.2026.44.4_suppl.XXX>

## At a glance

- **Sponsor:** <pharma / cooperative group>
- **PI / presenter:** <name, institution>
- **NCT ID:** <NCTxxxxxxxx>
- **Phase:** <1 / 2 / 3 / 1-2 / 2-3>
- **Design:** <arms, randomization, blinding>
- **N:** <enrolled / analyzed>
- **Primary endpoint(s):** <PFS / OS / ORR / DCR / DoR / pCR>
- **Comparator:** <SOC / placebo / active comparator>
- **Indication:** <tumor type, subtype, biomarker selection>
- **Line:** <neoadjuvant / adjuvant / 1L / 2L / 3L+ / perioperative>
- **Biomarker:** <KRAS-G12D, BRAF-V600E, HER2+, FGFR2-fusion, IDH1-R132, MSI-H, claudin 18.2+, ...>

## Headline result

<One paragraph. Numbers + HR + p-value. Cite JCO 4_suppl DOI for post-meeting data.>

## Mechanism / class

<Drug class, target, prior approvals if any. Cross-link to AACR mechanism sessions.>

## Discussant takeaway

<Named discussant + key framing. ASCO GI discussants set the field-level narrative
that propagates to ASCO main meeting in May.>

## Practice-changing?

<Yes / no / pending, with rationale: NCCN guideline implications, FDA filing path,
unmet need, prior SOC.>

## Cross-links

- **ASCO 2026 (May/Jun):** <follow-up Phase 3, OS confirmation, subgroup analysis>
- **AACR 2026 (Apr):** <related mechanism / biomarker session>
- **ESMO GI 2026 (Jul):** <EU-perspective follow-up>
- **JPM 2026:** <sponsor presentation week of Jan 12-15, same week as ASCO GI>
- **Prior ASCO GI:** <2024 / 2025 dose-finding or interim data>
- **Other ASCO GI 2026 trials:** <same class, same indication>

## Sources

- ASCO Meeting Library abstract: <URL>
- JCO 4_suppl publication: <DOI>
- Company press release: <URL>
- Trade-press recap: <OncLive / ASCO Post / VJOncology URL>
- ClinicalTrials.gov: <NCT URL>
```

## Master trial index — by disease group

January 8–10, 2026 retrospective. Numbers below are sourced from ASCO Meeting Library abstracts (released on-day), JCO 4_suppl 2026, and post-meeting trade-press recaps (VJOncology, OncLive, ASCO Post, Targeted Oncology). **Italicized results are pre-meeting toplines that should be reconciled against the on-day abstract** where the per-trial page hasn't yet been written.

### Colorectal cancer + anal (Day 1, Thu Jan 8)

| Trial | Sponsor | Indication | Phase | Endpoint | Result | Practice-changing? |
|---|---|---|---|---|---|---|
| **BREAKWATER cohort 3** | Pfizer (Seagen) | 1L BRAF-V600E mCRC | 3 | OS / PFS / ORR | *mOS ~30.3 vs 15.1 mo (HR ~0.55); ORR improved with EC+FOLFIRI vs FOLFIRI+bev; data trending positive but immature* | Yes — new SOC for BRAF-V600E 1L mCRC; neuropathy-free vs FOLFOXIRI alternative |
| **CIRCULATE-NA (CCTG CRC.10 / NRG-GI008)** | NCI / CCTG / NRG | Resected colon cancer, ctDNA-guided adjuvant | 2/3 | DFS | Interim ctDNA assay performance + adjuvant-arm randomization update | Confirmatory — ctDNA-guided adjuvant design path |
| **ctDNA doubling time / presurgical ctDNA** | Multi-academic | Resected colon cancer correlatives | obs | Recurrence timing | ctDNA doubling time correlates with time to recurrence; presurgical ctDNA prognostic | Biomarker — feeds adjuvant trial design |
| **FOxTROT-2** | UK MRC | Elderly perioperative colon cancer | 3 | DFS / OS | Elderly-population perioperative FOLFOX feasibility + outcomes | TBD |
| **OrigAMI-1 mCRC update** | J&J | Amivantamab in MSS/EGFR-amp mCRC | 1b/2 | DoR / PFS | Durability update post-AACR 2025 | Read-through for EGFR×MET bispecific class in CRC |
| **POD1UM-303 / EA2176** | Incyte / ECOG-ACRIN | Retifanlimab maintenance, anal cancer | 3 | OS | Maintenance IO sequel in advanced SCCA | Possible — first IO maintenance OS in anal |

### Pancreatic, neuroendocrine, hepatobiliary, small-bowel (Day 2, Fri Jan 9)

| Trial | Sponsor | Indication | Phase | Endpoint | Result | Practice-changing? |
|---|---|---|---|---|---|---|
| **Daraxonrasib Phase 1/2 + combo update** | Revolution Medicines | 1L+ metastatic PDAC, RAS-mut | 1/2 | ORR / PFS / safety | Monotherapy + chemo-combo expansion; sets up Rasolute-302 Plenary LBA5 at ASCO 2026 | Foundation — pivotal Phase 3 OS readout at ASCO May 31 |
| **RMC-9805 (zoldonrasib) PDAC expansion** | Revolution Medicines | KRAS-G12D PDAC | 1 | ORR / DCR / ctDNA clearance | ORR 30%, DCR 80% in evaluable PDAC pts; 86% had >50% KRAS-G12D ctDNA decline; 39% achieved 100% clearance | Yes (early) — first selective G12D inhibitor with PDAC activity |
| **NETTER-2 / radioligand NET update** | Novartis | 1L well-differentiated GEP-NET | 3 | PFS | Lu-177 dotatate + LAR vs LAR follow-up | Confirmatory — earlier radioligand use in NET |
| **KEYNOTE-937** | Merck | Adjuvant HCC post-resection/ablation | 3 | RFS | **Negative** — pembrolizumab failed to improve RFS vs placebo | No — preserves SOC (active surveillance) |
| **TACTICS-L / atezo-bev vs TACE** | Roche / academic | Intermediate-stage HCC | 3 | Time to treatment failure | Atezo-bev > TACE on TTTF | Possible — challenges TACE as intermediate-HCC SOC |
| **REFOCUS — lirafugratinib** | Relay Therapeutics | FGFRi-naïve FGFR2-fusion CCA | 2 | ORR / DoR | ~100 pt Phase 2; durable responses, favorable safety vs pemigatinib/futibatinib | Yes (likely) — best-in-class FGFR2 selective TKI for CCA |
| **IDH1-mutant CCA combination** | Servier / multiple | IDH1-R132 mut CCA | 2 | ORR / PFS | Ivosidenib + chemo / IO combinations follow-up | Read-through for IDH1 second-generation strategies |

### Gastric / GEJ / esophageal (Day 3, Sat Jan 10)

| Trial | Sponsor | Indication | Phase | Endpoint | Result | Practice-changing? |
|---|---|---|---|---|---|---|
| **HERIZON-GEA-01** | Jazz Pharmaceuticals | 1L HER2+ locally advanced/metastatic G/GEJ adenocarcinoma | 3 | PFS / OS | Both zanidatamab + chemo and zanidatamab + tislelizumab + chemo show statistically significant PFS improvement vs trastuzumab + chemo; IO-containing arm shows OS gain | **Yes** — practice-changing in 1L HER2+ G/GEJ; FDA submission triggered Q1 2026 |
| **ILUSTRO follow-up** | Astellas | Claudin 18.2+ G/GEJ | 2 | ORR / DoR | Zolbetuximab monotherapy + combination durability update | Confirmatory — extends zolbetuximab label rationale |
| **CheckMate-577 long-term** | BMS | Adjuvant nivolumab post-CRT esophageal/GEJ | 3 | DFS / OS | Long-term DFS / OS update | Confirmatory — extends established adjuvant nivo SOC |
| **HER2 ADC esophageal** | Multiple (T-DXd, disitamab) | HER2+ esophageal / GEJ ADC follow-up | 2 | ORR / DoR | T-DXd + disitamab vedotin durability updates | Class read-through |

## Cross-cutting themes

To synthesize across `trials/` if/when populated:

1. **HER2+ G/GEJ — zanidatamab arrives.** HERIZON-GEA-01 is the practice-changing readout of the meeting. Trastuzumab + chemo is no longer the SOC reference frame in 1L HER2+ G/GEJ. FDA filing motion + payer / NCCN follow-on through 2026.
2. **KRAS-class drugs become real in PDAC.** Daraxonrasib (pan-RAS) Phase 1/2 update sets up Rasolute-302 Plenary at ASCO May 31. RMC-9805 / zoldonrasib (G12D-selective) PDAC activity is the next-class signal. Cross-link to AACR 2025/2026 RAS mechanism sessions and Revolution Medicines JPM 2026 presentation.
3. **BRAF-V600E mCRC moves to first-line.** BREAKWATER cohort 3 (EC + FOLFIRI vs FOLFIRI + bev) is the new 1L benchmark, displacing FOLFOXIRI + bev for biomarker-selected patients. Neuropathy-free profile is the practical edge.
4. **FGFR2-fusion CCA — second-generation TKIs.** Lirafugratinib (REFOCUS) vs pemigatinib / futibatinib SOC; selective FGFR2 sparing FGFR1 toxicity. Class differentiation by hyperphosphatemia / ocular AE profile.
5. **Adjuvant IO in HCC fails (KEYNOTE-937).** Preserves SOC. Bears on the broader perioperative-IO theme threading ASCO 2026 (KEYNOTE-B15 bladder, PROTEUS prostate, LIBRETTO-432 lung, ALCHEMIST).
6. **ctDNA-guided adjuvant designs mature.** CIRCULATE-NA + correlative ctDNA presurgical / doubling-time data continue the DYNAMIC / GALAXY thread; will feed next-cycle CRC adjuvant trial design.
7. **Anal cancer gets its first IO maintenance signal.** POD1UM-303 / EA2176 retifanlimab — small but real for a long-neglected disease.

## Status notes

- **Per-trial pages:** deferred (priority is ASCO main meeting May 29 – Jun 2). Backfill from JCO 4_suppl 2026 + ASCO Meeting Library on demand.
- **Discussant identities:** captured in `program-notes.md` where available from post-meeting recaps.
- **Forward cross-links to ASCO 2026 / AACR 2026:** wired in the master index above; per-trial pages should resolve them when written.
