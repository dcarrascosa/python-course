"""Solución del ejercicio 01: Decorador de cache simple."""

import functools
from collections.abc import Callable
from typing import Any


def cache_simple(func: Callable[..., Any]) -> Callable[..., Any]:
    """Devuelve una versión de `func` que cachea por argumentos posicionales."""
    cache: dict[tuple[Any, ...], Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


if __name__ == "__main__":
    @cache_simple
    def cuadrado(n: int) -> int:
        print(f"Calculando {n}**2")
        return n * n

    print(cuadrado(5))
    print(cuadrado(5))
