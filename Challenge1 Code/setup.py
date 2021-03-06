# UMass Robotics Team
# Challenge01 Main Project File
#
# setup.py
#
# Created by Samuel DuBois and Andrew Tran
# Created on April 20, 2020

import RPi.GPIO as gpio     # GPIO Library
import Constants 			# Constants Python File

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
