# ARCHIVO: cliente.py

from abc import ABC, abstractmethod
from excepciones import ErrorValidacion

class Entidad(ABC):
    """
    Clase abstracta base del sistema.
    """

    @abstractmethod
    def mostrar_info(self):
        pass


class Cliente(Entidad):
    """
    Clase que representa un cliente.
    """

    def __init__(self, nombre, identificacion):
        # Validación de datos
        if not nombre or not identificacion:
            raise ErrorValidacion("Datos del cliente inválidos")

        # Encapsulación
        self.__nombre = nombre
        self.__identificacion = identificacion

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - ID: {self.__identificacion}"

    # Métodos getter
    def get_nombre(self):
        return self.__nombre

    def get_identificacion(self):
        return self.__identificacion
