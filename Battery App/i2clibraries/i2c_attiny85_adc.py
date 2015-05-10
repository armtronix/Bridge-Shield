from i2clibraries import i2c
import math
from time import *


class i2c_attiny85_adc:
		ReadID_Adc03H = 0x05
		ReadID_Adc03L = 0x06
		ReadID_Adc02H = 0x07
		ReadID_Adc02L = 0x08

		def __init__(self, port, addr=0x26):
			self.bus = i2c.i2c(port, addr)
		
		def __str__(self):
			ret_str = ""
		
			(adc02) = self.getadc02()
			(adc03) = self.getadc03() 
			ret_str += "ADC02:    "+str(adc02)+"\n"
			ret_str += "ADC03:    "+str(adc03)+"\n"
			return ret_str

		def getAdc02(self):
			scaleFactor =1
			#(adc02)= self.bus.read_16bit(self.ReadID_Adc02, True)
			(adc02H)= self.bus.read_byte(self.ReadID_Adc02H)
			(adc02L)= self.bus.read_byte(self.ReadID_Adc02L)
			(adc02)=((adc02H) << 8) | (adc02L)
			return (adc02 * scaleFactor)		

		def getAdc03(self):
			scaleFactor =1
			(adc03H)= self.bus.read_byte(self.ReadID_Adc03H)
			(adc03L)= self.bus.read_byte(self.ReadID_Adc03L)
			(adc03)=((adc03H) << 8) | (adc03L)
			#(adc03)= self.bus.read_16bit(self.ReadID_Adc03, True)
			return (adc03 * scaleFactor)

