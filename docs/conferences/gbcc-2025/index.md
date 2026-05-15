# GBCC 2025

**Galaxy and Bioconductor Community Conference 2025** — Cold Spring Harbor Laboratory, NY · June 23–26, 2025.

> **Status:** Scaffold — program ingested; per-tool entries queued. The full session-by-session program (5 oral sessions, 11 lightning talks, 10 hands-on workshops, 50+ posters) has been extracted into `_program-extracted.md`; bulk tool-page generation is the next pass.

## Why this is in the vault

GBCC2025 is the **first-ever joint conference between Galaxy and Bioconductor** — bridging the two flagship open-source bioinformatics communities (Galaxy = workflow / web-platform / training; Bioconductor = R packages for statistical genomics). For the AACR tools matrix this is uniquely valuable: it's the one place each year where workflow tools and analysis packages get presented under the same roof, with explicit "package wrapped into Galaxy" sessions making the integration story load-bearing.

GBCC2025 is the sister event to **EuroBioC2025** (Barcelona, Sep 17–19, 2025) — together they form the two annual community meetings in Bioconductor's calendar. EuroBioC is the European leg with a tighter R/package focus; GBCC is the joint US event where Galaxy workflow tools and Bioconductor packages share the same program. Roughly 30% of GBCC2025 oral talks introduce a named Bioconductor or Galaxy tool; another 20% introduce cross-platform integration scaffolding (e.g., GalaxyMCP, Bioconductor-R-Shiny on Galaxy, automatic R package wrapping).

