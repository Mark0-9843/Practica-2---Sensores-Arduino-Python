// TEAM markoboquiñechainajesu

// ESTE CÓDIGO REALIZA UNA LECTURA DE SENSORES PARA POSTERIORMENTE MANDARLOS A PYTHON Y GUARDARLOS EN UN ARCHIVO CSV.

// 25 / 03 / 2025 - V. 1. 0. 0 - INTEGRACIÓN DE SENSORES Y PROCESAMIENTO DE DATOS CON ARDUINO-PYTHON.

void setup() {
  Serial.begin(9600); // Inicia comunicación serial a 9600 baudios
}

void loop() {
  // Simula lectura de temperatura (ejemplo con sensor LM35)
  float temperatura = analogRead(A0) * 0.488; // Conversión a grados Celsius
  Serial.print("TEMP:"); // Encabezado para identificar el dato
  Serial.println(temperatura); // Envía el valor por serial
  delay(1000); // Espera 1 segundo entre lecturas
}
