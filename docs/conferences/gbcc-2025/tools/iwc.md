# Intergalactic Workflow Commission (IWC)

**Curated, tested, versioned registry of reproducible Galaxy workflows** — the Galaxy ecosystem's answer to "how do we standardize, test, and distribute community workflows?" IWC ingests workflow contributions, runs CI tests against reference data, versions releases, and publishes them so any Galaxy server can install a known-good copy.

- **Galaxy tool / platform:** [iwc.galaxyproject.org](https://iwc.galaxyproject.org/)
- **Source:** [github.com/galaxyproject/iwc](https://github.com/galaxyproject/iwc)
- **Documentation / training:** [iwc.galaxyproject.org](https://iwc.galaxyproject.org/) and the [Galaxy Training Network](https://training.galaxyproject.org/)
- **Lead author at GBCC2025:** Marius van den Beek
- **Status at GBCC2025:** workflow infrastructure / standardization

## Talk at GBCC2025

- **Speaker:** Marius van den Beek
- **Day / session:** Day 3 (Wed Jun 25, 2025) — Oral Session 3, Grace Auditorium
- **Talk title:** "The Intergalactic Workflow Commission: Standardizing, Testing, and Distributing Reproducible Galaxy Workflows"
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

IWC sits between workflow authors and Galaxy server admins. Authors PR a `.ga` workflow plus a test definition; CI runs the workflow on reference inputs and validates outputs; on merge, the workflow is versioned and published. Galaxy admins (and `usegalaxy.*` mirrors) can pull releases via Ephemeris into their tool panel, knowing each version was machine-tested. The system enforces metadata (license, author, tags), tracks tool dependencies via Conda / containers, and supports semver releases so reruns of an old version are reproducible long after publication.

## How it works

**Core idea.** A monorepo of curated `.ga` Galaxy workflows with CI-enforced linting and end-to-end test execution against reference inputs; merged workflows are version-tagged, mirrored to `iwc-workflows/*` repos, and registered with Dockstore and WorkflowHub for distribution.

**Inputs / outputs.** Input is a contributor PR containing a `.ga` workflow file, a test definition (inputs + expected outputs), and metadata (license, author, tags, institute). Output is a versioned workflow release that any Galaxy admin can pull into a server via Ephemeris, plus Dockstore / WorkflowHub registrations.

**Key innovation.** CI-on-workflows rather than CI-on-tools. Galaxy's tool wrappers have long been tested in the ToolShed; IWC extends that discipline to entire workflows, running them on reference data with every Galaxy release so a published workflow keeps passing as the underlying tool stack moves.

**Parameters / API surface worth knowing.**
- Workflow file — `.ga` Galaxy workflow format, PRed to `galaxyproject/iwc/workflows/`.
- Test definition — paired with each workflow, specifies inputs and expected output assertions for CI.
- Required metadata — license, author attribution, associated institute(s), tags.
- Distribution — GitHub releases per workflow (versioned), auto-deployed to usegalaxy.org / .eu / .org.au; published to Dockstore and WorkflowHub.
- Quality bar — automated linting + test-suite validation + human peer review before merge.

**Canonical example.** A workflow author opens a PR adding `workflows/sars-cov-2-variation/main_workflow.ga` plus a test file pointing to a small reference dataset and expected variant calls. CI lints the `.ga`, spins up a Galaxy instance, runs the workflow, and asserts the outputs match. After review and merge, the workflow is released, mirrored to `iwc-workflows/sars-cov-2-variation`, and auto-installed across the usegalaxy.* federation.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo-tools (workflow-as-code / reproducibility — the substrate beneath any analysis claim that wants to survive review)
- **Nextflow Summit 2026** ([cross-vault](../../nextflow-2026/index.md)) — IWC is to Galaxy what nf-core is to Nextflow: a curated, tested registry sitting on top of a workflow language. Worth tracking which conventions converge.
- **bioc-to-galaxy** ([entry](bioc-to-galaxy.md)) — auto-wrapped Bioconductor tools eventually flow into IWC-curated workflows
- **Workshop Platform** ([cross-vault](../../eurobioc-2025/tools/workshop-platform.md)) — IWC workflows are frequent tenants of hands-on tutorials

## Notes

The nf-core analogy is the fastest way in: IWC is the curation layer, not the runtime. Galaxy itself is the engine; IWC is the package index. Standardizing test fixtures across community workflows is the durable contribution — it converts "works on my server" into "passes CI on a clean install."
