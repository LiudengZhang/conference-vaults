# Bioinfo tool dossiers — design

**Date:** 2026-05-02
**Topic:** Bioinfo / Comp Bio / AI Methods — per-tool reference layer
**Owner:** liudengzhang91@gmail.com

## Goal

Add a per-tool reference layer under the `Bioinfo / Comp Bio / AI Methods` topic so that readers can answer the question *"who is using <tool> for what, on which data, with what gap"* directly from the corpus, without re-reading the upstream paper. The reference layer sits alongside the existing Overview / Landscape / Synthesis pages — it does not replace them.

## Non-goals

- No restructuring of the other 4 topics. Tool pages live under bioinfo-tools only; other topics link out.
- Not a replacement for upstream papers / READMEs. Dossiers cover what the AACR 2026 corpus uniquely shows; they do not re-derive architecture or training claims that are already documented upstream.
- No deep benchmark compilation or head-to-head leaderboards (deferred — would age fast).
- No reverse cross-topic surfacing on the dossier side beyond a single "Also surfaced in" line.

## Architecture

### File layout

```
docs/topics/bioinfo-tools/
├── index.md                                ← (existing, untouched modulo a one-paragraph add)
├── landscape.md                            ← (existing, untouched modulo find/replace tool→link)
├── synthesis-fm-pathology-traction.md      ← (existing, untouched modulo find/replace)
└── tools/
    ├── index.md                            ← landing + comparison matrix (Tabulator)
    ├── chief.md
    ├── uni.md
    ├── conch.md
    ├── pathchat.md
    ├── virchow.md
    ├── prov-gigapath.md
    ├── scgpt.md
    ├── geneformer.md
    ├── uce.md
    ├── scfoundation.md
    ├── nicheformer.md
    ├── tangram.md
    ├── cell2location.md
    └── …                                   ← only tools that pass inclusion gate

docs/assets/bioinfo-tools/
├── tool-mentions.json                      ← per-tool corpus mentions, refreshed each build
└── tool-matrix.json                        ← matrix table data
```

### Nav (`mkdocs.yml`)

Add a `Tools` collapsible section under the existing `Bioinfo / Comp Bio / AI Methods` group:

```yaml
- Bioinfo / Comp Bio / AI Methods:
  - Overview: topics/bioinfo-tools/index.md
  - Landscape: topics/bioinfo-tools/landscape.md
  - Synthesis — FM pathology traction: topics/bioinfo-tools/synthesis-fm-pathology-traction.md
  - Tools:
    - Index: topics/bioinfo-tools/tools/index.md
    - CHIEF: topics/bioinfo-tools/tools/chief.md
    - UNI / UNI2: topics/bioinfo-tools/tools/uni.md
    # … one entry per surviving dossier
```

## Tool selection

Curated candidate list, gated by inclusion threshold = **3 deduplicated corpus mentions** (posters union'd by `Id` across all 5 topics; sessions union'd by canonical slug). Cross-topic counting is deliberate — tools that surface in multiple topics shouldn't be penalized by topic boundary. Sub-threshold tools are dropped, not stubbed; they may be listed in a "Notable absences from the corpus" section at the bottom of `tools/index.md` if they're well-known enough to deserve a no-op note.

Candidates (22 total — final survivors determined by grep):

**Pathology FMs**: CHIEF, UNI/UNI2, CONCH, PathChat, Virchow/Virchow2, Prov-GigaPath, TITAN, PLIP
**Single-cell FMs**: scGPT, Geneformer, UCE, scFoundation, scBERT, Nicheformer, Cell2Sentence
**Spatial / multimodal**: Tangram, Cell2Location, SpatialData/Squidpy
**Perturbation / drug response**: GEARS, DrugCell/DeepCDR
**Protein / structure**: AlphaFold-Multimer, ESM family

Realistic post-grep survival: ~12-15.

## Per-tool dossier shape

Target ~500-700 words per page. Fixed skeleton so tools are scannable side by side.

