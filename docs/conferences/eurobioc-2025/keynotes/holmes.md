# Susan Holmes — "Latent variables as the best medicine for heterogeneity"

**Affiliation:** Stanford University, Department of Statistics
**Day / session:** Day 1 (Wed Sep 17, 2025) — afternoon keynote
**Talk title:** "Latent variables as the best medicine for heterogeneity"
**Slides (Zenodo DOI):** *to verify after publish*
**Video:** [Bioconductor YouTube — plenaries playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQS_qvtLJNdDqHL6z5jj5y_7) (keynotes recorded)
**Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## Thesis

Biological data — microbiome, single-cell, longitudinal multi-omics — is heterogeneous in ways that defeat both naive pooling and naive stratification: there is shared latent structure across samples that simple mixed-effects models miss and that fully separate per-stratum analyses cannot borrow strength across. The talk argues that latent-variable methods (factor models, generalized matrix factorization, latent-Dirichlet-style topic models, mixOmics-class integrative factorizations) are the right level of abstraction — they let heterogeneity be modeled as structure rather than noise, and they generalize across modalities.

## Speaker context

Susan Holmes is one of the most influential statisticians for biological data of the last two decades — co-author of *Modern Statistics for Modern Biology* (with Wolfgang Huber), longtime collaborator on microbiome statistics (`phyloseq` lineage), and a recurring methodological voice on multi-table / multi-omics integration. Her group has produced foundational work on multivariate methods for compositional and high-dimensional data, longitudinal analysis of pregnancy / preterm-birth cohorts, and the statistical foundations behind several Bioconductor workflows. Inviting her places the keynote slot squarely on *statistical method* rather than *application* — a deliberate signal in a program that otherwise leans heavily on platforms and packages.

## Connections to the corpus

- [omicsGMF](../tools/omicsgmf.md) — generalized matrix factorization is exactly the latent-variable family the keynote is about; this is the most direct package-level link in the EuroBioC2025 program
- [consICA](../tools/consica.md) — consensus independent component analysis; another latent-variable method shipping in the same release
- [edgeR](../tools/edger.md), [MOSCLIP](../tools/mosclip.md) — multi-omics methods that benefit from latent-structure framing
- AACR axis: bioinfo-tools (the statistical-methods sub-axis); virtual-cells (latent representations are the substrate any "virtual cell" model would learn over)

## Open questions

- Which application(s) carry the talk — microbiome, single-cell, longitudinal multi-omics, or all three as a tour? Holmes's recent work has spanned all of them.
- Does she engage directly with the deep-learning latent-variable literature (VAE / scVI-class models) or stay within classical / Bayesian factorization? The framing matters for how it lands with a younger audience.
- Concrete software recommendations or method-pluralism? Holmes tends toward the latter, which would shape any cross-links to specific Bioconductor packages.
