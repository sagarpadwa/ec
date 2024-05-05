#include <dht.h>

#define dht pin Ao

dht DHT

void Setup()

{

serial. begin (9600);

delay (500);

Serial. printan ("DHT II Humidity & temperature

delay(1000);

}

Sensor \n\n");

void loop()

{

DHT. read 11 (dht-apin); Serial.print ("Current humidity ="); Serial print("DHT. humidity"), Serial.print("%"); Serial.print("temperature"); Serial.print (DHT. temperature); serial. print in ("c");

delay (5000);

}

30/30