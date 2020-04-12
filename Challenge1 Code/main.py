# UMass Robotics Team
# Challenge01 Main Project File
#
# main.py
#
# Created by Samuel DuBois and Andrew Tran
# Created on April 11, 2020

import RPi.GPIO as gpio # GPIO Library
import time
import Constants 		# Constants Python File
import UltrasonicSensor
import MotorControls as mc

# MARK: Functions

# Description: Setup the Raspi's GPIO inputs for control as input and outputs
# function setupPins(void) -> void
def setupPins():

	# H-Bridge / Motor Controller Pins
	gpio.setmode(gpio.BOARD)
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
	setupPins()

	# Set the debug LED to ensure code is getting to robot
	gpio.output(Constants.LED, True)

	while True:
		
		# x = input()
		# if x = "w":
		# 	mc.forward()
		# 	time.sleep(0.03)
		# if x = "s":
		# 	mc.reverse()
		# 	time.sleep(0.03)
		# if x = "a":
		# 	mc.rotate_left()
		# 	time.sleep(0.03)
		# if x = "d":
		# 	mc.rotate_right()
		# 	time.sleep(0.03)
		# if x = "q":
		# 	mc.stop()
		# 	time.sleep(0.03)

	gpio.cleanup()
