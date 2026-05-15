# Trials — SITC 2026

One of two primary artifacts in this vault: **one Markdown file per drug or cell-therapy readout**. SITC 2026 reads out a heavy block of early- and mid-phase IO trials — CAR-T (autologous + allogeneic + in vivo), TIL, TCR-T, NK-cell, bispecifics, neoantigen vaccines, and checkpoint-resistance combos. Each gets a `trials/<slug>.md` entry. The methods / immune-profiling side lives in [`tools/`](../tools/index.md).

> **Status:** Template + master index. Per-trial pages will be populated as the SITC program is announced (program-at-a-glance typically posts in September; full abstracts via JITC supplement in October; presentation embargoes lift on the morning of the talk). Pre-meeting stubs flagged `*expected, subject to embargo*` are sourced from sponsor toplines, JPM 2026 / AACR 2026 / ASCO 2026 framing, and analyst preview pieces; numbers can shift on the actual abstract reveal.

## Per-trial template

Each trial file (e.g., `obe-cel-r2-all.md`, `bnt122-melanoma.md`) follows this schema. Copy and fill:

```markdown
# <Trial acronym / name> — <Drug regimen / cell-therapy product, indication, line>

> **Abstract:** <JITC abstract #, e.g., 102> · **Session:** <session name, date, time MST, room> · **Embargo:** <presentation date>

## At a glance

- **Sponsor:** <pharma / academic / cooperative group>
- **PI / presenter:** <name, institution>
- **NCT ID:** <NCTxxxxxxxx>
- **Modality:** <autologous CAR-T / allogeneic CAR-T / in vivo CAR-T / TIL / TCR-T / NK cell / bispecific / mRNA neoantigen vaccine / peptide vaccine / checkpoint combo / ADC + IO / immunocytokine>
- **Target / construct:** <CD19 / BCMA / GPRC5D / Claudin18.2 / HLA-A*02 NY-ESO-1 / personalized neoantigen / PD-1×VEGF / etc.>
- **Phase:** <1 / 1b / 2 / 1-2 / 2-3>
- **Design:** <dose-escalation / dose-expansion / randomized / single-arm / basket / platform>
- **N:** <enrolled / treated / analyzed>
- **Primary endpoint(s):** <ORR / CR / PFS / OS / DLT / safety / immunogenicity>
- **Indication:** <tumor type, subtype, biomarker selection (HLA, antigen expression, MSI, TMB)>
- **Line:** <neoadjuvant / adjuvant / 1L / 2L+ / R/R / heavily pretreated>

## Headline result

<One paragraph. ORR, CR rate, duration of response, safety profile if known.
If pre-embargo, mark `*expected per <company> topline <date>*` or
`*pre-embargo per <analyst source>*`.>

## Mechanism / class

<Modality detail: construct architecture for cell therapies (CAR design, costim
domain, edits); target rationale; manufacturing / vein-to-vein time;
neoantigen-selection pipeline for vaccines. Cross-link to related AACR
mechanism sessions where the biology was presented.>

## Biomarker / correlative readout

<This is the SITC-specific field. What immune-profiling assay anchored the
trial? Multiplex IF? scRNA-seq of TILs? TCR repertoire? ctDNA-MRD? Cross-link
to the corresponding `tools/<assay>.md` entry. Many SITC trials present
biomarker correlatives in the same talk as the efficacy numbers.>

## Discussant / session framing

<Session chair + co-presenters, if a themed concurrent session. SITC doesn't
have ASCO-style discussants, but session co-programming is itself a signal.>

## Practice-changing / class-defining?

<Yes / no / pending, with rationale: first-in-class signal, dose decision for
pivotal, BLA path, unmet need, competitive context vs prior cell therapies
or checkpoint baselines.>

## Cross-links

- **AACR 2026:** <related mechanism / TME / biology session>
- **AACR 2025:** <prior-year construct / target work>
- **ASCO 2026:** <if a Ph3 ASCO readout used the same construct / target>
- **JPM 2026:** <sponsor presentation / cell-therapy strategy slide / deal>
- **SITC 2026 tools:** <multiplex IF / TCR / spatial assay used for correlative>
- **Other SITC 2026 trials:** <same modality / target / sponsor>

## Sources

- JITC abstract supplement: <DOI URL or "pending JITC publication">
- Company press release: <URL>
- Trade-press recap: <OncLive / ACIR / Targeted Oncology URL>
- ClinicalTrials.gov: <NCT URL>
```

## Master trial index

Pre-meeting shortlist — to be expanded as the SITC 2026 program-at-a-glance posts (~Sep 2026). All entries below are **anticipated / speculative**, sourced from sponsor pipelines, AACR 2026 echo, JPM 2026 strategy slides, and SITC 2025 program shape. **Treat every row as `*expected, subject to embargo*` until JITC publishes.**

