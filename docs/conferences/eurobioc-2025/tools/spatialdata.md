# SpatialData

**An open and universal data framework for spatial omics** — a FAIR storage format and Python library collection for performant access, alignment, and processing of multi-modal spatial-omics datasets. Cross-language interop with R/Bioconductor is an active development direction and the focus of the EuroBioC2025 talk.

- **Authors / community:** scverse community — lead authors Luca Marconato, Giovanni Palla, Kevin A. Yamauchi, Helena Crowell
- **Upstream framework:** [github.com/scverse/spatialdata](https://github.com/scverse/spatialdata) (Python-primary; R interop layer in development)
- **Paper:** [Marconato et al., *Nature Methods* 2024](https://www.nature.com/articles/s41592-024-02212-x)
- **Status at EuroBioC2025:** external / pre-release in R (Python framework mature; R interop in development — focus of the talk)

## Talk at EuroBioC2025

- **Speaker:** Luca Marconato (lead Python author)
- **Day / session:** Day 2 (Thu Sep 18, 2025) — late-morning short-talk session, before the Ferruz keynote
- **Talk title:** "SpatialData framework for cross-language interoperability"
- **Slides:** [Zenodo 10.5281/zenodo.17293885](https://zenodo.org/records/17293885) (Marconato et al. — cross-community spatial-biology talk)
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

SpatialData defines a Zarr-backed FAIR storage format and a Python library stack for multi-modal spatial-omics data — co-registered images, tables, shapes (cells, regions), and points (transcripts) — with consistent transforms for alignment across modalities. The Bioconductor angle is interop: how `SpatialExperiment` / `SingleCellExperiment` objects round-trip to and from on-disk SpatialData stores so an R analyst can pick up a scverse-prepared dataset (or vice versa) without losing structure.

## How it works

**Core idea.** Define a single on-disk container (Zarr + Parquet, built on the OME-NGFF specification) that holds the five element types of a spatial-omics experiment plus a coordinate-system graph; every element declares one or more named extrinsic coordinate systems via affine transformations, so cross-modality alignment becomes a graph traversal rather than a re-resampling.

**Inputs / outputs.** Input: raw vendor outputs from Visium, Xenium, MERFISH, CosMx, IMC, etc., loaded via reader functions. Output: a single SpatialData store on disk (Zarr + Parquet) containing five element types — **images** (multiscale arrays, xarray/dask-backed), **labels** (integer pixel masks), **shapes** (geopandas polygons/circles, e.g. Visium spots or cell outlines), **points** (Parquet-backed single-molecule coordinates), and **tables** (AnnData objects annotating any of the above via `region_key`/`instance_key`).

**Key innovation.** Prior substrates handled one modality cleanly but composed badly: `AnnData` is table-first, `SpatialExperiment` is R-only, `Squidpy`/`Giotto` are tool-specific containers. SpatialData's contribution is the coordinate-system layer — intrinsic systems tied to each element plus named extrinsic systems linked by `scale`/`translation`/`rotation`/sequence transformations — which lets Visium spots, an H&E image, and a Xenium transcript map all live in one store and align on demand. The OME-NGFF foundation makes the format FAIR-by-construction (findable, interoperable, web-accessible via Zarr).

**Parameters worth knowing.** Coordinate-system names — the strings analysts use to ask "render everything aligned to `global`." Transformation type — `Identity`, `Scale`, `Translation`, `Affine`, `Sequence`. Multiscale image levels — pyramidal storage for lazy zoom. `region_key` / `instance_key` on tables — the join keys back to shapes or labels.

**Canonical example.** *Cross-language interop is the focus of the EuroBioC2025 talk and the specific R-side reader/writer story is not specified in vignette; needs talk slides.* The published paper demonstrates Visium + Xenium co-registration on a single tissue section and integrated multi-modal queries spanning images, transcripts, and cell tables in one store.

## Where it fits in the corpus

- **AACR 2026:** axis = single-cell & spatial omics; SpatialData is the de facto Python-side data substrate for spatial-omics pipelines
- **OSTA** ([entry](osta.md)) — both target spatial omics; OSTA covers the R/Bioc side, SpatialData covers Python with R-interop being the bridge
- **Helena Crowell Day 1 keynote** — Crowell is one of the SpatialData co-authors
- **ISMB 2026:** scaffold; scverse + spatial methods
- **GBCC 2025:** queued

## Notes

This is the cross-language bridge between scverse (Python) and the Bioconductor `SpatialExperiment` / OSTA-book ecosystem. Watching the R-interop layer mature is one of the more consequential storylines for the spatial-omics axis across both EuroBioC and the AACR vault's spatial dossiers.
