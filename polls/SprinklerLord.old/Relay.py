# This will import the GPIO library.
import Adafruit_BBIO.GPIO as GPIO
import logging
from time import sleep

class Relay:
	def __init__(self, pinNum):
		self.pinNum = pinNum
		self.state = 0
		
	def setup(self):
		#Configure the logger.
		#logging.basicConfig(filename='sprinklerOOP.log',format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')
		# This will setup the pin as an output.
		GPIO.setup(self.pinNum, GPIO.OUT)
		# This will set the output to high, making sure the relay is off.
		GPIO.output(self.pinNum, GPIO.HIGH)


	def on(self):
		self.state = 1
		GPIO.output(self.pinNum, GPIO.LOW)
		logging.info("turning on relay "+ self.pinNum)
		#GPIO.cleanup()
		sleep(1)

	def off(self):
		self.state = 0
		GPIO.output(self.pinNum, GPIO.HIGH)
		logging.info("turning off relay "+ self.pinNum)
		#GPIO.cleanup()
		sleep(1)

	def cleanup(self):
		GPIO.cleanup()
