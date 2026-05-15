# Bioinfo Tool Dossiers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a per-tool reference layer (~12-15 dossier pages + a sortable comparison matrix) under the Bioinfo / Comp Bio / AI Methods topic of the AACR 2026 MkDocs site.

**Architecture:** Extend `scripts/build_site.py` with a `build_tool_pages()` step that scans the whole corpus (5 topic JSONLs, deduped by `Id`; 26 unique session `.txt` files, deduped by canonical slug) for each tool's aliases, applies a 3-mention inclusion gate, and writes/refreshes the auto-generated mention block between HTML-comment markers in each `tools/<slug>.md` (preserving hand-written prose). Emits `tool-matrix.json` for a Tabulator table on the new `tools/index.md` landing page.

**Tech Stack:** Python 3 (stdlib only — `re`, `json`, `pathlib`, `collections`); MkDocs Material; Tabulator.js (already vendored); Cloudflare Pages auto-deploy on `git push`.

**Spec:** `docs/superpowers/specs/2026-05-02-bioinfo-tool-dossiers-design.md` (commit b33e29a).

---

## File structure

**Modified:**
- `scripts/build_site.py` — new `TOOLS` constant, `INCLUSION_GATE` constant, `build_tool_pages()` and helpers; one new call from `main()`. Single source for all build logic, matching the existing pattern (`build_poster_json`, `build_session_pages`).
- `mkdocs.yml` — add `Tools` collapsible group under the existing `Bioinfo / Comp Bio / AI Methods` nav block. Add `javascripts/tools-table.js` to `extra_javascript`.
- `docs/topics/bioinfo-tools/index.md` — one new paragraph linking to the Tools index.
- `docs/topics/bioinfo-tools/landscape.md` — manual find/replace, link tool names to dossiers.
- `docs/topics/bioinfo-tools/synthesis-fm-pathology-traction.md` — same find/replace pass.
- `docs/topics/virtual-cells/landscape.md` — same find/replace.
- `docs/topics/agentic-ai/landscape.md` — same find/replace.
- `docs/topics/single-cell-spatial-omics/landscape.md` — same find/replace.

**Created:**
- `scripts/test_build_tool_pages.py` — unit tests for the new module-level functions (regex match, dedup, gate, mention render).
- `docs/javascripts/tools-table.js` — small Tabulator init for the tools matrix (columns differ from posters table, so a parallel script is cleaner than overloading `posters.js`).
- `docs/topics/bioinfo-tools/tools/index.md` — landing page (intro paragraph + `<div class="tools-table" data-src="...">`).
- `docs/topics/bioinfo-tools/tools/<slug>.md` × ~12-15 — one per surviving tool. Author-written, with auto-regenerated mention block between markers.
- `docs/assets/bioinfo-tools/tool-matrix.json` — auto-emitted; consumed by `tools-table.js`.
- `docs/assets/bioinfo-tools/tool-mentions.json` — auto-emitted; available for downstream consumers.

---

## Task 1: Wire up the test harness and `TOOLS` constant

**Files:**
- Modify: `scripts/build_site.py`
- Create: `scripts/test_build_tool_pages.py`

- [ ] **Step 1: Add `TOOLS` and `INCLUSION_GATE` constants to `build_site.py`**

In `scripts/build_site.py`, after the existing `TOPICS` constant (around line 41), add:

```python
INCLUSION_GATE = 3  # min unique mentions (posters + sessions, deduped) to ship a dossier

# (display_name, slug, family, [aliases])
# aliases are matched case-insensitive with word boundaries on both sides
TOOLS = [
    ("CHIEF",                 "chief",          "path-fm",     ["CHIEF"]),
    ("UNI / UNI2",            "uni",            "path-fm",     ["UNI", "UNI2", "UNI-2"]),
    ("CONCH",                 "conch",          "path-fm",     ["CONCH"]),
    ("PathChat",              "pathchat",       "path-fm",     ["PathChat", "Path-Chat"]),
    ("Virchow / Virchow2",    "virchow",        "path-fm",     ["Virchow", "Virchow2", "Virchow-2"]),
    ("Prov-GigaPath",         "prov-gigapath",  "path-fm",     ["Prov-GigaPath", "GigaPath"]),
    ("TITAN",                 "titan",          "path-fm",     ["TITAN"]),
    ("PLIP",                  "plip",           "path-fm",     ["PLIP"]),
    ("scGPT",                 "scgpt",          "sc-fm",       ["scGPT", "SC-GPT"]),
    ("Geneformer",            "geneformer",     "sc-fm",       ["Geneformer"]),
    ("UCE",                   "uce",            "sc-fm",       ["UCE", "Universal Cell Embeddings"]),
    ("scFoundation",          "scfoundation",   "sc-fm",       ["scFoundation"]),
    ("scBERT",                "scbert",         "sc-fm",       ["scBERT"]),
    ("Nicheformer",           "nicheformer",    "sc-fm",       ["Nicheformer"]),
    ("Cell2Sentence",         "cell2sentence",  "sc-fm",       ["Cell2Sentence", "C2S"]),
    ("Tangram",               "tangram",        "spatial",     ["Tangram"]),
    ("Cell2Location",         "cell2location",  "spatial",     ["Cell2Location", "cell2location"]),
    ("GEARS",                 "gears",          "perturbation",["GEARS"]),
    ("AlphaFold-Multimer",    "alphafold-multimer", "protein", ["AlphaFold-Multimer", "AlphaFold Multimer"]),
    ("ESM",                   "esm",            "protein",     ["ESM-2", "ESM2", "ESMFold"]),
]
```

