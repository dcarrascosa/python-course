from datetime import datetime

import pytest

from loganalyzer.filters import filter_by_level, filter_by_pattern
from loganalyzer.parser import LogEntry


def _entry(level: str = "INFO", message: str = "hola") -> LogEntry:
    return LogEntry(
        timestamp=datetime(2026, 5, 13, 12, 0, 0),
        level=level,
        source="t",
        message=message,
    )


def test_filter_by_level_keeps_equal_or_higher() -> None:
    entries = [_entry("DEBUG"), _entry("INFO"), _entry("WARNING"), _entry("ERROR")]
    result = list(filter_by_level(entries, "WARNING"))
    assert [e.level for e in result] == ["WARNING", "ERROR"]


def test_filter_by_level_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Nivel desconocido"):
        list(filter_by_level([], "BOGUS"))


def test_filter_by_pattern_matches_regex() -> None:
    entries = [
        _entry(message="timeout: 5s"),
        _entry(message="all good"),
        _entry(message="db timeout"),
    ]
    result = list(filter_by_pattern(entries, r"timeout"))
    assert len(result) == 2


def test_filter_by_pattern_empty_when_no_match() -> None:
    entries = [_entry(message="nothing")]
    assert list(filter_by_pattern(entries, r"^xxx")) == []
