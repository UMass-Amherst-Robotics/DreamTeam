# UMass Robotics Team
# Challenge01 Main Project File
#
# main.py
#
# Created by Samuel DuBois and Andrew Tran
# Created on April 20, 2020

import RPi.GPIO as gpio 		# GPIO Library
import Constants 				# Constants Python File

# MARK: Functions

# Description: Setup the Raspi's GPIO inputs for control as input and outputs
# function setupPins(void) -> motors
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

        # Motors are instantiated with a frequency of 5000 Hz or 5 KHz
        motors = [gpio.PWM(Constants.IN1, 5000), gpio.PWM(Constants.IN2, 5000), gpio.PWM(Constants.IN3, 5000),
                  gpio.PWM(Constants.IN4, 5000)]
        for motor in motors:
            motor.start(0)

        return motors

