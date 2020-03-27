from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from polls.SprinklerLord import program
import logging

logging.basicConfig(filename='sprinklerTimes.log',format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')



def start():
	print "at updater start.from water schedule"
	scheduler = BackgroundScheduler()
	scheduler.add_job(program.runProgram, 'cron',day_of_week='0,2,4',hour=6,minute=30)
	scheduler.start()
	scheduler.get_jobs()