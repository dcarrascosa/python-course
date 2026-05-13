# Módulo 02 — Ejercicios
from collections import Counter, defaultdict


# Ejercicio 1
def longitud_palabras(palabras: list[str]) -> dict[str, int]:
    """Devuelve dict {palabra: longitud}."""
    raise NotImplementedError


# Ejercicio 2
def numeros_primos(limite: int) -> list[int]:
    """Devuelve lista de primos hasta limite (inclusive)."""
    raise NotImplementedError


# Ejercicio 3
def frecuencia_caracteres(texto: str) -> Counter:
    """Cuenta frecuencia de cada carácter."""
    raise NotImplementedError


# Ejercicio 4
def agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]:
    """Agrupa palabras por su longitud."""
    raise NotImplementedError


# --- Soluciones ---
# def longitud_palabras(palabras):
#     return {p: len(p) for p in palabras}
#
# def numeros_primos(limite):
#     def es_primo(n):
#         if n < 2: return False
#         return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
#     return [n for n in range(2, limite + 1) if es_primo(n)]
#
# def frecuencia_caracteres(texto):
#     return Counter(texto)
#
# def agrupar_por_longitud(palabras):
#     grupos = defaultdict(list)
#     for p in palabras:
#         grupos[len(p)].append(p)
#     return dict(grupos)
