/*********************************************************************
This is an example for our Monochrome OLEDs based on SSD1306 drivers

  Pick one up today in the adafruit shop!
  ------> http://www.adafruit.com/category/63_98

This example is for a 128x64 size display using I2C to communicate
3 pins are required to interface (2 I2C and one reset)

Adafruit invests time and resources providing this open source code, 
please support Adafruit and open-source hardware by purchasing 
products from Adafruit!

Written by Limor Fried/Ladyada  for Adafruit Industries.  
BSD license, check license.txt for more information
All text above, and the splash screen must be included in any redistribution
*********************************************************************/

#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);

#define NUMFLAKES 10
#define XPOS 0
#define YPOS 1
#define DELTAY 2


int relay01 = 2;
int relay02 = 3;


#define LOGO16_GLCD_HEIGHT 16 
#define LOGO16_GLCD_WIDTH  16 
static const unsigned char PROGMEM logo16_glcd_bmp[] =
{ B00000000, B11000000,
  B00000001, B11000000,
  B00000001, B11000000,
  B00000011, B11100000,
  B11110011, B11100000,
  B11111110, B11111000,
  B01111110, B11111111,
  B00110011, B10011111,
  B00011111, B11111100,
  B00001101, B01110000,
  B00011011, B10100000,
  B00111111, B11100000,
  B00111111, B11110000,
  B01111100, B11110000,
  B01110000, B01110000,
  B00000000, B00110000 };

#if (SSD1306_LCDHEIGHT != 64)
#error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif

void setup()   {                
  Serial.begin(115200);
  pinMode(relay01, OUTPUT);
  pinMode(relay02, OUTPUT);
  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3D (for the 128x64).
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println("Hello, world!");
  delay(3000);
  esp8266_setup();

}

void esp8266_setup()
{
 Serial.println("AT+RST");
 delay(3000);
 display_serial();
 Serial.println("AT");
 delay(2000);
 display_serial();
 Serial.println("AT+CIFSR");
 delay(3000);
 display_serial();
 Serial.println("AT+CIPMUX=1");
 delay(2000);
 display_serial();
 Serial.println("AT+CIPSERVER=1,8050");
 delay(2000);
 display_serial();
 
}


void loop() {
   display_serial_loop();
   serialFlush();
  
}


void serialFlush()
{
  while(Serial.available() > 0) 
  {
    char t = Serial.read();
  }
  
}  


unsigned long display_serial() 
{
char data[100];
char m;
while (Serial.available() > 0)
    {  
      for(m=0; m<100; m++) 
        {
         if (Serial.available() > 0) 
          {
           data[m]=Serial.read();
          }
         else 
          {
           data[m]=0;
          }
    }
 
   }
  
  display.fillScreen(BLACK);
  display.setCursor(0, 0);
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.print(data);
  display.display();
    
}


unsigned long display_serial_loop() 
{
char data[12];
  char m;


  
  while (Serial.available() > 0)
       { 
         if (Serial.available() > 0) 
          {
            if(Serial.find("+IPD"))
             {
               for(m=0; m<12; m++) 
                 {
                  data[m]=Serial.read();
                  delay(200);
                 }   
             }
           }
         
       }

    
      if((data[6]=='O')&&(data[7]=='n')&&(data[8]=='1'))
     {
      Serial.println("AT+CIPSEND=0,17");
      delay(2000);
      Serial.println("Relay one is on"); 
      digitalWrite(relay01, HIGH);
      display.fillScreen(BLACK);
      display.setCursor(0, 5);
      display.setTextColor(WHITE);
      display.setTextSize(1);
      display.print("Relay one is on");
      display.display();
      for(m=0; m<12; m++) 
        {
         data[m]=0;
         
        }
     }
    else if((data[6]=='O')&&(data[7]=='n')&&(data[8]=='2'))
     {
      Serial.println("AT+CIPSEND=0,17");
      delay(2000);
      Serial.println("Relay two is on"); 
      digitalWrite(relay02, HIGH);
      display.fillScreen(BLACK);
      display.setCursor(0, 10);
      display.setTextColor(WHITE);
      display.setTextSize(1);
      display.print("Relay two is on");
      display.display();
      for(m=0; m<12; m++) 
        {
         data[m]=0;
         
        }
     }
    else if((data[6]=='O')&&(data[7]=='f')&&(data[8]=='f')&&(data[9]=='1'))
     {
      Serial.println("AT+CIPSEND=0,18");
      delay(2000);
      Serial.println("Relay one is off"); 
      digitalWrite(relay01, LOW);
      display.fillScreen(BLACK);
      display.setCursor(0, 5);
      display.setTextColor(WHITE);
      display.setTextSize(1);
      display.print("Relay one is off");
      display.display();
      for(m=0; m<12; m++) 
        {
         data[m]=0;
         
        }  
     }
    else if((data[6]=='O')&&(data[7]=='f')&&(data[8]=='f')&&(data[9]=='2'))
     {
      Serial.println("AT+CIPSEND=0,18");
      delay(2000);
      Serial.println("Relay two is off"); 
      digitalWrite(relay01, HIGH);
      display.fillScreen(BLACK);
      display.setCursor(0, 10);
      display.setTextColor(WHITE);
      display.setTextSize(1);
      display.print("Relay two is off");
      display.display();
      for(m=0; m<12; m++) 
        {
         data[m]=0;
         
        }
     }
    

   
   
  
    
}





