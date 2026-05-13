"""Ejercicio 02: Config manager basado en JSON.

Implementa la clase `Config` que envuelve un fichero JSON:

- `Config(filepath)` carga el contenido. Si el fichero no existe, lanza
  `FileNotFoundError` con un mensaje que incluya la ruta.
- `config["clave"]` (vía `__getitem__`) devuelve el valor. Si la clave no
  existe, lanza `KeyError` con un mensaje que incluya el nombre del fichero.
- `config["clave"] = valor` (vía `__setitem__`) actualiza el valor en memoria.
- `config.save()` persiste el estado actual al fichero con `indent=2` y
  `ensure_ascii=False`.

El JSON se trata siempre como un objeto raíz (`dict`).
"""

from pathlib import Path
from typing import Any


class Config:
    """Gestor de configuración respaldado por un fichero JSON."""

    def __init__(self, filepath: str | Path) -> None:
        # TODO: implementar
        raise NotImplementedError

    def __getitem__(self, key: str) -> Any:
        # TODO: implementar
        raise NotImplementedError

    def __setitem__(self, key: str, value: Any) -> None:
        # TODO: implementar
        raise NotImplementedError

    def save(self) -> None:
        """Persiste el estado actual al fichero."""
        # TODO: implementar
        raise NotImplementedError
