# SpectriPy

**Cross-language mass spectrometry: bridging R Spectra and Python matchms** — enables R users of the `Spectra` package to call Python MS analysis code (matchms, MS-similarity scoring, etc.) without leaving R, and vice versa.

- **Maintainer:** Johannes Rainer (Eurac Research) — `Johannes.Rainer@eurac.edu`
- **Bioconductor:** [SpectriPy v1.2.0](https://bioconductor.org/packages/release/bioc/html/SpectriPy.html)
- **Source:** [git.bioconductor.org/packages/SpectriPy](https://git.bioconductor.org/packages/SpectriPy)
- **Vignettes:** [SpectriPy guide](https://bioconductor.org/packages/release/vignettes/SpectriPy/inst/doc/SpectriPy.html)
- **License:** Artistic-2.0
- **Status at EuroBioC2025:** methods talk on cross-language integration

## Talk at EuroBioC2025

- **Speaker:** Johannes Rainer (Eurac Research)
- **Day / session:** Day 1 (Wed Sep 17, 2025) — morning short-talk session, after the Crowell keynote
- **Talk title:** "SpectriPy for cross-language mass spectrometry analysis"
- **Slides:** [Zenodo 10.5281/zenodo.17119120](https://zenodo.org/records/17119120)
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

SpectriPy converts R `Spectra` objects to and from Python MS data structures, then wraps Python similarity-scoring functions from `matchms` so they can be called from R as if they were native. The practical effect: R-pipeline authors can pull in Python MS-ML models without rewriting them, and Python authors can ship their work to R-heavy MS communities.

## How it works

**Core idea.** Bidirectional conversion between R `Spectra` objects and Python `matchms.Spectrum` / `spectrum_utils` objects, plus R wrappers around `matchms` similarity scoring so Python MS routines look like native R calls. The Python side is reached through `reticulate`; in current versions the Python environment is declared via `py_require()` so dependencies (matchms, spectrum_utils, numpy) are pulled in automatically on first use.

**Inputs / outputs.** Input: an R `Spectra` object (from raw `mzML` via the Spectra package). Output: a Python list of `matchms.Spectrum` objects in the R session (via `rspec_to_pyspec`), or an R `Spectra` back the other way (`pyspec_to_rspec`), or an R numeric similarity matrix from `compareSpectriPy`.

**Key innovation.** Removes the practical wall between R-side and Python-side MS ecosystems — the R user keeps a single `Spectra` workflow but can invoke matchms scoring (CosineGreedy, ModifiedCosine, etc.) without writing Python. Comparable in spirit to `reticulate` for general R↔Python but specialized for MS data classes so the conversion is lossless.

**Parameters worth knowing.** Python dependency versions (matchms ≥ 0.1, spectrum_utils ≥ 0.3.2, numpy ≥ 2.2, Python ≥ 3.12 as of v0.99.6). The similarity-method object passed to `compareSpectriPy` (e.g. `CosineGreedy`). Optional reticulate environment overrides if a project already has a managed Python env.

**Canonical example.** Vignette loads a DDA mzML file via `MsDataHub::PestMix1_DDA.mzML()`, builds a `Spectra` object, filters to MS2 spectra with ≥3 peaks, then calls `rspec_to_pyspec(mzml_r)` — yielding a Python list of `matchms.Spectrum` ready for similarity scoring from R.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; cross-language interop is conceptually adjacent to AACR's pathology FM dossiers (also Python-trained, R-consumed)
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** related axis (workflow-level cross-language interop)

## Notes

Same author (Rainer) maintains the `xcms` package for raw LC-MS preprocessing — SpectriPy slots downstream of `xcms`'s output.
