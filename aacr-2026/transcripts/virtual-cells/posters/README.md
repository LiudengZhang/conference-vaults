# AACR Annual Meeting 2026 — Virtual Cells Posters

**48 poster abstracts, ~19,000 words** (of which ~15,700 are abstract body text). Harvested from `cattendee.abstractsonline.com` by union-searching for virtual-cell / cell-foundation-model keywords, then filtering to real poster presentations (`Activity ∈ {"Abstract Submission", "Late Breaking and Clinical Trials"}` with a Vimeo poster viewer URL).

Scope matches the sessions side: tier B — cell / transcriptomic foundation models, virtual cells, in silico perturbation, multimodal AI agents applied to cancer biology. Pathology foundation models appear here because they dominate the top poster sessions even though they're adjacent to (not the same as) cell foundation models.

## Files

- `abstracts.jsonl` (163 KB) — one JSON record per poster; full structured data:
  - `Id`, `Title`, `Abstract` (HTML-decoded), `AuthorBlock`, `SessionTitle`, `SessionId`
  - `PresentationNumber`, `PosterboardNumber`, `ControlNumber`
  - `Start`, `End`, `Activity`, `PresenterDisplayName`, `Topics`, `Keywords`
  - `PlayerUrl` — Vimeo/CTI poster PDF viewer link (for later PDF download)
  - `MatchedKeyword` — the keyword that first surfaced this poster (see breakdown below)
- `abstracts/` — 48 individual `.txt` files, one per poster:
  - Filename pattern: `<poster-number>-<title-slug>.txt`
  - Each file has title + metadata header + full abstract body
  - `rg` / `grep` across this folder to find posters by technique, author, gene, or model name

## Counts by day

| Day | Posters |
|---|---|
| Apr 19 (Sun) | 11 |
| Apr 20 (Mon) | 18 |
| Apr 21 (Tue) | 13 |
| Apr 22 (Wed) | 6 |

## Counts by session (top sessions)

| Session | Posters |
|---|---|
| Digital Pathology 1 / 2 / 3 | 13 |
| Radiomics and AI in Medical Imaging | 4 |
| Late-Breaking Research: Bioinformatics / Comp Bio / Systems Biology 1+2 | 6 |
| Integrative Computational Approaches 1+2 | 5 |
| Large Language Models in the Clinic | 3 |
| Machine Learning Approaches / Machine Learning for Image Analysis | 4 |
| Deep Learning in Cancer | 2 |
| Agentic AI in Cancer | 2 |
| (18 other sessions with 1 poster each) | 18 |

## Search keywords used

Quoted phrases where multi-word (Abstracts Online API does OR logic on unquoted multi-word queries, so quoting matters — see the `aacr-poster-abstracts` skill):

```
"virtual cell", "virtual cells",
scGPT, Geneformer, scFoundation, "Universal Cell Embeddings",
scBERT, scMulan, CellLM, Nicheformer,
"cell foundation model", "foundation model",
"in silico perturbation", "in silico screen", "perturbation prediction",
"digital twin"
```

## Keyword that first surfaced each poster

| Keyword | Posters |
|---|---|
| `"foundation model"` | 34 |
| `"digital twin"` | 4 |
| `Geneformer` | 3 |
| `"virtual cell"` | 3 |
| `scGPT` | 2 |
| `"in silico perturbation"` | 1 |
| `"in silico screen"` | 1 |

`cell foundation model`, `scFoundation`, `scBERT`, `scMulan`, `CellLM`, `Nicheformer`, `Universal Cell Embeddings`, `virtual cells`, and `perturbation prediction` all returned hits at the search stage but those hits were duplicates of posters already surfaced by more general terms — so they don't appear in the first-match column.

## Union math

- 88 unique presentation IDs across all keyword searches.
- 58 had `Activity ∈ {Abstract Submission, Late Breaking and Clinical Trials}` (i.e. real poster slots rather than session roles).
- **48** of those also had a `PlayerUrl` (Vimeo poster viewer) — these are the kept posters.
- 19 were Invited Speaker / Chairperson / Moderator / Other (session roles, not posters).

## Overlap with the single-cell-spatial-omics poster corpus

- **17 of the 48 virtual-cells posters** are also in `../../single-cell-spatial-omics/posters/abstracts.jsonl` (the `Id` is the same). That's a ~35% overlap — posters that use both virtual-cell terms *and* single-cell/spatial terms in their abstracts.
- **31 posters are unique to virtual-cells** — mostly pathology-foundation-model and AI-agent posters that don't mention single-cell / spatial assays explicitly.
- Conversely, 12 single-cell-spatial-omics posters strictly match virtual-cell terms but aren't in this set (6 were surfaced by a keyword not in the virtual-cells union, e.g. raw `scGPT` without quotes; 5 had `Activity = Invited Speaker` and got filtered out).

Per-topic folders are independent on disk (no symlinks at the poster `.txt` level — duplication of 17 small files costs ~68 KB, cheaper than cross-folder symlinks would complicate `rg` scans).

## PDFs (deferred)

Each record has a `PlayerUrl` like `https://cslide-us.ctimeetingtech.com/play/<uuid>/<token>/pdf?cover=`. These resolve to actual poster PDFs (~1–5 MB each, so full set ≈ 50–250 MB). Not downloaded by default. To grab one:

```bash
curl -L -o poster.pdf 'https://cslide-us.ctimeetingtech.com/play/<uuid>/<token>/pdf?cover='
```

Or to bulk-download this whole set (tokens should still be valid for a few more hours while the login session is fresh):

```bash
mkdir -p pdfs
jq -r '"\(.PresentationNumber) \(.PlayerUrl)"' abstracts.jsonl \
  | xargs -n 2 -P 6 sh -c 'curl -sS -L -o "pdfs/$0.pdf" "$1"'
```

## Extraction method

1. Log into `cattendee.abstractsonline.com/meeting/21436` (last name + 7-digit Registration ID).
2. `POST /oe3/Program/21436/Search/new/presentation` with `{"Phrase": "<keyword>"}` and `Backpack: <uuid>` header (from `localStorage.token`).
3. Poll `/Search/<SearchId>/Results?page=1&pagesize=2500` until `Search.Status == "Complete"`.
4. Union unique `Id`s across all keyword queries.
5. For each `Id`, fetch `/Presentation/<Id>` for full record.
6. Filter to poster activities + `PlayerUrl` present.
7. HTML-decode (`html.unescape` equivalent — done in-browser via `DOMParser`), strip tags, write JSONL.
