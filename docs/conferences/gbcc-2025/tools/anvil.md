# AnVIL

**NHGRI Genomic Analysis, Visualization, and Informatics Lab-space** — a cloud-based platform for secure, scalable analysis of controlled-access genomic data (TCGA, dbGaP, *All of Us*). AnVIL co-hosts Galaxy and Bioconductor on Terra/Google Cloud, giving researchers a single environment to bring code to data rather than the other way around.

- **Galaxy tool / platform:** [anvilproject.org](https://anvilproject.org/)
- **Source:** [github.com/anvilproject](https://github.com/anvilproject)
- **Documentation / training:** [anvilproject.org/learn](https://anvilproject.org/learn)
- **Lead authors at GBCC2025:** Stephen L Mosher, Michael C Schatz, Jonathan Lawson, Robert Carroll (oral); Frederick Tan (workshop); Kucher / Schatz (training-and-education talk)
- **Status at GBCC2025:** cloud platform — multi-talk and workshop coverage

## Talks at GBCC2025

- **Day 2 (Tue Jun 24, 2025) — Oral Session 1, Grace Auditorium (oral talk #9):** "Enabling Genomic Research at Scale with NHGRI AnVIL: A Cloud Platform for Genomic Data Analysis" (Mosher / Schatz / Lawson / Carroll)
- **Day 3 (Wed Jun 25) — workshop:** "AnVIL: Secure, scalable computing for controlled access data" (Frederick Tan)
- **Day 3 — Oral Session 4, talk #4:** "Training and education in the cloud with the NHGRI AnVIL" (Kucher / Schatz) — community / training-flavored
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

AnVIL is the NHGRI's strategic genomic-data analysis cloud — a Terra / Google-Cloud-backed environment where controlled-access cohorts (TCGA, dbGaP, *All of Us*) live and compute happens in-place. Researchers spin up Galaxy, Jupyter, RStudio / Bioconductor, or WDL workflow runners adjacent to the data, with NIH-compliant access controls. The GBCC coverage spans (1) the platform itself, (2) a hands-on workshop on running controlled-access analyses, and (3) the training / education pipeline that onboards new users.

## How it works

**Core idea.** AnVIL inverts the conventional "download cohort, analyze locally" pattern: large controlled-access genomic datasets live on AnVIL's cloud storage, and researchers bring compute (notebooks, workflows, R/Bioc sessions) to the data inside Terra workspaces — eliminating bulk egress and the duplication of restricted data across institutional servers.

**Inputs / outputs.** Input is a NIH dbGaP-approved researcher account plus a Terra workspace. Output is whatever the user's analysis produces — a Galaxy history, a Jupyter notebook, an R session, a WDL run — persisted into the workspace's cloud bucket under AnVIL's NIH-compliant access controls.

**Key innovation.** A single substrate (Terra on Google Cloud + Gen3 data commons) hosting both the data and the four main analysis surfaces — Galaxy, Bioconductor / RStudio, Jupyter, and WDL via Dockstore — so cross-toolkit pipelines run in-place against the same data without re-exporting between environments.

**Parameters / API surface worth knowing.**
- **Terra workspaces** — the unit of collaboration and billing; each holds data references, notebooks, workflows, and access controls.
- **Gen3 data commons** — the data-indexing layer that exposes 4.7 PB+ across ~293k participants and 380+ datasets (GTEx, CCDG, CMG, GREGoR, *All of Us*, 1000 Genomes, plus dbGaP studies).
- **Compute runtimes** — Galaxy server, JupyterLab, RStudio/Bioconductor, WDL via Cromwell/Dockstore.
- **Access tiers** — open datasets vs dbGaP-controlled access requiring NIH approval and project-level data-access agreements.

**Canonical example.** From AnVIL documentation: a researcher with dbGaP approval for a TCGA cohort opens a Terra workspace, references the cohort's Gen3-indexed data, launches an RStudio runtime preloaded with Bioconductor, and runs a `SummarizedExperiment`-based analysis against BAMs that never leave the cloud — outputs land in the workspace bucket, and the workspace itself is shareable with named collaborators under the same access controls.

## Where it fits in the corpus

- **AACR 2026:** axis = clinical-trials (controlled-access cohorts — TCGA, dbGaP, *All of Us* — are AACR-relevant for translational and population-genomics work)
- **bioc-to-galaxy** ([entry](bioc-to-galaxy.md)) — AnVIL is the cloud venue where both Galaxy and Bioconductor co-exist; auto-wrapping Bioc packages as Galaxy tools directly benefits AnVIL users
- **Workshop Platform** ([cross-vault entry](../../eurobioc-2025/tools/workshop-platform.md)) — sibling cloud-runtime story on the EuroBioC side
- **GBCC2025 community track** — AnVIL appearing in oral, workshop, and training slots reflects how central it has become

## Notes

Three appearances at one meeting (oral + workshop + training talk) is unusual — it signals that AnVIL is no longer a new platform being introduced but an established substrate that the Bioconductor / Galaxy communities increasingly assume. Cohorts of national scale (*All of Us* at ~1M participants) make in-place compute the only viable model.
