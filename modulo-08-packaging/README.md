# Módulo 08 — Packaging, Entornos y Deploy

## Objetivos

- Gestionar dependencias con `uv` (alternativa moderna a pip/poetry)
- Empaquetar un proyecto Python para distribución
- Desplegar una API FastAPI en producción (Railway, Docker)
- Configurar CI/CD con GitHub Actions

---

## 1. Gestión de dependencias — NuGet vs uv/pip

```bash
# .NET — NuGet
dotnet add package Newtonsoft.Json
dotnet restore
```

```bash
# Python moderno con uv (recomendado — 10-100x más rápido que pip)
curl -LsSf https://astral.sh/uv/install.sh | sh

uv init myproject        # equivalente a dotnet new
uv add fastapi httpx      # equivalente a dotnet add package
uv add --dev pytest ruff  # dependencias de desarrollo
uv sync                   # equivalente a dotnet restore
uv run python main.py     # ejecutar con entorno gestionado
```

### pyproject.toml — el .csproj de Python

```toml
[project]
name = "taskflow-api"
version = "0.1.0"
description = "API de gestión de tareas"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115",
    "uvicorn[standard]>=0.32",
    "httpx>=0.28",
    "pydantic>=2.10",
    "sqlalchemy>=2.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=8",
    "pytest-asyncio>=0.24",
    "ruff>=0.8",
    "mypy>=1.13",
]

[tool.ruff.lint]
select = ["E", "F", "I", "UP"]

[tool.mypy]
strict = true
```

---

## 2. Estructura de un proyecto Python de producción

```
taskflow-api/
├── pyproject.toml
├── uv.lock                  # equivalente a packages.lock.json
├── .env                     # nunca en git
├── .env.example
├── Dockerfile
├── src/
│   └── taskflow/
│       ├── __init__.py
│       ├── main.py          # FastAPI app
│       ├── config.py        # Settings con pydantic-settings
│       ├── models/
│       ├── routers/
│       └── services/
└── tests/
    ├── conftest.py
    └── test_*.py
```

---

## 3. Variables de entorno — appsettings.json vs pydantic-settings

```csharp
// C# — IConfiguration
builder.Services.Configure<AppSettings>(builder.Configuration.GetSection("App"));
```

```python
# Python — pydantic-settings
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str
    secret_key: str
    debug: bool = False
    allowed_origins: list[str] = ["http://localhost:3000"]
    max_connections: int = 10

settings = Settings()  # carga automáticamente de .env y variables de entorno
print(settings.database_url)
```

---

## 4. Docker

```dockerfile
# Dockerfile — multi-stage para imagen mínima
FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

FROM python:3.12-slim
WORKDIR /app

COPY --from=builder /app/.venv ./.venv
COPY src/ ./src/

ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000

CMD ["uvicorn", "taskflow.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t taskflow-api .
docker run -p 8000:8000 --env-file .env taskflow-api
```

---

## 5. Deploy en Railway

```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

Railway detecta automáticamente proyectos Python con `pyproject.toml`. Configura las variables de entorno desde el dashboard.

| Azure App Service | Railway |
|-------------------|---------|
| App Settings | Variables de entorno |
| Deployment Center | GitHub integration |
| Scale out | Replicas |
| Log stream | Logs en tiempo real |

---

## 6. CI/CD con GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v4
        with:
          version: "latest"

      - name: Set up Python
        run: uv python install 3.12

      - name: Install dependencies
        run: uv sync --frozen

      - name: Lint
        run: uv run ruff check src tests

      - name: Type check
        run: uv run mypy src

      - name: Test
        run: uv run pytest --cov=src --cov-fail-under=80

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: railwayapp/railway-deploy@v1  # deploy automático si tests pasan
        with:
          railway-token: ${{ secrets.RAILWAY_TOKEN }}
```

---

## 7. Linting y type checking — equivalente a Roslyn Analyzers

```bash
# Ruff — linter y formatter ultrarrápido (reemplaza flake8 + black + isort)
uv run ruff check src      # lint
uv run ruff format src     # format

# Mypy — type checker estático
uv run mypy src

# Ejecutar todo
uv run ruff check src && uv run mypy src && uv run pytest
```

---

## Ejercicios

### Ejercicio 1 — Proyecto con uv

Crea un proyecto nuevo con `uv init`. Añade `fastapi`, `uvicorn` y `httpx` como dependencias. Añade `pytest` y `ruff` como dependencias de desarrollo. Configura `ruff` en `pyproject.toml`.

### Ejercicio 2 — Dockerfile optimizado

Crea un Dockerfile multi-stage para la API de TaskFlow. Verifica que la imagen final pese menos de 200 MB. Añade un healthcheck endpoint `/health` en FastAPI.

### Ejercicio 3 — Pipeline completo

Configura un workflow de GitHub Actions que: lint con ruff → type check con mypy → tests con pytest (min 80% cobertura) → build Docker → deploy a Railway solo en pushes a `main`.

---

## Proyecto TaskFlow — versión final

Al completar el curso tienes:
- API FastAPI con autenticación JWT
- CRUD completo de tareas con SQLAlchemy
- Tests con >80% de cobertura
- Linting y type checking configurados
- Docker image optimizada
- Deploy automático a Railway con GitHub Actions
