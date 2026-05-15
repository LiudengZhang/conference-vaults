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


def test_match_aliases_word_boundary():
    from build_site import match_aliases
    text = "We applied scGPT and SC-GPT variants alongside Geneformer."
    aliases = ["scGPT", "SC-GPT"]
    assert match_aliases(text, aliases) is True


def test_match_aliases_negative_inside_word():
    from build_site import match_aliases
    # 'UCE' should not match inside 'reduces' or 'produces'
    text = "This reduces noise and produces clean embeddings."
    assert match_aliases(text, ["UCE"]) is False


def test_match_aliases_case_insensitive():
    from build_site import match_aliases
    assert match_aliases("we used cell2location to deconvolve", ["Cell2Location"]) is True


def test_load_corpus_dedups_posters():
    from build_site import load_corpus
    from conferences import CONFERENCES
    aacr_conf = next(c for c in CONFERENCES if c["slug"] == "aacr-2026")
    corpus = load_corpus(aacr_conf)
    # poster Ids must be unique
    poster_ids = [p["Id"] for p in corpus["posters"]]
    assert len(poster_ids) == len(set(poster_ids))
    # session keys must be unique stems
    assert len(corpus["sessions"]) == len(set(s["stem"] for s in corpus["sessions"]))
    # corpus has substantial content
    assert len(corpus["posters"]) > 1500
    assert len(corpus["sessions"]) >= 20
    # every poster carries the topic-tracking fields
    for p in corpus["posters"]:
        assert "_topic" in p and isinstance(p["_topic"], str)
        assert "_topics" in p and isinstance(p["_topics"], list) and p["_topics"]
    # at least one poster surfaces in multiple topics (cross-topic dedup actually happened)
    assert any(len(p["_topics"]) > 1 for p in corpus["posters"])


def test_scan_mentions_returns_structured_hits():
    from build_site import load_corpus, scan_mentions
    from conferences import CONFERENCES
    aacr_conf = next(c for c in CONFERENCES if c["slug"] == "aacr-2026")
    corpus = load_corpus(aacr_conf)
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
    assert "**LB123**" in block
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
    assert "TODO" in out
