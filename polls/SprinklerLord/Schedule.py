#!/usr/bin/env python

from Station import Station
import logging
# This will import the sleep function for the timer below.
from time import sleep
#from apscheduler.schedulers.background import BackgroundScheduler

class Schedule:


	def __init__(self, duration, stations):
		self.duration = duration
		self.stations = stations

	def runSchedule(self):

		for x in sorted(self.stations):
			self.stations[x].on()
			sleep(self.duration)
			print "turning on "+self.stations[x].name
			logging.info("turning on "+self.stations[x].name)
			self.stations[x].off()
			sleep(2)
			print "turning off "+self.stations[x].name
			logging.info("turning off "+self.stations[x].name)
		for y in self.stations:
			self.stations[y].cleanup()
		print "End of Sprinkler program"
		logging.info("End of Sprinkler program")