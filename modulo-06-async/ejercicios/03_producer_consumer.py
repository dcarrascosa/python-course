"""Ejercicio 03: Patrón producer / consumer con `asyncio.Queue`.

Implementa el patrón clásico:

- `producer(queue, urls)` encola todas las URLs en `queue` y termina poniendo
  un sentinel `None` por cada consumer activo.
- `consumer(queue, worker_id, results)` consume URLs hasta encontrar el
  sentinel `None`. Para cada URL, hace `GET` con `httpx.AsyncClient` y
  agrega un dict a `results` con `{"url": ..., "status": int}` o
  `{"url": ..., "error": str}` si falla. Llama a `queue.task_done()` en cada
  iteración.
- `main_producer_consumer()` orquesta: `Queue` con `maxsize=5`, 3 consumers
  en paralelo con `create_task`, y un producer con 10 URLs. Devuelve la
  lista `results` al final.

Pista: el número de sentinels que pone el producer debe coincidir con el
número de consumers para que todos terminen.
"""

import asyncio


async def producer(queue: asyncio.Queue, urls: list[str]) -> None:
    """Encola las URLs y un sentinel por consumer."""
    # TODO: implementar
    raise NotImplementedError


async def consumer(queue: asyncio.Queue, worker_id: int, results: list) -> None:
    """Consume URLs hasta encontrar el sentinel None."""
    # TODO: implementar
    raise NotImplementedError


async def main_producer_consumer() -> list:
    """Orquesta producer + 3 consumers sobre 10 URLs."""
    # TODO: implementar
    raise NotImplementedError
