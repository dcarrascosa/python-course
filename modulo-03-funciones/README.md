# Módulo 03 — Funciones avanzadas

## Objetivos

- Entender funciones como objetos de primera clase (vs delegates en C#)
- Dominar `*args` y `**kwargs`
- Comprender closures y su relación con captured variables
- Implementar y usar decoradores (equivalente a atributos/middleware)
- Usar generadores para procesamiento lazy

---

## 1. Funciones como objetos de primera clase

En C# usarías `Func<T>`, `Action<T>` o delegates. En Python, las funciones son objetos directamente.

🔵 **C#**
```csharp
Func<int, int> doblar = x => x * 2;
Action<string> imprimir = s => Console.WriteLine(s);

// Pasar función como parámetro
List<int> Transformar(List<int> lista, Func<int, int> fn)
    => lista.Select(fn).ToList();
```

🐍 **Python**
```python
doblar = lambda x: x * 2
imprimir = lambda s: print(s)

# O como función nombrada (preferible para funciones con lógica)
def doblar(x: int) -> int:
    return x * 2

# Pasar como parámetro
def transformar(lista: list[int], fn) -> list[int]:
    return [fn(x) for x in lista]

transformar([1, 2, 3], doblar)         # [2, 4, 6]
transformar([1, 2, 3], lambda x: x**2) # [1, 4, 9]
```

### Funciones de orden superior

```python
# Devolver una función — como factory method
def multiplicador(factor: int):
    def multiplicar(x: int) -> int:
        return x * factor
    return multiplicar

triplicar = multiplicador(3)
triplicar(5)  # 15
```

---

## 2. *args y **kwargs

Equivale a `params T[]` y a pasar un diccionario de parámetros nombrados.

🔵 **C#**
```csharp
void ImprimirTodos(params string[] valores)
{
    foreach (var v in valores)
        Console.WriteLine(v);
}
```

🐍 **Python**
```python
# *args: número variable de argumentos posicionales
def imprimir_todos(*valores: str) -> None:
    for v in valores:
        print(v)

imprimir_todos("uno", "dos", "tres")

# **kwargs: número variable de argumentos nombrados
def configurar(**opciones: str) -> None:
    for clave, valor in opciones.items():
        print(f"{clave} = {valor}")

configurar(host="localhost", puerto="5432", db="mydb")

# Combinar todo
def completo(requerido: str, *args, **kwargs) -> None:
    print(requerido, args, kwargs)

# Desempaquetar lista/dict al llamar
numeros = [1, 2, 3]
print(*numeros)           # equivale a print(1, 2, 3)

config = {"end": "\n", "sep": ", "}
print("a", "b", **config) # equivale a print("a", "b", end="\n", sep=", ")
```

---

## 3. Closures

Muy similar a las captured variables en lambdas de C#.

🔵 **C#**
```csharp
int contador = 0;
Action incrementar = () => contador++;
Func<int> obtener = () => contador;

incrementar();
incrementar();
obtener(); // 2
```

🐍 **Python**
```python
def crear_contador():
    cuenta = 0
    
    def incrementar() -> None:
        nonlocal cuenta    # necesario para modificar variable del scope externo
        cuenta += 1
    
    def obtener() -> int:
        return cuenta
    
    return incrementar, obtener

incrementar, obtener = crear_contador()
incrementar()
incrementar()
obtener()  # 2
```

⚠️ **Trampa común:** Sin `nonlocal`, Python crea una variable local nueva en vez de modificar la del scope externo. En C# esto es automático con captured variables.

---

## 4. Decoradores — equivalente a atributos/middleware

Un decorador es una función que envuelve otra función. En C# lo harías con atributos + middleware o con el patrón Decorator.

🔵 **C# (patrón Decorator)**
```csharp
public class LoggingService : IMyService
{
    private readonly IMyService _inner;
    public LoggingService(IMyService inner) => _inner = inner;
    
    public string Execute(string input)
    {
        Console.WriteLine($"Llamando con: {input}");
        var result = _inner.Execute(input);
        Console.WriteLine($"Resultado: {result}");
        return result;
    }
}
```

🐍 **Python**
```python
import functools
import time

# Decorador de logging
def log_llamadas(func):
    @functools.wraps(func)  # preserva nombre y docstring de la función original
    def wrapper(*args, **kwargs):
        print(f"Llamando {func.__name__} con {args} {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

# Decorador de tiempo
def medir_tiempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{func.__name__} tardó {fin - inicio:.4f}s")
        return resultado
    return wrapper

# Aplicar decoradores con @
@log_llamadas
@medir_tiempo
def procesar(texto: str) -> str:
    return texto.upper()

procesar("hola")  # log + tiempo automáticos
```

### Decorador con parámetros

```python
def reintentar(veces: int = 3):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(veces):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if intento == veces - 1:
                        raise
                    print(f"Intento {intento + 1} fallido: {e}")
        return wrapper
    return decorador

@reintentar(veces=3)
def llamada_api(url: str) -> str:
    # simula llamada que puede fallar
    ...
```

---

## 5. Generadores — procesamiento lazy

Equivale a `IEnumerable<T>` con `yield return` en C#. La sintaxis es idéntica conceptualmente.

🔵 **C#**
```csharp
IEnumerable<int> GenerarPares(int hasta)
{
    for (int i = 0; i <= hasta; i += 2)
        yield return i;
}
```

🐍 **Python**
```python
def generar_pares(hasta: int):
    for i in range(0, hasta + 1, 2):
        yield i  # igual que yield return en C#

# Consumir
for par in generar_pares(10):
    print(par)

# Generator expression (lazy comprehension)
pares = (n for n in range(100) if n % 2 == 0)  # paréntesis en vez de corchetes
list(pares)  # materializa solo cuando se necesita

# útil para ficheros grandes
def leer_lineas(fichero: str):
    with open(fichero) as f:
        for linea in f:
            yield linea.strip()
```

---

## Aportación al proyecto hilo

En este módulo añadimos al `loganalyzer` un **decorador de validación de
fichero** y refactorizamos la lectura para que devuelva un generador lazy
(útil cuando los logs son grandes).

```python
# extracto: decorador + lectura lazy
import functools
from collections.abc import Iterator
from pathlib import Path


def validar_fichero(func):
    """Valida que el primer argumento sea un fichero existente."""
    @functools.wraps(func)
    def wrapper(ruta: str, *args, **kwargs):
        if not Path(ruta).exists():
            raise FileNotFoundError(f"No se encontró: {ruta}")
        if not Path(ruta).is_file():
            raise ValueError(f"No es un fichero: {ruta}")
        return func(ruta, *args, **kwargs)
    return wrapper


@validar_fichero
def leer_log(ruta: str) -> Iterator[str]:
    with open(ruta) as f:
        for linea in f:
            if linea.strip():
                yield linea.strip()
```

---

## ✅ Ejercicios

| # | Fichero | Enunciado breve |
|---|---------|-----------------|
| 01 | [`ejercicios/01_cache_simple.py`](./ejercicios/01_cache_simple.py) | Decorador que cachea por argumentos posicionales. |
| 02 | [`ejercicios/02_fibonacci.py`](./ejercicios/02_fibonacci.py) | Generador infinito de Fibonacci con `yield`. |
| 03 | [`ejercicios/03_pipeline.py`](./ejercicios/03_pipeline.py) | `pipeline(*funciones)` que las aplica en cadena. |

Cada fichero contiene el enunciado completo en el docstring. Resuelve sin abrir
[`soluciones/`](./soluciones/) y contrasta al terminar.
