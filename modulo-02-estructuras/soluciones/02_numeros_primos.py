"""Solución del ejercicio 02: Números primos hasta un límite."""


def _es_primo(n: int) -> bool:
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def numeros_primos(limite: int) -> list[int]:
    """Devuelve los primos entre 2 y limite (inclusive)."""
    if limite < 2:
        return []
    return [n for n in range(2, limite + 1) if _es_primo(n)]


if __name__ == "__main__":
    print(numeros_primos(20))
