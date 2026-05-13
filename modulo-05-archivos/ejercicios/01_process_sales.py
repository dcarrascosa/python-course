"""Ejercicio 01: Procesador de CSV de ventas.

Implementa `process_sales(filepath)` que lee un CSV con columnas
`product`, `quantity` y `price` y devuelve un diccionario con el total
vendido (`quantity * price`) por producto.

Si el mismo producto aparece varias veces, los importes se suman.

Usa `csv.DictReader` y abre el fichero con `with`, codificación UTF-8 y
`newline=""`.

Ejemplo de fichero:

```csv
product,quantity,price
Teclado,2,29.50
Ratón,3,10.00
Teclado,1,29.50
```

>>> process_sales(Path("ventas.csv"))
{'Teclado': 88.5, 'Ratón': 30.0}
"""

from pathlib import Path


def process_sales(filepath: Path) -> dict[str, float]:
    """Devuelve {producto: total_vendido} a partir de un CSV de ventas."""
    # TODO: implementar
    raise NotImplementedError
