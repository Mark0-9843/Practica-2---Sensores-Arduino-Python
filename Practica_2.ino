// TEAM markoboquiñechainajesu

// ESTE CÓDIGO REALIZA UNA LECTURA DE SENSORES PARA POSTERIORMENTE MANDARLOS A PYTHON Y GUARDARLOS EN UN ARCHIVO CSV.

// 25 / 03 / 2025 - V. 2. 0. 0 - INTEGRACIÓN DE SENSORES Y PROCESAMIENTO DE DATOS CON ARDUINO-PYTHON.

#include <DHT.h> //incluye la libreria del sensor 

#define DHTPIN 3       // Pin digital donde está conectado el DHT11
#define DHTTYPE DHT11  // Definir el tipo de sensor DHT

DHT dht(DHTPIN, DHTTYPE);

const int potPin = A0; // Pin analógico donde está conectado el potenciómetro
const int sonidoPin = A1;


void setup() {
    Serial.begin(9600); //Inicia la comunicación serie 
    dht.begin(); // pone en funcionamiento el sensor y habilitar la lectura de temperatura y humedad 
}

void loop() {
    // Leer el valor del potenciómetro
    int valor_pot = analogRead(potPin);
    float voltaje = valor_pot * (5.0 / 1023.0); // Convertir a voltaje

    // Leer la temperatura y la humedad del DHT11
    float temperatura = dht.readTemperature(); // En grados Celsius
    float humedad = dht.readHumidity();
    
    int valor_audio = analogRead(sonidoPin); // Leer el valor del sensor de sonido
    
    // Enviar datos en formato CSV
    Serial.print(valor_pot);
    Serial.print(",");
    Serial.print(voltaje);
    Serial.print(",");
    Serial.print(temperatura);
    Serial.print(",");
    Serial.print(humedad);
    Serial.print(",");
    Serial.println(valor_audio); // Salto de línea al final

    delay(200); // Esperar medio segundo antes de la siguiente lectura
}
