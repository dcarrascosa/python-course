"""Solución del ejercicio 03: Patrón producer / consumer con `asyncio.Queue`."""

import asyncio

import httpx

NUM_WORKERS = 3


async def producer(queue: asyncio.Queue, urls: list[str]) -> None:
    """Encola las URLs y un sentinel por consumer."""
    for url in urls:
        await queue.put(url)
    for _ in range(NUM_WORKERS):
        await queue.put(None)


async def consumer(queue: asyncio.Queue, worker_id: int, results: list) -> None:
    """Consume URLs hasta encontrar el sentinel None."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        while True:
            url = await queue.get()
            if url is None:
                queue.task_done()
                break
            try:
                resp = await client.get(url)
                results.append({"url": url, "status": resp.status_code})
                print(f"Worker {worker_id}: {url} -> {resp.status_code}")
            except Exception as exc:
                results.append({"url": url, "error": str(exc)})
            finally:
                queue.task_done()


async def main_producer_consumer() -> list:
    """Orquesta producer + 3 consumers sobre 10 URLs."""
    urls = ["https://httpbin.org/get"] * 10
    queue: asyncio.Queue = asyncio.Queue(maxsize=5)
    results: list = []
    workers = [asyncio.create_task(consumer(queue, i, results)) for i in range(NUM_WORKERS)]
    producer_task = asyncio.create_task(producer(queue, urls))
    await asyncio.gather(producer_task, *workers)
    return results


if __name__ == "__main__":
    print(asyncio.run(main_producer_consumer()))
