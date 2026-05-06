"""CLI entry points: check, run, advise.

Usage:
    python -m openrouter_mcp check           # validate key, make 1 worker call
    python -m openrouter_mcp run <prompt>     # one-shot worker call
    python -m openrouter_mcp advise <prompt>  # one-shot advisor call
                         [--effort medium|high|max] [--show-reasoning]
"""

import argparse
import os
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="openrouter-mcp",
        description="OpenRouter MCP CLI — smoke-test or one-shot calls.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check", help="Validate API key and make a test call")

    run_parser = sub.add_parser("run", help="One-shot worker call")
    run_parser.add_argument("prompt", help="Task prompt")

    advise_parser = sub.add_parser("advise", help="One-shot advisor call (reasoning)")
    advise_parser.add_argument("prompt", help="Question or problem")
    advise_parser.add_argument(
        "--effort", choices=["medium", "high", "max"], default="max",
    )
    advise_parser.add_argument(
        "--show-reasoning", action="store_true",
        help="Include <reasoning> block from thinking mode in output",
    )

    args = parser.parse_args()

    if args.command == "check":
        _cmd_check()
    elif args.command == "run":
        _cmd_run(args)
    elif args.command == "advise":
        _cmd_advise(args)


def _cmd_check() -> None:
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        print("FAIL: OPENROUTER_API_KEY not set.")
        print("Get a key at https://openrouter.ai/settings/keys")
        sys.exit(2)
    if len(key) < 8:
        print("FAIL: OPENROUTER_API_KEY looks too short.")
        sys.exit(2)
    print(f"Key found ({len(key)} chars). Making test call...", flush=True)

    from openrouter_mcp.server import call_worker
    result = call_worker({"prompt": "Return exactly: ok"})
    print(result)
    print("\nPASS: openrouter-mcp is working.")


def _cmd_run(args: argparse.Namespace) -> None:
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        print("FAIL: OPENROUTER_API_KEY not set.", file=sys.stderr)
        sys.exit(2)

    from openrouter_mcp.server import call_worker
    result = call_worker({"prompt": args.prompt})
    print(result)


def _cmd_advise(args: argparse.Namespace) -> None:
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        print("FAIL: OPENROUTER_API_KEY not set.", file=sys.stderr)
        sys.exit(2)

    from openrouter_mcp.server import call_advisor
    call_args = {
        "prompt": args.prompt,
        "effort": args.effort,
        "system": None,
        "show_reasoning": args.show_reasoning,
    }
    result = call_advisor(call_args)
    print(result)


if __name__ == "__main__":
    main()
