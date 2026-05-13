# Módulo 03 — Ejercicios
import functools
from typing import Callable, Any


# Ejercicio 1: cache simple
def cache_simple(func: Callable) -> Callable:
    """Decorador que cachea resultados por argumentos."""
    raise NotImplementedError


# Ejercicio 2: generador fibonacci
def fibonacci():
    """Generador infinito de números de Fibonacci."""
    raise NotImplementedError


# Ejercicio 3: pipeline
def pipeline(*funciones: Callable) -> Callable:
    """Devuelve una función que aplica las funciones en cadena."""
    raise NotImplementedError


# --- Soluciones ---
# def cache_simple(func):
#     cache = {}
#     @functools.wraps(func)
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#     return wrapper
#
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# def pipeline(*funciones):
#     def aplicar(valor):
#         for fn in funciones:
#             valor = fn(valor)
#         return valor
#     return aplicar
