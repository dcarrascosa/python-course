"""Solución del ejercicio 02: Mock de servicio externo."""

from unittest.mock import MagicMock, patch

import httpx
import pytest


class WeatherService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://api.weather.example.com"

    def get_temperature(self, city: str) -> float:
        resp = httpx.get(
            f"{self.base_url}/current",
            params={"q": city, "key": self.api_key},
        )
        resp.raise_for_status()
        return resp.json()["temp_c"]


def test_get_temperature_success() -> None:
    service = WeatherService(api_key="test")
    mock_response = MagicMock()
    mock_response.json.return_value = {"temp_c": 22.5}
    mock_response.raise_for_status.return_value = None

    with patch("httpx.get", return_value=mock_response) as mock_get:
        temp = service.get_temperature("Madrid")

    assert temp == 22.5
    mock_get.assert_called_once_with(
        f"{service.base_url}/current",
        params={"q": "Madrid", "key": "test"},
    )


def test_get_temperature_api_error() -> None:
    service = WeatherService(api_key="test")
    error = httpx.HTTPStatusError(
        "Not Found",
        request=MagicMock(),
        response=MagicMock(status_code=404),
    )

    with patch("httpx.get", side_effect=error) as mock_get:
        with pytest.raises(httpx.HTTPStatusError):
            service.get_temperature("CiudadFalsa")

    mock_get.assert_called_once_with(
        f"{service.base_url}/current",
        params={"q": "CiudadFalsa", "key": "test"},
    )
