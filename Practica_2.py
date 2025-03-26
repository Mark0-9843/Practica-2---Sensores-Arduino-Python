# TEAM markoboquiñechainajesu

# ESTE CÓDIGO REALIZA UNA LECTURA DE DATOS DE SENSORES ENVIADOS POR ARDUINO PARA POSTERIORMENTE GUARDARLOS EN UN ARCHIVO CSV.

# 25 / 03 / 2025 - V. 1. 0. 0 - INTEGRACIÓN DE SENSORES Y PROCESAMIENTO DE DATOS CON ARDUINO-PYTHON.

import serial
import time

# Configura el puerto serie (cambia 'COM4' por tu puerto Arduino)
arduino = serial.Serial ('COM4', 9600, timeout=1)

try:
    while True:
        if arduino.in_waiting > 0:
            linea = arduino.readline().decode('utf-8').strip()
            
            if linea.startswith("TEMP:"):
                temperatura = float(linea.split(":")[1])  # Extrae el valor numérico
                print(f"Temperatura recibida: {temperatura} °C")

except KeyboardInterrupt:
    print("Interrupción por usuario. Cerrando conexión.")
    arduino.close()
