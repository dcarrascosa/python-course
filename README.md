# Python para Desarrolladores C#

Curso práctico de Python orientado a desarrolladores con experiencia en C# y .NET. Cada módulo establece puentes explícitos entre los conceptos que ya conoces y su equivalente en Python.

## Prerequisitos

- Experiencia en C# y .NET (cualquier versión)
- Conocimientos básicos de POO
- Familiaridad con la línea de comandos

## Instalación del entorno

```bash
# Instalar uv (gestor de paquetes moderno, equivalente a dotnet CLI)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Crear proyecto nuevo
uv init mi-proyecto
cd mi-proyecto

# Activar entorno virtual
uv venv
.venv\Scripts\activate  # Windows
```

## Mapa del curso

| Módulo | Tema | Equivalente C# |
|--------|------|----------------|
| 01 | [Fundamentos](./modulo-01-fundamentos/) | Variables, tipos, control de flujo |
| 02 | [Estructuras de datos](./modulo-02-estructuras/) | Colecciones, LINQ |
| 03 | [Funciones avanzadas](./modulo-03-funciones/) | Delegates, Func, lambdas |
| 04 | [POO](./modulo-04-poo/) | Clases, interfaces, herencia |
| 05 | [Archivos y serialización](./modulo-05-archivos/) | Streams, System.Text.Json |
| 06 | [Async/await](./modulo-06-async/) | Task, async/await en .NET |
| 07 | [Testing con pytest](./modulo-07-testing/) | xUnit, NUnit, Moq |
| 08 | [Packaging y distribución](./modulo-08-packaging/) | NuGet, dotnet publish |

## Proyecto del curso

A lo largo del curso construirás una **CLI de análisis de logs** que lee ficheros de log, los parsea, filtra y genera un resumen. Cada módulo añade funcionalidad nueva usando los conceptos aprendidos.

## Convenciones del curso

- 🔵 **C#** — bloque de código equivalente en C#
- 🐍 **Python** — bloque de código Python
- ⚠️ **Trampa común** — diferencia que suele confundir a devs C#
- ✅ **Ejercicio** — práctica propuesta