## What we have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Schedule (at-a-glance)** | full 4-day grid | [gbcc2025 program/glance](https://gbcc2025.bioconductor.org/program/glance/) |
| **Scientific program** | every oral talk: title, speaker, affiliation, session, chair | [gbcc2025 scientific_program](https://gbcc2025.bioconductor.org/program/scientific_program/) |
| **Meeting report** | community recap with lightning-talk + workshop summaries | [Galaxy June 2025 newsletter](https://galaxyproject.org/news/2025-07-11-june2025-newsletter/) |
| **CSHL meeting page** | conference-level metadata, organizers | [meetings.cshl.edu (galaxy)](https://meetings.cshl.edu/meetings.aspx?meet=galaxy) |
| **Repo** | Hugo source for site; speaker/abstract YAML | [github.com/Bioconductor/gbcc2025](https://github.com/Bioconductor/gbcc2025) |
| **Abstract book** | full abstracts (PDF) | URL referenced as `meetings.cshl.edu/posters/galaxy25/gbcc25_AbstractBook.pdf` — **404 at fetch time**; flagged for retry |
| **CoFest recap** | which Bioconductor tools wrapped into Galaxy at the post-conf hackathon | [Bringing Bioconductor to Galaxy (Bioconductor blog)](https://blog.bioconductor.org/posts/2025-07-03-bioc-to-galaxy/) |
| **Plenary recordings** | keynotes + selected talks | "GBCC2025 YouTube Playlist" referenced in the meeting report — playlist URL not surfaced in current crawl |
| **Slides** | varies | Bioconductor speakers typically deposit to [Zenodo Bioconductor community](https://zenodo.org/communities/bioconductor); Galaxy speakers vary |

## Program shape

- **Day 1 (Mon Jun 23)** — Registration → dinner → Opening Ceremony → "GBCC2025 LIVE!" evening session.
- **Day 2 (Tue Jun 24)** — **Keynote 1: Sergei L. Kosakovsky Pond** (Temple) "Interactive Genomic Analytics with responsive notebooks, in-the-browser computation, and AI-assisted development" → **Oral Session 1** (9 talks; Galaxy infrastructure / AI agents / R-Bioc-into-Galaxy integration; chair Sehyun Oh) → 5 concurrent **workshops** (Galaxy workflows; AI-predicted-outcomes inference; Galaxy backend; autonomous workflows for materials labs; spatial-omics) → **Oral Sessions 2A** (12 talks; Galaxy workflows + ML + multi-omics; chair Jenny Drnevich) **and 2B** (12 talks; Bioconductor packages — RAIDS, signifinder, SEMplR, HiFi-MAG, etc.; chair Vincent Carey) → wine-and-cheese networking → poster session 1.
- **Day 3 (Wed Jun 25)** — **Keynote 2: Charlotte Soneson** (Friedrich Miescher Institute) "From classes to community — How Bioconductor has advanced my research" → **Lightning Talks** (11 short talks: Tidyomics, atena, iscream, SummarizedExperiment-tidy interfaces, kinome analysis, FAIR-EASE, Galaxy-E ecology, etc.) → **Birds of a Feather** sessions → **Oral Session 3** (6 talks; imaging × multi-omics, Visium HD, sosta, genome-assembly curation; chair Lambda Moses) → 5 concurrent **workshops** (Bioc-tools-in-Galaxy; microbiome with Bioc; immunopeptidogenomics; AnVIL secure cloud; IGB Galaxy alignment) → **Oral Session 4** (6 talks; community / training / global access; chair Mike Love) → second BoF block → banquet → DJ Party + Galaxy 20th Anniversary celebration.
- **Day 4 (Thu Jun 26)** — **Keynote 3: Jason Williams** (CSHL) "Conquest of Abundance: Genomics in a Time of Plenty" → **Oral Session 5** (8 talks; plyxp, microbiome orchestration, predicted-data inference, mitology, Galaxy ecology, infrastructure; chair Scott Cain) → lunch + departure.
- **Post-conference (Jun 27–28)** — **CoFest** at the Sandra and Edward Meyer building (separate registration) — Galaxy + Bioconductor hackathon. Featured artifact: GSVA wrapped as a Galaxy tool; on-site team Doyle, Yagudayeva, Soneson, Ramos Pérez.

**Counts:** 3 keynotes · 53 oral talks across 5 sessions · 11 lightning talks · 10 workshops · 50+ posters · ~6 BoF slots.

## Organization

```
conferences/gbcc-2025/
├── index.md                 # this page
├── _program-extracted.md    # working notes — every talk with package + tags
├── themes.md                # cross-day synthesis (deferred)
├── digest/                  # day-by-day recap (deferred)
│   ├── day-1.md
│   ├── day-2.md
│   ├── day-3.md
│   └── day-4.md
├── topics/                  # cross-cutting bins (deferred)
│   ├── galaxy-infra/        # AI agents, MCP, dataset collections, scheduling
│   ├── bioc-packages/       # short-talk Bioc package introductions
│   ├── spatial-imaging/     # Visium HD, sosta, histopathology FMs
│   ├── multi-omics/         # RAIDS, signifinder, gINTomics, MOSClip-adjacent
│   ├── training-community/  # Africa, Canada, sertão, AnVIL training
│   └── integration/         # the seam — Bioc-in-Galaxy, R-Shiny-on-Galaxy
├── tools/                   # PRIMARY artifact — one entry per package or Galaxy tool
│   └── index.md
└── sessions/                # full abstracts, indexed (deferred until abstract-book PDF available)
    └── index.md
```

The `tools/` directory is, as in the EuroBioC2025 vault, the load-bearing artifact. GBCC adds two new entry shapes the EuroBioC template doesn't quite cover: **Galaxy workflow tools** (web-deployable, often with no R/Python "import" surface) and **integration scaffolding** (e.g., automatic R-package-to-Galaxy wrapping pipelines). The tools/index.md template stub flags this as Open Question 5.

## What's different from EuroBioC2025

- **Two ecosystems on one program** — every "Bioc package" entry has a sibling "Galaxy tool" question: was it wrapped? is the wrapper PR open? what's its tool-shed ID? The sister-vault cross-link from `eurobioc-2025/tools/<pkg>` to `gbcc-2025/tools/<pkg>` matters more here because GBCC is where the wrapping conversation actually happens.
- **Galaxy is workflow-first**, conceptually adjacent to **Nextflow Summit 2026** even though the engines and communities differ. Cross-link target: `nextflow-2026/` — the seam to watch is "what does each platform's tool-wrapping story look like, and which papers reference which?"
- **CoFest as a separate artifact** — the post-conference 2-day hackathon produces concrete "package X is now a Galaxy tool" deliverables that don't exist after EuroBioC. These belong in the GBCC vault, not the per-package pages.
- **Training and global-access talks are first-class** — Session 4 (Doyle on Bioconductor in Africa; Gauthier on UseGalaxy Canada; Santana on Brazilian sertão research; Kucher on AnVIL training) is structurally larger than EuroBioC's equivalent. We track these as community-talk entries (not tool entries) but link them from the relevant tool pages where applicable.

## Sources

- [GBCC2025 conference site](https://gbcc2025.bioconductor.org/)
- [GBCC2025 schedule (at a glance)](https://gbcc2025.bioconductor.org/program/glance/)
- [GBCC2025 scientific program](https://gbcc2025.bioconductor.org/program/scientific_program/)
- [GBCC2025 about / overview](https://gbcc2025.bioconductor.org/about/overview/)
- [GBCC2025 BoFs overview](https://gbcc2025.bioconductor.org/bofs/overview/)
- [GBCC2025 CoFest overview](https://gbcc2025.bioconductor.org/cofest/overview/)
- [Galaxy June 2025 newsletter — GBCC meeting report](https://galaxyproject.org/news/2025-07-11-june2025-newsletter/)
- [Bringing Bioconductor to Galaxy — CoFest recap (Bioconductor blog)](https://blog.bioconductor.org/posts/2025-07-03-bioc-to-galaxy/)
- [GBCC2025 announcement (Bioconductor blog, 2024-09-03)](https://blog.bioconductor.org/posts/2024-09-03-gbcc2025-announcement/)
- [GBCC2025 announcement (Galaxy hub, 2024-09-03)](https://galaxyproject.org/news/2024-09-03-gbc-c2025/)
- [CSHL meeting page (galaxy)](https://meetings.cshl.edu/meetings.aspx?meet=galaxy)
- [Bioconductor/gbcc2025 GitHub repo](https://github.com/Bioconductor/gbcc2025)
- [Bioconductor on Zenodo](https://zenodo.org/communities/bioconductor)

## Next step

See [`tools/`](tools/) for the per-tool entry template and the talks-with-packages list. After that template is reviewed against the EuroBioC2025 version, the bulk pass populates ~25–30 tool pages from `_program-extracted.md`. Open question — whether Galaxy workflow tools share the Bioconductor template or get their own variant — is tracked there as Q5.
