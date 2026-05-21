# SuperWebsearch MCP

SuperWebsearch MCP は、6551 SuperWebsearch API を利用したライブウェブ検索ツールを
提供します。

公開 MCP パッケージには上流モデルゲートウェイキーは含まれていません。ユーザーは
https://www.newsliquid.com/mcp から 6551 API トークンを取得して認証を行い、
MCP サーバーがそのトークンをホストされたバックエンドに送信し、バックエンドが
プロンプト組み立て、レート制限、上流モデルアクセスを処理します。

## インストール

```bash
uv sync
```

または他のプロジェクトにインストール：

```bash
uv pip install -e .
```

## 認証

https://www.newsliquid.com/mcp でトークンを取得し、以下を設定してください：

```bash
export SUPERWEBSEARCH_TOKEN="<your-token>"
```

オプション設定：

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

## ツール

`SuperWebsearch(query)`

パラメータ：

- `query`：検索、URL 読み取り、ファクトチェック、ソース発見、またはリサーチリクエストの
  完全なクエリ。

レスポンス：

ツールはバックエンドからの JSON 文字列を返します。成功レスポンスの形式：

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

## レート制限

サーバーリソースが限られているため、各 API トークンは 10 分に 1 回のみ呼び出し可能です。

## セキュリティレビューチェックリスト

本パッケージ：

- 設定された `SUPERWEBSEARCH_API_BASE` にのみ接続します。
- `SUPERWEBSEARCH_TOKEN` またはローカルの `config.json` から 6551 トークンを読み取ります。
- 上流ゲートウェイ API キーを含みません。
- シェルコマンドの実行、ユーザーファイルの書き込み、ブラウザプロファイルの読み取りは行いません。
