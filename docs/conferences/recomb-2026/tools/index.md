# RECOMB 2026 — Tools

RECOMB 2026 has **65 peer-reviewed accepted papers** across 14 single-track sessions plus 4 keynotes and 7 satellite workshops. The subset that yields tool pages is the intersection of (a) papers that ship a maintained software artifact (most do — RECOMB requires code release for replicability), (b) papers whose method overlaps AACR / EuroBioC / GBCC / ISMB topics (single-cell, spatial omics, cancer evolution, protein/ML, privacy/PRS), and (c) satellite-workshop talks that announce a named package. Pure-theory papers (proof-of-correctness, complexity results, minimizer-density bounds) get a one-paragraph topic entry in `../topics/sequence-phylogeny/` rather than a full tool page.

**Ecosystem field = `standalone-Python / standalone-R / C++ / Rust / Julia / web-service / scverse / Bioconductor / other`** — at RECOMB the modal package is standalone-Python (PyTorch/JAX for ML papers) or C++ (sequence-algorithm papers). Bioconductor and scverse packages are rare at RECOMB itself — they typically surface at EuroBioC / GBCC / ISMB-BOSC instead.

> **Status:** Template stub. Per-tool format proposed here for review *before* bulk extraction runs immediately after the meeting closes (May 29, 2026). Once locked, expected ~50–60 entries get populated from the accepted-paper list + bioRxiv preprints + satellite-workshop rosters.

## Per-tool entry template

Each tool gets its own page (`tools/<package-slug>.md`) following this structure. The shape mirrors EuroBioC2025 / GBCC2025 / ISMB 2026 with three RECOMB-specific additions (a **Proceedings** row for the partnering-journal DOI, a **Session** field naming the RECOMB session, and a **Preprint** row for the bioRxiv/arXiv link):

````markdown
# <ToolName>

**One-line description** — what the tool does in plain language.

- **Maintainer:** <name> (<institution>)
- **Ecosystem:** standalone-Python / standalone-R / C++ / Rust / Julia / web-service / scverse / Bioconductor / other
- **Package / source:** [GitHub link]
- **Docs / vignette:** [link]
- **Status at RECOMB 2026:** accepted paper / satellite-workshop talk / poster / keynote-spinout
- **Preprint:** [bioRxiv or arXiv link — most RECOMB papers have one]
- **Proceedings:** [*Cell Systems* / *Genome Research* / *Journal of Computational Biology* DOI — populated post-meeting; partnering-journal venue announced per paper]

## Talk at RECOMB 2026

- **Authors:** ...
- **Day / Session:** Tue May 26 / Session 1: Sequence I · Wed May 27 / Session 5: Multi-Omics · etc.
- **Slides:** [Zenodo or lab site if posted]
- **Video:** [if a recording is posted to RECOMB YouTube — many sessions are not recorded]
- **Best-paper award:** [Best Paper / Best Student Paper / — — announced at the closing session Fri May 29]

## What it does

2–3 sentences: the problem it solves, the key methodological idea, what it consumes/produces, what it's benchmarked against. RECOMB-specific: name the theoretical guarantee or algorithmic advance (e.g., "O(n log n) instead of O(n²)", "first PAC bound for X", "calibrated FDR under model misspecification").

## Where it fits in the corpus

- AACR 2026: [link if mentioned]
- EuroBioC 2025: [link if mentioned]
- GBCC 2025: [link if mentioned]
- ISMB 2026: [link if mentioned — most RECOMB methods re-surface at ISMB MLCSB / RegSys / HiTSeq]
- BioC 2026: [link if mentioned — Aug 10-12 Seattle]
- Nextflow Summit 2026 / JPM 2026 / EuroBioC 2026 / GBCC 2026: [link if mentioned]

## Notes

Free-form impressions, benchmarks claimed, comparisons to alternatives, AACR-axis fit notes. Flag whether the artifact is a maintained tool (release-ready, versioned, documented) vs. a research codebase (paper-only, reproducibility-grade). RECOMB papers split roughly 50/50 between these two categories.
````

## Tool index

