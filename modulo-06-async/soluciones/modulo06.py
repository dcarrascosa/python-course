# Soluciones Módulo 06 — Async/Await

import asyncio
import httpx


# Ejercicio 1 — Fetch concurrente
async def fetch_prices(symbols: list[str]) -> dict[str, float]:
    base = "https://query1.finance.yahoo.com/v8/finance/chart/"
    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [
            client.get(f"{base}{symbol}", params={"interval": "1d", "range": "1d"})
            for symbol in symbols
        ]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
    prices = {}
    for symbol, resp in zip(symbols, responses):
        if isinstance(resp, Exception):
            prices[symbol] = -1.0
        else:
            try:
                data = resp.json()
                prices[symbol] = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
            except Exception:
                prices[symbol] = -1.0
    return prices


# Ejercicio 2 — Rate limiter con Semaphore
async def fetch_with_limit(urls: list[str], max_concurrent: int = 5) -> list[str]:
    semaphore = asyncio.Semaphore(max_concurrent)

    async def fetch_one(client: httpx.AsyncClient, url: str) -> str:
        async with semaphore:
            resp = await client.get(url)
            return resp.text

    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [fetch_one(client, url) for url in urls]
        return await asyncio.gather(*tasks)


# Ejercicio 3 — Producer / Consumer
async def producer(queue: asyncio.Queue, urls: list[str]) -> None:
    for url in urls:
        await queue.put(url)
    # señal de fin
    for _ in range(3):  # un sentinel por consumer
        await queue.put(None)


async def consumer(queue: asyncio.Queue, worker_id: int, results: list) -> None:
    async with httpx.AsyncClient(timeout=10.0) as client:
        while True:
            url = await queue.get()
            if url is None:
                break
            try:
                resp = await client.get(url)
                results.append({"url": url, "status": resp.status_code})
                print(f"Worker {worker_id}: {url} -> {resp.status_code}")
            except Exception as e:
                results.append({"url": url, "error": str(e)})
            finally:
                queue.task_done()


async def main_producer_consumer():
    urls = ["https://httpbin.org/get"] * 10
    queue: asyncio.Queue = asyncio.Queue(maxsize=5)
    results: list = []
    workers = [asyncio.create_task(consumer(queue, i, results)) for i in range(3)]
    await producer(queue, urls)
    await asyncio.gather(*workers)
    return results
