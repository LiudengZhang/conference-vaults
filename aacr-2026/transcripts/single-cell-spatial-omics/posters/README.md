# AACR Annual Meeting 2026 — Single-Cell & Spatial Omics Posters

**1,015 poster abstracts, ~328,000 words of research text.** Harvested from `cattendee.abstractsonline.com` by union-searching for single-cell / spatial-omics keywords, then filtering to real poster presentations (Activity = "Abstract Submission" or "Late Breaking and Clinical Trials", with a Vimeo poster viewer URL).

## Files

- `abstracts.jsonl` (3.4 MB) — one JSON record per poster, full structured data:
  - `Id`, `Title`, `Abstract` (HTML-decoded), `AuthorBlock`, `SessionTitle`, `SessionId`
  - `PresentationNumber` (e.g. `1026`), `PosterboardNumber`, `ControlNumber`
  - `Start`, `End` — date/time of poster session
  - `PlayerUrl` — Vimeo/CTI poster PDF viewer link (for later PDF download)
  - `Activity`, `Topics`, `Keywords`, `PresenterDisplayName`
- `abstracts/` (4 MB) — 1,015 individual `.txt` files, one per poster:
  - Filename pattern: `<poster-number>-<title-slug>.txt`
  - Each file has title + metadata header + full abstract body
  - `grep` / `ripgrep` across this folder to find posters by technique, author, gene, etc.

## Poster counts by day

| Day | Posters |
|---|---|
| Apr 19 (Sun) | ~180 |
| Apr 20 (Mon) | ~330 |
| Apr 21 (Tue) | ~330 |
| Apr 22 (Wed) | ~175 |

## Search keywords used

Union of (with quoted phrase matches where useful):
`"single-cell"`, `"single cell"`, `"single nucleus"`, `"spatial transcriptomics"`, `"spatial omics"`, `"spatial proteomics"`, `"imaging mass cytometry"`, `MERFISH`, `Visium`, `Xenium`, `CODEX`, `CyCIF`, `snRNA-seq`, `scRNA-seq`, `scATAC`, `CITE-seq`.

1,331 total hits from presentation search → **1,015 real posters** after filtering (1,079 Abstract Submissions + 68 Late Breaking + 109 Invited Speakers + 19 Chairpersons + 55 Other + 1 Moderator; posters have a `PlayerUrl` Vimeo viewer link).

## PDFs (deferred)

Each record has a `PlayerUrl` like `https://cslide-us.ctimeetingtech.com/play/<uuid>/<token>/pdf?cover=`. These resolve to actual poster PDFs (~1-5 MB each, so full set = ~1-2.5 GB). Not downloaded yet — when/if you want a specific poster's PDF, run:

```bash
curl -L -o poster.pdf 'https://cslide-us.ctimeetingtech.com/play/<uuid>/<token>/pdf?cover='
```

Or to bulk-download a scoped subset (e.g. strong-fit method terms only), let me know the filter and I'll grab them. VTT signatures in the abstractsonline tokens may expire, so bulk downloading should happen while the login session is still fresh.

## Extraction method

1. Log into `cattendee.abstractsonline.com/meeting/21436` (last name + 7-digit Registration ID).
2. `POST https://www.abstractsonline.com/oe3/Program/21436/Search/new/presentation` with `{"Phrase": "<keyword>"}` and `Backpack: <uuid>` header (from `localStorage.token` after login).
3. Returns `SearchId`, used to paginate `GET /Search/<sid>/Results?page=N&pagesize=1000`.
4. For each result `Id`, fetch `GET /Program/21436/Presentation/<id>` for full record.
5. Filter to `Activity in ["Abstract Submission", "Late Breaking and Clinical Trials"]` with `PlayerUrl` present.
6. Decode HTML entities + strip tags from `Title`, `Abstract`, `AuthorBlock`.
