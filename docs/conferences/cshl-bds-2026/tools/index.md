# CSHL GI 2026 (Biological Data Science slot) — Tools

CSHL late-fall methods meetings — both Genome Informatics (odd years) and Biological Data Science (even years, including 2026) — are tools-dense by design. The 2026 program is **Biological Data Science**, Nov 4–7, with six sessions (Algorithmics, Population Genetics & Personalized Medicine, Machine Learning, Tools/Visualization/Infrastructure, Functional Genomics, Spatial Genomics & Spatial Biology). Based on shape inference from BDS 2024 and GI 2025, expect ~60–70 oral talks and ~120–150 posters; **most oral talks introduce or update a methods package** with an associated bioRxiv preprint.

> **Status:** Template stub — meeting is upcoming (~6 months out as of May 2026). Per-tool entries are queued for post-meeting bulk extraction. Pre-meeting prep (which methods/groups are likely to present, cross-vault overlap candidates) lives in [`../program-notes.md`](../program-notes.md).

## Per-tool entry template

Each tool gets its own page (`tools/<package-slug>.md`) following this structure. This is the EuroBioC2025 / GBCC2025 / RECOMB2026 template adapted for CSHL's no-recording policy and biennial-slot context:

````markdown
# <PackageName>

**One-line description** — what the package does in plain language.

- **Maintainer:** <name> (<institution>)
- **Repo:** [GitHub link]
- **Docs / vignette:** [link]
- **Bioconductor / PyPI / Bioconda:** [package page if applicable]
- **Status at CSHL BDS 2026:** new release / major update / methods talk / case study / poster

## Talk / poster at CSHL BDS 2026

- **Speaker / first author:** ...
- **Session:** Algorithmics / PopGen & Personalized Medicine / ML / Tools-Viz-Infra / Functional Genomics / Spatial
- **Day:** Day 1 (Wed Nov 4) / Day 2 (Thu Nov 5) / Day 3 (Fri Nov 6) / Day 4 (Sat Nov 7)
- **Format:** invited / contributed talk / lightning / poster
- **Preprint:** [bioRxiv DOI] — ~85–90% of CSHL methods talks have one at the time of presentation
- **Slides:** [Zenodo / lab-site link] or "(not deposited — CSHL no-record policy; check #CSHLmeetings Bluesky for talk-day reactions)"
- **Recording:** none (CSHL meeting policy)
- **Abstract:** [link to CSHL abstract book PDF when posted]

## What it does

2–3 sentences: the problem it solves, key methodological idea, what it consumes/produces, benchmarks claimed.

## Where it fits in the corpus

- AACR 2026: [link if mentioned]
- AACR 2027: [forward link if author has AACR-axis applications]
- ISMB 2026: [link if mentioned]
- RECOMB 2026: [link if mentioned]
- EuroBioC 2025: [link if Bioconductor-adjacent]
- GBCC 2025: [link if Galaxy-wrapped or sibling-venue overlap]
- Nextflow Summit 2026: [link if pipeline-component]

## Notes

Free-form impressions, benchmarks claimed, comparisons to alternatives, social-media reactions from talk day, post-meeting preprint-to-journal status.
````

## Per-tool entry — fields specific to CSHL BDS / GI

Three template additions vs. the EuroBioC base shape:

- **Session field** names the BDS 2026 session (one of the six). The session label is load-bearing — a "spatial-omics methods talk" in the Spatial Genomics session has a different downstream audience and citation graph than a "spatial-omics methods talk" in the Functional Genomics session.
- **Recording field defaults to "none"** because CSHL has a no-record policy. The field gets overwritten only when a speaker independently deposits a recording (rare; happens via Zenodo or YouTube). Slides are similarly opt-in — track Zenodo + speaker lab pages for ~2–4 weeks post-meeting.
- **Preprint field is mandatory.** CSHL methods talks almost always have a bioRxiv preprint by the time of presentation. The preprint is the single most reliable artifact for tool-page enrichment given the absence of recordings.

