# v0.1.9
"""chromologger - Módulo de logging avanzado para Python.

Este módulo proporciona una solución completa y fácil de usar para el logging
en aplicaciones Python. Permite crear registros estructurados con timestamps
precisos, manejo automático de excepciones y archivos de log organizados.

Características principales:
    - Logging automático con timestamps
    - Manejo inteligente de excepciones con traceback
    - Archivos de log organizados por tipo
    - Integración con chromolog para salida colorizada
    - Gestión automática de rutas de archivos
    - Registros internos para debug del propio módulo

Requerimientos: 
    - chromolog==0.2.5 (Para salida colorizada en consola)

Historial de versiones:
    - v0.1.9: Revise este enlace para más información (https://pypi.org/project/chromologger/0.1.9)
    - v0.1.9rc2: Revise este enlace para más información (https://pypi.org/project/chromologger/0.1.9rc2)
    - v0.1.9rc1: Revise este enlace para más información (https://pypi.org/project/chromologger/0.1.9rc1)
    - v0.1.9a2: Revise este enlace para más información (https://pypi.org/project/chromologger/0.1.9a2)
    - v0.1.9a1: Revise este enlace para más información (https://pypi.org/project/chromologger/0.1.9a1)
    - v0.1.8: Agregué manejo de "errores" en el método `log_e(e: Exception)` y actualización del nombre de usuario
    - v0.1.7: Errores menores
    - v0.1.6: Actualización de dependencias 
    - v0.1.5: Arreglé el error que generé en la v0.1.4, nunca importé el traceback :|
    - v0.1.4: Se añadió el manejo de dependencias automáticas correctamente, antes las manejaba con `subpoccess`, pero ahora se hace con el `pip` original (`.toml[dependencies]`)
    - v0.1.3: El usuario queda libre de instalar dependencias, se instalan automáticamente
    - v0.1.2: Arreglo de errores por twine
    - v0.1.1: Algunos errores arreglados
    - v0.1.0: Versión inicial

Ejemplos de uso:
    >>> from chromologger import Logger
    >>> logger = Logger('mi_app.log')
    >>> logger.log('Aplicación iniciada correctamente')
    >>> try:
    ...     resultado = 10 / 0
    ... except Exception as e:
    ...     logger.log_e(e)
    >>> logger.close()

Para más información, visite: [chromologger](https://docs.dev2forge.software)

@author Tutos Rive
@version 0.1.9
@since 2024
"""
import inspect
from io import TextIOWrapper
from datetime import datetime
from typing import Optional, Union

# Importación de utilidades propias del módulo
from .utils.dates import Dates
from .utils.files_manager import FileManager
from chromolog import Print

# Información del módulo
__version__ = "0.1.9"
__author__ = "Tutos Rive"

# Obtener ruta absoluta del directorio actual del módulo
# Esta ruta se usa para los archivos de log internos del módulo
current_path: str = FileManager.get_abs_dir(__file__)

# Configurar la impresora de mensajes con colores para la consola
# Se utiliza para mostrar mensajes informativos, de error y debug
printer_chromolog: Print = Print()

# Mostrar mensaje informativo al importar el módulo
printer_chromolog.inf('Visite esta página (https://docs.dev2forge.software) antes de ejecutar este módulo')

