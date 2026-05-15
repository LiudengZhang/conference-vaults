# Caveats

## Session transcripts

- **All captions are Vimeo AI-generated English.** Expect misheard names ("Foersch" → "Firsch" / "Forster", "Bunne" → "Bonner") and technical terms ("scGPT" → "SC-GPT", "AACR" → "ACR"). Find/replace before quoting.
- **Sub-talks share the parent video.** To extract just one sub-talk from a multi-speaker session, time-slice the parent VTT. See the `transcripts/agentic-ai/at02-per-speaker/` directory in the repo for a worked example.
- **VTT signatures in raw Vimeo configs have expired** (signed URLs valid ~6 hours). Re-extracting a session means re-navigating the live session page, not re-using the saved JSON.

## Poster abstracts

- **HTML entities decoded, tags stripped.** Any markup in the original abstract body is flattened. Tables and figures are not preserved — the AACR Abstracts Online system doesn't include them in the API response anyway.
- **"Activity" field distinguishes** `Abstract Submission` from `Late Breaking and Clinical Trials`. Both are kept; other activities (`Invited Speaker`, `Chairperson`, etc.) are session-role records, not posters, and are filtered out.
- **`PlayerUrl` required.** Posters without a Vimeo poster-viewer link are filtered out (typically ~75-80% of raw activity-filtered records have PlayerUrl).
- **Token signatures in `PlayerUrl`** may expire in hours. PDFs are not downloaded by default; if you want a specific poster's PDF, re-extract the PlayerUrl from a fresh session or grab it from the embedded JSON while the original session is still authenticated.

## Poster-corpus construction

- **Overlap handled by duplication, not symlinks.** A poster appearing in multiple topic folders has its `.txt` file duplicated (~4 KB × ~534 duplicates = ~2 MB total) so each folder is self-contained for ripgrep. The JSONL-level `Id` is the dedup key if you union across topics.
- **Keyword union is OR-based when unquoted.** The AACR Abstracts Online search returns posters matching any word in a multi-word query unless the query is phrase-quoted. All multi-word terms in the harvest were phrase-quoted (`"virtual cell"` not `virtual cell`).
- **`@AllPosters=Yes` token + text search returns 0.** The filter/text combination is broken in the API; filter downstream on `Activity` + `PlayerUrl` instead.

## Clinical Trials — session transcripts deferred

The Clinical Trials topic has **no session transcripts** in this corpus. Rationale:

1. CT minisymposium talks at AACR are typically authors reading their own poster abstracts verbatim, then taking questions.
2. Adding ~15 × 90 min = 22+ hours of auto-captioned video transcript would duplicate the poster corpus substantively.
3. Extraction requires Fastly CAPTCHA handling + per-session Vimeo config capture; the Chrome download flow was blocked during the harvest session.

25 CT parent sessions are identified by ID in the repo's `transcripts/clinical-trials/README.md`. Each can be extracted on demand — each session costs ~5-10 minutes of live interactive work.

## Known discrepancies

- **The 38-file scso reconciliation**: early in corpus construction, the slugification algorithm for `.txt` filenames differed slightly from the final version. This caused 38 duplicate `.txt` files (same presentation number, old slug + new slug) in `single-cell-spatial-omics/posters/abstracts/`. These were deleted and the directory regenerated fresh from the JSONL in the initial commit. Count is now exactly 1,015 `.txt` files matching 1,015 JSONL records.
- **Character handling**: `<` and `>` in the JSONL may represent stripped-tag remnants (now gone) or actual mathematical/scientific notation (e.g., `≤` → `&#8804;` → `≤`). The `DOMParser`-based decode handles these correctly, but very old abstracts with HTML-within-entities may need manual review.

## Intellectual property

- Poster abstracts are © their authors. This corpus is for personal research / analysis only. Any republication should be via the original AACR attribution and conference identifiers (`ControlNumber`, `PresentationNumber`).
- Session transcripts are auto-captions of proprietary video recordings. Same caveat.
- The `aacr-2026` GitHub repo is **private** because of this — do not share the URL publicly.
