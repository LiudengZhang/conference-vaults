# Bioconductor Workshop Platform

**Hosted infrastructure for authoring and running Bioconductor workshops** — Galaxy-based infrastructure providing containerized, Bioconductor-pre-installed workshop environments. Workshop authors ship Quarto/Rmarkdown content paired with a Docker image so attendees get a one-click reproducible session.

- **Maintainer:** Alexandru Mahmoud (Bioconductor core team)
- **Platform:** [workshop.bioconductor.org](https://workshop.bioconductor.org/)
- **Related package:** [BiocBook](https://bioconductor.org/packages/release/bioc/html/BiocBook.html) (Jacques Serizay) — the Quarto-book authoring framework that pairs with the platform
- **Status at EuroBioC2025:** infrastructure / runtime platform

## Workshop at EuroBioC2025

- **Presenter:** Alexandru Mahmoud (Bioconductor core)
- **Day / session:** Day 2 (Thu Sep 18, 2025) — afternoon hands-on workshop (parallel with OSTA, mia, msqrob2, iSEE)
- **Workshop title:** "Bioconductor Workshop Platform authoring"
- **Format:** hands-on tutorial walking authors through building a workshop image and deploying it to the hosted platform
- **Workshop materials:** *to verify — typically linked from [workshop.bioconductor.org](https://workshop.bioconductor.org/)*
- **Video:** workshops not recorded; the Bioconductor YouTube playlist covers plenaries only
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

The Workshop Platform is a Galaxy-style on-demand container hosting service: an attendee opens a URL, gets a fresh Bioconductor-preinstalled R/RStudio session in a browser, and runs the workshop's Quarto/Rmarkdown materials without any local install. Authors build a Docker image with their package + dependencies, register the workshop, and the platform handles spin-up, isolation, and tear-down. It is the runtime that hosts BiocBook-authored content during BioC, EuroBioC, and GBCC hands-on sessions.

## How it works

**Core idea.** A Galaxy-derived backend orchestrates per-attendee Docker containers behind a Keycloak-authenticated web frontend. Each workshop is packaged as a Docker image preloaded with the relevant Bioconductor release + workshop-specific dependencies; the platform spins up one container per attendee on demand and proxies an in-browser RStudio session to it.

**Inputs / outputs.** Author input: a Docker image (typically built on a `bioconductor/bioconductor_docker` base, layered with the workshop's package and Quarto/Rmarkdown materials) plus a workshop registration record. Attendee input: a workshop URL + Bioconductor account (Keycloak SSO). Output: a fresh, isolated RStudio session in the browser with the workshop content checked out and ready to run; teardown is automatic after the session ends.

**Key innovation.** Pairing with **BiocBook** (Jacques Serizay's Quarto-book authoring framework) closes the loop: BiocBook generates the workshop content as a Quarto book tied to an R package, the package bundles its Docker image build instructions, and the Workshop Platform hosts the resulting image. Authors get a one-pipeline path from package → book → hosted workshop without managing servers or per-event JupyterHub deployments.

**Parameters worth knowing.** Choice of Bioconductor release base image (release vs devel). Per-container resource limits (CPU/RAM/timeout — *exact values not in the public landing page*). Whether the workshop is registered as public or gated. Materials format (Quarto book via BiocBook is the recommended path; raw Rmarkdown also works).

**Canonical example.** *Not specified in vignette* — there is no single canonical example; the platform routinely hosts the EuroBioC2025, BioC2025, and GBCC2025 hands-on sessions (OSTA, mia, msqrob2, iSEE all use it). The Workshop Platform authoring session at EuroBioC2025 itself was the meta-example, walking authors through building a Docker image and registering it.

## Where it fits in the corpus

- **AACR 2026:** no direct dossier; relevant as runtime infrastructure for any AACR adjacent workshop content
- **BiocBook** — pairs with the platform as the authoring half (BiocBook → Workshop Platform pipeline)
- **iSEE** ([entry](isee.md)) — iSEE workshops are typical Workshop Platform tenants
- **OSTA** ([entry](osta.md)) — OSTA chapters can be served via the platform for hands-on sessions
- **Day 3 closing keynote (Jacques Serizay)** — likely covered the BiocBook half of this pipeline
- **GBCC 2025:** queued — used for GBCC hands-on tutorials too

## Notes

Distinct from BiocBook: BiocBook is the *authoring* tool (Quarto-based book scaffolding tied to a package); Workshop Platform is the *runtime* (Galaxy-style on-demand container hosting). Together they form the pipeline used by EuroBioC, BioC, and GBCC for hands-on tutorials.
