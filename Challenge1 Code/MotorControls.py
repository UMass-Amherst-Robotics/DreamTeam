# UMass Robotics Code

import RPi.GPIO as gpio
import time
import Constants


# we use gpio.clean up on exit of program


# Description: stops all movement when sensor detects object directly in front of it
def stop():
    # set all H-Bridge pins to low
    gpio.output(Constants.IN1, False)
    gpio.output(Constants.IN2, False)
    gpio.output(Constants.IN3, False)
    gpio.output(Constants.IN4, False)


# Description: moves car in forward direction
def foward():
    gpio.output(Constants.IN1, False)
    gpio.output(Constants.IN2, True)
    gpio.output(Constants.IN3, False)
    gpio.output(Constants.IN4, True)


# Description: moves car backwards
def reverse():
    gpio.output(Constants.IN1, True)
    gpio.output(Constants.IN2, False)
    gpio.output(Constants.IN3, True)
    gpio.output(Constants.IN4, False)


def rotate_left():
    gpio.output(Constants.IN1, True)
    gpio.output(Constants.IN2, False)
    gpio.output(Constants.IN3, False)
    gpio.output(Constants.IN4, True)


def rotate_right():
    gpio.output(Constants.IN1, False)
    gpio.output(Constants.IN2, True)
    gpio.output(Constants.IN3, True)
    gpio.output(Constants.IN4, False)







