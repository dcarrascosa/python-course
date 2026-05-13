"""Solución del ejercicio 01: Fetch concurrente de precios."""

import asyncio

import httpx


async def fetch_prices(symbols: list[str]) -> dict[str, float]:
    """Devuelve {símbolo: precio} obteniendo todos en paralelo."""
    base = "https://query1.finance.yahoo.com/v8/finance/chart/"
    async with httpx.AsyncClient(timeout=10.0) as client:
        tareas = [
            client.get(f"{base}{symbol}", params={"interval": "1d", "range": "1d"})
            for symbol in symbols
        ]
        respuestas = await asyncio.gather(*tareas, return_exceptions=True)

    precios: dict[str, float] = {}
    for symbol, resp in zip(symbols, respuestas, strict=True):
        if isinstance(resp, Exception):
            precios[symbol] = -1.0
            continue
        try:
            data = resp.json()
            precios[symbol] = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        except Exception:
            precios[symbol] = -1.0
    return precios


if __name__ == "__main__":
    print(asyncio.run(fetch_prices(["AAPL", "MSFT"])))
