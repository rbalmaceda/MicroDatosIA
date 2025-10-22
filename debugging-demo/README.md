# Demo de depuración en Python

Este pequeño ejemplo muestra cómo depurar un proyecto simple en Python donde `main` importa y llama a funciones de otro fichero (`helper_module.py`). Incluye instrucciones para ejecutar y depurar en la terminal y en Visual Studio Code.

Archivos:
- `main_debug_demo.py`: script principal que genera datos y llama a funciones del módulo auxiliar.
- `helper_module.py`: módulo con funciones `compute_statistics` y `transform_and_sum`.

Cómo ejecutar:

1. Desde PowerShell (Windows):

```powershell
# Ejecutar normalmente
python .\debugging-demo\main_debug_demo.py


3. En Visual Studio Code:
- Abre la carpeta del workspace en VS Code.
- Abre `main_debug_demo.py` y `helper_module.py`.
- Pon breakpoints (clic a la izquierda del número de línea) en `main_debug_demo.py` y/o dentro de `helper_module.py`.
- Ejecuta la configuración "Python: Current File" o crea una configuración de lanzamiento que apunte a `debugging-demo/main_debug_demo.py`.
- Usa "Step Into" (F11) para entrar en funciones del módulo auxiliar.

Notas:
- El ejemplo está intencionalmente sencillo para que puedas practicar "step into", inspeccionar variables y ver pilas de llamada.
- Puedes modificar los valores y añadir ramas (ej. `multiplier=0`) para practicar diferentes flujos.
