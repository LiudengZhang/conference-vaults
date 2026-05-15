# EHA 2026

**31st EHA Hybrid Congress** — Stockholmsmässan, Stockholm, Sweden · June 11 – 14, 2026 (plus virtual platform). ~15,000+ attendees, the largest hematology meeting in Europe and the practice-changing readout venue six months ahead of [ASH 2026](../ash-2026/index.md).

> **Status:** Scaffold — meeting is **~1 month out** as of today (May 11, 2026). Regular abstracts release tomorrow (**May 12, 2026, 15:30 CEST**); late-breakers release **June 2, 2026, 15:30 CEST**. Structure is landing now so the pre-meeting prep, abstract-release ingest (May 12 onward), and live-coverage build (June 11–14) can run sequentially against a stable scaffold. Anything in this vault dated before May 12 abstract release is reconstructed from company toplines, EHA press-program previews, ASCO 2026 heme spillover, and analyst notes — flagged inline.

## Why this is in the vault

EHA is the **mid-year practice-changing readout venue for hematology in Europe** — six months ahead of ASH on the calendar and frequently the **first public reveal** for trials that then update at ASH in December. The relationship is asymmetric: most ASH 2026 plenary trials will have had a phase-2 or interim phase-3 readout at EHA 2026 first, with ASH carrying the longer follow-up. EHA owns the European cooperative-group studies (HOVON, GIMEMA, GELTAMO, GMLL, BSH) that don't always travel to ASH, plus a strong red-cell / hemoglobinopathy / non-malignant heme axis tied to European patient registries.

EHA is also a **load-bearing European regulatory signal** — readouts here feed CHMP / EMA filings the same way ASH readouts feed FDA. The 2026 venue (Stockholm) and the Nordic / Karolinska investigator network gives this year extra weight on **gene therapy for sickle cell and beta-thalassemia** (Karolinska is a Casgevy authorized treatment center) and **MDS / lower-risk MDS** (the Nordic MDS Group is a major cooperative-group voice).

**Format note (and the design decision behind this vault):** EHA, like ASH and ASCO, is **clinical, not tools-focused**. The per-tool template that loads the EuroBioC2025 / GBCC2025 / ISMB 2026 vaults does not fit here. The primary artifact for EHA 2026 is the **per-trial / per-readout** entry, identical in shape to ASH 2026 and ASCO 2026. See `trials/index.md` for the schema.

