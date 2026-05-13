"""Ejercicio 02: Endpoint de healthcheck en FastAPI.

Implementa una mini-app FastAPI con dos endpoints:

- `GET /` devuelve `{"message": "TaskFlow API", "docs": "/docs"}`.
- `GET /health` devuelve un modelo `HealthResponse` con:
  - `status: str` siempre `"ok"`.
  - `uptime_seconds: float` (segundos desde el arranque, 2 decimales).
  - `version: str` igual a `"0.1.0"`.

Pistas:

- Guarda el momento de arranque en una constante de módulo (`START_TIME`).
- Define `HealthResponse` como `pydantic.BaseModel`.
- Decora el endpoint con `response_model=HealthResponse` para validar la
  salida.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TaskFlow API", version="0.1.0")


class HealthResponse(BaseModel):
    """Respuesta del endpoint /health."""

    # TODO: definir los campos


@app.get("/")
async def root() -> dict:
    # TODO: implementar
    raise NotImplementedError


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    # TODO: implementar
    raise NotImplementedError
