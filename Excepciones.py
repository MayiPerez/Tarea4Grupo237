# ARCHIVO: excepciones.py

# Este archivo define las excepciones personalizadas del sistema

class ErrorSistema(Exception):
    """
    Clase base para todos los errores del sistema.
    """
    pass


class ErrorValidacion(ErrorSistema):
    """
    Se usa cuando hay errores en los datos ingresados.
    """
    pass


class ErrorReserva(ErrorSistema):
    """
    Se usa cuando ocurre un problema en las reservas.
    """
    pass
