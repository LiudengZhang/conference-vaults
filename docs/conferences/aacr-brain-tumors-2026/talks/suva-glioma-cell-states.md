# Mario Suva keynote — glioma cell states, lineage, and therapeutic implications

**Plenary keynote anchoring the single-cell cell-state framework (AC-/MES-/OPC-/NPC-like) that underpins much of the rest of the Brain 26 program.**

- **Speaker(s):** Mario L. Suva, MD, PhD (also Brain 26 co-chair)
- **Affiliation:** Harvard Medical School / Broad Institute / Massachusetts General Hospital
- **Anchor type:** study (mechanism / biology keynote)
- **Day / session:** Day 1 plenary (Mon Mar 23, 2026)
- **Status:** post-meeting; details captured from AACR Brain 26 program notes, the chair-disclosed keynote topic, and the Suva-lab published corpus (Patel/Suva Science 2014; Tirosh/Suva Nature 2016; Neftel/Suva Cell 2019; subsequent perturb-seq and lineage-tracing work); specific Brain 26 dataset specifics TBD pending abstract supplement and any accompanying paper

## Headline finding

Plenary synthesis of the glioma cell-state framework: AC-like (astrocyte-like), MES-like (mesenchymal-like), OPC-like (oligodendrocyte-precursor-like), and NPC-like (neural-progenitor-like) states defined by single-cell RNA-seq across primary and recurrent glioma, plus new perturbation / lineage-tracing data showing how these states interconvert under therapy. The 2026 update integrates spatial transcriptomics, clinically-paired (pre/post-treatment) specimens, and perturbation-derived state transitions. Specific datasets and new state-transition rules from the keynote TBD pending the supplement.

## Mechanism / methodology

Single-cell and single-nucleus RNA-seq of fresh tumor and matched recurrence specimens, framed by the Neftel et al. four-state model; layered on top: spatial transcriptomics (Visium HD / Xenium-class), CRISPR perturb-seq to map state-determining transcription factors, and lineage-tracing (DNA barcoding) to test whether the same clone can occupy multiple states. The framework explicitly connects to developmental neural lineages, and integrates microenvironmental context (hypoxia, TAM proximity, neural-circuit input) as state-biasing signals.

## Mechanism / methodology deep dive

**Underlying biology.** The Neftel/Suva four-state framework holds that malignant glioma cells occupy a continuum bounded by four developmentally-informed transcriptional states — AC-like (astrocyte-lineage, e.g., GFAP, AQP4), MES-like (mesenchymal / wound-healing, e.g., CD44, CHI3L1), OPC-like (oligodendrocyte-precursor, e.g., OLIG1/2, PDGFRA), and NPC-like (neural-progenitor, e.g., DLL3, SOX11) — biased toward specific states by recurrent genetic drivers (EGFR → AC; NF1 → MES; PDGFRA → OPC; CDK4 → NPC) and by TME inputs (hypoxia / necrosis → MES; neural-circuit input → NPC/OPC).

**Therapeutic design.** Not a therapeutic per se, but a target-selection framework: dictates which surface antigens (IL-13Rα2 enriched in MES; EGFR/EGFRvIII enriched in AC/OPC; GD2 enriched in OPC/NPC; DLL3 in NPC) are tractable and where antigen-loss escape will land. Perturb-seq screens nominate state-master TFs (e.g., NFIA/B for AC; CEBPB/FOSL for MES; ASCL1/OLIG2 for OPC/NPC) as state-stabilizing or state-locking pharmacological nodes.

**Resistance / failure modes.** Plasticity itself is the resistance mechanism: therapy (RT, TMZ, IDH-i, CAR-T) reproducibly shifts cell-state distribution toward MES-like / stem-like programs, mediating recurrence without classical genetic resistance.

**Translational gaps.** Whether state transitions can be pharmacologically blocked (rather than just observed) is unproven; the framework was built on adult IDH-wt GBM and its fit for pediatric DMG and IDH-mut glioma is still being calibrated.

## Where it fits in the corpus

- **AACR 2026:** Suva is a chair / speaker on the Annual single-cell / spatial-omics topic four weeks later; this keynote sets up that thread.
- **SITC 2026:** cell-state-directed CAR-T target selection — the link from atlas biology to therapeutic engineering.
- Related Brain 26 entries: `parrinello-injury-programs.md`, `monje-gd2-cart-dipg.md`, `neuroscience-of-gliomas-tam.md`, `vorasidenib-post-indigo.md`.

## Open questions

- Which state transitions are deterministically therapy-induced (TMZ, RT, IDH-i, CAR-T) versus stochastic, and which can be blocked pharmacologically?
- How tightly does the AC/MES/OPC/NPC-like framework hold for pediatric DMG / DIPG and IDH-mutant glioma — both have lineage features the adult-GBM framework wasn't built around.
