# AACR Annual Meeting 2026 — Virtual Cells Transcripts

Vimeo auto-generated English captions for sessions on **virtual cells, cell/transcriptomic foundation models, in silico perturbation, and multimodal AI agents** for cancer research.

**6 sessions, ~80,500 words, ~8 hours of video.** One session was freshly extracted for this topic; the remaining five are symlinks to sessions that already live under `agentic-ai/` or `single-cell-spatial-omics/` (the three bodies of work overlap heavily — same videos, shared methodological vocabulary).

Captions are Vimeo AI-generated English — expect misheard names ("Bunne" → "Bonner", "Moor" → "Moore") and model names ("scGPT" → "SC-GPT"). Find/replace before quoting.

## Scope (tier B — foundation-model centric)

Sessions were included if they cover any of: **cell / transcriptomic foundation models** (scGPT, Geneformer, TxFM, CELLama, etc.), **virtual patient / virtual cell simulations**, **in silico perturbation prediction**, or **multimodal AI agents built on top of cell/pathology foundation models** for cancer research.

Excluded as out-of-scope: generic deep-learning-on-scRNA methods papers, pathology-only foundation models with no cell-state modeling, and federated-learning / oncology-AI-governance sessions (e.g. FLAIMME was considered and skipped).

## Strong-fit (cell / transcriptomic foundation models, virtual patient / in silico)

| File (date-prefix) | Session title | Date (PT) | Words | Duration | Video ID | Origin |
|---|---|---|---|---|---|---|
| `2026-04-17-pm-foundation-models-multimodal-ai-cancer-research` | Foundation Models and Multimodal AI for Cancer Research (ED03 — Bunne / Yeung-Levy / Moor) | Fri 4/17 4:45–6:15 PM | 11,668 | 79.9 min | 1179385340 | **native** |
| `2026-04-20-am-ai-revolution-in-cancer-research` | AI Revolution in Cancer Research (includes Bo Wang's single-cell foundation-model talk) | Mon 4/20 8:00 AM | 15,915 | 109.8 min | 1179383963 | symlink ← `agentic-ai/` |
| `2026-04-18-ai-in-biomarker-discovery-and-drug-development` | AI in Biomarker Discovery and Drug Development (includes TxFM transcriptomic foundation model) | Sat 4/18 12:30 PM | 12,941 | 92.1 min | 1179383828 | symlink ← `agentic-ai/` |

## Moderate-fit (pathology foundation models + multimodal/agentic AI with cell-state reasoning)

| File (date-prefix) | Session title | Date (PT) | Words | Duration | Video ID | Origin |
|---|---|---|---|---|---|---|
| `2026-04-21-at02-agentic-ai-cancer-researcher` | Agentic AI as the Cancer Researcher — pathology FMs + COMPASS TME model | Tue 4/21 2:30 PM | 12,831 | 92.1 min | 1179383827 | symlink ← `agentic-ai/` |
| `2026-04-18-pm-3d-tissue-imaging-and-cancer` | 3D Tissue Imaging and Cancer — pathology foundation models in 2D/3D | Sat 4/18 12:30 PM | 16,035 | 91.3 min | 1179385155 | symlink ← `single-cell-spatial-omics/` |
| `2026-04-21-pm-dissecting-hematologic-malignancies-single-cell-spatial` | Dissecting Hematologic Malignancies at Single-Cell Resolution — foundation models for scRNA/spatial | Tue 4/21 12:30 PM | 11,126 | 86.7 min | 1179383947 | symlink ← `single-cell-spatial-omics/` |

## Overlap with other topics

The three "bodies of work" at AACR 2026 — agentic-ai, single-cell-spatial-omics, virtual-cells — share videos:

| Session | Also appears in |
|---|---|
| AI Revolution, AI in Biomarker Discovery, AT02 | `agentic-ai/full-sessions/` (primary) |
| 3D Tissue Imaging, Dissecting Hematologic | `single-cell-spatial-omics/full-sessions/` (primary) |
| Foundation Models & Multimodal AI (ED03) | **lives here** — only fit for virtual-cells |

Edit the underlying file once; all symlinks read-through. `ls -L` to dereference.

## Posters

Separately harvested from `cattendee.abstractsonline.com`: **48 abstracts, ~19,000 words** of research text. See `posters/README.md` for details.

## Pipeline (for the single native extraction)

1. Swapcard search for "foundation model" → 2 hits, one (ED03) was a new parent session not already extracted.
2. Navigate to planning page `UGxhbm5pbmdfNDQxNDA1NA==` → Vimeo iframe loads player config.
3. Network request `player.vimeo.com/video/1179385340/config?...transcript=1` → save JSON to `../../raw/virtual-cells/config-2026-04-17-pm-foundation-models-multimodal-ai-cancer-research.json`.
4. Extract `request.text_tracks[0].url` (signed `captions.vimeo.com` URL) → curl with `Referer: https://vimeo.com/` → `.vtt`.
5. Strip cue numbers + timestamps → plain `.txt`.

VTT signatures expire ~6 hours after extraction. Re-extracting means re-navigating the live session page.