The closest sibling vaults are **[ASH 2026](../ash-2026/index.md)** (the December counterpart — same disease axes, same investigator network, same per-trial template) and **[ASCO 2026](../asco-2026/index.md)** (which precedes EHA by 1–2 weeks — May 29 – Jun 2, 2026 — and frequently shares heme readouts via parallel plenary slots). The EHA vault borrows the ASH "trials/ + themes + day-by-day digest" pattern verbatim; the only EHA-specific differentiator is the **European cooperative-group axis** (HOVON, GIMEMA, GELTAMO, EBMT registry data) and the **EMA / CHMP regulatory read-through**, which sit alongside the disease-axis tracks.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **EHA Congress program** | session grid, plenary slate, oral abstract schedule | [ehaweb.org/congress/eha2026-hybrid-congress](https://ehaweb.org/connect-network/eha2026-congress) |
| **EHA abstracts** (via *HemaSphere* supplement) | abstract full-text, available **May 12, 2026, 15:30 CEST** (regular); late-breakers **June 2, 2026, 15:30 CEST** | [HemaSphere journal](https://journals.lww.com/hemasphere/pages/default.aspx) — primary source for per-trial pages |
| **EHA press program** | embargoed media briefings; recordings + press releases tied to "Presidential Symposium" picks | EHA publishes a press-program preview ~late May |
| **EHA Learning Center** | post-meeting on-demand session library | [learningcenter.ehaweb.org](https://learningcenter.ehaweb.org/) — free to registrants |
| **The ASCO Post (heme coverage)** | weekly recap issues June–July 2026 | [ascopost.com](https://ascopost.com/) |
| **OncLive / Targeted Oncology / Healio HemOnc Today / CancerNetwork** | discussant-level depth, expert reaction video stand-ups | [onclive.com](https://www.onclive.com/), [targetedonc.com](https://www.targetedonc.com/), [healio.com/hematology-oncology](https://www.healio.com/hematology-oncology) |
| **Evaluate / ApexOnco / BioPharma Dive / Endpoints / STAT / Reuters / Bloomberg** | analyst framing, sponsor stock reactions, EMA filing read-through | sub-required for some |
| **Company press releases** | toplines (often pre-embargo), full presentation decks (post-presentation) | PRNewswire / BusinessWire / EU regulatory news syndication |
| **Presidential Symposium livestream + replay** | full talk video + discussant | EHA virtual platform; replay via Learning Center for registrants |
| **Social** | **#EHA2026** on X / Bluesky / LinkedIn | useful for real-time room reactions; not primary |

The **EHA abstracts in *HemaSphere* supplement is the load-bearing primary source** — every accepted abstract has a permalink with title, authors, affiliations, methods, results, and conclusions. Per-trial pages should cite the abstract DOI / *HemaSphere* permalink, not the company press release.

## Program shape

EHA 2026 runs **Thursday June 11 (opening) through Sunday June 14 (closing)**, four days. Stockholmsmässan, Älvsjö, Stockholm. Hybrid (in-person + virtual). The structure (per the EHA-standard pattern):

- **Presidential Symposium — Saturday June 13** (the practice-changing slot). Typically 6–8 top-scoring abstracts spanning malignant + non-malignant heme. Topics historically: practice-changing phase 3 readouts in DLBCL / MM / AML / CLL, plus one or two non-malignant or gene-therapy abstracts. Discussion follows each presentation.
- **Late-Breaking Abstracts session — Sunday June 14** (closing day). 8–10 LBAs released June 2; the most-watched of the meeting alongside the Presidential Symposium.
- **Plenary Abstracts sessions** (Friday + Saturday) — high-scoring abstracts second to the Presidential Symposium.
- **Oral Abstract Sessions** — ~300–400 oral presentations across disease axes and methodology tracks.
- **Educational Program** — disease-axis state-of-the-art talks; not data-presenting but heavily attended.
- **>3,000 abstracts total** (orals + posters + publication-only). [*expected per prior-year scale, subject to May 12 release*]
- **Tracks dominating the corpus:** Aggressive lymphoma (DLBCL, MCL), Indolent lymphoma + CLL, Myeloma, AML, ALL, MDS / MPN, CAR-T and cellular therapies, Bispecifics in heme, Gene therapies (sickle cell, beta-thalassemia, hemophilia), Thrombosis & Hemostasis, Red cell biology & hemoglobinopathies, Stem cell transplantation / EBMT.
- **Press program** (separate, embargoed media briefings) Thu–Sun mornings; "Best of EHA" recap follows the following week.

## Organization

```
conferences/eha-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep: tracks, presidential preview, expected LBAs, watch list, key dates
├── trials/              # PRIMARY artifact — one entry per trial / readout
│   └── index.md         # template + master trial index table
├── themes.md            # cross-day synthesis (deferred until post-meeting)
└── digest/              # day-by-day recap (deferred until post-meeting)
    ├── day-1-thursday.md  # Jun 11 — opening, education, first orals
    ├── day-2-friday.md    # Jun 12 — major oral sessions, plenary abstracts
    ├── day-3-saturday.md  # Jun 13 — PRESIDENTIAL SYMPOSIUM (load-bearing day)
    └── day-4-sunday.md    # Jun 14 — LATE-BREAKING ABSTRACTS + closing
```

The `trials/` directory is load-bearing. Each trial gets one Markdown file. Template at `trials/index.md`. Expected ~30–50 entries spanning the Presidential Symposium slate, Late-Breaking Abstracts, and the major track headliners (top DLBCL bispecifics, MM CAR-T pivots, AML menin / IDH / FLT3 updates, sickle cell gene-therapy real-world durability, European cooperative-group MDS / CLL trials).

## Anticipated big readouts (speculative, pre-abstract-release)

To be reconciled against the **May 12, 2026** abstract drop (tomorrow). As of May 11, 2026, **all of the following are flagged speculative** based on company pipelines, ASCO 2026 heme subset, AACR 2026 mechanism sessions, and prior-year EHA patterns:

1. **Bispecifics in DLBCL — 1L combinations + interim 3-yr durability.** Epcoritamab and glofitamab interim updates; EPCORE NHL-2 cohort updates; SUNMO and STARGLO follow-up; 1L combinations (epco-R-CHOP, glofit-Pola-R-CHP) interim. EHA frequently gets the interim readout; ASH gets the longer follow-up.
2. **Bispecifics + CAR-T in multiple myeloma.** MajesTEC-3 interim, MonumenTAL-3 interim, talquetamab and teclistamab European cohorts, RedirecTT-1 dual-bispecific in EMD myeloma updates, cilta-cel CARTITUDE-4 long-term, allogeneic anti-BCMA CAR-T early phase. The bispecific-vs-CAR-T sequencing question is centered on European real-world.
3. **CLL — pirtobrutinib and venetoclax fixed-duration European cohorts.** BRUIN CLL-321 European subset; GAIA / CLL13 follow-up (German CLL Study Group); FLAIR follow-up (UK); MAJIC. CLL is heavily represented at EHA via European cooperative groups.
4. **AML — menin, IDH, FLT3 + European cooperative-group studies.** Revumenib and ziftomenib post-approval European real-world; AML-Bridge / GMLL combinations; HOVON-AML maintenance studies; IDH inhibitor frontline data.
5. **Gene therapy for sickle cell disease and beta-thalassemia — European real-world.** Exa-cel (Casgevy) and lovo-cel (Lyfgenia) European treatment-center early experience; beta-thalassemia transfusion-independence durability; in-vivo base-edited next-gen approaches (Beam, Editas pipelines) early-phase. Stockholm venue gives Karolinska / Nordic data extra prominence.
6. **MDS — Nordic MDS Group cohorts + imetelstat / luspatercept European real-world.** Imetelstat post-approval European TI data; luspatercept COMMANDS European subset; IDH-mut MDS; IPSS-M-guided transplant in the EBMT registry.
7. **Hemophilia gene therapy — European durability + real-world.** Roctavian (val-rox) and Hemgenix (etranadez) European registry 2–4 year FIX/FVIII expression curves; Mim8 / concizumab / fitusiran European pivot updates.
8. **Red cell / hemoglobinopathy biology.** Mitapivat in sickle cell, thalassemia; etavopivat follow-up; PNH C5 vs C3 inhibitor combinations.

These eight clusters are the expected "spine" of the meeting. The Presidential Symposium + Late-Breakers will pull from clusters 1, 2, 4, and 5 most heavily.

## What's different from ASH

- **EHA is six months earlier in the calendar** (June vs December). The same trials often read out at EHA first with shorter follow-up and then update at ASH. EHA owns the "first interim" / "phase 2 mature" slot; ASH owns the "phase 3 longer follow-up" / "post-approval real-world" slot.
- **European cooperative-group studies are first-class at EHA** — HOVON (Dutch-Belgian), GIMEMA (Italian), GELTAMO (Spanish lymphoma), GMLL (German AML), German CLL Study Group, French LYSA / FILO / IFM, UK FLAIR / NCRI. ASH carries these as secondary; EHA carries them as primary.
- **EMA / CHMP regulatory read-through** is centered at EHA the way FDA read-through is centered at ASH. Watch for European-only approvals or label-expansions tied to EHA presentations.
- **Red-cell biology / non-malignant heme** is proportionally larger at EHA than ASH (though ASH still has the larger absolute count). Mitapivat, etavopivat, hemoglobinopathy gene therapy, PNH inhibitors are EHA-strong.
- **Abstract release timing.** Regular abstracts release **May 12 (~4 weeks pre-meeting)**; LBAs release **June 2 (~9 days pre-meeting)**. Shorter lead time than ASH; the analyst-preview cycle is more compressed.
- **EBMT registry** (European Society for Blood and Marrow Transplantation) is the European CIBMTR-analog and a major data source on transplant + CAR-T cohorts at EHA.

## Cross-vault links

- **[ASH 2026](../ash-2026/index.md)** — the December counterpart. Many EHA 2026 readouts will have an ASH 2026 update with longer follow-up. The `program-notes.md` for ASH 2026 already flags EHA reconciliation as a key pre-meeting step.
- **[ASCO 2026](../asco-2026/index.md)** — heme readouts at ASCO (May 29 – Jun 2) precede EHA by ~10 days. Several heme trials read out at both within the same fortnight (e.g., frontMIND DLBCL 1L on the ASCO 2026 LBA slate gets a parallel or interim treatment at EHA).
- **[AACR 2026](../aacr-2026/index.md)** — the mechanism / biomarker / discovery side of the same heme-cancer investigator network. Many EHA presenters had AACR 2026 mechanism sessions backing their trials (menin biology → revumenib/ziftomenib pivots; CAR-T construct engineering → durability readouts; base-editing platform → gene-therapy early phase).
- **[ESMO 2026](../esmo-2026/index.md)** — ESMO occasionally hosts heme readouts (rituximab follow-ups historically), but EHA is the dominant European venue for heme. Use ESMO 2026 mainly for IO read-through that bears on heme.
- **[JPM 2026](../jpm-2026/index.md)** — the financing / dealmaking layer. Multiple EHA 2026 sponsors were on the JPM stage in January (Gilead/Kite CAR-T pipeline, BMS cilta-cel + ide-cel, Genmab/AbbVie epcoritamab, Roche glofitamab, Vertex/CRISPR Casgevy, BioMarin Roctavian, Geron imetelstat, Servier IDH).
- **[Conferences timeline](../../timeline.md)** — EHA's position in the year's oncology cycle (AACR Apr → ASCO May/Jun → **EHA Jun** → ESMO Oct → ASH Dec → JPM Jan). EHA bookends the spring oncology cycle on the heme side; whatever lands here drives the ASH 2026 framing in the back half of the year.

## Next step

- **Now (T-1 day to abstract release, May 11, 2026):** populate `program-notes.md` with the expected-readout shortlist (anticipated phase 3 toplines, bispecific class watch list, gene-therapy durability watch list, CAR-T pivots, EU cooperative-group studies). Track company-disclosed toplines through Q1/Q2 2026 earnings calls and ASCO 2026 (May 29 – Jun 2) heme readouts that will set the EHA framing.
- **Abstract release (May 12, 2026, 15:30 CEST):** drop regular-abstract full-text into trial pages. Batch the priority shortlist first. Tomorrow is the load-bearing day for vault ingest.
- **LBA release (June 2, 2026, 15:30 CEST):** add Late-Breaking Abstracts. ~9 days pre-meeting, tight turnaround.
- **Live meeting (June 11 – 14, 2026):** real-time capture per day-digest. Saturday Presidential Symposium (Jun 13) + Sunday LBA (Jun 14) are the high-priority slots.
- **Post-meeting (June 15 – July 31, 2026):** finalize `themes.md`. Carry-forward to **ASH 2026** as "EHA-first, ASH-update" tags in `ash-2026/trials/`.

## Sources

- [EHA 2026 Congress home](https://ehaweb.org/connect-network/eha2026-congress)
- [EHA 2026 Details and deadlines](https://ehaweb.org/connect-network/eha2026-congress/eha2026-details-and-deadlines)
- [HemaSphere (EHA journal)](https://journals.lww.com/hemasphere/pages/default.aspx)
- [EHA Learning Center](https://learningcenter.ehaweb.org/)
- [The ASCO Post — Hematologic Malignancies](https://ascopost.com/specialty-pages/hematologic-malignancies/)
- [OncLive — Hematologic Malignancies](https://www.onclive.com/specialty/hematologic-malignancies)
- [Healio — Hematology / Oncology](https://www.healio.com/hematology-oncology)
- [ASH 2026 vault](../ash-2026/index.md) — the December counterpart that EHA readouts update into
