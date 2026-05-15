# Tools

Per-tool reference dossiers for the foundation models, single-cell models, and analysis tools that surface in the AACR 2026 corpus. Each tool with ≥3 deduplicated mentions across all 5 topics gets a dedicated page covering: family, modality, license, architecture, every poster and session that names it, and where the evidence in the corpus is weak.

The matrix below is sortable and filterable. Click a tool name for the full dossier.

<div class="tools-table" data-src="../../../assets/bioinfo-tools/tool-matrix.json"></div>

## Index

### Pathology foundation models

| Tool | Architecture | Released | License | Dossier |
|---|---|---|---|---|
| CHIEF | CTransPath + attention-MIL | 2024 (Nature) | AGPL-3.0, non-commercial | [chief.md](chief.md) |
| UNI / UNI2 | ViT-L/16 (UNI), ViT-H/14 (UNI2-h) | 2024 / 2025 | CC-BY-NC-ND 4.0 | [uni.md](uni.md) |
| Prov-GigaPath | ViT + LongNet slide encoder | 2024 (Nature) | Gated, non-commercial research | [prov-gigapath.md](prov-gigapath.md) |
| Virchow / Virchow-2 | ViT-H/14, 632M | 2024 / 2024 | Virchow Apache-2.0; Virchow-2 CC-BY-NC-ND 4.0 | [virchow.md](virchow.md) |
| Hibou-B / Hibou-L | ViT-B/14 (86M), ViT-L/14 (307M) | 2024 (HistAI) | Apache-2.0, commercial use allowed | [hibou.md](hibou.md) |
| PathChat / PathChat-2 | UNI vision + 13B Llama-2 (LLaVA-style) | 2024 (Nature) | Closed weights; FDA Breakthrough (PathChat DX) | [pathchat.md](pathchat.md) |

### Single-cell foundation models

| Tool | Modality | Released | License | Dossier |
|---|---|---|---|---|
| scGPT | scRNA-seq | 2024 (Nature Methods) | MIT | [scgpt.md](scgpt.md) |
| Geneformer | scRNA-seq | 2023 (Nature) | Apache-2.0 | [geneformer.md](geneformer.md) |
| scFoundation | scRNA-seq (continuous-valued, xTrimoGene 100M) | 2024 (Nature Methods) | Apache-2.0 (code); separate model-weight license | [scfoundation.md](scfoundation.md) |
| UCE | scRNA-seq (cross-species, ESM2-tokenized; 33-layer, ~650M) | 2023 (bioRxiv) | MIT (code) | [uce.md](uce.md) |
| GET | scATAC-seq peaks + DNA sequence (regulatory FM) | 2025 (Nature) | Open-source (GET-Foundation org) | [get.md](get.md) |
| CellPLM | scRNA-seq + SRT (cell-as-token, ~85M) | 2024 (ICLR) | BSD-2-Clause | [cellplm.md](cellplm.md) |

### Spatial / other

| Tool | Modality | Released | License | Dossier |
|---|---|---|---|---|
| Cell2Location | Spatial transcriptomics deconvolution | 2022 (Nat Biotech) | Apache-2.0 | [cell2location.md](cell2location.md) |

## Notable absences from the corpus

_To be populated after first survey — tools that fall below the 3-mention gate but are well-known enough to flag (e.g. scBERT, PLIP)._
