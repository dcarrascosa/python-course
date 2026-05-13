"""Ejercicio 02: Generador infinito de Fibonacci.

Implementa una **función generadora** `fibonacci` que produce la secuencia
de Fibonacci de forma infinita: 0, 1, 1, 2, 3, 5, 8, 13...

Como es infinita, el consumidor decide cuándo parar usando
`itertools.islice` o un break.

Ejemplos:

>>> from itertools import islice
>>> list(islice(fibonacci(), 7))
[0, 1, 1, 2, 3, 5, 8]
"""

from collections.abc import Iterator


def fibonacci() -> Iterator[int]:
    """Genera números de Fibonacci de forma infinita."""
    # TODO: implementar usando yield
    raise NotImplementedError
