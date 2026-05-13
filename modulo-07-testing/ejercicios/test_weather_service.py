"""Ejercicio 02: Mock de servicio externo.

`WeatherService` (más abajo) llama a una API HTTP real. Tu tarea es escribir
tests que **mocken la llamada HTTP** para no depender de la red:

1. `test_get_temperature_success`: mockea `httpx.get` para que devuelva un
   `MagicMock` cuyo `.json()` retorne `{"temp_c": 22.5}` y cuyo
   `.raise_for_status()` no haga nada. Verifica que
   `service.get_temperature("Madrid")` devuelve `22.5`.
2. `test_get_temperature_api_error`: mockea `httpx.get` para que lance
   `httpx.HTTPStatusError`. Verifica que se propaga la excepción con
   `pytest.raises`.

Usa `unittest.mock.patch` como context manager.
"""

import pytest  # noqa: F401


class WeatherService:
    """Cliente sencillo de una API meteorológica. **No modifiques esta clase.**"""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://api.weather.example.com"

    def get_temperature(self, city: str) -> float:
        import httpx
        resp = httpx.get(
            f"{self.base_url}/current",
            params={"q": city, "key": self.api_key},
        )
        resp.raise_for_status()
        return resp.json()["temp_c"]


# TODO: escribe test_get_temperature_success usando patch + MagicMock
# TODO: escribe test_get_temperature_api_error usando patch + side_effect
