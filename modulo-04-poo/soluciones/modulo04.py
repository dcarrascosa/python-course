# Soluciones Módulo 04 — POO

# Ejercicio 1
class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("El depósito debe ser positivo")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if amount > self._balance:
            raise ValueError("Saldo insuficiente")
        self._balance -= amount

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"


acc = BankAccount("David", 1000.0)
acc.deposit(500)
acc.withdraw(200)
print(acc)  # BankAccount(owner='David', balance=1300.00)


# Ejercicio 2
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def fuel_cost_per_km(self) -> float:
        ...

    def __repr__(self) -> str:
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Vehicle):
    def __init__(self, make: str, model: str, year: int, kwh_per_100km: float):
        super().__init__(make, model, year)
        self.kwh_per_100km = kwh_per_100km
        self.price_per_kwh = 0.15

    def fuel_cost_per_km(self) -> float:
        return (self.kwh_per_100km / 100) * self.price_per_kwh


class GasCar(Vehicle):
    def __init__(self, make: str, model: str, year: int, liters_per_100km: float):
        super().__init__(make, model, year)
        self.liters_per_100km = liters_per_100km
        self.price_per_liter = 1.70

    def fuel_cost_per_km(self) -> float:
        return (self.liters_per_100km / 100) * self.price_per_liter


tesla = ElectricCar("Tesla", "Model 3", 2024, 14.0)
fiat = GasCar("Fiat", "Punto", 2018, 6.5)
print(f"{tesla}: {tesla.fuel_cost_per_km():.4f} €/km")
print(f"{fiat}: {fiat.fuel_cost_per_km():.4f} €/km")


# Ejercicio 3
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: float
    department: str

    def __post_init__(self):
        if self.salary <= 0:
            raise ValueError(f"Salario inválido: {self.salary}")

    def __lt__(self, other: "Employee") -> bool:
        return self.salary < other.salary


employees = [
    Employee("Ana", 45000, "Engineering"),
    Employee("Carlos", 38000, "Marketing"),
    Employee("Eva", 52000, "Engineering"),
]
for e in sorted(employees):
    print(f"{e.name}: {e.salary:,.0f}€")
