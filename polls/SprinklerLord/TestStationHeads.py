#!/usr/bin/env python
#Created by Edward Salcido 11/27/2018
#from Relay import *
from Station import *
from Schedule import *
from Relay import *

# This will import the sleep function for the timer below.
from time import sleep


#Duration 
durationInMin = 8 * 60
#durationInMin = 5

#set up the relay objects
relays= ["P8_8","P8_9"]

# #use a dictionary comprehension to create Stations
# holder = {pinNum:Station(name = pinNum,pinNum=pinNum) for pinNum in relays}

# for  x in holder:
# 	holder[x].setup()
# 	print("Station name is "+holder[x].name +". Station pinNum is "+holder[x].pinNum)


relay1 = Relay("P8_8")
relay2 = Relay("P8_8")

relay1.setup()
relay2.setup()

relay1.on()
sleep(120)
relay1.off()

relay2.on()
sleep(120)
relay2.off()