```markdown
# CHIEF

**Family:** Pathology FM — slide-level
**Modality:** H&E whole-slide images
**Released:** 2024 (Wang et al., Nature)
**License:** non-commercial research
**Code/checkpoint:** github.com/mahmoodlab/CHIEF
**Also surfaced in:** virtual-cells, agentic-ai

> One-paragraph plain-language description (~3 sentences).

## Architecture & training

A few sentences: backbone, pretraining corpus, objective, parameters.

## Use in the AACR 2026 corpus

<!-- mentions:start -->

**Posters mentioning CHIEF (n=6):**
- [LB123 — *Title…*](../../../sessions/...)
  1-sentence context auto-extracted from abstract.
- …

**Sessions mentioning CHIEF (n=2):**
- [foundation-models-multimodal-ai-cancer-research](../../../sessions/...)
  1-sentence context.
- …

<!-- mentions:end -->

## What's missing / where evidence is weak

Hand-written bulleted notes — independent reading of the corpus.

## Takeaway

One paragraph. What this corpus uniquely teaches us about the tool.
```

**Field provenance:**
- Header metadata (license, paper, code link, also-surfaced-in) — hand-curated.
- "Use in the AACR 2026 corpus" block — auto-generated between `<!-- mentions:start -->` / `<!-- mentions:end -->` markers, regenerated every build.
- "What's missing" + "Takeaway" — hand-written.

## Tools index page

`docs/topics/bioinfo-tools/tools/index.md` is the landing page. One paragraph of intro, then a sortable Tabulator table (reusing existing `posters.js` plumbing, different data source: `docs/assets/bioinfo-tools/tool-matrix.json`).

Columns:

| # | Column | Source | Notes |
|---|---|---|---|
| 1 | Tool | hand | links to dossier page |
| 2 | Family | hand | path-fm / sc-fm / spatial / perturbation / protein |
| 3 | Modality | hand | H&E / scRNA / spatial / multimodal / protein |
| 4 | Released | hand | year |
| 5 | Posters (n) | auto | corpus poster mentions |
| 6 | Sessions (n) | auto | corpus session mentions |
| 7 | License | hand | OSS / non-commercial / proprietary |
| 8 | Standout claim | hand | ≤12 words |

Default sort: `Posters (n)` desc.

Below the table, one paragraph per family — short prose orienting the reader to which tool dominates the AACR 2026 slice of that family.

## Build pipeline

Extension to `scripts/build_site.py`. New module-level constant + new function, called from `main()`.

```python
TOOLS = [
    # name, slug, family, aliases (case-insensitive, word-boundary)
    ("CHIEF",         "chief",         "path-fm",  ["CHIEF"]),
    ("UNI / UNI2",    "uni",           "path-fm",  ["UNI", "UNI2", "UNI-2"]),
    ("CONCH",         "conch",         "path-fm",  ["CONCH"]),
    ("PathChat",      "pathchat",      "path-fm",  ["PathChat", "Path-Chat"]),
    ("Virchow / V2",  "virchow",       "path-fm",  ["Virchow", "Virchow2", "Virchow-2"]),
    ("Prov-GigaPath", "prov-gigapath", "path-fm",  ["Prov-GigaPath", "GigaPath"]),
    ("scGPT",         "scgpt",         "sc-fm",    ["scGPT", "SC-GPT"]),  # SC-GPT = caption mishearing
    ("Geneformer",    "geneformer",    "sc-fm",    ["Geneformer"]),
    ("UCE",           "uce",           "sc-fm",    ["UCE", "Universal Cell Embeddings"]),
    ("scFoundation",  "scfoundation",  "sc-fm",    ["scFoundation"]),
    ("Nicheformer",   "nicheformer",   "sc-fm",    ["Nicheformer"]),
    ("Tangram",       "tangram",       "spatial",  ["Tangram"]),
    ("Cell2Location", "cell2location", "spatial",  ["Cell2Location", "cell2location"]),
    # other candidates added; grep gate culls below threshold
]

INCLUSION_GATE = 3  # ≥3 poster+session mentions to ship a dossier page
```

`build_tool_pages()`:

1. **Inventory** — load posters from all 5 topic JSONLs (deduplicated by `Id`) and the 26 unique session `.txt` files (deduplicated by canonical slug, following symlinks). One whole-corpus pass per build.
2. **Match** — for each tool, regex word-boundary match (case-insensitive) across each alias against `Title + Abstract` (posters) and full text (sessions). Capture poster `Id`, `Title`, `PresentationNumber`, plus a 1-sentence context window around the first hit.
3. **Gate** — drop tools with `mentions < INCLUSION_GATE`. Log dropped tools to stdout for review.
4. **Render mention sections** — for each surviving tool:
   - If `<slug>.md` exists, regenerate only the block between `<!-- mentions:start -->` and `<!-- mentions:end -->`. Hand-written prose preserved.
   - If `<slug>.md` does not exist, scaffold a stub with the skeleton above (header metadata as `TODO`, prose sections as `TODO`) so the human author can fill in.
