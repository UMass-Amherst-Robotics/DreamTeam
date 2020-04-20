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
	# setting up pins
	setup.setupPins()

	# instantiate motor class
	Motors = mc.Motors([Constants.IN1, Constants.IN2, Constants.IN3, Constants.IN4])

	Motors.forwards(78)

	Motors.shutdown()

	"""
	# Constants and Variables
	intervalsUntilCompletion = 0	# Number of readings until the program is terminated
	previousDistanceReading = 0		# Records the previous distance reading to be compared with the current
	numOfSameDistanceReadings = 0	# Records the number of distance readings that were the same

	while intervalsUntilCompletion < 20:

		# MARK: Setup and Receive Data -----------------

		# Setup Pins
		setup.setupPins()
		Motors = mc.Motors([Constants.IN1, Constants.IN2, Constants.IN3, Constants.IN4])

		# Set the debug LED to ensure code is getting to robot
		gpio.output(Constants.LED, True)

		### TODO ### Make this Stuck Code more robust

		# Check and see if the robot is stuck
		if numOfSameDistanceReadings > 2:
			# If the robot is stuck,
			print("Robot is stuck, moving backwards")
			for _ in range(0, 50):
				mc.reverse(78)
				time.sleep(0.030)
			print("Rotating right")
			for x in range(0, 50):
				mc.rotateRight(100)
				time.sleep(0.030)
			numOfSameDistanceReadings = 0

		# MARK: Main Loop -------------------------------

		# Get distance reading from Ultrasonic Sensor (takes about a second)
		distance = us.getDistanceFromSensor()
		print(distance)

		# Read the distance and check to see
		if distance > 40:
			mc.forwards(50)
			print("Moving Forward")
		else:
			mc.rotateRight(80)
			print("Rotating Right")

		# MARK: Cleanup -----------------------------------

		# Check to see if the previous distance is relatively the same as the current
		if int(abs(distance - previousDistanceReading)) < 2:
			# They are relatively the same so increment
			numOfSameDistanceReadings += 1
		else:
			numOfSameDistanceReadings = 0

		# Record the distance for the next cycle and increment number of intervals performed
		previousDistanceReading = distance
		intervalsUntilCompletion += 1

		gpio.cleanup()

	print("Exited Program. Timer up.")
	mc.shutdown()
	"""
