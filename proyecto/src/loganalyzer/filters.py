"""Filtros sobre flujos de `LogEntry`."""

from __future__ import annotations

import re
from collections.abc import Iterable, Iterator

from loganalyzer.parser import LogEntry

_SEVERITY = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50,
}


def filter_by_level(entries: Iterable[LogEntry], min_level: str) -> Iterator[LogEntry]:
    """Devuelve solo las entradas con nivel >= `min_level`.

    Lanza `ValueError` si `min_level` no es uno de los niveles estándar.
    """
    if min_level not in _SEVERITY:
        raise ValueError(f"Nivel desconocido: {min_level!r}")
    minimo = _SEVERITY[min_level]
    for e in entries:
        if _SEVERITY.get(e.level, 0) >= minimo:
            yield e


def filter_by_pattern(entries: Iterable[LogEntry], pattern: str) -> Iterator[LogEntry]:
    """Devuelve solo las entradas cuyo mensaje hace match con el regex."""
    regex = re.compile(pattern)
    for e in entries:
        if regex.search(e.message):
            yield e
