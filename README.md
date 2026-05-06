# openrouter-mcp

[![MIT License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](pyproject.toml)

Use any OpenRouter model from Claude Code or any MCP-compatible client as a small, cheap supervised worker.

Fork of [arizen-dev/deepseek-mcp](https://github.com/arizen-dev/deepseek-mcp), rewired to use [OpenRouter](https://openrouter.ai) instead of DeepSeek directly.

`openrouter-mcp` is a tiny stdio MCP server with two tools:

```text
worker(prompt, system?)          — fast, non-thinking task execution
advisor(prompt, system?, effort?) — deeper reasoning mode
```

Currently configured to use **Nemotron 3 Super 120B** (`nvidia/nemotron-3-super-120b-a12b`) via OpenRouter. Change the model constants at the top of `server.py` to try any other OpenRouter model.

## Quickstart

### 1. Install

```bash
git clone https://github.com/SouthSideSurf/openrouter-mcp.git
cd openrouter-mcp
pip install -e .
```

### 2. Add your OpenRouter key

Create an API key at https://openrouter.ai/settings/keys, then export it:

```bash
export OPENROUTER_API_KEY="sk-or-..."
```

### 3. Configure for Claude Code (system-wide)

Register the MCP server at user scope so it's available in every project:

```bash
claude mcp add-json --scope user openrouter \
  '{"type":"stdio","command":"openrouter-mcp-server","args":[],"env":{"OPENROUTER_API_KEY":"sk-or-..."}}'
```

(Replace `sk-or-...` with your real key, or substitute `"$OPENROUTER_API_KEY"` if you have it exported.)

Restart Claude Code. The tools will be available as:

```text
mcp__openrouter__worker    — fast task execution
mcp__openrouter__advisor   — reasoning mode
```

## CLI

```bash
# Validate setup
python -m openrouter_mcp check

# One-shot worker call
python -m openrouter_mcp run "Classify: urgent / later — 'Server down in prod'"

# Advisor call with reasoning
python -m openrouter_mcp advise "Should we build or buy analytics?" --effort max
```

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENROUTER_API_KEY` | — | Required. Your OpenRouter API key. |
| `OPENROUTER_BASE_URL` | `https://openrouter.ai/api/v1` | API base URL. |
| `OPENROUTER_MCP_LOG` | (unset) | Set to `1` to log call metadata to `~/.openrouter-mcp/calls.jsonl`. |

## Changing models

Edit `WORKER_MODEL` and `ADVISOR_MODEL` at the top of `src/openrouter_mcp/server.py`. Update the `PRICING` dict to match. Any OpenRouter model works.

## Security notes

- The worker returns text only. It cannot call tools, write files, or access your repo.
- Do not commit API keys.
- Treat model output as untrusted candidate text.

## License

MIT (forked from [arizen-dev/deepseek-mcp](https://github.com/arizen-dev/deepseek-mcp))