- [ ] **Step 2: Create the test file with one failing import test**

Create `scripts/test_build_tool_pages.py`:

```python
"""Tests for the tool-dossier build pipeline added to build_site.py."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


def test_tools_constant_loads():
    from build_site import TOOLS, INCLUSION_GATE
    assert isinstance(TOOLS, list)
    assert len(TOOLS) >= 15
    assert INCLUSION_GATE == 3
    # each row is (name, slug, family, aliases)
    for name, slug, family, aliases in TOOLS:
        assert isinstance(name, str) and name
        assert isinstance(slug, str) and slug.replace("-", "").isalnum()
        assert family in {"path-fm", "sc-fm", "spatial", "perturbation", "protein"}
        assert isinstance(aliases, list) and aliases
```

- [ ] **Step 3: Run test to verify it passes**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py -v
```

Expected: PASS (or `pytest` not installed — install with `pip install pytest` first).

- [ ] **Step 4: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add scripts/build_site.py scripts/test_build_tool_pages.py
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
build: add TOOLS constant + INCLUSION_GATE for tool dossiers

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: Alias-match utility

**Files:**
- Modify: `scripts/build_site.py`
- Modify: `scripts/test_build_tool_pages.py`

- [ ] **Step 1: Write the failing test**

Append to `scripts/test_build_tool_pages.py`:

```python
def test_match_aliases_word_boundary():
    from build_site import match_aliases
    text = "We applied scGPT and SC-GPT variants alongside Geneformer."
    aliases = ["scGPT", "SC-GPT"]
    assert match_aliases(text, aliases) is True

def test_match_aliases_negative_inside_word():
    from build_site import match_aliases
    # 'UCE' should not match inside 'reduced' or 'producer'
    text = "This reduces noise and produces clean embeddings."
    assert match_aliases(text, ["UCE"]) is False

def test_match_aliases_case_insensitive():
    from build_site import match_aliases
    assert match_aliases("we used cell2location to deconvolve", ["Cell2Location"]) is True
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py -v
```

Expected: 3 failures (`match_aliases not defined`).

- [ ] **Step 3: Implement `match_aliases` in `build_site.py`**

Add after the constants section, before `ensure_dirs()`:

```python
def _alias_pattern(alias: str) -> re.Pattern:
    """Word-boundary, case-insensitive match for one alias."""
    return re.compile(rf"(?<![A-Za-z0-9_]){re.escape(alias)}(?![A-Za-z0-9_])", re.IGNORECASE)


def match_aliases(text: str, aliases: list[str]) -> bool:
    """Return True if any alias matches `text` with word boundaries."""
    return any(_alias_pattern(a).search(text) for a in aliases)
```

(Note: standard `\b` boundary doesn't work for tokens that start/end with non-word characters like `SC-GPT`. The custom lookbehind/lookahead handles that.)

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py -v
```

Expected: 4 PASS.

- [ ] **Step 5: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add scripts/build_site.py scripts/test_build_tool_pages.py
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
build: add alias word-boundary matcher with tests

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: Whole-corpus inventory loader

**Files:**
- Modify: `scripts/build_site.py`
- Modify: `scripts/test_build_tool_pages.py`

- [ ] **Step 1: Write the failing test**

Append to `scripts/test_build_tool_pages.py`:

```python
def test_load_corpus_dedups_posters():
    from build_site import load_corpus
    corpus = load_corpus()
    # poster Ids must be unique
    poster_ids = [p["Id"] for p in corpus["posters"]]
    assert len(poster_ids) == len(set(poster_ids))
    # session keys must be unique stems
    assert len(corpus["sessions"]) == len(set(s["stem"] for s in corpus["sessions"]))
    # corpus has substantial content
    assert len(corpus["posters"]) > 1500
    assert len(corpus["sessions"]) >= 20
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py::test_load_corpus_dedups_posters -v
```

Expected: FAIL (`load_corpus not defined`).

- [ ] **Step 3: Implement `load_corpus()` in `build_site.py`**

Add after `match_aliases`:

```python
def load_corpus() -> dict:
    """Load every poster JSONL across all 5 topics (deduped by Id) and every
    unique session .txt (deduped by canonical slug, follows symlinks).

    Returns: {"posters": [{"Id","Title","Abstract","_topic"}, ...],
              "sessions": [{"stem","text","_topics":[...]}, ...]}
    """
    posters_by_id: dict[str, dict] = {}
    for topic_slug, _ in TOPICS:
        jsonl = TRANSCRIPTS / topic_slug / "posters" / "abstracts.jsonl"
        if not jsonl.exists():
            continue
        with jsonl.open() as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                p = json.loads(line)
                pid = p.get("Id")
                if not pid:
                    continue
                if pid in posters_by_id:
                    posters_by_id[pid].setdefault("_topics", []).append(topic_slug)
                else:
                    p["_topic"] = topic_slug
                    p["_topics"] = [topic_slug]
                    posters_by_id[pid] = p

    sessions_by_stem: dict[str, dict] = {}
    for topic_slug, _ in TOPICS:
        fs_dir = TRANSCRIPTS / topic_slug / "full-sessions"
        if not fs_dir.exists():
            continue
        for txt in sorted(fs_dir.glob("*.txt")):
            stem = txt.stem
            if stem in sessions_by_stem:
                sessions_by_stem[stem]["_topics"].append(topic_slug)
                continue
            text = resolve_symlink(txt).read_text()
            sessions_by_stem[stem] = {
                "stem": stem,
                "text": text,
                "_topics": [topic_slug],
            }

    return {
        "posters": list(posters_by_id.values()),
        "sessions": list(sessions_by_stem.values()),
    }
```

