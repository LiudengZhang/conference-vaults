# GalaxyMCP

**Model Context Protocol bridge for Galaxy** — an MCP server that exposes Galaxy's tools, workflows, histories, and datasets to any MCP-aware AI client (Claude Desktop, IDE assistants, custom agents). Turns a Galaxy instance into a first-class context source for AI assistants, with conversational analyses materialising as fully reproducible Galaxy histories.

- **Authors:** Dannon Baker, Junhao Qiu, Jeremy Goecks, Mike Schatz
- **Galaxy tool / platform:** [galaxyproject/galaxy-mcp](https://github.com/galaxyproject/galaxy-mcp)
- **Source:** [github.com/galaxyproject/galaxy-mcp](https://github.com/galaxyproject/galaxy-mcp)
- **Documentation / training:** [server README](https://github.com/galaxyproject/galaxy-mcp/blob/main/mcp-server-galaxy-py/README.md)
- **Status at GBCC2025:** oral talk on an MCP server for Galaxy

## Talk at GBCC2025

- **Speakers:** Dannon Baker, Junhao Qiu, Jeremy Goecks, Mike Schatz
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 1, Grace Auditorium (chair: Sehyun Oh)
- **Talk title:** "Introducing GalaxyMCP: Integrating AI Assistants with Galaxy Through the Model Context Protocol"
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

GalaxyMCP is a Python MCP server (FastMCP + BioBlend) that exposes Galaxy operations — tool search, workflow invocation, history/dataset access, result retrieval — as MCP tools. An AI assistant connects to a Galaxy instance, then accepts human-language instructions and translates them into BioBlend API calls, leaving behind the same auditable Galaxy history a hand-driven session would. Where GAIA is a complete agent product, GalaxyMCP is the substrate: any MCP client (Claude Desktop, Cursor, custom agents) can drive Galaxy through it.

## How it works

**Core idea.** A FastMCP-based Python server wraps BioBlend (the official Python client for the Galaxy REST API) and re-exposes Galaxy operations as MCP tools that any MCP-aware client can call. The server is the protocol adapter; BioBlend does the actual REST work.

**Inputs / outputs.** Input is a Galaxy connection (URL + API key, or OAuth-issued temporary key) plus MCP tool calls from a client. Output is JSON-shaped results — search hits, tool descriptors, history/dataset metadata, workflow invocation IDs — flowing back to the AI client over MCP.

**Key innovation.** Roughly 21 specialized MCP tools across five functional groups — tool management (search / view / execute), workflow integration (including pulls from the Interactive Workflow Composer), history operations, dataset and file management, and server info — turning a full Galaxy instance into a first-class MCP context source rather than a single ad-hoc tool.

**Parameters / API surface worth knowing.**
- Transport: stdio (default, local) or streamable HTTP with optional OAuth (remote / browser clients).
- Auth: API key via environment variables, or OAuth flow that exchanges credentials for a temporary Galaxy API key.
- Quickstart: `uvx galaxy-mcp` (stdio) or `uvx galaxy-mcp --transport streamable-http --host 0.0.0.0 --port 8000` (HTTP).
- Configuration: register the server in `claude_desktop_config.json` with `GALAXY_URL` and `GALAXY_API_KEY` env vars.

**Canonical example.** From the README: configure the server in Claude Desktop, then ask the model something like "give a summary with my histories" — Claude calls the MCP `list_histories` tool, which calls BioBlend, which calls the Galaxy REST API, and the result flows back into the chat as a human-readable summary.

## Where it fits in the corpus

- **AACR 2026:** axis = agentic AI; the protocol-layer story complements GAIA's product-layer one
- **GAIA** ([entry](gaia.md)) — sister talk, same authors, same session
- **EuroBioC 2025:** no direct equivalent (Bioconductor side has no MCP server yet — gap worth flagging)
- **Nextflow Summit 2026:** parallel to "AI control of Nextflow pipelines" discussions

## Notes

MCP is Anthropic's open protocol for tool/context exchange between AI assistants and external systems. GalaxyMCP makes Galaxy itself an MCP server, joining the broader MCP ecosystem (filesystem, GitHub, databases, etc.). Strategically the more durable of the two GBCC2025 AI talks — protocol bets tend to outlive specific agent products.
