# ECCB 2026 — Tools

ECCB 2026 will run 4 distinguished keynotes + ~9 main scientific sessions (Proceedings + Highlight talks) + 4 ELIXIR Track sessions + 4 Focus sessions + 1 Industry session over 3 main-conference days, plus tutorials/workshops (Sep 3), the ISCB Student Council Symposium (Sep 3), and Communities Day satellites (Sep 4). The subset that yields tool pages is the intersection of (a) Proceedings papers published in *Bioinformatics* (peer-reviewed full papers with DOIs), (b) Highlight talks that name a maintained package (recent published research, post Mar 1, 2025), (c) ELIXIR Track talks announcing a community-maintained registry/tool/standard, and (d) Tutorial/Workshop tracks anchored on a single tool. **Ecosystem field = `Bioconductor / scverse / Galaxy / ELIXIR-infra / standalone-Python / standalone-R / web-service / C++`** — same broad ecosystem palette as ISMB 2026, with `ELIXIR-infra` added for the European registry/infrastructure layer.

> **Status:** Template stub. Per-tool format proposed here for review *before* bulk extraction runs after the meeting closes (Sep 4, 2026) and the *Bioinformatics* OUP supplement is fully indexed. Once locked, expected ~30–60 entries get populated from the proceedings-paper list + highlight-talk acceptances + ELIXIR Track rosters + tutorial syllabi.

## Per-tool entry template

Each tool gets its own page (`tools/<package-slug>.md`) following this structure. The shape mirrors ISMB 2026 / RECOMB 2026 / EuroBioC2025 / GBCC2025 with three ECCB-specific additions (a Proceedings DOI row, a Scientific Area field, an ELIXIR Community field):

````markdown
# <ToolName>

**One-line description** — what the tool does in plain language.

- **Maintainer:** <name> (<institution>)
- **Ecosystem:** Bioconductor / scverse / Galaxy / ELIXIR-infra / standalone-Python / standalone-R / web-service / C++ / other
- **Package / source:** [GitHub link]
- **Docs / vignette:** [link]
- **Status at ECCB 2026:** proceedings paper / highlight talk / ELIXIR demo / tutorial / workshop / Communities Day satellite / poster
- **Proceedings:** [*Bioinformatics* OUP DOI if applicable — null for highlight talks / ELIXIR demos / posters]
- **Scientific Area:** Genomics / Transcriptomics / Proteins-Structural / Systems Biology / Biodiversity-Sustainability / cross-area
- **ELIXIR Community:** [named ELIXIR community if applicable — null otherwise]

## Talk at ECCB 2026

- **Speaker:** ...
- **Day / Session:** Mon Aug 31 / Sci Session 1 · Tue Sep 1 / ELIXIR Track 2 · Wed Sep 2 / Focus Session 4 · Thu Sep 3 / Tutorial · etc.
- **Slot:** morning / afternoon / poster session 1 / poster session 2
- **Slides:** [Zenodo DOI or lab site]
- **Video:** [recording link if posted; ECCB recording coverage is historically uneven]
- **Abstract / talk page:** [ECCB program link]
- **Preprint:** [bioRxiv / arXiv link if applicable — for highlight talks, the published paper DOI]

## What it does

2–3 sentences: the problem it solves, the key methodological idea, what it consumes/produces, what it's benchmarked against.

## Where it fits in the corpus

- AACR 2026: [link if mentioned]
- EuroBioC 2025: [link if mentioned]
- GBCC 2025: [link if mentioned]
- ISMB 2026: [link if mentioned — Jul 12–16 Washington DC; same proceedings journal, partial speaker overlap]
- RECOMB 2026: [link if mentioned — May 26–29 Thessaloniki; pure-methods sibling]
- BioC 2026: [link if mentioned — Aug 10–12 Seattle, likely re-up for Bioconductor speakers]
- Nextflow Summit 2026: [link if mentioned]
- JPM 2026: [link if mentioned]

## Notes

Free-form impressions, benchmarks claimed, comparisons to alternatives, AACR-axis fit notes, ELIXIR-community context if applicable.
````

## Tool index

Placeholder table. ~30–60 entries expected after bulk extraction; the populated table will be sortable by Ecosystem, Scientific Area, or Session type. Slide DOIs and video links typically populate over the 2–6 weeks following the meeting (recording posting cadence is uneven for ECCB historically).

