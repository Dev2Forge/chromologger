# Changelog

Todas las versiones y cambios relevantes del proyecto **Chromologger**.

---

## [0.1.9] - 2025-07-16

### Añadido
- Se añadió la clase `FileManager`, responsable de gestionar todas las operaciones relacionadas con archivos: apertura, cierre, escritura y lectura. Mejora la cohesión y cumple con el principio **SOLID** de responsabilidad única.
- Soporte para rutas relativas al definir archivos de log, resolviéndolas correctamente con `pathlib.Path`.

### Cambiado
- El parámetro `log_file_name` en la clase `Logger` ya no es obligatorio (salvo que especifiques explícitamente una ruta).
- Ahora se detecta automáticamente el script que instanció el logger:
   1. Se obtiene el directorio del script llamador.
   2. Se construye la ruta del archivo de log en ese directorio.
   3. Si no se indica nombre, se usa el valor predeterminado `log.log`.
- Migración del cálculo de rutas absolutas de `os.path` a `pathlib.Path`.

> ⚠️ Si el nombre del archivo no incluye ruta explícita, se crea en el mismo directorio desde donde se invocó el logger.

---

## [0.1.9rc2]
- Actualización del README.md.

---

## [0.1.9rc1]
- Pruebas finales de la versión candidata antes del release.

---

## [0.1.9a2]
- Corrección en el nombre del archivo de log que provocaba errores en algunos sistemas.

---

## [0.1.9a1]
- Refactor del manejo de rutas: de `os` a `pathlib`.
- Soporte completo para rutas relativas.
- Nuevo formato de mensajes de log:
   - Método `log`:
     ```txt
     [INFO][2025-07-15 17:57:50.137718] - Mensaje de registro
     ```
   - Método `log_e`:
     ```txt
     [ERROR][2025-07-15 18:57:50.137718] - Exception - FileNotFoundError - File - ruta/al/archivo.py - ErrorLine: 35 - Message: descripción del error
     ```
- Mejoras en la apertura y escritura de archivos.

---

## [0.1.8]
- Manejo de errores mejorado en `log_e(e: Exception)`.
- Actualización del nombre de usuario en los logs.

---

## [0.1.7]
- Corrección de errores menores.

---

## [0.1.6]
- Actualización de dependencias.

---

## [0.1.5]
- Corrección: se agregó la importación faltante de `traceback`.

---

## [0.1.4]
- Mejora en el manejo automático de dependencias usando `pip` directamente en lugar de `subprocess`.

---

## [0.1.3]
- Instalación automática de dependencias; el usuario ya no debe instalarlas manualmente.

---

## [0.1.2]
- Arreglo de errores relacionados con la publicación en PyPI (twine).

---

## [0.1.1]
- Corrección de varios errores menores.

---

## [0.1.0]
- Versión inicial del proyecto.

---

Para más detalles, visita:
- 📖 Documentación: https://docs.dev2forge.software/chromologger/
- 🔗 Repositorio: https://github.com/Dev2Forge/chromologger
- 🐍 PyPI: https://pypi.org/project/chromologger  
