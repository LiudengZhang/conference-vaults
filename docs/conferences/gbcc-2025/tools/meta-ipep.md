# Meta-iPep

**Metaimmunopeptidomics pipeline implemented in Galaxy** — characterizes HLA-bound peptides from mass-spectrometry immunopeptidomics data with an extended search space that includes microbial peptides, supporting neoantigen and microbial-antigen discovery for cancer immunotherapy.

- **Galaxy tool / platform:** [usegalaxy.org](https://usegalaxy.org/) — pipeline distributed via the Galaxy proteomics tool suite (Mehta / Jagtap, U Minnesota)
- **Source:** [github.com/galaxyproteomics](https://github.com/galaxyproteomics) — search for `meta-ipep` / `iPep` repos
- **Documentation / training:** [Galaxy Training Network — proteomics](https://training.galaxyproject.org/training-material/topics/proteomics/) (Meta-iPep-specific tutorial TBD)
- **Authors at GBCC2025:** Katherine T Do, Subina Mehta et al. (U Minnesota Galaxy proteomics team — Pratik Jagtap collaborating)
- **Status at GBCC2025:** oral talk on a Galaxy-native immunopeptidomics pipeline

## Talk at GBCC2025

- **Speakers:** Katherine T Do, Subina Mehta
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2B
- **Talk title:** "Meta-iPep: A metaimmunopeptidomics pipeline implemented within Galaxy platform to characterize HLA-bound microbial peptides for immunotherapy"
- **Slides:** [Zenodo 10.5281/zenodo.15982018](https://zenodo.org/records/15982018)
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

Meta-iPep is an end-to-end Galaxy workflow for immunopeptidomics: from raw MS spectra of HLA-class-I/II eluted peptides through database search (extended with microbial peptide databases — the "meta" prefix), FDR control, and HLA binding-affinity filtering. The output is a list of high-confidence HLA-bound peptides annotated with origin (human / microbial), suitable for neoantigen ranking or microbial-antigen discovery. Implementing it in Galaxy makes the pipeline reproducible and shareable across the immunopeptidomics community.

## How it works

**Core idea.** Meta-iPep follows the U Minnesota Galaxy-P group's metaproteomics blueprint — a Galaxy workflow that chains custom database construction → peptide-spectrum matching → FDR-controlled identification → taxonomic / functional annotation — and re-targets it at HLA-eluted peptides, with the database extended to include microbial sequences alongside the host proteome.

**Inputs / outputs.** Input: raw MS spectra from HLA class-I / class-II immunoprecipitation eluates (mzML / RAW). Output: an FDR-filtered list of HLA-bound peptides annotated by source organism (human / microbial), suitable for neoantigen ranking or microbial-antigen discovery.

**Key innovation.** The "meta" prefix — extending the immunopeptidomics search space to microbial peptides. Standard HLA peptidomics pipelines search only the human proteome and discard everything else; Meta-iPep builds a composite human + microbial database so tumor-associated microbial peptides (gut or intratumoral) get a chance to be identified rather than silently rejected.

**Parameters / API surface worth knowing.**
- Search engine — *not specified in the public Zenodo landing*; the related U Minnesota clinical-metaproteomics workflow (Do et al., JoVE 2025) uses SearchGUI-orchestrated engines (X!Tandem / MS-GF+ / Comet) within Galaxy, which is the likely substrate.
- Database construction — composite host + microbial peptide database (the "meta" step); microbial sequences likely sourced from a curated metaproteomics database such as MetaPep.
- FDR control — standard target-decoy strategy at the PSM / peptide level; specific tool — *not specified in landing*.
- HLA binding filter — predictor (NetMHCpan-family) and threshold not specified in the public abstract.

**Canonical example.** *Not specified in the public Zenodo landing for slides 10.5281/zenodo.15982018.* The talk's framing positions the canonical run as HLA-I/II eluates from a tumor sample passed through the Galaxy workflow, yielding a peptide list partitioned into human-derived (candidate neoantigens) and microbial-derived (candidate microbial antigens) for immunotherapy follow-up.

## Where it fits in the corpus

- **AACR 2026:** axes = clinical-trials + bioinfo-tools — HLA-bound peptide characterization is the MHC-I/II ligandome readout that drives neoantigen-based vaccines and TCR-T therapies, AACR-bread-and-butter
- **Pratik Jagtap workshop (Day 3)** — "Immunopeptidogenomics Pipeline in Galaxy for MHC-Bound Neoantigens" — same U Minnesota Galaxy proteomics team, hands-on counterpart to the Meta-iPep oral talk
- **GBCC2025 cancer-immunotherapy thread** — direct line to neoantigen / TCR-T translational work

## Notes

Direct cancer-immunotherapy relevance — this is the readout layer for any neoantigen-vaccine or TCR-T program. The "meta" prefix is the differentiator: standard immunopeptidomics searches skip microbial sequences, but tumor-associated microbes (gut microbiome, intratumoral bacteria) contribute peptides worth scanning for. Galaxy implementation is the reproducibility lever — these pipelines historically lived as bespoke scripts on individual lab servers.
