# mcPCR — Syndex Bio

**Syndex Bio's mcPCR ("methyl-copying PCR") co-amplifies DNA sequence and methylation in a single reaction, sidestepping the bisulfite-conversion damage that has constrained methylation sequencing since the 1990s.**

## At a glance

- **Vendor / launch date / availability:** Syndex Bio; profiled at AGBT 2026 (Marco Island, Feb 22–25); roadmap (not commercially shipping at AGBT) *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Chemistry / modality:** Methyl-copying PCR — single-reaction co-amplification of DNA sequence and methylation state, preserving methyl-mark information through amplification without bisulfite or enzymatic conversion *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Throughput (PR):** **TBD** — reactions/run and amplicons/reaction not enumerated in public AGBT 2026 coverage.
- **Read length:** n/a (mcPCR is a library-prep / amplification chemistry; read length is set by downstream sequencer choice).
- **Accuracy (PR):** **TBD** — no per-CpG methylation-call accuracy, no conversion-efficiency-equivalent metric, no comparison to bisulfite / EM-seq / TAPS in public AGBT coverage.
- **List price / cost-per-sample:** **TBD** — roadmap-status reagent kit, no pricing surfaced.

> **Source caveat:** AGBT 2026 public coverage of Syndex Bio is limited to the [GEN recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) inclusion. All quantitative fields are flagged **TBD**; **(vendor PR — no independent benchmark)** applies to all spec claims.

## What's new vs prior generation

Methylation sequencing has historically required converting DNA before sequencing — bisulfite (Frommer 1992) degrades 90%+ of input, EM-seq (NEB) and TAPS (Cambridge Epigenetix) reduce damage but still require a chemical/enzymatic conversion step. mcPCR's pitch is to preserve methyl marks *through* amplification rather than reading them off a converted template, which would:

- Reduce input requirements (relevant for liquid-biopsy cfDNA workflows where input is the binding constraint).
- Preserve sequence context (no C→T conversion ambiguity).
- Co-amplify sequence + methylation in one reaction (vs running parallel WGS + WGBS libraries).

The strategic positioning is liquid-biopsy methylation panels and cancer early-detection cfDNA workflows.

## Headline benchmarks

> **TBD** — no published demonstration cohort, no comparison to bisulfite/EM-seq/TAPS on standard methylation benchmarks (e.g. SEQC2 reference, NIST methylation standards) indexed at time of writing.

## Reception / competitive context

mcPCR enters a crowded methylation-prep landscape (bisulfite kits, NEB EM-seq, Cambridge Epigenetix TAPS, Illumina Infinium arrays for targeted methylation). Differentiation is on the *amplification* step rather than the conversion step — if mcPCR genuinely preserves methylation through PCR cycles, it would slot upstream of any methylation-aware sequencer and downstream methylation analysis stack. The natural commercial use case is cfDNA liquid biopsy where low input + multiplexed methylation + sequence calls in one reaction has obvious appeal for early-detection assays (Grail Galleri-class).

## Cross-links

- **Downstream methylation analysis tools (Bioconductor):**
  - [bsseq (GBCC 2025)](../../gbcc-2025/index.md) — methylation analysis on bisulfite-converted data; would need an mcPCR-aware import path if the chemistry ships.
  - [decemedip (EuroBioC 2025)](../../eurobioc-2025/index.md) — methylation deconvolution; downstream of any methylation chemistry including mcPCR.
  - [methylKit](https://bioconductor.org/packages/methylKit/) — general methylation differential analysis.
- **AACR axis — methylation / liquid biopsy:** mcPCR is too new for AACR 2026 *data* posters; expect first methods abstracts at AACR 2027 if Syndex ships in 2026. Methylation cfDNA early-detection is one of the most-watched AACR axes (Grail, Exact Sciences, Freenome) and mcPCR's pitch lands squarely in that segment.
- **AGBT 2026 lineage:** Syndex Bio is profiled alongside Codetta, Cellanome, and Volta in the [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) as part of the "emerging platforms" sweep.

## Sources

- [GEN — AGBT 2026 Recap: NGS Big Bets and Spatial's Rising Momentum](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) — Feb–Mar 2026 (Syndex Bio listed in emerging-platforms recap; specifics not enumerated).
- [AGBT 2026 program-notes vendor index](../program-notes.md) — Syndex Bio entry under "Vendor PR coverage indexed by company".

> **Open items:** locate a primary Syndex Bio press release or methods preprint enumerating mcPCR's conversion-free chemistry, methylation-call accuracy, and benchmark against bisulfite/EM-seq. Backfill spec table when a primary source is reachable.
