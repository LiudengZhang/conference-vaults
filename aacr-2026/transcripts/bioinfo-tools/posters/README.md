# AACR 2026 — Bioinfo / Comp Bio / AI Methods Posters

**536 poster abstracts, ~210,000 words** spanning 24 methods-oriented poster sessions. Complete session coverage — every real poster (Abstract Submission + Late-Breaking with `PlayerUrl`) in each of the 24 sessions is included.

## Files

- `abstracts.jsonl` (1.8 MB) — one JSON record per poster: `Id`, `Title`, `Abstract` (HTML-decoded), `AuthorBlock`, `SessionTitle`, `SessionId`, `PresentationNumber`, `PosterboardNumber`, `ControlNumber`, `Activity`, `Start`, `End`, `PresenterDisplayName`, `Topics`, `Keywords`, `PlayerUrl`.
- `abstracts/` — 536 `.txt` files, pattern `<poster-number>-<title-slug>.txt`.

## Session coverage

Full presentations from these 24 sessions (all posters retrieved via `/Session/<sid>/Presentations`):

**Core bioinformatics**
- Application of Bioinformatics to Cancer Biology 1 / 2 / 3 / 4 / 5 (137 posters)
- New Algorithms and Computational Methods (26)
- New Software Tools for Data Analysis (29)
- Integrative Computational Approaches 1 / 2 (50)
- Network Biology and Precision Medicine (25)
- Innovative Therapeutic Modalities and Translational Platforms (27)
- Computational, Technological, and Mechanistic Advances (27)
- Molecular Pathology (12)
- Late-Breaking Research: Bioinformatics/Comp Bio/Systems Biology 1 / 2 (31)

**AI / ML methods**
- Machine Learning Approaches for Cancer Prediction (23)
- Machine Learning for Image Analysis (8)
- Deep Learning in Cancer (18)
- Digital Pathology 1 / 2 / 3 (59)
- Radiomics and AI in Medical Imaging (21)

**LLM / Agentic**
- Large Language Models in the Clinic (25)
- Agentic AI in Cancer (18)

## Counts by day

| Day | Posters |
|---|---|
| Apr 19 (Sun) | 134 |
| Apr 20 (Mon) | 164 |
| Apr 21 (Tue) | 171 |
| Apr 22 (Wed) | 67 |

## Activity breakdown

- 505 Abstract Submission
- 31 Late Breaking and Clinical Trials

## Session-endpoint approach (vs keyword union)

The other topics use keyword-union searches on abstract content. For methods, that would have drowned in false positives (any paper mentioning "machine learning" briefly would hit). Instead this topic uses the `/Session/<sid>/Presentations` endpoint, fetching every presentation in the sessions tagged as methods-oriented. Tradeoff: captures only posters in these 24 sessions — if a methods-interesting poster is in a disease-specific session (e.g., a new pipeline presented in "Lung Cancer Research"), it won't be here. That's fine for the intended use case: *what did AACR show as methods content?*

## PDFs (deferred)

Each record has a `PlayerUrl` like `https://cslide-us.ctimeetingtech.com/play/<uuid>/<token>/pdf?cover=`. ~1-5 MB per PDF, so full set ≈ 500 MB – 2.5 GB. Bulk download:

```bash
mkdir -p pdfs
jq -r '"\(.PresentationNumber) \(.PlayerUrl)"' abstracts.jsonl \
  | xargs -n 2 -P 6 sh -c 'curl -sS -L -o "pdfs/$0.pdf" "$1"'
```

Token signatures in PlayerUrl expire after a few hours — bulk-download while the login session is fresh.
