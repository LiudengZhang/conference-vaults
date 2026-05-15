# Per-launch dossiers — AGBT 2026

One page per vendor announcement. Because AGBT abstracts are closed-ish, the per-launch template is the natural unit of the vault (not the per-talk or per-tool template used elsewhere).

## Per-launch template

Each dossier follows this shape:

```
# <Platform/Launch name> — <vendor>

- Vendor / launch date / availability
- Chemistry / read length / throughput / accuracy / cost-per-Gb
- What's new vs prior generation
- Headline benchmarks (with source caveats)
- Reception / competitive context
- Cross-links to relevant tools and downstream talks
```

Every spec line ends with *per vendor PR release dated <date>* or a third-party citation. Numbers are ceiling claims unless an independent benchmark exists.

## Index

| Launch | Vendor | Modality | Throughput (PR) | Read length | Accuracy (PR) | Availability | List price / cost-per-genome | Status |
|---|---|---|---|---|---|---|---|---|
| [**Axelios 1**](roche-axelios-1.md) | Roche | Nanopore SBX (sequencing by expansion) | 16 human genomes/run | Avg duplex ~230–250 bp | Q38 duplex | Pre-order post-AGBT; formal launch summer 2026 | $750k instrument; **$150 / 30× duplex genome**; $0.06 / M reads simplex | ✅ |
| [**VITARI**](element-vitari.md) | Element Biosciences | Short-read SBS (Avidity) | 10B reads/run; 3 TB / 2×150 dual-sided | 2×75 / 2×150 (2×300 roadmap) | >90% Q30 | Pre-orders open; ships H2 2026 | **$689k**; **$100 genome**; $1/Gb | ✅ |
| [**UG200 / UG200 Ultra**](ultima-ug200.md) | Ultima Genomics | Single-end SBS on wafers (isothermal amp) | 162 Tb/wk max; 60 wafers/wk; ~1,350 genomes-equiv (Ultra) | up to ~300 bp single-end; PE roadmap (Solaris 2.0) | Q60 ppmSeq duplex-equivalent | At AGBT | $850k (single wafer) / $1.25M (Ultra) | ✅ |
| [**DNBSEQ-T7+**](complete-dnbseq-t7-plus.md) | Complete Genomics (→ Swiss Rockets) | DNB short-read | **48B reads/24h** (4 flow cells); ~28k genomes/yr | Standard PE | Q40 per-base | Shipping US/CA now | **$800k**; **$100 / genome**; $1/Gb | ✅ |
| [**TruPath**](illumina-trupath.md) | Illumina | Synthetic long-read via NovaSeq X (constellation mapped reads) | 16 genomes/day per NSX | Short reads phased | NovaSeq X Q-scores | Shipping | **$395 / genome** | ✅ |
| [**Q70 duplex kits**](illumina-q70-duplex.md) | Illumina | NovaSeq X duplex chemistry | n/a (kit) | n/a | **Q70** target | Early access H2 2026 | TBD | ✅ |
| [**CiFi**](pacbio-cifi.md) | PacBio + UC Davis | Long-read 3C / Hi-C variant | Chromosome-scale assembly from 1 SMRT cell | HiFi (Revio SPRQ) | HiFi (Q≥30 base) | Shipping | Reagent-only | ✅ |
| [**SPRQ-Hq / SMRT-cell reuse**](pacbio-sprq-hq.md) | PacBio | Revio chemistry update | 2 runs/SMRT cell beta | HiFi | HiFi | Beta → international EA Feb 2026; broad rollout 2026 | $300/genome with SPRQ-Nx | ✅ |
| [**PureTarget**](pacbio-puretarget.md) | PacBio | Targeted long-read enrichment | Capture-based | HiFi | HiFi | Shipping | TBD | ✅ |
| [**PromethION cfDNA/cfRNA multiomic**](ont-promethion-cf-multiomic.md) | Oxford Nanopore | Nanopore | PromethION-class | Long-read | Q38 duplex roadmap | Roadmap | TBD | ✅ |
| [**G4X Spatial Sequencer**](singular-g4x.md) | Singular Genomics | Spatial multiomics | 128 samples / 40 cm² tissue, 5-day workflow | n/a | n/a | Officially released week of AGBT | ~$100s/sample reagent | ✅ |
| [**Xenium RNA+Protein**](10x-xenium-rna-protein.md) | 10x Genomics | In-situ multiomics | 500-plex RNA + 28-plex protein | n/a | n/a | Commercial mid-2026 | TBD | ✅ |
| [**Atera (roadmap preview)**](10x-atera.md) | 10x Genomics | Whole-transcriptome spatial | 18k-gene WTA + stackable 1k-gene panels | n/a | n/a | Formal launch AACR Apr 2026; ships H2 2026 | **$495k instrument**; ~**$2,200 / sample** WTA reagent | ✅ |
| [**CellScape**](bruker-cellscape.md) | Bruker Spatial Biology | Spatial proteomics | Next-gen leap (PR) | n/a | n/a | Roadmap | TBD | ✅ |
| [**PaintScape**](bruker-paintscape.md) | Bruker Spatial Biology | 3D genome visualization | n/a | n/a | n/a | Roadmap | TBD | ✅ |
| [**CosMx mouse whole-transcriptome + 64-protein**](bruker-cosmx-mouse-wt.md) | Bruker (NanoString) | Spatial molecular imager | Mouse WT | n/a | n/a | Roadmap | TBD | ✅ |
| [**MERSCOPE Ultra / MERFISH 2.0**](vizgen-merscope-ultra.md) | Vizgen | Spatial transcriptomics + proteomics | Expanded predesigned panels, organoid support | n/a | n/a | Roadmap | TBD | ✅ |
| [**Pyxa**](stellaromics-pyxa.md) | Stellaromics | 3D spatial imager | First commercial 3D spatial imager (PR) | n/a | n/a | Newcomer launch | TBD | ✅ |
| [**Rhapsody (refresh under Waters)**](waters-rhapsody.md) | Waters (ex-BD) | Single-cell multiomics | Existing platform; new owner messaging | n/a | n/a | Shipping | TBD | ✅ |
| [**Concerto**](codetta-concerto.md) | Codetta Bio | Multimodal biomarker (DNA/RNA/protein) | n/a | n/a | n/a | Commercial | TBD | ✅ |
| [**CellCage**](cellanome-cellcage.md) | Cellanome | Temporal single-cell tracking | Transcriptome over time per cell | n/a | n/a | Roadmap | TBD | ✅ |
| [**mcPCR**](syndex-mcpcr.md) | Syndex Bio | Methyl-copying PCR | Co-amplification of DNA + methylation | n/a | n/a | Roadmap | TBD | ✅ |
| [**Callisto (expanded)**](volta-callisto.md) | Volta Labs | Automated library prep | Expanded capabilities; Roche + Watchmaker partnerships | n/a | n/a | Shipping | TBD | ✅ |

## How to add a dossier

1. Create `launches/<vendor>-<launch-slug>.md` (e.g. `launches/roche-axelios-1.md`).
2. Follow the per-launch template above.
3. Every numeric spec line must end with a citation, e.g. `*per [Element press release dated 2026-02-19](https://...)*`.
4. Flag any vendor figure that lacks third-party validation as **(vendor PR — no independent benchmark)**.
5. Cross-link to:
   - Downstream Bioconductor packages (SpatialExperiment, SpatialFeatureExperiment, BSgenome, DESpace).
   - Downstream AACR / EuroBioC / GBCC talks that report data from this platform.
   - The relevant AGBT plenary or concurrent session (where attribution is possible from public coverage).
