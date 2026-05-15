# AACR Annual Meeting 2026 — Clinical Trials

Poster abstracts for the clinical-trials track at AACR 2026 — Phase 0/I/II/III trials, Late-Breaking Clinical Research, design workshops, and CT-adjacent biomarker/correlative studies.

**642 posters, ~294,000 words of abstract text.** Session transcripts are deferred (the CT minisymposiums are mostly serial readings of these posters; the 294k-word poster corpus is the primary artifact for this topic).

## Files

- `posters/abstracts.jsonl` (2.3 MB) — 642 JSON records, standard schema (`Id`, `Title`, `Abstract`, `AuthorBlock`, `SessionTitle`, `Activity`, `Start`, `PlayerUrl`, etc.)
- `posters/abstracts/` — 642 `.txt` files, pattern `<poster-number>-<title-slug>.txt`
- `full-sessions/` — empty (see "Session transcripts deferred" below)

## Activity breakdown

- **360** Abstract Submission
- **282** Late Breaking and Clinical Trials

## Counts by day

| Day | Posters |
|---|---|
| Apr 19 (Sun) | 72 |
| Apr 20 (Mon) | 247 |
| Apr 21 (Tue) | 241 |
| Apr 22 (Wed) | 82 |

## Session coverage

### Core Phase I / II / III sessions (191 posters)

| Session | Posters | Session ID |
|---|---|---|
| Phase I Clinical Trials in Progress | 28 | 651 |
| Phase I and Phase II Clinical Trials in Progress | 27 | 657 |
| Phase II and Phase III Clinical Trials | 26 | 653 |
| Phase II Clinical Trials | 25 | 656 |
| First-in-Human Phase I Clinical Trials | 23 | 650 |
| Phase II and Phase III Clinical Trials in Progress | 22 | 655 |
| Phase 0 and First-in-Human Phase I Clinical Trials | 21 | 652 |
| Phase I Clinical Trials | 19 | 654 |

### Late-Breaking Research: Clinical Research (66 posters)

| Session | Posters | Session ID |
|---|---|---|
| Late-Breaking Research: Clinical Research 2 | 19 | 630 |
| Late-Breaking Research: Clinical Research 4 | 17 | 632 |
| Late-Breaking Research: Clinical Research 3 | 16 | 631 |
| Late-Breaking Research: Clinical Research 1 | 14 | 629 |

### Methodology / design / access (≥3 posters per session)

| Session | Posters | Session ID |
|---|---|---|
| Biostatistics in Clinical Trials / Surgical Oncology | 13 | 283 |
| Clinical Correlates of Immunotherapy | 10 | — |
| Vaccines and Other Immunomodulatory Agents | 7 | — |
| Regulatory Science and Policy | 6 | — |
| Biomarkers Predictive of Therapeutic Benefit 1–6 | 23 | — |

### CT-adjacent spillover

~385 additional posters across 100+ sessions — biomarker-predictive-of-benefit papers, ADC therapies, immune checkpoint blockade, cellular therapies, etc. — that mention Phase I/II/III or clinical trial in their abstracts. These are CT results reported in subject-specific poster sessions rather than the central CT track.

## Session transcripts deferred

This topic's **session transcripts are not extracted**. Rationale:

1. CT minisymposium talks at AACR are typically authors reading their own poster abstracts verbatim, then taking questions. Adding ~15 × 90 min = 22+ hours of video transcript would duplicate the poster corpus substantially.
2. The poster corpus (~294k words of structured abstract text) is more readily searchable than unstructured auto-captioned transcripts.
3. Session extraction from Swapcard requires CAPTCHA handling + per-session navigation + Vimeo config capture; Chrome downloads are currently blocked in this Claude extraction environment, making the workflow ~5× slower than in the virtual-cells / bioinfo-tools extractions.

If you want specific CT session transcripts, the 25 identified parent sessions are documented below. Each requires one fresh Swapcard navigation.

### High-value CT session targets (for on-demand extraction)

| Session | Session ID | Likely Planning URL pattern |
|---|---|---|
| Clinical Trial Design Workshop: Real World Evidence | 219 | `UGxhbm5pbmdf<b64>` |
| Bayesian and Model-Assisted Designs for Early-Phase Trials | 220 | — |
| Bridging the Gap: Multilevel Strategies to Expand Access to Cancer Clinical Trials | 201 | — |
| New Drugs on the Horizon: Part 1 / 2 / 3 | 547 / 548 / 549 | — |
| Advancing Patient-Centered Clinical Trials | 20 | — |
| Modernizing Clinical Trial Communication: NCI's AI-Enabled Toolkit | 695 | — |
| Leveraging Novel Technologies and Knowledge Bases to Optimize Trial Success | 121 | — |
| Aiming for Cure: Perioperative Clinical Trials | 672 | — |
| Advancing Early-Phase Pediatric Cancer Trials | 23 | — |
| Biostatistics in Clinical Trials / Surgical Oncology | 283 | — |

Planning URLs are in Swapcard's `/event/aacr2026/planning/UGxhbm5pbmdf<base64>` format — discover via search on `connect.aacr26.org`.

## Overlap with sibling topic poster corpora

- **76 posters** also in `single-cell-spatial-omics/posters/` — CT posters with molecular correlates
- **24 posters** also in `bioinfo-tools/posters/` — CT posters with computational/AI content
- **6 posters** also in `virtual-cells/posters/` — CT posters mentioning foundation models
- **546 posters** unique to clinical-trials — pure Phase X / LBCT / biomarker-correlative content

## Extraction pipeline

Different from the other topics due to CT data spanning many sessions:

1. **Keyword union** for abstracts mentioning Phase I/II/III or "clinical trial": 790 unique IDs
2. **Session endpoint** for 25 known CT-track sessions via `/Session/<sid>/Presentations`: 386 presentations
3. **Union by Id**, filter `Activity ∈ {Abstract Submission, Late Breaking and Clinical Trials}` + `PlayerUrl present` → **642 posters**
4. HTML-decode via `DOMParser`, emit JSONL
5. Transport via httpbin POST+echo (Chrome download blocked in this session); extract `.data` field with jq

## PDFs (deferred)

Each record has `PlayerUrl`. ~1–5 MB per PDF × 642 = 0.6–3.2 GB if downloaded in bulk. Token signatures in `PlayerUrl` expire within hours. Bulk download recipe:

```bash
mkdir -p pdfs
jq -r '"\(.PresentationNumber) \(.PlayerUrl)"' abstracts.jsonl \
  | xargs -n 2 -P 6 sh -c 'curl -sS -L -o "pdfs/$0.pdf" "$1"'
```
