"""Tool registrations for SuperWebsearch MCP."""

from __future__ import annotations

import json
from typing import Optional

from mcp.server.fastmcp import Context

from superwebsearch_mcp.app import AppContext, mcp
from superwebsearch_mcp.config import make_serializable


@mcp.tool(
    name="SuperWebsearch",
    annotations={
        "title": "SuperWebsearch",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    },
)
async def superwebsearch(
    query: str,
    max_tokens: Optional[int] = None,
    ctx: Context | None = None,
) -> str:
    """Search or read live public web content through SuperWebsearch.

    Put the full request in `query`: latest facts, URL reading, source
    discovery, fact-checking, public social-post lookup, news, market snapshots,
    or a requested output format. Include URLs, date windows, source
    preferences, and formatting requirements directly in `query`.
    """
    if not query or not query.strip():
        return json.dumps({"ok": False, "error": "query cannot be empty"}, ensure_ascii=False)

    if ctx is None:
        from superwebsearch_mcp.api_client import SuperWebsearchClient

        api = SuperWebsearchClient()
        try:
            result = await api.search(query=query.strip(), max_tokens=max_tokens)
        finally:
            await api.close()
    else:
        app_ctx = ctx.request_context.lifespan_context
        if not isinstance(app_ctx, AppContext):
            return json.dumps({"ok": False, "error": "invalid MCP lifespan context"}, ensure_ascii=False)
        result = await app_ctx.api.search(query=query.strip(), max_tokens=max_tokens)

    return json.dumps(make_serializable(result), ensure_ascii=False, indent=2)
