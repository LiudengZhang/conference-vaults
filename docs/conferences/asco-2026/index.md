# ASCO 2026

**62nd ASCO Annual Meeting** — McCormick Place, Chicago, IL · May 29 – Jun 2, 2026. ~40,000 attendees, the largest oncology meeting of the year.

> **Status:** Scaffold — meeting is **3 weeks out** as of today (May 11, 2026). The structure is landing now so live-coverage build (Plenary May 31, LBA-by-LBA reveal across May 29 – Jun 2) can run immediately. Abstract titles are public (released Apr 21); the **regular-abstract embargo lifts May 21, 5:00 PM ET**; **LBAs (including all Plenary abstracts) release at 7:00 AM CT on the day of presentation**. Anything in this vault dated before its embargo lift is built from company topline press releases, ASCO press-program previews, and analyst notes — flagged inline.

## Why this is in the vault

ASCO is the **clinical-translation counterpart** to [AACR 2026](../aacr-2026/index.md). Same investigators, one phase later: where AACR shows the biology and the early-phase signal, ASCO shows whether it works in patients at randomized phase 3 scale. Strong overlap with AACR's clinical-trials axis — multiple plenary trials at ASCO 2026 (PROTEUS, LIBRETTO-432, HARMONi-6, Rasolute-302) have AACR 2025/2026 mechanism-of-action sessions backing them.

**Format note (and the design decision behind this vault):** ASCO is **clinical, not tools-focused**. The per-tool template that loads the EuroBioC2025 / GBCC2025 / ISMB 2026 vaults does not fit here — there are no Bioconductor packages debuting on the Plenary stage. The primary artifact for ASCO 2026 is the **per-trial / per-readout** entry. See `trials/index.md` for the schema.

