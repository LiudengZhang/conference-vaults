# AACR 2026 — Clinical Trials Posters

**642 poster abstracts, ~294,000 words** covering Phase 0/I/II/III trials, Late-Breaking Clinical Research, and CT-adjacent biomarker/correlative studies.

## Files

- `abstracts.jsonl` (2.3 MB) — one JSON record per poster with `Id`, `Title`, `Abstract` (HTML-decoded), `AuthorBlock`, `SessionTitle`, `Activity` (Abstract Submission vs Late Breaking), `Start`, `End`, `PresentationNumber`, `PlayerUrl`.
- `abstracts/` — 642 `.txt` files, pattern `<poster-number>-<title-slug>.txt`.

## Counts

| | |
|---|---|
| Total posters | 642 |
| Abstract Submission | 360 |
| Late Breaking and Clinical Trials | 282 |
| Total abstract text (words) | ~294,000 |

## Top session groupings

- **Phase I/II/III core sessions** — 191 posters (8 sessions)
- **Late-Breaking Research: Clinical Research 1-4** — 66 posters
- **Biomarker-correlative** (Biomarkers Predictive of Therapeutic Benefit 1-6, etc.) — 50+ posters
- **Cellular therapy / CAR-T trials** — 30+ posters
- **ADC / bispecific antibody trials** — 20+ posters
- **Regulatory / design / access** — 25+ posters (Biostatistics, Regulatory Science, Bridging the Gap, etc.)

Full per-session breakdown in the parent `../README.md`.

## Common `jq` recipes

```bash
# All Phase I trials
jq -c 'select(.SessionTitle | test("^Phase 0|^First-in-Human|^Phase I Clinical Trials"; "i"))' abstracts.jsonl

# All ADC-related posters
jq -c 'select((.Title + .Abstract) | test("antibody.drug conjugate|\\bADC\\b"; "i"))' abstracts.jsonl | wc -l

# NCT IDs in abstracts
jq -r '.Abstract' abstracts.jsonl | grep -oE 'NCT[0-9]{8}' | sort -u | wc -l

# Trials by cancer type (lung)
jq -c 'select(.Abstract | test("NSCLC|lung cancer|SCLC"; "i")) | {num: .PresentationNumber, title: .Title[:80]}' abstracts.jsonl | head -20
```

## Session transcripts deferred

Unlike the other topic folders, clinical-trials has **no session transcripts**. Rationale: CT minisymposium content is largely a serial reading of posters by their authors; the 294k-word poster corpus already covers the material. See parent `README.md` for the list of 25 CT session IDs that can be extracted on demand.

## Extraction approach

Hybrid of keyword union + session endpoint (see parent README). The 642-poster union is conservative — it captures posters whose abstracts literally mention "Phase I/II/III" or "clinical trial", plus every presentation in the 25 identified CT-track sessions. Posters reporting early trial data that don't use these phrases (e.g., "dose-escalation" only) are in subject-specific sessions and would appear in those topic folders instead.
