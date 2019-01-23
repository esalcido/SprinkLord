from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore

from polls.forecastUpdater import forecastApi



def start():

	jobstores = {
	'mongo':MongoDBJobStore()
	}

	#connect jobstore to a mongodb
	print "at updater start."

	scheduler = BackgroundScheduler()
	scheduler.configure(jobstores=jobstores)

	scheduler.add_job(forecastApi.update_forecast, 'interval', minutes=10,id='forecastdaemon',replace_existing=True)
	

	scheduler.start()
	jobs = scheduler.get_jobs()
	print jobs