# Sergei L. Kosakovsky Pond — "Interactive Genomic Analytics with responsive notebooks, in-the-browser computation, and AI-assisted development"

**Affiliation:** Temple University — Institute for Genomics and Evolutionary Medicine
**Day / session:** Day 2 (Tue Jun 24, 2025) — Keynote 1, Grace Auditorium (9:00–10:00)
**Talk title:** "Interactive Genomic Analytics with responsive notebooks, in-the-browser computation, and AI-assisted development"
**Slides (Zenodo DOI):** *to verify after publish*
**Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
**Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## Thesis

Genomic analysis is migrating off the server and into the browser — responsive notebooks running compiled code via WASM (Pyodide / WebR / native HyPhy builds), with LLM agents drafting the analysis scaffolding around them. The argument is almost certainly that the *combination* of in-browser compute, reactive notebook UI, and AI-assisted authoring collapses the distance between a published method and a non-developer using it on their own data — i.e., what Datamonkey did for selection analysis, generalized.

## Speaker context

Pond is the lead developer of [HyPhy](http://www.hyphy.org/) (likelihood-based phylogenetic inference for selection, recombination, and rate variation) and a long-time contributor to [Datamonkey](https://www.datamonkey.org/), the public web front-end that has made HyPhy's selection-analysis methods accessible to non-developers for two decades. The Day-2 opening keynote slot is well chosen: Datamonkey is one of the older "compute-on-our-server" web tools in genomics, so a talk from its lead author about *moving compute into the user's browser* is a credible signal that the architecture is shifting. Beyond the title, the specific tooling — Pyodide vs. WebR vs. a HyPhy-native WASM build — is not yet knowable from the schedule alone.

## Connections to the corpus

- AACR axis: **agentic-ai** — "AI-assisted development" puts this talk in conversation with the LLM-agent thread running through Day 2's Oral Session 1
- [GAIA](../tools/gaia.md) — Galaxy's AI agent framework; same Day-2 morning, sets the AI tone for the whole conference
- [GalaxyMCP](../tools/galaxymcp.md) — the MCP-server-for-Galaxy entry; complementary "AI meets workflow tooling" angle
- Cross-link to the [GBCC2025 index](../index.md) for the full Day-2 oral lineup that this keynote opens

## Open questions

- Which WASM runtime does Pond actually demo — a HyPhy-native build, Pyodide, WebR, or all three? The browser-compute story changes meaningfully depending on whether "in-the-browser" means a port of HyPhy or a generic Python/R kernel.
- How concrete is the AI-assisted development claim — a working notebook agent, or a forward-looking sketch? Datamonkey-as-an-LLM-tool would be a natural next step but isn't promised by the title.
- Does the talk address the deployment / privacy argument for browser-side compute (no server, no upload of patient data) explicitly, or stay on the developer-experience side?
