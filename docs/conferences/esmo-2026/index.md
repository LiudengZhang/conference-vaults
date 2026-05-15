# ESMO 2026

**ESMO Congress 2026** — IFEMA Madrid, Spain · October 23 – 27, 2026. The European Society for Medical Oncology Annual Congress, ~30,000 attendees, the European practice-changing-trial counterpart to ASCO.

> **Status:** Scaffold — meeting **5 months out** as of today (May 11, 2026); structure landed for live-coverage build when the conference opens. Abstract submission deadline is **May 12, 2026** (tomorrow); late-breaker deadline **Sep 8, 2026**. The official program won't be public until **~July/August 2026**. Anything in this vault dated before its embargo lift is built from company topline press releases, analyst notes, and prior-year patterns — flagged inline.

## Why this is in the vault

ESMO is the **European clinical-translation counterpart** to [ASCO 2026](../asco-2026/index.md) — same investigator network, same trial vocabulary, often the same drugs at a different timepoint in the year. ESMO sits in October, four months after ASCO and three months before [JPM 2026](../jpm-2026/index.md), and tends to absorb:

- **OS / long-term follow-up** of trials that read PFS at ASCO (ASCO May/Jun PFS → ESMO Oct OS is a common rhythm).
- **European-led cooperative-group trials** — EORTC, GETUG, ICORG, AGITG, GERCOR, GBG, MAGIC consortia — that don't typically pick ASCO as the disclosure venue.
- **EMA-track regulatory data** — trials sized for EU first registration / EMA filings, including academic-led de-escalation studies that European payers care about more than CMS.
- **Asian / China-origin assets** that already presented topline at ASCO and want a second European look (HARMONi-6 PFS at ESMO 2025 → OS at ASCO 2026 → updates back at ESMO 2026 is the pattern).
- **ctDNA-guided trial designs** — ESMO has emphasized ctDNA-guided escalation/de-escalation in recent Presidential Symposia (IMvigor011 MIBC, DYNAMIC-III stage III CRC at ESMO 2025).

**Format note (and the design decision behind this vault):** ESMO is **clinical, not tools-focused** — the same structural choice that drove the ASCO 2026 vault applies here. The per-tool template that loads EuroBioC2025 / GBCC2025 / ISMB 2026 vaults does not fit. The primary artifact is the **per-trial / per-readout** entry. See `trials/index.md` for the schema (copied from ASCO with ESMO branding — they are siblings).

