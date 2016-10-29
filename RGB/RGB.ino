int LED_R = 9;
int LED_G = 10;
int LED_B = 11;

int rojo = 0;
int verde = 0;
int azul = 0;

byte flag = 0;

void setup()
{
  Serial.begin(9600);
  randomSeed(analogRead(0));

  pinMode(LED_R, INPUT);
  pinMode(LED_G, INPUT);
  pinMode(LED_B, INPUT);
}

void loop()
{
  while(Serial.available() > 1) // Para leer al menos dos bytes
  {
    flag = Serial.read();

    switch(flag)
    {
      case 'r':
        rojo = Serial.parseInt();
        break;
      case 'g':
        verde = Serial.parseInt();
        break;
      case 'b':
        azul  = Serial.parseInt();
        break;
    }
  }

  colorLed(rojo, verde, azul);
  delay(100);
}

void colorLed(byte r, int g, int b)
{
  analogWrite(LED_R, r);
  analogWrite(LED_G, g);
  analogWrite(LED_B, b);
}
