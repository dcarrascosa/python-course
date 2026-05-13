from datetime import datetime

from loganalyzer.parser import LogEntry, parse_line


def test_parse_line_valid() -> None:
    linea = "2026-05-13 21:15:42 INFO [app.main] starting up"
    entry = parse_line(linea)
    assert entry == LogEntry(
        timestamp=datetime(2026, 5, 13, 21, 15, 42),
        level="INFO",
        source="app.main",
        message="starting up",
    )


def test_parse_line_invalid_returns_none() -> None:
    assert parse_line("esto no encaja con el formato") is None


def test_parse_line_strips_trailing_newline() -> None:
    entry = parse_line("2026-05-13 21:15:42 ERROR [db] timeout\n")
    assert entry is not None
    assert entry.message == "timeout"


def test_parse_line_unknown_level_returns_none() -> None:
    assert parse_line("2026-05-13 21:15:42 BOGUS [x] msg") is None
