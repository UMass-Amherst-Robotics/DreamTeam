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
import wiringpi

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
    usleep(50)


def forward(tf, dc):
    gpio.output(Constants.IN1, False)
    m1 = gpio.PWM(Constants.IN2, 50)
    m2 = gpio.PWM(Constants.IN3, 50)
    gpio.output(Constants.IN4, False)

    m1.start(50)
    m2.start(50)
    sleep(0.030)
    m1.stop()
    m2.stop()

def reverse(tf, dc):
    wiringpi.softPwmWrite(Constants.IN1, dc)
    wiringpi.softPwmWrite(Constants.IN2, 0)
    wiringpi.softPwmWrite(Constants.IN3, 0)
    wiringpi.softPwmWrite(Constants.IN4, dc)
    wiringpi.delay(tf)

# function rotate_left/right(time) --> void
# must have some parameter to let car know how long to rotate for
# will have to sample timings to understand math behind it.
def rotate_left(tp, dc):
    wiringpi.softPwmWrite(Constants.IN1, 0)
    wiringpi.softPwmWrite(Constants.IN2, dc)
    wiringpi.softPwmWrite(Constants.IN3, 0)
    wiringpi.softPwmWrite(Constants.IN4, dc)
    wiringpi.delay(tf)


def rotate_right(tp, dc):
    wiringpi.softPwmWrite(Constants.IN1, dc)
    wiringpi.softPwmWrite(Constants.IN2, 0)
    wiringpi.softPwmWrite(Constants.IN3, dc)
    wiringpi.softPwmWrite(Constants.IN4, 0)
    wiringpi.delay(tf)
