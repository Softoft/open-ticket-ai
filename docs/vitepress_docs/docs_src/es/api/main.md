---
description: Documentación oficial para el punto de entrada de la interfaz de línea de comandos
  (CLI) de Open Ticket AI. Esta guía cubre main.py, detallando cómo configurar los
  niveles de registro y lanzar la aplicación.
---
# Documentación para `**/ce/*.py`

## Módulo: `open_ticket_ai\src\ce\app.py`



---

## Módulo: `open_ticket_ai\src\ce\main.py`

Punto de entrada de la CLI de Open Ticket AI.
Este módulo proporciona la interfaz de línea de comandos para la aplicación Open Ticket AI.
Configura los niveles de registro (logging) y lanza la aplicación principal.


### <span class='text-warning'>def</span> `main(verbose: bool, debug: bool)`

Configura el registro (logging) según las opciones de la CLI.
Esta función establece el nivel de registro para la aplicación basándose en los indicadores (flags) de la línea de comandos proporcionados.
Soporta dos niveles de verbosidad:
- `--verbose` para el nivel de registro INFO
- `--debug` para el nivel de registro DEBUG

Si no se proporcionan indicadores, el nivel de registro por defecto es WARNING. La función también configura
el formato de los registros y suprime las bibliotecas ruidosas (p. ej., urllib3).

**Parámetros:**

- **`verbose`** (`bool`) - Habilita el registro de nivel INFO cuando es True.
- **`debug`** (`bool`) - Habilita el registro de nivel DEBUG cuando es True.



### <span class='text-warning'>def</span> `start()`

Inicializa el contenedor e inicia la aplicación.
Este comando realiza las siguientes acciones:
1. Configura el contenedor de inyección de dependencias
2. Obtiene la instancia principal de la aplicación desde el contenedor
3. Ejecuta la aplicación
4. Muestra un banner de inicio estilizado usando `pyfiglet`

La aplicación sigue un patrón de inyección de dependencias donde todas las dependencias requeridas
se resuelven a través del `DIContainer`.



---