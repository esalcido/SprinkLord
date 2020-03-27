#!/usr/bin/env python
#Created by Edward Salcido 4/16/2019

from Relay import *
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_12", GPIO.OUT)
# This will set the output to high, making sure the relay is off.
#GPIO.output("P8_12", GPIO.HIGH)

GPIO.output("P8_12", GPIO.LOW)
sleep(1)
GPIO.output("P8_12", GPIO.HIGH)



relay = Relay("P8_12")
relay.setup()
relay.on()
relay.off()

relay.cleanup()