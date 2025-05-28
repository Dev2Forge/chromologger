# CHROMOLOGGER

<div style="display: flex; align-items: center; justify-content: center; margin: 10px 0; gap: 10px; max-height: 48px; height: 48px;">
  <a href="https://github.com/sponsors/tutosrive" target="_blank">
  <img src="https://img.shields.io/badge/Sponsor-%F0%9F%92%96%20tutosrive-orange?style=for-the-badge&logo=github" alt="Sponsor me on GitHub">
</a>
  <a href="https://www.buymeacoffee.com/tutosrive">
    <img 
      src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=☕&slug=tutosrive&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" 
      style="height: 48px; width: auto; object-fit: contain; border-radius: 6px;" 
      alt="Buy me a coffee button">
  </a>
</div>

<!-- Badges -->
  <div>
<!-- Total downloads -->
    <a href="https://pepy.tech/projects/chromologger"><img src="https://static.pepy.tech/badge/chromologger" alt="PyPI Downloads"></a>
<!-- Versión actual -->
    <a href="https://pypi.org/project/chromologger/"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/chromologger?label=chromologger"></a>
<!-- Python versions supported -->
    <a href="https://python.org/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/chromologger"></a> 
<!-- Author -->
    <a href="https://github.com/tutosrive"><img alt="Static Badge" src="https://img.shields.io/badge/Tutos%20Rive-Author-brightgreen"></a>
<!-- Licencia -->
    <a href="https://raw.githubusercontent.com/tutosrive/chromologger/main/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/tutosrive/chromologger"></a>
  </div>

```shell
pip install chromologger
```
---

> ### Visite [chromologger](https://dev2forge.github.io/chromologger/) para más documentación

```md
# Se instalará automáticamente
Requerimientos:
    - chromolog>=0.2.0
    # pip install chromolog
    # Esto instalará la versión más reciente (v0.2.4)
```

"**Chromologger**" es un módulo diseñado para facilitar la creación de registros (_logs_) en aplicaciones desarrolladas con **Python**. Proporciona una manera sencilla y estructurada de documentar eventos, errores y actividades en los programas, mejorando la capacidad de monitoreo y depuración del código.

> Ejemplo de registro: En una línea
```md
>  
2025-01-06 19:52:08.636560 - Exception - FileNotFoundError - File - c:\Users\srm\Desktop\msqlite\msqlite\__logger.py - ErrorLine: 35 - Messsage: [Errno 2] - No such file or directory: './data/log'
```

Para empezar a usar, iniciaría con una instancia de la _clase_ **Logger**, la cual toma como argumentos el siguiente parámetro:

- `name:str`: Nombre del archivo en el cual se guardarán los registros (Ej: `'log.log'`).
> NOTA: Es necesario que el directorio donde se guardará el archivo esté creado, ÚNICAMENTE el **directorio**, el archivo se creará dentro de automáticamente...

## Métodos públicos disponibles:

- **log**: Permite guardar mensajes **generales** en el registro, es decir, **NO ERRORES**, mensajes de información _ordinaria_ (general).
- **log_e**: Permite registrar errores, es un registro más específico (Tomar registros de `Exception`)

### Métodos privados 🔏

- **__write**: Escribe los mensages en el archivo cargado
- **__date**: Obtiene la fecha actual
- **__log**: Toma registro de errores internos, guarda los registros en el archivo "./log.log" (En el directorio raíz del módulo)

## Versiones:
- `v0.1.8`: Agrgué manejo de "errores" en el método `log_e(e: Exception)` y actualización del nombre de usuario
- `v0.1.7`: Errores menores
- `v0.1.6`: Actualización de dependencias 
- `v0.1.5`: Arreglé el error que generé en la `v0.1.4`, nunca importé el traceback :|
- `v0.1.4`: Se añadió el manejo de dependencias automáticas correctamente, antes las manejaba con `subpoccess`, pero ahora se hace con el `pip` original (`.toml[dependencies]`)
- `v0.1.3`: El usuario queda libre de instalar dependencias, se instalan automáticamente
- `v0.1.2`: Arreglo de errores por twine
- `v0.1.1`: Algunos errores arreglados
- `v0.1.0`: Versión inicial

Si desea conocer más acerca de, visite:
- [Web de soporte](https://dev2forge.github.io/chromologger/)
- [Web pypi.org](https://pypi.org/project/chromologger/)
- [Github project](https://github.com/tutosrive/chromologger/)
