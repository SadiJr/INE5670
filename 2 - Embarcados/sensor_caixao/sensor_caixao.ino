#include "pitches.h"

int melody[] = {
  NOTE_AS4, NOTE_AS4, NOTE_AS4, NOTE_AS4,
  NOTE_AS4, NOTE_AS4, NOTE_AS4, NOTE_AS4,
  NOTE_AS4, NOTE_AS4, NOTE_AS4, NOTE_AS4,
  NOTE_AS4, NOTE_AS4, NOTE_AS4, NOTE_AS4,
  NOTE_AS4, NOTE_AS4, NOTE_AS4, NOTE_AS4,
  NOTE_D5, NOTE_D5, NOTE_D5, NOTE_D5,
  NOTE_C5, NOTE_C5, NOTE_C5, NOTE_C5,
  NOTE_F5, NOTE_F5, NOTE_F5, NOTE_F5,
  NOTE_G5, NOTE_G5, NOTE_G5, NOTE_G5,
  NOTE_G5, NOTE_G5, NOTE_G5, NOTE_G5,
  NOTE_G5, NOTE_G5, NOTE_G5, NOTE_G5,
  NOTE_C5, NOTE_AS4, NOTE_A4, NOTE_F4,
  NOTE_G4, 0, NOTE_G4, NOTE_D5,
  NOTE_C5, 0, NOTE_AS4, 0,
  NOTE_A4, 0, NOTE_A4, NOTE_A4,
  NOTE_C5, 0, NOTE_AS4, NOTE_A4,
  NOTE_G4, 0, NOTE_G4, NOTE_AS5,
  NOTE_A5, NOTE_AS5, NOTE_A5, NOTE_AS5,
  NOTE_G4, 0, NOTE_G4, NOTE_AS5,
  NOTE_A5, NOTE_AS5, NOTE_A5, NOTE_AS5,
  NOTE_G4, 0, NOTE_G4, NOTE_D5,
  NOTE_C5, 0, NOTE_AS4, 0,
  NOTE_A4, 0, NOTE_A4, NOTE_A4,
  NOTE_C5, 0, NOTE_AS4, NOTE_A4,
  NOTE_G4, 0, NOTE_G4, NOTE_AS5,
  NOTE_A5, NOTE_AS5, NOTE_A5, NOTE_AS5,
  NOTE_G4, 0, NOTE_G4, NOTE_AS5,
  NOTE_A5, NOTE_AS5, NOTE_A5, NOTE_AS5

};

int noteDurations[] = {
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
  4, 4, 4, 4,
};

// Distancia minima para apitar o alarme e acende o LED vermelho. Usa cm.
unsigned const int MIN_DISTANCE = 30;

// Portas usadas na placa para o TRIG e ECHO do sensor
unsigned const int TRIG = 3; // Recebe o pulso sonoro
unsigned const int ECHO = 2; // Envia o pulso sonoro

// Portas dos LEDs e do Buzzer
unsigned const int GREEN = 7;
unsigned const int RED = 8;
unsigned const int BUZZER = 9;

// Intervalo do loop
unsigned const int LOOP = 100;

// Variaveis para funcionamento do Buzzer, declaradas aqui pra alocar somente uma vez.
float seno;
unsigned int frequency;

void setup() {
  Serial.begin(9600);

  // Configura sensor
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  // Configura LEDs
  pinMode(GREEN, OUTPUT);
  pinMode(RED, OUTPUT);

  // Configura Buzzer
  pinMode(BUZZER, OUTPUT);
}

void loop() {
  int distance = sensor();

  if (distance <= MIN_DISTANCE) {
    Serial.print("Distância mínima atingida/ultrapassada: ");
    Serial.print(distance);
    Serial.println(" cm.");

    // Desliga LED verde, liga LED vermelho e toca o alarme
    digitalWrite(GREEN, LOW);
    digitalWrite(RED, HIGH);
    coffin();
  } else {
    Serial.print("Possível objeto à: ");
    Serial.print(distance);
    Serial.println(" cm.");

    digitalWrite(GREEN, HIGH);
    digitalWrite(RED, LOW);
    noTone(BUZZER);
  }
  delay(LOOP);
}

int sensor() {
  // Funciona igual um sensor de morcego
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  // O uso do 58 pode ser entendido na documentação oficial:https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf
  // Mas, sinceramente, não li muito a fundo, já que explicações detalhadas envolvem a física das ondas.
  return pulseIn(ECHO, HIGH) / 58;
}

// Musiquinha do caixão, encontrada em: https://create.arduino.cc/projecthub/Shubham_Desai/astronomia-coffin-dance-song-using-arduino-buzzer-044783
void coffin() {
  for (int thisNote = 0; thisNote < 112; thisNote++)
  {

    int noteDuration = 750 / noteDurations[thisNote];
    tone(BUZZER, melody[thisNote], noteDuration);

    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);

    noTone(BUZZER);
  }
}
