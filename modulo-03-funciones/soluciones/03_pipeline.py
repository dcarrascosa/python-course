"""Solución del ejercicio 03: Pipeline de funciones."""

from collections.abc import Callable
from typing import Any


def pipeline(*funciones: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Devuelve una función que aplica `funciones` en cadena."""
    def aplicar(valor: Any) -> Any:
        for fn in funciones:
            valor = fn(valor)
        return valor
    return aplicar


if __name__ == "__main__":
    p = pipeline(lambda n: n * 2, lambda n: n + 1, str)
    print(p(3))
