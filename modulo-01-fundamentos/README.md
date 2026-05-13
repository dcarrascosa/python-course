# Módulo 01 — Fundamentos de Python para devs C#

## Objetivos

- Entender el sistema de tipos dinámico de Python vs el estático de C#
- Dominar variables, tipos primitivos y control de flujo
- Comprender la indentación como estructura sintáctica
- Usar type hints para aproximarse al tipado fuerte

---

## 1. Variables y tipos

En C# declaras el tipo explícitamente. En Python el tipo lo infiere el intérprete en tiempo de ejecución.

🔵 **C#**
```csharp
string nombre = "David";
int edad = 40;
bool activo = true;
double precio = 99.9;
```

🐍 **Python**
```python
nombre = "David"
edad = 40
activo = True
precio = 99.9
```

⚠️ **Trampa común:** En Python `True` y `False` van con mayúscula inicial (no `true`/`false` como en C#).

### Type hints (tipado opcional)

Desde Python 3.5 puedes añadir anotaciones de tipo. No las fuerza el intérprete, pero sí las usan IDEs y herramientas como `mypy`.

```python
nombre: str = "David"
edad: int = 40
activo: bool = True
precio: float = 99.9
```

Equivale al `var` de C# pero con la anotación explícita. Es la práctica recomendada en proyectos profesionales.

---

## 2. Tipos primitivos principales

| C# | Python | Notas |
|----|--------|-------|
| `string` | `str` | Inmutable en ambos |
| `int` | `int` | En Python no hay límite de tamaño |
| `long` | `int` | Mismo tipo en Python |
| `double` / `float` | `float` | Python `float` = double de 64 bits |
| `bool` | `bool` | `True`/`False` con mayúscula |
| `decimal` | `Decimal` (módulo) | `from decimal import Decimal` |
| `null` | `None` | `None` es un objeto, no un puntero nulo |
| `object` | `object` | Clase base de todo en ambos |

### Strings

🔵 **C#**
```csharp
var nombre = "David";
var saludo = $"Hola, {nombre}";
var multilinea = """
    Línea 1
    Línea 2
    """;
```

🐍 **Python**
```python
nombre = "David"
saludo = f"Hola, {nombre}"          # f-string, igual que $ en C#
multilinea = """
    Línea 1
    Línea 2
"""

# Métodos útiles
nombre.upper()        # "DAVID" — como ToUpper()
nombre.lower()        # "david" — como ToLower()
nombre.strip()        # trim — como Trim()
nombre.replace("a", "@")  # como Replace()
" hola ".strip()      # "hola" — como Trim()
```

---

## 3. Control de flujo

### if / elif / else

🔵 **C#**
```csharp
if (edad >= 18)
{
    Console.WriteLine("Mayor de edad");
}
else if (edad >= 16)
{
    Console.WriteLine("Casi mayor");
}
else
{
    Console.WriteLine("Menor de edad");
}
```

🐍 **Python**
```python
if edad >= 18:
    print("Mayor de edad")
elif edad >= 16:
    print("Casi mayor")
else:
    print("Menor de edad")
```

⚠️ **Trampa común:** No hay llaves `{}`. La indentación (4 espacios) define los bloques. Un error de indentación es un error de sintaxis.

### Operador ternario

🔵 **C#**
```csharp
var estado = edad >= 18 ? "adulto" : "menor";
```

🐍 **Python**
```python
estado = "adulto" if edad >= 18 else "menor"
```

### Bucles

🔵 **C#**
```csharp
// for clásico
for (int i = 0; i < 5; i++)
    Console.WriteLine(i);

// foreach
var nombres = new[] { "Ana", "Luis", "Eva" };
foreach (var n in nombres)
    Console.WriteLine(n);

// while
int x = 0;
while (x < 5) x++;
```

🐍 **Python**
```python
# range equivale al for clásico
for i in range(5):
    print(i)

# iterar lista — equivale a foreach
nombres = ["Ana", "Luis", "Eva"]
for n in nombres:
    print(n)

# enumerate cuando necesitas índice + valor
for i, n in enumerate(nombres):
    print(f"{i}: {n}")

# while
x = 0
while x < 5:
    x += 1
```

⚠️ **Trampa común:** En Python no existe `for (int i = 0; i < n; i++)`. Siempre es `for elemento in iterable`. Usa `range()` cuando necesites índices numéricos.

---

## 4. Funciones básicas

🔵 **C#**
```csharp
public string Saludar(string nombre, string saludo = "Hola")
{
    return $"{saludo}, {nombre}!";
}

// Llamada con argumento nombrado
Saludar(nombre: "David", saludo: "Buenos días");
```

🐍 **Python**
```python
def saludar(nombre: str, saludo: str = "Hola") -> str:
    return f"{saludo}, {nombre}!"

# Llamada con argumento nombrado (keyword argument)
saludar(nombre="David", saludo="Buenos días")
saludar("David")  # usa el valor por defecto
```

### Múltiples valores de retorno

En C# usarías `(int, string)` tuple o `out` params. En Python es nativo:

```python
def dividir(a: int, b: int) -> tuple[int, int]:
    cociente = a // b
    resto = a % b
    return cociente, resto

cociente, resto = dividir(17, 5)
print(f"{cociente} resto {resto}")  # 3 resto 2
```

---

## 5. None vs null

🔵 **C#**
```csharp
string? nombre = null;
if (nombre is null)
    Console.WriteLine("Sin nombre");

// Null coalescing
var resultado = nombre ?? "Desconocido";
```

🐍 **Python**
```python
nombre: str | None = None
if nombre is None:
    print("Sin nombre")

# Equivalente a ??
resultado = nombre if nombre is not None else "Desconocido"
# O más idiomático:
resultado = nombre or "Desconocido"  # cuidado: False/0/"" también activan el or
```

⚠️ **Trampa común:** `or` en Python no es exactamente `??` de C#. `nombre or "default"` devuelve `"default"` si `nombre` es cualquier valor *falsy*: `None`, `""`, `0`, `[]`, `False`. Usa `if nombre is not None` cuando quieras solo verificar `None`.

---

## Aportación al proyecto hilo

En este módulo construimos el **esqueleto de la CLI** del `loganalyzer`:
lectura básica de argumentos y validación de entrada.

```python
import sys

def main() -> None:
    args = sys.argv[1:]  # equivale a string[] args en Main()

    if not args:
        print("Uso: python cli.py <fichero_log>")
        sys.exit(1)

    fichero = args[0]
    print(f"Procesando: {fichero}")

if __name__ == "__main__":
    main()
```

⚠️ **Trampa común:** `if __name__ == "__main__"` es el equivalente al `static void Main()` de C#. Sin esto, el código se ejecuta al importar el módulo.

---

## ✅ Ejercicios

| # | Fichero | Enunciado breve |
|---|---------|-----------------|
| 01 | [`ejercicios/01_imc.py`](./ejercicios/01_imc.py) | Calcular el IMC validando entradas. |
| 02 | [`ejercicios/02_fizzbuzz.py`](./ejercicios/02_fizzbuzz.py) | Devolver la secuencia FizzBuzz hasta `n`. |
| 03 | [`ejercicios/03_parsear_version.py`](./ejercicios/03_parsear_version.py) | Parsear `"MAJOR.MINOR.PATCH"` a tupla. |

Cada fichero contiene el enunciado completo en el docstring. Resuelve sin abrir
[`soluciones/`](./soluciones/) y contrasta al terminar.
