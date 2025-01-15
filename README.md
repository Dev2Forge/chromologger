# CHROMOLOGGER 
### [Versión actual: 0.1.5](#versiones)

> ### Visite [chromologger](https://tutosrivegamerlq.github.io/chromologger/) para más documentación

```md
Requerimientos:
    - chromolog>=0.2.0
    # pip install chromolog
    # Esto instalará la versión más reciente (v0.2.2)
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
- **log_e**: Permite registrar errores, es un registro más específico.

### Métodos privados 🔏

- **__write**: Escribe los mensages en el archivo cargado
- **__date**: Obtiene la fecha actual
- **__log**: Toma registro de errores internos, guarda los registros en el archivo "./log.log" (En el directorio raíz del módulo)

## Versiones:
- `v0.1.5`: Arreglé el error que generé en la `v0.1.4`, nunca importé el traceback :|
- `v0.1.4`: Se añadió el manejo de dependencias automáticas correctamente, antes las manejaba con `subpoccess`, pero ahora se hace con el `pip` original (`.toml[dependencies]`)
- `v0.1.3`: El usuario queda libre de instalar dependencias, se instalan automáticamente
- `v0.1.2`: Arreglo de errores por twine
- `v0.1.1`: Algunos errores arreglados
- `v0.1.0`: Versión inicial

Si desea conocer más acerca de, visite:
- [Web de soporte](https://tutosrivegamerlq.github.io/chromologger/)
- [Web pypi.org](https://pypi.org/project/chromologger/)
- [Github project](https://github.com/tutosrivegamerLQ/chromologger/)