| Package | Ecosystem | Scientific Area | Speaker | Day / Session | Proceedings | ELIXIR Community | Slides | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|---|
| *(populated post-meeting from proceedings list + highlight-talk acceptances + ELIXIR roster; see [`../program-notes.md`](../program-notes.md) for the candidate shortlist)* | | | | | | | | |

## Why this format

- **Proceedings DOI is the anchor for ECCB**, same as ISMB — the *Bioinformatics* OUP supplement paper is what survives long after the talk. Putting it on the same row as the talk metadata keeps the citation chain intact.
- **Scientific Area** (5 named areas: Genomics, Transcriptomics, Proteins/Structural, Systems Biology, Biodiversity/Sustainability) is the cleanest sort dimension at ECCB. It's coarser than ISMB's 22-COSI grid but finer than EuroBioC's single-track shape. Five-way faceting matches the reality of how the program committee organizes accepted talks.
- **ELIXIR Community field** captures the European-infrastructure dimension. ISMB has BOSC but no equivalent "named European community" tag (Bio.tools, Galaxy Europe, BioContainers, GA4GH-adjacent, etc. all surface here). Faceting by ELIXIR Community lets a reader find the Bio.tools registry update, the BioContainers update, and the Galaxy Europe update without searching the full table.
- **Ecosystem field** same palette as ISMB (Bioconductor / scverse / Galaxy / standalone-Python / standalone-R / web-service / C++) with `ELIXIR-infra` added for registry/standards/community tooling.
- **Cross-vault "Mentioned elsewhere"** picks up the European-side Bioconductor / scverse / SIB speakers who tour EuroBioC → GBCC → ISMB → ECCB → BioC2026 in a single year (Soneson, Mangiola, Crowell, Marconato, Borman, Castelo, Marini, Robinson-lab, etc.) so a reader of any one entry can hop sideways.

## Open questions

1. **Granularity** — locked: **one page per tool**, same as ISMB / RECOMB / EuroBioC / GBCC.
2. **Highlight-talk mirror policy** — open: highlight talks at ECCB are *recently published* papers (post Mar 1, 2025) — many will have already been covered at EuroBioC 2025, ISMB 2025 (Liverpool), or BioC 2025. For a tool that already has a 2025 vault entry, do we mirror as a fresh ECCB 2026 entry or just append an "ECCB 2026 highlight" section to the existing page? Proposed: **append to existing entry**, link from the new ECCB session; the highlight talk is a re-presentation, not a new artifact.
3. **ELIXIR Track entries vs. tool entries** — open: ELIXIR registry/standards talks (Bio.tools, BioContainers, GA4GH genomic-data toolkit, Galaxy Europe) are *infrastructure*, not algorithmic methods. The per-tool template's `Status` field has an `ELIXIR demo` value, but several ELIXIR contributions are community frameworks (no single GitHub repo). Proposed: keep ELIXIR-infra entries in `topics/elixir-infra/` as community-framework pages rather than per-tool pages; cross-link from `tools/index.md` but don't expand them to full tool format.
4. **Communities Day satellites (Fri Sep 4)** — open: Communities Day events are SIB-Community-led satellites on biodiversity, pathogen surveillance, and research infrastructures. Tools that emerge from biodiversity / pathogen satellites may not fit the AACR axis at all. Proposed: triage at satellite granularity — log all Communities Day satellites in `digest/day-5-friday.md`, expand to tool pages only when the tool has an AACR-axis-relevant use case (e.g., pathogen-genomics tooling that connects to cancer-microbiome, or biodiversity tools that get used in environmental cancer epidemiology).
5. **Tutorials (Thu Sep 3) as tool pages** — open: ECCB tutorials are typically 6–10 half-day or full-day sessions, each anchored on one tool/stack (similar shape to ISMB IP1–IP9). The official tutorial list isn't yet public for ECCB 2026; the Tutorials chairs (Palagi + Marek, SIB) typically post the list in late-June 2026. Proposed: same pattern as ISMB — each tutorial gets a tool page treating the tutorial as a `Status: tutorial` entry.
6. **Coverage budget** — open: ~30–60 entries target. Filter: (a) any *Bioinformatics* OUP proceedings paper with code + maintained repo, (b) any highlight talk that names a package (post Mar 1, 2025 published — so already-released tools), (c) any ELIXIR Track talk that names a registry/standard/community framework (treated as infrastructure entry), (d) any tutorial/workshop anchored on a single tool, (e) any existing-in-corpus tool that gets a public ECCB 2026 slot (update section appended to its existing vault page).
