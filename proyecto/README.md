# loganalyzer — proyecto hilo del curso

CLI de análisis de logs que recorre el curso de Python para devs C#. Cada
módulo añade una funcionalidad encima de la anterior, hasta entregar un
paquete instalable con tests, lint y CI.

## Instalación local

```bash
# Desde la raíz del repo
cd proyecto
uv sync --group dev
uv run loganalyzer samples/app.log
```

## Uso

```bash
# Resumen básico
uv run loganalyzer samples/app.log

# Filtrar por nivel mínimo
uv run loganalyzer samples/app.log --level ERROR

# Filtrar por regex en el mensaje
uv run loganalyzer samples/app.log --match "postgres"

# Top N mensajes más frecuentes
uv run loganalyzer samples/app.log --top 3
```

Ejemplo de salida:

```
Total de entradas: 10

Por nivel:
  DEBUG      1
  ERROR      3
  INFO       4
  WARNING    2

Por fuente:
  app.config           1
  app.main             2
  auth                 1
  db.pool              2
  http.client          1
  http.server          3

Top 5 mensajes:
  (  2) conexión a postgres rechazada
  (  2) GET /health 200
  ...
```

## Estructura

```
proyecto/
├── pyproject.toml          # paquete instalable + deps + ruff + pytest
├── src/loganalyzer/
│   ├── __init__.py         # API pública
│   ├── cli.py              # entry point con argparse
│   ├── parser.py           # LogEntry + parse_line + parse_file (lazy)
│   ├── filters.py          # filter_by_level, filter_by_pattern
│   └── reporter.py         # Summary + summarize + format_summary
├── tests/
│   ├── test_parser.py
│   ├── test_filters.py
│   ├── test_reporter.py
│   └── test_cli.py
└── samples/
    └── app.log
```

## Roadmap por módulo

Cada módulo del curso añade una pieza:

| Módulo | Aportación |
|--------|------------|
| 01 Fundamentos | Esqueleto del CLI con `argparse` y `if __name__ == "__main__"`. |
| 02 Estructuras | `LogEntry` como dataclass, agregaciones con `Counter` y `defaultdict`. |
| 03 Funciones | Lectura lazy (`yield` en `parse_file`), decorador `validar_fichero`. |
| 04 POO | `LogEntry` como dataclass frozen, jerarquía de fuentes (futuro). |
| 05 Archivos | Lectura de múltiples formatos texto/JSON/CSV (futuro) con `pathlib`. |
| 06 Async | Análisis en paralelo de varios ficheros con `asyncio` + `Semaphore` (futuro). |
| 07 Testing | Batería completa con `pytest`, fixtures con `tmp_path`, `capsys`. |
| 08 Packaging | Paquete instalable con `uv` + `hatchling`, entry point `loganalyzer`. |

Los puntos marcados "futuro" son extensiones naturales que el alumno puede
practicar siguiendo el patrón.

## Ejecutar los tests

```bash
cd proyecto
uv run pytest -v
```
