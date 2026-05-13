"""Ejercicio 01: Fixtures y parametrize sobre `Product`.

La clase `Product` que está más abajo es el código bajo test (te lo damos
hecho). Tu tarea es escribir los tests:

1. **Fixture `product_catalog`** que devuelva una lista de 5 productos
   variados.
2. **Test parametrizado `test_discounted_price`** que verifique que aplicar
   un descuento del 0, 10, 25, 50 y 100 % al precio de cada producto del
   catálogo devuelve el resultado esperado. Usa `pytest.approx`.
3. **Test `test_negative_price_raises`** que verifique que crear un
   `Product` con precio negativo lanza `ValueError` con mensaje que
   contenga "negativo".

Convención del fichero: pytest descubre los `test_*.py` por defecto, por eso
en este módulo no usamos el prefijo numérico de otros módulos.
"""

import pytest  # noqa: F401


class Product:
    """Producto con precio y descuento. **No modifiques esta clase.**"""

    def __init__(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError(f"Precio negativo: {price}")
        self.name = name
        self.price = price

    def discounted_price(self, percent: float) -> float:
        return self.price * (1 - percent / 100)


# TODO: escribe la fixture product_catalog
# TODO: escribe test_discounted_price parametrizado
# TODO: escribe test_negative_price_raises
