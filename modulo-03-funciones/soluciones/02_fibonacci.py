"""Solución del ejercicio 02: Generador infinito de Fibonacci."""

from collections.abc import Iterator


def fibonacci() -> Iterator[int]:
    """Genera números de Fibonacci de forma infinita."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    from itertools import islice
    print(list(islice(fibonacci(), 10)))
