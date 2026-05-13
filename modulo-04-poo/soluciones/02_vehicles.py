"""Solución del ejercicio 02: Jerarquía de vehículos."""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Vehículo abstracto con coste por km."""

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def fuel_cost_per_km(self) -> float:
        ...

    def __repr__(self) -> str:
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Vehicle):
    """Coche eléctrico."""

    price_per_kwh = 0.15

    def __init__(self, make: str, model: str, year: int, kwh_per_100km: float) -> None:
        super().__init__(make, model, year)
        self.kwh_per_100km = kwh_per_100km

    def fuel_cost_per_km(self) -> float:
        return (self.kwh_per_100km / 100) * self.price_per_kwh


class GasCar(Vehicle):
    """Coche de combustión."""

    price_per_liter = 1.70

    def __init__(self, make: str, model: str, year: int, liters_per_100km: float) -> None:
        super().__init__(make, model, year)
        self.liters_per_100km = liters_per_100km

    def fuel_cost_per_km(self) -> float:
        return (self.liters_per_100km / 100) * self.price_per_liter


if __name__ == "__main__":
    tesla = ElectricCar("Tesla", "Model 3", 2024, 14.0)
    fiat = GasCar("Fiat", "Punto", 2018, 6.5)
    print(f"{tesla}: {tesla.fuel_cost_per_km():.4f} €/km")
    print(f"{fiat}: {fiat.fuel_cost_per_km():.4f} €/km")
