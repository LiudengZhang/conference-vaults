# Conference Corpus — Multi-Conference Refactor

**Status:** Draft, awaiting user review
**Date:** 2026-05-06
**Branch:** `refactor/conference-corpus`

## Goal

Convert the single-conference `aacr-2026` repo into a multi-conference monorepo (`conference-corpus`) hosting AACR 2026, Nextflow Summit 2026, and a JPM 2026 placeholder, served as one MkDocs Material site with per-conference top-level tabs. One repo, one build pipeline, one Cloudflare Pages deploy, one Basic Auth gate, three visually-separated conferences.

## Why

- Two new conference corpora are arriving (Nextflow Summit transcripts already in `_Extra/`, JPM 2026 placeholder coming).
- The build pipeline (`scripts/build_site.py`, mention-block injector, Tabulator wiring, Cloudflare Pages auth) is genuinely shared across conferences — splitting into per-conference repos would force vendoring or submodules. A monorepo keeps the shared infra in one place.
- The MkDocs `navigation.tabs` feature already gives clean visual separation for free.

## Non-goals

- **Backwards-compatible URL preservation.** The repo rename and `docs/conferences/...` move will change URLs. Cloudflare Pages will redeploy on the new URL space; Hypothesis annotations anchored to old URLs are accepted as collateral damage (the user has not yet relied on durable URLs).
- **Splitting AACR into separate sub-repos per topic.** Topics stay where they are, just nested under `aacr-2026/`.
- **Building a per-conference standalone site.** One unified site is the target.
- **Migrating JPM 2026 content.** That folder ships empty with a placeholder page.

## Disk layout (after)

```
conference-corpus/                          # repo root (renamed from aacr-2026)
├── aacr-2026/
│   ├── transcripts/{agentic-ai,...,clinical-trials}/...   (moved from repo root)
│   └── raw/{agentic-ai,...,clinical-trials}/...           (moved from repo root)
├── nextflow-2026/
│   └── transcripts/sessions/                              (3 .md files moved from _Extra/Nextflow, all populated)
│       ├── 2026-04-30-nextflow-summit-day-1-am.md         (was transcript_day_1_before_lunch.md, ~108 KB)
│       ├── 2026-04-30-nextflow-summit-day-1-pm.md         (was transcript_day_1_after_lunch.md, ~121 KB — protein-design competition + AI workflows; May 3 in caption header is a captioner artifact)
│       └── 2026-05-01-nextflow-summit-day-2.md            (was transcript_day_2.md, ~142 KB — community training + ambassador program)
├── jpm-2026/
│   └── README.md                                          (placeholder; "no content yet")
├── docs/
│   ├── index.md                                           (3-conference home page; rewritten)
│   ├── conferences/
│   │   ├── aacr-2026/                                     (everything currently under docs/topics/, sessions/, etc.)
│   │   │   ├── index.md                                   (current root index becomes this)
│   │   │   ├── topics/...
│   │   │   └── sessions/...
│   │   ├── nextflow-2026/
│   │   │   ├── index.md                                   (new; conference overview)
│   │   │   └── sessions/...                               (auto-generated from nextflow-2026/transcripts/)
│   │   └── jpm-2026/
│   │       └── index.md                                   (new; placeholder)
│   ├── notes/                                             (extraction.md, caveats.md — shared)
│   ├── assets/, javascripts/, stylesheets/                (shared, unchanged paths)
│   └── superpowers/                                       (specs + plans, unchanged)
├── scripts/build_site.py                                  (generalized — see Build pipeline)
├── mkdocs.yml                                             (top-level tab per conference + Notes)
├── functions/_middleware.js                               (unchanged; one Basic Auth covers the whole site)
├── README.md                                              (rewritten as conference-corpus home README)
└── requirements.txt, .gitignore, ...                      (unchanged)
```

## Conference config

Introduce a single source of truth at `scripts/conferences.py` (or a `conferences.yml` if non-Python users will edit it — leaning Python because `build_site.py` already imports modules):