The closest sibling vault in shape is **[ASCO 2026](../asco-2026/index.md)**. The ESMO vault uses the same template, the same per-trial schema, and the same "themes + day-by-day digest" pattern. The differences are venue/embargo specifics noted below.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **ESMO Online Programme** | session grid, Presidential Symposia, late-breaker slate | [esmo.org/meeting-calendar/esmo-congress-2026](https://www.esmo.org/meeting-calendar/esmo-congress-2026) — full program published ~July/August 2026 |
| **Annals of Oncology — Abstract Book supplement** | full abstract text, online-only, post-Congress | [annalsofoncology.org](https://www.annalsofoncology.org/) — the ESMO Meeting Library equivalent; abstracts release at the embargo lift (typically day-of for LBAs, day-prior for accepted regular abstracts) |
| **ESMO Daily Reporter** | first-pass post-session recaps, official ESMO editorial | [dailyreporter.esmo.org](https://dailyreporter.esmo.org/) — runs during Congress |
| **OncologyPRO** | educational content + member-side abstract access pre-Congress | [oncologypro.esmo.org](https://oncologypro.esmo.org/) |
| **OncLive / Targeted Oncology / CancerNetwork** | discussant-level depth, expert reaction video stand-ups | parallel to ASCO coverage; ESMO 2025 set the template |
| **Evaluate / ApexOnco / BioPharma Dive / Endpoints / STAT** | analyst framing, sponsor stock reactions, EU regulatory read-through | sub-required for some; ApexOnco runs an annual "ESMO preview" piece in late August |
| **Company press releases** | toplines (often pre-embargo), full presentation decks (post-presentation) | PRNewswire / BusinessWire / sponsor IR; many companies stage releases to match the EU morning |
| **Presidential Symposium livestream** | full talk video + discussant | ESMO Virtual; replay typically gated behind registration for the meeting year |
| **Social** | #ESMO26 on X / Bluesky / LinkedIn | LinkedIn is heavier-trafficked for ESMO than ASCO (European clinician norm); useful for real-time room reactions |

The **Annals of Oncology Abstract Book supplement is the load-bearing primary source** — every accepted abstract gets a citable entry with DOI. Per-trial pages should cite the abstract reference, not the company press release.

## Program shape

ESMO 2026 runs **Friday October 23 (educational sessions begin) through Tuesday October 27 (closing)**, five days, IFEMA Madrid. The historical structure (per ESMO 2024 / 2025 patterns — *2026 program not yet public*):

- **Three Presidential Symposia** — the practice-changing slots. ESMO splits the load across three sessions (typically Saturday, Sunday, Monday) rather than ASCO's single Plenary. Each Presidential Symposium hosts 4 LBAs with named discussants. *Slate not yet announced — expected July/August 2026.*
- **Proffered Paper Sessions** — ~25 across the week, the equivalent of ASCO Oral Abstract Sessions. Many late-breakers land here rather than in Presidential.
- **Educational track** — runs in parallel, anchors the meeting's identity as a teaching congress as much as a research one (the ESMO/ESMO Open guideline-update venue).
- **Mini-Oral Sessions + posters** — large poster halls; e-poster + walk-around format.
- **Major Symposium / Multidisciplinary** — cross-cutting clinical themes (e.g., real-world evidence, precision-oncology platform trials, AI in oncology).
- **Tracks** (per ESMO category structure): Breast, GI (Upper/Lower/HBP separately), GU (Prostate/Bladder/Kidney/Penile), Lung & Thoracic, Melanoma, Sarcoma, GYN, Head & Neck, CNS, Haematological, Endocrine/NET, Supportive/Palliative, Geriatric, Cancer Biology / Translational, Immunotherapy, Precision Oncology, Public Health / Health Services, Developmental Therapeutics.
- **Press programme** (separate, embargoed media briefings) Friday – Monday mornings; ESMO Press Office issues themed press releases through the week.

## Organization

```
conferences/esmo-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep: tracks, expected LBAs, presidential symposia slate, discussant watch list, key dates
├── trials/              # PRIMARY artifact — one entry per trial / readout
│   └── index.md         # template + master trial index table
├── themes.md            # cross-day synthesis (deferred until post-meeting)
└── digest/              # day-by-day recap (deferred until post-meeting)
    ├── day-1-friday.md      # Oct 23 — Educational + first oral sessions
    ├── day-2-saturday.md    # Oct 24 — Presidential Symposium I (typical)
    ├── day-3-sunday.md      # Oct 25 — Presidential Symposium II
    ├── day-4-monday.md      # Oct 26 — Presidential Symposium III
    └── day-5-tuesday.md     # Oct 27 — closing oral sessions
```

The `trials/` directory is load-bearing. Each trial gets one Markdown file. Template at `trials/index.md`. Expected ~40–70 entries spanning the three Presidential Symposia, the top-polled LBAs across the major tracks, and the ASCO 2026 follow-ups (OS updates, longer-term subgroup data).

## What's different from ASCO 2026

- **Three Presidential Symposia, not one Plenary.** The "practice-changing slot" is spread across Saturday/Sunday/Monday, which dilutes the single-day intensity but extends the news cycle. Per-trial page priority should weight Presidential placement equivalently to ASCO Plenary placement.
- **Embargo policy is stricter on the regular-abstract side.** ESMO holds copyright on accepted abstracts and does **not** release them publicly weeks ahead the way ASCO does. Regular abstracts typically appear online on the day of (or day prior to) presentation. LBAs are day-of. This means *less pre-meeting reconstruction is possible* than for ASCO — more of the build happens during the meeting.
- **European-led cooperative groups are heavier in the corpus.** EORTC, GETUG, ICORG, GBG, AGITG, GERCOR. Worth tagging cooperative-group sponsors in the per-trial schema (added field).
- **Annals of Oncology is the citation venue.** Every accepted abstract gets indexed as a supplement to Annals of Oncology with a DOI. ASCO Meeting Library has direct permalinks; ESMO routes through the journal. Cross-link convention: cite the Annals of Oncology DOI when available, fall back to the OncologyPRO session page.
- **Drug-name index is identical to ASCO** (same drugs, same investigators) but the regulatory framing tilts EMA. Several trials at ESMO are sized specifically for EMA registration rather than FDA (e.g., academic-led, EU-population, sometimes without a US sponsor).

## Cross-vault links

- **[ASCO 2026](../asco-2026/index.md)** — sibling vault. Many ESMO 2026 trials are ASCO 2026 OS or longer-follow-up updates; cross-link aggressively on the per-trial pages. The "drug-name index" page (TBD) should unify ASCO + ESMO entries.
- **[AACR 2026](../aacr-2026/index.md)** — the mechanism / biomarker / discovery side. AACR April → ASCO May/Jun → ESMO Oct is the standard translational cycle.
- **[JPM 2026](../jpm-2026/index.md)** — the financing layer. Many ESMO 2026 sponsors were on the JPM stage in January (AZ Enhertu / Imfinzi, Roche Phesgo / Itovebi, Lilly Verzenio / Retevmo, Merck Welireg, BMS Opdivo). ESMO data → end-of-year guidance / Q4 catalyst for the same sponsors.
- **[Conferences timeline](../../timeline.md)** — ESMO's position in the year's oncology cycle (AACR Apr → ASCO May/Jun → ESMO Oct → ASH Dec → JPM Jan).

## Next step

- **Now (5 months pre-meeting, May 11):** structure landed. Populate `program-notes.md` with the verified key dates, the historical Presidential-Symposium structure, the conservative shortlist of trials with known H2 2026 readout timing, and the discussant-watch placeholder. Flag every speculative item.
- **Abstract submission deadline (May 12):** regular abstracts close — no public effect yet, but starts the clock.
- **Mid-cycle (May – early Aug):** monitor ASCO 2026 PFS readouts that will mature for ESMO OS (HARMONi-6, Rasolute-302, frontMIND, ASCENT-04, SERENA-6 are the top candidates). Update `program-notes.md` as topline press releases land.
- **Program publication (~July/August 2026):** ESMO Online Programme goes live. Lift trial titles, session assignments, named Presidential LBAs, discussants. Build trial stubs for the top 15–20.
- **Late-breaker deadline (Sep 8):** late-breaker slate finalizes ~4 weeks after submission.
- **Pre-meeting (early Oct):** ApexOnco / OncLive / Targeted Oncology preview pieces drop. Cross-reference for any missing topline disclosures.
- **Live meeting (Oct 23 – 27):** real-time capture per day-digest. Three Presidential Symposia days are the high-priority slots.
- **Post-meeting (Oct 28 – Nov 30):** finalize `themes.md`. Likely threads (highly tentative this far out): ADC durability + sequencing (SATEEN-style ADC-after-ADC), CDK4/6 post-progression endocrine combinations (evERA fallout), perioperative IO maturity (KEYNOTE-B15 / PROTEUS OS), ctDNA-guided escalation/de-escalation continuation, PD-1×VEGF bispecific class read-through (HARMONi follow-ups + AbbVie RC148 first data), pan-RAS Ph3 follow-up (Rasolute-302 OS confirmation), EMA-track adjuvant TKI registrations.

## Sources

- [ESMO Congress 2026 home](https://www.esmo.org/meeting-calendar/esmo-congress-2026)
- [ESMO Congress 2026 Abstract page](https://www.esmo.org/meeting-calendar/esmo-congress-2026/abstracts)
- [ESMO Congress 2026 Programme](https://www.esmo.org/meeting-calendar/esmo-congress-2026/programme)
- [ESMO Congress 2026 Venue (IFEMA Madrid)](https://www.esmo.org/meeting-calendar/esmo-congress-2026/venue)
- [Annals of Oncology](https://www.annalsofoncology.org/)
- [OncologyPRO](https://oncologypro.esmo.org/)
- [ESMO Daily Reporter](https://dailyreporter.esmo.org/)
- [IFEMA Madrid — ESMO 2026 venue page](https://www.ifema.es/en/esmo-congress)
- [Tourism Madrid — ESMO 2026 event listing](https://www.esmadrid.com/en/whats-on/esmo-madrid-congress-ifema-madrid)
