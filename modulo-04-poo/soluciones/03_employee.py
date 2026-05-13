"""Solución del ejercicio 03: Dataclass con validación."""

from dataclasses import dataclass


@dataclass
class Employee:
    """Empleado con salario y departamento."""

    name: str
    salary: float
    department: str

    def __post_init__(self) -> None:
        if self.salary <= 0:
            raise ValueError(f"Salario inválido: {self.salary}")

    def __lt__(self, other: "Employee") -> bool:
        return self.salary < other.salary


if __name__ == "__main__":
    employees = [
        Employee("Ana", 45000, "Engineering"),
        Employee("Carlos", 38000, "Marketing"),
        Employee("Eva", 52000, "Engineering"),
    ]
    for e in sorted(employees):
        print(f"{e.name}: {e.salary:,.0f}€")
