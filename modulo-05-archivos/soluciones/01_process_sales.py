"""Solución del ejercicio 01: Procesador de CSV de ventas."""

import csv
from pathlib import Path


def process_sales(filepath: Path) -> dict[str, float]:
    """Devuelve {producto: total_vendido} a partir de un CSV de ventas."""
    totales: dict[str, float] = {}
    with open(filepath, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            producto = row["product"]
            importe = float(row["quantity"]) * float(row["price"])
            totales[producto] = totales.get(producto, 0.0) + importe
    return totales


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(process_sales(Path(sys.argv[1])))
