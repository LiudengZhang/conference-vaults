# ISMB 2026 — Tools

ISMB 2026 will run ~5 distinguished keynotes + ~600 scientific talks across 22 COSI tracks + nested BOSC + special tracks (NIH/ODSS, Industry Workshop, Pathogen Data Network, Q4LS) + 9 full-day Sunday tutorials. The subset that yields tool pages is the intersection of (a) Proceedings papers published in *Bioinformatics* (peer-reviewed full papers with DOIs), (b) COSI-invited talks that announce a named package or method, and (c) BOSC talks that introduce a Bioconductor / Galaxy / scverse / open-source tool. **Ecosystem field = `Bioconductor / scverse / Galaxy / standalone-Python / standalone-R / web-service / C++`** — broader than EuroBioC's R-only and GBCC's R+Galaxy.

> **Status:** Template stub. Per-tool format proposed here for review *before* bulk extraction runs immediately after the meeting closes (Jul 16, 2026). Once locked, expected ~60–120 entries get populated from the proceedings-paper list + COSI program books.

## Per-tool entry template

Each tool gets its own page (`tools/<package-slug>.md`) following this structure. The shape mirrors EuroBioC2025 and GBCC2025 with two ISMB-specific additions (a Proceedings DOI row, a COSI track field):

````markdown
# <ToolName>

**One-line description** — what the tool does in plain language.

- **Maintainer:** <name> (<institution>)
- **Ecosystem:** Bioconductor / scverse / Galaxy / standalone-Python / standalone-R / web-service / C++ / other
- **Package / source:** [GitHub link]
- **Docs / vignette:** [link]
- **Status at ISMB 2026:** new release / major update / proceedings paper / methods talk / case study / tutorial / BOSC demo
- **Proceedings:** [*Bioinformatics* DOI if applicable — null for COSI-invited / methods talks]

## Talk at ISMB 2026

- **Speaker:** ...
- **Day / COSI track:** Mon Jul 13 / MLCSB · Tue Jul 14 / RegSys · etc.
- **Session slot:** 11:00–13:00 | 14:20–16:00 | 16:40–18:00
- **Slides:** [Zenodo DOI or lab site]
- **Video:** [ISCB Nucleus on-demand link if posted]
- **Abstract / talk page:** [ISMB program link]

## What it does

2–3 sentences: the problem it solves, the key methodological idea, what it consumes/produces, what it's benchmarked against.

## Where it fits in the corpus

- AACR 2026: [link if mentioned]
- EuroBioC 2025: [link if mentioned]
- GBCC 2025: [link if mentioned]
- BioC 2026: [link if mentioned — Aug 10-12 Seattle, likely re-up for Bioconductor speakers]
- Nextflow Summit 2026: [link if mentioned]
- JPM 2026 / RECOMB 2026: [link if mentioned]

## Notes

Free-form impressions, benchmarks claimed, comparisons to alternatives, AACR-axis fit notes.
````

## Tool index

Placeholder table. ~60–120 entries expected after bulk extraction; the populated table will be sortable by Ecosystem, Domain, or COSI. Slide DOIs and video links typically populate over the 2–4 weeks following the meeting (ISCB Nucleus on-demand is posted incrementally).

| Package | Ecosystem | Domain | Speaker | Day / COSI | Proceedings | Slides | Video | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|---|
| *(populated post-meeting from proceedings list + COSI rosters; see [`../program-notes.md`](../program-notes.md) for the candidate shortlist)* | | | | | | | | |

## Why this format

- **Proceedings DOI is the anchor for ISMB** — unlike EuroBioC / GBCC (where slide-deck DOIs are the most stable artifact), the *Bioinformatics* paper is what survives. Putting it on the same row as the talk metadata keeps the citation chain intact.
- **COSI track** is the cleanest sort dimension at this scale. ISMB has 22 COSIs; faceting by COSI gives 30–60 entries per slice instead of 600.
- **Ecosystem field broadened** beyond EuroBioC's Bioconductor-implicit assumption — at ISMB, scverse (SpatialData, anndata, scanpy) and standalone-Python (DeepChem-class, foundation-model adapters) tools are first-class and shouldn't be forced into a Bioconductor template.
- **Cross-vault "Mentioned elsewhere"** picks up the Bioconductor speakers who run EuroBioC → GBCC → ISMB (BOSC) → BioC2026 in a single year (Soneson, Mangiola, Castelo, Carey, Borman, Marini, etc.) so a reader of any one entry can hop sideways.

## Open questions

1. **Granularity** — locked: **one page per tool**, same as EuroBioC / GBCC.
2. **Proceedings-paper linking** — *new for ISMB, open*: when a tool's ISMB Proceedings paper is also cited in an AACR poster / talk, do we mirror the entry into the AACR vault, or just cross-link with a "Mentioned at AACR 2026" line? Proposed default: **cross-link only**, full entry stays in ISMB vault — the AACR poster usually treats the tool as a black-box dependency, not the artifact under study. Mirror only when the AACR poster is methodologically central (e.g., a benchmark of the ISMB-released tool on cancer data).
3. **BOSC entries vs. main-program entries** — open: BOSC runs as a 2-day COSI inside ISMB. A Bioconductor package introduced at BOSC is "an ISMB 2026 tool" in this vault, but the same package may also surface at BioC2026 in Seattle a month later. Proposed: **one tool entry, two talk slots within it** (one BOSC, one BioC2026) — the talk-slot block in the template repeats per appearance.
4. **Coverage budget** — open: 600+ talks. We don't expand 600 tool pages. Filter: (a) any proceedings paper with code + maintained repo, (b) any COSI-invited talk in MLCSB / RegSys / NetBio / VarI / TransMed / Microbiome / CompMS / 3DSIG / BOSC that names a package, (c) any tool that is an update to an existing-in-corpus entry. Estimated ~60–120 after filtering.
5. **Tutorials as tool pages** — open: 9 Sunday tutorials, each ~6 hours, each effectively a hands-on workshop for one tool/stack (Agentic AI, Cytoscape+NDEx, Quantum-for-multi-omics, k-mer biophysical ML, etc.). Proposed: yes, each tutorial gets a tool page treating the tutorial as a `Status: tutorial` entry — same pattern as EuroBioC2025's workshop entries (OSTA, msqrob2, iSEE, mia, Workshop Platform).
