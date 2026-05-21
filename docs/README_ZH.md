# SuperWebsearch MCP

SuperWebsearch MCP 提供一个由 6551 SuperWebsearch API 驱动的实时网页搜索工具。

公开的 MCP 包不包含上游模型网关密钥。用户通过 https://www.newsliquid.com/mcp 获取
6551 API 令牌进行认证，MCP 服务器将该令牌发送到托管后端，后端负责提示词组装、
速率限制和上游模型访问。

## 安装

```bash
uv sync
```

或安装到其他项目：

```bash
uv pip install -e .
```

## 认证

在 https://www.newsliquid.com/mcp 获取令牌并设置：

```bash
export SUPERWEBSEARCH_TOKEN="<your-token>"
```

可选设置：

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

## 工具

`SuperWebsearch(query)`

参数：

- `query`：完整的搜索、URL 读取、事实核查、来源发现或研究请求。

响应：

工具返回后端的 JSON 字符串。成功响应格式：

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

## 频率限制

由于服务器资源有限，每个 API 令牌每 10 分钟只能调用一次。

## 安全审查清单

本包：

- 仅连接到配置的 `SUPERWEBSEARCH_API_BASE`。
- 从 `SUPERWEBSEARCH_TOKEN` 或本地 `config.json` 读取 6551 令牌。
- 不包含上游网关 API 密钥。
- 不执行 shell 命令、不写入用户文件、不读取浏览器配置。