| Modality | Sponsor / lab | Indication | Phase | Target / construct | Anticipated readout | Why it's on the list |
|---|---|---|---|---|---|---|
| **In vivo CAR-T** | Capstan / AstraZeneca | Autoimmune + onc | 1 | CD19 lipid-nanoparticle | First-in-human safety + B-cell depletion kinetics | The in vivo CAR-T thesis — one of SITC 2026's likely headline tracks |
| **Allogeneic CAR-T** | Allogene / Caribou / Cellectis | R/R LBCL / MM | 1/2 | CD19 / BCMA, gene-edited | Updated CR durability, donor-derived persistence | Allogeneic remains the off-the-shelf bet |
| **Solid-tumor CAR-T** | various academic + biotech | GBM, mesothelioma, colorectal | 1 | CLDN18.2, GPC3, GD2, mesothelin | Dose-escalation safety + early response | Solid-tumor CAR-T inflection thesis |
| **TIL therapy** | Iovance | 2L+ melanoma, NSCLC, cervical | 2/3 | TIL (Amtagvi follow-on cohorts) | Real-world durability + NSCLC update | Post-Amtagvi-approval data |
| **TCR-T** | Adaptimmune / TScan / Immatics | Synovial sarcoma, MAGE-A4+ solid | 2 | HLA-A*02 MAGE-A4 / NY-ESO-1 | Durability beyond afami-cel approval | TCR-T solid-tumor thesis |
| **Bispecific (T-cell engager)** | Janssen / Pfizer / Roche / IGM | MM, DLBCL, solid (incl Claudin18.2) | 1/2 | BCMA×CD3, CD20×CD3, CLDN18.2×CD3 | Updated ORR + step-up dosing safety | Bispecific class durability in heme + GI |
| **PD-1 × VEGF bispecific** | Summit / Akeso / BMS / AbbVie | NSCLC, CRC, HCC | 1b/2 | PD-1×VEGF (ivonescimab and follow-ons) | Mechanism-of-action correlative data | Class follow-through from HARMONi-6 ASCO Plenary |
| **NK-engager** | Affimed / Sanofi / Cytovia | R/R LBCL, AML | 1/2 | CD16A×CD30, CD16A×BCMA | Updated CR + persistence | NK platform reset post-Sanofi deal |
| **Personalized mRNA neoantigen vaccine** | Moderna / Merck | Adjuvant melanoma, NSCLC, RCC | 2/3 | mRNA-4157 (V940) + pembro | Updated RFS, immunogenicity correlative | The neoantigen-vaccine signal — top of mind for Wu Smalley lecture |
| **Personalized mRNA neoantigen vaccine** | BioNTech / Genentech | Pancreatic adjuvant, CRC | 1/2 | BNT122 (autogene cevumeran) + chemo / atezo | Updated RFS, T-cell expansion | The DFCI / MSK pancreatic vaccine thread |
| **Shared-antigen peptide vaccine** | Gritstone / Nouscom / EpiVax | Adjuvant CRC, MSS CRC, lung | 1/2 | KRAS-mut shared neoantigens | T-cell response + recurrence signal | Shared-neoantigen platform comparison |
| **Checkpoint × LAG-3** | BMS / Regeneron / Macrogenics | Melanoma 1L combos | 2/3 | Relatlimab + nivo follow-ons; novel LAG-3 | Updated mPFS, biomarker-defined subsets | LAG-3 class status |
| **Checkpoint × TIGIT** | Roche / iTeos / Gilead | NSCLC, GI subsets | 2 | Tiragolumab / EOS-448 + checkpoint | Subset rescue post-Skyscraper failure | TIGIT class status |
| **Microbiome × IO** | Vedanta / Seres / Finch / academic | Melanoma + RCC checkpoint-refractory | 1/2 | Defined consortium, FMT | Response rate after FMT or VE303-class | Microbiome × IO maturation (Wargo continued) |
| **ADC × IO combo** | Pfizer / Gilead / Daiichi | mUC, TNBC, HER2+ GC | 1b/2 | EV+pembro, Trop2-ADC+IO, T-DXd+IO | Safety + ORR uplift | ADC×IO combo durability |
| **Immunocytokine** | Philogen / Mural / Asher Bio | Melanoma, RCC, NSCLC | 1/2 | IL-2v-targeted, IL-12-tumor-localized | Tolerability + intratumoral T-cell expansion | Cytokine-engineering revival |

**Additional candidates** to stub once the program lists land:

- **CAR-NK** updates (NKARTA, ImmunityBio, Wugen, Affimed)
- **Engineered Tregs** (early-phase IO and autoimmune crossover)
- **In vivo gene-edited cell therapy** — beyond Capstan; competitive set
- **Checkpoint combos in MSS CRC** — long-standing unmet need cohort
- **Brain-tumor IO** — GBM cell therapy, neoadjuvant IO in glioma
- **HPV-driven cancer vaccines + checkpoint** — head & neck, cervical

## Cross-cutting themes (for post-meeting `themes.md`)

To synthesize across `trials/` once populated:

1. **Solid-tumor CAR-T inflection.** Whether GBM, GI, and mesothelioma CAR-T cohorts cross the response threshold that justifies pivotal trials.
2. **In vivo CAR-T arrives.** Capstan / Umoja / Orna / Outpace LNP-delivered constructs — first-in-human safety + B-cell kinetics will define a new modality.
3. **Neoantigen-vaccine signal hardens (or doesn't).** Moderna mRNA-4157 RFS update + BioNTech BNT122 pancreatic + Gritstone shared-antigen CRC. Wu Smalley lecture frames the field.
4. **Bispecific durability and resistance.** BCMA × CD3 and CD20 × CD3 long-term follow-up — antigen escape, T-cell exhaustion, sequencing vs CAR-T.
5. **LAG-3 / TIGIT class status.** Post-Skyscraper TIGIT cohorts and LAG-3 expansion data — which checkpoint partner survives.
6. **Microbiome × IO matures.** Defined-consortium and FMT data in checkpoint-refractory melanoma + RCC, the through-line from Wargo's SITC 2025 keynote.
7. **PD-1 × VEGF bispecific class.** Mechanism-of-action correlatives following HARMONi-6 OS readout at ASCO Plenary.
