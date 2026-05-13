"""Generación de resúmenes a partir de `LogEntry`."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass

from loganalyzer.parser import LogEntry


@dataclass(frozen=True)
class Summary:
    """Resumen agregado de un conjunto de entradas."""

    total: int
    by_level: dict[str, int]
    by_source: dict[str, int]
    top_messages: list[tuple[str, int]]


def summarize(entries: Iterable[LogEntry], top_n: int = 5) -> Summary:
    """Calcula el resumen agregado de las entradas."""
    entries_list = list(entries)
    return Summary(
        total=len(entries_list),
        by_level=dict(Counter(e.level for e in entries_list)),
        by_source=dict(Counter(e.source for e in entries_list)),
        top_messages=Counter(e.message for e in entries_list).most_common(top_n),
    )


def format_summary(summary: Summary) -> str:
    """Convierte un `Summary` en texto legible."""
    lineas: list[str] = [
        f"Total de entradas: {summary.total}",
        "",
        "Por nivel:",
    ]
    for lvl, n in sorted(summary.by_level.items()):
        lineas.append(f"  {lvl:<10} {n}")
    lineas.append("")
    lineas.append("Por fuente:")
    for src, n in sorted(summary.by_source.items()):
        lineas.append(f"  {src:<20} {n}")
    if summary.top_messages:
        lineas.append("")
        lineas.append(f"Top {len(summary.top_messages)} mensajes:")
        for msg, n in summary.top_messages:
            preview = msg[:60] + ("…" if len(msg) > 60 else "")
            lineas.append(f"  ({n:>3}) {preview}")
    return "\n".join(lineas)
