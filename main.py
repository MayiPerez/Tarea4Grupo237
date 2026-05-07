# ARCHIVO: main.py 

 

from cliente import Cliente 

from servicio import Sala, Equipo, Asesoria 

from reserva import Reserva 

from excepciones import ErrorSistema 

import datetime 

 

# Función para registrar errores en archivo 

def registrar_log(mensaje): 

    with open("logs.txt", "a") as archivo: 

        archivo.write(f"{datetime.datetime.now()} - {mensaje}\n") 

 

 

clientes = [] 

servicios = [] 

reservas = [] 

 

print("=== SIMULACIÓN DEL SISTEMA ===") 

 

# Simulación de 10 casos 

for i in range(10): 

    try: 

        # Crear cliente (caso inválido en i=3) 

        if i == 3: 

            cliente = Cliente("", "") 

        else: 

            cliente = Cliente(f"Cliente{i}", i) 

 

        clientes.append(cliente) 

 

        # Crear servicio 

        if i % 3 == 0: 

            servicio = Sala("Sala", 100) 

        elif i % 3 == 1: 

            servicio = Equipo("Equipo", 200) 

        else: 

            servicio = Asesoria("Asesoría", 300) 

 

        servicios.append(servicio) 

 

        # Crear reserva (caso inválido en i=5) 

        if i == 5: 

            reserva = Reserva(cliente, servicio, -1) 

        else: 

            reserva = Reserva(cliente, servicio, i + 1) 

 

        reservas.append(reserva) 

 

        # Procesar reserva 

        costo = reserva.procesar() 

        print(f"Reserva exitosa - Costo: {costo}") 

 

    except ErrorSistema as e: 

        print(f"Error controlado: {e}") 

        registrar_log(f"Error del sistema: {e}") 

 

    except Exception as e: 

        print(f"Error inesperado: {e}") 

        registrar_log(f"Error inesperado: {e}") 

 

print("=== FIN DE LA SIMULACIÓN ===") 
