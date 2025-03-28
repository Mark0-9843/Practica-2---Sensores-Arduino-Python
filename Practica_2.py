# TEAM markoboquiñechainajesu

# ESTE CÓDIGO REALIZA UNA LECTURA DE DATOS DE SENSORES ENVIADOS POR ARDUINO PARA POSTERIORMENTE GUARDARLOS EN UN ARCHIVO CSV.

# 27 / 03 / 2025 - V. 3. 0. 0 - INTEGRACIÓN DE SENSORES Y PROCESAMIENTO DE DATOS CON ARDUINO-PYTHON.

import serial #Se usa para enviar y recibir datos entre dispositivos
import csv  #se usa para leer y escribir archivos en formato CSV
import time time  #proporciona funciones para manejar el tiempo y pausas en la ejecución del código.

# Configurar el puerto serial 
PUERTO_SERIAL = "COM3" # Define el puerto donde está conectado el Arduino (cambiar si es necesario)
BAUD_RATE = 9600 # Velocidad de comunicación serial en baudios (debe coincidir con el valor en Arduino)
ARCHIVO = "datos_sensores.csv" # Nombre del archivo donde se guardarán los datos

# Abrir conexión serial
arduino = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=1) # Establece la conexión con el puerto serie
time.sleep(2)  # Esperar a que el Arduino inicie 
# Crear y abrir el archivo CSV
with open(ARCHIVO, mode="w", newline="") as file: : #Abre un archivo con nombre ARCHIVO,Si el archivo ya existe, se sobrescribirá,Usa with, lo que garantiza que el archivo se cierre automáticamente.
    escribir = csv.writer(file) # permite escribir datos en un archivo de manera estructurada
    escribir.writerow(["Potenciometro", "Voltaje (V)", "Temperatura (°C)", "Humedad (%)"])  # Encabezados

    try:
         # Bucle infinito para leer datos continuamente desde Arduino
        while True: # Se ejecuta indefinidamente hasta que se interrumpa manualmente
            linea = arduino.readline().decode().strip()  # Leer línea y decodificar
            if linea: # Verificar que la línea no esté vacía
                datos = linea.split(",")  # Separar valores por coma
                if len(datos) == 4:  # Verificar que sean 4 valores
                    escribir.writerow(datos)  # Guardar en el CSV
                    print("Datos guardados:", datos) # Imprimir los datos guardados en la consola
    except KeyboardInterrupt:  # Captura la interrupción del teclado (Ctrl + C)
        print("\nPrograma terminado por el usuario.") # Mensaje de finalización
    finally:   #  se asegura el cierre del puerto serial
        arduino.close()  # Cerrar el puerto serial
