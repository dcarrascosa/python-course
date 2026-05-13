"""Solución del ejercicio 03: Parsear una versión semántica."""


def parsear_version(version: str) -> tuple[int, int, int]:
    """Devuelve la tupla (major, minor, patch) de una versión semántica."""
    partes = version.split(".")
    if len(partes) != 3:
        raise ValueError(f"Versión inválida: {version!r}")
    try:
        major, minor, patch = (int(p) for p in partes)
    except ValueError as exc:
        raise ValueError(f"Versión inválida: {version!r}") from exc
    return major, minor, patch


if __name__ == "__main__":
    print(parsear_version("1.2.3"))
