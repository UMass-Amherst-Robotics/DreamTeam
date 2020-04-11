# UMass Robotics Team 
# Challenge01 Main Project File
#
# main.py
#
# Created by Samuel DuBois and Andrew Tran
# Created on April 11, 2020

import RPi.GPIO as gpio 
import time

# MARK: Constants and Variables

# H-Bridge / Motor Controller
IN1 = 7
IN2 = 11
IN3 = 13
IN4 = 15

# HC-SR04 Ultrasonic Sensor
TRIG = 16
ECHO = 18

# Status LED
LED = 22

# MARK: Functions

# Description: Setup the Raspi's GPIO inputs for control as input and outputs
# function setupPins(void) -> void
def setupPins():

	# H-Bridge / Motor Controller Pins
	gpio.setmode(gpio.BOARD)
	gpio.setup(IN1, gpio.OUT)
	gpio.setup(IN2, gpio.OUT)
	gpio.setup(IN3, gpio.OUT)
	gpio.setup(IN4, gpio.OUT)

	# HC-SR04 Ultrasonic Sensor Pins
	gpio.setup(TRIG, gpio.OUT)
	gpio.setup(ECHO, gpio.IN)

	# LED Status Pin
	gpio.setup(LED, gpio.OUT)

if __name__ == "__main__":
	setupPins()
	print("Hello World")