Placeholder table. ~50–60 entries expected after bulk extraction; the populated table will be sortable by Ecosystem, Domain, or Session. Slide DOIs and video links populate over the 2–4 weeks following the meeting (RECOMB does not have a central recording archive; some sessions land on the [RECOMB YouTube channel](https://www.youtube.com/@recombseries) 6–10 weeks post-meeting).

| Package | Ecosystem | Domain | First Author | Day / Session | Preprint | Proceedings | Slides | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|---|
| *(populated post-meeting from accepted-paper list + bioRxiv links; see [`../program-notes.md`](../program-notes.md) for the candidate shortlist)* | | | | | | | | |

## Why this format

- **Preprint row is the anchor for RECOMB** — unlike ISMB (where the *Bioinformatics* DOI is the stable artifact) or EuroBioC / GBCC (where slide DOIs are the most stable artifact), RECOMB's partnering-journal model means the final DOI may take 3–9 months to materialize. The bioRxiv / arXiv preprint is the citation chain that exists *now* and survives even if the partnering-journal submission is rejected.
- **Session field** is the cleanest sort dimension at RECOMB's scale. 14 sessions ÷ 65 papers ≈ 4–6 talks per session. Faceting by session gives the same per-slice size that COSI gives at ISMB.
- **Proceedings row is partnering-journal-aware.** Three possible venues (*Cell Systems* / *Genome Research* / *Journal of Computational Biology*) with different review timelines. The default for unselected papers is the JCB special issue.
- **Ecosystem field favors standalone over framework.** Unlike EuroBioC's Bioconductor-implicit assumption or ISMB's COSI-flavored ecosystem split, at RECOMB the modal entry is standalone-Python (PyTorch / JAX) or C++ (sequence algorithms). scverse / Bioconductor / Galaxy tags are rare at RECOMB itself.
- **Cross-vault "Mentioned elsewhere"** picks up the RECOMB → ISMB cycle (most RECOMB MLCSB-adjacent methods get re-presented at ISMB MLCSB 6–8 weeks later) and the RECOMB → AACR application cycle (methods from RECOMB single-cell / cancer-evolution sessions tend to show up in AACR posters 9–12 months later).

## Open questions

1. **Granularity** — locked: **one page per tool**, same as EuroBioC / GBCC / ISMB.
2. **Theory-only papers** — *new for RECOMB, proposed*: pure-theory papers (no software artifact, no benchmarks on real data — e.g., complexity bounds, minimizer-density results, proofs about flow decomposition correctness) do **not** get tool pages. Instead, they get a one-paragraph topic entry under `../topics/sequence-phylogeny/` with the bioRxiv link. Estimated ~5–8 of 65 papers fall into this bin.
3. **Satellite-workshop tools** — *open*: tools introduced at RECOMB-Seq, RECOMB-CCB, RECOMB-CG, RECOMB-Genetics, RECOMB-Privacy, RECOMB-Arch, or RECOMB-RSG (all May 24–25). Proposed: yes, each gets a tool page with `Status: satellite-workshop` and a `Satellite` field naming the workshop. Same template, lighter required-content bar (satellite workshops have weaker peer review than the main RECOMB program).
4. **Coverage budget** — open: 65 papers + ~30–50 satellite talks ≈ 100–115 candidate tools. We don't expand all of them. Filter: (a) any main-program paper that ships maintained code with a public repo (~50 of 65), (b) any satellite-workshop talk that names a package with a release tag, (c) any keynote spinout (Medvedev / Myers / Stamatakis / Mostafavi lab tools mentioned in the keynote). Estimated ~50–60 after filtering.
5. **Cross-link to ISMB 2026** — *new pattern*: RECOMB → ISMB is a tight 6–8-week pipeline. Many MLCSB-adjacent RECOMB methods get re-presented at ISMB MLCSB Wed Jul 15 or Thu Jul 16 (Zitnik keynote on Wed sets that table). Proposed: when a RECOMB tool page is created and its ISMB MLCSB talk is also confirmed, **cross-link reciprocally** — RECOMB page gets `ISMB 2026: <link>` in "Where it fits in the corpus"; ISMB page gets `RECOMB 2026: <link>` symmetrically. This is the primary cross-vault traffic pattern we expect.
6. **Best-paper flagging** — locked: best-paper and best-student-paper winners get a callout badge in the tool-page header (`Status: accepted paper — BEST PAPER`) and a top-of-list position in this index table. Winners are announced at the closing session Fri May 29 PM; update is same-day.
