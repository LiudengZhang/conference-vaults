# Demystifying Base LLM Reproducibility and Accuracy in ACMG/AMP Variant Classification

**Platform benchmark of base (non-fine-tuned) large language models against the ACMG/AMP 2015 variant-classification framework — testing reproducibility, accuracy, and per-evidence-code drift across reruns and across models.**

- **Speaker / institution:** Platform speaker TBC from GIM abstract supplement; submission tracks to AI / Informatics track
- **Anchor type:** tool / methods
- **Day / session:** Day 3–5 (Mar 12–14, 2026), AI / Informatics platform session (specific slot TBD)
- **Status:** post-meeting; from ACMG meeting site session listing; per-model accuracy numbers, dataset composition, and authorship TBD pending GIM supplement and Digital Edition recording

## Headline finding

First systematic clinical-lab benchmark of **base** (off-the-shelf, non-fine-tuned) LLMs — including GPT, Claude, Gemini-class models — on the ACMG/AMP 2015 five-tier variant-classification task (Pathogenic / Likely Pathogenic / VUS / Likely Benign / Benign). The talk is positioned as a **reproducibility** study: how stable is the same model's output across repeated runs on the same variant, and how concordant are different models on the same evidence inputs? Quantitative concordance rates, per-evidence-code (PVS1, PS1–4, PM1–6, PP1–5, BA1, BS1–4, BP1–7) accuracy, and final classification agreement against ClinVar 2-star+ ground truth TBD pending supplement.

## Methodology / framework

Benchmark design likely: curated test set of variants with established ClinVar expert-panel classifications (ClinGen VCEPs as gold standard); LLM prompted to apply ACMG/AMP 2015 rules to a structured evidence package; multiple reruns per variant to measure intra-model reproducibility; cross-model comparison for inter-model concordance. Distinguishes **evidence-code assignment accuracy** from **final tier assignment accuracy** — a model can hit the right tier with the wrong evidence stack. Critical comparison to existing classification aids (Franklin, VarSome, InterVar, CardioBoost, BayesDel as PP3 proxy).

## Lab-translation deep dive

**Validation requirements.** A base LLM that participates in any classification decision triggers CLIA-style analytical validation: stability of output across reruns (intra-run reproducibility), stability across model versions (vendor silently rotates model weights — a load-bearing validation hazard), and accuracy against ClinVar 2-star+ / VCEP-curated ground truth stratified by gene, evidence-code mix, and variant rarity. The reproducibility framing of the talk is precisely the failure mode CLIA requires labs to characterize before clinical use. Concordance floors and stability windows TBD pending GIM supplement.

**Lab-stack changes.** Most clinical hereditary-cancer labs already run rule-based classifiers (Franklin, VarSome, InterVar) under a curator-in-the-loop model. Inserting an LLM means: (a) prompt-engineering as a versioned, change-controlled lab document; (b) input-evidence package construction as its own validated module (PubMed search, population-frequency lookup, functional-evidence retrieval, splice-prediction summary); (c) audit-trail logging of every prompt + response per variant; (d) periodic re-validation when the underlying model is updated. RAG-with-ClinGen and fine-tuning shift more validation burden onto the lab.

**Regulatory / insurance.** FDA has signaled (via the LDT final rule and AI/ML guidance) that AI-augmented classification is in-scope as a clinical decision support tool. CAP MIN-checklist updates anticipated for AI-augmented variant curation. Payer impact is indirect — reclassification of historical VUS triggers re-billing and re-counseling pathways.

**Variant curation.** Highest-value role is likely **VUS-triage assist** (auto-summarize literature, propose evidence codes, flag candidate reclassifications) with mandatory human sign-out, rather than autonomous classification. Liability and CLIA framing currently preclude autonomous LLM classification.

## Where it fits in the corpus

- **AACR 2026:** every cancer-variant classification in hereditary-cancer panels rests on this framework; LLM-assisted curation feeds AACR cohort-classification posters downstream
- **ASHG 2026:** foundation-model variant-effect predictor talks (AlphaMissense follow-ons, ESM, EVO); sibling methods framing
- **ISMB 2026 / RECOMB 2026:** upstream methods venue for LLM-as-variant-classifier benchmarks
- Related ACMG 2026: [acmg-sf-v33-secondary-findings.md](./acmg-sf-v33-secondary-findings.md), [hereditary-cancer-adult-genetics.md](./hereditary-cancer-adult-genetics.md)

## Open questions

- Is base-model performance adequate for any clinical-lab role, or is fine-tuning / RAG-with-ClinGen mandatory?
- How does LLM accuracy degrade on rare / novel variants (the cases where automation matters most)?
- Liability and CLIA/CAP framing — can a base LLM be part of a regulated lab workflow at all?

## Sources

- [ACMG 2026 meeting site](https://www.acmgmeeting.net/)
- GIM abstract: pending supplement publication (~April–May 2026)
- ACMG Digital Edition recording: [acmgeducation.net](https://www.acmgeducation.net/)
- Anticipated trade-press recap: GenomeWeb / 360Dx
