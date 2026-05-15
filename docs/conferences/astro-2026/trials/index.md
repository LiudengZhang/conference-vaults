# Trials — ASTRO 2026

The primary artifact of this vault: **one Markdown file per trial / readout**. ASTRO 2026 is a clinical-readout meeting where the contested variable is usually **modality, dose, fractionation, or volume** rather than drug-vs-comparator. The unit of analysis is the trial — not the device, not the vendor, not the speaker.

> **Status:** Template + master index. Per-trial pages will be populated as the program grid is finalized (late summer) and as embargoes lift in stages around the meeting (Sep 26–30, 2026). The Plenary slate (3–5 top-rated abstracts) is announced approximately 4–6 weeks pre-meeting. LBAs release on the morning of presentation. Anything in this index dated before its embargo lift is built from company / cooperative-group toplines, abstract titles, and analyst previews — flagged inline.

## Per-trial template

Each trial file (e.g., `nrg-gu005-update.md`) follows this schema. Copy and fill:

```markdown
# <Trial acronym / name> — <Modality, indication, key variable>

> **Abstract:** <abstract # / LBA #> · **Session:** <session name, date, time ET, room> · **Embargo:** <date>

## At a glance

- **Sponsor / cooperative group:** <NRG / RTOG-F / EORTC / industry / academic-led>
- **PI / presenter:** <name, institution>
- **NCT ID:** <NCTxxxxxxxx>
- **Phase:** <1 / 2 / 2R / 3>
- **Design:** <arms, randomization, blinding>
- **N:** <enrolled / analyzed>
- **Primary endpoint(s):** <OS / PFS / LRC / DFS / toxicity / QoL / pCR>
- **Comparator:** <SOC fractionation / SOC modality / observation / chemo-only>
- **Indication:** <tumor type, stage, risk group>
- **Treatment intent:** <definitive / adjuvant / neoadjuvant / palliative / oligometastatic ablation / re-irradiation>

## Radiation specifics

- **Modality:** <3D-CRT / IMRT / VMAT / SBRT / SABR / proton (PBS / passive) / carbon-ion / MR-linac / FLASH / brachytherapy / radioligand>
- **Dose / fractionation:** <total dose Gy / # fractions / Gy-per-fraction; α/β if specified>
- **Target volume(s):** <GTV / CTV / PTV definitions>
- **Plan-evaluation method:** <DVH constraints / Monte Carlo / TPS used>
- **Image guidance:** <CBCT / MR-linac / surface guidance>
- **Adaptive workflow:** <none / offline / online / daily>
- **AI tooling used:** <auto-contouring tool / dose-prediction model / synthetic-CT / none>

## Headline result

<One paragraph. Numbers + HR + p-value if known. If pre-embargo, mark
`*expected per <source> topline <date>*`. For radiation trials,
prioritize **locoregional control, toxicity, QoL**, then survival.>

## Mechanism / rationale

<Why this dose / volume / modality. Cite the dose-response / biological-modeling /
prior phase 2 work. Cross-link to AACR radiation-biology if relevant.>

## Discussant takeaway

<Named discussant + key framing once known. ASTRO discussants typically come from
the disease-specific committee; identity is a signal.>

## Practice-changing?

<Yes / no / pending, with rationale: NCCN guideline implications, ASTRO clinical
practice statement path, payer / Medicare LCD implications (for proton / FLASH /
SBRT fractionation), unmet need, prior SOC.>

## Cross-links

- **ASCO 2026:** <related systemic-arm trial in same disease, if applicable>
- **ESMO 2026:** <related European cooperative-group readout>
- **AACR 2026:** <prior-year radiogenomics / immuno-RT mechanism session>
- **Other ASTRO 2026 trials:** <same modality / same disease / same cooperative group>
- **RSNA 2026 / MICCAI 2026 tools:** <if a named auto-contouring / dose-prediction model anchored the workflow>
- **JPM 2026:** <vendor presentation / deal — Elekta, Varian, ViewRay, RaySearch, FLASH player>

## Sources

- ASTRO Meeting Library (amportal) abstract: <URL or "pending embargo">
- Red Journal companion publication: <DOI or "pending">
- ASTRO Daily News recap: <URL>
- Cooperative-group / sponsor press release: <URL>
- Trade-press recap (OncLive / ASCO Post / Cancer Letter): <URL>
- ClinicalTrials.gov: <NCT URL>
```

## Master trial index

The shortlist for pre-meeting stub creation. All numbers below are **pre-embargo, sourced from cooperative-group quarterly updates, sponsor / device-vendor toplines, ASTRO press kits (2025 carryover where relevant), and "Predict the Plenary"–style preview pieces** — to be reconciled with the official abstract / presentation. **`Result` column entries marked italic are speculative / topline only.**

