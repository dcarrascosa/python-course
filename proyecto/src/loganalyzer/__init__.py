"""loganalyzer — CLI de análisis de logs.

Proyecto hilo del curso "Python para Devs C#".
"""

from loganalyzer.filters import filter_by_level, filter_by_pattern
from loganalyzer.parser import LogEntry, parse_file, parse_line
from loganalyzer.reporter import Summary, format_summary, summarize

__version__ = "0.1.0"

__all__ = [
    "LogEntry",
    "Summary",
    "filter_by_level",
    "filter_by_pattern",
    "format_summary",
    "parse_file",
    "parse_line",
    "summarize",
]
