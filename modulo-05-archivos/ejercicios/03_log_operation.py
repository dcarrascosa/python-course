"""Ejercicio 03: Context manager `log_operation`.

Implementa un context manager `log_operation(name)` que:

- Al entrar, imprime `"[START] {name}"`.
- Al salir sin excepción, imprime `"[OK]    {name}"`.
- Al salir con excepción, imprime `"[ERROR] {name}: {excepción}"`, escribe
  la traza completa en un fichero `errors.log` (modo append, UTF-8) con la
  fecha actual, y **vuelve a lanzar** la excepción.

Implementación recomendada: `@contextlib.contextmanager` sobre una función
generadora.

Ejemplo de uso:

>>> with log_operation("carga de datos"):
...     do_stuff()
"""

from collections.abc import Generator
from contextlib import contextmanager


@contextmanager
def log_operation(name: str) -> Generator[None, None, None]:
    """Loguea el inicio, fin y excepciones de una operación."""
    # TODO: implementar
    raise NotImplementedError
