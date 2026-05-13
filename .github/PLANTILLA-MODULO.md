# Plantilla de módulo

Esta es la estructura canónica que sigue cada módulo del curso. Úsala como
referencia al crear contenido nuevo o revisar un módulo existente.

## Estructura de carpetas

```
modulo-XX-tema/
  README.md
  ejercicios/
    01_<descripcion>.py
    02_<descripcion>.py
    ...
  soluciones/
    01_<descripcion>.py
    02_<descripcion>.py
    ...
```

Reglas:

- **Un ejercicio = un fichero.** Permite enunciados largos y casos de prueba en
  el docstring sin amontonar.
- **Padding numérico** (`01_`, `02_`, ..., `10_`) para mantener orden
  lexicográfico limpio.
- **Misma firma** entre `ejercicios/NN_x.py` y `soluciones/NN_x.py`. Así una
  batería de tests sirve para ambos.
- **Sin efectos secundarios al importar.** Cualquier `print` o demostración va
  dentro de `if __name__ == "__main__":`.
- **El `__main__` es opcional**, solo para demos rápidas. La lógica testeable
  vive en funciones puras.

## Plantilla de fichero de ejercicio

```python
"""Ejercicio NN: <título corto>.

<Enunciado completo. Describe qué debe hacer la función, qué casos esquina
manejar y qué excepciones lanzar. Incluye ejemplos:>

>>> nombre_funcion(arg1, arg2)
resultado_esperado
"""


def nombre_funcion(param1: tipo, param2: tipo) -> tipo:
    """<Una línea describiendo el contrato>."""
    # TODO: implementar
    raise NotImplementedError
```

## Plantilla de fichero de solución

```python
"""Solución del ejercicio NN: <título corto>."""


def nombre_funcion(param1: tipo, param2: tipo) -> tipo:
    """<Una línea describiendo el contrato>."""
    # implementación


if __name__ == "__main__":
    # demo opcional
    print(nombre_funcion(...))
```

## Plantilla del README del módulo

```md
# Módulo XX — <Tema>

<Frase de gancho de 1-2 líneas: qué se aprende y por qué importa para un dev C#.>

## Objetivos

- <Habilidad concreta 1>
- <Habilidad concreta 2>
- <Habilidad concreta 3>

## Mapa C# ↔ Python

| Concepto | C# | Python |
|----------|----|--------|
| ... | ... | ... |

## Teoría

### <Sub-tema>

🔵 **C#**

​`​`​`csharp
// código de referencia en C#
​`​`​`

🐍 **Python**

​`​`​`python
# código equivalente en Python
​`​`​`

> ⚠️ **Trampa común:** <diferencia que suele confundir al dev C#>

## ✅ Ejercicios

| # | Fichero | Enunciado breve |
|---|---------|-----------------|
| 01 | [`ejercicios/01_xxx.py`](./ejercicios/01_xxx.py) | <una línea> |
| 02 | [`ejercicios/02_xxx.py`](./ejercicios/02_xxx.py) | <una línea> |

Resuelve los ejercicios sin abrir `soluciones/`. Cuando termines, contrasta
con [`soluciones/`](./soluciones/).

## Aportación al proyecto hilo

<Qué funcionalidad del `loganalyzer` se construye o refactoriza en este
módulo aplicando los conceptos aprendidos.>

## Recursos

- <Enlaces a docs oficiales relevantes>
```
