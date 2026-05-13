"""Solución del ejercicio 02: Rate limiter async con `Semaphore`."""

import asyncio

import httpx


async def fetch_with_limit(urls: list[str], max_concurrent: int = 5) -> list[str]:
    """Descarga las URLs con un máximo de peticiones simultáneas."""
    semaphore = asyncio.Semaphore(max_concurrent)

    async def fetch_one(client: httpx.AsyncClient, url: str) -> str:
        async with semaphore:
            resp = await client.get(url)
            return resp.text

    async with httpx.AsyncClient(timeout=10.0) as client:
        tareas = [fetch_one(client, url) for url in urls]
        return await asyncio.gather(*tareas)


if __name__ == "__main__":
    urls = ["https://httpbin.org/get"] * 20
    textos = asyncio.run(fetch_with_limit(urls, max_concurrent=3))
    print(f"Descargadas {len(textos)} respuestas")