- [ ] **Step 4: Run test to verify it passes**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py::test_load_corpus_dedups_posters -v
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add scripts/build_site.py scripts/test_build_tool_pages.py
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
build: add whole-corpus loader with poster/session dedup

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: Per-tool mention scan

**Files:**
- Modify: `scripts/build_site.py`
- Modify: `scripts/test_build_tool_pages.py`

- [ ] **Step 1: Write the failing test**

Append to `scripts/test_build_tool_pages.py`:

```python
def test_scan_mentions_returns_structured_hits():
    from build_site import load_corpus, scan_mentions
    corpus = load_corpus()
    # CHIEF should have at least one hit somewhere in the corpus
    hits = scan_mentions(corpus, ["CHIEF"])
    assert "posters" in hits and "sessions" in hits
    # Each hit has the fields the renderer needs
    if hits["posters"]:
        h = hits["posters"][0]
        assert "Id" in h and "Title" in h and "context" in h and "_topics" in h
    if hits["sessions"]:
        h = hits["sessions"][0]
        assert "stem" in h and "context" in h
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py::test_scan_mentions_returns_structured_hits -v
```

Expected: FAIL (`scan_mentions not defined`).

- [ ] **Step 3: Implement `scan_mentions` in `build_site.py`**

Add after `load_corpus`:

```python
def _context_window(text: str, alias: str, chars: int = 220) -> str:
    """Return ~`chars` chars of `text` centered on the first alias hit, single line."""
    pat = _alias_pattern(alias)
    m = pat.search(text)
    if not m:
        return ""
    start = max(0, m.start() - chars // 2)
    end = min(len(text), m.end() + chars // 2)
    snippet = text[start:end].strip()
    snippet = re.sub(r"\s+", " ", snippet)
    if start > 0:
        snippet = "…" + snippet
    if end < len(text):
        snippet = snippet + "…"
    return snippet


def scan_mentions(corpus: dict, aliases: list[str]) -> dict:
    """Find unique poster + session hits for any alias in `aliases`.

    Returns {"posters": [...], "sessions": [...]}, each item a dict
    augmented with `context` (~220-char snippet around first match).
    """
    poster_hits = []
    for p in corpus["posters"]:
        haystack = (p.get("Title", "") or "") + "\n" + (p.get("Abstract", "") or "")
        if not match_aliases(haystack, aliases):
            continue
        ctx = ""
        for a in aliases:
            ctx = _context_window(haystack, a)
            if ctx:
                break
        poster_hits.append({
            "Id": p["Id"],
            "Title": p.get("Title", ""),
            "PresentationNumber": p.get("PresentationNumber", "") or p.get("Id", ""),
            "context": ctx,
            "_topics": p.get("_topics", [p.get("_topic", "")]),
        })

    session_hits = []
    for s in corpus["sessions"]:
        if not match_aliases(s["text"], aliases):
            continue
        ctx = ""
        for a in aliases:
            ctx = _context_window(s["text"], a)
            if ctx:
                break
        session_hits.append({
            "stem": s["stem"],
            "context": ctx,
            "_topics": s["_topics"],
        })

    return {"posters": poster_hits, "sessions": session_hits}
```

- [ ] **Step 4: Run test to verify it passes**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py -v
```

Expected: all tests PASS.

- [ ] **Step 5: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add scripts/build_site.py scripts/test_build_tool_pages.py
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
build: per-tool mention scanner with context windows

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: Dry-run survey (no file writes)

**Files:**
- Modify: `scripts/build_site.py`

- [ ] **Step 1: Add a survey helper that prints the gate result**

Add to `scripts/build_site.py` after `scan_mentions`:

```python
def survey_tools() -> dict:
    """Compute mention counts for every tool in TOOLS and report which pass the gate.

    Returns {"survivors": [...], "dropped": [...]}, each list item a dict.
    Prints a summary table to stdout.
    """
    corpus = load_corpus()
    survivors, dropped = [], []
    for name, slug, family, aliases in TOOLS:
        hits = scan_mentions(corpus, aliases)
        np_, ns_ = len(hits["posters"]), len(hits["sessions"])
        total = np_ + ns_
        row = {"name": name, "slug": slug, "family": family,
               "n_posters": np_, "n_sessions": ns_, "total": total,
               "hits": hits}
        (survivors if total >= INCLUSION_GATE else dropped).append(row)

    print(f"\n{'Tool':<24} {'Family':<14} {'Posters':>8} {'Sessions':>9} {'Total':>6}")
    print("-" * 65)
    for r in sorted(survivors, key=lambda x: -x["total"]):
        print(f"{r['name']:<24} {r['family']:<14} {r['n_posters']:>8} {r['n_sessions']:>9} {r['total']:>6}  ✓")
    for r in sorted(dropped, key=lambda x: -x["total"]):
        print(f"{r['name']:<24} {r['family']:<14} {r['n_posters']:>8} {r['n_sessions']:>9} {r['total']:>6}  dropped")
    print(f"\n{len(survivors)} survivors, {len(dropped)} dropped (gate={INCLUSION_GATE})")
    return {"survivors": survivors, "dropped": dropped}
