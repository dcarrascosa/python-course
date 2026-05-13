"""Solución del ejercicio 01: Longitud de palabras."""


def longitud_palabras(palabras: list[str]) -> dict[str, int]:
    """Mapea cada palabra a su longitud."""
    return {p: len(p) for p in palabras}


if __name__ == "__main__":
    print(longitud_palabras(["python", "go", "rust"]))
