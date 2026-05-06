# Example CLAUDE.md snippet

Copy this into your `~/.claude/CLAUDE.md` (global) or `<project>/CLAUDE.md` to instruct Claude Code on when to delegate to the openrouter MCP worker.

Without an instruction like this, Claude knows the tools exist but defaults to doing tasks itself. Adding this directive shifts the default toward delegation for bounded, mechanical work.

---

## Offload mechanical tasks to the OpenRouter MCP worker

The `openrouter` MCP server is available system-wide. Use it to conserve context budget and reduce cost on tasks where Claude's full capability is overkill.

**Use `mcp__openrouter__worker`** for bounded, mechanical tasks where the answer pattern is clear:
- Classification / categorization (filenames, tickets, logs, notes)
- Extraction (TODOs, names, dates, structured fields from messy text)
- Format conversion (text → JSON, CSV, table; reshape between formats)
- Summarization that you will review anyway
- Template population
- Pattern-copy refactors where the transformation is obvious

**Use `mcp__openrouter__advisor`** when you want a second opinion or independent reasoning on a consequential call:
- Architectural tradeoffs ("build vs buy", "approach A vs B")
- Sanity-check on a non-obvious decision before committing to it
- Ambiguity where you're not confident
- Set `effort` to `medium` (faster, cheaper) or `max` (default, most thorough)

**Don't use either for:**
- Tasks that require reading the codebase or running tools — the worker can't do that, you'd just be paraphrasing what you already know
- Final user-facing prose, security decisions, or anything where being wrong has real cost (`worker` only — `advisor` is fine for these)
- Tasks small enough that the round-trip latency exceeds the time to just do it

Treat worker/advisor output as candidate text to review, not a finished answer. The user reviews your output; you review the MCP output.
