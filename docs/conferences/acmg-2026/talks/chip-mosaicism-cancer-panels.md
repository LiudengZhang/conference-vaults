# Clonal Hematopoiesis, Somatic and Post-Zygotic Mosaicism in Multigene Cancer Testing for Geneticists

**ACMG 2026 dedicated symposium on the clinical-lab translation of population-scale CHIP and mosaicism findings into multigene hereditary-cancer panel testing — incidental-finding handling, reporting thresholds, and germline-vs-clonal disambiguation.**

- **Speaker / institution:** Symposium panel — clinical-lab CHIP working-group representatives, Bick-aligned and Natarajan-aligned investigator pool, hereditary-cancer panel lab medical directors (Ambry / GeneDx / Color / Invitae-successor labs); specific speaker slate TBC from GIM supplement
- **Anchor type:** methods + clinical
- **Day / session:** Mid-meeting symposium (Day 3–4, Mar 12–13, 2026); exact slot TBD
- **Status:** post-meeting; from ACMG meeting site featured-session listing; speaker slate and concrete reporting recommendations TBD pending GIM supplement and Digital Edition

## Headline finding

Multigene cancer panels run on **blood DNA** routinely surface variants in genes (DNMT3A, TET2, ASXL1, TP53, PPM1D, CHEK2, JAK2, ATM, others) at **non-germline variant allele fractions** — clonal hematopoiesis of indeterminate potential (CHIP) — alongside post-zygotic mosaic variants that are biologically distinct from CHIP but operationally hard to distinguish in a clinical lab. The symposium frames the **reporting decision tree**: when is a sub-50% VAF call CHIP (don't report as germline), when is it post-zygotic mosaicism (report with caveat), and when is it germline-with-allelic-imbalance. Cohort numerics from contributing labs (CHIP detection rates in hereditary-cancer panel submissions, age-stratified prevalence, downstream MN-risk follow-up) TBD pending supplement.

## Methodology / framework

Operational framework combining: (1) VAF distribution analysis with tissue-comparator (buccal / fibroblast / skin) when available; (2) gene-list stratification (canonical CHIP drivers vs hereditary-cancer-syndrome genes with CHIP overlap, particularly TP53, CHEK2, ATM); (3) deeper sequencing of borderline VAFs; (4) longitudinal resampling for suspected clonal expansion. ACMG/AMP framework adaptation: PM6 / PS2 cannot apply to clonal events; PM2 / BS1 frequency thresholds need clonal-event-aware modification.

## Lab-translation deep dive

**Validation requirements.** Disambiguating CHIP from post-zygotic mosaicism vs germline-with-allelic-imbalance requires the lab to validate (a) VAF accuracy at low fractions (10–40%) with replicate variance characterized, (b) sensitivity of variant callers at sub-50% VAF on hereditary-cancer-panel coverage depths (typically 300–500x), and (c) a tissue-comparator workflow (buccal swab, cultured fibroblast, or skin punch) with its own end-to-end validation. Many existing hereditary-cancer panels were validated only for germline (~50% / ~100% VAF expectations) — extension to clonal calls is a net-new analytical-validation event.

**Lab-stack changes.** Operational additions: reflex tissue-comparator collection workflow (logistics + consent), deeper sequencing for borderline VAFs, longitudinal resampling at defined intervals (6–12 months) for suspected clonal expansion, and pipeline-level flags that block germline-style reporting on canonical CHIP-driver variants (DNMT3A, TET2, ASXL1, PPM1D, JAK2). LIMS schema needs a clonal-status field per variant.

**Regulatory / insurance.** No CAP-checklist requirement specific to CHIP disambiguation as of 2026 (TBD pending symposium recommendations and ACMG Practice Resources). Payer coverage for reflex tissue-comparator testing is patchwork — typically billed against the hereditary-cancer-panel CPT code rather than separately. Insurance implications of incidental CHIP reporting (life / long-term-care underwriting) are an emerging ELSI question.

**Variant curation.** ACMG/AMP framework modifications required: PM6 / PS2 (de novo) cannot apply to clonal events; PM2 / BS1 (population frequency) needs clonal-event-aware thresholds; functional-evidence interpretation (PS3 / BS3) must consider clonal-selection bias. Gene-specific guidance for TP53 / CHEK2 / ATM (overlap genes) is the highest-leverage curation deliverable from this symposium.

## Where it fits in the corpus

- **ASH 2026:** clinical sequelae — CHIP → CCUS → MDS / AML progression; same investigator pool with the outcomes framing
- **ASHG 2026:** population-scale CHIP statistical-genetics talks (Bick / Natarajan / Jaiswal-aligned)
- **AACR 2026:** germline-somatic integration and therapy-related MN sessions inherit the CHIP-disambiguation framing
- **ASCO 2026:** therapy-related MN risk in cancer survivors with CHIP at baseline

## Open questions

- Should clinical hereditary-cancer-panel reports include a CHIP-status section as standard?
- TP53 / CHEK2 sub-50% VAF: germline-mosaic vs CHIP — what tissue panel does a lab actually run?
- Patient counseling for incidental CHIP — who owns the longitudinal MN-risk follow-up?

## Sources

- [ACMG 2026 meeting site](https://www.acmgmeeting.net/)
- GIM abstract supplement: pending (~April–May 2026)
- ACMG Digital Edition: [acmgeducation.net](https://www.acmgeducation.net/)
- Related: [hereditary-cancer-adult-genetics.md](./hereditary-cancer-adult-genetics.md), [llm-acmg-amp-reproducibility.md](./llm-acmg-amp-reproducibility.md)
