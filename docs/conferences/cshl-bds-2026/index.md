# CSHL Genome Informatics 2026

**Cold Spring Harbor Laboratory's late-fall methods-and-tools meeting — but 2026 is the off-year.** Genome Informatics (GI) runs **biennially in odd years**; the 2026 slot in the CSHL calendar is held by its sibling meeting **Biological Data Science (BDS)**, November 4–7, 2026. The next true Genome Informatics meeting is November 2027.

> **Status:** Scaffold — meeting upcoming (sibling slot). The 2026 vault is built around **Biological Data Science 2026** (the BDS-in-GI-off-year slot at CSHL) because no Genome Informatics 2026 exists. The next pure Genome Informatics meeting (GI 2027) gets its own vault when its program drops in ~Jun 2027.

> **Calendar correction up front:** an early version of this task brief assumed CSHL Genome Informatics 2026 was a real meeting on the calendar. It isn't. CSHL GI alternates with Hinxton's Biology of Genomes Informatics meeting and runs in odd years (2023, 2025, 2027); 2024 and 2026 host BDS in roughly the same week, same venue, same community. The BDS-2026 program (organizers: Karlsson / Schatz / Vallejos; sessions: Algorithmics, Population Genetics & Personalized Medicine, ML, Tools/Viz/Infra, Functional Genomics, Spatial Genomics & Spatial Biology) is what fills this vault slot in 2026.

## Why this is in the vault

