# ASH 2026

**68th ASH Annual Meeting & Exposition** — Ernest N. Morial Convention Center, New Orleans, LA · December 12 – 15, 2026 (plus online platform). ~30,000 attendees, the largest hematology meeting of the year.

> **Status:** Scaffold — meeting is **~7 months out** as of today (May 11, 2026). Structure is landing now so that pre-meeting prep (topline tracking through summer/fall 2026), abstract-release ingest (regular abstracts Nov 4, 2026, 9:00 AM ET; late-breakers ~late Nov 2026), and live-coverage build (Dec 12–15) can run sequentially against a stable scaffold. Anything in this vault dated before Nov 4 abstract release is reconstructed from company toplines, ASH press-program previews, and analyst notes — flagged inline.

## Why this is in the vault

ASH is the **practice-changing readout venue for hematologic malignancies and non-malignant heme**. It is the clinical-translation counterpart to [AACR 2026](../aacr-2026/index.md) for the heme-cancer subset — same investigators, one or two phases later. AACR shows the mechanism (menin-MLL biology, CAR-T construct design, gene-editing platform), ASH shows whether it works in patients at randomized or pivotal single-arm scale. Strong overlap with AACR's clinical-trials axis: heme cancers (DLBCL, AML, MM, CLL, MDS) are a major AACR subset, and many ASH 2026 presenters had AACR 2025/2026 mechanism sessions backing their trials.

ASH is also the **cell-and-gene-therapy mothership** — CAR-T durability data, allogeneic CAR-T pivotal readouts, gene-edited therapies for sickle cell and beta-thalassemia, and gene therapy for hemophilia all converge here. The bispecific-T-cell-engager class story (DLBCL, MM, AML) also matures at ASH each year.

**Format note (and the design decision behind this vault):** ASH is **clinical, not tools-focused**. The per-tool template that loads the EuroBioC2025 / GBCC2025 / ISMB 2026 vaults does not fit here — there are no Bioconductor packages debuting on the ASH plenary stage. The primary artifact for ASH 2026 is the **per-trial / per-readout** entry, identical in shape to ASCO 2026 and ESMO 2026. See `trials/index.md` for the schema.