The closest sibling vault in shape is **[JPM 2026](../jpm-2026/index.md)** — also non-tools, also public-coverage-driven (no slide decks public for many sessions), also synthesis-by-day. The ASCO vault borrows JPM's "themes + day-by-day digest" pattern, but adds a per-trial detail page that JPM doesn't need (JPM doesn't have randomized phase 3 readouts).

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **ASCO Meeting Library** | abstract full-text (regular) post-May 21; LBA full-text on day of presentation | [asco.org/abstracts](https://www.asco.org/abstracts) — primary source for the per-trial pages |
| **ASCO 2026 Program page** | session grid, Plenary slate, Discussant assignments | [asco.org/annual-meeting/program](https://www.asco.org/annual-meeting/program) — Plenary is Sun May 31 |
| **ASCO Daily News** | first-pass post-session recaps, official ASCO editorial | [dailynews.ascopubs.org](https://dailynews.ascopubs.org/) |
| **The ASCO Post** | weekly recap issues June – August 2026 | [ascopost.com](https://ascopost.com/) |
| **OncLive / Targeted Oncology / CancerNetwork** | discussant-level depth, "expert reaction" video stand-ups | [onclive.com](https://www.onclive.com/), [targetedonc.com](https://www.targetedonc.com/), [cancernetwork.com](https://www.cancernetwork.com/) |
| **Evaluate / ApexOnco / BioPharma Dive / Endpoints / STAT** | analyst framing, sponsor stock reactions, M&A read-through | sub-required for some; STAT runs a real-time blog |
| **Company press releases** | toplines (often pre-embargo), full presentation decks (post-presentation) | wire-service syndication via PRNewswire, BusinessWire |
| **Plenary livestream + replay** | full talk video + discussant | ASCO Virtual; replay typically free for ~3 months post-meeting |
| **Social** | #ASCO26 on X / Bluesky | useful for real-time room reactions; not primary |

The **ASCO Meeting Library is the load-bearing primary source** — every accepted abstract has a permalink with title, authors, affiliations, methods, results, and conclusions. Per-trial pages should cite the abstract DOI / permalink, not the company press release.

## Program shape

ASCO 2026 runs **Friday May 29 (Education Day) through Tuesday June 2 (closing)**, five days, McCormick Place West / South. The structure:

- **Plenary Session — Sunday May 31** (the practice-changing slot). Six abstracts: **LBA1 PROTEUS** (Erleada/apalutamide, prostate, perioperative), **LBA2 SARC041** (abemaciclib, dedifferentiated liposarcoma), **LBA3 LIBRETTO-432** (selpercatinib, adjuvant RET+ NSCLC), **LBA4 HARMONi-6** (ivonescimab, 1L squamous NSCLC, China-only), **LBA5 Rasolute-302** (daraxonrasib, 2L pancreatic PDAC, RAS), plus one TBD. Discussants for the Plenary are usually announced ~2 weeks pre-meeting; we'll capture them in `program-notes.md`.
- **Opening Session (Sat May 30)** — Presidential Address + Karnofsky Award lecture.
- **23 Oral Abstract Sessions + 25 Rapid Oral + 13 Clinical Science Symposia** — ~450 oral abstract presentations.
- **>7,000 abstracts total** (orals + posters + online-only publications).
- **Tracks dominating the corpus:** GI (CRC, pancreatic, gastric), GU (prostate, RCC, bladder), Lung (NSCLC, SCLC), Breast (HR+/HER2-, TNBC, HER2+), Heme (DLBCL, MM, AML), Melanoma, GYN, Sarcoma, Symptoms/Survivorship. Cross-cutting: **ADCs, bispecifics, radioligands, RAS-class inhibitors, perioperative IO**.
- **Press program** (separate, embargoed media briefings) Fri-Tue mornings; ASCO Daily News and STAT have AM newsletters during the meeting.

## Organization

```
conferences/asco-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep: tracks, plenary preview, expected LBAs, discussant watch list, key dates
├── trials/              # PRIMARY artifact — one entry per trial / readout
│   └── index.md         # template + master trial index table
├── themes.md            # cross-day synthesis (deferred until post-meeting)
└── digest/              # day-by-day recap (deferred until post-meeting)
    ├── day-1-friday.md      # May 29 — Education Day, first LBAs (incl. LBA8500 WU-KONG28)
    ├── day-2-saturday.md    # May 30 — Opening, Presidential, first oral sessions, frontMIND
    ├── day-3-sunday.md      # May 31 — PLENARY (LBA1–LBA5); the load-bearing day
    ├── day-4-monday.md      # Jun 1 — ALCHEMIST, OptimUM-02 melanoma (LBA9503), more orals
    └── day-5-tuesday.md     # Jun 2 — closing orals, TRIPLEX SCLC
```

The `trials/` directory is load-bearing. Each trial gets one Markdown file. Template at `trials/index.md`. Expected ~50–80 entries spanning the Plenary slate, top-polled LBAs, and the major track headliners.

## What's different from AACR 2026

- **No biology, no posters-on-AI-platforms.** Pure clinical readouts. The AACR template (mechanism + assay + scRNA-seq cohort + xenograft + clinical-translation appendix) does not apply.
- **Public coverage is the load-bearing source, not full transcripts.** Like JPM, much of what happens in the room only reaches us via trade-press editorial. Unlike JPM, every claim is backed by an embargoed peer-curated abstract — the Meeting Library makes ASCO the **most-citable non-journal venue** in oncology.
- **Embargo discipline matters.** Anything written pre-embargo about a regular abstract is reconstructed from titles + company toplines + analyst preview pieces. Plenary LBAs only release the morning of presentation. Flag everything pre-embargo as `*expected, subject to embargo*` and update post-presentation.
- **Drug names are the index, not tool names.** Cross-linking goes through INN / brand / mechanism (e.g., "PD-1×VEGF bispecific" links HARMONi-6 ↔ Summit ivonescimab JPM 2026 entry ↔ AbbVie RC148 deal ↔ BMS pumitamig).

## Cross-vault links

- **[AACR 2026](../aacr-2026/index.md)** — the mechanism / biomarker / discovery side of the same investigator network. Many ASCO 2026 plenary trials have AACR 2025 or 2026 mechanism sessions (e.g., RAS-inhibitor preclinical at AACR → Rasolute-302 at ASCO Plenary).
- **[JPM 2026](../jpm-2026/index.md)** — the financing / dealmaking layer. Multiple ASCO 2026 trial sponsors were on the JPM stage in January (Lilly Retevmo / Verzenio, Pfizer Padcev, Summit/Akeso ivonescimab licensing, Revolution Medicines daraxonrasib).
- **[Conferences timeline](../../timeline.md)** — ASCO's position in the year's oncology cycle (AACR Apr → ASCO May/Jun → ESMO Oct → ASH Dec → JPM Jan).

## Next step

- **Now (pre-meeting, May 11–21):** populate `program-notes.md` with the expected-LBA shortlist (~25 trials), plenary slate, and discussant watch list as named. Pre-build trial stubs for the top 10 — Plenary LBAs + frontMIND + OptimUM-02 + ALCHEMIST + KEYNOTE-B15.
- **Embargo lift (May 21, 5pm ET):** drop regular-abstract full-text into trial pages. ~7,000 abstracts go public at once — batch the priority shortlist first.
- **Live meeting (May 29 – Jun 2):** real-time capture per day-digest. Plenary day (May 31) is the high-priority slot — LBAs 1–5 reveal in a single 3-hour session.
- **Post-meeting (Jun 3 – Jun 30):** finalize `themes.md`. Expected threads: RAS-class drugs become real (daraxonrasib + KRAS-G12D early-phase), perioperative IO expansion (KEYNOTE-B15, ALCHEMIST, PROTEUS), PD-1×VEGF bispecific class read-through (HARMONi-6 OS, AbbVie RC148 echo), ADC durability (ASCENT-04 PFS2), endocrine-backbone resistance (persevERA miss, SERENA-6 PFS2).

## Sources

- [ASCO Annual Meeting home](https://www.asco.org/annual-meeting)
- [ASCO 2026 Program](https://www.asco.org/annual-meeting/program)
- [Dates to Know](https://www.asco.org/annual-meeting/dates-know)
- [Abstract Policies / Embargoes](https://www.asco.org/annual-meeting/abstracts-presentations/abstract-policies-embargoes-exceptions/faqs)
- [ASCO Meeting Library](https://www.asco.org/abstracts)
- [ASCO Daily News](https://dailynews.ascopubs.org/)
- [The ASCO Post](https://ascopost.com/)
- [OncLive — ASCO 2026 lung cancer poll picks](https://www.onclive.com/view/onclive-polls-reveal-picks-for-top-lung-cancer-abstracts-at-asco-2026)
- [OncLive — ASCO 2026 breast cancer poll picks](https://www.onclive.com/view/poll-results-highlight-breast-cancer-abstracts-of-interest-at-asco-2026)
- [ApexOnco — ASCO 2026 preview (Revolution Medicines)](https://www.oncologypipeline.com/apexonco/asco-2026-preview-revolution-completes-its-rout)
- [ASCO press release — 2026 Annual Meeting lifestyle & treatment strategies](https://www.asco.org/about-asco/press-center/news-releases/new-research-highlights-lifestyle-treatment-strategies-2026-annual-meeting)
