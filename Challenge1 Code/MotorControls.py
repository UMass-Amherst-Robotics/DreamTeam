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

PWM used to slow down dc motors on cars.
Duty cycle = Constants.DUTYCYCLE%
Frequency = Constants.FREQHz
"""

# TODO: Still need to test these methods to make sure bot doesn't go too fast

def stop():
    # make output signals PWM
    # change second argument to change frequency of signal
    PWM1 = gpio.PWM(Constants.IN1, Constants.FREQ)
    PWM2 = gpio.PWM(Constants.IN2, Constants.FREQ)
    PWM3 = gpio.PWM(Constants.IN3, Constants.FREQ)
    PWM4 = gpio.PWM(Constants.IN4, Constants.FREQ)

    PWM1.stop()
    PWM2.stop()
    PWM3.stop()
    PWM4.stop()


def forward():
    # make output signals PWM
    # change second argument to change frequency of signal
    PWM1 = gpio.PWM(Constants.IN1, Constants.FREQ)
    PWM2 = gpio.PWM(Constants.IN2, Constants.FREQ)
    PWM3 = gpio.PWM(Constants.IN3, Constants.FREQ)
    PWM4 = gpio.PWM(Constants.IN4, Constants.FREQ)

    PWM1.stop()
    PWM2.start(Constants.DUTYCYCLE)
    PWM3.start(Constants.DUTYCYCLE)
    PWM4.stop()


def reverse():
    # make output signals PWM
    # change second argument to change frequency of signal
    PWM1 = gpio.PWM(Constants.IN1, Constants.FREQ)
    PWM2 = gpio.PWM(Constants.IN2, Constants.FREQ)
    PWM3 = gpio.PWM(Constants.IN3, Constants.FREQ)
    PWM4 = gpio.PWM(Constants.IN4, Constants.FREQ)

    PWM1.start(Constants.DUTYCYCLE)
    PWM2.stop()
    PWM3.start(Constants.DUTYCYCLE)
    PWM4.stop()


# function rotate_left/right(time) --> void
# must have some parameter to let car know how long to rotate for
# will have to sample timings to understand math behind it.
def rotate_left(tp):
    # make output signals PWM
    # change second argument to change frequency of signal
    PWM1 = gpio.PWM(Constants.IN1, Constants.FREQ)
    PWM2 = gpio.PWM(Constants.IN2, Constants.FREQ)
    PWM3 = gpio.PWM(Constants.IN3, Constants.FREQ)
    PWM4 = gpio.PWM(Constants.IN4, Constants.FREQ)

    PWM1.stop()
    PWM2.start(Constants.DUTYCYCLE)
    PWM3.stop()
    PWM4.start(Constants.DUTYCYCLE)

    time.sleep(tp)
    stop()


def rotate_right(tp):
    # make output signals PWM
    # change second argument to change frequency of signal
    PWM1 = gpio.PWM(Constants.IN1, Constants.FREQ)
    PWM2 = gpio.PWM(Constants.IN2, Constants.FREQ)
    PWM3 = gpio.PWM(Constants.IN3, Constants.FREQ)
    PWM4 = gpio.PWM(Constants.IN4, Constants.FREQ)

    PWM1.start(Constants.DUTYCYCLE)
    PWM2.stop()
    PWM3.start(Constants.DUTYCYCLE)
    PWM4.stop()

    time.sleep(tp)
    stop()
