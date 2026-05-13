# Ejemplo: FastAPI app con healthcheck para ejercicio 2

from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(title="TaskFlow API", version="0.1.0")

START_TIME = time.time()


class HealthResponse(BaseModel):
    status: str
    uptime_seconds: float
    version: str


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        uptime_seconds=round(time.time() - START_TIME, 2),
        version="0.1.0",
    )


@app.get("/")
async def root() -> dict:
    return {"message": "TaskFlow API", "docs": "/docs"}
