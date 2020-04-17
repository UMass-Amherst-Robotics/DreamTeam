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
Duty cycle = 50%
Frequency = 100Hz
"""

# TODO: Still need to test these methods to make sure bot doesn't go too fast

def stop():
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, 100)
    pwm2 = gpio.pwm(Constants.IN2, 100)
    pwm3 = gpio.pwm(Constants.IN3, 100)
    pwm4 = gpio.pwm(Constants.IN4, 100)

    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()


def forward():
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, 100)
    pwm2 = gpio.pwm(Constants.IN2, 100)
    pwm3 = gpio.pwm(Constants.IN3, 100)
    pwm4 = gpio.pwm(Constants.IN4, 100)

    pwm1.stop()
    pwm2.start(50)
    pwm3.start(50)
    pwm4.stop()


def reverse():
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, 100)
    pwm2 = gpio.pwm(Constants.IN2, 100)
    pwm3 = gpio.pwm(Constants.IN3, 100)
    pwm4 = gpio.pwm(Constants.IN4, 100)

    pwm1.start(50)
    pwm2.stop()
    pwm3.start(50)
    pwm4.stop()


# function rotate_left/right(time) --> void
# must have some parameter to let car know how long to rotate for
# will have to sample timings to understand math behind it.
def rotate_left(tp):
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, 100)
    pwm2 = gpio.pwm(Constants.IN2, 100)
    pwm3 = gpio.pwm(Constants.IN3, 100)
    pwm4 = gpio.pwm(Constants.IN4, 100)

    pwm1.stop()
    pwm2.start(50)
    pwm3.stop()
    pwm4.start(50)

    time.sleep(tp)
    stop()


def rotate_right(tp):
    # make output signals pwm
    # change second argument to change frequency of signal
    pwm1 = gpio.pwm(Constants.IN1, 100)
    pwm2 = gpio.pwm(Constants.IN2, 100)
    pwm3 = gpio.pwm(Constants.IN3, 100)
    pwm4 = gpio.pwm(Constants.IN4, 100)

    pwm1.start(50)
    pwm2.stop()
    pwm3.start(50)
    pwm4.stop()

    time.sleep(tp)
    stop()