class Logger:
    """Clase principal para la gestión de registros (logging).
    
    Esta clase proporciona una interfaz completa para crear y gestionar archivos
    de log con timestamps automáticos, manejo de excepciones y organización
    estructurada de los registros.
    
    La clase maneja automáticamente:
    - Creación y apertura de archivos de log
    - Formato consistente de mensajes con timestamps
    - Logging de excepciones con traceback completo
    - Registros internos del módulo para debug
    - Gestión de rutas absolutas y relativas
    
    Attributes:
        log_file_name (str): Nombre del archivo de log principal
        caller_script (str): Ruta del script que instancia la clase
        path (str): Ruta absoluta completa del archivo de log
        file (TextIOWrapper): Objeto archivo abierto para escritura
        
    Examples:
        >>> # Uso básico con archivo por defecto
        >>> logger = Logger()
        >>> logger.log('Mensaje de prueba')
        >>> logger.close()
        
        >>> # Uso con archivo personalizado
        >>> logger = Logger('mi_aplicacion.log')
        >>> logger.log('Aplicación iniciada')
        >>> try:
        ...     resultado = operacion_riesgosa()
        ... except Exception as e:
        ...     logger.log_e(e)
        >>> logger.close()
    """
    
    def __init__(self, log_file_name: str = 'log.log') -> None:
        """Inicializa una nueva instancia del Logger.
        
        Configura todos los parámetros necesarios para el logging, incluyendo
        la ruta del archivo, la detección del script llamador y la apertura
        del archivo de log.
        
        Args:
            log_file_name (str, optional): Nombre del archivo de log. 
                Si es 'log.log', se creará en el directorio del script llamador.
                Si es otro nombre, se puede especificar una ruta completa.
                Defaults to 'log.log'.
                
        Note:
            - Si log_file_name es 'log.log', el archivo se crea en el mismo
              directorio que el script que llama al Logger
            - Si log_file_name contiene una ruta, se respeta esa ubicación
            - El archivo se abre automáticamente en modo append
        """
        # Almacenar el nombre del archivo de log
        self.log_file_name: str = log_file_name

        # Obtener el directorio del script que está llamando a esta clase
        # Usa inspect para rastrear la llamada y obtener la ubicación real
        self.caller_script = FileManager.get_abs_dir(inspect.currentframe().f_back.f_code.co_filename)

        # Construir la ruta completa del archivo de log
        # Si es el nombre por defecto, va en el directorio del llamador
        # Si no, se trata como ruta absoluta o se procesa como tal
        self.path: str = f'{self.caller_script}/{self.log_file_name}' if log_file_name == 'log.log' else FileManager.get_abs_path(log_file_name)
        print(self.path)  # Debug: mostrar la ruta calculada

        # Abrir el archivo para escritura
        self.file: TextIOWrapper = self.__open()
    
    def __open(self) -> Union[TextIOWrapper, int]:
        """Abre el archivo de log para escritura.
        
        Intenta abrir el archivo especificado en la ruta configurada durante
        la inicialización. Si el archivo no existe, lo crea. Si ocurre un
        error, registra la excepción internamente.
        
        Returns:
            Union[TextIOWrapper, int]: 
                - TextIOWrapper: Objeto archivo abierto exitosamente
                - int: -1 si ocurrió un error al abrir el archivo
                
        Raises:
            FileNotFoundError: Cuando no se puede crear o acceder al archivo
            (se maneja internamente y se registra)
            
        Note:
            Este método es privado y solo debe ser llamado durante la
            inicialización de la clase. Los errores se registran usando
            el sistema de logging interno.
        """
        try:
            # Intentar abrir el archivo usando el FileManager
            # El FileManager se encarga de crear directorios si es necesario
            return FileManager.open_file(self.path)
        except FileNotFoundError as e:
            # Si no se puede abrir/crear el archivo, registrar error interno
            self.__log(e)
            return -1

    def close(self) -> bool:
        """Cierra el archivo de log y libera los recursos.
        
        Este método debe ser llamado cuando se termina de usar el logger
        para asegurar que todos los datos se escriban al disco y se liberen
        los recursos del sistema.
        
        Returns:
            bool: 
                - True si el archivo se cerró exitosamente
                - False si no había un archivo válido que cerrar
                
        Note:
            - Es recomendable usar el patrón with o llamar explícitamente
              a este método al finalizar el uso del logger
            - Si el archivo ya está cerrado o nunca se abrió correctamente,
              el método retorna False sin generar errores
              
        Example:
            >>> logger = Logger('mi_app.log')
            >>> logger.log('Mensaje de prueba')
            >>> success = logger.close()
            >>> if success:
            ...     print("Archivo cerrado correctamente")
        """
        # Verificar que el objeto file es realmente un archivo válido
        if type(self.file) == TextIOWrapper: 
            self.file.close()
            return True

        # Indica que el archivo NO se pudo cerrar (no era válido)
        return False

    def log(self, msg: any) -> None:
        """Registra un mensaje informativo en el archivo de log.
        
        Este es el método principal para logging general. Acepta cualquier tipo
        de dato y lo convierte a string para su registro. Cada mensaje se 
        almacena con timestamp automático y nivel INFO.
        
        Args:
            msg (any): Mensaje a registrar. Puede ser string, número, objeto, etc.
                      Se convertirá automáticamente a string para su almacenamiento.
                      
        Note:
            - Automáticamente añade timestamp en formato ISO
            - El nivel de log por defecto es 'INFO'
            - Muestra la ruta del archivo de log en consola (modo debug)
            - Los errores durante la escritura se manejan internamente
            
        Examples:
            >>> logger = Logger()
            >>> logger.log("Aplicación iniciada")
            >>> logger.log(f"Usuario {usuario} conectado")
            >>> logger.log({"evento": "login", "usuario": "admin"})
            >>> logger.log(42)  # También acepta números
            
        See Also:
            log_e(): Para registrar excepciones con traceback completo
        """
        # Escribir el mensaje usando el método privado __write
        # Por defecto usa el nivel 'info'
        self.__write(msg)

        # Mostrar información al usuario sobre dónde encontrar los logs
        # TODO: Implementar modo debug para controlar cuándo mostrar esto
        printer_chromolog.inf(f'Revise {self.path} para ver los registros.')
    
    def log_e(self, e: Exception) -> None:
        """Registra una excepción con información detallada de traceback.
        
        Este método especializado captura excepciones y las registra con
        información completa incluyendo el tipo de excepción, archivo donde
        ocurrió, línea de error y mensaje descriptivo.
        
        Args:
            e (Exception): La excepción que se quiere registrar. Debe ser una
                         instancia de Exception o sus subclases.
                         
        Note:
            - Automáticamente extrae información de traceback
            - Registra con nivel 'ERROR' 
            - Incluye: nombre de la excepción, archivo, línea, mensaje
            - Si ocurre un error al procesar la excepción, se registra
              internamente usando el sistema de logging del módulo
              
        Examples:
            >>> logger = Logger()
            >>> try:
            ...     resultado = 10 / 0
            ... except ZeroDivisionError as e:
            ...     logger.log_e(e)
            
            >>> try:
            ...     archivo = open('inexistente.txt')
            ... except FileNotFoundError as e:
            ...     logger.log_e(e)  # Registra error de archivo no encontrado
                
        See Also:
            __traceback(): Método interno que extrae información del traceback
            log(): Para registros informativos generales
        """
        try:
            # Extraer información detallada del traceback de la excepción
            trace: dict = self.__traceback(e)
            
            # Construir mensaje completo con toda la información relevante
            msg: str = f'Exception: {e.__class__.__name__} - File: {trace.get("path")} - ErrorLine: {trace.get("line")} - Message: {e}'
            
            # Registrar como error (nivel ERROR)
            self.__write(msg, 'error')
        except Exception as e:
            # Si ocurre algún error al procesar la excepción original,
            # registrarlo usando el sistema interno de logging
            self.__log(e)

    def __write(self, msg: str, log_type: Optional[str] = 'info') -> None:
        """Método privado para escribir mensajes formateados al archivo de log.
        
        Este método interno se encarga de la escritura real de mensajes al archivo,
        aplicando el formato estándar con timestamp, nivel de log y mensaje.
        
        Args:
            msg (str): Mensaje a escribir en el archivo
            log_type (Optional[str], optional): Nivel del log (info, error, warning, etc.).
                                              Defaults to 'info'.
                                              
        Note:
            - Formato: [NIVEL][YYYY-MM-DD HH:MM:SS.microseconds] - mensaje
            - El nivel se convierte automáticamente a mayúsculas
            - Añade salto de línea automáticamente
            - Los errores durante la escritura se capturan y registran internamente
            - TODO: Implementar soporte para múltiples archivos simultáneos
            
        Raises:
            Exception: Cualquier error durante la escritura se maneja internamente
                      mediante __log() sin propagarse al llamador
                      
        Internal Note:
            Este método es privado (__write) y no debe llamarse directamente.
            Es usado internamente por log() y log_e().
        """
        # TODO: Implementar soporte para múltiples archivos de log simultáneos
        # Feature: Mantener una lista de archivos abiertos para cerrarlos apropiadamente

        try:
            # Obtener timestamp actual con precisión completa
            __date: datetime = Dates.now_date()
            
            # Escribir mensaje con formato estándar al archivo
            # Formato: [NIVEL][TIMESTAMP] - mensaje\n
            self.file.writelines([f'[{log_type.upper()}][{__date}] - {msg}\n'])
        except Exception as e:
            # Si ocurre cualquier error durante la escritura,
            # registrarlo usando el sistema de logging interno del módulo
            self.__log(e)

    def __log(self, e: Exception) -> None:
        """Sistema de logging interno para errores del propio módulo.
        
        Este método privado maneja los errores que ocurren dentro del propio
        módulo chromologger. Crea un archivo de log separado específicamente
        para debug y mantenimiento del módulo.
        
        Args:
            e (Exception): Excepción interna del módulo que necesita ser registrada
            
        Note:
            - Crea un archivo log.log en el directorio del módulo (no del usuario)
            - Utiliza el mismo formato que los logs regulares
            - Muestra mensajes de error en consola usando chromolog
            - Extrae información completa de traceback
            - Maneja múltiples tipos de excepciones específicas
            
        Error Handling:
            - FileNotFoundError: Problemas de permisos o rutas
            - TypeError: Problemas de tipos de datos internos
            - SyntaxError: Problemas de sintaxis en código dinámico
            
        Internal Note:
            Este archivo de log interno es independiente del archivo del usuario
            y sirve para diagnosticar problemas del propio módulo chromologger.
        """
        try:
            # Extraer información detallada del traceback de la excepción interna
            trace: dict = self.__traceback(e)

            # Construir ruta para el archivo de logs internos del módulo
            # Se crea en el directorio del módulo, no en el del usuario
            __log_file_intern: str = FileManager.join_paths(current_path, 'log.log')

            # Mostrar error en consola para notificar al desarrollador
            # TODO: Implementar modo debug para controlar cuándo mostrar esto
            printer_chromolog.err(f'Revise el archivo "log" que se encuentra en esta ruta: {__log_file_intern}')

            # Escribir registro del error interno al archivo del módulo
            # Usa FileManager para escritura directa (no el sistema de logging regular)
            FileManager.write_plain_text_file(
                __log_file_intern, 
                f'[ERROR][{Dates.now_date()}] - Exception: {e.__class__.__name__} -File: {trace.get("path")} - ErrorLine: {trace.get("line")} - Message: {e}\n'
            )
        except FileNotFoundError as e: 
            # Error crítico: no se puede crear el archivo de log interno
            printer_chromolog.exc(e)
        except TypeError as e: 
            # Error de tipos de datos en el procesamiento interno
            printer_chromolog.exc(e)
        except SyntaxError as e: 
            # Error de sintaxis en operaciones dinámicas
            printer_chromolog.exc(e)

    def __traceback(self, e: Exception) -> dict:
        """Extrae información detallada de traceback de una excepción.
        
        Este método privado analiza el objeto de excepción y extrae información
        precisa sobre dónde y en qué línea ocurrió el error, proporcionando
        datos esenciales para el debugging.
        
        Args:
            e (Exception): Excepción de la cual extraer información de traceback
            
        Returns:
            dict: Diccionario con información del error:
                - 'line' (int): Número de línea donde ocurrió la excepción
                - 'path' (str): Ruta completa del archivo donde ocurrió la excepción
                
        Note:
            - Utiliza el módulo traceback de Python para análisis preciso
            - Extrae información del último frame del stack ([-1])
            - Proporciona tanto la línea como la ruta completa del archivo
            - Es utilizado internamente por log_e() y __log()
            
        Example:
            El diccionario retornado tiene la estructura:
            {
                'line': 42,
                'path': '/path/to/script.py'
            }
            
        Internal Note:
            Este método importa traceback localmente para evitar importaciones
            innecesarias si no se usan excepciones. Es un patrón de lazy loading.
        """
        # Importación local del módulo traceback para análisis de errores
        # Se hace aquí para evitar importaciones innecesarias si no hay errores
        import traceback
        
        # Extraer el traceback completo de la excepción
        trace_back = traceback.extract_tb(e.__traceback__)
        
        # Retornar información del último frame (donde realmente ocurrió el error)
        # [1] = línea, [0] = archivo/ruta
        return {
            'line': trace_back[-1][1],  # Número de línea del error
            'path': trace_back[-1][0]   # Ruta completa del archivo con error
        }