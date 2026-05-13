# Módulo 04 — Programación Orientada a Objetos

## Objetivos

- Crear clases en Python y compararlas con las de C#
- Entender herencia, encapsulación y polimorfismo en Python
- Usar dataclasses y protocolos como alternativas modernas

---

## 1. Clases básicas

```csharp
// C#
public class Product
{
    public string Name { get; set; }
    public decimal Price { get; set; }

    public Product(string name, decimal price)
    {
        Name = name;
        Price = price;
    }

    public string Describe() => $"{Name} cuesta {Price}€";
}
```

```python
# Python
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def describe(self) -> str:
        return f"{self.name} cuesta {self.price}€"

p = Product("Teclado", 89.99)
print(p.describe())  # Teclado cuesta 89.99€
```

> **Clave:** `self` es equivalente a `this` en C#. El primer parámetro de todo método de instancia siempre es `self`.

---

## 2. Encapsulación — propiedades vs getters/setters

```csharp
// C# — propiedad con validación
private decimal _price;
public decimal Price
{
    get => _price;
    set
    {
        if (value < 0) throw new ArgumentException("Precio negativo");
        _price = value;
    }
}
```

```python
# Python — decorator @property
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price  # convención: _ = "privado"

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Precio negativo")
        self._price = value

p = Product("Ratón", 29.99)
p.price = 25.0   # usa el setter
print(p.price)   # usa el getter
```

> **Nota:** Python no tiene modificadores `private`/`protected` reales. La convención es `_nombre` (protegido) y `__nombre` (name mangling).

---

## 3. Herencia

```csharp
// C#
public class Animal
{
    public string Name { get; }
    public Animal(string name) => Name = name;
    public virtual string Sound() => "...";
}

public class Dog : Animal
{
    public Dog(string name) : base(name) {}
    public override string Sound() => "Guau";
}
```

```python
# Python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self) -> str:
        return "..."

class Dog(Animal):  # herencia entre paréntesis
    def sound(self) -> str:  # override implícito
        return "Guau"

    def fetch(self):
        return f"{self.name} trae la pelota"

class GoldenRetriever(Dog):
    def __init__(self, name: str):
        super().__init__(name)  # equivalente a base(name)
        self.breed = "Golden Retriever"

d = GoldenRetriever("Rex")
print(d.sound())   # Guau — hereda el override
print(d.fetch())   # Rex trae la pelota
```

---

## 4. Métodos especiales (dunder methods)

Equivalentes a sobrecargar operadores en C#:

```csharp
// C#
public static Product operator +(Product a, Product b)
    => new Product($"{a.Name}+{b.Name}", a.Price + b.Price);

public override string ToString() => $"Product({Name}, {Price})";
```

```python
# Python — dunder (double underscore) methods
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self) -> str:          # equivalente a ToString()
        return f"Product({self.name!r}, {self.price})"

    def __add__(self, other: "Product") -> "Product":
        return Product(f"{self.name}+{other.name}", self.price + other.price)

    def __eq__(self, other: object) -> bool:  # equivalente a Equals()
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __lt__(self, other: "Product") -> bool:  # para sorted()
        return self.price < other.price

a = Product("Teclado", 89.99)
b = Product("Ratón", 29.99)
print(a + b)        # Product('Teclado+Ratón', 119.98)
print(sorted([a, b]))  # ordena por precio
```

---

## 5. Dataclasses — el equivalente a records de C# 9+

```csharp
// C# 9+ record
public record Point(double X, double Y);
```

```python
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Point:
    x: float
    y: float

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

# __init__, __repr__ y __eq__ generados automáticamente
p1 = Point(3.0, 4.0)
p2 = Point(3.0, 4.0)
print(p1 == p2)               # True
print(p1.distance_to_origin()) # 5.0

@dataclass(frozen=True)  # inmutable — equivalente a record
class ImmutablePoint:
    x: float
    y: float
```

---

## 6. Protocolos (Duck Typing formal)

Equivalente a interfaces en C#, pero sin herencia obligatoria:

```csharp
// C#
public interface IDescribable
{
    string Describe();
}
```

```python
from typing import Protocol

class Describable(Protocol):
    def describe(self) -> str: ...

# Cualquier clase con método describe() cumple el protocolo
# SIN necesidad de herencia explícita
class Task:
    def describe(self) -> str:
        return "Una tarea"

class Product:
    def describe(self) -> str:
        return "Un producto"

def print_description(item: Describable) -> None:
    print(item.describe())

print_description(Task())    # funciona
print_description(Product()) # funciona
```

---

## Ejercicios

### Ejercicio 1 — Clase BankAccount

Crea una clase `BankAccount` con:
- Atributos: `owner`, `balance` (privado)
- Métodos: `deposit(amount)`, `withdraw(amount)` (lanza `ValueError` si no hay saldo)
- Propiedad `balance` solo lectura
- `__repr__` informativo

### Ejercicio 2 — Jerarquía de vehículos

Crea `Vehicle` (base) con `make`, `model`, `year` y método abstracto `fuel_cost_per_km()`. Luego `ElectricCar` y `GasCar` que sobrescriban el método. Usa `abc.ABC` y `@abstractmethod`.

### Ejercicio 3 — Dataclass con validación

Crea una dataclass `Employee` con `name`, `salary` y `department`. Usa `__post_init__` para validar que el salario sea positivo. Implementa `__lt__` para poder ordenar empleados por salario.

---

## Solución

Ver [`soluciones/modulo04.py`](./soluciones/modulo04.py)
