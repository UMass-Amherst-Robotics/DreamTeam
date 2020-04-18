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
import wiringpi					# Pulse Width Modulation (PWM)

# MARK: Functions

# Description: Setup the Raspi's GPIO inputs for control as input and outputs
# function setupPins(void) -> void
def setupPins():

	# WiringPi and GPIO Board Setup
	wiringpi.wiringPiSetup()
	# gpio.setmode(gpio.BOARD)

	# H-Bridge / Motor Controller Pins
		# Specify pins as outputs
	wiringpi.pinMode(Constants.IN1, Constants.OUTPUT)
	wiringpi.pinMode(Constants.IN2, Constants.OUTPUT)
	wiringpi.pinMode(Constants.IN3, Constants.OUTPUT)
	wiringpi.pinMode(Constants.IN4, Constants.OUTPUT)
		# Delegate them as Software PWM and set initial value to 0, max to 100
	wiringpi.softPwmCreate(Constants.IN1, 0, 100)
	wiringpi.softPwmCreate(Constants.IN2, 0, 100)
	wiringpi.softPwmCreate(Constants.IN3, 0, 100)
	wiringpi.softPwmCreate(Constants.IN4, 0, 100)

	# HC-SR04 Ultrasonic Sensor Pins
	# gpio.setup(Constants.TRIG, gpio.OUT)
	# gpio.setup(Constants.ECHO, gpio.IN)

	# LED Status Pin
	# gpio.setup(Constants.LED, gpio.OUT)


# Description: Main Method for executing main code
# Main Code
if __name__ == "__main__":

	setupPins()

	x = 0
	while x < 50:

		# Set the debug LED to ensure code is getting to robot
		# gpio.output(Constants.LED, True)

		print("Moving Backwards")
		mc.forward(10, 75)
		x += 1

	print("Exited Program. Timer up.")