- **Pure-methods, small, high-signal.** ~250 attendees, single-track main program, Cold Spring Harbor venue (Grace Auditorium). Tools-and-methods density is roughly tied with RECOMB for highest in the corpus — every oral talk is either a method, an algorithm, an infrastructure piece, or a benchmark. There is no industry track, no clinical-translation track, no community/training spillover (those live at GBCC).
- **BDS-as-GI-off-year is the relevant 2026 surface.** Schatz (organizer of BDS 2026) is a recurring GI organizer; Karlsson and Vallejos both have BDS/GI cross-history. The audience overlap with GI 2025 is essentially complete — same lab groups, same Bluesky chatter, same poster-session networking pool. From the vault's perspective, BDS 2026 *is* the CSHL late-fall tools meeting for 2026.
- **AACR bioinfo-axis fit, narrow but deep.** The six BDS sessions slice cleanly onto our axes: **Spatial Genomics & Spatial Biology** ↔ AACR spatial-omics + EuroBioC SpatialData / DESpace / OSTA; **Machine Learning** + **Functional Genomics** ↔ AACR foundation-model / agentic-AI dossiers + ISMB MLCSB + RECOMB Protein/ML sessions; **Tools, Visualization, and Infrastructure** ↔ GBCC Galaxy-infra + Nextflow Summit; **Population Genetics & Personalized Medicine** ↔ AACR translational-genomics + RECOMB Statistical Genetics; **Algorithmics** ↔ RECOMB Sequence/Phylogeny upstream-infra bin. There is one bin (Spatial Biology) where AACR clinical talks and BDS methods talks routinely cite the same Voyager/SpatialData/Visium-HD substrate — that's the cross-vault link target.
- **Cross-vault people overlap is dense.** Schatz appears in GBCC 2025 keynote (Jason Williams talk references his group's pangenome work), RECOMB 2026 (Cuttlefish 3 co-author Rob Patro is downstream of Schatz's pangenome program), and ISMB 2026 (BOSC + MLCSB co-chair history). Vallejos overlaps with EuroBioC (R/Bioconductor scRNA stats — `BASiCS`). Karlsson overlaps with the canid-genomics + AGBT 2026 platform-launch axis (Darwin's Ark, conservation genomics). Tracking BDS 2026 catches the upstream-methods previews of work that surfaces at AACR 2027 / EuroBioC 2026 / GBCC 2026.

## What we have to work with

| Source | Coverage | Notes |
|---|---|---|
| **CSHL BDS 2026 meeting page** | dates, venue, organizers, six session topics, registration | [meetings.cshl.edu/meetings.aspx?meet=DATA](https://meetings.cshl.edu/meetings.aspx?meet=DATA) |
| **CSHL GI 2025 (prior GI; reference for shape)** | full program (last GI before this slot) | [meetings.cshl.edu/meetings.aspx?meet=info](https://meetings.cshl.edu/meetings.aspx?meet=info) — Nov 5–8, 2025; organizers Iqbal/Langmead/Marchet; keynotes Safonova + Zitnik |
| **CSHL Biological Data Science archives** | prior BDS programs (2020, 2022, 2024) for shape reference | [meetings.cshl.edu/archivesmeetings.aspx?meet=DATA](https://meetings.cshl.edu/archivesmeetings.aspx?meet=DATA) |
| **2026 program / talks list** | **not yet public** | CSHL typically posts the session-by-session program ~6–8 weeks before the meeting (i.e., Sep 2026). Abstract deadline historically falls in early September. |
| **Abstract book** | not yet generated | CSHL posts at `meetings.cshl.edu/posters/data26/data26_AbstractBook.pdf` post-meeting (pattern from prior years) |
| **Slide / recording deposits** | sparse and ad-hoc | CSHL meetings historically have **no central recording**; some speakers deposit to Zenodo or lab sites. #CSHLmeetings on Bluesky catches talk-day reactions. |
| **Sibling vaults** | GBCC 2025 (same venue, summer slot), EuroBioC 2025, RECOMB 2026, ISMB 2026 | already in the corpus — heavy author + tool overlap expected |

## Program shape

CSHL late-fall methods meetings (both GI and BDS) follow a stable 4-day, single-track-with-poster-sessions pattern. The expected 2026 shape based on prior BDS years (2020, 2022, 2024) and the published session list:

- **Day 1 (Wed Nov 4)** — Late-afternoon registration → 7:30 PM opening + **Keynote 1** (typically a senior methods/genomics figure; not yet announced for 2026) → reception.
- **Day 2 (Thu Nov 5)** — **Algorithmics** (sequence algorithms, indexing, pangenomes — upstream-infra bin) + **Population Genetics and Personalized Medicine** (PRS, biobank-scale GWAS, ancestry-aware methods) → afternoon **poster session 1** → evening session.
- **Day 3 (Fri Nov 6)** — **Machine Learning** (foundation models for genomics; deep-learning protein/regulatory; expected agentic-AI talks given 2025 GI agentic-AI track presence) + **Tools, Visualization, and Infrastructure** (Galaxy/Nextflow/AnVIL-adjacent; JBrowse-class viewers; cloud-native pipelines) → **poster session 2** → banquet.
- **Day 4 (Sat Nov 7)** — **Functional Genomics** + **Spatial Genomics and Spatial Biology** (Visium HD, MERFISH/seqFISH analysis, spatial-graph methods — direct EuroBioC / AACR cross-link surface) → closing keynote → lunch + departure.

**Expected counts** (extrapolating from BDS 2024 and GI 2025): ~60–70 oral talks across 6 sessions · 2 keynotes · ~120–150 posters across 2 sessions · ~250 attendees.

> Caveats: 2026-specific keynote speakers, oral-talk titles, and the session-to-day mapping are **not yet announced** as of May 2026. The above is shape inference from prior-year programs, not extracted content. The 2026 program drops typically in Sep 2026; this vault rescaffolds at that point.

## Organization

```
conferences/cshl-bds-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep — dates, venue, sources, expected sessions, cross-vault overlap watch
├── themes.md            # cross-session synthesis (deferred until post-meeting)
├── digest/              # day-by-day recap (deferred until post-meeting)
│   ├── day-1-wednesday.md
│   ├── day-2-thursday.md
│   ├── day-3-friday.md
│   └── day-4-saturday.md
├── topics/              # cross-cutting bins (deferred)
│   ├── algorithmics/                    # pangenomes, indexing, sequence algorithms
│   ├── popgen-personalized/             # PRS, biobank-scale, ancestry-aware
│   ├── machine-learning/                # FM/agentic AI, deep-learning regulatory/protein
│   ├── tools-viz-infra/                 # Galaxy/Nextflow/AnVIL/JBrowse-adjacent
│   ├── functional-genomics/             # regulatory, CRISPR-screen analysis
│   └── spatial/                         # Visium HD, MERFISH analysis, spatial-graph methods
├── tools/               # PRIMARY artifact — one entry per method / package presented
│   └── index.md
└── sessions/            # full per-session abstract index (post-meeting)
    └── index.md
```

The `tools/` directory is the load-bearing artifact, same shape as EuroBioC 2025 / GBCC 2025 / RECOMB 2026. BDS/GI-specific additions to the per-tool template (see [`tools/index.md`](tools/)): a **Session** field naming the BDS 2026 session, a **Preprint** row for bioRxiv (CSHL methods talks almost always have a preprint), and a **Recording: none (CSHL no-record policy)** default that gets flipped to a Zenodo/lab-site link only when a speaker self-deposits.

## What's different from EuroBioC / GBCC / RECOMB / ISMB

- **BDS-not-GI-this-year.** The biggest shape difference from a normal GI year: 2026 is BDS, not GI. The two meetings share venue, week, and community pool but BDS leans slightly more **infrastructure + applied statistics** (population genetics, ML for personalized medicine, Tools/Viz/Infra is its own session) where GI leans slightly more **algorithms + assembly + pangenomes** (PanGenomes is its own session at GI 2025). For our tools matrix the practical difference is small — the same authors present at both.
- **No recordings, sparse slides.** Unlike ISMB (recorded), GBCC (recorded selectively), or RECOMB (occasional YouTube), CSHL meetings have a strict no-recording policy. Post-meeting tool-page enrichment relies on (a) speaker-uploaded slides, (b) preprints, (c) #CSHLmeetings Bluesky/X reactions for talk-day signal.
- **Single-track. Every attendee sees every talk.** Same single-track property as RECOMB. No parallel-session triage during tool-page extraction.
- **High preprint ratio.** Empirically ~85–90% of CSHL methods talks have a bioRxiv preprint at the time of presentation. Tool pages can be scaffolded from preprints alone before the meeting once the program drops.
- **Late-fall slot in the calendar.** Sits between SITC 2026 (Nov 4–8) and RSNA 2026 (Nov 29–Dec 3) on the conference timeline. The audience overlap with SITC is zero; with RSNA is near-zero; with the methods-and-tools conferences (RECOMB May, ISMB Jul, GBCC Jun, Nextflow Summit Oct, EuroBioC Sep) is heavy. BDS 2026 is the methods-axis bookend for the calendar year.

## Sources

- [CSHL Biological Data Science 2026 (the actual meeting in this slot)](https://meetings.cshl.edu/meetings.aspx?meet=DATA)
- [CSHL Genome Informatics 2025 (last GI; reference for shape)](https://meetings.cshl.edu/meetings.aspx?meet=info)
- [CSHL BDS archives (prior BDS programs)](https://meetings.cshl.edu/archivesmeetings.aspx?meet=DATA)
- [CSHL GI archives (prior GI programs)](https://meetings.cshl.edu/archivesmeetings.aspx?meet=INFO)
- [CSHL Meetings homepage](https://meetings.cshl.edu/meetings)
- [CSHL Genetics Meetings 2026/2027](https://meetings.cshl.edu/genetics-meetings)
- [JXTX Foundation (Taylor Foundation graduate scholarships — historically funds both GI and BDS attendees)](https://jxtxfoundation.org/)

## Next step

- **Now (pre-meeting, May 2026):** scaffold per-tool template ([`tools/`](tools/)) and identify cross-vault overlap candidates from prior-year (BDS 2024, GI 2025) speaker rosters. See [`program-notes.md`](program-notes.md) for the overlap watch list.
- **When the program drops (~Sep 2026):** extract speaker list, talk titles, session mapping; pre-scaffold ~30–40 tool pages from preprints linked off speaker pages.
- **During the meeting (Nov 4–7, 2026):** real-time capture of keynote speakers (announced from stage), poster-session standouts via #CSHLmeetings social.
- **Post-meeting (Nov 8+, 2026):** bulk tool-page extraction; cross-vault link sweep against EuroBioC 2025 / GBCC 2025 / RECOMB 2026 / ISMB 2026 / Nextflow Summit 2026.
- **GI 2027 (Nov 2027):** new vault for the next true Genome Informatics meeting. Schatz/Iqbal/Langmead-class organizer roster expected.