5. **Emit matrix data** — `docs/assets/bioinfo-tools/tool-matrix.json` for the index Tabulator table.
6. **Emit tool-mentions.json** for cross-topic linking convenience (downstream pages may consume).

The script remains idempotent. Re-running the build never overwrites prose.

## Cross-topic linking

One-directional: dossiers live under `bioinfo-tools/tools/`; other topics link in.

- `docs/topics/virtual-cells/landscape.md` — find/replace pass: scGPT, Geneformer, UCE, scFoundation, Nicheformer become links to `../bioinfo-tools/tools/<slug>.md`.
- `docs/topics/agentic-ai/landscape.md` — same for PathChat and any agentic-flavored mentions.
- `docs/topics/single-cell-spatial-omics/landscape.md` — same for sc + spatial tools.
- `docs/topics/clinical-trials/landscape.md` — likely no links (CT corpus rarely names FMs).

Reverse direction (on the dossier page): a single line at the top — `**Also surfaced in:** virtual-cells, agentic-ai` — generated from the cross-topic mention scan. No deeper backlink.

## Integration with existing bioinfo pages

Minimal, no rewrites:

- `topics/bioinfo-tools/index.md`: one new paragraph linking to `tools/index.md`, plus a sentence in the topic intro flagging the new layer.
- `topics/bioinfo-tools/landscape.md`: find/replace pass — when the existing prose names a tool that has a dossier, that name becomes a link.
- `topics/bioinfo-tools/synthesis-fm-pathology-traction.md`: same find/replace.

The 7-method-family landscape essay stays — it's still the right shape for orienting the reader to the topic. Tool dossiers complement, not replace, that essay.

## Sub-threshold tools

Tools with <3 mentions are dropped silently from the dossier set. The build logs `dropped: <name> (n=<count>)` to stdout. The author reviews logs after each build and decides whether any dropped tool deserves a one-line note in a `## Notable absences from the corpus` section at the bottom of `tools/index.md` (e.g., "scBERT (n=1) — predates the recent wave; no current AACR posters cite it."). This avoids dead-page proliferation.

## Resolved decisions

- **Metadata source of truth — inline in the dossier `.md` file.** Header fields (`**Family:**`, `**Modality:**`, `**License:**`, etc.) are bold-prefix lines at the top of each `<slug>.md`. The build script parses them via regex (`^\*\*(\w[\w /]*?):\*\*\s*(.+)$`) when assembling `tool-matrix.json`. Single source of truth — no sidecar YAML, no frontmatter, no second-system drift.
- **Aliases for caption transcripts** — Vimeo auto-captions mishear technical names (scGPT → "SC-GPT", "S.C. G.P.T."). The `aliases` list in `TOOLS` enumerates the most common variants observed in the existing transcripts. New aliases get added by hand when a missed mention is discovered.
- **Find/replace pass for cross-topic linking** — manual, one-shot. The number of references is small (5-10 per landscape page) and link decisions are judgement-laden (which mention deserves a link vs which is a passing reference). Not scripting this.

## Out of scope (explicitly)

- Per-tool benchmark leaderboards.
- Comparison head-to-head matrix (e.g., CHIEF vs UNI on shared tasks). Posters report inconsistent baselines; aggregating would mislead.
- Auto-fetching upstream paper bibs / arxiv IDs.
- Tools section on topics other than bioinfo-tools.
- Dossiers for tools below the inclusion gate.

## Success criteria

1. `mkdocs build` produces `tools/` section under bioinfo-tools without errors.
2. Each surviving tool has a dossier page with: header metadata filled, auto-generated mentions block populated, hand-written "What's missing" + "Takeaway" sections.
3. Tools index page renders the matrix correctly with sort/filter working.
4. Cross-topic landscape pages have working links to dossiers for at least scGPT, Geneformer, UCE.
5. Re-running `python scripts/build_site.py && mkdocs build` does not overwrite hand-written prose in dossier `.md` files.
6. The build logs sub-threshold dropped tools so the author can decide on the notable-absences list.
