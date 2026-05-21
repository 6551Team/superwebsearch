"""FastMCP application instance."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from superwebsearch_mcp.api_client import SuperWebsearchClient

KNOWLEDGE_DIR = Path(__file__).resolve().parent.parent.parent / "knowledge"


INSTRUCTIONS = """\
SuperWebsearch MCP provides a single live web search and URL reading tool backed
by the 6551 SuperWebsearch API.

Use SuperWebsearch when the user needs current facts, public web evidence,
source discovery, URL reading, news/event verification, or concise research
synthesis with links. Put all constraints, date windows, source preferences,
and output format requirements into the query.
"""


@dataclass
class AppContext:
    api: SuperWebsearchClient


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    api = SuperWebsearchClient()
    try:
        yield AppContext(api=api)
    finally:
        await api.close()


mcp = FastMCP(
    "superwebsearch-6551",
    instructions=INSTRUCTIONS,
    lifespan=app_lifespan,
    json_response=True,
)


def _read_knowledge(name: str) -> str:
    path = KNOWLEDGE_DIR / name
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"Knowledge file '{name}' not found."


@mcp.resource("knowledge://guide")
async def knowledge_guide() -> str:
    """Usage guide with authentication, cost, and common workflows."""
    return _read_knowledge("guide.md")
