"""Punto de entrada CLI del loganalyzer."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Iterable, Iterator
from pathlib import Path

from loganalyzer.filters import filter_by_level, filter_by_pattern
from loganalyzer.parser import LogEntry, parse_file
from loganalyzer.reporter import format_summary, summarize


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="loganalyzer",
        description="Analiza ficheros de log y produce un resumen.",
    )
    parser.add_argument("fichero", type=Path, help="Ruta al fichero de log.")
    parser.add_argument(
        "--level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Filtrar por nivel mínimo (por defecto: sin filtro).",
    )
    parser.add_argument(
        "--match",
        help="Filtrar por regex aplicado al mensaje.",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Cuántos mensajes top mostrar (defecto: 5).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point. Devuelve el exit code."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    if not args.fichero.exists():
        print(f"Fichero no encontrado: {args.fichero}", file=sys.stderr)
        return 1

    entries: Iterable[LogEntry] | Iterator[LogEntry] = parse_file(args.fichero)
    if args.level:
        entries = filter_by_level(entries, args.level)
    if args.match:
        entries = filter_by_pattern(entries, args.match)

    summary = summarize(entries, top_n=args.top)
    print(format_summary(summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
