---
name: superwebsearch
description: "Live public web search and URL reading through the 6551 SuperWebsearch API. Useful for latest facts, source discovery, claim verification, public web research, and evidence-backed summaries."

user-invocable: true
metadata:
  openclaw:
    requires:
      env:
        - SUPERWEBSEARCH_TOKEN
      bins:
        - curl
    primaryEnv: SUPERWEBSEARCH_TOKEN
    install:
      - id: curl
        kind: brew
        formula: curl
        label: curl (HTTP client)
    os:
      - darwin
      - linux
      - win32
  version: 1.0.0
---

# SuperWebsearch Skill

SuperWebsearch is a live public web search and URL reading tool powered by
6551.io.

Get your token: https://www.newsliquid.com/mcp

Base URL: `https://ai.6551.io`

## Authentication

All requests require:

```http
Authorization: Bearer $SUPERWEBSEARCH_TOKEN
```

## Search

```bash
curl -s -X POST "https://ai.6551.io/open/websearch" \
  -H "Authorization: Bearer $SUPERWEBSEARCH_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query":"latest Anthropic Model Context Protocol updates with sources"}'
```

## Request

```json
{
  "query": "Open/read https://example.com and summarize it with source links"
}
```

## Response

```json
{
  "ok": true,
  "answer": "...",
  "sources": ["https://..."],
  "meta": {
    "point_cost": 10
  }
}
```

## Notes

- Put date windows, source requirements, URLs, and output format requirements
  directly into `query`.
- Treat volatile data such as prices, latest posts, and social metrics as a
  timestamped snapshot.
