# UMass Robotics Team 
# Challenge01 Main Project File
#
# UltrasonicSensor.py
#
# Created by Samuel DuBois and Andrew Tran
# Created on April 11, 2020

import RPi.GPIO as gpio
import time
import Constants

# Description: gets data from the Ultrasonic Sensor and returns an int; in cm
def getDistanceFromSensor():

	# Set the TRIG to false in order to settle sensor
	gpio.output(Constants.TRIG, False)
	time.sleep(2)

	# Trigger the TRIG to start the sensor
	gpio.output(Constants.TRIG, True)
	time.sleep(0.0001)
	gpio.output(Constants.TRIG, False)

	# Record the start and end of the pulse to determine the time it took to come back
	while gpio.input(ECHO) == 0:
		pulse_start = time.time()

	while gpio.input(ECHO) == 1:
		pulse_end = time.time()

	# Mathemetically calculate distance
	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	return distance
