"""Ejercicio 04: Agrupar palabras por longitud.

Dada una lista de palabras, devuelve un diccionario que agrupa las palabras
por su longitud. Cada clave es una longitud y su valor es la lista de
palabras con esa longitud, en el orden en que aparecen en la entrada.

Pista: `collections.defaultdict(list)` te ahorra el `if key in dict`.

El resultado se devuelve como `dict` normal (no `defaultdict`) para evitar
sorpresas en quien lo consume.

Ejemplos:

>>> agrupar_por_longitud(["go", "rust", "python", "c#", "ada"])
{2: ['go', 'c#'], 4: ['rust'], 6: ['python'], 3: ['ada']}
>>> agrupar_por_longitud([])
{}
"""


def agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]:
    """Agrupa las palabras por su longitud."""
    # TODO: implementar
    raise NotImplementedError