```

Add a CLI flag in `main()`:

```python
def main():
    if "--survey" in sys.argv:
        survey_tools()
        return
    ensure_dirs()
    # ... existing logic ...
```

- [ ] **Step 2: Run the survey**

```bash
cd /Users/lzhang34/Desktop/AACR && python scripts/build_site.py --survey
```

Expected: a table listing all 20 tools with poster/session counts and ✓/dropped marks. Save the output (paste into commit message body) — this is the canonical list of dossiers to author.

- [ ] **Step 3: Commit (with the survey output captured)**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add scripts/build_site.py
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
build: --survey flag for tool-dossier inclusion gate

Survey output (gate=3):
<paste table from Step 2 here>

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: Render the auto-generated mention block

**Files:**
- Modify: `scripts/build_site.py`
- Modify: `scripts/test_build_tool_pages.py`

- [ ] **Step 1: Write the failing test**

Append to `scripts/test_build_tool_pages.py`:

```python
def test_render_mentions_block_format():
    from build_site import render_mentions_block
    hits = {
        "posters": [
            {"Id": "3074", "Title": "SPOT-Met: …", "PresentationNumber": "LB123",
             "context": "We used CHIEF to predict outcomes…", "_topics": ["bioinfo-tools"]},
        ],
        "sessions": [
            {"stem": "2026-04-17-pm-foundation-models-multimodal-ai-cancer-research",
             "context": "…CHIEF demo by the Mahmood lab…", "_topics": ["bioinfo-tools"]},
        ],
    }
    block = render_mentions_block("CHIEF", hits)
    assert "<!-- mentions:start -->" in block
    assert "<!-- mentions:end -->" in block
    assert "Posters mentioning CHIEF (n=1)" in block
    assert "Sessions mentioning CHIEF (n=1)" in block
    assert "**LB123**" in block  # posters render as bold number + italic title (no individual pages)
    assert "../../../sessions/2026-04-17-pm-foundation-models" in block

def test_inject_mentions_block_preserves_prose():
    from build_site import inject_mentions_block
    md = """# CHIEF

Hand-written intro.

<!-- mentions:start -->
old auto content
<!-- mentions:end -->

## What's missing

Hand-written notes preserved.
"""
    new_block = "<!-- mentions:start -->\nnew auto\n<!-- mentions:end -->"
    out = inject_mentions_block(md, new_block)
    assert "Hand-written intro." in out
    assert "Hand-written notes preserved." in out
    assert "new auto" in out
    assert "old auto content" not in out
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py -v
```

Expected: 2 new failures.

- [ ] **Step 3: Implement renderers**

Add to `scripts/build_site.py` after `survey_tools`:

```python
MENTIONS_START = "<!-- mentions:start -->"
MENTIONS_END = "<!-- mentions:end -->"


def render_mentions_block(tool_name: str, hits: dict) -> str:
    """Build the markdown block (markers included) for a tool's corpus mentions."""
    lines = [MENTIONS_START, ""]
    posters = hits["posters"]
    sessions = hits["sessions"]

    lines.append(f"**Posters mentioning {tool_name} (n={len(posters)}):**")
    lines.append("")
    if not posters:
        lines.append("_No posters in the AACR 2026 corpus mention this tool._")
    else:
        for p in sorted(posters, key=lambda x: x.get("PresentationNumber", "")):
            num = p.get("PresentationNumber") or p.get("Id", "")
            title = p.get("Title", "").strip()
            ctx = p.get("context", "")
            lines.append(f"- **{num}** — *{title}*")
            if ctx:
                lines.append(f"  {ctx}")
    lines.append("")

    lines.append(f"**Sessions mentioning {tool_name} (n={len(sessions)}):**")
    lines.append("")
    if not sessions:
        lines.append("_No session transcripts in the AACR 2026 corpus mention this tool._")
    else:
        for s in sorted(sessions, key=lambda x: x["stem"]):
            stem = s["stem"]
            ctx = s.get("context", "")
            lines.append(f"- [{stem}](../../../sessions/{stem}.md)")
            if ctx:
                lines.append(f"  {ctx}")
    lines.append("")
    lines.append(MENTIONS_END)
    return "\n".join(lines)


