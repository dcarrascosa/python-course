"""Solución del ejercicio 01: Fixtures y parametrize sobre `Product`."""

import pytest


class Product:
    def __init__(self, name: str, price: float) -> None:
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


@pytest.mark.parametrize(
    ("percent", "factor"),
    [
        (0, 1.00),
        (10, 0.90),
        (25, 0.75),
        (50, 0.50),
        (100, 0.00),
    ],
)
def test_discounted_price(
    product_catalog: list[Product], percent: float, factor: float
) -> None:
    for product in product_catalog:
        expected = product.price * factor
        assert product.discounted_price(percent) == pytest.approx(expected)


def test_negative_price_raises() -> None:
    with pytest.raises(ValueError, match="negativo"):
        Product("X", -5.0)
