"""Solución del ejercicio 02: Config manager basado en JSON."""

import json
from pathlib import Path
from typing import Any


class Config:
    """Gestor de configuración respaldado por un fichero JSON."""

    def __init__(self, filepath: str | Path) -> None:
        self._path = Path(filepath)
        if not self._path.exists():
            raise FileNotFoundError(f"Config no encontrada: {self._path}")
        with open(self._path, encoding="utf-8") as f:
            self._data: dict[str, Any] = json.load(f)

    def __getitem__(self, key: str) -> Any:
        if key not in self._data:
            raise KeyError(f"Clave {key!r} no existe en {self._path.name}")
        return self._data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._data[key] = value

    def save(self) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2, ensure_ascii=False)
