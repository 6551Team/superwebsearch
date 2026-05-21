# SuperWebsearch MCP Usage Guide

SuperWebsearch is a single-search-box tool for current public web research.

## Authentication

Use a 6551 API token from https://6551.io/mcp:

```bash
export SUPERWEBSEARCH_TOKEN="<your-token>"
```

The public MCP sends this token as:

```http
Authorization: Bearer $SUPERWEBSEARCH_TOKEN
```

## Tool

`SuperWebsearch(query)`

Use it for:

- Latest public facts and source discovery.
- Opening and summarizing URLs.
- Fact-checking claims with direct links.
- Public news, market, and social-post lookup.
- Research synthesis where current evidence matters.

## Cost

Hosted SuperWebsearch requests are charged by the 6551 API key system. The
server-side product cost is 10 pts per request.