The closest sibling vaults are **[ASCO 2026](../asco-2026/index.md)** and **[ESMO 2026](../esmo-2026/index.md)** — also clinical, also trial-indexed, also embargo-driven. The ASH vault borrows the ASCO "trials/ + themes + day-by-day digest" pattern verbatim; the only ASH-specific differentiator is the **cell-and-gene-therapy sub-track**, which sits alongside the disease-axis tracks (DLBCL, AML, MM, CLL, MDS) rather than slicing across them.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **ASH Annual Meeting program** | session grid, plenary slate, oral abstract schedule | [hematology.org/meetings/annual-meeting](https://www.hematology.org/meetings/annual-meeting) |
| **ASH abstracts** (via *Blood* supplement) | abstract full-text, available **Nov 4, 2026, 9:00 AM ET** (regular); late-breakers ~late Nov | [ashpublications.org/blood](https://ashpublications.org/blood) — primary source for per-trial pages |
| **ASH press program** | embargoed media briefings; recordings + press releases tied to "Best of ASH" picks | ASH publishes a press-program preview ~Oct/Nov |
| **ASH Clinical News** | first-pass post-session recaps, official ASH editorial | [ashclinicalnews.org](https://ashclinicalnews.org/) |
| **The ASCO Post (heme coverage)** | weekly recap issues Dec 2026 – Feb 2027 | [ascopost.com](https://ascopost.com/) |
| **OncLive / Targeted Oncology / Healio HemOnc Today / CancerNetwork** | discussant-level depth, expert reaction video stand-ups | [onclive.com](https://www.onclive.com/), [targetedonc.com](https://www.targetedonc.com/), [healio.com/hematology-oncology](https://www.healio.com/hematology-oncology) |
| **Evaluate / ApexOnco / BioPharma Dive / Endpoints / STAT** | analyst framing, sponsor stock reactions, M&A read-through | sub-required for some |
| **Company press releases** | toplines (often pre-embargo), full presentation decks (post-presentation) | PRNewswire / BusinessWire syndication |
| **Plenary livestream + replay** | full talk video + discussant | ASH virtual platform; replay free for registrants |
| **Social** | #ASH26 on X / Bluesky | useful for real-time room reactions; not primary |

The **ASH abstracts in *Blood* supplement is the load-bearing primary source** — every accepted abstract has a permalink with title, authors, affiliations, methods, results, and conclusions. Per-trial pages should cite the abstract DOI / *Blood* supplement permalink, not the company press release.

## Program shape

ASH 2026 runs **Saturday December 12 (opening) through Tuesday December 15 (closing)**, four days plus pre-meeting workshops Thursday–Friday Dec 10–11. Ernest N. Morial Convention Center, New Orleans. Hybrid (in-person + virtual). The structure (per the ASH-standard pattern):

- **Plenary Scientific Session — Sunday Dec 13** (the practice-changing slot). Typically 6 abstracts spanning malignant + non-malignant heme. Topics historically: practice-changing phase 3 readouts in DLBCL / MM / AML, plus one or two non-malignant or gene-therapy abstracts. Discussion follows each presentation.
- **Late-Breaking Abstracts session — Tuesday Dec 15** (closing). 6–8 LBAs released ~late Nov; the most-watched of the meeting after the Plenary.
- **Oral Abstract Sessions** — ~600 oral presentations across disease axes and methodology tracks.
- **Education Program** (Sat morning + Sun morning) — disease-axis state-of-the-art talks; not data-presenting but heavily attended.
- **>5,000 abstracts total** (orals + posters + publication-only).
- **Tracks dominating the corpus:** Lymphoma (DLBCL, FL, MCL, CLL), Myeloma, Acute Leukemias (AML, ALL), MDS / MPN, CAR-T and cellular therapies, Bispecifics in heme, Gene therapies (sickle cell, beta-thalassemia, hemophilia), Thrombosis & Hemostasis, Bone Marrow Failure & Aplastic Anemia, Transplantation.
- **Press program** (separate, embargoed media briefings) Sat–Tue mornings; "Best of ASH" recap typically the following weekend.

## Organization

```
conferences/ash-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep: tracks, plenary preview, expected LBAs, watch list, key dates
├── trials/              # PRIMARY artifact — one entry per trial / readout
│   └── index.md         # template + master trial index table
├── themes.md            # cross-day synthesis (deferred until post-meeting)
└── digest/              # day-by-day recap (deferred until post-meeting)
    ├── day-1-saturday.md   # Dec 12 — opening, education, first orals
    ├── day-2-sunday.md     # Dec 13 — PLENARY (load-bearing day)
    ├── day-3-monday.md     # Dec 14 — major oral sessions, CAR-T / bispecific / gene-therapy tracks
    └── day-4-tuesday.md    # Dec 15 — LATE-BREAKING ABSTRACTS + closing
```

The `trials/` directory is load-bearing. Each trial gets one Markdown file. Template at `trials/index.md`. Expected ~40–70 entries spanning the Plenary slate, Late-Breaking Abstracts, and the major track headliners (top DLBCL bispecifics, MM CAR-T pivots, AML menin / IDH / FLT3 updates, sickle cell gene-therapy real-world durability, MDS / lower-risk-MDS pivots).

## Anticipated big readouts (speculative, pre-abstract-release)

To be reconciled against the Nov 4 abstract drop. As of May 2026, **all of the following are flagged speculative** based on company pipelines, AACR 2026 mechanism sessions, and 7-months-out trial trackers:

1. **Bispecifics in DLBCL — durability + earlier-line.** Epcoritamab and glofitamab follow-up in r/r DLBCL (3+ year durability); 1L / 2L combinations (epco-R-CHOP, glofit-Pola-R-CHP); CD20×CD3 head-to-head data; safety / CRS profiles. Cross-link to AACR-side construct biology.
2. **Bispecifics + CAR-T in multiple myeloma.** MajesTEC update (teclistamab post-ASCO), talquetamab combinations, RedirecTT-1 dual-bispecific in EMD myeloma, cilta-cel and ide-cel 4–5 year follow-up, allogeneic anti-BCMA CAR-T. Sequencing of bispecific-after-CAR-T (or vice versa) is the recurring clinical question.
3. **CAR-T durability — long-term curves and second malignancy signal.** The "CAR-T tail" — fraction still in remission at 5+ years for axi-cel / liso-cel / cilta-cel / ide-cel; updated FDA second-primary-malignancy reporting; real-world registry data (CIBMTR).
4. **Gene therapy for sickle cell disease — durability + access.** Exa-cel (Casgevy) and lovo-cel (Lyfgenia) 3+ year follow-up post-approval; pediatric data; real-world access barriers; next-gen base-edited / in-vivo approaches (Beam, Editas pipelines). Cross-link to AACR cell-and-gene-therapy biology.
5. **AML — maintenance, menin, and IDH / FLT3 evolution.** Post-induction venetoclax maintenance trials; revumenib + ziftomenib post-approval real-world; combinations of menin + FLT3 / IDH / hypomethylators; AML MRD-guided therapy.
6. **CLL — BTKi resistance, BCL2 sequencing, fixed-duration combinations.** Pirtobrutinib in covalent-BTKi-resistant CLL; venetoclax-based fixed-duration combinations; CAR-T (lisocabtagene maraleucel) in r/r CLL.
7. **MDS / lower-risk MDS.** Imetelstat post-approval real-world; luspatercept frontline ESA-naive (COMMANDS follow-up); IDH inhibitors in IDH-mut MDS; allogeneic transplant decisions in IPSS-M era.
8. **Hemophilia gene therapy — real-world durability.** Roctavian (val-rox) and Hemgenix (etranadez) 2–4 year FIX/FVIII expression curves; emicizumab combination + non-factor competitor data.

These eight clusters are the expected "spine" of the meeting. The Plenary + Late-Breakers will pull from clusters 1, 2, 4, and 5 most heavily.

## What's different from ASCO / ESMO

- **Cell-and-gene-therapy is a first-class axis at ASH** — not a sub-track. ASCO covers CAR-T in heme but ESMO largely doesn't; ASH owns the cell-therapy durability narrative.
- **Non-malignant heme** (sickle cell, hemophilia, thrombosis, bone marrow failure) is half the meeting. ASCO is purely oncology, ESMO is purely oncology. ASH has both.
- **Late-Breaking Abstracts come at the end** (Tuesday closing slot), unlike ASCO where LBAs anchor the Plenary mid-meeting. Means the closing day is the second high-priority slot.
- **Embargo discipline.** Regular abstracts release Nov 4 (~6 weeks pre-meeting); LBAs release ~late Nov (~2 weeks pre-meeting). Long enough lead time that the pre-meeting analyst-preview cycle is substantial.
- **Drug names are the index, not tool names.** Cross-linking goes through INN / brand / target / mechanism (e.g., "anti-CD20×CD3 bispecific" links epcoritamab ↔ glofitamab ↔ mosunetuzumab follow-up).

## Cross-vault links

- **[AACR 2026](../aacr-2026/index.md)** — the mechanism / biomarker / discovery side of the same heme-cancer investigator network. Many ASH 2026 plenary trials will have AACR 2026 mechanism sessions (menin biology → ASH revumenib pivots; CAR-T construct engineering → ASH durability readouts; bispecific T-cell engager structure → ASH DLBCL / MM data).
- **[ASCO 2026](../asco-2026/index.md)** — heme readouts at ASCO are typically the practice-changing-in-solid-tumors-or-overlap subset (e.g., frontMIND DLBCL 1L on the ASCO 2026 LBA slate). ASH gets the deeper, more numerous heme readouts six months later.
- **[ESMO 2026](../esmo-2026/index.md)** — ESMO occasionally hosts heme readouts (rituximab follow-ups historically), but ASH is the dominant venue for heme. Use ESMO 2026 mainly for IO read-through that bears on heme.
- **[JPM 2026](../jpm-2026/index.md)** — the financing / dealmaking layer. Multiple ASH 2026 sponsors were on the JPM stage in January (Gilead/Kite CAR-T pipeline, BMS cilta-cel + ide-cel, Genmab/AbbVie epcoritamab, Roche glofitamab, Vertex/CRISPR Casgevy, BioMarin Roctavian).
- **[Conferences timeline](../../timeline.md)** — ASH's position in the year's oncology cycle (AACR Apr → ASCO May/Jun → ESMO Oct → **ASH Dec** → JPM Jan). ASH is the year-closer; whatever lands here sets the H1-2027 dealmaking narrative at JPM 2027.

## Next step

- **Now (pre-meeting, May–October 2026):** populate `program-notes.md` with the expected-readout shortlist (anticipated phase 3 toplines, bispecific class watch list, gene-therapy durability watch list, CAR-T pivots). Track company-disclosed toplines through Q2/Q3 2026 earnings calls and ASCO 2026 + EHA 2026 (Jun 11–14, Milan) heme readouts that will set the ASH 2026 framing.
- **EHA 2026 reconciliation (mid-June 2026):** European Hematology Association meeting is the major mid-year heme readout venue. Several trials read out at EHA first and update at ASH; capture those in `program-notes.md` as "EHA-first, ASH-update" entries.
- **Abstract release (Nov 4, 2026, 9:00 AM ET):** drop regular-abstract full-text into trial pages. Late-breakers release ~Nov 24. Batch the priority shortlist first.
- **Live meeting (Dec 12 – 15, 2026):** real-time capture per day-digest. Sunday Plenary (Dec 13) + Tuesday LBA (Dec 15) are the high-priority slots.
- **Post-meeting (Dec 16 – Jan 31, 2027):** finalize `themes.md`. Carry-forward to **JPM 2027** narrative — whatever practice-changing reads at ASH 2026 becomes the H1-2027 dealmaking thesis.

## Sources

- [ASH Annual Meeting home](https://www.hematology.org/meetings/annual-meeting)
- [ASH Abstracts (in *Blood*)](https://ashpublications.org/blood)
- [ASH Clinical News](https://ashclinicalnews.org/)
- [The ASCO Post — Hematologic Malignancies](https://ascopost.com/specialty-pages/hematologic-malignancies/)
- [OncLive — Hematologic Malignancies](https://www.onclive.com/specialty/hematologic-malignancies)
- [Healio — Hematology / Oncology](https://www.healio.com/hematology-oncology)
- [EHA 2026 Annual Congress](https://ehaweb.org/congress/eha2026-hybrid-congress/) — mid-year heme reconciliation point
