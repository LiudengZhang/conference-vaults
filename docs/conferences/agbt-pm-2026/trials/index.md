# Per-program dossiers — AGBT Precision Health 2026

One page per clinical study, biobank initiative, real-world implementation program, or precision-therapeutic case presented at AGBT-PM 2026. Because AGBT-PM abstracts are closed (attendee-only), the per-program template — not per-talk — is the natural unit, with each dossier reconstructed from public coverage of the speaker's program rather than the talk itself.

> **Status:** Pre-meeting scaffold (T-4 months as of May 11, 2026). The index below will be populated after the September 14–16, 2026 meeting from confirmed speaker affiliations + their public program output. Pre-meeting, this page documents the **template** and the **anticipated dossier candidates** based on the 15 confirmed speakers.

## Per-program template

Each dossier follows this shape:

```
# <Program / Trial / Initiative name> — <PI / institution>

- Presenter / session / date at AGBT-PM 2026
- Program type: rare-disease dx | MRD trial | population biobank | gene-therapy n=1 | implementation | pharmacogenomics
- Cohort size / current enrollment / endpoints
- Key reported findings (with source citation — vendor PR, society PR, preprint, peer-reviewed paper, podcast)
- Platform / assay used (cross-link to AGBT 2026 launch dossier if applicable)
- Clinical-implementation status: research-only | LDT | FDA-cleared | reimbursed | guideline-recommended
- Reception / competitive context (Guardant vs Natera vs Personalis vs Foundation, etc.)
- Cross-links: AACR / ASCO / ESMO / SITC / ASHG sibling read-outs; AGBT GM platform vendor
```

Every clinical claim ends with a citation. Distinguish **interim** vs **mature** read-outs. Note **n** explicitly.

## Anticipated dossier candidates (pre-meeting forecast)

Built from the 15 confirmed speakers' affiliations and recent public output. **Not yet populated** — these are scaffold slots to be filled after the meeting.

### Rare-disease genomic diagnostics

