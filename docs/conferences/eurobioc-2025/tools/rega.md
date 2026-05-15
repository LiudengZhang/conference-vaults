# Rega

**R Interface to European Genome-Phenome Archive** — a streamlined, extensible R interface to the EGA API for programmatic upload of metadata, providing a GEO-like Excel submission template by default.

- **Maintainer:** Igor Cervenka (University of Basel) — `igor.cervenka@unibas.ch`
- **Bioconductor:** [Rega v1.0.0](https://bioconductor.org/packages/release/bioc/html/Rega.html)
- **Source:** [git.bioconductor.org/packages/Rega](https://git.bioconductor.org/packages/Rega)
- **Vignettes:** [Rega](https://bioconductor.org/packages/release/bioc/vignettes/Rega/inst/doc/Rega.html)
- **License:** Artistic-2.0
- **Status at EuroBioC2025:** new release (v1.0.0)

## Talk at EuroBioC2025

- **Speaker:** Igor Cervenka (University of Basel)
- **Day / session:** Day 1 (Wed Sep 17, 2025) — afternoon short-talk session, after the Holmes keynote
- **Talk title:** "Rega R interface for EGA metadata submission"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded — short talks at EuroBioC2025 were not part of the plenary YouTube playlist
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

Rega wraps the European Genome-Phenome Archive API in R so that metadata for controlled-access submissions can be assembled, validated, and uploaded programmatically. By default it accepts a GEO-style Excel submission template, lowering the friction for groups already familiar with GEO conventions to deposit into EGA instead.

## How it works

**Core idea.** A three-stage pipeline — parse, validate, submit — over an EGA-shaped Excel template. The template is parsed into a structured in-memory metadata object, run through a client-side validator that checks the schema before any API call, then pushed to EGA via an `httr2`-based client whose endpoints are generated from a bundled YAML API specification.

**Inputs / outputs.** Input: an `ega_full_template_v3.xlsx` workbook with sheets for studies, samples, experiments, runs, datasets, and analyses (columns include `title`, `description`, `alias`, `phenotype`, `biological_sex`, `instrument_model_id`, file references). Output: a parsed metadata object, a validation summary, and — on submission — EGA-side metadata records returned with submission IDs and a yaml log.

**Key innovation.** Client-side validation against the EGA schema *before* anything hits the server — `default_validator()` runs 38+ checks (uniqueness of study/sample/experiment aliases, referential integrity across tables, title length 3–20 words, description length 3–5 sentences, null detection). And the GEO-style default template is a deliberate adoption nudge for groups already submitting to GEO.

**Parameters worth knowing.** `create_client(api, verbosity)` — initializes the authenticated API client; OAuth via `httr2` by default with credentials in OS keyring (no hard-coded secrets). `default_parser()` / `default_validator()` — swap to custom parser/validator if the user has a non-default template. `finalise_submission(id, release_date)` — explicit two-step release.

**Canonical example.** Vignette: `parsed <- default_parser(system.file("extdata/submission_example.xlsx", package = "Rega"))`, then `default_validator(parsed)` to surface schema violations, then `new_submission(parsed, logfile = "log.yaml")` to push to EGA. Submission is finalised separately via `finalise_submission()` (or the EGA GUI) once curators have reviewed.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; relevant axis is clinical-trials / data deposition — EGA submission is a regulatory step for controlled clinical genomics data
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** not mentioned; conceptually adjacent for pipelines that close out by lodging results in EGA

## Notes

Streamlines controlled-data submission — adjacent to the AACR clinical-trials axis where data deposition is a regulatory step. First Bioconductor release; the GEO-template-by-default choice is a deliberate adoption nudge.
