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
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, Constants.FREQ)
    pwm2 = gpio.pwm(Constants.IN2, Constants.FREQ)
    pwm3 = gpio.pwm(Constants.IN3, Constants.FREQ)
    pwm4 = gpio.pwm(Constants.IN4, Constants.FREQ)

    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()


def forward():
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, Constants.FREQ)
    pwm2 = gpio.pwm(Constants.IN2, Constants.FREQ)
    pwm3 = gpio.pwm(Constants.IN3, Constants.FREQ)
    pwm4 = gpio.pwm(Constants.IN4, Constants.FREQ)

    pwm1.stop()
    pwm2.start(Constants.DUTYCYCLE)
    pwm3.start(Constants.DUTYCYCLE)
    pwm4.stop()


def reverse():
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, Constants.FREQ)
    pwm2 = gpio.pwm(Constants.IN2, Constants.FREQ)
    pwm3 = gpio.pwm(Constants.IN3, Constants.FREQ)
    pwm4 = gpio.pwm(Constants.IN4, Constants.FREQ)

    pwm1.start(Constants.DUTYCYCLE)
    pwm2.stop()
    pwm3.start(Constants.DUTYCYCLE)
    pwm4.stop()


# function rotate_left/right(time) --> void
# must have some parameter to let car know how long to rotate for
# will have to sample timings to understand math behind it.
def rotate_left(tp):
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, Constants.FREQ)
    pwm2 = gpio.pwm(Constants.IN2, Constants.FREQ)
    pwm3 = gpio.pwm(Constants.IN3, Constants.FREQ)
    pwm4 = gpio.pwm(Constants.IN4, Constants.FREQ)

    pwm1.stop()
    pwm2.start(Constants.DUTYCYCLE)
    pwm3.stop()
    pwm4.start(Constants.DUTYCYCLE)

    time.sleep(tp)
    stop()


def rotate_right(tp):
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, Constants.FREQ)
    pwm2 = gpio.pwm(Constants.IN2, Constants.FREQ)
    pwm3 = gpio.pwm(Constants.IN3, Constants.FREQ)
    pwm4 = gpio.pwm(Constants.IN4, Constants.FREQ)

    pwm1.start(Constants.DUTYCYCLE)
    pwm2.stop()
    pwm3.start(Constants.DUTYCYCLE)
    pwm4.stop()

    time.sleep(tp)
    stop()
