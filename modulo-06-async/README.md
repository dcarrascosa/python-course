# Módulo 06 — Async/Await y Concurrencia

## Objetivos

- Entender el modelo async de Python vs C#
- Usar `asyncio`, `aiohttp` y `httpx` para I/O no bloqueante
- Conocer cuándo usar `threading` vs `multiprocessing` vs `asyncio`

---

## 1. Async/Await — comparativa directa

```csharp
// C# — async/await
public async Task<string> FetchDataAsync(string url)
{
    using var client = new HttpClient();
    return await client.GetStringAsync(url);
}

public async Task RunAsync()
{
    var result = await FetchDataAsync("https://api.example.com/data");
    Console.WriteLine(result);
}
```

```python
import asyncio
import httpx

async def fetch_data(url: str) -> str:
    async with httpx.AsyncClient() as client:  # context manager async
        response = await client.get(url)
        response.raise_for_status()
        return response.text

async def main():
    result = await fetch_data("https://httpbin.org/get")
    print(result)

asyncio.run(main())  # punto de entrada — equivalente a await RunAsync()
```

> **Clave:** En C# el runtime gestiona el threadpool. En Python, `asyncio` usa un único thread con un event loop. Es concurrente pero NO paralelo por defecto.

---

## 2. Tareas concurrentes — Task.WhenAll

```csharp
// C# — ejecutar varias tareas en paralelo
var tasks = urls.Select(url => FetchDataAsync(url));
var results = await Task.WhenAll(tasks);
```

```python
# Python — asyncio.gather equivale a Task.WhenAll
async def fetch_all(urls: list[str]) -> list[str]:
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)  # lanza todas a la vez
        return [r.text for r in responses]

# Con manejo de errores individuales
results = await asyncio.gather(*tasks, return_exceptions=True)
for r in results:
    if isinstance(r, Exception):
        print(f"Error: {r}")
    else:
        print(r)
```

---

## 3. asyncio.timeout — CancellationToken

```csharp
// C#
using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(5));
await FetchDataAsync(url, cts.Token);
```

```python
# Python 3.11+
try:
    async with asyncio.timeout(5.0):  # timeout en segundos
        result = await fetch_data(url)
except TimeoutError:
    print("Timeout al obtener datos")

# Python 3.8+
try:
    result = await asyncio.wait_for(fetch_data(url), timeout=5.0)
except asyncio.TimeoutError:
    print("Timeout")
```

---

## 4. Threading vs Multiprocessing vs Asyncio

| Escenario | C# | Python |
|-----------|----|--------|
| I/O concurrente (HTTP, DB, ficheros) | `async/await` | `asyncio` |
| CPU intensivo | `Task.Run` + threadpool | `multiprocessing` |
| Librerías síncronas en paralelo | `Thread` | `threading` |

```python
import concurrent.futures

# CPU intensivo — multiprocessing
def heavy_computation(n: int) -> int:
    return sum(i * i for i in range(n))

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = list(executor.map(heavy_computation, [10**6, 10**6, 10**6]))

# Librerías síncronas — threading
def fetch_sync(url: str) -> str:
    import requests
    return requests.get(url).text

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(fetch_sync, url) for url in urls]
    results = [f.result() for f in concurrent.futures.as_completed(futures)]
```

---

## 5. Asyncio en FastAPI/contextos web

En FastAPI (o cualquier framework async), los endpoint `async def` corren en el event loop:

```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/weather/{city}")
async def get_weather(city: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://wttr.in/{city}?format=j1")
        return resp.json()

# Si necesitas llamar código síncrono bloqueante desde un endpoint async:
from fastapi.concurrency import run_in_threadpool

@app.get("/sync-work")
async def mixed_endpoint():
    result = await run_in_threadpool(some_blocking_function, arg1, arg2)
    return {"result": result}
```

---

## 6. Async generators y streams

```python
async def paginate_api(base_url: str):
    """Genera resultados de una API paginada."""
    page = 1
    async with httpx.AsyncClient() as client:
        while True:
            resp = await client.get(base_url, params={"page": page})
            data = resp.json()
            if not data["items"]:
                break
            for item in data["items"]:
                yield item  # async generator
            page += 1

async def main():
    async for item in paginate_api("https://api.example.com/tasks"):
        print(item["title"])
```

---

## Ejercicios

### Ejercicio 1 — Fetch concurrente

Escribe una función `fetch_prices(symbols: list[str]) -> dict[str, float]` que consulte una API de precios para cada símbolo de forma concurrente con `asyncio.gather`. Usa `httpx.AsyncClient`.

### Ejercicio 2 — Rate limiter async

Implementa un semáforo async que limite a 5 peticiones simultáneas usando `asyncio.Semaphore`.

### Ejercicio 3 — Producer/Consumer

Implementa el patrón producer/consumer usando `asyncio.Queue`: un producer que encole URLs, y múltiples consumers (workers) que las procesen concurrentemente.

---

## Solución

Ver [`soluciones/modulo06.py`](./soluciones/modulo06.py)
