# HiFi-MAG Pipeline

**Long-read metagenomics within Galaxy** — a Snakemake-based workflow (originally PacBio's `pb-metagenomics-tools`) for recovering high-quality Metagenome-Assembled Genomes (MAGs) from PacBio HiFi reads, packaged into Galaxy by the Schatz lab alongside new profilers and ties to the BioDIGS soil-metagenomics dataset. Schatz lab's contribution to Galaxy's metagenomics stack.

- **Authors:** Tyler Collins, Alex Ostrovsky, Michael Schatz (JHU — Schatz lab)
- **Galaxy tool / platform:** TBD — verify from the talk slides (likely on usegalaxy.org tool panel)
- **Source:** [PacificBiosciences/pb-metagenomics-tools](https://github.com/PacificBiosciences/pb-metagenomics-tools) (upstream Snakemake) · Galaxy wrappers TBD
- **Documentation / training:** [HiFi-MAG-Pipeline tutorial](https://github.com/PacificBiosciences/pb-metagenomics-tools/blob/master/docs/Tutorial-HiFi-MAG-Pipeline.md)
- **Status at GBCC2025:** oral talk on long-read metagenomics within Galaxy

## Talk at GBCC2025

- **Speakers:** Tyler Collins, Alex Ostrovsky, Michael Schatz
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2B
- **Talk title:** "Broadening Metagenomic Horizons in Galaxy: Introducing the HiFi-MAG Pipeline, New Profilers, and Insights from BioDIGS"
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

The pipeline takes HiFi metagenomic assemblies and runs a "completeness-aware" binning strategy: contigs >500kb are screened with CheckM2, those >93% complete are pulled directly into the final MAG set, the rest are binned with MetaBat2 and SemiBin2, merged via DAS_Tool, QC'd with CheckM2 again, and taxonomically assigned with GTDB-Tk. The GBCC talk extends this with new taxonomic profilers and showcases application to BioDIGS (a citizen-science soil microbiome project run out of JHU).

## How it works

**Core idea.** A Snakemake workflow that recovers MAGs from pre-assembled PacBio HiFi metagenomes by short-circuiting the binning step for already-complete long contigs and only running the expensive binning ensemble on what remains.

**Inputs / outputs.** Per sample: `SAMPLE.fasta` (HiFi reads) and `SAMPLE.contigs.fasta` (assembly produced upstream by hifiasm-meta, metaMDBG, or metaFlye — the pipeline recommends these but does not run them itself). Outputs: MAG FASTA files, summary tables joining CheckM2 quality with GTDB-Tk taxonomy, and plots of completeness, contamination, genome sizes, and read-mapping stats.

**Key innovation.** Completeness-aware binning (v2 strategy). Contigs >500 kb are evaluated independently with CheckM2; any that exceed 93% completeness are pulled directly into the final MAG set without going through binning, sidestepping the failure mode where binners fragment a high-quality single-contig genome. Remaining contigs are pooled and binned with MetaBat2 + SemiBin2, merged by DAS_Tool, re-QC'd by CheckM2, and taxonomically assigned by GTDB-Tk.

**Parameters / API surface worth knowing.**
- Contig screening threshold — `min_length` (default 500 kb) for the direct-promotion path.
- Completeness gate — 93% CheckM2 completeness for direct promotion.
- Filter thresholds — completeness ≥70%, contamination <10%, contigs per bin <20 (all configurable).
- Binners — MetaBat2 + SemiBin2 (long-read-tuned), merged by DAS_Tool.

**Canonical example.** From the tutorial: provide HiFi reads and contigs per sample, run `snakemake --use-conda`, and the workflow emits a MAG set with a summary table linking each bin to its CheckM2 quality and GTDB-Tk lineage. The GBCC talk's headline application is BioDIGS soil samples, where HiFi MAGs resolve strains a short-read pipeline would collapse.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo-tools (microbiome / cancer-microbiome); long-read MAGs are the gold standard for strain-resolved cancer-microbiome work
- **mia** ([entry](../../eurobioc-2025/tools/mia.md)) — complementary roles: HiFi-MAG = upstream pipeline producing MAGs; mia = downstream R/Bioconductor analysis container for the resulting community profiles
- **EuroBioC 2025:** mia + miaverse on the analysis side
- **Nextflow Summit 2026:** parallel to nf-core/mag

## Notes

PacBio HiFi long-read MAGs increasingly outperform short-read assemblies for strain-level resolution — relevant for cancer-microbiome studies that need to discriminate closely related taxa. The Schatz-lab Galaxy wrapping makes the pipeline accessible to biologists who don't want to drive Snakemake directly.
