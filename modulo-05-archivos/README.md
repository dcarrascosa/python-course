# Módulo 05 — Archivos, Excepciones y Contextos

## Objetivos

- Leer y escribir ficheros en Python
- Gestionar excepciones correctamente (vs try/catch de C#)
- Crear context managers propios con `with`
- Trabajar con JSON, CSV y rutas con `pathlib`

---

## 1. Lectura y escritura de ficheros

```csharp
// C#
var content = File.ReadAllText("data.txt");
File.WriteAllText("output.txt", "Hola");

using var reader = new StreamReader("data.txt");
string line;
while ((line = reader.ReadLine()) != null)
    Console.WriteLine(line);
```

```python
# Python — with garantiza el cierre (equivalente a using)
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()          # todo el fichero

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:              # línea a línea, eficiente en memoria
        print(line.strip())

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hola\n")
    f.writelines(["línea 1\n", "línea 2\n"])

# Modos: "r" leer, "w" escribir (sobreescribe), "a" append, "rb" binario
```

---

## 2. pathlib — el Path de .NET

```csharp
// C#
var path = Path.Combine("data", "config.json");
bool exists = File.Exists(path);
var dir = Path.GetDirectoryName(path);
```

```python
from pathlib import Path

path = Path("data") / "config.json"  # operador / para combinar
print(path.exists())          # True/False
print(path.suffix)            # .json
print(path.stem)              # config
print(path.parent)            # data

# Crear directorios
Path("output/reports").mkdir(parents=True, exist_ok=True)

# Listar ficheros
for py_file in Path(".").glob("**/*.py"):
    print(py_file)

# Leer/escribir directamente desde Path
content = path.read_text(encoding="utf-8")
path.write_text("nuevo contenido", encoding="utf-8")
```

---

## 3. JSON

```csharp
// C# — System.Text.Json
var user = JsonSerializer.Deserialize<User>(jsonString);
var json = JsonSerializer.Serialize(user);
```

```python
import json

# Deserializar
with open("users.json", encoding="utf-8") as f:
    data = json.load(f)          # dict/list de Python

user = json.loads('{"name": "David", "age": 40}')  # desde string

# Serializar
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

json_str = json.dumps({"name": "David"}, indent=2)  # a string
```

---

## 4. CSV

```python
import csv
from pathlib import Path

# Leer
with open("products.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # cada fila es un dict
    products = list(reader)

# Escribir
fieldnames = ["name", "price", "stock"]
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([
        {"name": "Teclado", "price": 89.99, "stock": 5},
        {"name": "Ratón",   "price": 29.99, "stock": 12},
    ])
```

---

## 5. Excepciones

```csharp
// C#
try
{
    var result = Divide(10, 0);
}
catch (DivideByZeroException ex)
{
    Console.WriteLine($"Error: {ex.Message}");
}
catch (Exception ex) when (ex is ArgumentException or InvalidOperationException)
{
    Console.WriteLine("Arg o InvalidOp");
}
finally
{
    Console.WriteLine("Siempre");
}
```

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (ValueError, TypeError) as e:  # múltiples tipos
    print(f"Valor o tipo incorrecto: {e}")
except Exception as e:
    print(f"Error genérico: {e}")
    raise  # re-lanzar
else:
    print("Sin errores")  # se ejecuta si NO hubo excepción
finally:
    print("Siempre")  # equivalente a finally en C#

# Excepciones propias
class InsufficientStockError(ValueError):
    def __init__(self, product: str, requested: int, available: int):
        super().__init__(f"Stock insuficiente para {product}: pedido {requested}, disponible {available}")
        self.product = product
        self.requested = requested
        self.available = available
```

---

## 6. Context Managers propios

Equivalente a implementar `IDisposable` en C#:

```csharp
// C# — IDisposable
public class TempFile : IDisposable
{
    public string Path { get; } = System.IO.Path.GetTempFileName();
    public void Dispose() => File.Delete(Path);
}

using var tmp = new TempFile();
```

```python
from contextlib import contextmanager
from pathlib import Path
import tempfile

# Opción 1 — decorador (más simple)
@contextmanager
def temp_file(suffix: str = ".txt"):
    path = Path(tempfile.mktemp(suffix=suffix))
    try:
        yield path          # el bloque with recibe path
    finally:
        path.unlink(missing_ok=True)  # se ejecuta al salir del with

with temp_file(".json") as tmp:
    tmp.write_text('{"test": true}')
    print(tmp.read_text())
# fichero eliminado automáticamente

# Opción 2 — clase con __enter__ / __exit__
class Timer:
    import time
    def __enter__(self):
        self.start = __import__("time").time()
        return self
    def __exit__(self, *args):
        self.elapsed = __import__("time").time() - self.start
        print(f"Tiempo: {self.elapsed:.3f}s")

with Timer() as t:
    sum(range(1_000_000))
```

---

## Ejercicios

### Ejercicio 1 — Procesador de CSV

Crea una función `process_sales(filepath: Path) -> dict` que lea un CSV con columnas `product`, `quantity`, `price` y devuelva un dict con el total vendido por producto.

### Ejercicio 2 — Config manager

Crea una clase `Config` que:
- Cargue un fichero JSON al instanciarse
- Permita acceder a valores con `config["key"]`
- Tenga un método `save()` que persista los cambios
- Lance `KeyError` con mensaje descriptivo si la clave no existe

### Ejercicio 3 — Context manager de log

Crea un context manager `log_operation(name)` que imprima cuándo empieza y termina una operación, y capture cualquier excepción registrándola en un fichero `errors.log`.

---

## Solución

Ver [`soluciones/modulo05.py`](./soluciones/modulo05.py)
