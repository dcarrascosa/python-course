# Soluciones Módulo 07 — Testing con pytest
# Nota: estos ejemplos se ejecutan con pytest, no directamente

import pytest
from unittest.mock import MagicMock, patch


# --- Ejercicio 1 ---
class Product:
    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError(f"Precio negativo: {price}")
        self.name = name
        self.price = price

    def discounted_price(self, percent: float) -> float:
        return self.price * (1 - percent / 100)


@pytest.fixture
def product_catalog() -> list[Product]:
    return [
        Product("Teclado", 89.99),
        Product("Ratón", 29.99),
        Product("Monitor", 349.00),
        Product("Auriculares", 79.99),
        Product("Webcam", 59.99),
    ]


@pytest.mark.parametrize("percent,factor", [
    (0,   1.00),
    (10,  0.90),
    (25,  0.75),
    (50,  0.50),
    (100, 0.00),
])
def test_discounted_price(product_catalog: list[Product], percent: float, factor: float):
    for product in product_catalog:
        expected = round(product.price * factor, 10)
        assert product.discounted_price(percent) == pytest.approx(expected)


# --- Ejercicio 2 ---
class WeatherService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.weather.example.com"

    def get_temperature(self, city: str) -> float:
        import httpx
        resp = httpx.get(f"{self.base_url}/current", params={"q": city, "key": self.api_key})
        resp.raise_for_status()
        return resp.json()["temp_c"]


def test_get_temperature_success():
    service = WeatherService(api_key="test")
    mock_response = MagicMock()
    mock_response.json.return_value = {"temp_c": 22.5}
    mock_response.raise_for_status.return_value = None

    with patch("httpx.get", return_value=mock_response):
        temp = service.get_temperature("Madrid")

    assert temp == 22.5


def test_get_temperature_api_error():
    import httpx
    service = WeatherService(api_key="test")

    with patch("httpx.get", side_effect=httpx.HTTPStatusError(
        "Not Found", request=MagicMock(), response=MagicMock(status_code=404)
    )):
        with pytest.raises(httpx.HTTPStatusError):
            service.get_temperature("CiudadFalsa")
