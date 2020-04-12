# UMass Robotics Code
# Challenge01 Main Project File
#
# MotorControls.py
#
# Created by Samuel DuBois and Andrew Tran
# Created on April 11, 2020

import RPi.GPIO as gpio
import time
import Constants

"""
Motor controls for the robot to be used in tandem with UltrasonicSensor.py to create
basic algorithm for movement

IN1 and IN2 control left side of the bot
IN3 and IN4 control right side of the bot

False-False --> off
False-True --> forward
True-False --> reverse
"""


def stop():
    gpio.output(Constants.IN1, False)
    gpio.output(Constants.IN2, False)
    gpio.output(Constants.IN3, False)
    gpio.output(Constants.IN4, False)


def forward():
    gpio.output(Constants.IN1, False)
    gpio.output(Constants.IN2, True)
    gpio.output(Constants.IN3, False)
    gpio.output(Constants.IN4, True)


def reverse():
    gpio.output(Constants.IN1, True)
    gpio.output(Constants.IN2, False)
    gpio.output(Constants.IN3, True)
    gpio.output(Constants.IN4, False)

# function rotate_left/right(time) --> void
# must have some parameter to let car know how long to rotate for
# will have to sample timings to understand math behind it.
def rotate_left(time):
    gpio.output(Constants.IN1, True)
    gpio.output(Constants.IN2, False)
    gpio.output(Constants.IN3, False)
    gpio.output(Constants.IN4, True)

    time.sleep(time)


def rotate_right(time):
    gpio.output(Constants.IN1, False)
    gpio.output(Constants.IN2, True)
    gpio.output(Constants.IN3, True)
    gpio.output(Constants.IN4, False)

    time.sleep(time)
