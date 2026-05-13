"""Solución del ejercicio 04: Agrupar palabras por longitud."""

from collections import defaultdict


def agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]:
    """Agrupa las palabras por su longitud."""
    grupos: defaultdict[int, list[str]] = defaultdict(list)
    for p in palabras:
        grupos[len(p)].append(p)
    return dict(grupos)


if __name__ == "__main__":
    print(agrupar_por_longitud(["go", "rust", "python", "c#", "ada"]))
