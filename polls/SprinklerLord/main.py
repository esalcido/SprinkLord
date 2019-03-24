#!/usr/bin/env python
#Created by Edward Salcido 11/27/2018
#from Relay import *
from Station import *
from Schedule import *
import logging
from SoilHygrometer import *
# This will import the sleep function for the timer below.
from time import sleep
import requests
import json

logging.basicConfig(filename='sprinklerOOP.log',format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')

#Duration 
#durationInMin = 8 * 60
durationInMin = 5

#set up the relay objects
relays= ["P8_8","P8_9"]

#use a dictionary comprehension to create Stations
holder = {pinNum:Station(name = pinNum,pinNum=pinNum) for pinNum in relays}

for  x in holder:
	holder[x].setup()
	print("Station name is "+holder[x].name +". Station pinNum is "+holder[x].pinNum)



# This is a timer that will pause for 1 second.
sleep(1)

#check to see if it is raining
lat = "34.203194"
lon = "-118.371566"
url = "https://api.openweathermap.org/data/2.5/weather?appid=b7057926f8211721b670ca7795400a58&lat="+lat+"&lon="+lon

r = requests.get(url)
print r.json()

weather_data = r.json()

weather = weather_data['weather'][0]['main']
print "weather is "+ str(weather)

if (weather == "Rain") or (weather =="Light Rain"):
	logging.info('weather is '+ str(weather) )
else:
	#create schedule to run through all stations
	schl = Schedule(durationInMin, holder)
	#schl.runSchedule()

soilMeter = SoilHygrometer("P9_39")
soilMeter.setup()
reading = soilMeter.read()

print ("soil level is "+ str(reading)) 
