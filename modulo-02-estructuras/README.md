# Módulo 02 — Estructuras de datos y colecciones

## Objetivos

- Dominar `list`, `dict`, `set` y `tuple`
- Entender list/dict comprehensions como alternativa a LINQ
- Usar slicing y operaciones funcionales sobre colecciones
- Conocer las estructuras de `collections` y `itertools`

---

## 1. Listas — equivalente a `List<T>`

🔵 **C#**
```csharp
var numeros = new List<int> { 1, 2, 3, 4, 5 };
numeros.Add(6);
numeros.Remove(3);
var primero = numeros[0];
var ultimo = numeros[^1];
var sublista = numeros[1..3];
```

🐍 **Python**
```python
numeros: list[int] = [1, 2, 3, 4, 5]
numeros.append(6)          # Add()
numeros.remove(3)          # Remove() por valor
numeros.pop(0)             # RemoveAt() por índice
primero = numeros[0]
ultimo = numeros[-1]       # índice negativo = desde el final
sublista = numeros[1:3]    # slicing: [inicio:fin] fin excluido
todos_menos_ultimo = numeros[:-1]
reverso = numeros[::-1]    # step -1 = invertir
```

### Operaciones comunes

```python
nombres = ["Eva", "Ana", "Luis", "Pedro"]

len(nombres)               # Count
sorted(nombres)            # OrderBy() — devuelve nueva lista
nombres.sort()             # ordena in-place
"Ana" in nombres           # Contains()
nombres.index("Luis")      # IndexOf()
nombres.count("Ana")       # cuantas veces aparece
nombres.extend(["Mar"])    # AddRange()
[*nombres, "Bea"]          # spread operator — concat sin mutar
```

---

## 2. Diccionarios — equivalente a `Dictionary<K,V>`

🔵 **C#**
```csharp
var persona = new Dictionary<string, object>
{
    { "nombre", "David" },
    { "edad", 40 }
};
persona["email"] = "david@example.com";
var nombre = persona.GetValueOrDefault("nombre", "Desconocido");
bool existe = persona.ContainsKey("email");
persona.Remove("email");
```

🐍 **Python**
```python
persona: dict[str, object] = {
    "nombre": "David",
    "edad": 40
}
persona["email"] = "david@example.com"
nombre = persona.get("nombre", "Desconocido")  # GetValueOrDefault()
existe = "email" in persona                    # ContainsKey()
del persona["email"]                           # Remove()

# Iterar
for clave, valor in persona.items():           # equivale a foreach KeyValuePair
    print(f"{clave}: {valor}")

# Solo claves o solo valores
for clave in persona.keys(): ...
for valor in persona.values(): ...

# Merge de diccionarios (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merge = d1 | d2            # {"a": 1, "b": 2}
d1 |= d2                   # in-place merge
```

---

## 3. Conjuntos — equivalente a `HashSet<T>`

```python
a: set[int] = {1, 2, 3, 4}
b: set[int] = {3, 4, 5, 6}

a | b    # unión        — Union()
a & b    # intersección — Intersect()
a - b    # diferencia  — Except()
a ^ b    # diferencia simétrica

3 in a   # Contains()
a.add(7)
a.discard(1)  # elimina sin error si no existe
```

---

## 4. Tuplas — inmutables

```python
# Tupla — como ValueTuple pero inmutable
punto: tuple[int, int] = (10, 20)
x, y = punto           # destructuring — como (var x, var y) = punto

# Named tuple — como record struct
from typing import NamedTuple

class Punto(NamedTuple):
    x: int
    y: int
    etiqueta: str = "origen"

p = Punto(10, 20)
print(p.x, p.etiqueta)
```

---

## 5. Comprehensions — equivalente a LINQ

Esta es una de las diferencias más importantes. En C# usarías LINQ con `Where`, `Select`, etc. En Python usarás comprehensions.

🔵 **C#**
```csharp
var numeros = Enumerable.Range(1, 10).ToList();

// Where + Select
var pares = numeros.Where(n => n % 2 == 0).ToList();
var cuadrados = numeros.Select(n => n * n).ToList();
var cuadradosPares = numeros
    .Where(n => n % 2 == 0)
    .Select(n => n * n)
    .ToList();
```

🐍 **Python**
```python
numeros = list(range(1, 11))

# List comprehension: [expresion for item in iterable if condicion]
pares = [n for n in numeros if n % 2 == 0]
cuadrados = [n * n for n in numeros]
cuadrados_pares = [n * n for n in numeros if n % 2 == 0]

# Dict comprehension
cuadrados_dict = {n: n * n for n in numeros}
# {1: 1, 2: 4, 3: 9, ...}

# Set comprehension
letras_unicas = {letra for letra in "banana"}
# {'b', 'a', 'n'}
```

### map, filter, reduce (alternativa funcional)

```python
from functools import reduce

# filter — equivale a Where()
pares = list(filter(lambda n: n % 2 == 0, numeros))

# map — equivale a Select()
cuadrados = list(map(lambda n: n * n, numeros))

# reduce — equivale a Aggregate()
total = reduce(lambda acc, n: acc + n, numeros, 0)

# Pero en Python se prefieren comprehensions sobre map/filter
# y sum() / max() / min() sobre reduce para operaciones comunes
total = sum(numeros)
maximo = max(numeros)
```

### any / all — equivalente a Any() / All()

```python
numeros = [1, 2, 3, 4, 5]

any(n > 4 for n in numeros)   # True — alguno > 4
all(n > 0 for n in numeros)   # True — todos > 0
```

---

## 6. collections — estructuras avanzadas

```python
from collections import defaultdict, Counter, deque

# defaultdict: diccionario con valor por defecto
# Equivalente a GetOrAdd en ConcurrentDictionary
grupos: defaultdict[str, list] = defaultdict(list)
grupos["backend"].append("David")
grupos["frontend"].append("Ana")

# Counter: contar frecuencias — muy común en análisis
palabras = ["python", "c#", "python", "java", "python"]
conteo = Counter(palabras)
# Counter({'python': 3, 'c#': 1, 'java': 1})
conteo.most_common(2)  # los 2 más frecuentes

# deque: cola doble eficiente — equivale a LinkedList o Queue
cola: deque[str] = deque()
cola.append("primero")
cola.appendleft("antes")
cola.pop()
cola.popleft()
```

---

## Proyecto del módulo: parser de logs

```python
# modulo-02-estructuras/log_parser.py
from collections import Counter, defaultdict
from dataclasses import dataclass

@dataclass
class LogEntry:
    timestamp: str
    nivel: str
    mensaje: str

def parsear_linea(linea: str) -> LogEntry | None:
    partes = linea.strip().split(" ", 2)
    if len(partes) < 3:
        return None
    return LogEntry(timestamp=partes[0], nivel=partes[1], mensaje=partes[2])

def analizar_logs(lineas: list[str]) -> dict:
    entradas = [e for linea in lineas if (e := parsear_linea(linea))]
    niveles = Counter(e.nivel for e in entradas)
    por_nivel: defaultdict[str, list] = defaultdict(list)
    for e in entradas:
        por_nivel[e.nivel].append(e.mensaje)
    return {
        "total": len(entradas),
        "por_nivel": dict(niveles),
        "mensajes": dict(por_nivel)
    }
```

---

## ✅ Ejercicios

1. Dada una lista de palabras, usa un dict comprehension para crear `{palabra: len(palabra)}`.
2. Filtra con list comprehension los números primos del 1 al 50.
3. Usa `Counter` para contar la frecuencia de cada carácter en una cadena.
4. Implementa `agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]` usando `defaultdict`.
