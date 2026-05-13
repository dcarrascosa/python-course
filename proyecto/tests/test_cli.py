from pathlib import Path

import pytest

from loganalyzer.cli import main


@pytest.fixture
def sample_log(tmp_path: Path) -> Path:
    path = tmp_path / "app.log"
    path.write_text(
        "\n".join([
            "2026-05-13 12:00:00 INFO [app] arrancando",
            "2026-05-13 12:00:01 ERROR [db] conexión perdida",
            "2026-05-13 12:00:02 WARNING [http] respuesta lenta",
            "linea con formato malo",
            "",
        ]),
        encoding="utf-8",
    )
    return path


def test_main_runs_and_prints_summary(
    sample_log: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code = main([str(sample_log)])
    assert exit_code == 0
    output = capsys.readouterr().out
    # 3 válidas, 1 descartada por formato
    assert "Total de entradas: 3" in output


def test_main_filters_by_level(
    sample_log: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code = main([str(sample_log), "--level", "ERROR"])
    assert exit_code == 0
    output = capsys.readouterr().out
    assert "Total de entradas: 1" in output


def test_main_filters_by_match(
    sample_log: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code = main([str(sample_log), "--match", "lenta"])
    assert exit_code == 0
    output = capsys.readouterr().out
    assert "Total de entradas: 1" in output


def test_main_missing_file_returns_error_code(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code = main([str(tmp_path / "no_existe.log")])
    assert exit_code == 1
    assert "no encontrado" in capsys.readouterr().err