| Anticipated program | PI / institution | Source for forecast |
|---|---|---|
| **GREGoR Consortium** — diagnostic-odyssey rare-disease cohort | Heidi Rehm (Broad), with multi-site network | [NIH GREGoR](https://gregorconsortium.org/) |
| **BabySeq / Rapid-WGS in NICU** | Monica Wojcik (Boston Children's) | Recurring AGBT-PM thread; multiple peer-reviewed cohorts |
| **Penn Rare Disease Program** | Theodore Drivas (Penn) | Recurring Penn medical-genomics implementation |
| **Long-read clinical sequencing for rare disease** | Andrew Stergachis (UW) | [Stergachis Lab](https://stergachislab.com/) — Fiber-seq / phased clinical assemblies |
| **Broad clinical sequencing platform** | Niall Lennon (Broad) | Broad Clinical Labs throughput / case mix |

### AI in clinical genomics

| Anticipated program | PI / institution | Source for forecast |
|---|---|---|
| **DL for variant interpretation / functional genomics** | Alexis Battle (JHU) | Recurring AGBT-PM speaker on QTL / DL methods |
| **Foundation models for genomic medicine** | Sara Mostafavi (UW / Allen) | Recent enformer / genomic-LLM work |
| **eMERGE network — clinical-decision support** | Marylyn Ritchie (MUSC) | eMERGE phase IV implementation reports |

### Precision therapeutics & gene editing

| Anticipated program | PI / institution | Source for forecast |
|---|---|---|
| **In-vivo CRISPR for monogenic disease** | Kiran Musunuru (Penn) | VERVE-101 / individualized base-editing for FH program |
| **Custom CRISPR therapeutics platform** | Fyodor Urnov (IGI Berkeley) | n=1 / ultra-rare editing therapeutic pipeline |

### Population genomics & biobanks

| Anticipated program | PI / institution | Source for forecast |
|---|---|---|
| **Regeneron Genetics Center — exome+** | Gonçalo Abecasis (Regeneron) | Recurring; latest WES/WGS cohort updates |
| **UK Genomic Medicine Service / Oxford** | Jenny Taylor (Oxford) | Genomics England 100K → NHS GMS transition |
| **NIH All of Us research workbench** | (TBD — All of Us workshop in past years) | [All of Us AGBT-PM 2025 workshop](https://allofus.nih.gov/article/applied-genomics-and-biological-technologies-agbt-precision-health-meeting-workshop-leveraging-all-us-researcher-workbench-advance-precision-health) |

### Newborn / prenatal precision sequencing

| Anticipated program | PI / institution | Source for forecast |
|---|---|---|
| **NICHD prenatal sequencing** | Diana Bianchi (NICHD) | NICHD director, prenatal-sequencing portfolio |
| **Newborn WGS pilots** | Monica Wojcik (Boston Children's) | BabySeq2, NewbornsInSC, GUARDIAN comparisons |

### Vendor / industry tracks (expected, not yet sourced to confirmed speaker)

- **Guardant** — Reveal MRD + Shield colorectal screening real-world performance (likely vendor-track)
- **Natera** — Signatera MRD across indications (likely vendor-track)
- **Personalis** — NeXT Personal Dx ultra-sensitive MRD (likely vendor-track)
- **Foundation Medicine / Tempus / Caris** — comprehensive genomic profiling implementation
- **Illumina / Element / Roche / Ultima** — clinical-throughput claims tied to [AGBT GM 2026 launches](../../agbt-2026/launches/index.md)

## Confirmed dossiers

> *None yet — meeting is T-4 months out. Per-program dossiers will be added during and after the meeting from public coverage of each confirmed speaker's program.*

## How to add a dossier

1. Create `trials/<pi-or-program-slug>.md` (e.g. `trials/wojcik-babyseq.md`, `trials/regeneron-genetics-center.md`).
2. Follow the per-program template above.
3. Every clinical figure (cohort n, sensitivity/specificity, PPV/NPV, OS/PFS, diagnostic yield) must end with a citation to a peer-reviewed paper, preprint, society press release, or vendor PR — never reconstruct from a tweet alone.
4. Cross-link to:
   - **Upstream platform** in [`../../agbt-2026/launches/`](../../agbt-2026/launches/index.md) if the program uses an AGBT-GM-launched instrument.
   - **Sibling read-outs** at [AACR 2026](../../aacr-2026/index.md), [ASCO 2026](../../asco-2026/index.md), [ESMO 2026](../../esmo-2026/index.md), [SITC 2026](../../sitc-2026/index.md), [ASHG 2026](../../ashg-2026/index.md).
   - **Tool / pipeline** dossiers in [EuroBioC 2025](../../eurobioc-2025/index.md) / [GBCC 2025](../../gbcc-2025/index.md) / [Nextflow 2026](../../nextflow-2026/index.md) when the program is built on a publicly named workflow.
5. Flag any vendor figure that lacks third-party validation as **(vendor PR — no independent validation)**.

## Caveats specific to AGBT-PM dossiers

- **Clinical implementation programs evolve faster than the conference cycle.** A "real-world implementation" presented in September 2026 reflects data cut some months earlier. Note the data-cut date when known.
- **Patient privacy.** Storytelling sessions and rare-disease case reports often include patient-family voices; do not reconstruct any patient-identifying detail beyond what the program has publicly released.
- **Vendor MRD claims are routinely PR-distorted.** Each MRD vendor (Natera, Guardant, Personalis) has different limit-of-detection, longitudinal cadence, and indication-specific evidence. Compare to a common ASCO/ESMO endpoint (DFS, MRD-detection lead time) rather than vendor's preferred metric.
- **GREGoR diagnostic-yield numbers** vary substantially by recruitment criteria (prior-WES-negative vs unselected, prior-WGS-negative vs WES-naive). Always include cohort selection in the dossier.
