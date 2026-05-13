"""Parser de líneas de log al modelo `LogEntry`."""

from __future__ import annotations

import re
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# Formato esperado: "YYYY-MM-DD HH:MM:SS LEVEL [source] mensaje"
_LINE_RE = re.compile(
    r"^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+"
    r"\[(?P<source>[^\]]+)\]\s+"
    r"(?P<message>.*)$"
)


@dataclass(frozen=True)
class LogEntry:
    """Entrada de log normalizada."""

    timestamp: datetime
    level: str
    source: str
    message: str


def parse_line(linea: str) -> LogEntry | None:
    """Parsea una línea. Devuelve `None` si no encaja con el formato."""
    m = _LINE_RE.match(linea.rstrip("\n"))
    if not m:
        return None
    return LogEntry(
        timestamp=datetime.fromisoformat(m["ts"]),
        level=m["level"],
        source=m["source"],
        message=m["message"],
    )


def parse_file(ruta: Path) -> Iterator[LogEntry]:
    """Itera por las entradas de un fichero, descartando líneas inválidas.

    Lectura lazy: cada línea se procesa al vuelo, sin cargar el fichero entero
    en memoria.
    """
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            entry = parse_line(linea)
            if entry is not None:
                yield entry
