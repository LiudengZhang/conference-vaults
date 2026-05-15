# Trials — ASCO GU 2026

The primary artifact of this vault: **one Markdown file per trial / readout**. ASCO GU is a clinical-readout meeting, and — unlike ASCO main, where the Plenary is the singular load-bearing event — every day of GU has a practice-changing entry. Per-trial pages are the right unit.

> **Status:** Template + master index built post-meeting (today: May 11, 2026 — 10 weeks after the Feb 26–28 symposium). Per-trial detail pages will be populated from the ASCO Meeting Library abstracts + post-meeting trade-press recaps. Pre-stub entries below are reconstructed from public coverage; numerical results are flagged with their source and will be reconciled against the abstract permalink when each detail page is built. Trials whose ASCO GU readout was interim and whose mature data is expected at ASCO 2026 main meeting (May 29 – Jun 2) or ESMO 2026 (Oct 23 – 27) are flagged `*forward-looking*`.

## Per-trial template

Each trial file (e.g., `keynote-b15.md`) follows this schema. Copy and fill:

```markdown
# <Trial acronym / name> — <Drug regimen, indication, line>

> **Abstract:** <abstract #, e.g., LBA630> · **Session:** <session name, date, time PT, hall> · **Embargo:** <date lifted>

## At a glance

- **Sponsor:** <pharma / cooperative group>
- **PI / presenter:** <name, institution>
- **NCT ID:** <NCTxxxxxxxx>
- **Phase:** <1 / 2 / 3 / 2-3>
- **Design:** <arms, randomization, blinding>
- **N:** <enrolled / analyzed>
- **Primary endpoint(s):** <PFS / OS / EFS / DFS / ORR / pCR / rPFS / MFS / BI-EFS>
- **Comparator:** <SOC / placebo / active comparator>
- **Indication:** <tumor type, subtype, biomarker selection — be specific (e.g., HRR-altered mCRPC, PD-L1+ MIBC)>
- **Line:** <neoadjuvant / adjuvant / 1L / 2L / 3L+ / perioperative / mHSPC / mCRPC>

## Headline result

<One paragraph. Numbers + HR + p-value as presented. Cite the abstract permalink, not the company press release. If interim, flag `*OS / mature follow-up expected at <ASCO main / ESMO / SUO>*`.>

## Mechanism / class

<Drug class, target, prior approvals if any. Cross-link to related AACR mechanism sessions or JPM sponsor pipeline pages.>

## Discussant takeaway

<Named discussant + key framing. ASCO GU assigns senior figures in the relevant
disease group; the discussant's framing typically defines the post-meeting
narrative until the next major update.>

## Practice-changing?

<Yes / no / pending, with rationale: NCCN guideline implications, FDA filing path,
unmet need, prior SOC. Note that ASCO GU readouts often trigger NCCN updates
within 60-90 days of the meeting.>

## Cross-links

- **ASCO 2026 main:** <related Plenary / session / OS follow-up entry, if applicable>
- **AACR 2026:** <related mechanism session / preclinical work>
- **AACR 2025:** <prior-year mechanism / biomarker work>
- **Other ASCO GU 2026 trials:** <same class, same indication>
- **JPM 2026:** <sponsor presentation / deal>
- **ESMO 2025 / 2026:** <prior or expected follow-up readout>

## Sources

- ASCO Meeting Library abstract: <URL>
- Company press release: <URL>
- Trade-press recap: <OncLive / Targeted Oncology / Cancer Therapy Advisor / Renal & Urology News URL>
- ClinicalTrials.gov: <NCT URL>
```

## Master trial index

The post-meeting shortlist for detail-page creation. **All numerical entries below are reconstructed from post-meeting trade-press coverage** (OncLive "Experts Recount", Targeted Oncology preview, OncoDaily roundup, MedDataX summary) — to be reconciled against the ASCO Meeting Library abstract when each detail page is built.

### Renal Cell Carcinoma (Day 1 — Thu Feb 26)

| Trial | Abstract | Sponsor | Indication | Phase | Endpoint | Result | Practice-changing? |
|---|---|---|---|---|---|---|---|
| **LITESPARK-022** | LBA418 | Merck | Adjuvant high-risk clear cell RCC (post-nephrectomy) | 3 | DFS | DFS HR 0.72 (95% CI 0.59–0.87, p=0.0003) for pembro + belzutifan vs pembro mono | **Yes — sNDA already under FDA priority review** at time of GU readout (Feb 2026). First HIF-2α + IO adjuvant combo. |
| **LITESPARK-011** | LBA417 | Merck | 2L+ metastatic ccRCC (post-IO/TKI) | 3 | PFS / OS | Belzutifan + lenvatinib vs cabozantinib; result mixed per Motzer presentation — *details to reconcile against Meeting Library* | Pending — class read-through for HIF-2α + VEGF |
| **CYTOSHRINK** | Oral | Cooperative group | Metastatic RCC | 2 | PFS | SBRT + nivo/ipi vs nivo/ipi alone — neoantigen-release hypothesis | Exploratory; signal-generating |

