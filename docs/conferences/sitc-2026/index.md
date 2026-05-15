# SITC 2026

**SITC 41st Annual Meeting & Pre-Conference Programs** — Phoenix Convention Center, Phoenix, AZ · November 4 – 8, 2026. ~6,000 attendees, the premier cancer-immunotherapy venue of the year.

> **Status:** Scaffold — meeting is **6 months out** as of today (May 11, 2026). Vault structure is being seeded now so we can move quickly on the abstract embargo (regular abstracts open Apr 22 → close Jun 25; presentation embargoes lift on the morning of the talk in early November). Anything in this vault dated before SITC 2026 is built from SITC 2025 program shape, company toplines, and partner / sponsor press from JPM 2026, AACR 2026, and ASCO 2026 — flagged inline.

## Why this is in the vault

SITC is the **immunotherapy half-life** of the oncology calendar — the venue where checkpoint, cell therapy (CAR-T, TIL, TCR-T), bispecifics, neoantigen vaccines, and tumor-microenvironment biology converge in one program. It sits at a deliberate intersection with two AACR axes:

1. **Clinical-trials axis** — early- and mid-phase IO readouts (Ph1/2 cell-therapy and bispecific cohorts, checkpoint-resistance combos, neoantigen-vaccine signal). Many SITC presentations are the IO trials that didn't fit the ASCO Plenary calendar or the AACR mechanism slot — earlier-phase data on drugs that will land at ASCO 2027 or ESMO 2027.
2. **Single-cell / spatial-omics axis** — immune profiling is half the program. Multiplex IF, spatial transcriptomics, scRNA-seq, TCR repertoire, ctDNA-MRD, and microbiome readouts anchor a large block of the methods program. Same tools, same labs as the EuroBioC / GBCC / RECOMB tools axis, applied to IO-specific biological questions.

**Hybrid template (and the design decision behind this vault):** SITC is **neither pure-clinical (ASCO) nor pure-tools (EuroBioC)** — it's both, in the same program, often back-to-back in the same session. Pure per-trial pages miss the methods talks; pure per-tool pages miss the cell-therapy cohorts. We're running **both templates in parallel**:

- `trials/` — per-trial / per-readout entries for drug + cell-therapy readouts (CAR-T cohorts, bispecific Ph1/2, neoantigen-vaccine arms, checkpoint-resistance combos). Schema borrowed from [ASCO 2026 trials](../asco-2026/trials/index.md).
- `tools/` — per-tool entries for biomarker, immune-profiling, and spatial-immune methods (multiplex IF panels, TCR repertoire pipelines, ctDNA-MRD assays, microbiome 16S/shotgun protocols, spatial-immune classifiers). Schema borrowed from [EuroBioC 2025 tools](../eurobioc-2025/tools/index.md).

