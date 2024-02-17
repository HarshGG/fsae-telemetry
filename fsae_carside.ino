#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// CE and CSN pin assignments
RF24 radio(28, 34);

const byte address[6] = "00001";
char dataToSend[32] = "Hello World";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}

void loop() {
  const bool result = radio.write(&dataToSend, sizeof(dataToSend));
  if (result) {
    Serial.println("Data sent successfully");
  } else {
    Serial.println("Sending failed");
  }
  delay(1000);
}
