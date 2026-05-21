# SuperWebsearch MCP

SuperWebsearch MCP exposes one live web search tool backed by the 6551
SuperWebsearch API.

The public MCP package does not contain the upstream model gateway key. Users
authenticate with a 6551 API token from https://www.newsliquid.com/mcp, the MCP server
sends that token to the hosted backend, and the backend handles prompt assembly,
rate limiting, and upstream model access.

## Install

```bash
uv sync
```

Or install into another project:

```bash
uv pip install -e .
```

## Authentication

Get a token at https://www.newsliquid.com/mcp and set:

```bash
export SUPERWEBSEARCH_TOKEN="<your-token>"
```

Optional settings:

```bash
export SUPERWEBSEARCH_API_BASE="https://ai.6551.io"
export SUPERWEBSEARCH_ENDPOINT="/open/websearch"
```

## Claude Desktop / Claude Code

```json
{
  "mcpServers": {
    "superwebsearch": {
      "command": "uv",
      "args": ["--directory", "/path/to/superwebsearch-mcp", "run", "superwebsearch-mcp"],
      "env": {
        "SUPERWEBSEARCH_TOKEN": "<your-token>"
      }
    }
  }
}
```

## Tool

`SuperWebsearch(query)`

Parameters:

- `query`: full search, URL reading, fact-checking, source discovery, or
  research request.

Response:

The tool returns a JSON string from the backend. A successful response has:

```json
{
  "ok": true,
  "answer": "...",
  "sources": ["https://..."],
  "meta": {
    "point_cost": 10,
    "elapsed_seconds": 12.3
  }
}
```

## Rate Limit

Due to limited server resources, each API token can only be called once every 10 minutes.

## Safety Review Checklist

This package:

- Connects only to the configured `SUPERWEBSEARCH_API_BASE`.
- Reads the 6551 token from `SUPERWEBSEARCH_TOKEN` or local `config.json`.
- Does not contain the upstream gateway API key.
- Does not execute shell commands, write user files, or read browser profiles.
