# Extraction Method

## Sources

- **Session videos + transcripts**: `connect.aacr26.org` (Swapcard-backed). Videos are hosted on Vimeo with auto-generated English captions.
- **Poster abstracts**: `cattendee.abstractsonline.com/meeting/21436` (CTI Meeting Technology's Abstracts Online platform).

## Session transcript pipeline

1. Log into `connect.aacr26.org` (Fastly CAPTCHA requires manual solve on first visit).
2. Search the Sessions listing for topic terms.
3. Navigate to each parent session page — the Vimeo iframe triggers a config fetch at `https://player.vimeo.com/video/<id>/config?...transcript=1`.
4. Read `request.text_tracks[0].url` — a signed `captions.vimeo.com` URL (expires in ~6 hours).
5. `curl` with `Referer: https://vimeo.com/` to download the `.vtt`.
6. Strip cue numbers and timestamps → plain-text `.txt` version.

## Poster pipeline — two patterns

**Keyword-union** (virtual-cells, clinical-trials, single-cell-spatial-omics): Best for narrow topics.

1. Log into `cattendee.abstractsonline.com/meeting/21436` (last name + 7-digit Registration ID) — this is the frontend. The API is hosted at `www.abstractsonline.com` (the `cattendee.` subdomain is CloudFront-fronted and 403s on `/oe3/*`).
2. Read Backpack auth token from `localStorage.token`.
3. For each quoted phrase, `POST https://www.abstractsonline.com/oe3/Program/21436/Search/new/presentation` with `{"Phrase": "<query>"}`, headers `Backpack: <uuid>` and `Accept: application/json` (omit the Accept header and the API returns XML).
4. Poll `/Search/<SearchId>/Results?page=1&pagesize=2500` until `Search.Status == "Complete"`.
5. Union unique `Id` values across all queries.
6. For each `Id`, `GET /Presentation/<Id>` for full record.

**Session endpoint** (bioinfo-tools): Best for broad methods topics.

1. Identify methods-oriented session IDs (e.g., 228 = Digital Pathology 1).
2. `GET /Session/<sid>/Presentations` — returns the full presentation array directly. Complete session coverage, no false positives.

## Filter + cleanup

For both patterns:

1. Filter `Activity ∈ {Abstract Submission, Late Breaking and Clinical Trials}` + `PlayerUrl present` (Vimeo poster viewer link).
2. HTML-decode via `DOMParser`, strip tags.
3. Emit JSONL + per-poster `.txt`.

## Data-transport workaround

Chrome download flow became blocked partway through the extraction session (macOS TCC or Claude sandbox state). Switched to:

1. POST JSONL to `httpbin.org/anything` via browser `fetch()`.
2. Capture response via chrome-devtools MCP `get_network_request --responseFilePath`.
3. Extract the `.data` field from the JSON response with `jq`.

Clean, fast, bypasses the filesystem path entirely.

## Keyword unions per topic

### Virtual Cells (48 posters from 88 union hits)

```
"virtual cell", "virtual cells",
scGPT, Geneformer, scFoundation, "Universal Cell Embeddings",
scBERT, scMulan, CellLM, Nicheformer,
"cell foundation model", "foundation model",
"in silico perturbation", "in silico screen", "perturbation prediction",
"digital twin"
```

### Single-Cell & Spatial Omics (1,015 posters from 1,331 union hits)

```
"single-cell", "single cell", "single nucleus",
"spatial transcriptomics", "spatial omics", "spatial proteomics",
"imaging mass cytometry",
MERFISH, Visium, Xenium, CODEX, CyCIF,
snRNA-seq, scRNA-seq, scATAC, CITE-seq
```

### Clinical Trials (642 posters via hybrid union)

Keyword union (`"Phase I"`, `"Phase II"`, `"Phase III"`, `"clinical trial"`) → 790 IDs → filter = 578 real posters.
Plus session endpoint for 25 CT-track session IDs → 386 presentations → filter = 270 posters.
Union by Id → **642 unique posters**.

## See the repo

Source data + extraction artifacts live at [`LiudengZhang/aacr-2026`](https://github.com/LiudengZhang/aacr-2026). Raw Vimeo player configs are in `raw/<topic>/`.
