# SuperWebsearch MCP

SuperWebsearch MCP는 6551 SuperWebsearch API를 기반으로 한 실시간 웹 검색 도구를
제공합니다.

공개 MCP 패키지에는 업스트림 모델 게이트웨이 키가 포함되어 있지 않습니다. 사용자는
https://www.newsliquid.com/mcp 에서 6551 API 토큰을 발급받아 인증하며, MCP 서버가
해당 토큰을 호스팅된 백엔드로 전송하고, 백엔드에서 프롬프트 조립, 속도 제한 및
업스트림 모델 접근을 처리합니다.

## 설치

```bash
uv sync
```

또는 다른 프로젝트에 설치:

```bash
uv pip install -e .
```

## 인증

https://www.newsliquid.com/mcp 에서 토큰을 발급받고 다음을 설정하세요:

```bash
export SUPERWEBSEARCH_TOKEN="<your-token>"
```

선택 설정:

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

## 도구

`SuperWebsearch(query)`

매개변수:

- `query`: 검색, URL 읽기, 팩트체크, 출처 발견 또는 리서치 요청의 전체 쿼리.

응답:

도구는 백엔드에서 JSON 문자열을 반환합니다. 성공 응답 형식:

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

## 속도 제한

서버 자원이 제한되어 있어 각 API 토큰은 10분에 한 번만 호출할 수 있습니다.

## 보안 검토 체크리스트

본 패키지:

- 설정된 `SUPERWEBSEARCH_API_BASE`에만 연결합니다.
- `SUPERWEBSEARCH_TOKEN` 또는 로컬 `config.json`에서 6551 토큰을 읽습니다.
- 업스트림 게이트웨이 API 키를 포함하지 않습니다.
- 셸 명령 실행, 사용자 파일 쓰기, 브라우저 프로필 읽기를 수행하지 않습니다.