### Urothelial / Bladder (Day 2 — Fri Feb 27)

| Trial | Abstract | Sponsor | Indication | Phase | Endpoint | Result | Practice-changing? |
|---|---|---|---|---|---|---|---|
| **KEYNOTE-B15 / EV-304** | LBA630 | Merck + Pfizer/Astellas | Perioperative MIBC, cisplatin-eligible | 3 | EFS / pCR / OS | EFS HR 0.53 (95% CI 0.41–0.70, p<0.001); 24-mo OS 86.9% vs 81.3% for EV+pembro vs gem/cis | **Yes — displaces cisplatin in curative-intent perioperative MIBC**. *Forward-looking: OS-mature update expected at ASCO 2026 main meeting (May 29 – Jun 2).* |
| **IMvigor011** | Oral | Roche/Genentech | Adjuvant MIBC, ctDNA-positive | 3 | DFS | ctDNA-guided atezo vs observation in ctDNA+ post-cystectomy — *positive per topline* | Yes — establishes ctDNA-guided adjuvant as deployable, not just theoretical |
| **NIAGARA biomarker analyses** | Oral | AstraZeneca | Perioperative MIBC | 3 (sub-analysis) | ctDNA dynamics / urine tumor DNA | Biomarker sub-analysis from positive NIAGARA durvalumab trial | Confirms dynamic ctDNA surveillance role |
| **SunRISE-2** | Oral | Johnson & Johnson | MIBC alternative to chemoradiotherapy | — | BI-EFS | **Missed primary BI-EFS endpoint**; CR rates compelling enough to warrant further study per investigators | No — primary miss; signal-only |

### Prostate (Day 3 — Sat Feb 28)

| Trial | Abstract | Sponsor | Indication | Phase | Endpoint | Result | Practice-changing? |
|---|---|---|---|---|---|---|---|
| **PEACE-3 / EORTC 1333** | Oral | EORTC | Bone-mets mCRPC (1L post-ARPI) | 3 | OS | OS HR 0.76 (95% CI 0.60–0.96, one-sided p=0.0096) for enza + Ra-223 vs enza alone | **Yes — re-validates alpha-emitter combo with modern bone protection**. Follow-up to rPFS readout at ESMO 2024. |
| **PSMAaddition** | Oral | Novartis | 1L metastatic hormone-sensitive prostate (mHSPC) | 3 | rPFS / OS | ¹⁷⁷Lu-PSMA-617 + ADT + ARPI vs ADT + ARPI — *positive rPFS per topline; OS interim* | **Yes — moves RLT from 3L+ (per VISION) to 1L mHSPC**. *Forward-looking: OS mature follow-up at ASCO main meeting or ESMO 2026.* |
| **MEVPRO-3** | Oral | Pfizer | mCRPC | 3 | rPFS | Mevrometostat (selective EZH2i) + enza vs enza — Ph1 showed rPFS 14.3 vs 6.2 mo; Ph3 readout interim | Pending — Ph1 signal striking; Ph3 confirmation watched |
| **BRCAAway** | Oral | Cooperative group | HRR-altered mCRPC | 2 | PFS | PARPi + ARPI combination (vs sequential) | Tests upfront combo vs sequential PARPi/ARPI |
| **CAPItello-281** | Oral | AstraZeneca | PTEN-deficient mHSPC | 3 | rPFS / OS | Capivasertib + abi vs placebo + abi — *positive per topline; PRO assessments emphasized* | Yes if confirmed — first PTEN-biomarker-selected Ph3 in mHSPC |
| **²²⁵Ac-PSMA first-in-human** | Oral | Investigator-initiated | mCRPC (post-¹⁷⁷Lu-PSMA) | 1 | Safety / activity (dose escalation) | Alpha-emitter PSMA, presented by Fred Saad | Early — signal-generating for alpha-emitter PSMA class |

### Rare GU (testicular, penile, adrenal — across days)

