"""CLI entry point for pad_rag."""

import argparse

from pad_rag import __version__

NOT_IMPLEMENTED_MESSAGE = (
    "RAG pipeline is not implemented yet. "
    "This repository currently contains only the lab 1 project foundation."
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pad-rag", description="PAD RAG coursework CLI")
    parser.add_argument("--version", action="version", version=f"pad-rag {__version__}")

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("status", help="Show current implementation status")
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "status":
        print(NOT_IMPLEMENTED_MESSAGE)
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
