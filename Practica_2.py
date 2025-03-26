# TEAM markoboquiñechainajesu

# ESTE CÓDIGO REALIZA UNA LECTURA DE DATOS DE SENSORES ENVIADOS POR ARDUINO PARA POSTERIORMENTE GUARDARLOS EN UN ARCHIVO CSV.

# 25 / 03 / 2025 - V. 2. 0. 0 - INTEGRACIÓN DE SENSORES Y PROCESAMIENTO DE DATOS CON ARDUINO-PYTHON.

import serial
import csv
import time

# Configurar el puerto serial 
PUERTO_SERIAL = "COM3"
BAUD_RATE = 9600
ARCHIVO = "datos_sensores.csv"

# Abrir conexión serial
arduino = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=1)
time.sleep(2)  # Esperar a que el Arduino inicie

# Crear y abrir el archivo CSV
with open(ARCHIVO, mode="w", newline="") as file:
    escribir = csv.writer(file)
    escribir.writerow(["Potenciometro", "Voltaje (V)", "Temperatura (°C)", "Humedad (%)"])  # Encabezados

    try:
        while True:
            linea = arduino.readline().decode().strip()  # Leer línea y decodificar
            if linea:
                datos = linea.split(",")  # Separar valores por coma
                if len(datos) == 4:  # Verificar que sean 4 valores
                    escribir.writerow(datos)  # Guardar en el CSV
                    print("Datos guardados:", datos)
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
    finally:
        arduino.close()  # Cerrar el puerto serial
