"""Ejercicio 02: Jerarquía de vehículos.

Define una clase abstracta `Vehicle` con `make`, `model`, `year` y un método
abstracto `fuel_cost_per_km() -> float`. Implementa `__repr__` en la base
para devolver `"YYYY MAKE MODEL"`.

Crea dos subclases concretas:

- `ElectricCar`: añade `kwh_per_100km`. Asume `price_per_kwh = 0.15`.
  `fuel_cost_per_km` devuelve `(kwh_per_100km / 100) * price_per_kwh`.
- `GasCar`: añade `liters_per_100km`. Asume `price_per_liter = 1.70`.
  `fuel_cost_per_km` devuelve `(liters_per_100km / 100) * price_per_liter`.

Usa `abc.ABC` y `@abstractmethod`. Instanciar `Vehicle` directamente debe
lanzar `TypeError`.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Vehículo abstracto con coste por km."""

    def __init__(self, make: str, model: str, year: int) -> None:
        # TODO: implementar
        raise NotImplementedError

    @abstractmethod
    def fuel_cost_per_km(self) -> float:
        """Devuelve el coste de combustible/energía por km en €."""
