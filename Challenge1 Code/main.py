# UMass Robotics Team
# Challenge01 Main Project File
#
# main.py
#
# Created by Samuel DuBois and Andrew Tran
# Created on April 11, 2020

import RPi.GPIO as gpio 		# GPIO Library
import time						# Time Library
import Constants 				# Constants Python File
import UltrasonicSensor as us	# UltrasonicSensor.py
import MotorControls as mc		# MotorControls.py
import setup

# MARK: Functions


# Description: Main Method for executing main code
# Main Code
if __name__ == "__main__":
	# MARK: Setup and Receive Data -----------------

	# setting up pins
	setup.setupPins()

	# instantiate motor class
	Motors = mc.Motors([Constants.IN1, Constants.IN2, Constants.IN3, Constants.IN4])

	# Set the debug LED to ensure code is getting to robot
	gpio.output(Constants.LED, True)


	# MARK: Main pathing code ------------------------
	# TODO: Find perfect values for dc and time.sleep to rotate 90 degrees
	# variables to keep track if vertex has been found
	v1, v2, v3, v4 = False
	# list to keep track of edge weights
	edges = []
	
	# finds the next vertex and stops when edge is reached
	# rotates car 90 to face next wall and records that distance from v_x to v_(x+1) in edges
	while v1 == False:
		distance = us.getDistanceFromSensor()
		if distance > 20:
			Motors.forwards(50)

		else:
			Motors.rotate(50)
			time.sleep(0.01)
			Motors.stop()
			v1 = True

	distance = us.getDistanceFromSensor()
	edges.append(distance)

	# finds first vertex of area
	while v2 == False:
		distance = us.getDistanceFromSensor()
		if distance > 20:
			Motors.forwards(50)

		else:
			Motors.rotate(50)
			time.sleep(0.01)
			Motors.stop()
			v2 = True

	distance = us.getDistanceFromSensor()
	edges.append(distance)

	while v3 == False:
		distance = us.getDistanceFromSensor()
		if distance > 20:
			Motors.forwards(50)

		else:
			Motors.rotate(50)
			time.sleep(0.01)
			Motors.stop()
			v3 = True

	distance = us.getDistanceFromSensor()
	edges.append(distance)
	
	while v4 == False:
		distance = us.getDistanceFromSensor()
		if distance > 20:
			Motors.forwards(50)

		else:
			Motors.rotate(50)
			time.sleep(0.01)
			Motors.stop()
			v4 = True

	distance = us.getDistanceFromSensor()
	edges.append(distance)
	
	perimeter = sum(edges)
	print(perimeter)


	gpio.cleanup()



