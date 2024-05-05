#include <SPI.h>

#indude <MFRC522.h> #define SS. PIN 10 #define RST-PIN 9 MFR C522 mfrc 522 (SS. PIN, RST. PIN); void setup()

{ Serial, begin (9600); SPI.begin(); mfrc 522. PC D. Init(); Serial, print In ("Approximate your card to the reader...");

Serial.printin();

} void loop()

{ if (!mfrc 522. PICC-IS Newcard Present())

{ return;

if (!mfrc 522. PICC Read Card serial c))

{ return;

Serial.print ("110 tag");

string content="";

byte letter,

for (byte i=0; i<mfrc 522. uid. size; itt)

{

Serial.print(mfrc 522 .uid.uid Byte [i] <0×10? "0":"");

Serial.print (mfrc 522.uid.uid Byte [i], HEX); content.concat (string (mfrc 522.uid.uid Byte [i]< oxlo "o"." "));

content.concat (string (mfrcs22, uid, uid Byte [1]. HEX));

CS CamScanner

1

serial print An();

Serial.print("Message:")

content. to. Upper Case()i

if (content. Substring (1) = =" Fg 21 E4 D5 ") {

Serial.print In ("Authorized access"); serial printin()

delay (3000);

Serial printan ("Access denied");

delay (3000);

}

else

{

}

}