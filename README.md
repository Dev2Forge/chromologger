# CHROMOLOGGER

---

<div align="center" style="display: flex; align-items: center; justify-content: center; margin: 10px 0; gap: 10px; max-height: 48px; height: 48px;">
  <a href="https://github.com/sponsors/tutosrive" target="_blank">
  <img src="https://img.shields.io/badge/Sponsor-%F0%9F%92%96%20Dev2Forge-blue?style=for-the-badge&logo=github" alt="Sponsor me on GitHub">
</a>
  <a href="https://ko-fi.com/D1D61GNZR1" target="_blank">
  <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Sponsor me on Ko-Fi">
</a>
</div>

---

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

> ### Visite [chromologger](https://docs.dev2forge.software/chromologger/) para más documentación

> Descarga nuestro nuevo proyecto: [`pip install bridgex`](https://github.com/Dev2Forge/bridgex)
> <div align="center"><img src="https://cdn.jsdelivr.net/gh/tutosrive/images-projects-srm-trg@main/dev2forge/logos/bridgex-v0.1.0.webp" width="200"></div>

"**Chromologger**" es un módulo avanzado de logging diseñado para facilitar la creación de registros (_logs_) profesionales en aplicaciones desarrolladas con **Python**. Proporciona una solución completa y fácil de usar para documentar eventos, excepciones y actividades del sistema, mejorando significativamente la capacidad de monitoreo, debugging y mantenimiento del código.

## 🚀 Características Principales

- **Logging automático con timestamps precisos** - Cada registro incluye fecha y hora con microsegundos
- **Manejo inteligente de excepciones** - Traceback completo con archivo, línea y descripción
- **Archivos de log organizados** - Soporte para múltiples niveles (INFO, ERROR, etc.)
- **Integración con chromolog** - Salida colorizada en consola para mejor visualización
- **Gestión automática de rutas** - Detección inteligente del directorio del script llamador
- **Sistema de logging interno** - Debug y mantenimiento del propio módulo
- **API simple e intuitiva** - Fácil implementación en cualquier proyecto

## 📦 Instalación

```bash
# Instalar chromologger
pip install chromologger

# Instalar dependencia (si no se instala automáticamente)  
pip install chromolog==0.2.5
```

## 🔧 Uso Rápido

### Uso Básico
```python
from chromologger import Logger

# Crear logger (archivo por defecto: log.log en directorio del script)
logger = Logger()

# Registrar mensaje informativo
logger.log('Aplicación iniciada correctamente')

# Registrar excepción
try:
    resultado = 10 / 0
except Exception as e:
    logger.log_e(e)

# Cerrar logger (liberar recursos)
logger.close()
```

### Uso Avanzado
```python
from chromologger import Logger
import os

# Crear directorio si no existe
os.makedirs('./logs', exist_ok=True)

# Logger con archivo personalizado
app_logger = Logger('./logs/mi_aplicacion.log')

# Registrar diferentes tipos de eventos
app_logger.log('Sistema iniciado')
app_logger.log({'evento': 'login', 'usuario': 'admin'})
app_logger.log(f'Procesados 150 elementos')

# Manejo de errores
try:
    with open('archivo_inexistente.txt', 'r') as f:
        contenido = f.read()
except FileNotFoundError as e:
    app_logger.log_e(e)  # Registra traceback completo

app_logger.close()
```

## 📋 Formato de Registro

Los registros se almacenan con formato estructurado y timestamps precisos:

**Mensaje informativo:**
```
[INFO][2025-01-06 19:52:08.636560] - Aplicación iniciada correctamente
```

**Registro de excepción:**
```
[ERROR][2025-01-06 19:52:08.636560] - Exception: FileNotFoundError - File: c:\Users\app\main.py - ErrorLine: 35 - Message: [Errno 2] No such file or directory: './data/config.json'
```

## 🔧 API Documentación

### Clase Logger

#### Constructor
```python
Logger(log_file_name: str = 'log.log')
```
- **log_file_name** (str, opcional): Nombre o ruta del archivo de log
  - Si es `'log.log'`: Se crea en el directorio del script llamador
  - Si es otra ruta: Se respeta la ubicación especificada

#### Métodos Públicos

##### 🗒️ log(msg: any) → None
Registra mensajes informativos generales con nivel INFO y timestamp automático.

- **Parámetros**: `msg` - Mensaje a registrar (acepta cualquier tipo de dato)
- **Características**: Conversión automática a string, timestamp con microsegundos

##### ⚠️ log_e(e: Exception) → None
Registra excepciones con información detallada de traceback.

- **Parámetros**: `e` - Instancia de Exception o subclases
- **Información incluida**: Tipo de excepción, archivo, línea, mensaje completo

##### 🔒 close() → bool
Cierra el archivo de log y libera recursos del sistema.

- **Retorna**: `True` si se cerró exitosamente, `False` en caso contrario

## 🔥 Ejemplos Avanzados

### Aplicación Web con Logging Completo
```python
from chromologger import Logger
from datetime import datetime
import os

# Configurar logging por fecha
log_dir = './logs'
os.makedirs(log_dir, exist_ok=True)
app_logger = Logger(f'{log_dir}/app_{datetime.now().strftime("%Y%m%d")}.log')

class WebApplication:
    def __init__(self):
        app_logger.log('Inicializando aplicación web')
    
    def handle_request(self, user_id, endpoint):
        try:
            app_logger.log(f'Usuario {user_id} accediendo a {endpoint}')
            # ... lógica de procesamiento ...
            app_logger.log(f'Request procesado exitosamente para {user_id}')
        except Exception as e:
            app_logger.log_e(e)
            app_logger.log(f'Error procesando request de usuario {user_id}')
    
    def shutdown(self):
        app_logger.log('Cerrando aplicación web')
        app_logger.close()
```

### Sistema de Monitoreo con Múltiples Loggers
```python
from chromologger import Logger

# Diferentes loggers para diferentes propósitos
access_logger = Logger('./logs/access.log')
error_logger = Logger('./logs/errors.log')
performance_logger = Logger('./logs/performance.log')

def monitor_system():
    try:
        access_logger.log('Sistema de monitoreo iniciado')
        # ... trabajo del sistema ...
        performance_logger.log('Operación completada en 2.5 segundos')
    except Exception as e:
        error_logger.log_e(e)
    finally:
        # Cerrar todos los loggers
        for logger in [access_logger, error_logger, performance_logger]:
            logger.close()
```

## ⚙️ Características Técnicas

### Formato de Timestamp
- **Precisión**: Microsegundos para debugging detallado
- **Formato**: `YYYY-MM-DD HH:MM:SS.microseconds`

### Niveles de Log
- **[INFO]** - Mensajes informativos generales
- **[ERROR]** - Excepciones y errores del sistema
- **Futuros**: WARNING, DEBUG, CRITICAL

### Gestión de Rutas
- **Detección automática**: Identifica el directorio del script llamador
- **Rutas relativas**: Soporte completo para `./logs/app.log`
- **Rutas absolutas**: Compatible con rutas completas del sistema
- **Creación automática**: El archivo se crea si no existe

## 🔧 Solución de Problemas

### Errores Comunes

**1. FileNotFoundError al crear el logger**
```python
# ❌ Error: directorio no existe
logger = Logger('./logs_inexistentes/app.log')

# ✅ Solución: crear directorio primero
import os
os.makedirs('./logs', exist_ok=True)
logger = Logger('./logs/app.log')
```

**2. Verificar inicialización correcta**
```python
logger = Logger()
if hasattr(logger, 'file') and logger.file != -1:
    logger.log('Logger funcionando correctamente')
else:
    print('Error: Logger no se inicializó correctamente')
```

## ✨ Mejores Prácticas

### 1. Organización de Logs
```python
from datetime import datetime

# Por fecha
date_str = datetime.now().strftime("%Y%m%d")
logger = Logger(f'./logs/app_{date_str}.log')

# Por funcionalidad
auth_logger = Logger('./logs/authentication.log')
db_logger = Logger('./logs/database.log')
api_logger = Logger('./logs/api_requests.log')
```

### 2. Manejo de Recursos
```python
# Patrón recomendado
def process_data():
    logger = Logger('data_processing.log')
    try:
        logger.log('Iniciando procesamiento')
        # ... procesamiento ...
        logger.log('Procesamiento completado')
    except Exception as e:
        logger.log_e(e)
    finally:
        logger.close()
```

### 3. Logging Informativo vs Errores
```python
# ✅ Usar log() para eventos normales
logger.log('Usuario autenticado exitosamente')
logger.log('Base de datos conectada')
logger.log('Archivo procesado: 150 registros')

# ✅ Usar log_e() solo para excepciones
try:
    # operación riesgosa
    pass
except Exception as e:
    logger.log_e(e)  # Información completa de traceback
```

## 🚀 Próximas Características

- 🔄 Soporte para múltiples niveles de log (WARNING, DEBUG, CRITICAL)
- 🔄 Context managers (with statement)
- 🔄 Rotación automática de archivos por tamaño/fecha
- 🔄 Configuración de formato personalizada
- 🔄 Filtros de log por nivel
- 🔄 Exportación a JSON/CSV

## 📚 Recursos y Documentación

- **[Documentación Completa](https://docs.dev2forge.software/chromologger/)** - Guía completa con ejemplos avanzados
- **[PyPI Package](https://pypi.org/project/chromologger/)** - Información del paquete y versiones
- **[GitHub Repository](https://github.com/Dev2Forge/chromologger)** - Código fuente y contribuciones
- **[Changelog](https://github.com/Dev2Forge/chromologger/blob/main/CHANGELOG.md)** - Historial de versiones y cambios

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes sugerencias:

1. Crea un [Issue](https://github.com/Dev2Forge/chromologger/issues) para reportar bugs
2. Envía un [Pull Request](https://github.com/Dev2Forge/chromologger/pulls) con mejoras
3. Comparte feedback en las [Discussions](https://github.com/Dev2Forge/chromologger/discussions)

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](https://raw.githubusercontent.com/tutosrive/chromologger/main/LICENSE) para más detalles.

## 🙏 Agradecimientos

Desarrollado por [Tutos Rive](https://github.com/tutosrive) con ❤️ para la comunidad Python.

---

> **¿Te gusta chromologger?** ⭐ ¡Dale una estrella en GitHub y compártelo!

> **Nuevo proyecto:** Descarga [`bridgex`](https://github.com/Dev2Forge/bridgex) - Nuestro último proyecto para desarrollo avanzado
