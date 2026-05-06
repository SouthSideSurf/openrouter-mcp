# Contributing

## Issues

Bug reports and feature requests are welcome. Use the GitHub issue templates.

## Pull requests

Keep PRs focused on a single concern. Open an issue first if the change is non-trivial.

## Design principles

- Zero surprise behavior — no telemetry, no phoning home, no hidden state.
- Fail visibly — errors should be clear and actionable.
- One server, two tools — `worker` for bounded mechanical tasks, `advisor` for reasoning. No file ops, no plugins.
- MCP stdio only — no HTTP, no daemon, no database.
- Provider-neutral — the server speaks OpenAI-compatible chat completions, so any OpenRouter model works by changing the constants at the top of `server.py`.
