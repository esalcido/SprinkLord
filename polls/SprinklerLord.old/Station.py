# This will import the GPIO library.
import Adafruit_BBIO.GPIO as GPIO
import logging
from Relay import Relay
#jf3poem 
class Station(Relay):
	def __init__(self, name,pinNum):
		Relay.__init__(self, pinNum)
		self.name = name
		self.relayName = pinNum
		self.active = 0

		