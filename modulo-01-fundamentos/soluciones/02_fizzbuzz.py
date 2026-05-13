"""Solución del ejercicio 02: FizzBuzz."""


def fizzbuzz(n: int) -> list[str]:
    """Devuelve la secuencia FizzBuzz del 1 al n."""
    resultado: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(i))
    return resultado


if __name__ == "__main__":
    print(fizzbuzz(15))
