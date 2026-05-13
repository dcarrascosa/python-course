"""Solución del ejercicio 01: Clase BankAccount."""


class BankAccount:
    """Cuenta bancaria con saldo encapsulado."""

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
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


if __name__ == "__main__":
    acc = BankAccount("David", 1000.0)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc)