def inject_mentions_block(md_text: str, new_block: str) -> str:
    """Replace the existing mentions block (between markers) with `new_block`.

    If markers are missing, append `new_block` to the end. `new_block` must
    contain its own start/end markers.
    """
    if MENTIONS_START in md_text and MENTIONS_END in md_text:
        pattern = re.compile(
            re.escape(MENTIONS_START) + r".*?" + re.escape(MENTIONS_END),
            re.DOTALL,
        )
        return pattern.sub(new_block, md_text)
    sep = "" if md_text.endswith("\n") else "\n"
    return md_text + sep + "\n" + new_block + "\n"
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py -v
```

Expected: all tests PASS.

- [ ] **Step 5: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add scripts/build_site.py scripts/test_build_tool_pages.py
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
build: render + inject mention blocks between HTML-comment markers

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 7: Stub generator + `build_tool_pages()` orchestrator

**Files:**
- Modify: `scripts/build_site.py`
- Modify: `scripts/test_build_tool_pages.py`

- [ ] **Step 1: Write the failing test**

Append to `scripts/test_build_tool_pages.py`:

```python
def test_stub_template_has_all_required_sections():
    from build_site import stub_dossier
    out = stub_dossier(
        name="CHIEF", slug="chief", family="path-fm",
        also_in=["virtual-cells"],
    )
    assert "# CHIEF" in out
    assert "**Family:**" in out
    assert "**Modality:**" in out
    assert "**License:**" in out
    assert "**Code/checkpoint:**" in out
    assert "**Also surfaced in:**" in out
    assert "## Architecture & training" in out
    assert "## Use in the AACR 2026 corpus" in out
    assert "<!-- mentions:start -->" in out
    assert "<!-- mentions:end -->" in out
    assert "## What's missing" in out
    assert "## Takeaway" in out
    assert "TODO" in out  # placeholders flag the human-author items
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py::test_stub_template_has_all_required_sections -v
```

Expected: FAIL.

- [ ] **Step 3: Implement `stub_dossier` and `build_tool_pages`**

Add to `scripts/build_site.py`:

```python
def stub_dossier(name: str, slug: str, family: str, also_in: list[str]) -> str:
    """Author-fillable scaffold for a new tool dossier."""
    also = ", ".join(sorted(set(also_in))) if also_in else "(none)"
    return f"""# {name}

**Family:** {family}
**Modality:** TODO
**Released:** TODO
**License:** TODO
**Code/checkpoint:** TODO
**Also surfaced in:** {also}

> TODO — one-paragraph plain-language description (~3 sentences). What
> the tool does, what it trains on, what its standout claim is.

## Architecture & training

TODO — backbone, pretraining corpus, objective, parameter count.

## Use in the AACR 2026 corpus

{MENTIONS_START}
_Auto-generated on next build._
{MENTIONS_END}

## What's missing / where evidence is weak

- TODO

## Takeaway

TODO — one paragraph on what the AACR 2026 corpus uniquely teaches us
about {name}.
"""


def build_tool_pages():
    """Survey the corpus, gate, then write/refresh dossier mention blocks
    and emit the matrix + mentions JSON for the index page."""
    tools_dir = DOCS / "topics" / "bioinfo-tools" / "tools"
    tools_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = DOCS / "assets" / "bioinfo-tools"
    assets_dir.mkdir(parents=True, exist_ok=True)

    survey = survey_tools()
    survivors = survey["survivors"]
    dropped = survey["dropped"]

    matrix_rows = []
    mentions_dump = {}
    metadata_re = re.compile(r"^\*\*([\w/ ]+?):\*\*\s*(.+)$", re.MULTILINE)

    for r in survivors:
        slug, name, family, hits = r["slug"], r["name"], r["family"], r["hits"]
        page = tools_dir / f"{slug}.md"

        # Determine "also surfaced in" topics
        topics_for_tool = set()
        for h in hits["posters"]:
            topics_for_tool.update(h["_topics"])
        for h in hits["sessions"]:
            topics_for_tool.update(h["_topics"])
        topics_for_tool.discard("bioinfo-tools")
        also_in = sorted(topics_for_tool)

        if not page.exists():
            page.write_text(stub_dossier(name, slug, family, also_in))
            print(f"→ scaffolded {page.relative_to(ROOT)}")

        # Refresh the mention block in place
        md = page.read_text()
        new_block = render_mentions_block(name, hits)
        md = inject_mentions_block(md, new_block)
        page.write_text(md)

        # Parse header metadata for matrix
        meta = dict(metadata_re.findall(md))
        matrix_rows.append({
            "tool": name,
            "slug": slug,
            "family": family,
            "modality": meta.get("Modality", "").strip(),
            "released": meta.get("Released", "").strip(),
            "license": meta.get("License", "").strip(),
            "n_posters": r["n_posters"],
            "n_sessions": r["n_sessions"],
            "also_in": also_in,
        })
        mentions_dump[slug] = hits

    (assets_dir / "tool-matrix.json").write_text(
        json.dumps(matrix_rows, ensure_ascii=False, indent=2)
    )
    (assets_dir / "tool-mentions.json").write_text(
        json.dumps(mentions_dump, ensure_ascii=False)
    )
    print(f"→ {len(survivors)} dossiers + tool-matrix.json + tool-mentions.json")
    if dropped:
        print(f"  dropped (n<{INCLUSION_GATE}): " + ", ".join(
            f"{d['name']} (n={d['total']})" for d in dropped
        ))
```

Then update `main()` to call it:

```python
def main():
    if "--survey" in sys.argv:
        survey_tools()
        return
    ensure_dirs()
    vendor_tabulator()
    total_posters = 0
    for topic_slug, _ in TOPICS:
        total_posters += build_poster_json(topic_slug)
    total_sessions = build_session_pages()
    build_tool_pages()
    print(f"\nBuild preprocessing complete.")
    print(f"  Posters  : {total_posters:>5} total across {len(TOPICS)} topics")
    print(f"  Sessions : {total_sessions:>5} unique transcript pages")
```

- [ ] **Step 4: Run tests + a real build**

```bash
cd /Users/lzhang34/Desktop/AACR && python -m pytest scripts/test_build_tool_pages.py -v
cd /Users/lzhang34/Desktop/AACR && python scripts/build_site.py
```

Expected: all tests PASS. Build run scaffolds `docs/topics/bioinfo-tools/tools/<slug>.md` for each survivor and writes `docs/assets/bioinfo-tools/tool-matrix.json`. Inspect:

```bash
ls /Users/lzhang34/Desktop/AACR/docs/topics/bioinfo-tools/tools/
cat /Users/lzhang34/Desktop/AACR/docs/assets/bioinfo-tools/tool-matrix.json | python -m json.tool | head -40
```

- [ ] **Step 5: Commit (scaffolds + assets)**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add scripts/build_site.py scripts/test_build_tool_pages.py docs/topics/bioinfo-tools/tools/ docs/assets/bioinfo-tools/
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
build: scaffold tool dossier stubs + emit matrix/mentions JSON

Each surviving tool gets a TODO-marked stub page on first build.
Subsequent builds refresh the auto-generated mention block in place
without touching hand-written prose.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 8: Tools index page + Tabulator wiring

**Files:**
- Create: `docs/topics/bioinfo-tools/tools/index.md`
- Create: `docs/javascripts/tools-table.js`
- Modify: `mkdocs.yml`

- [ ] **Step 1: Create the tools index landing page**

Create `docs/topics/bioinfo-tools/tools/index.md`:

```markdown
# Tools

