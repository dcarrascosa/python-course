"""Solución del ejercicio 01: Índice de Masa Corporal."""


def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """Devuelve el IMC redondeado a 2 decimales."""
    if peso_kg <= 0 or altura_m <= 0:
        raise ValueError("Peso y altura deben ser positivos")
    return round(peso_kg / (altura_m ** 2), 2)


if __name__ == "__main__":
    print(calcular_imc(70, 1.75))
