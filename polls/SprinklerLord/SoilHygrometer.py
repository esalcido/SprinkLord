import Adafruit_BBIO.ADC as ADC
import time


class SoilHygrometer:
	def __init__(self, pinNum):
		self.pinNum = pinNum
	
	def setup(self):
		ADC.setup()

	def read(self):
		result = ADC.read(self.pinNum)
		return result


