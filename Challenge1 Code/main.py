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

# MARK: Functions

# Description: Setup the Raspi's GPIO inputs for control as input and outputs
# function setupPins(void) -> void
def setupPins():

	gpio.setmode(gpio.BCM)

	# H-Bridge / Motor Controller Pins
	gpio.setup(Constants.IN1, gpio.OUT)
	gpio.setup(Constants.IN2, gpio.OUT)
	gpio.setup(Constants.IN3, gpio.OUT)
	gpio.setup(Constants.IN4, gpio.OUT)

	# HC-SR04 Ultrasonic Sensor Pins
	gpio.setup(Constants.TRIG, gpio.OUT)
	gpio.setup(Constants.ECHO, gpio.IN)

	# LED Status Pin
	gpio.setup(Constants.LED, gpio.OUT)


# Description: Main Method for executing main code
# Main Code
if __name__ == "__main__":

	# Constants and Variables
	intervalsUntilCompletion = 0	# Number of readings until the program is terminated
	previousDistanceReading = 0		# Records the previous distance reading to be compared with the current
	numOfSameDistanceReadings = 0	# Records the number of distance readings that were the same

	while intervalsUntilCompletion < 60:

		# MARK: Setup and Receive Data -----------------

		# Setup Pins
		setupPins()

		# Set the debug LED to ensure code is getting to robot
		gpio.output(Constants.LED, True)

		# Check and see if the robot is stuck
		if numOfSameDistanceReadings > 2:
			# If the robot is stuck,
			print("Robot is stuck, moving backwards")
			for _ in range(0, 30):
				mc.reverse(0.030, 50, 50)
			print("Rotating right")
			for _ in range(0, 30):
				mc.rotateRight(0.030, 50, 50)
			numOfSameDistanceReadings = 0

		# MARK: Main Loop -------------------------------

		# Get distance reading from Ultrasonic Sensor (takes about a second)
		distance = us.getDistanceFromSensor()
		print(distance)

		# Read the distance and check to see
		if distance > 40:
			mc.forwards(0.030, 5000, 77)
			print("Moving Forward")
		else:
			mc.rotateRight(0.030, 5000, 77)
			print("Rotating Right")

		if int(distance - previousDistanceReading) < 2:
			numOfSameDistanceReadings += 1

		previousDistanceReading = distance

		intervalsUntilCompletion += 1

	print("Exited Program. Timer up.")
