# Gotchas

## MCP servers start at client launch

If you change MCP configuration or environment variables, restart Claude Code or your MCP client.

## Model IDs do not include the `openrouter/` prefix

When calling OpenRouter's API directly (which this server does), use the bare model ID, e.g. `nvidia/nemotron-3-super-120b-a12b` — not `openrouter/nvidia/...`. The `openrouter/` prefix is only used when *another* provider routes to OpenRouter as a backend.

## The model is not the owner

Worker models are useful for bounded tasks like classification, extraction, and formatting. They should not be the final authority on security, architecture, legal, client-facing, or public communication decisions. Treat output as candidate text to review.
