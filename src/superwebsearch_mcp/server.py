"""Entry point for the SuperWebsearch MCP server."""

from __future__ import annotations

from superwebsearch_mcp.app import mcp

import superwebsearch_mcp.tools  # noqa: F401


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()

