from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from polls.SprinklerLord.Station import *
from polls.SprinklerLord.Schedule import *
import logging

def runProgram():
	print "at updater start. from program"

	durationInMin = 5

	#set up the relay objects
	relays= ["P8_8","P8_9"]

	try:
		#use a dictionary comprehension to create Stations
		holder = {pinNum:Station(name = pinNum,pinNum=pinNum) for pinNum in relays}
		#station1 = Station("P8_8","P8_8")
		#station2 = Station("P8_9","P8_9")

		#holder={station1,station2}
		print "Setting up relays"
		logging.info("Setting up relays")
		for  x in holder:
			holder[x].setup()
			print("Station name is "+holder[x].name +". Station pinNum is "+holder[x].pinNum)


		# This is a timer that will pause for 1 second.
		sleep(1)

		#create schedule to run through all stations
		sch1 = Schedule(durationInMin, holder)
		sch1.runSchedule()

	except  Exception as e:
		print "error at "
		print e