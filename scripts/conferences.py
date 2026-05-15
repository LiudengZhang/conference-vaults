"""Conference registry — single source of truth for the multi-conference build.

Each entry describes one conference. `build_site.py` iterates this list and
dispatches per-conference work. Path fields are repo-relative.

AACR `data_dir` was moved to `aacr-2026/` in Task 4; `docs_dir` was
moved to `docs/conferences/aacr-2026/` in Task 5.
"""

CONFERENCES = [
    {
        "slug": "aacr-2026",
        "label": "AACR 2026",
        "data_dir": "aacr-2026",                     # was: ""
        "docs_dir": "docs/conferences/aacr-2026",     # was: "docs" (moved in Task 5)
        "topics": [
            ("agentic-ai", "Agentic AI"),
            ("single-cell-spatial-omics", "Single-Cell & Spatial Omics"),
            ("virtual-cells", "Virtual Cells"),
            ("bioinfo-tools", "Bioinfo / Comp Bio / AI Methods"),
            ("clinical-trials", "Clinical Trials"),
        ],
        "has_posters": True,
        "has_tools_index": True,
        "session_source": "txt-transcripts",          # build_session_pages reads .txt from full-sessions/
    },
    {
        "slug": "nextflow-2026",
        "label": "Nextflow Summit 2026",
        "data_dir": "nextflow-2026",
        "docs_dir": "docs/conferences/nextflow-2026",
        "topics": [],
        "has_posters": False,
        "has_tools_index": False,
        "session_source": "md-transcripts",           # session .md files copied with admonition wrapper
    },
    {
        "slug": "jpm-2026",
        "label": "JPM 2026",
        "data_dir": "jpm-2026",
        "docs_dir": "docs/conferences/jpm-2026",
        "topics": [],
        "has_posters": False,
        "has_tools_index": False,
        "placeholder_only": True,
    },
]
