"""Solución del ejercicio 03: Frecuencia de caracteres."""

from collections import Counter


def frecuencia_caracteres(texto: str) -> Counter[str]:
    """Cuenta la frecuencia de cada carácter en el texto."""
    return Counter(texto)


if __name__ == "__main__":
    print(frecuencia_caracteres("banana"))
