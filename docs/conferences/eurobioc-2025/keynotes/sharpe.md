# James Sharpe — "C3PO: Cell 3D Positioning by Optical encoding"

**Affiliation:** EMBL Barcelona (head of unit; Multicellular Systems Biology)
**Day / session:** Day 2 (Thu Sep 18, 2025) — morning keynote
**Talk title:** "C3PO: Cell 3D Positioning by Optical encoding"
**Slides (Zenodo DOI):** *to verify after publish*
**Video:** [Bioconductor YouTube — plenaries playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQS_qvtLJNdDqHL6z5jj5y_7) (keynotes recorded)
**Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## Thesis

C3PO appears to be a new optical-encoding approach to assign 3D spatial positions to individual cells — a non-trivial problem for dissociated single-cell experiments where the tissue context is lost at sequencing time, and a complementary problem for in-situ methods where segmentation in 3D is hard. Sharpe's lab has historically argued that *acquisition geometry* is itself a methodological frontier (Optical Projection Tomography, mouse limb development atlases), so the talk likely frames C3PO as another "encode the geometry into the measurement" play rather than reconstructing geometry post-hoc.

## Speaker context

James Sharpe heads the Multicellular Systems Biology unit at EMBL Barcelona and is one of the inventors of Optical Projection Tomography (OPT), a foundational 3D imaging method for developmental biology. His group's signature work has been on mouse limb morphogenesis — combining live imaging, computational modeling, and quantitative cell tracking. Inviting him to a Bioconductor / methods conference signals that the program wants the *upstream* end of the spatial-omics pipeline represented: the data that downstream R/Python frameworks ingest is shaped by what the microscope and the labeling chemistry can encode. C3PO is, on the title alone, a continuation of that lineage.

## Connections to the corpus

- [SpatialData](../tools/spatialdata.md) — at the data-substrate level: any 3D-positioning method has to produce coordinates that downstream frameworks (SpatialData, SpatialExperiment) can hold and visualize
- AACR axis: single-cell-spatial-omics — but this is the *acquisition* end of that axis, not the analysis end; most AACR spatial dossiers are about analysis tools that assume coordinates are already in hand
- Closest analytical kin in the corpus: cross-modality registration / segmentation tooling rather than gene-level methods

## Open questions

- Is C3PO an optical / hardware method, a barcoding-based method, or a hybrid (e.g., spatial barcoding patterns read out by imaging)? The acronym "Optical encoding" hints at hardware-side, but the field has converged on hybrids.
- What is the readout — can it be combined with single-cell sequencing on the same cells (a la Slide-seq / Stereo-seq lineage), or is it imaging-only?
- Is there an open-source software component (a Bioconductor or scverse package) that ships with the method, or is this a pure-method talk in front of a software audience?
