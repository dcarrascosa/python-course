"""Solución del ejercicio 02: Endpoint de healthcheck en FastAPI."""

import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TaskFlow API", version="0.1.0")

START_TIME = time.time()


class HealthResponse(BaseModel):
    """Respuesta del endpoint /health."""

    status: str
    uptime_seconds: float
    version: str


@app.get("/")
async def root() -> dict:
    return {"message": "TaskFlow API", "docs": "/docs"}


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        uptime_seconds=round(time.time() - START_TIME, 2),
        version="0.1.0",
    )
