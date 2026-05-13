"""Ejercicio 01: Decorador de cache simple.

Implementa un decorador `cache_simple` que memoriza el resultado de una
función a partir de sus argumentos posicionales. No uses
`functools.lru_cache`; la gracia es implementarlo a mano.

Restricciones:

- Solo cachea argumentos posicionales (puedes asumir que no se pasan kwargs).
- La cache vive en el closure del decorador, una por función decorada.
- Usa `functools.wraps` para preservar metadatos.

Ejemplo de uso:

>>> @cache_simple
... def cuadrado(n):
...     return n * n
>>> cuadrado(5)
25
>>> cuadrado(5)  # esta vez sale de la cache, sin recalcular
25
"""

from collections.abc import Callable
from typing import Any


def cache_simple(func: Callable[..., Any]) -> Callable[..., Any]:
    """Devuelve una versión de `func` que cachea por argumentos posicionales."""
    # TODO: implementar
    raise NotImplementedError
