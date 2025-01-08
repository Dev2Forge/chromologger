"""Easylog es un módulo diseñado para facilitar la creación de registros (logs).

Diseñado para usarlo en aplicaciones desarrolladas con Python. 
Proporciona una manera sencilla y estructurada de documentar eventos, 
errores y actividades en los programas, mejorando la capacidad de monitoreo y 
depuración del código.

Requerimientos: 
    - chromolog==0.2.0

Historial de versiones:
    - v0.1.0: Versión inicial

Para saber más sobre el módulo, visite: [easylog](https://tutosrivegamerlq.github.io/easylog/)

@author Tutos Rive Gamer
"""


from io import TextIOWrapper
from datetime import datetime
# from msqlite.__print import Print
from chromolog import Print
import traceback
import os

__version__ = "0.1.0"
__author__ = "Tutos Rive Gamer"

# Ruta absoluta de este módulo
current_path:str = os.path.dirname(__file__)
# Escribir mensajes por consola con colores
p:Print = Print()

class Logger:
    """Escribir registros de ejecución en archivos y almacenar sus registros claros y con fechas de ejecución exactas
    """
    def __init__(self, name:str = 'log.log') -> None:
        # Nombre del archivo
        self.name:str = name
        # Archivo abierto
        self.file:TextIOWrapper = self.__open()
        # Ruta absoluta del archivo
        self.path:str
    
    def __open(self) -> TextIOWrapper | int:
        """Abrir archivos

        Returns:
            `TextIOWrapper`: Archivo
                o
            `int`: `-1`: Error
        """
        try:
            self.path = os.path.abspath(self.name)
            # Retornar archivo
            return open(self.name, 'a', encoding='utf-8')
        except FileNotFoundError as e:
            # Escribir un resgistro "interno"
            self.__log(e)
            return -1

    def log(self, msg:any) -> None:
        """Crear registros

        Args:
            `msg:str`: Mensaje que se quiere registrar 
        """
        # Escribir mensaje de registro
        self.__write(self.__date(), msg)
        # Mostrar ruta del archivo log.log
        p.inf(f'Revise {self.path} para ver los registros.')
    
    def log_e(self, e: Exception) -> None:
        """Regiistrar errores (`Excepcition`)

        Args:
            `e:Exception`: Excepción conla cual se trabajará
        """
        trace:dict = self.__traceback(e)
        msg:str = f'Exception: {e.__class__.__name__} - File: {trace.get('path')} - ErrorLine: {trace.get('line')} - Messsage: {e}'
        self.log(msg)

    def __write(self, date:datetime, msg:str) -> int:
        """Escribir registros

        Args:
            `msg:str`: Mensaje del registro que se escribirá

        Returns:
            `int`: Cantidad de caracteres escritos:
                `-1`: Ocurrió una `excepción`
                `>= 0`: Caracteres escritos
        """
        try:
            # Escribir mensaje en archivo
            self.file.writelines([f'{date} - {msg}\n'])
        except TypeError as e:
            # Crear registro en módulo
            self.__log(e)
            return -1
    
    def __date(self) -> datetime:
        """Obtener la fecha-hora actual

        Returns:
            `datetime`: Hora actual (Obtenida con `datetime.datetime.now()`)
        """
        return datetime.now()

    def __log(self, e:Exception) -> int:
        """Crear registros "internos" (Del propio módulo)

        Args:
            `e:Exception`: Excepción "capturada"

        Returns:
            `int`: Cantidad de caracteres escritos:
                `-1`: Ocurrió una `excepción`
                `>= 0`: Caracteres escritos
        """
        state:int
        try:
            # Registro de excepciones (Ruta de archivo y línea de error)
            trace:dict = self.__traceback(e)
            # Ruta absoluta de este archivo
            filename:str = os.path.join(current_path, 'log.log')
            p.err(f'Revise el archivo "log" que se encuentra en esta ruta: {filename}')
            # Escribir registro del error "interno"
            with open(filename, 'a', encoding='utf-8') as f:
                w = f.writelines([f'{self.__date()} - Exception: {e.__class__.__name__} -File: {trace.get('path')} - ErrorLine: {trace.get('line')} - Messsage: {e}\n'])
                f.close() 
                state = w
        except FileNotFoundError as e:
            state = -1
            p.exc(e)
        except TypeError as e:
            state = -1
            p.exc(e)
        except SyntaxError as e:
            state = -1
            p.exc(e)
        # Estado del registro
        return state

    def __traceback(self, e:Exception) -> dict:
        """Obtener un registro preciso de la excepción

        Args:
            `e:Exception`: Exceeption con la cual se trabajará

        Returns:
            `dict`: Diccionario con claves: line (Línea del error), path (Ruta del archivo de error)
        """
        trace_back = traceback.extract_tb(e.__traceback__)
        return {'line': trace_back[-1][1], 'path': trace_back[-1][0]}