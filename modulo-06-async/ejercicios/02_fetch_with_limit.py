"""Ejercicio 02: Rate limiter async con `Semaphore`.

Implementa `fetch_with_limit(urls, max_concurrent=5)` que descarga el texto
de cada URL, pero garantiza que **nunca haya más de `max_concurrent`
peticiones en vuelo a la vez**.

Usa `asyncio.Semaphore` para regular la concurrencia y `httpx.AsyncClient`
con timeout de 10 segundos.

El orden del resultado debe coincidir con el orden de las URLs de entrada.

Pista: define una función interna `fetch_one(client, url)` que adquiera el
semáforo antes de hacer la petición.

Ejemplo:

>>> textos = await fetch_with_limit(["https://httpbin.org/get"] * 20, max_concurrent=3)
>>> len(textos)
20
"""

import asyncio  # noqa: F401


async def fetch_with_limit(urls: list[str], max_concurrent: int = 5) -> list[str]:
    """Descarga las URLs con un máximo de peticiones simultáneas."""
    # TODO: implementar
    raise NotImplementedError
