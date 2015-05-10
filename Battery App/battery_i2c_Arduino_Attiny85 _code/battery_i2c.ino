

#include "TinyWireS.h"                  // wrapper class for I2C slave routines

#define I2C_SLAVE_ADDR  0x26            // i2c slave address (38)

#define analogInPina3  A3  // Analog input pin that is PB3 for power good 
#define analogInPina4  A2   //Analog input pin that is PB4 for battery charge level

int readVala3=0;
byte hia3;
byte loa3;
int readVala4=0;
byte hia4;
byte loa4;
int count=0;

void setup()
{
  
  TinyWireS.begin(I2C_SLAVE_ADDR);      // init I2C Slave mode
  TinyWireS.onRequest(requestEvent);
}


void loop()
{
  
    readVala3 = analogRead(analogInPina3);
    hia3 = highByte(readVala3);
    loa3 = lowByte(readVala3);
    readVala4 = analogRead(analogInPina4);
    hia4 = highByte(readVala4);
    loa4 = lowByte(readVala4);  
  
}


void requestEvent()
{ 
  byte byteRcvd = 0;

  byteRcvd = TinyWireS.receive();     // get the byte from master
    if(byteRcvd==0x05)
    { 
     TinyWireS.send(hia3);
    }
    else if(byteRcvd==0x06)
   {
     TinyWireS.send(loa3);
   }
    else if(byteRcvd==0x07)
    {
     TinyWireS.send(hia4);
    }
    else if(byteRcvd==0x08)
    {
     TinyWireS.send(loa4);
    }
    else
    {
     TinyWireS.send(255);
    }
}



