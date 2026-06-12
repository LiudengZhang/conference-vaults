# Single Cell Genomics Day 2026 (SCGD26)

**The Satija Lab's annual one-day, free, virtual single-cell meeting — captured this year from a full livestream transcript.** Single Cell Genomics Day (SCGD) is hosted by the **Satija Lab at the New York Genome Center (NYGC)**, runs as a single-track day of keynotes + talks, and is streamed live on YouTube with global virtual attendance. **Rahul Satija** MCs and runs the live Q&A.

- **Event:** Single Cell Genomics Day 2026 — "keynote talks and AI in biology"
- **Date:** June 12, 2026 (one day)
- **Host:** Satija Lab / New York Genome Center
- **Format:** Free virtual livestream (YouTube) + live/written Q&A
- **Site:** [satijalab.org/scgd26](https://satijalab.org/scgd26/)

> **Status: ✅ built from transcript, speakers verified.** Unlike most of the corpus (pre-meeting scaffolds), this vault is populated from an **actual session transcript of the SCGD26 livestream** — nine talks including three keynotes. Content is extracted from what speakers said on the day; all nine speaker names, affiliations, talk titles, and (where they exist) preprints/DOIs/Addgene IDs were then cross-checked against the [official SCGD26 schedule](https://satijalab.org/scgd26/) and published sources — see the **Sources** section on each talk page. A few residual items (archived video link, a handful of lab-member name spellings) remain open and are flagged below.

## Brand disambiguation (read this first)

**SCGD is *not* the same meeting as the [`single-cell-genomics-2026/`](../single-cell-genomics-2026/) vault.** That vault is a compound scaffold for the two 2026 *academic-society* flagships — the **GRC Single-Cell Genomics** (Les Diablerets, May 10–15, off-the-record) and the **Wellcome Single Cell Biology** (Hinxton, Jun 10–12). **Single Cell Genomics *Day*** is a separate, distinct event: a free one-day NYGC livestream organized by Rahul Satija's group, running annually since the mid-2010s. Same sub-discipline, different meeting, different organizers, different format (fully public + recorded, vs. GRC's closed-door rule). The two vaults are siblings and cross-link, but should not be merged.

## Why this is in the vault

- **Real delivered-talk content, not a scaffold.** This is one of the few corpus entries built from a verbatim transcript. It gives ground-truth previews of methods that will be cited at AACR 2027 and that overlap heavily with the AACR 2026 single-cell + spatial and virtual-cells topics.
- **Dense AACR-axis fit.** The day spans molecular recorders, in vivo Perturb-seq at whole-brain scale, single-cell genotyping, sequencing-based connectomics, sequence-to-function foundation models, the "virtual cell / lab-in-the-loop" program, and ultra-scalable combinatorial-indexing methods — direct overlap with [`aacr-2026/topics/single-cell-spatial-omics/`](../aacr-2026/topics/single-cell-spatial-omics/) and [`aacr-2026/topics/virtual-cells/`](../aacr-2026/topics/virtual-cells/).
- **The "AI in biology" turn, stated explicitly.** Two of the three keynotes (Regev, and the Kundaje methods talk) are squarely about sequence/expression foundation models, interpretability, and using models to *design* experiments rather than just predict — the same thread the AACR virtual-cells and agentic-AI dossiers track.

## Program (Jun 12, 2026) — as delivered

Single track. Order below is the order of delivery on the livestream. Keynotes marked **★**.

| # | Speaker | Affiliation | Talk / method | Page |
|---|---|---|---|---|
| 1 | **Dingchang Lin** | Johns Hopkins (David Baker Lab collab) | **GEMINI** — genetically encoded protein-assembly molecular recorder | [molecular-recorder-gemini](talks/molecular-recorder-gemini.md) |
| 2 ★ | **Xin Jin** | Scripps Research | In vivo Perturb-seq → whole-brain genome-scale CRISPR screen | [xin-jin-in-vivo-perturbseq](talks/xin-jin-in-vivo-perturbseq.md) |
| 3 | **Sydney B. Blattman** | MSKCC (Pe'er / Chaligné / LaReau labs) | **GIFT** — Genotyping In Fixed Transcriptomes | [sydney-blattman-gift](talks/sydney-blattman-gift.md) |
| 4 | **Amanda Urke** | Macosko Lab, Broad / Harvard | **Synapse-seq** — sequencing-based synaptic connectomics | [amanda-urke-synapseseq](talks/amanda-urke-synapseseq.md) |
| 5 | **Anshul Kundaje** | Stanford | **ChromBPNet** + fibroblast reprogramming dynamics | [anshul-kundaje-chrombpnet](talks/anshul-kundaje-chrombpnet.md) |
| 6 ★ | **Aviv Regev** | Genentech | "From Cell Atlases to Medicines, with AI" — virtual cell / lab-in-the-loop | [aviv-regev-virtual-cell](talks/aviv-regev-virtual-cell.md) |
| 7 | **Alexandra (Alex) Bradu** | Satija Lab, NYGC | **VIPerturb-seq** + the **GuEST-List** library | [alex-vip-perturbseq](talks/alex-vip-perturbseq.md) |
| 8 | **Kevin (Yu-Kai) Chao** | Harvard / Fei Chen Lab, Broad | **TimeVault** — vault-protein transcriptome recorder | [kevin-chao-timevault](talks/kevin-chao-timevault.md) |
| 9 ★ | **Junyue Cao** | Rockefeller University | Scalable combinatorial-indexing single-cell + temporal/spatial | [junyue-cao-scalable-singlecell](talks/junyue-cao-scalable-singlecell.md) |

See [`talks/`](talks/index.md) for the per-talk index.

## What we have to work with

| Source | Coverage | Notes |
|---|---|---|
| **SCGD26 livestream transcript** | all 9 talks + Q&A (two contiguous segments) | primary artifact — content extracted into per-talk pages |
| **satijalab.org/scgd26** | event page, schedule, registration | [link](https://satijalab.org/scgd26/) |
| **YouTube livestream / chat** | recording + audience Q&A (speakers answered some questions in chat after sign-off) | check the Satija Lab / NYGC YouTube channel for the archived stream |
| **Speaker preprints / papers** | confirmed for most talks — GIFT (bioRxiv), Synapse-seq (bioRxiv), VIPerturb-seq (bioRxiv + GuEST-List on Addgene), TimeVault (*Science* 2026 + Addgene), ChromBPNet reprogramming (*Nature Genetics* / interactive browser), whole-brain Perturb-seq atlas (Hugging Face) | DOIs/links on each talk page's **Sources** section |

## Cross-vault targets

- [`single-cell-genomics-2026/`](../single-cell-genomics-2026/) — sibling academic-society vault (GRC + Wellcome). Many of the same tools/people recur.
- [`aacr-2026/topics/single-cell-spatial-omics/`](../aacr-2026/topics/single-cell-spatial-omics/) — largest AACR topic folder; the methods here are its upstream.
- [`aacr-2026/topics/virtual-cells/`](../aacr-2026/topics/virtual-cells/) — Regev's and Kundaje's "virtual cell" framing maps directly.
- [`cshl-bds-2026/`](../cshl-bds-2026/), [`eurobioc-2025/`](../eurobioc-2025/) — overlapping single-cell/spatial methods cohort.

## Verified post-stream

All nine speakers confirmed against the [official SCGD26 schedule](https://satijalab.org/scgd26/). Notable transcript→reality corrections:

- **Talk 1** — the unidentified GEMINI speaker is **Dingchang Lin** (Johns Hopkins); paper in *Nature* 2026 + bioRxiv.
- **Talk 3** — "Sydney Blackman" → **Sydney B. Blattman** (MSKCC); GIFT preprint on bioRxiv.
- **Talk 4** — "Amanda Urkey" → **Amanda Urke**; method published as **Synapse-seq** (senior author Evan Z. Macosko).
- **Talk 7** — "Alex" → **Alexandra (Alex) Bradu** (Satija Lab); method is **VIPerturb-seq** and the library is **GuEST-List** (Addgene #248188/#248189).
- **Talk 8** — "Kevin Chow" → **Kevin (Yu-Kai) Chao** (Fei Chen Lab, Broad); TimeVault published in *Science* 2026.
- **Talks 2, 5, 6, 9** — Xin Jin, Anshul Kundaje, Aviv Regev, Junyue Cao all confirmed as attributed.

### Still open

- **Archived video link** — the SCGD26 livestream recording URL (the event is live today, Jun 12, 2026; check the NYGC/Satija Lab YouTube once posted).
- **A few lab-member name spellings** inside individual talk pages (flagged per page) and the exact identity of the **MOSCATO** integration layer in the Regev talk.
- **Edition slug** — filed as 2026 / `scgd26` per the event URL.

## Sources

- [Single Cell Genomics Day 2026 — event page](https://satijalab.org/scgd26/)
- [Satija Lab](https://satijalab.org/)
- SCGD26 livestream transcript (captured Jun 12, 2026) — internal
