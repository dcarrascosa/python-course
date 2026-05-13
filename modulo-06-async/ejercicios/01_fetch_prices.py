"""Ejercicio 01: Fetch concurrente de precios.

Implementa `fetch_prices(symbols)` que para cada símbolo consulta su precio
actual en una API y los devuelve agrupados en un dict. Todas las peticiones
deben lanzarse **concurrentemente** con `asyncio.gather`, no secuencialmente.

Usa `httpx.AsyncClient` con timeout de 10 segundos. Para cada símbolo que
falle (excepción o respuesta inválida), devuelve `-1.0` como precio.

Endpoint sugerido:

```
https://query1.finance.yahoo.com/v8/finance/chart/<symbol>?interval=1d&range=1d
```

El precio se obtiene de `data["chart"]["result"][0]["meta"]["regularMarketPrice"]`.

Ejemplo:

>>> await fetch_prices(["AAPL", "MSFT"])
{'AAPL': 175.43, 'MSFT': 412.10}
"""

import asyncio  # noqa: F401  (lo necesitarás en la implementación)


async def fetch_prices(symbols: list[str]) -> dict[str, float]:
    """Devuelve {símbolo: precio} obteniendo todos en paralelo."""
    # TODO: implementar con httpx.AsyncClient + asyncio.gather
    raise NotImplementedError