| Trial | Sponsor / Co-op | Indication | Modality / Variable | Phase | Endpoint | Result (pre-embargo) | AI-tool flag | Practice-changing? |
|---|---|---|---|---|---|---|---|---|
| **NRG-GU005 long-term** | NRG | Intermediate-risk localized prostate | SBRT 36.25 Gy / 5 fx vs moderate hypofractionation | 3 | QoL, biochemical control | *5-yr data update following 2-yr positive QoL+BC at ASTRO 2025* | Auto-contouring varies by site | Likely — consolidates 5-fx SBRT as SOC |
| **RADCOMP cardiac follow-up** | NRG / Penn | Non-metastatic breast (post-mastectomy / regional nodal RT-eligible) | Proton vs photon | 3 | MACE (3-yr); locoregional recurrence | *Primary MACE readout presented ASTRO 2025; 2026 likely longer-term + subgroup* | — | Pending — payer-coverage implications for breast proton |
| **PROTECT** | RTOG-F / international | Resectable / locally advanced esophageal | Proton vs photon (concurrent chemo) | 3 | Toxicity composite, OS | *expected, subject to embargo* | — | Yes if positive — esophageal proton coverage |
| **TORPEdO follow-up** | CRUK | Oropharyngeal (intermediate/advanced) | Proton vs IMRT | 3 | Toxicity reduction, QoL | *Phase 3 readout at ASTRO 2025 (PL-01); 2026 long-term + subgroup* | — | Pending — H&N proton policy |
| **SABR-COMET-10** | Canadian / international | Oligometastatic solid tumors (4–10 lesions) | SABR to all lesions + SOC vs SOC | 3 | OS | *expected, subject to embargo* | — | Possibly — extends SABR-COMET to 4–10 mets |
| **PACIFIC-9 / PACIFIC-R successor** | AZ / cooperative | Unresectable stage III NSCLC | chemo-RT + IO + add-on vs chemo-RT + durva | 3 | PFS, OS | *expected, subject to embargo* | — | Possibly — first PACIFIC successor since 2017 |
| **NRG-LU007** | NRG | Limited-stage SCLC | TRT fractionation + IO consolidation | 2/3 | PFS, OS | *expected; cross-link ASCO 2026 TRIPLEX LBA8005* | — | Pending |
| **FAST-02 / FAST-01 follow-up** | Cincinnati / Varian | Bone metastases (FLASH first-in-human) | FLASH proton vs conventional proton (8 Gy single fx) | 1/2 | Pain response, feasibility | *FAST-01 feasibility 2024; FAST-02 expanded sites — 2026 readout expected* | — | Class-defining for FLASH if positive |
| **EMPOWER / single-fx WBI** | UK / cooperative | Early-stage breast (post-lumpectomy) | Single-fx vs multi-fx WBI | 3 | Local recurrence, cosmesis | *expected, subject to embargo* | — | Possibly — extends FAST-FORWARD logic |
| **POSTILV** | EORTC / cooperative | Post-prostatectomy adverse-feature | Adjuvant vs early-salvage RT (long-term) | 3 | bDFS, MFS | *expected; cross-link to RAVES/RADICALS-RT meta* | — | Confirmatory |
| **SAKK 09/10 successor** | SAKK | Post-prostatectomy salvage | Dose-escalation salvage RT | 3 | bDFS | *expected, subject to embargo* | — | Pending |
| **HYPRO long-term** | Dutch / EORTC | Intermediate / high-risk prostate | Moderate hypofractionation 10-year | 3 | Failure-free survival, late toxicity | *expected; long-term confirmatory* | — | Confirmatory |
| **ARTNET / MR-linac adaptive** | Multi-center consortium | Pancreatic SBRT, oligo-met, prostate | Online-adaptive MR-linac (Unity / MRIdian) | 2 | Plan quality, toxicity | *expected; multiple per-site readouts* | Adaptive-replanning AI flagged | Workflow-defining for MR-linac SOC |
| **CC-486 / NRG-CC008** | NRG | Hippocampal-sparing WBRT | HA-WBRT + memantine vs SRS | 3 | Cognitive decline | *expected; extends NRG-CC001* | Auto-contouring of hippocampus is critical | Pending |
| **RT + IO immuno-RT mechanism** | Various academic | Multiple — NSCLC, melanoma, GU | Abscopal trials + biomarker | 1/2 | Response, immune signature | *Multiple early-phase readouts; cross-link AACR 2026 radiation-immunology* | — | Mechanism / hypothesis-generating |