```python
CONFERENCES = [
    {
        "slug": "aacr-2026",
        "label": "AACR 2026",
        "data_dir": "aacr-2026",                 # disk path for transcripts/raw
        "docs_dir": "docs/conferences/aacr-2026",
        "topics": [                              # existing TOPICS list moves here
            ("agentic-ai", "Agentic AI"),
            ("single-cell-spatial-omics", "Single-Cell & Spatial Omics"),
            ("virtual-cells", "Virtual Cells"),
            ("bioinfo-tools", "Bioinfo / Comp Bio / AI Methods"),
            ("clinical-trials", "Clinical Trials"),
        ],
        "has_posters": True,
        "has_tools_index": True,                 # bioinfo-tools dossier matrix
    },
    {
        "slug": "nextflow-2026",
        "label": "Nextflow Summit 2026",
        "data_dir": "nextflow-2026",
        "docs_dir": "docs/conferences/nextflow-2026",
        "topics": [],                            # no per-topic split — flat session list
        "has_posters": False,
        "has_tools_index": False,
    },
    {
        "slug": "jpm-2026",
        "label": "JPM 2026",
        "data_dir": "jpm-2026",
        "docs_dir": "docs/conferences/jpm-2026",
        "topics": [],
        "has_posters": False,
        "has_tools_index": False,
        "placeholder_only": True,                # build skips data discovery; emits stub index
    },
]
```

`build_site.py` consumes this list and dispatches per-conference work. AACR retains all its existing behavior (topic-aware poster JSON, sessions, mention-block injection, tools matrix); Nextflow gets a flat sessions list; JPM gets a stub.

## Build pipeline changes

`scripts/build_site.py` becomes a thin top-level loop:

```python
for conf in CONFERENCES:
    if conf.get("placeholder_only"):
        emit_placeholder(conf)
        continue
    if conf["has_posters"]:
        for slug, _ in conf["topics"]:
            build_poster_json(conf, slug)
    if conf["has_tools_index"]:
        build_tool_matrix(conf)
        inject_mentions_blocks(conf)
    build_session_pages(conf)
```

Concretely:
- Existing functions (`build_poster_json`, `build_session_pages`, `build_tool_matrix`, `inject_mentions_blocks`) take a `conf` dict and use `conf["data_dir"]` and `conf["docs_dir"]` for path resolution instead of hard-coded `transcripts/` and `docs/`.
- `TOPICS` constant deletes; topics live on the AACR conference dict only.
- Output paths gain a conference prefix: `docs/assets/{conf}/posters/{topic}.json`, `docs/conferences/{conf}/sessions/{slug}.md`, etc.
- The session pages no longer dump into a flat `docs/sessions/` — each conference owns its own. Cross-topic-within-AACR symlink resolution stays the same; cross-conference linking is not introduced.

## MkDocs nav

```yaml
nav:
  - Home: index.md
  - AACR 2026:
    - Overview: conferences/aacr-2026/index.md
    - Agentic AI:
      - Overview: conferences/aacr-2026/topics/agentic-ai/index.md
      - Landscape: conferences/aacr-2026/topics/agentic-ai/landscape.md
      - Synthesis — AT02 vs corpus: conferences/aacr-2026/topics/agentic-ai/synthesis-at02-vs-corpus.md
    # ... existing AACR topic structure, paths re-prefixed
    - All AACR sessions: conferences/aacr-2026/sessions/index.md
  - Nextflow Summit 2026:
    - Overview: conferences/nextflow-2026/index.md
    - All sessions: conferences/nextflow-2026/sessions/index.md
  - JPM 2026:
    - Overview: conferences/jpm-2026/index.md
  - Notes:
    - Extraction method: notes/extraction.md
    - Caveats: notes/caveats.md
```

`navigation.tabs` is already enabled, so each top-level entry renders as a tab. Visual separation via tabs, visual unity via shared theme/search/auth.

## Home page (`docs/index.md`)

3-conference card grid (using attr_list / md_in_html, both already enabled):

```markdown
# Conference Corpus

Curated transcripts and abstracts from biomedical and computational biology meetings, organized into a single searchable site.

## Conferences

[**AACR 2026**](conferences/aacr-2026/){ .md-button }
American Association for Cancer Research Annual Meeting. ~26 sessions, ~2,300 posters across 5 topics: agentic AI, single-cell & spatial omics, virtual cells, bioinfo / comp bio / AI methods, and clinical trials.

[**Nextflow Summit 2026**](conferences/nextflow-2026/){ .md-button }
Nextflow Summit (April 30 – May 1, 2026). 3 session transcripts (~370 KB total) on AI in scientific workflows, protein-design competition pipelines, and Nextflow community training.

[**JPM 2026**](conferences/jpm-2026/){ .md-button }
J.P. Morgan Healthcare Conference 2026. Placeholder — no content yet.
```

## Cloudflare Pages

No deploy-side changes. `functions/_middleware.js` Basic Auth covers `/*` and continues to do so. The Cloudflare Pages project is renamed via the dashboard if desired (or left at the existing name — DNS is not affected by the GitHub repo rename). The build command (`pip install -r requirements.txt && python scripts/build_site.py && mkdocs build`) is unchanged.

