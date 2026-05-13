"""Ejercicio 03: Dataclass con validación.

Implementa `Employee` como `@dataclass` con tres campos:

- `name: str`
- `salary: float`
- `department: str`

En `__post_init__` valida que `salary > 0`; si no, lanza `ValueError` con un
mensaje que incluya el salario inválido.

Implementa `__lt__` para que los empleados puedan ordenarse por salario con
`sorted(...)`.

Ejemplo:

>>> emps = [Employee("Ana", 45000, "Eng"), Employee("Bob", 38000, "Sales")]
>>> [e.name for e in sorted(emps)]
['Bob', 'Ana']
"""

from dataclasses import dataclass


@dataclass
class Employee:
    """Empleado con salario y departamento."""

    name: str
    salary: float
    department: str

    def __post_init__(self) -> None:
        # TODO: validar que salary > 0
        raise NotImplementedError

    def __lt__(self, other: "Employee") -> bool:
        # TODO: comparar por salario
        raise NotImplementedError
