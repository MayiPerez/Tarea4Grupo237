# ARCHIVO: servicio.py
from abc import ABC, abstractmethod
class Servicio(ABC):
 """
 Clase abstracta para los servicios.
 """
 def __init__(self, nombre, precio_base):
 self.nombre = nombre
 self.precio_base = precio_base
 @abstractmethod
 def calcular_costo(self):
 pass
 @abstractmethod
 def descripcion(self):
 pass
class Sala(Servicio):
 """
 Servicio de reserva de salas.
 """
 def calcular_costo(self, horas=1):
 return self.precio_base * horas
 def descripcion(self):
 return "Reserva de sala"
class Equipo(Servicio):
 """
 Servicio de alquiler de equipos.
 """
 def calcular_costo(self, dias=1):
 return self.precio_base * dias
 def descripcion(self):
 return "Alquiler de equipo"
class Asesoria(Servicio):
 """
 Servicio de asesoría especializada.
 """
 def calcular_costo(self, horas=1, descuento=0):
 costo = self.precio_base * horas
 return costo - (costo * descuento)
 def descripcion(self):
 return "Asesoría especializada"