## GitHub repo rename

Rename `LiudengZhang/aacr-2026` → `LiudengZhang/conference-corpus` via the GitHub web UI **after** the in-repo refactor lands. GitHub serves redirects from the old URL indefinitely. Update `mkdocs.yml`'s `repo_url` and `repo_name` and the README's clone command in the same commit as the rename.

## Migration order

This is a structural rewrite. Order matters because builds need to keep passing for review:

1. **Branch & spec** — `refactor/conference-corpus` branched off `tools/dossiers`. (Done.)
2. **Conference config scaffold** — add `scripts/conferences.py` with the 3 entries; AACR entry mirrors current behavior. Update `build_site.py` to read from it but keep current paths working (no file moves yet).
3. **Move AACR data** — `git mv transcripts/ aacr-2026/transcripts/`, same for `raw/`. Update conference config `data_dir`. Build & verify identical output.
4. **Move AACR docs** — `git mv docs/topics/ docs/conferences/aacr-2026/topics/`, same for `docs/sessions/`. Move `docs/index.md` content into `docs/conferences/aacr-2026/index.md`. Update build script paths and nav. Build & verify all AACR pages still render.
5. **Add Nextflow** — create `nextflow-2026/transcripts/sessions/` with the 3 transcripts moved from `_Extra/Nextflow/` (renamed per the disk-layout section). Add `docs/conferences/nextflow-2026/index.md`. Add Nextflow tab to nav. Build & verify Nextflow sessions render.
6. **Add JPM placeholder** — create `jpm-2026/README.md` and `docs/conferences/jpm-2026/index.md`. Add JPM tab to nav.
7. **Rewrite home page** — new `docs/index.md` 3-conference card grid.
8. **Rewrite README** — repo-level README becomes conference-corpus overview.
9. **Push & preview** — push branch, let Cloudflare Pages preview-deploy, smoke-test all 3 tabs in the preview URL.
10. **Repo rename** — rename on GitHub. Update `mkdocs.yml` repo_url/repo_name.
11. **Merge to main**, deploy production.

Steps 2–7 each end in a passing `mkdocs build --strict` (modulo the 49 pre-existing strict-mode warnings that are out of scope) and a commit. Each commit is reviewable in isolation.

## Test plan

- After step 3: `mkdocs build` warning count unchanged from pre-refactor baseline.
- After step 4: every URL that was `/topics/X/...` now redirects via the new `/conferences/aacr-2026/topics/X/...` path; navigate the site locally and click 5 representative pages (one per topic).
- After step 5: Nextflow sessions list renders, each of the 3 transcript pages is non-empty.
- After step 7: home page lists all 3 conferences, each card link works.
- After step 9: Cloudflare Pages preview deploy succeeds, Basic Auth still gates the site.
- Word counts and file checksums for AACR transcripts before/after the move match (paranoia check that no content was lost).

## Resolved questions

1. **Nextflow event name.** Confirmed via Goldcast event link (https://events.goldcast.io/e/ff174b87-316f-47c7-8c7b-a51028b670b7) that this is the **Nextflow Summit 2026**. Slug uses `nextflow-summit-day-1-am`, `nextflow-summit-day-1-pm`, `nextflow-summit-day-2`. The "Vicksville" in transcript headers is a captioner mishearing of "Nextflow."
2. **Day-1 PM date.** Confirmed: day 1 = April 30, day 2 = May 1. The "May 3" in the day-1 PM caption header is a captioner artifact and is ignored. Slugs use `2026-04-30-` for both day-1 AM and PM, `2026-05-01-` for day 2.
3. **JPM 2026 placeholder.** Page is intentionally blank — just a stub `index.md` with the conference title and a one-line "No content yet" note. No expected-content or timeline copy.
4. **Repo rename timing.** Rename on GitHub **after** the refactor PR merges (matches the "Migration order" step 10). PR does not span a rename; new name takes effect once the new structure is on `main`.

## Out of scope (follow-on work)

- Search-result grouping by conference (current MkDocs search is global; that may be desired or undesired — defer until users ask).
- Per-conference Hypothesis groups (currently one site-wide group).
- Migrating the bioinfo-tools dossier framework to other conferences (Nextflow Summit could in principle have a "tools" matrix for nf-core / Seqera tools mentioned, but that's a separate spec).
- Cross-conference cross-linking (e.g., "this scGPT paper was discussed at both AACR and Nextflow Summit") — interesting but premature.
