"""Ejercicio 01: Clase BankAccount.

Implementa una clase `BankAccount` con:

- `__init__(self, owner: str, initial_balance: float = 0.0)`
- Atributo `owner` público.
- Saldo encapsulado en `_balance`, expuesto como **propiedad de solo lectura**
  `balance`.
- Método `deposit(amount: float) -> None`. Si `amount` <= 0 lanza `ValueError`.
- Método `withdraw(amount: float) -> None`. Si `amount` <= 0 lanza
  `ValueError`; si excede el saldo, lanza `ValueError("Saldo insuficiente")`.
- `__repr__` que muestre el owner y el saldo con 2 decimales.

Ejemplo:

>>> acc = BankAccount("David", 1000)
>>> acc.deposit(500)
>>> acc.withdraw(200)
>>> acc.balance
1300.0
"""


class BankAccount:
    """Cuenta bancaria con saldo encapsulado."""

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        # TODO: implementar
        raise NotImplementedError
