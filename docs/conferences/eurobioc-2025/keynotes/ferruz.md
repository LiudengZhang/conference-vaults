# Noelia Ferruz — "Controllable protein design with language models"

**Affiliation:** IRB Barcelona (Institute for Research in Biomedicine); Ferruz Lab — protein language models (ProtGPT2, ZymCTRL, and successors)
**Day / session:** Day 2 (Thu Sep 18, 2025) — afternoon keynote
**Talk title:** "Controllable protein design with language models"
**Slides:** [Zenodo 10.5281/zenodo.17193056](https://zenodo.org/records/17193056)
**Video:** [Bioconductor YouTube — plenaries playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQS_qvtLJNdDqHL6z5jj5y_7) (keynotes recorded)
**Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## Thesis

Protein language models — autoregressive transformers trained on UniProt-scale sequence corpora — can generate plausible novel proteins, but the practical question for design is *control*: conditioning generation on function (EC class, binding target, stability), on structure (fold family), or on sequence constraints (active-site motifs). The talk likely argues that controllability — via conditional training tags (ZymCTRL-style), classifier-free guidance, or structure-conditioned decoding — is what moves protein-LMs from "interesting samplers" to "useful design tools," with wet-lab validation as the load-bearing evidence.

## Speaker context

Noelia Ferruz leads a group at IRB Barcelona focused on protein language models and their use for de novo design. Her lab released ProtGPT2 (2022), one of the first GPT-2-class autoregressive models trained on protein sequences to demonstrate that LMs can sample novel, foldable, expressible proteins; ZymCTRL extended the approach with conditional control tokens for enzyme class. The lab has continued publishing on controllability, evaluation, and wet-lab characterization of generated sequences. Inviting her into a Bioconductor program signals deliberate bridging — protein-LMs are not native to the R/Bioconductor ecosystem, but they are increasingly the framing for any "AI-driven biology" conversation a methods audience needs to track.

## Connections to the corpus

- AACR axis: virtual-cells — protein-LMs are a foundational layer for any "virtual cell" that needs to reason over protein sequence / function
- AACR axis: agentic-ai — controllable generation is the substrate that closed-loop design agents (generate → predict → assay → update) build on
- AACR axis: bioinfo-tools — the foundation-model sub-axis; closest neighbor in the corpus is the protein / sequence-LM thread of AACR 2026 dossiers (when those come online)
- This is the most "adjacent" keynote in the EuroBioC program — no direct Bioconductor package crosslink, intentionally

## Open questions

- What's new since the last Ferruz public talk — a new model release, a wet-lab campaign, a benchmarking framework, or a methods-paper synthesis? The recording will tell.
- Does she engage with the structure-prediction / inverse-folding literature (ESM3, ProteinMPNN, RFdiffusion) directly, or stay within the sequence-only autoregressive frame? The hybrid is where the field is moving.
- Any concrete tooling story for a Bioconductor / R audience — an interface, a benchmarking dataset, a way for non-ML labs to use these models — or is this a "here's where the field is" talk?