Per-tool reference dossiers for the foundation models, single-cell models, and analysis tools that surface in the AACR 2026 corpus. Each tool with ≥3 deduplicated mentions across all 5 topics gets a dedicated page covering: family, modality, license, architecture, every poster and session that names it, and where the evidence in the corpus is weak.

The matrix below is sortable and filterable. Click a tool name for the full dossier.

<div class="tools-table" data-src="../../../assets/bioinfo-tools/tool-matrix.json"></div>

## Notable absences from the corpus

_To be populated after first survey — tools that fall below the 3-mention gate but are well-known enough to flag (e.g. scBERT, PLIP)._
```

- [ ] **Step 2: Create the Tabulator init script**

Create `docs/javascripts/tools-table.js`:

```javascript
// Tools matrix on the bioinfo-tools/tools/ index page.
// Different columns from the posters table → its own init.

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".tools-table").forEach(initToolsTable);
});

async function initToolsTable(container) {
  const src = container.dataset.src;
  if (!src) return;
  try {
    const resp = await fetch(src);
    if (!resp.ok) throw new Error(`Fetch failed: ${resp.status}`);
    const rows = await resp.json();
    new Tabulator(container, {
      data: rows,
      layout: "fitColumns",
      pagination: false,
      initialSort: [{ column: "n_posters", dir: "desc" }],
      columns: [
        {
          title: "Tool", field: "tool", widthGrow: 2,
          formatter: (cell) => {
            const r = cell.getRow().getData();
            return `<a href="${r.slug}/">${r.tool}</a>`;
          },
        },
        { title: "Family", field: "family", headerFilter: "list",
          headerFilterParams: { values: true, clearable: true } },
        { title: "Modality", field: "modality" },
        { title: "Released", field: "released", width: 100 },
        { title: "Posters", field: "n_posters", width: 100, sorter: "number" },
        { title: "Sessions", field: "n_sessions", width: 100, sorter: "number" },
        { title: "License", field: "license" },
        {
          title: "Also in", field: "also_in", widthGrow: 2,
          formatter: (cell) => (cell.getValue() || []).join(", "),
        },
      ],
    });
  } catch (e) {
    container.innerHTML = `<p><strong>Error loading tools matrix:</strong> ${e.message}</p>`;
  }
}
```

- [ ] **Step 3: Wire `tools-table.js` into `mkdocs.yml`**

In `mkdocs.yml`, under `extra_javascript`, add the line so it reads:

```yaml
extra_javascript:
  - javascripts/tabulator.min.js
  - javascripts/posters.js
  - javascripts/tools-table.js
  - https://hypothes.is/embed.js
```

- [ ] **Step 4: Local build + visual smoke test**

```bash
cd /Users/lzhang34/Desktop/AACR && python scripts/build_site.py && mkdocs build --strict
```

Expected: build succeeds, no warnings about missing pages. Then:

```bash
cd /Users/lzhang34/Desktop/AACR && mkdocs serve -a 127.0.0.1:8765 &
```

Visit `http://127.0.0.1:8765/topics/bioinfo-tools/tools/`. Verify the matrix renders with rows, headers, sorting, and clickable tool names. Stop the server (`kill %1`).

- [ ] **Step 5: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add mkdocs.yml docs/javascripts/tools-table.js docs/topics/bioinfo-tools/tools/index.md
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
ui: tools matrix index page with Tabulator

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 9: Author dossier prose for surviving tools

**Files:**
- Modify: every `docs/topics/bioinfo-tools/tools/<slug>.md` produced in Task 7

This is the highest-judgement task — the build pipeline is in place; what remains is real prose. Author each surviving dossier in turn. Use the survey output (Task 5) as the worklist.

- [ ] **Step 1: For each surviving tool, fill the metadata header**

For `<slug>.md`, replace each `TODO` value with verified content. Source preference (in order):
1. The tool's upstream paper / GitHub README.
2. The Hugging Face model card (if applicable).
3. Recent reviews citing the tool.

Required fields: `Modality`, `Released`, `License`, `Code/checkpoint`. Don't leave any `TODO` strings — if a field genuinely doesn't apply, write `n/a` and explain in prose.

- [ ] **Step 2: Write the description blockquote**

The `> TODO …` line becomes a 2-3 sentence plain-language summary. Three sentence pattern: (1) what it is and what task, (2) what it trains on, (3) what its standout claim is. Cite the upstream paper inline if possible.

- [ ] **Step 3: Write the Architecture & training section**

3-5 sentences covering: backbone (e.g. ViT-L/16), pretraining corpus size (e.g. "60K WSIs from 19 sites"), pretraining objective (contrastive, MLM, etc.), parameter count if known.

- [ ] **Step 4: Write "What's missing / where evidence is weak"**

