# EuroBioC 2025

**European Bioconductor Conference 2025** — Barcelona Biomedical Research Park (PRBB), Barcelona, Spain · September 17–19, 2025.

> **Status:** Pilot vault — scaffolding the bioinformatics-tools template here before scaling to GBCC2025, BioC2026, ISMB, and RECOMB. Conference concluded; source material public and stable.

## Why this is in the vault

Bioconductor is *the* release pipeline for R-based bioinformatics — every short talk maps to an installable package with vignette + GitHub repo + benchmarks. EuroBioC2025 is the European leg, ~3 days, tighter signal than the broader GBCC2025 (Galaxy + Bioconductor joint). Five keynotes and ~25 short talks span the axes we care about: single-cell, spatial omics, statistical modeling, AI-driven design, infrastructure, multi-omics.

This vault gives the AACR tools matrix a deeper bench: not just "tool used in a cancer paper" but "tool released, reviewed, and benchmarked in the package ecosystem."

## What we have to work with

| Source | Coverage | Notes |
|---|---|---|
| **Plenary recordings** | keynotes | [Bioconductor YouTube playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQS_qvtLJNdDqHL6z5jj5y_7) |
| **Schedule** | full program | [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html) |
| **Community recap** | overview + photos | [Bioconductor blog post](https://blog.bioconductor.org/posts/2025-10-24-EuroBioC2025-recap/) |
| **Slides** | varies per talk | typically posted to [Zenodo Bioconductor community](https://zenodo.org/communities/bioconductor) |
| **Packages** | every short talk | Bioconductor / CRAN page + source + vignette + downloads |
| **Workshops** | day 2 afternoon | OSTA, microbiome, msqrob2, Workshop Platform, iSEE — public GitHub repos |
| **Press** | minimal | academic conf, no general-press coverage |

## Program shape

- **Day 1 (Wed Sep 17)** — Vince Carey "A coherent ecosystem for genomic data science: 25 years of Bioconductor"; Helena Crowell "Colorectal cancer through whole-transcriptome imaging"; short-talk session on metabolomics / proteomics / network methods; Susan Holmes "Latent variables as the best medicine for heterogeneity"; short-talk session on differential expression / multi-omics / community resources; poster session; conference dinner.
- **Day 2 (Thu Sep 18)** — James Sharpe "C3PO: Cell 3D Positioning by Optical encoding"; short-talk sessions on epigenomics and spatial omics; Noelia Ferruz "Controllable protein design with language models"; afternoon hands-on workshops (OSTA, microbiome, msqrob2, Workshop Platform, iSEE); poster session.
- **Day 3 (Fri Sep 19)** — Jacques Serizay "Enhancing genomic research with community-driven flexible software"; flash talks; Birds of a Feather; closing.

## Organization

```
conferences/eurobioc-2025/
├── index.md                 # this page
├── themes.md                # cross-day synthesis
├── digest/
│   ├── day-1.md
│   ├── day-2.md
│   └── day-3.md
├── topics/                  # Bioconductor subdomains
│   ├── single-cell/
│   ├── spatial/
│   ├── multi-omics/
│   ├── statistical-genomics/
│   ├── infra-devops/
│   └── visualization/
├── tools/                   # PRIMARY artifact — one entry per package
│   └── index.md
└── sessions/                # full abstracts, indexed
    └── index.md
```

The `tools/` directory is the load-bearing artifact — every short talk yields one entry, each keynote gets a longer treatment.

## What's different from AACR / Nextflow templates

- `tools/` is **primary**, not secondary — every short talk yields a row, not just the noteworthy ones
- Each tool entry has the full source quartet: package page + vignette + slides (Zenodo DOI when available) + video (where recorded)
- Cross-vault "Mentioned at:" links — a tool released at EuroBioC2025 can point to its appearance in the AACR vault, the planned GBCC2025 / BioC2026 vaults, and vice versa

## Sources

- [EuroBioC2025 conference site](https://eurobioc2025.bioconductor.org/)
- [EuroBioC2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)
- [Plenary recordings (YouTube)](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQS_qvtLJNdDqHL6z5jj5y_7)
- [EuroBioC2025 community recap](https://blog.bioconductor.org/posts/2025-10-24-EuroBioC2025-recap/)
- [Bioconductor.org](https://www.bioconductor.org/)
- [Bioconductor on Zenodo](https://zenodo.org/communities/bioconductor)

## Next step

See [`tools/`](tools/) for the per-tool entry template. We're drafting 3 sample entries (single-cell / infra / visualization) before running bulk extraction via Codex over the ~25 short talks + 5 keynotes + 5 workshops.
