from datetime import datetime

from loganalyzer.parser import LogEntry
from loganalyzer.reporter import Summary, format_summary, summarize


def _entry(level: str, source: str, message: str) -> LogEntry:
    return LogEntry(
        timestamp=datetime(2026, 5, 13, 12, 0, 0),
        level=level,
        source=source,
        message=message,
    )


def test_summarize_counts_total_levels_sources_and_top_messages() -> None:
    entries = [
        _entry("INFO", "app", "starting"),
        _entry("INFO", "app", "starting"),
        _entry("ERROR", "db", "timeout"),
    ]
    summary = summarize(entries)
    assert summary.total == 3
    assert summary.by_level == {"INFO": 2, "ERROR": 1}
    assert summary.by_source == {"app": 2, "db": 1}
    assert summary.top_messages[0] == ("starting", 2)


def test_summarize_empty() -> None:
    summary = summarize([])
    assert summary == Summary(total=0, by_level={}, by_source={}, top_messages=[])


def test_format_summary_includes_total_and_levels() -> None:
    summary = Summary(
        total=2,
        by_level={"INFO": 2},
        by_source={"x": 2},
        top_messages=[("hola", 2)],
    )
    rendered = format_summary(summary)
    assert "Total de entradas: 2" in rendered
    assert "INFO" in rendered
    assert "hola" in rendered
