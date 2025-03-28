# TEAM markoboquiñechainajesu

# ESTE CÓDIGO REALIZA UNA LECTURA DE DATOS DE SENSORES ENVIADOS POR ARDUINO PARA POSTERIORMENTE GUARDARLOS EN UN ARCHIVO CSV.

# 27 / 03 / 2025 - V. 3. 0. 0 - INTEGRACIÓN DE SENSORES Y PROCESAMIENTO DE DATOS CON ARDUINO-PYTHON.

import serial #Se usa para enviar y recibir datos entre dispositivos
import csv  #se usa para leer y escribir archivos en formato CSV
import time time  #proporciona funciones para manejar el tiempo y pausas en la ejecución del código.

# Configurar el puerto serial 
PUERTO_SERIAL = "COM3" 
BAUD_RATE = 9600
ARCHIVO = "datos_sensores.csv"

# Abrir conexión serial
arduino = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=1)
time.sleep(2)  # Esperar a que el Arduino inicie

# Crear y abrir el archivo CSV
with open(ARCHIVO, mode="w", newline="") as file: : #Abre un archivo con nombre ARCHIVO,Si el archivo ya existe, se sobrescribirá,Usa with, lo que garantiza que el archivo se cierre automáticamente.
    escribir = csv.writer(file) # permite escribir datos en un archivo de manera estructurada
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
