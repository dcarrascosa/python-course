# Módulo 01 — Ejercicios
# Completa cada función según el enunciado del README

# Ejercicio 1: IMC
def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """Calcula el Índice de Masa Corporal y lo clasifica."""
    # TODO: implementar
    raise NotImplementedError


# Ejercicio 2: FizzBuzz
def fizzbuzz(n: int) -> list[str]:
    """Devuelve lista con FizzBuzz del 1 al n."""
    # TODO: implementar
    raise NotImplementedError


# Ejercicio 3: Parsear versión
def parsear_version(version: str) -> tuple[int, int, int]:
    """Recibe '1.2.3' y devuelve (1, 2, 3)."""
    # TODO: implementar
    raise NotImplementedError


# --- Soluciones (descomenta para ver) ---

# def calcular_imc(peso_kg: float, altura_m: float) -> float:
#     imc = peso_kg / (altura_m ** 2)
#     if imc < 18.5:
#         print("Bajo peso")
#     elif imc < 25:
#         print("Peso normal")
#     elif imc < 30:
#         print("Sobrepeso")
#     else:
#         print("Obesidad")
#     return imc
#
# def fizzbuzz(n: int) -> list[str]:
#     result = []
#     for i in range(1, n + 1):
#         if i % 15 == 0:
#             result.append("FizzBuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         elif i % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(i))
#     return result
#
# def parsear_version(version: str) -> tuple[int, int, int]:
#     partes = version.split(".")
#     return (int(partes[0]), int(partes[1]), int(partes[2]))