## Tool index

Template stub. **No entries yet** — the BDS 2026 program is not public as of May 2026. CSHL typically posts session-by-session schedules in early September; abstract deadlines fall in early September; the abstract book is posted post-meeting.

| Package | Domain | Speaker | Session | Day | Preprint | Slides | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|
| *(pending program release)* | — | — | — | — | — | — | — |

**Anticipated entry count:** ~30–40 tool pages (extrapolating from BDS 2024 = ~58 oral talks, of which ~30 introduced a named tool/package, plus ~5–10 poster-only tools with strong preprint signal).

## Tool-page extraction plan

1. **When the program drops (~Sep 2026):** extract the full speaker list + talk titles + session-to-day mapping into `_program-extracted.md` (working file).
2. **Pre-meeting (Sep–Oct 2026):** for each oral-talk title, look up the speaker's recent bioRxiv preprints. Match preprint → talk. Scaffold tool-page skeletons with preprint + speaker affiliation + session + day filled.
3. **During the meeting (Nov 4–7):** track #CSHLmeetings on Bluesky/X for talk-day signal (audience reactions, benchmark claims, methodological surprises). Add a "talk-day reactions" line to relevant tool pages.
4. **Post-meeting (Nov 8+):** abstract book drops on CSHL site; backfill abstract links + clarify any ambiguities. Run cross-vault link sweep — every tool gets evaluated against EuroBioC 2025, GBCC 2025, RECOMB 2026, ISMB 2026, AACR 2026, Nextflow Summit 2026 for mention/use.
5. **Slide-deposit re-sweep (~4 weeks post-meeting, early Dec 2026):** ~30–50% of speakers will have deposited slides to Zenodo or lab sites by then. Backfill the Slides field.

## Why this format

- **Cross-vault links are the value-add.** A BDS 2026 spatial-omics methods talk often presents the algorithmic substrate that surfaces six months later as an EuroBioC 2026 short talk or an AACR 2027 cancer-research poster. The per-tool page is the one place that chain becomes navigable.
- **Preprint-first reflects CSHL reality.** No recordings → preprints become the canonical artifact. This is different from EuroBioC (Zenodo slides primary) or ISMB (mixed slides + selective recordings) or RECOMB (proceedings papers primary).
- **Session field enables topic-bin slicing** without duplicating into `topics/` pages. The six BDS 2026 sessions map cleanly to the topic bins in [`../`](../).

## Open questions for the pilot

1. **Whether to fold GI 2025 tools into this vault retroactively** — GI 2025 ran Nov 5–8, 2025 with strong tool density (Iqbal/Langmead/Marchet's program included PanGenomes, Single-Cell + Spatial, AI/ML/Integrative Omics sessions; keynotes by Safonova on adaptive-immune-repertoire methods + Zitnik on therapeutic-graph FMs). Currently flagged as a *separate retroactive vault target* (`cshl-gi-2025/`), not folded into this 2026 vault. Decision deferred until post-BDS 2026.
2. **Poster handling** — CSHL posters often have preprints but no slides. The current template treats posters as first-class entries with a `Format: poster` field. If post-meeting volume is high (~50+ poster-with-preprint entries), may need a lighter-weight `posters/index.md` table rather than full per-poster pages.
3. **Sibling-vault link target ambiguity** — for talks where the author has both an EuroBioC entry (Bioconductor package) and a GBCC entry (Galaxy wrapper) and a BDS entry (latest methods preprint), which is the canonical page? Current convention: tool-debut venue is canonical; later venues link back. Spot-check needed once entries populate.
4. **GI 2027 hand-off** — when the next true Genome Informatics meeting runs (Nov 2027), authors who present *both* at BDS 2026 and GI 2027 will have entries in both vaults. Plan: append a "CSHL GI 2027 update" section to the BDS 2026 page rather than create a duplicate.
