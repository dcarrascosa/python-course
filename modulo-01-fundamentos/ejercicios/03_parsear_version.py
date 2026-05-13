"""Ejercicio 03: Parsear una versión semántica.

Implementa la función `parsear_version` que dado un string con formato
`"MAJOR.MINOR.PATCH"` devuelve una tupla `(major, minor, patch)` con los
tres enteros.

Reglas:

- Si el formato no es válido (número incorrecto de partes, o alguna parte no
  es un entero), lanza `ValueError`.

Ejemplos:

>>> parsear_version("1.2.3")
(1, 2, 3)
>>> parsear_version("10.0.42")
(10, 0, 42)
"""


def parsear_version(version: str) -> tuple[int, int, int]:
    """Devuelve la tupla (major, minor, patch) de una versión semántica."""
    # TODO: implementar
    raise NotImplementedError
