# ISMB 2026

**34th Intelligent Systems for Molecular Biology (ISMB) Conference** — Washington Hilton, Washington, DC, USA · July 12–16, 2026. Hybrid (in-person + ISCB Nucleus virtual platform).

> **Status:** Scaffold — meeting upcoming (~9 weeks out as of May 11, 2026); structure landed now so bulk per-tool extraction can run immediately after the meeting closes Jul 16, 2026. Program shape is fixed (day-by-day COSI grid published), keynote slate is announced, accepted-paper list is not yet public.

> **One factual correction up front:** the original task brief listed this as the joint ISMB/ECCB year in Liverpool. That was last year — **ISMB/ECCB 2025** ran Jul 20–24, 2025 in Liverpool. **ISMB 2026** is ISMB-only in Washington, DC. **ECCB 2026** is a separate event (Geneva, Aug 31–Sep 4, 2026, "Biodiversity, AI & Health" theme); we treat ECCB 2026 as a possible future sister vault, not folded into this one.

## Why this is in the vault

- **Methods-and-tools depth.** ISMB is the largest computational-biology meeting (~2000–3000 attendees) and the one venue where methods underlying tools like CHIEF, GigaPath, Geneformer, scGPT, Cell2location, SpatialData, SCimilarity, and PerturbNet get peer-reviewed and presented. Many tools we've already documented from EuroBioC2025 / GBCC2025 (msqrob2, edgeR, SpatialData, Voyager, plyxp, Tidyomics, OSTA, signifinder, sosta, footprintR, …) re-surface here with updates, methods papers, or new downstream uses.
- **Formal peer-reviewed proceedings.** Unlike EuroBioC / GBCC (community workshops with informal talk selection), ISMB has a real two-round peer-reviewed proceedings track that publishes in *Bioinformatics* (Oxford University Press) ~1 month before the meeting. Tool entries from ISMB can cite a published DOI — a depth the community-conference vaults don't get.
- **AACR axis fit.** Six ISMB COSIs map directly onto the AACR vault's axes: **MLCSB** (foundation models / scGPT-class), **TransMed** (translational), **BioVis** (figure / dashboard tooling), **HiTSeq** (sequencing methods used in cancer cohorts), **VarI** (somatic variant interpretation), **NetBio** (pathway / network methods). MICROBIOME, RegSys, Function, 3DSIG, CompMS, BOSC, and EvolCompGen feed adjacent axes (cancer-microbiome, regulatory genomics, structural drug-target work, proteomics, open-source infrastructure).
- **Cross-vault people overlap.** The Robinson lab (Zurich), Love lab (UNC), Carey (Channing/Harvard), Soneson (FMI), Mangiola (Adelaide), Castelo (UPF), Borman (Turku), Marconato (EMBL), and the broader scverse / SpatialData crowd typically split between EuroBioC, GBCC, and ISMB each year. We expect substantial speaker overlap to drive cross-vault links.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Abridged agenda (PDF)** | full 5-day grid by room and COSI | [programme.AbridgedAgenda.ISMB.2026.pdf](https://www.iscb.org/documents/programmes/programme.AbridgedAgenda.ISMB.2026.pdf) — already extracted in `program-notes.md` |
| **Distinguished Keynotes page** | 5 plenary speakers, talk titles for 2 | [iscb.org/ismb2026/whats-happening/distinguished-keynotes](https://www.iscb.org/ismb2026/whats-happening/distinguished-keynotes) |
| **Track Details page** | all COSI + special + open tracks | [iscb.org/ismb2026/whats-happening/track-details](https://www.iscb.org/ismb2026/whats-happening/track-details) |
| **Proceedings (*Bioinformatics* journal)** | peer-reviewed full papers | online-only OUP special issue, posted ~1 month pre-conference; CC-BY; ~$700 author APC. Submission window Nov 11, 2025 – Jan 20, 2026 (closed); notifications May 5, 2026; APC due May 7, 2026. **Accepted-paper list not yet public as of May 11**. |
| **Per-COSI sites** | per-track speaker rosters | each COSI runs its own page (e.g., [microbiome-cosi.org/ismb-2026](https://www.microbiome-cosi.org/ismb-2026/overview), [evolcompgen.org/ismb_2026](https://evolcompgen.org/doku.php?id=meetings:ismb_2026)) — populated as accept notifications go out from May 5 |
| **BOSC 2026 site** | Bioconductor / open-source track inside ISMB | [open-bio.org/events/bosc-2026/](https://www.open-bio.org/events/bosc-2026/) — 2 keynotes (Eric Green, Maryam Zaringhalam) + 2 panels |
| **ISCB Nucleus platform** | virtual + on-demand recordings | post-meeting; logged-in registrants get on-demand video for ~6 months |
| **Preprints** | bioRxiv preprints flagged "to appear in ISMB 2026" | typical pattern — most ISMB Proceedings papers have a bioRxiv mirror filed Jan–Mar 2026 |
| **Slide deposits** | uneven; some on Zenodo, some on speaker labs | no central Zenodo community for ISMB; expect ad-hoc per-speaker |
| **Press / social** | extensive; #ISMB2026 on Bluesky, Mastodon, X | useful for tracking real-time talk reactions; not a primary source |

## Program shape

ISMB 2026 runs Sunday Jul 12 (tutorials + opening keynote) through Thursday Jul 16 (closing keynote). Mon–Thu morning starts with a Distinguished Keynote followed by 11 parallel COSI / special-track sessions in three slots (11:00–13:00, 14:20–16:00, 16:40–18:00). The Sunday day-zero is tutorials + Student Council Symposium + DREAM Challenge.

**Counts:**

- **5 Distinguished Keynotes** (one per day, ~1 hour each)
- **22 COSI tracks** + 7 special / closed tracks + 1 Open Session ("Bioinformatics in the USA") + 1 equity track + 1 publishing session + Industry Workshop + Pathogen Data Network forum + NIH/ODSS
- **9 tutorials** (IP1–IP9), all Sunday Jul 12, full-day
- **>600 expected scientific talks** (per ISCB's own framing)
- **Two posters-and-exhibitors blocks per day** (morning + afternoon coffee), Mon–Thu
- **BOSC 2026 nested inside** — Jul 14–15, runs as a 2-day COSI within ISMB
- **CollaborationFest (CoFest)** Jul 17–18, separate registration, hackathon-style follow-on (sister event to GBCC2025's CoFest)

## Organization

```
conferences/ismb-2026/
├── index.md             # this page
├── program-notes.md     # internal working file — day-by-day grid + COSI shortlist
├── themes.md            # cross-day synthesis (deferred until post-meeting)
├── digest/              # day-by-day recap (deferred until post-meeting)
│   ├── day-0-sunday.md      # tutorials + SCS + DREAM + Durbin keynote
│   ├── day-1-monday.md      # Troyanskaya + HitSeq/iRNA/RegSys/Microbiome/CompMS/...
│   ├── day-2-tuesday.md     # Majumder + HitSeq/iRNA/RegSys/NetBio/SysMod/BioVis/BOSC/...
│   ├── day-3-wednesday.md   # Zitnik + MLCSB/TransMed/3D/NetBio/EvolCompGen/VarI/BOSC/CAMDA/...
│   └── day-4-thursday.md    # MLCSB/3D/EvolCompGen/CAMDA + Bustamante closing
├── keynotes/            # one entry per distinguished keynote (deferred)
├── topics/              # cross-cutting bins (deferred)
│   ├── foundation-models/   # MLCSB-heavy (Zitnik, Troyanskaya keynotes feed this)
│   ├── spatial-imaging/     # MLCSB + RegSys + BioVis overlap
│   ├── single-cell/         # MLCSB + RegSys + Function overlap
│   ├── variant-interpretation/   # VarI + TransMed
│   ├── microbiome/          # Microbiome COSI
│   ├── proteomics-massspec/ # CompMS + Function
│   ├── open-source-infra/   # BOSC + BOKR
│   └── translational/       # TransMed + Industry Workshop + NIH/ODSS
├── tools/               # PRIMARY artifact — one entry per package / method
│   └── index.md
└── sessions/            # full abstract index (post-meeting, after accept notifications)
    └── index.md
```

The `tools/` directory is the load-bearing artifact, same shape as EuroBioC2025 and GBCC2025. ISMB-specific additions to the per-tool template (see [`tools/index.md`](tools/)): a **Proceedings** row pointing to the published *Bioinformatics* DOI when applicable, and a **COSI track** field to make the cross-COSI traffic visible (e.g., a single-cell method may land in MLCSB but be benchmarked against RegSys).

## What's different from EuroBioC / GBCC

- **Scale.** EuroBioC ~250 attendees, GBCC ~300. ISMB ~2000–3000 attendees, >600 talks, 22 parallel tracks. Per-tool extraction will be substantially larger — the constraint is reviewer bandwidth, not source availability.
- **Peer-reviewed proceedings.** Every accepted proceedings paper has a DOI before the meeting, so tool pages here will be unusually "complete" — DOI + GitHub + benchmarks + figures — even before talks happen.
- **Domain breadth.** EuroBioC = Bioconductor (R). GBCC = Galaxy + Bioconductor. ISMB spans Python, R, C++, Julia, web, cloud, and quantum (yes — Q4LS / Quantum for Life Sciences runs as a Tuesday track). Tool entries cannot assume any one ecosystem.
- **Awards and recognition arc.** ISMB hands out four ISCB awards in 2026 (Senior Scientist → Durbin; Innovator → Troyanskaya; Overton → Zitnik; plus career awards for fellows). Keynote treatments need an "award arc" note that the EuroBioC / GBCC keynotes don't have.
- **BOSC + Bioconductor-2026 spillover.** BioC2026 is Aug 10–12, 2026 in Seattle — a month after ISMB. Many Bioconductor speakers present at BOSC during ISMB and then again at BioC2026. Tool entries built from BOSC at ISMB will need to anticipate a BioC2026 re-up.

## Sources

- [ISMB 2026 home](https://www.iscb.org/ismb2026/home)
- [ISMB 2026 abridged agenda PDF](https://www.iscb.org/documents/programmes/programme.AbridgedAgenda.ISMB.2026.pdf)
- [Distinguished Keynotes](https://www.iscb.org/ismb2026/whats-happening/distinguished-keynotes)
- [Track Details](https://www.iscb.org/ismb2026/whats-happening/track-details)
- [Call for Proceedings](https://www.iscb.org/ismb2026/call-for-submissions/proceedings)
- [Call for Abstracts](https://www.iscb.org/ismb2026/call-for-submissions/abstracts)
- [Key Dates](https://www.iscb.org/ismb2026/key-dates)
- [BOSC 2026 page (Open Bioinformatics Foundation)](https://www.open-bio.org/events/bosc-2026/)
- [BOSC 2026 keynotes](https://www.open-bio.org/events/bosc-2026/bosc-2026-keynotes/)
- [Microbiome COSI @ ISMB 2026](https://www.microbiome-cosi.org/ismb-2026/overview)
- [EvolCompGen COSI @ ISMB 2026](https://evolcompgen.org/doku.php?id=meetings:ismb_2026)
- [MLCSB COSI home](https://cosi.iscb.org/wiki/MLCSB:Home)
- [Bioconductor 2026 (sister event, Aug 10–12 Seattle)](https://bioc2026.bioconductor.org/)
- [ECCB 2026 (separate event, Aug 31–Sep 4 Geneva)](https://eccb2026.org/)
- *Bioinformatics* (OUP) — proceedings publication venue

## Next step

- **Now (pre-meeting):** monitor for the public accepted-papers list. Notifications to authors go out May 5, 2026; the *Bioinformatics* supplement typically posts ~mid-June. Once the list is public we can scaffold likely tool pages from titles + bioRxiv pairs without waiting for the meeting.
- **During the meeting (Jul 12–16):** real-time capture of slide DOIs / Zenodo deposits via #ISMB2026 social.
- **Bulk tool-page extraction (immediately post-meeting, Jul 17+):** roughly 60–120 candidate entries spanning the proceedings papers + COSI-invited talks. Existing-in-corpus tools (Tidyomics, edgeR, SpatialData, signifinder, OSTA, msqrob2, sosta, footprintR, plyxp, mia, Voyager) get an "ISMB 2026 update" section appended; new ISMB-debuting tools get fresh entries.
- **CoFest follow-up (Jul 17–18):** capture any Bioconductor↔Galaxy↔ISMB tool wrapping artifacts that emerge (parallel to GBCC2025 CoFest's GSVA wrapper deliverable).