Cross-links between the two are the load-bearing piece: a CAR-T cohort in `trials/` should link to the spatial-immune profiling tool that read its biopsies in `tools/`, and vice versa.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **SITC Annual Meeting site** | program, plenary slate, pre-conference workshops | [sitcancer.org/2026](https://www.sitcancer.org/2026/home) — primary |
| **Journal for ImmunoTherapy of Cancer (JITC)** | abstract supplement (published as JITC volume, open access) | [jitc.bmj.com](https://jitc.bmj.com/) — the official abstract record, citable DOI per abstract |
| **SITC press program** | embargoed media briefings during the meeting | press releases typically wire-syndicated same day |
| **ACIR Weekly Digest** | curated post-session expert recap | [acir.org](https://acir.org/) — Cancer Research Institute editorial, names key abstracts |
| **Cancer Research Institute blog** | conference-week editorial | [cancerresearch.org/blog](https://www.cancerresearch.org/blog) |
| **OncLive / Targeted Oncology / CancerNetwork** | trade-press recaps, video stand-ups | similar pattern to ASCO |
| **Endpoints / STAT / BioPharma Dive / Evaluate** | analyst framing, sponsor stock reactions | sub-required for some |
| **Company press releases** | toplines (often pre-meeting), full deck post-presentation | wire-service syndication |
| **Plenary livestream + replay** | session video for hybrid attendees | SITC virtual platform |
| **Social** | #SITC26 on X / Bluesky / LinkedIn | useful for real-time room reactions |

The **JITC abstract supplement is the load-bearing primary source** — every accepted abstract gets a citable DOI and full text via JITC, which is the same property that makes the ASCO Meeting Library load-bearing for ASCO. Per-trial and per-tool pages should cite the JITC abstract permalink, not the company press release.

## Program shape (per SITC 2025 + early SITC 2026 announcements)

SITC 2026 runs **Wednesday Nov 4 – Sunday Nov 8**, five days. The structure:

- **Wed Nov 4 – Thu Nov 5: Pre-Conference Programs.** Workshops on cellular therapy, biomarkers / immune-monitoring, regulatory science, primer courses. ~10 parallel tracks.
- **Fri Nov 6 – Sun Nov 8: Annual Meeting** proper. Plenary + concurrent sessions + poster halls.
- **Keynote:** Ton Schumacher, PhD (Netherlands Cancer Institute) — "T Cell Recognition of Human Cancer: 'Cracking the Code'" (TCR / neoantigen-recognition biology).
- **Smalley Memorial Award & Lectureship:** Catherine J. Wu, MD (Dana-Farber) — neoantigen-vaccine science (the personalized-vaccine program that started at DFCI and now anchors Moderna, BioNTech, and Gritstone competitor reads).
- **Abstract scale:** ~1,200 abstracts, several hundred posters, >40 oral / concurrent sessions.
- **Tracks dominating the corpus** (per SITC 2025 shape):
  - **Cellular therapies** — CAR-T (autologous + allogeneic), TIL, TCR-T, NK-cell, engineered macrophages. Solid-tumor cell therapy is the growth area.
  - **Checkpoint resistance** — combinations to overcome primary / acquired anti-PD-(L)1 resistance; novel checkpoints (LAG-3, TIGIT, TIM-3, VISTA).
  - **Bispecifics + ADCs** — T-cell engagers, NK engagers, immunocytokines; checkpoint × VEGF, checkpoint × CD3.
  - **Neoantigen vaccines** — personalized mRNA, peptide, DNA platforms; shared-neoantigen approaches; vaccine + checkpoint combos.
  - **Biomarkers / immune monitoring** — multiplex IF, spatial transcriptomics, TCR repertoire, ctDNA-MRD, single-cell.
  - **Microbiome × immunotherapy axis** — FMT, defined-consortium products, dietary intervention, prebiotic / probiotic combinations (the Wargo thread, continued).
  - **Spatial-immune profiling** — tumor microenvironment characterization across response / resistance; spatial classifiers as biomarker-development substrate.

## Organization

```
conferences/sitc-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep: dates, venue, tracks, expected readouts, tool-talk watch list, key dates
├── trials/              # per-trial template — drug + cell-therapy readouts
│   └── index.md         # template + master trial index table (CAR-T, bispecific, neoantigen vaccine, checkpoint-resistance combo)
└── tools/               # per-tool template — biomarker / immune-profiling / spatial-immune methods
    └── index.md         # template + master tool index table (multiplex IF, TCR repertoire, ctDNA-MRD, microbiome, spatial classifiers)
```

Day-by-day digest (`digest/day-N-*.md`) and cross-day themes (`themes.md`) deferred until post-meeting, modeled on the ASCO / Nextflow / JPM 2026 vaults.

## What's different from ASCO 2026 and AACR 2026

- **Smaller, denser, more IO-pure.** ~6,000 attendees vs ASCO's ~40,000 and AACR's ~22,000. Every session is IO; no GU non-IO, no symptoms-and-survivorship track, no non-cancer biology.
- **Earlier-phase data than ASCO.** Most cell-therapy and bispecific readouts at SITC are Ph1/2 cohorts and dose-escalation updates, not randomized Ph3. Closer in maturity to AACR's clinical-trials track than to ASCO's Plenary slate.
- **Tools-and-trials in the same program.** Unlike ASCO (pure clinical) or EuroBioC (pure tools), SITC programs methods talks adjacent to drug readouts. Spatial-immune profiling on biopsies from the same Ph2 cohort that's reading out in the next session.
- **JITC as the citable record.** Unlike ASCO Meeting Library (proprietary), JITC is open-access BMJ-published; every abstract gets a DOI. Easier to cite, more permanent.
- **Microbiome / spatial-immune themes** — both are bigger at SITC than at any other oncology meeting. Microbiome × IO especially: SITC is where defined-consortium products and FMT-in-IO trial data appear.

## Cross-vault links

- **[AACR 2026](../aacr-2026/index.md)** — IO biology / mechanism / discovery side. Many SITC 2026 presenters had AACR 2026 sessions in April. Single-cell / spatial axis overlaps heavily.
- **[ASCO 2026](../asco-2026/index.md)** — clinical-translation counterpart. Some SITC 2026 trials will reach ASCO 2027 as randomized readouts.
- **[JPM 2026](../jpm-2026/index.md)** — financing layer. Multiple SITC 2026 sponsors (cell-therapy companies, neoantigen-vaccine platforms, bispecific developers) were on the JPM stage in January.
- **[EuroBioC 2025 tools](../eurobioc-2025/tools/index.md)** — methods axis. Spatial-omics packages (SpatialData, DESpace, spatialFDA), TCR / clonal-tracking (barbieQ), and microbiome (mia, miaTime) all have direct application in SITC immune-monitoring talks.
- **[Conferences timeline](../../timeline.md)** — SITC's position in the year's cycle (AACR Apr → ASCO May/Jun → ESMO Oct → **SITC Nov** → ASH Dec → JPM Jan).

## Next step

- **Now (May – Jun 2026, abstract window open):** populate `program-notes.md` with the expected-readout shortlist (~20 trials, ~15 tools) and watch list for the cell-therapy / bispecific / vaccine sponsor tracks. Pre-build top stubs for the Schumacher keynote and the Wu Smalley lecture.
- **Abstract acceptance (Sep 2026):** when SITC posts the program-at-a-glance + accepted-abstract list, expand `trials/` and `tools/` stubs to match the actual session grid.
- **JITC abstract supplement (Oct 2026):** when JITC publishes the abstract issue, fill in full-text per stub.
- **Live meeting (Nov 4 – 8):** real-time capture per day. Hybrid format means slides + video available post-session for many tracks.
- **Post-meeting (Nov – Dec 2026):** finalize `themes.md`. Expected threads (speculative, to be revised): solid-tumor CAR-T inflection point, neoantigen-vaccine signal across pancreatic / melanoma / kidney, TIGIT / LAG-3 class status post-skyscraper failures, microbiome × IO maturation, spatial-immune biomarker convergence.

## Sources

- [SITC 2026 Annual Meeting home](https://www.sitcancer.org/2026/home)
- [SITC main site](https://www.sitcancer.org/)
- [Journal for ImmunoTherapy of Cancer (JITC)](https://jitc.bmj.com/)
- [ACIR — SITC 2025 40th Anniversary recap](https://acir.org/weekly-digests/2025/november/sitc-40th-anniversary-annual-meeting-2025)
- [Cancer Research Institute — SITC 2025 blog](https://www.cancerresearch.org/blog/sitc2025)
- [SITC 2025 schedule reference](https://www.sitcancer.org/2025/home)