**Additional shortlist candidates** to stub post-embargo:

- **GU:** PSMA-directed re-irradiation; STAMPEDE-2 RT-arm subgroups; oligo-progression PSMA-guided ablation; brachytherapy + EBRT (ASCENDE-RT 10-yr).
- **Lung:** Stage I NSCLC SBRT (RTOG-F successor to RTOG 0813 / 0915); pre-op SBRT + IO neoadjuvant; PACIFIC subgroups.
- **Breast:** APBI 5-fx (FAST-FORWARD partial-breast); regional-nodal hypofractionation (RT CHARM follow-up); skip-RT after neoadjuvant pCR (NSABP B-51 / NRG-RT-005).
- **CNS:** Post-op cavity SRS fractionation; leptomeningeal proton CSI; pediatric craniospinal proton long-term.
- **GI:** Anal canal de-escalation (PLATO follow-up); rectal TNT non-operative (OPRA / RAPIDO long-term); pancreatic SBRT MR-linac.
- **H&N:** HPV+ de-escalation (NRG-HN005 follow-up, MC1675 / MC1273); re-irradiation registry.
- **Technology / AI:** Auto-contouring validation (Limbus / MIM / Siemens AI-Rad); synthetic-CT MR-only workflows; dose-prediction GANs; Ethos adaptive online workflow; carbon-ion (NIRS / Heidelberg) outcomes.

## AI-tools secondary track (cross-link table)

ASTRO 2026 will host a meaningful but secondary AI-in-treatment-planning track. These don't get standalone tool pages here — they're cross-linked to the matching dossiers at RSNA / MICCAI. When a named tool anchors an ASTRO trial workflow, log it in that trial's `## Radiation specifics → AI tooling used` field and link out.

| Tool / Method | Use case | RSNA 2026 dossier | MICCAI 2026 dossier |
|---|---|---|---|
| TotalSegmentator-RT | Auto-contouring of OARs (CT) | cross-link | cross-link |
| MedSAM / SegVol | Promptable segmentation for target volumes | cross-link | cross-link |
| Limbus AI Contour | Commercial OAR auto-contouring | cross-link | — |
| Synthetic-CT GANs (e.g., MR-only workflow) | MR-only treatment planning | cross-link | cross-link |
| Dose-prediction CNNs | KBP / automated planning | — | cross-link |
| Ethos Intelligent Optimization Engine | Varian online-adaptive workflow AI | — | — |
| Elekta Unity online-adaptive ML | Per-fraction re-planning on MR-linac | — | — |

If the post-meeting corpus warrants it, this table promotes to a standalone `tools/index.md` directory.

## Cross-cutting themes (for post-meeting `themes.md`)

To synthesize across `trials/` once populated:

1. **SBRT fractionation consolidation.** 5-fx SBRT for intermediate-risk prostate (NRG-GU005 long-term), 5-fx ultra-hypofractionated WBI (FAST-FORWARD / EMPOWER), single-fx bone-met / FLASH (FAST-02). The fractionation curve continues to drop.
2. **Proton vs photon — the payer question.** RADCOMP (breast), TORPEdO (H&N), PROTECT (esophageal). Each readout is also a Medicare LCD / commercial-payer coverage event.
3. **MR-linac workflow maturation.** Online-adaptive (Unity / MRIdian) moves from feasibility to outcomes in pancreas, oligo-met, prostate. Vendor-led commercial story (Elekta / ViewRay) overlaps with the trial readouts — cross-link to JPM 2026 vendor pages.
4. **FLASH-RT first-in-human expansion.** FAST-02 (bone mets) is the watch. If FLASH-RT clears phase 1/2 safety in a second site, the field shifts from "interesting physics" to "next-decade modality."
5. **Oligometastatic ablation as a discipline.** SABR-COMET-10 (4–10 mets), oligo-progression-guided treatment, PSMA-directed re-irradiation. The field is defining its own clinical category separate from definitive vs palliative.
6. **Immuno-RT — mechanism over outcome.** RT + IO trials continue to surface, but the big OS swing remains elusive outside specific contexts. Biomarker-driven trials (NRG-LU007 type designs) are the watch.
7. **AI in planning is plumbing, not headline.** Auto-contouring, dose-prediction, synthetic-CT — all moving to routine use. Few standalone "AI trial" Plenary readouts; the AI shows up as workflow inside other trials.
8. **Re-irradiation as a sub-discipline.** Multi-disease re-RT registries (H&N, prostate PSMA-directed, recurrent gliomas) consolidate into clinical guidance.
