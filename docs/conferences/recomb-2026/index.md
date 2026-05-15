# RECOMB 2026

**30th Annual International Conference on Research in Computational Molecular Biology** — Thessaloniki Concert Hall, Thessaloniki, Greece · May 26–29, 2026. In-person. Satellite workshops + H.bioinfo'17 run May 24–25.

> **Status:** Scaffold landed pre-meeting (~15 days out as of May 11, 2026). Program is fixed (full session-by-session schedule public), all 4 keynote speakers announced, and the **complete 65-paper accepted-list is already public** — so unlike ISMB 2026 (where the proceedings list is still embargoed in May), RECOMB 2026 tool-page extraction can be scaffolded *before* the meeting from titles + bioRxiv preprints, then enriched with talk-day metadata + slide DOIs immediately post-meeting.

> **One factual correction up front:** the task brief framed RECOMB 2026 as having "concluded last month." It hasn't — the conference runs **May 26–29, 2026**, which is ~2 weeks in the future as of today (May 11, 2026). The build-out below treats the meeting as upcoming. The accepted-papers list and program schedule are already public; what's missing is talk delivery, best-paper announcements, and slide/recording deposits.

## Why this is in the vault

- **Pure methods/algorithms venue.** RECOMB is the premier theoretical computational-biology conference — smaller and tighter than ISMB (65 accepted papers vs. ISMB's ~600 talks), peer-reviewed proceedings, no industry/translational/community tracks to wade through. Every accepted paper is a methods or algorithms contribution with a code repo. Highest signal-to-noise ratio of any vault we maintain.
- **Foundational-method pipeline upstream of AACR.** RECOMB papers tend to be the algorithmic substrate (alignment, phylogeny, single-cell statistics, foundation-model architectures, privacy-preserving inference) that *later* shows up productized at ISMB, applied at AACR, or wrapped at Nextflow Summit / BOSC. Watching RECOMB lets us anticipate which tools will surface at AACR 2027 / EuroBioC 2026 / GBCC 2026.
- **AACR axis fit — narrower but deep.** The 65-paper program breaks down into 6 tight bins: **single-cell** (CAMP, DiCoLo, scDesignPop, MOSAIC, scProfiterole, GeoAdvAE, Gene-First, CycleGRN, DeltaNMF, error-correction, Nullstrap-DE, Information-Geometry), **cancer evolution** (Arborist, Cycle-Extractor for ecDNA, POTTR, subclonal tree alignment), **spatial omics** (MOSAICField, DIME, LineageMap), **protein/ML** (ProtFlow, MutPred-PPI, MSA-Transformer hybrids, foundation-model adapters, synthetic-lethality predictors), **statistical/privacy genetics** (Private PRS leakage, GOPHER, biobank G×E, pangenome privacy), and **sequence/phylogeny algorithms** (Cuttlefish 3, PBWT/SLAB, minimizers, quartet trees, STELAR-X). Bins 1–4 are directly relevant to AACR; bin 5 is relevant to AACR-axis privacy/PRS work; bin 6 is upstream infrastructure.
- **Cross-vault people overlap.** Bonnie Berger (MIT, steering chair) and Anna Sappington (Berger lab) appear on 2 RECOMB papers and overlap with ISMB MLCSB. Olga Troyanskaya (Princeton, ISMB 2026 keynote on Mon Jul 13) co-authors a RECOMB paper here (Aggarwal/Sokolova/Troyanskaya on multi-modal tissue-aware GNN). Sara Mostafavi (RECOMB keynote Fri May 29) co-authors paper #19 ("Deep genomic models of allele-specific measurements"). Ben Raphael (Princeton) is on 3 papers. Rob Patro is on Cuttlefish 3 (paper #49) — same person whose tximeta/fishpond surfaces at GBCC 2025 and ISMB 2026 (BOSC). Jingyi Jessica Li (UCLA) authors 3 papers (Information-Geometry, Nullstrap-DE, scDesignPop) — high-overlap with ISMB MLCSB.

## What we have / will have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Accepted-papers page** | full 65-paper list, titles + author lists, no abstracts | [recomb.org/recomb2026/accepted_papers.html](http://recomb.org/recomb2026/accepted_papers.html) — extracted in `program-notes.md` |
| **Program schedule page** | 14 sessions across 4 days, 4 keynotes, paper-to-session mapping | [recomb.org/recomb2026/program.html](http://recomb.org/recomb2026/program.html) — extracted in `program-notes.md` |
| **Keynotes page** | 4 distinguished speakers; talk titles not yet public | [recomb.org/recomb2026/keynotes.html](http://recomb.org/recomb2026/keynotes.html) — speaker images only; titles likely posted day-of or via Twitter/Bluesky |
| **Committees page** | steering, program chair, organizing, posters, fellowships | [recomb.org/recomb2026/committees.html](http://recomb.org/recomb2026/committees.html) |
| **Call for Papers** | proceedings + dual-submission rules; **no Springer LNBI this year** | [recomb.org/recomb2026/call_for_papers.html](http://recomb.org/recomb2026/call_for_papers.html) |
| **Proceedings (no LNBI)** | RECOMB 2026 **breaks the LNBI tradition** — papers route to partnering journals instead | Partnering journals: **Cell Systems**, **Genome Research**, **Journal of Computational Biology** (default special-issue venue). Authors of selected papers may be invited to submit expanded versions to Cell Systems or Genome Research for expedited review; the remainder land in a JCB special issue. |
| **bioRxiv / arXiv preprints** | most RECOMB papers have a public preprint | [recomb.org/proceedings/proceedings/2030-2026/2026/](https://recomb.org/proceedings/proceedings/2030-2026/2026/) is the running proceedings hub and includes preprint links per paper |
| **Satellite-workshop sites** | 7 satellites Sun–Mon May 24–25 | RECOMB-Seq, RECOMB-CCB, RECOMB-CG, RECOMB-Genetics, RECOMB-Privacy, RECOMB-Arch, RECOMB-RSG. H.bioinfo'17 also May 25. Per-satellite programs at recomb-seq.github.io, recomb-cg.org, etc. — populated separately. |
| **Slide deposits** | ad-hoc; no central RECOMB Zenodo community | Expect lab-site or speaker-Bluesky deposits. Berger lab + Mirarab lab + Klau lab historically deposit slides; many others don't. |
| **Recordings** | RECOMB main program traditionally **not recorded** | Recheck post-meeting; some sessions occasionally posted to the RECOMB YouTube channel ~6–10 weeks late |
| **Press / social** | #RECOMB2026 on Bluesky + X | useful for talk reactions and best-paper announcements (named on stage at the closing session, Fri May 29) |

## Program shape

RECOMB 2026 runs Tue May 26 through Fri May 29, single-track main program (no parallel sessions during the conference proper). Each day has 3–4 paper sessions of 3–6 talks each, plus 1 keynote (Tue/Wed/Thu/Fri). Total: **14 paper sessions, 65 contributed talks, 4 keynotes**. Satellites + H.bioinfo'17 run on the two days before (Sun May 24 + Mon May 25) as parallel side events; same venue but different rooms.

**Counts:**

- **4 Distinguished Keynotes:** Paul Medvedev (Tue), Gene Myers (Wed), Alexandros Stamatakis (Thu), Sara Mostafavi (Fri)
- **14 paper sessions** organized by topic: Sequence I/II, Protein/ML I/II, Single-Cell I/II/III, Multi-Omics, Small Molecules, Transcriptomics, Phylogeny I/II, Cancer & Evolution, Statistical Genetics
- **65 peer-reviewed accepted papers** (PC Chair: Rayan Chikhi, Institut Pasteur; PC ~100 members)
- **7 satellite workshops** May 24–25 (RECOMB-Seq, -CCB, -CG, -Genetics, -Privacy, -Arch, -RSG) + H.bioinfo'17 (Hellenic Bioinformatics Society) May 25
- **Posters** — multiple sessions; not yet enumerated by the public page (Posters Chair: Kaiyuan Zhu)
- **No industry track, no tutorials, no parallel "special tracks"** — single-track main program is the entire conference. This is the major shape difference from ISMB.

## Organization

```
conferences/recomb-2026/
├── index.md             # this page
├── program-notes.md     # internal working file — full 65-paper list + day-by-day grid + tool shortlist
├── themes.md            # cross-session synthesis (deferred until post-meeting)
├── digest/              # day-by-day recap (deferred until post-meeting)
│   ├── day-1-tuesday.md     # Medvedev keynote + Sequence I + Protein/ML I + Single-Cell I
│   ├── day-2-wednesday.md   # Myers keynote + Sequence II + Multi-Omics + Small Molecules + Transcriptomics
│   ├── day-3-thursday.md    # Stamatakis keynote + Phylogeny I/II + Single-Cell II + Cancer & Evolution
│   └── day-4-friday.md      # Mostafavi keynote + Protein/ML II + Statistical Genetics + Single-Cell III + closing/best-paper
├── keynotes/            # one entry per keynote (deferred)
├── satellites/          # per-satellite-workshop entries (deferred; populated from per-satellite sites)
│   ├── recomb-seq.md
│   ├── recomb-ccb.md
│   ├── recomb-cg.md
│   ├── recomb-genetics.md
│   ├── recomb-privacy.md
│   ├── recomb-arch.md
│   └── recomb-rsg.md
├── topics/              # cross-cutting bins (deferred)
│   ├── single-cell-methods/      # 12+ papers across Sessions 3, 9, 14
│   ├── cancer-evolution/         # Session 11 (Arborist, ecDNA, POTTR, subclonal trees)
│   ├── spatial-omics/            # MOSAICField, DIME, LineageMap (Sessions 5+9)
│   ├── protein-ml/               # Sessions 2 + 12
│   ├── privacy-statgen/          # Session 13 + PangenomePrivacy + GOPHER + PRS-leakage
│   └── sequence-phylogeny/       # Sessions 1, 4, 8, 10 — upstream-infra bin
├── tools/               # PRIMARY artifact — one entry per package / method
│   └── index.md
└── sessions/            # full per-session abstract index (post-meeting)
    └── index.md
```

The `tools/` directory is the load-bearing artifact, same shape as EuroBioC2025 / GBCC2025 / ISMB 2026. RECOMB-specific additions to the per-tool template (see [`tools/index.md`](tools/)): a **Proceedings** row pointing to the partnering-journal DOI (Cell Systems / Genome Research / JCB) when known, a **Session** field naming the RECOMB session (e.g., "Session 11: Cancer & Evolution"), and a **Preprint** row for the bioRxiv/arXiv link that exists for most papers.

## What's different from EuroBioC / GBCC / ISMB

- **Pure-methods filter.** EuroBioC = R/Bioconductor community workshop. GBCC = Galaxy + Bioconductor joint, applied focus. ISMB = 22-track everything-soup with industry + tutorials + BOSC + COSI politics. RECOMB = **algorithms only**, single track, peer-reviewed proceedings. Every accepted paper is a tool/method/theory contribution. Tool-page coverage ratio is the highest of any vault: 65 papers → likely ~50–60 tool pages.
- **No Springer LNBI this year.** Previous RECOMB years published proceedings as a single Springer Lecture Notes in Bioinformatics (LNBI) volume. RECOMB 2026 breaks this tradition: papers route to **Cell Systems**, **Genome Research**, or **Journal of Computational Biology** (default). This raises the citation profile per paper but means DOI lookup is per-paper, not per-volume — slows down tool-page enrichment vs. an LNBI year.
- **Smaller scale, single track.** ~250–400 attendees (vs. ISMB ~3000, EuroBioC ~250, GBCC ~300). No parallel sessions during the main program — so unlike ISMB, every attendee sees every talk. Tool-page extraction doesn't need a parallel-track triage step.
- **No tutorials, no BOSC equivalent.** RECOMB-CCB and RECOMB-RSG are the closest analogues to applied tracks, but they're separate satellites on May 24–25 — not nested inside the main program. Bioconductor / scverse / Galaxy ecosystem packages **rarely** debut at RECOMB; when they do, it's the underlying algorithm paper, not the package release.
- **Heavy phylogeny / sequence-algorithm load.** ~20 of 65 papers (≈30%) are in Sessions 1, 4, 8, 10 — pure sequence algorithms, phylogenetic inference, pangenome indexing, minimizers, PBWT, de Bruijn graphs. This bin has minimal AACR axis fit and is treated as upstream infrastructure (one paragraph per paper in `topics/sequence-phylogeny/`, not full tool pages unless the artifact is a maintained tool with a release — e.g., Cuttlefish 3, MaxGeomHash).
- **Closing-day best-paper announcement.** RECOMB traditionally announces best-paper and best-student-paper awards at the closing session (Fri May 29 PM). Updating the vault to flag winners is a same-day post-meeting task.

## Sources

- [RECOMB 2026 home](http://recomb.org/recomb2026/)
- [Accepted Papers](http://recomb.org/recomb2026/accepted_papers.html) (65 papers)
- [Program Schedule](http://recomb.org/recomb2026/program.html)
- [Keynotes](http://recomb.org/recomb2026/keynotes.html)
- [Committees](http://recomb.org/recomb2026/committees.html)
- [Call for Papers](http://recomb.org/recomb2026/call_for_papers.html)
- [RECOMB Proceedings hub](https://recomb.org/proceedings/proceedings/2030-2026/2026/)
- [RECOMB Conference Series](https://recomb.org/)
- [RECOMB Satellite Meetings index](https://recomb.org/satellites/)
- [RECOMB-Seq satellite](https://recomb-seq.github.io/)
- [RECOMB-CG satellite](https://recomb-cg.org/)
- *Cell Systems* / *Genome Research* / *Journal of Computational Biology* — partnering journals

## Next step

- **Now (pre-meeting, May 11–26):** the accepted-paper list is already public, so scaffold likely tool pages from titles + bioRxiv preprints. The `program-notes.md` shortlist below identifies the ~12–15 highest-priority entries. No need to wait.
- **During the meeting (May 26–29):** real-time capture of (a) keynote talk titles when announced from stage, (b) best-paper / best-student-paper award winners at the closing session Fri May 29, (c) slide deposits posted to #RECOMB2026 social, (d) any preprint-to-journal redirects (Cell Systems / Genome Research / JCB acceptances announced at the closing).
- **Satellite-workshop pass (May 24–25):** scaffold the 7 satellites + H.bioinfo'17 in `satellites/`. Each gets its own page with workshop-specific accepted-papers list (separate from main RECOMB).
- **Bulk tool-page extraction (post-meeting, May 30+):** ~50–60 candidate entries spanning the 65 papers. Existing-in-corpus tools (Cuttlefish, Voyager-adjacent spatial work, SpatialData spillovers, Tidyomics-adjacent statistical-genetics work) get an "RECOMB 2026 update" section appended; new RECOMB-debuting tools get fresh entries.
- **Partnering-journal DOI sweep (Jul–Sep 2026):** the partnering-journal track means each accepted paper acquires a final DOI on a per-paper schedule, not a single LNBI volume drop. Plan a re-sweep in Jul / Sep to backfill *Cell Systems* / *Genome Research* / *JCB* DOIs into the tool-page Proceedings rows.
