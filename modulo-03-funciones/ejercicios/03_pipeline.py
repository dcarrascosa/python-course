"""Ejercicio 03: Pipeline de funciones.

Implementa `pipeline(*funciones)` que recibe varias funciones de un solo
argumento y devuelve una nueva función que las aplica en orden, pasando el
resultado de cada una a la siguiente.

Si no se pasa ninguna función, el pipeline debe ser la identidad: devolver
el valor recibido tal cual.

Ejemplos:

>>> doblar = lambda n: n * 2
>>> sumar_uno = lambda n: n + 1
>>> a_str = lambda n: str(n)
>>> p = pipeline(doblar, sumar_uno, a_str)
>>> p(3)
'7'
>>> pipeline()("hola")
'hola'
"""

from collections.abc import Callable
from typing import Any


def pipeline(*funciones: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Devuelve una función que aplica `funciones` en cadena."""
    # TODO: implementar
    raise NotImplementedError
