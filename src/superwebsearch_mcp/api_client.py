"""HTTP client for the hosted 6551 SuperWebsearch backend."""

from __future__ import annotations

from typing import Any, Optional

import httpx

from superwebsearch_mcp.config import API_BASE_URL, API_ENDPOINT, TIMEOUT_SECONDS, require_token


class SuperWebsearchClient:
    """Async HTTP client for the public SuperWebsearch endpoint."""

    def __init__(
        self,
        base_url: str = API_BASE_URL,
        endpoint: str = API_ENDPOINT,
        token: Optional[str] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"
        self.token = token or require_token()
        self._client: Optional[httpx.AsyncClient] = None

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                timeout=httpx.Timeout(TIMEOUT_SECONDS, connect=30.0),
                headers=self._headers(),
            )
        return self._client

    async def close(self) -> None:
        if self._client and not self._client.is_closed:
            await self._client.aclose()
        self._client = None

    async def search(
        self,
        *,
        query: str,
        max_tokens: Optional[int] = None,
    ) -> dict[str, Any]:
        body: dict[str, Any] = {
            "query": query,
        }
        if max_tokens is not None:
            body["max_tokens"] = max_tokens

        client = await self._get_client()
        response = await client.post(f"{self.base_url}{self.endpoint}", json=body)
        try:
            payload = response.json()
        except ValueError:
            payload = {"ok": False, "error": response.text}

        if response.status_code >= 400:
            return {
                "ok": False,
                "status_code": response.status_code,
                "error": payload.get("error") if isinstance(payload, dict) else str(payload),
                "details": payload,
            }
        return payload
