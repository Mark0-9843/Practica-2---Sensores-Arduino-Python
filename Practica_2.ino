// TEAM markoboquiñechainajesu

// ESTE CÓDIGO REALIZA UNA LECTURA DE SENSORES PARA POSTERIORMENTE MANDARLOS A PYTHON Y GUARDARLOS EN UN ARCHIVO CSV.

// 27 / 03 / 2025 - V. 3. 0. 0 - INTEGRACIÓN DE SENSORES Y PROCESAMIENTO DE DATOS CON ARDUINO-PYTHON.

#include <DHT.h> //incluye la libreria del sensor 

#define DHTPIN 3       // Pin digital donde está conectado el DHT11
#define DHTTYPE DHT11  // Definir el tipo de sensor DHT

DHT dht(DHTPIN, DHTTYPE); //Crea un objeto DHT para interactuar con el sensor

const int potPin = A0; // Pin analógico donde está conectado el potenciómetro
const int sonidoPin = A1; // Define el pin analógico donde está conectado el sensor de sonido


void setup() {
    Serial.begin(9600); //Inicia la comunicación serie 
    dht.begin(); // pone en funcionamiento el sensor y habilitar la lectura de temperatura y humedad 
}

void loop() {
    // Leer el valor del potenciómetro
    int valor_pot = analogRead(potPin); // Obtiene el valor analógico del potenciómetro
    float voltaje = valor_pot * (5.0 / 1023.0); // Convertir a voltaje

    // Leer la temperatura y la humedad del DHT11
    float temperatura = dht.readTemperature(); // En grados Celsius
    float humedad = dht.readHumidity(); // Leer la humedad relativa desde el sensor DHT1
    
    int valor_audio = analogRead(sonidoPin); // Leer el valor del sensor de sonido
    
    // Enviar datos en formato CSV
    Serial.print(valor_pot); // Imprime el valor del potenciómetro
    Serial.print(","); // Separador de datos
    Serial.print(voltaje); // Imprime el voltaje calculado
    Serial.print(","); // Separador de datos
    Serial.print(temperatura); // Imprime la temperatura
    Serial.print(","); // Separador de datos
    Serial.print(humedad); // Imprime la humedad
    Serial.print(","); // Separador de datos
    Serial.println(valor_audio); // Salto de línea al final

    delay(200); // Esperar medio segundo antes de la siguiente lectura
}
