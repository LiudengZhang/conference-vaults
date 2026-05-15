# NOVA (Neutrons Open Visualization and Analysis)

**Galaxy for neutron-scattering data analysis** — an ORNL-led framework that runs on top of NDIP (Neutrons Data Interpretation Platform), itself a Galaxy-based workflow engine for non-bio domains. NOVA bundles `nova-galaxy` (NDIP/Galaxy API client), `nova-trame` (interactive UI), and `nova-mvvm` (consistent app skeleton) so neutron scientists can ship analysis apps without reinventing the workflow stack.

- **Authors:** Gregory R Watson et al. (ORNL Neutron Sciences)
- **Galaxy tool / platform:** [NOVA at ORNL](https://nova.ornl.gov/)
- **Source:** [github.com/neutrons](https://github.com/neutrons) (ORNL neutron-scattering org); core packages also on [code.ornl.gov/ndip](https://code.ornl.gov/ndip)
- **Documentation / training:** [NOVA developer workshop tutorial](https://nova.ornl.gov/tutorial/)
- **Status at GBCC2025:** cross-domain Galaxy deployment

## Talk at GBCC2025

- **Speaker:** Gregory R Watson (ORNL)
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2A, Bush Hall
- **Talk title:** "NOVA: Leveraging Galaxy for Neutrons Scattering Data Analysis and Visualization"
- **Slides:** [Zenodo 10.5281/zenodo.16943194](https://zenodo.org/records/16943194)
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

NDIP is a Galaxy-derived workflow management system tuned for neutron-scattering science: automated data ingestion from beamlines, job submission to ORNL HPC, resource management, and visualization. NOVA is the developer-facing framework on top — three Python libraries that together let an instrument scientist write a Trame UI, wire it to NDIP/Galaxy job execution, and ship a domain-specific app. Reference: Watson, Maier, Yakubov, and Doak, *Frontiers in High-Performance Computing* 2024 ("A galactic approach to neutron scattering science").

## How it works

**Core idea.** NDIP is a Galaxy instance tuned for ORNL's neutron-scattering beamlines — same workflow engine, same tool-wrapping idioms — and NOVA is a three-library Python SDK that lets an instrument scientist build a domain-specific GUI application on top of NDIP without having to re-implement the workflow execution, HPC submission, or data-ingestion plumbing.

**Inputs / outputs.** Input is raw neutron-scattering data ingested from ORNL beamline instruments, plus user-defined Trame UI components describing the desired interactive interface. Output is a deployable scientific app that submits jobs to ORNL HPC via NDIP/Galaxy, visualizes results back in the Trame UI, and persists analysis artefacts in the NDIP workspace.

**Key innovation.** Re-using Galaxy as a non-bio workflow runner: NDIP demonstrates that the Galaxy stack — tool wrappers, history tracking, workflow definitions, job scheduling — is general enough to host materials-science instrumentation pipelines, and NOVA packages the developer experience so domain scientists ship apps rather than scripts.

**Parameters / API surface worth knowing.**
- `nova-galaxy` — Python client for NDIP/Galaxy: submit jobs, fetch results, manage histories from inside an app.
- `nova-trame` — Trame-based interactive UI library (vtk.js + Vue under the hood) for plotting and parameter controls.
- `nova-mvvm` — Model-View-ViewModel skeleton enforcing a consistent app structure across the suite.
- ORNL HPC integration via NDIP's job-submission backend; beamline data-ingestion hooks for automated experiment-to-analysis flow.

**Canonical example.** From the NOVA developer-workshop tutorial: an instrument scientist scaffolds an app using `nova-mvvm`, builds a parameter-entry + 2D-plot UI with `nova-trame`, and wires "Run analysis" buttons through `nova-galaxy` to NDIP-hosted reduction/refinement tools — when an end user clicks Run, the job lands on ORNL HPC via Galaxy's scheduler and results render back in the Trame view, with the full history captured in NDIP.

## Where it fits in the corpus

- **AACR 2026:** orthogonal to AACR axes — this is materials science / physics, not cancer biology
- **EuroBioC 2025:** no equivalent
- **Nextflow Summit 2026:** parallel to nf-core's cross-domain push (e.g. nf-core for chemistry / non-bio workflows)

## Notes

NOVA exemplifies Galaxy's "any-domain workflow runner" pitch. Included for ecosystem-mapping completeness, not direct cancer-research relevance — but the existence of a serious non-bio Galaxy deployment at a national-lab scale is the kind of substrate evidence that makes the platform durable for the bio side too.
