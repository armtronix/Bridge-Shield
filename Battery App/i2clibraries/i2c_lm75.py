from i2clibraries import i2c
import math
from time import *


class i2c_lm75:
		ReadID = 0x00

		def __init__(self, port, addr=0x48):
				self.bus = i2c.i2c(port, addr)

		def __str__(self):
					ret_str = ""
					(x) = self.getTemp() 
					ret_str += "T:    "+str(x)+"\n"
					return ret_str

		def getTemp(self):
				scaleFactor =1
				(temp)= self.bus.read_16bittemp(self.ReadID, True)
				return (temp * scaleFactor)
