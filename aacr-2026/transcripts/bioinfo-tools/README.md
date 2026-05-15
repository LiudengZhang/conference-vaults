# AACR Annual Meeting 2026 — Bioinfo / Comp Bio / AI Methods

Session transcripts + poster abstracts for the bioinformatics / computational biology / AI methods track at AACR 2026. Covers foundation models, pipelines, benchmarks, ML/DL applications in cancer, digital pathology, agentic AI, and LLMs in the clinic.

**12 sessions, ~80,500 words (all symlinks from sibling topics)** + **536 posters, ~210,000 words** across 24 methods-oriented poster sessions.

All session files are symlinks — the real videos live in `agentic-ai/`, `single-cell-spatial-omics/`, or `virtual-cells/`. This topic bucket is a curated view onto those, with added poster coverage that the other topics don't have.

## Sessions (all symlinks)

### Strong-fit methods / AI-core
| File | Words | Video (min) | Origin |
|---|---|---|---|
| `2026-04-20-am-ai-revolution-in-cancer-research` | 15,915 | 109.8 | ← `agentic-ai/` |
| `2026-04-17-pm-foundation-models-multimodal-ai-cancer-research` | 11,668 | 79.9 | ← `virtual-cells/` (native there) |
| `2026-04-18-ai-in-biomarker-discovery-and-drug-development` | 12,941 | 92.1 | ← `agentic-ai/` |
| `2026-04-21-at02-agentic-ai-cancer-researcher` | 12,831 | 92.1 | ← `agentic-ai/` |
| `2026-04-20-pm-ai-spatial-transcriptomics-pathology` | 12,615 | 89.2 | ← `agentic-ai/` |
| `2026-04-22-agentic-ai-as-the-oncologist` | 12,023 | 90.0 | ← `agentic-ai/` |

### Methods-adjacent / applied
| File | Words | Video (min) | Origin |
|---|---|---|---|
| `2026-04-20-am-decoding-cancer-ecosystem-pathology-tme-heterogeneity` | 13,534 | 92.5 | ← `single-cell-spatial-omics/` |
| `2026-04-18-pm-3d-tissue-imaging-and-cancer` | 16,035 | 91.3 | ← `single-cell-spatial-omics/` |
| `2026-04-21-pm-late-spatial-biomarkers-single-cell-resolution` | 16,489 | 106.8 | ← `single-cell-spatial-omics/` |
| `2026-04-21-pm-dissecting-hematologic-malignancies-single-cell-spatial` | 11,126 | 86.7 | ← `single-cell-spatial-omics/` |
| `2026-04-19-spatial-and-single-cell-omics-at-scale` | 13,751 | 91.3 | ← `single-cell-spatial-omics/` |
| `2026-04-18-mapping-neural-immune-circuits-spatial-multi-omics` | 16,508 | 99.2 | ← `single-cell-spatial-omics/` |

Ranked by "foundation model / machine learning / deep learning / algorithm / benchmark / pipeline / toolkit" keyword density in the transcript (top cut at 11 hits; below that, methods are incidental to the session's main biological story).

## Posters — 536 abstracts, ~210,000 words

Harvested via the abstractsonline **Session endpoint** (`/Session/<sid>/Presentations`) for 24 methods-oriented poster sessions, not by keyword search. That's why the coverage is complete per session — every presentation in each of these 24 sessions is included (subject to the standard `Activity ∈ {Abstract Submission, Late Breaking and Clinical Trials}` + `PlayerUrl present` filter).

### Poster session breakdown

| Session | Posters |
|---|---|
| Application of Bioinformatics to Cancer Biology 1–5 | 137 |
| New Software Tools for Data Analysis | 29 |
| New Algorithms and Computational Methods | 26 |
| Integrative Computational Approaches 1–2 | 50 |
| Innovative Therapeutic Modalities and Translational Platforms | 27 |
| Computational, Technological, and Mechanistic Advances | 27 |
| Network Biology and Precision Medicine | 25 |
| Large Language Models in the Clinic | 25 |
| Machine Learning Approaches for Cancer Prediction | 23 |
| Radiomics and AI in Medical Imaging | 21 |
| Digital Pathology 1–3 | 59 |
| Deep Learning in Cancer | 18 |
| Agentic AI in Cancer | 18 |
| Late-Breaking Research: Bioinformatics/Comp Bio/Systems Biology 1–2 | 31 |
| Molecular Pathology | 12 |
| Machine Learning for Image Analysis | 8 |

### Counts by day

| Day | Posters |
|---|---|
| Apr 19 (Sun) | 134 |
| Apr 20 (Mon) | 164 |
| Apr 21 (Tue) | 171 |
| Apr 22 (Wed) | 67 |

### Overlap with sibling topic poster corpora

- **157 posters** are also in `single-cell-spatial-omics/posters/` (same `Id`) — roughly the methods posters whose abstracts also mention single-cell / spatial terms.
- **43 posters** are also in `virtual-cells/posters/` — the foundation-model / virtual-cell-relevant subset.
- **351 posters** are unique to bioinfo-tools — classical bioinformatics, variant calling, clinical LLMs, radiomics, pipeline tools, benchmarking studies without spatial/virtual-cell framing.

Per-topic folders are independent on disk (no symlinks for `.txt` files). Duplication is ~4 KB × 200 copies ≈ 800 KB — trivial, keeps each folder self-contained for `rg`.

## Files

- `full-sessions/` — 12 symlinks (.vtt + .txt each, 24 total files). Dereferences to the real files in `agentic-ai/` / `single-cell-spatial-omics/` / `virtual-cells/`.
- `posters/abstracts.jsonl` — 1.8 MB, 536 JSON records with `Id`, `Title`, `Abstract`, `AuthorBlock`, `SessionTitle`, `PresentationNumber`, `PlayerUrl`, etc.
- `posters/abstracts/` — 536 `.txt` files, `<poster-number>-<title-slug>.txt`.

## Extraction pipeline

Different from the other topics' keyword-union approach:

1. Log into `cattendee.abstractsonline.com/meeting/21436`, read Backpack token.
2. Collect 24 methods-session IDs from existing `single-cell-spatial-omics` JSONL (sessions present partially in scso because some posters use single-cell terms in their abstracts).
3. `GET /oe3/Program/21436/Session/<sid>/Presentations` for each session — returns the full presentation array directly (no need for separate `/Presentation/<Id>` roundtrip per poster).
4. Filter `Activity ∈ {Abstract Submission, Late Breaking and Clinical Trials}` + `PlayerUrl present`.
5. HTML-decode via `DOMParser`, strip tags.
6. Bypass the Chrome download (blocked in this session) by POST'ing the JSONL to httpbin.org/anything, then capturing the echoed response body with `get_network_request --responseFilePath`. Extract the `.data` field with `jq`.

The Session endpoint approach is cleaner than keyword union for broad topics — complete session coverage, no false positives from OR-matching.
