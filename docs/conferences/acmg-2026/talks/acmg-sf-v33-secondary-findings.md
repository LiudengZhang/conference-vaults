# Beyond The List — Scope and Implementation of ACMG Secondary Findings (v3.3+)

**ACMG 2026 standards-update symposium on the Secondary Findings list — current v3.3 implementation gaps, future scope expansion (including pediatric-onset cancer-predisposition reporting), and the "Beyond The List" question of whether SF should remain a closed gene-set or shift to a framework-based model.**

- **Speaker / institution:** ACMG Secondary Findings Working Group (SF WG); panel composition TBC from GIM supplement and ACMG Statements
- **Anchor type:** guideline
- **Day / session:** Mid-meeting featured symposium (Day 3–4, Mar 12–13, 2026); exact slot TBD
- **Status:** post-meeting; from ACMG meeting site featured-session listing; whether SF v3.4 was officially released at the meeting TBD pending GIM supplement and ACMG Statements page

## Headline finding

The Secondary Findings list — first published 2013 with 56 genes, now at **v3.3 (2023, 81 genes)** — is at a structural inflection: incremental gene-addition cycles are reaching diminishing returns, while the underlying clinical-lab universe has shifted (universal-WGS pediatric programs, expanded carrier screening, newborn-WGS pilots, NIFS) in ways that strain the original SF framing. **Cancer-predisposition genes dominate** the list — BRCA1, BRCA2, TP53, MLH1, MSH2, MSH6, PMS2, APC, MUTYH, PTEN, RB1, RET, VHL, WT1, plus newer additions — and the policy load on the list comes disproportionately from cancer reporting. Specific SF v3.4 gene additions / removals (if any) and revised reporting recommendations TBD pending GIM supplement and the ACMG Statements page.

## Methodology / framework

Framework discussion: (a) actionability criteria — clinical-management change must be available, validated, and meaningful; (b) penetrance thresholds — minimum age-of-onset-adjusted penetrance for inclusion; (c) gene-list maintenance cadence vs framework-based opt-in; (d) pediatric reporting framing — should adult-onset cancer-predisposition genes (BRCA, Lynch) be reported in pediatric WGS at all? Cross-references ClinGen Hereditary Cancer VCEPs for gene-disease validity backbone.

## Lab-translation deep dive

**Validation requirements.** SF reporting requires the lab to validate the same genes on the same sample to the same depth / completeness as the primary indication — there is no half-validated SF tier. Practical floor: ≥20x at >99% of coding bases for the entire 81-gene v3.3 list, with explicit PMS2 / PMS2-pseudogene disambiguation (a perennial SF-list bioinformatics failure mode), PMS2CL handling, MSH2 inversion detection, and SMN1/SMN2 distinguishing capability for any genes with paralog issues. Validation packages must include exon-level CNV detection for relevant genes (BRCA1, BRCA2, MLH1, MSH2, MSH6, PMS2, EPCAM).

**Lab-stack changes.** WGS labs absorb SF reporting more easily than panel / exome labs because coverage is uniform; panel labs must explicitly add SF capture probes when SF is offered as opt-in. Operational adds: opt-in / opt-out consent capture at order, SF-specific curation queue, separate SF report (or clearly delineated SF section), and patient-facing return-of-results workflow for the inevitable BRCA / Lynch positive that lands on a patient consented to SF but ordered for an unrelated indication.

**Regulatory / insurance.** SF reporting is in-scope under CLIA / CAP as part of any test offering SF — no separate FDA pathway. Payer coverage is the load-bearing constraint: BRCA / Lynch positives identified via SF need downstream surveillance / risk-reducing intervention coverage that often hinges on family-history criteria the patient may not meet. Equity / access is the most-cited gap.

**Variant curation.** ClinGen Hereditary Cancer VCEPs are the gene-disease-validity backbone; SF v3.3 already incorporates VCEP curation. SF v3.4 framework-vs-list question (TBD pending GIM supplement) materially changes curation cadence — a framework-based SF requires per-variant actionability gating, not just per-gene inclusion.

## Where it fits in the corpus

- **AACR 2026:** hereditary-cancer panel composition and universal-testing implementation sessions — the SF list is the floor below which cancer-genetics labs cannot go
- **ASCO 2026:** trial-eligibility pathways for BRCA / Lynch / Li-Fraumeni patients identified via incidental SF reporting
- **ASHG 2026 / ESHG 2026:** parallel European policy debates (which are more restrictive on incidental cancer reporting)
- Related ACMG 2026: [presidential-plenary-nbs-expansion.md](./presidential-plenary-nbs-expansion.md), [hereditary-cancer-adult-genetics.md](./hereditary-cancer-adult-genetics.md), [nifs-non-invasive-fetal-sequencing.md](./nifs-non-invasive-fetal-sequencing.md)

## Open questions

- Should SF v3.4 (or successor) shift from a closed gene-list to a framework-based opt-in?
- Pediatric-WGS reporting of adult-onset cancer-predisposition variants — at what age, to whom?
- Equity / access — SF reporting is only as good as the downstream surveillance pathway

## Sources

- [ACMG 2026 meeting site](https://www.acmgmeeting.net/)
- [ACMG main site / Statements](https://www.acmg.net/)
- GIM abstract supplement: pending (~April–May 2026)
- ACMG Digital Edition: [acmgeducation.net](https://www.acmgeducation.net/)
- [ClinGen Resource](https://www.clinicalgenome.org/) — gene-disease validity backbone for SF list
