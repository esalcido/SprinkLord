from SoilHygrometer import * 
import logging

logging.basicConfig(filename='/home/debian/SprinklerLord/moistureReadings.log', format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

soilMeter = SoilHygrometer("P9_39")
soilMeter.setup()
reading = soilMeter.read()

logging.info('reading: '+str(reading) )


