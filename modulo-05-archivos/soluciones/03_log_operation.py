"""Solución del ejercicio 03: Context manager `log_operation`."""

import datetime
import traceback
from collections.abc import Generator
from contextlib import contextmanager


@contextmanager
def log_operation(name: str) -> Generator[None, None, None]:
    """Loguea el inicio, fin y excepciones de una operación."""
    print(f"[START] {name}")
    try:
        yield
    except Exception as exc:
        print(f"[ERROR] {name}: {exc}")
        with open("errors.log", "a", encoding="utf-8") as log:
            log.write(f"{datetime.datetime.now()} | {name} | {exc}\n")
            log.write(traceback.format_exc())
        raise
    else:
        print(f"[OK]    {name}")


if __name__ == "__main__":
    with log_operation("carga de datos"):
        data = {"key": "value"}
        print(f"Datos cargados: {data}")