Read the auto-generated mention block on the page. Look for patterns:
- Is most usage off-the-shelf (no fine-tuning/improvement)?
- Are baselines inconsistent across the posters?
- Are there modalities/diseases the corpus doesn't cover?
- Is reuse vs novel-pretraining the split?

Write 3-5 bullets, each one a real observation grounded in the mention list.

- [ ] **Step 5: Write the Takeaway paragraph**

One paragraph (3-5 sentences). The bar: would a reader who already read the upstream paper still get value here? If the takeaway is just "this is a good model" — too thin. Aim at: "the AACR 2026 corpus shows X about how this tool is being adopted in the wild, which the upstream paper doesn't tell you."

- [ ] **Step 6: Re-run the build to refresh mention blocks**

```bash
cd /Users/lzhang34/Desktop/AACR && python scripts/build_site.py && mkdocs build --strict
```

Expected: prose is preserved; mention blocks re-rendered cleanly. Spot-check 2-3 dossier pages in the local server.

- [ ] **Step 7: Commit per cluster of tools**

Group by family for review-ability. Commit pathology FMs together, single-cell FMs together, etc.

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add docs/topics/bioinfo-tools/tools/chief.md docs/topics/bioinfo-tools/tools/uni.md docs/topics/bioinfo-tools/tools/conch.md docs/topics/bioinfo-tools/tools/pathchat.md docs/topics/bioinfo-tools/tools/virchow.md docs/topics/bioinfo-tools/tools/prov-gigapath.md
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
content: pathology FM dossiers (CHIEF, UNI, CONCH, PathChat, Virchow, Prov-GigaPath)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

Repeat for `sc-fm`, `spatial`, `perturbation`, `protein` clusters.

---

## Task 10: Wire dossiers into the nav

**Files:**
- Modify: `mkdocs.yml`

- [ ] **Step 1: Update the Bioinfo nav block**

In `mkdocs.yml`, replace the existing Bioinfo block:

```yaml
- Bioinfo / Comp Bio / AI Methods:
  - Overview: topics/bioinfo-tools/index.md
  - Landscape: topics/bioinfo-tools/landscape.md
  - Synthesis — FM pathology traction: topics/bioinfo-tools/synthesis-fm-pathology-traction.md
```

with:

```yaml
- Bioinfo / Comp Bio / AI Methods:
  - Overview: topics/bioinfo-tools/index.md
  - Landscape: topics/bioinfo-tools/landscape.md
  - Synthesis — FM pathology traction: topics/bioinfo-tools/synthesis-fm-pathology-traction.md
  - Tools:
    - Index: topics/bioinfo-tools/tools/index.md
    # Surviving tool list (alphabetical within family clusters).
    # Update this list after running --survey if the survivor set changes.
    - CHIEF: topics/bioinfo-tools/tools/chief.md
    - CONCH: topics/bioinfo-tools/tools/conch.md
    - PathChat: topics/bioinfo-tools/tools/pathchat.md
    - Prov-GigaPath: topics/bioinfo-tools/tools/prov-gigapath.md
    - UNI / UNI2: topics/bioinfo-tools/tools/uni.md
    - Virchow / Virchow2: topics/bioinfo-tools/tools/virchow.md
    - Cell2Sentence: topics/bioinfo-tools/tools/cell2sentence.md
    - Geneformer: topics/bioinfo-tools/tools/geneformer.md
    - Nicheformer: topics/bioinfo-tools/tools/nicheformer.md
    - scFoundation: topics/bioinfo-tools/tools/scfoundation.md
    - scGPT: topics/bioinfo-tools/tools/scgpt.md
    - UCE: topics/bioinfo-tools/tools/uce.md
    - Cell2Location: topics/bioinfo-tools/tools/cell2location.md
    - Tangram: topics/bioinfo-tools/tools/tangram.md
    # Drop entries here for any slug that didn't survive the gate.
```