| Trial | Abstract | Sponsor | Indication | Phase | Endpoint | Result | Practice-changing? |
|---|---|---|---|---|---|---|---|
| **InPACT** | Oral | International cooperative | Locally advanced penile cancer | 3 | OS / EFS | Neoadjuvant chemo vs chemoradiation — *details to reconcile* | Pending — rare disease, small trials |
| **Testicular GCT updates** | Various | Various | Relapsed testicular germ cell tumor | 1–2 | ORR | Salvage HD chemo + novel agent combos | Incremental |
| **Adrenocortical carcinoma** | Poster | Various | mACC | 2 | ORR / PFS | IO + mitotane / TKI combos | Signal-generating; rare-disease updates |

## Cross-cutting themes

Themes to fold into trial-page "cross-links" sections (no standalone themes.md given the 3-day program):

1. **HIF-2α moves to adjuvant + 2L.** LITESPARK-022 DFS positive (adjuvant) + LITESPARK-011 (2L belzutifan + lenva) define belzutifan's expansion beyond VHL / 3L mRCC. Cross-link to AACR 2025 / 2026 HIF-2α mechanism work.
2. **ctDNA-guided adjuvant is real.** IMvigor011 (atezo, MIBC) + NIAGARA biomarker analyses (durva, MIBC) establish dynamic ctDNA surveillance as deployable. Cross-link to bladder ADC / IO entries.
3. **Perioperative IO+ADC displaces cisplatin in MIBC.** KEYNOTE-B15 / EV-304 EFS HR 0.53 is the practice-changing moment for MIBC. *Forward-looking: ASCO 2026 main-meeting OS update expected.*
4. **Radioligands expand into earlier prostate lines.** PSMAaddition (1L mHSPC ¹⁷⁷Lu-PSMA) + PEACE-3 (enza + Ra-223 mCRPC OS) + ²²⁵Ac-PSMA first-in-human define the RLT prostate roadmap from 1L mHSPC → mCRPC → post-¹⁷⁷Lu salvage.
5. **PARPi + ARPI upfront combos.** BRCAAway (HRR-altered mCRPC) tests upfront vs sequential; CAPItello-281 (capivasertib + abi PTEN-deficient mHSPC) extends the biomarker-selected combo logic to AKT pathway.
6. **Sibling to ASCO main meeting.** PROTEUS (apalutamide perioperative HRLPC) on the ASCO main Plenary LBA1 slot in May is the ASCO-main GU headliner; it complements the ASCO GU 2026 prostate slate (PEACE-3 mCRPC, PSMAaddition mHSPC, CAPItello-281 mHSPC) by covering the localized / perioperative HRLPC space that GU did not own this year.

## Forward-looking flags

- **ASCO 2026 main meeting (May 29 – Jun 2):** PROTEUS LBA1 (perioperative HRLPC); KEYNOTE-B15 OS-mature update expected; PEACE-3 bone-mets subgroup follow-up; LITESPARK-022 OS-interim.
- **ESMO 2026 (Oct 23 – 27):** typical venue for OS-mature follow-up of GU trials whose primary DFS / PFS endpoint hit at GU. Reconcile post-ESMO.
- **SUO 2026 (Dec):** surgical-oncology perspective on perioperative MIBC and prostate trials.

## Sources

- [ASCO Meeting Library](https://meetings.asco.org/) — primary source for all per-trial abstract permalinks
- [OncoDaily — ASCO GU 2026: 10 Most Promising Trials](https://oncodaily.com/trial-updates/asco-gu-2026)
- [OncLive — Experts Recount the Most Notable Data From the 2026 GU Cancers Symposium](https://www.onclive.com/view/experts-recount-the-most-notable-data-from-the-2026-genitourinary-cancers-symposium)
- [Targeted Oncology — ASCO GU 2026 Preview: Highlights of Key Trials](https://www.targetedonc.com/view/asco-gu-2026-preview-highlights-of-key-trials-in-bladder-kidney-prostate-and-rare-cancers)
- [MedDataX — Key Trial Data Presented at 2026 ASCO GU](https://meddatax.com/news/2026-asco-gu-symposium-trial-results)
- [Renal & Urology News — ASCO GU 2026: 6 Key Takeaways](https://www.renalandurologynews.com/features/asco-gu-2026-6-takeaways/)
- [Cancer Therapy Advisor — ASCO GU 2026 to Highlight the Latest Developments](https://www.cancertherapyadvisor.com/reports/asco-gu-2026-to-highlight-the-latest-developments-in-genitourinary-cancer/)
- [UroToday — ASCO GU 2026 conference highlights](https://www.urotoday.com/conference-highlights/asco-gu-2026/)
- [Merck press release — bladder and kidney cancer data at 2026 ASCO GU](https://www.urotoday.com/conference-highlights/asco-gu-2026/asco-gu-2026-press-releases/166586-merck-advances-treatment-of-bladder-and-kidney-cancers-with-new-data-at-2026-asco-gu-cancers-symposium.html)
