"""Configuration helpers for SuperWebsearch MCP."""

from __future__ import annotations

import json
import os
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = PROJECT_ROOT / "config.json"


def _load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        return {}
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


_cfg = _load_config()

API_BASE_URL = (
    os.environ.get("SUPERWEBSEARCH_API_BASE")
    or _cfg.get("api_base_url")
    or "https://ai.6551.io"
).rstrip("/")
API_ENDPOINT = os.environ.get("SUPERWEBSEARCH_ENDPOINT") or _cfg.get("endpoint") or "/open/websearch"
API_TOKEN = os.environ.get("SUPERWEBSEARCH_TOKEN") or _cfg.get("api_token") or ""
TIMEOUT_SECONDS = float(os.environ.get("SUPERWEBSEARCH_TIMEOUT_SECONDS", "300"))


def require_token() -> str:
    if not API_TOKEN:
        raise ValueError(
            "SUPERWEBSEARCH_TOKEN is not configured. Get a 6551 API token at "
            "https://www.newsliquid.com/mcp and set SUPERWEBSEARCH_TOKEN."
        )
    return API_TOKEN


def make_serializable(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, dict):
        return {key: make_serializable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [make_serializable(item) for item in value]
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value