(Remove rows for any tool that did NOT survive in Task 5. Add rows for any survivor that isn't listed here.)

- [ ] **Step 2: Build with `--strict` to verify all referenced pages exist**

```bash
cd /Users/lzhang34/Desktop/AACR && python scripts/build_site.py && mkdocs build --strict
```

Expected: zero warnings. If `mkdocs build --strict` complains about a missing page, the nav references a tool that didn't survive — remove it. If it complains about an orphan page, the survivor isn't in the nav — add it.

- [ ] **Step 3: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add mkdocs.yml
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
nav: add Tools sub-section under bioinfo-tools

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 11: One-paragraph link from the bioinfo overview

**Files:**
- Modify: `docs/topics/bioinfo-tools/index.md`

- [ ] **Step 1: Read the file and find the right insertion point**

```bash
cd /Users/lzhang34/Desktop/AACR && head -40 docs/topics/bioinfo-tools/index.md
```

Identify a natural break — typically after the topic-intro paragraph and before the per-section breakdown.

- [ ] **Step 2: Add the linking paragraph**

Insert (Edit tool, exact strings):

```markdown
## Tool dossiers

Some of the named tools below — CHIEF, scGPT, Geneformer, UCE, etc. — have dedicated reference dossiers covering every corpus mention plus what the evidence is missing. See **[Tools index](tools/index.md)** for the full sortable matrix.
```

- [ ] **Step 3: Build and verify**

```bash
cd /Users/lzhang34/Desktop/AACR && mkdocs build --strict
```

Expected: zero warnings, link resolves.

- [ ] **Step 4: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add docs/topics/bioinfo-tools/index.md
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
content: link from bioinfo overview to tools index

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 12: Cross-topic linking pass (manual)

**Files:**
- Modify: `docs/topics/bioinfo-tools/landscape.md`
- Modify: `docs/topics/bioinfo-tools/synthesis-fm-pathology-traction.md`
- Modify: `docs/topics/virtual-cells/landscape.md`
- Modify: `docs/topics/agentic-ai/landscape.md`
- Modify: `docs/topics/single-cell-spatial-omics/landscape.md`

For each landscape/synthesis page, every first-mention of a surviving tool becomes a markdown link to its dossier. Subsequent mentions in the same paragraph remain plain text (avoids link clutter).

- [ ] **Step 1: For each cross-topic page, list tools to link**

For each `landscape.md` and synthesis page in the modified list, run:

```bash
cd /Users/lzhang34/Desktop/AACR
for f in docs/topics/bioinfo-tools/landscape.md docs/topics/bioinfo-tools/synthesis-fm-pathology-traction.md docs/topics/virtual-cells/landscape.md docs/topics/agentic-ai/landscape.md docs/topics/single-cell-spatial-omics/landscape.md; do
  echo "=== $f ==="
  grep -nE "(CHIEF|UNI|CONCH|PathChat|Virchow|Prov-GigaPath|scGPT|Geneformer|UCE|scFoundation|Nicheformer|Cell2Sentence|Tangram|Cell2Location)" "$f" | head -20
done
```

This shows the candidate link sites.

- [ ] **Step 2: Replace first occurrence in each page with a link**

Use the Edit tool, one-shot per first occurrence. Compute the relative path:

- From `topics/bioinfo-tools/landscape.md` → `tools/<slug>.md`
- From `topics/bioinfo-tools/synthesis-fm-pathology-traction.md` → `tools/<slug>.md`
- From any other topic landscape → `../bioinfo-tools/tools/<slug>.md`

Example edit on `docs/topics/virtual-cells/landscape.md`:

```
old: scGPT (Hu et al. 2024) is a transformer
new: [scGPT](../bioinfo-tools/tools/scgpt.md) (Hu et al. 2024) is a transformer
```

- [ ] **Step 3: Build with `--strict` to verify all relative links resolve**

```bash
cd /Users/lzhang34/Desktop/AACR && mkdocs build --strict 2>&1 | tail -30
```

Expected: no `WARNING - Doc file ... contains an unrecognized relative link` messages.

- [ ] **Step 4: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add docs/topics/
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
content: cross-topic links from landscape pages to tool dossiers

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 13: Final build, push, and verify on the deployed site

**Files:**
- None (deploy + verify)

- [ ] **Step 1: Final clean build**

```bash
cd /Users/lzhang34/Desktop/AACR
rm -rf site/
python scripts/build_site.py && mkdocs build --strict
```

Expected: clean build, `site/` populated, no warnings.

- [ ] **Step 2: Push to origin**

```bash
cd /Users/lzhang34/Desktop/AACR && git push origin main
```

Cloudflare Pages auto-builds from `main`. Wait ~2 min.

- [ ] **Step 3: Verify on the production alias**

Visit `https://aacr-2026.pages.dev/topics/bioinfo-tools/tools/` (Basic Auth: `aacr` / `$SITE_PASSWORD`).

Smoke checklist:
- Matrix renders with rows.
- Sorting on `Posters` (default desc) works.
- Filter on `Family` works.
- Clicking a tool name opens its dossier page.
- Each dossier shows: filled metadata header, prose, mention block with poster + session links.
- Cross-topic link from e.g. `topics/virtual-cells/landscape.md` resolves to the matching dossier.
- Hypothes.is annotation toolbar appears on dossier pages (right edge).

- [ ] **Step 4: If any smoke check fails, fix and re-push**

Don't merge a partial result. Re-run the local strict build first; only push when local is clean.

- [ ] **Step 5: Update the README to mention the new layer**

In `/Users/lzhang34/Desktop/AACR/README.md`, under the "Interactive site" section, add one bullet:

```
- Per-tool dossiers under `Bioinfo / Comp Bio / AI Methods → Tools` for each FM/method with ≥3 corpus mentions, plus a sortable comparison matrix.
```

Commit + push.

```bash
cd /Users/lzhang34/Desktop/AACR
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" add README.md
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "$(cat <<'EOF'
docs: README note about tool dossiers + matrix

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
git push origin main
```

---

## Out-of-scope / explicit non-tasks

- No tests for the prose-authoring tasks (Task 9). That's editorial work, not code.
- No CI for the build script. The existing repo doesn't have CI; adding it is its own project.
- No automated cross-topic linker. Manual is correct for ~30-40 link decisions.
- No fixture corpus for tests. Tests run against the real on-disk JSONLs/transcripts (read-only); they're integration tests not unit tests, but for this scale that's fine.

## Success criteria (from spec)

1. ✅ `mkdocs build --strict` produces `tools/` section under bioinfo-tools without errors → Task 8 + Task 10.
2. ✅ Each surviving tool has dossier with filled header, auto mentions, hand-written `What's missing` + `Takeaway` → Task 7 (auto) + Task 9 (prose).
3. ✅ Tools index renders matrix with sort/filter → Task 8.
4. ✅ Cross-topic landscape pages link to dossiers → Task 12.
5. ✅ Re-running the build never overwrites prose → Task 6 (`inject_mentions_block` preserves text outside markers).
6. ✅ Sub-threshold tools logged for the absences list → Task 5 + Task 7.
