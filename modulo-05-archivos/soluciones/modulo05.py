# Soluciones Módulo 05 — Archivos, Excepciones y Contextos

import csv
import json
from contextlib import contextmanager
from pathlib import Path
from typing import Generator


# Ejercicio 1
def process_sales(filepath: Path) -> dict[str, float]:
    totals: dict[str, float] = {}
    with open(filepath, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            product = row["product"]
            amount = float(row["quantity"]) * float(row["price"])
            totals[product] = totals.get(product, 0.0) + amount
    return totals


# Ejercicio 2
class Config:
    def __init__(self, filepath: str | Path):
        self._path = Path(filepath)
        if not self._path.exists():
            raise FileNotFoundError(f"Config no encontrada: {self._path}")
        with open(self._path, encoding="utf-8") as f:
            self._data: dict = json.load(f)

    def __getitem__(self, key: str):
        if key not in self._data:
            raise KeyError(f"Clave '{key}' no existe en {self._path.name}")
        return self._data[key]

    def __setitem__(self, key: str, value) -> None:
        self._data[key] = value

    def save(self) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2, ensure_ascii=False)


# Ejercicio 3
@contextmanager
def log_operation(name: str) -> Generator[None, None, None]:
    print(f"[START] {name}")
    try:
        yield
        print(f"[OK]    {name}")
    except Exception as e:
        print(f"[ERROR] {name}: {e}")
        with open("errors.log", "a", encoding="utf-8") as log:
            import traceback, datetime
            log.write(f"{datetime.datetime.now()} | {name} | {e}\n")
            log.write(traceback.format_exc())
        raise


with log_operation("carga de datos"):
    data = {"key": "value"}
    print(f"Datos cargados: {data}")
