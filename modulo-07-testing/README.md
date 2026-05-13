# Módulo 07 — Testing con pytest

## Objetivos

- Escribir tests con pytest y compararlos con xUnit/NUnit
- Usar fixtures como equivalente a los setup/teardown de C#
- Implementar mocks con `unittest.mock`
- Medir cobertura con `pytest-cov`

---

## 1. Setup — xUnit vs pytest

```bash
# Instalar
pip install pytest pytest-cov pytest-asyncio
```

Estructura de proyecto:
```
project/
  src/
    myapp/
      models.py
      services.py
  tests/
    conftest.py        # fixtures compartidas — equivalente a fixtures de xUnit
    test_models.py
    test_services.py
  pyproject.toml
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"

[tool.coverage.run]
source = ["src"]
```

---

## 2. Tests básicos

```csharp
// xUnit
public class ProductTests
{
    [Fact]
    public void Discount_AppliesCorrectly()
    {
        var product = new Product("Teclado", 100.0m);
        Assert.Equal(90.0m, product.DiscountedPrice(10));
    }

    [Theory]
    [InlineData(0, 100.0)]
    [InlineData(10, 90.0)]
    [InlineData(100, 0.0)]
    public void Discount_Theory(int percent, decimal expected)
    {
        var product = new Product("Test", 100.0m);
        Assert.Equal(expected, product.DiscountedPrice(percent));
    }
}
```

```python
# pytest
from myapp.models import Product
import pytest

def test_discount_applies_correctly():
    product = Product("Teclado", 100.0)
    assert product.discounted_price(10) == 90.0

# @pytest.mark.parametrize equivale a [Theory][InlineData]
@pytest.mark.parametrize("percent,expected", [
    (0,   100.0),
    (10,   90.0),
    (100,   0.0),
])
def test_discount_parametrized(percent: int, expected: float):
    product = Product("Test", 100.0)
    assert product.discounted_price(percent) == expected

def test_negative_price_raises():
    with pytest.raises(ValueError, match="negativo"):
        Product("X", -5.0)
```

---

## 3. Fixtures — equivalente a constructores de test y IClassFixture

```csharp
// xUnit — constructor como setup
public class OrderTests : IDisposable
{
    private readonly AppDbContext _db;
    public OrderTests() { _db = new AppDbContext(InMemoryOptions()); }
    public void Dispose() => _db.Dispose();
}
```

```python
# pytest fixtures — en conftest.py o en el mismo fichero
import pytest
from myapp.database import create_test_db, drop_test_db
from myapp.models import User, Task

@pytest.fixture
def sample_user() -> User:
    return User(name="David", email="david@test.com")

@pytest.fixture
def sample_task(sample_user: User) -> Task:  # fixtures pueden depender de otras
    return Task(title="Test task", user=sample_user)

@pytest.fixture(scope="module")  # se crea una vez por módulo — como IClassFixture
def db_session():
    session = create_test_db()
    yield session              # código post-yield = teardown
    drop_test_db(session)

def test_task_belongs_to_user(sample_task: Task, sample_user: User):
    assert sample_task.user == sample_user
```

---

## 4. Mocks — equivalente a Moq

```csharp
// C# — Moq
var mockRepo = new Mock<ITaskRepository>();
mockRepo.Setup(r => r.GetAll()).Returns(new List<Task> { task1 });
var service = new TaskService(mockRepo.Object);
```

```python
from unittest.mock import MagicMock, patch, AsyncMock
from myapp.services import TaskService
from myapp.repositories import TaskRepository

def test_service_returns_tasks():
    mock_repo = MagicMock(spec=TaskRepository)  # spec = type safety
    mock_repo.get_all.return_value = [{"id": 1, "title": "Test"}]

    service = TaskService(repo=mock_repo)
    tasks = service.get_all_tasks()

    assert len(tasks) == 1
    mock_repo.get_all.assert_called_once()

# Mockear con patch (para imports directos)
def test_with_patch():
    with patch("myapp.services.send_email") as mock_email:
        mock_email.return_value = True
        service = TaskService()
        service.create_task("Nueva tarea")
        mock_email.assert_called_once()

# Mocks async
async def test_async_service():
    mock_client = AsyncMock()
    mock_client.get.return_value.json.return_value = {"data": []}
    result = await fetch_tasks(client=mock_client)
    assert result == []
```

---

## 5. Tests async

```python
import pytest

@pytest.mark.asyncio  # o asyncio_mode = "auto" en pyproject.toml
async def test_async_endpoint():
    from httpx import AsyncClient
    from myapp.main import app  # FastAPI app

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

---

## 6. Cobertura

```bash
# Ejecutar con cobertura
pytest --cov=src --cov-report=term-missing --cov-report=html

# Ver reporte en htmlcov/index.html
```

```bash
# Fallar si cobertura < 80%
pytest --cov=src --cov-fail-under=80
```

---

## Aportación al proyecto hilo

En este módulo blindamos el `loganalyzer` con una batería de tests con
pytest: fixtures para logs sintéticos, parametrización de los parsers y
mocks para los accesos a I/O. El objetivo es alcanzar cobertura razonable
sobre el código del paquete.

---

## ✅ Ejercicios

> Excepción a la convención del curso: aquí los ficheros se llaman
> `test_<nombre>.py` (sin prefijo numérico) para que pytest los descubra
> automáticamente.

| # | Fichero | Enunciado breve |
|---|---------|-----------------|
| 01 | [`ejercicios/test_product.py`](./ejercicios/test_product.py) | Fixture + `parametrize` + `pytest.raises` sobre `Product`. |
| 02 | [`ejercicios/test_weather_service.py`](./ejercicios/test_weather_service.py) | Mockear `httpx.get` con `unittest.mock.patch`. |

Cada fichero incluye el código bajo test y el enunciado en el docstring.
Ejecuta tus tests con:

```bash
pytest modulo-07-testing/ejercicios/
```

Cuando termines, contrasta con [`soluciones/`](./soluciones/).
