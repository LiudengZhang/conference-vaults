# Bioconductor-to-Galaxy auto-integration

**The load-bearing GBCC2025 storyline** — the joint Galaxy-Bioconductor event's central rationale. A pair of oral talks plus a workshop plus a CoFest deliverable establish the pipeline for wrapping Bioconductor R packages as Galaxy tools, with GSVA as the proof-of-concept and an AI-driven automation pipeline as the production target.

- **Cross-platform integration:** a pair of GBCC2025 talks + a workshop + a CoFest deliverable that together establish the pipeline for wrapping Bioconductor R packages as Galaxy tools
- **Lead community:** Cleveland Clinic / Galaxy Project (Daniel Blankenberg group) + Bioconductor maintainers
- **CoFest deliverable:** GSVA Galaxy tool wrapper (draft PR) — [GSVA on Bioconductor](https://bioconductor.org/packages/release/bioc/html/GSVA.html) (v2.6.1, maintainer Robert Castelo)
- **Status at GBCC2025:** integration / infrastructure (multi-talk + workshop + CoFest)

## Sessions at GBCC2025

### Talk 1 — Day 2 Oral Session 1 (#3)

- **Speakers:** Jayadev Joshi, Fabio Cumbo, Daniel Blankenberg (Cleveland Clinic / Galaxy)
- **Title:** "Automated integration of R/Bioconductor tools into Galaxy"
- **Theme:** the production pipeline — taking arbitrary Bioconductor packages and emitting Galaxy tool XML + Conda environment + test data automatically

### Talk 2 — Day 2 Oral Session 2A (#8)

- **Speakers:** Fabio Cumbo, Jayadev Joshi, Daniel Blankenberg
- **Title:** "Towards the automatic integration of tools in Galaxy: the anvi'o suite and a new AI-driven automation pipeline"
- **Theme:** AI-driven extension of the same pipeline — using LLMs to infer parameter schemas, generate test cases, and reduce the manual effort of Galaxy tool wrapping. anvi'o is the case study; Bioc is the broader target

### Workshop — Day 3

- **Presenter:** Daniel Blankenberg (Cleveland Clinic / Galaxy Project)
- **Title:** "Streamlining Bioinformatics: Adding Bioconductor Tools in Galaxy"
- **Format:** hands-on; participants wrap a Bioconductor package as a Galaxy tool live

### CoFest deliverable — Day 5-6

- **Target:** GSVA (Bioc) → Galaxy tool wrapper, draft PR
- **Team:** Fabio Cumbo, Jayadev Joshi, Bryan Raubenolt, Daniel Blankenberg + on-site Sean Doyle, Polina Yagudayeva, Charlotte Soneson, Marcel Ramos Pérez; remote Robert Castelo (GSVA maintainer)
- **Why GSVA:** widely-used pathway-scoring method, stable API, Castelo is engaged as remote maintainer — low-risk proof-of-concept for the auto-integration pipeline

## What it does (and why it matters)

Bioconductor's value is its 2,000+ curated R packages; Galaxy's value is reproducible web-accessible workflow execution for users who don't write code. The historical friction is that wrapping a Bioc package as a Galaxy tool is hand-built, version-fragile, and labor-bottlenecked on a small number of maintainers. The GBCC2025 sequence — two talks scoping the automation pipeline, a workshop teaching the manual baseline, a CoFest sprint producing a real wrapper (GSVA) — is the joint community's coordinated push to industrialize the bridge: an AI-assisted generator that takes a Bioc package's `DESCRIPTION` + man pages + vignette and emits a working Galaxy tool with minimal human review.

## How it works

**Core idea.** Auto-translate the metadata that already exists in an R/Bioconductor package — `DESCRIPTION`, roxygen-documented function signatures, man pages, vignette code — into the four artefacts a Galaxy tool needs: a tool XML (parameters + outputs + help), a Conda `<requirements>` block pinning R + Bioc + the package, a wrapper R script that maps Galaxy CLI args back to the function call, and a test definition with reference inputs.

**Inputs / outputs.** Input: a target R/Bioconductor package (URL or name) and the chosen entry-point function(s). Output: a PR-ready Galaxy tool wrapper — XML + R driver + Conda env + tests — that can be merged into `galaxyproject/tools-iuc` and from there into IWC workflows.

**Key innovation.** LLM-assisted wrapper drafting (Cumbo / Joshi / Blankenberg). The initial GSVA wrapper was drafted by Gemini from the package's R-side documentation, then refined by humans — proof that LLM agents can produce the tedious schema-translation step. A parallel Python-side pipeline (the [R2G2 framework](https://www.biorxiv.org/content/10.64898/2025.12.22.695980v1) and the anvi'o argparse-driven approach) shows the same principle ports to Python tools.

**Parameters / API surface worth knowing.**
- Source signal — R `DESCRIPTION` (package + version + deps), roxygen `@param` tags (parameter types + help), vignette code (canonical usage examples for test fixtures).
- Output artefacts — Galaxy tool XML (`<inputs>`, `<outputs>`, `<command>`, `<requirements>`, `<tests>`); R wrapper script; Conda env file; reference test data.
- LLM step — used to map roxygen `@param` descriptions to Galaxy XML parameter types (boolean / integer / float / select / data) and to draft help text.
- Manual review gate — humans verify the generated XML, parameter coverage, and test outputs before merging the PR.

**Canonical example.** GSVA (the CoFest deliverable). The pipeline ingested the [GSVA Bioconductor package](https://bioconductor.org/packages/release/bioc/html/GSVA.html), produced a draft Galaxy tool wrapper exposing the `method`, `kernel`, and `min.sz` / `max.sz` parameters, ran the wrapper against a reference expression matrix + gene-set collection, and confirmed the output gene-set-by-sample score matrix matched a direct R call — making GSVA the demonstration that the auto-wrap pipeline can produce a real, mergeable Galaxy tool from a real Bioc package.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo-tools (Galaxy-wrapped Bioc tools are exactly what enables wet-lab cancer biologists to run reproducible analyses without an R bench scientist)
- **mia** ([entry](mia.md)) — Tuomas Borman is core to both the microbiome Bioc ecosystem AND its Galaxy bridge; the GBCC mia framing emphasized Galaxy / cross-platform export
- **GAIA** ([entry](gaia.md)) and **GalaxyMCP** ([entry](galaxymcp.md)) — sister AI-/automation-flavored Galaxy talks; together with this entry they trace the AI-augmented future of the Galaxy platform
- **atena** ([entry](atena.md)) — Castelo-maintained; a natural next package for the same auto-integration pipeline once GSVA is shaken out
- **EuroBioC 2025:** not presented (this is the GBCC-specific story — the joint event's whole rationale)
- **Nextflow Summit 2026:** parallel question in a different ecosystem (Nextflow vs. Galaxy as workflow substrates); not directly cross-referenced but worth tracking

## Notes

This is the load-bearing GBCC story — the "joint Galaxy-Bioconductor conference" exists as a venue precisely to coordinate this integration work. The CoFest GSVA wrapper is the proof-of-concept that the automation pipeline can produce a real, mergeable Galaxy tool from a real Bioc package; the auto-integration pipeline (talks 1 + 2) is the production target that scales the proof-of-concept to the long tail of Bioc. If the pipeline ships, the bridge between Bioconductor and Galaxy stops being a per-package craft project.
