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
import main

"""
---------------------------------------------------------------------------------------
How the Motors Work:

Motor controls for the robot to be used in tandem with UltrasonicSensor.py to create
basic algorithm for movement

IN1 and IN2 control left side of the bot
IN3 and IN4 control right side of the bot

False-False --> off
False-True --> forward
True-False --> reverse
---------------------------------------------------------------------------------------
"""
# MARK: Variables

def getMotorsForPWM():
    main.setupPins()
    motors = [gpio.PWM(Constants.IN1, 5000), gpio.PWM(Constants.IN2, 5000), gpio.PWM(Constants.IN3, 5000), gpio.PWM(Constants.IN4, 5000)]
    for motor in motors:
        motor.start(0)

    return motors

motors = getMotorsForPWM()

def shutdown():
    for motor in motor:
        motor.stop()
    gpio.cleanup()


# Description: stops all motors for a specified time frame (tf)
# function stop(tf: Int) -> Void
def stop(tf):
    gpio.output(Constants.IN1, False)
    gpio.output(Constants.IN2, False)
    gpio.output(Constants.IN3, False)
    gpio.output(Constants.IN4, False)

    time.sleep(tf)
    gpio.cleanup()

# Description: moves all motors in a forwards direction
# Parameters: tf = timeFrame, fq = Frequency (Hz), dc = Duty Cycle
# function forward(tf: Int, fq: Int, dc: Int) -> Void
def forwards(dc):
    motors[0].ChangeDutyCycle(0)
    motors[1].ChangeDutyCycle(dc)
    motors[2].ChangeDutyCycle(dc)
    motors[3].ChangeDutyCycle(0)

    gpio.cleanup()

# Description: moves all motors in a reverse direction
# Parameters: tf = timeFrame, fq = Frequency (Hz), dc = Duty Cycle
# function reverse(tf: Int, fq: Int, dc: Int) -> Void
def reverse(tf, fq, dc):
    m1 = gpio.PWM(Constants.IN1, fq)
    gpio.output(Constants.IN2, False)
    gpio.output(Constants.IN3, False)
    m2 = gpio.PWM(Constants.IN4, fq)

    m1.start(dc); m2.start(dc)
    time.sleep(tf)
    m1.stop(); m2.stop()

    gpio.cleanup()

# Description: rotates all motors in a leftwards direction
# Parameters: tf = timeFrame, fq = Frequency (Hz), dc = Duty Cycle
# function rotateLeft(tf: Int, fq: Int, dc: Int) -> Void
def rotateLeft(tp, fq, dc):
    gpio.output(Constants.IN1, False)
    m1 = gpio.PWM(Constants.IN2, fq)
    gpio.output(Constants.IN3, False)
    m2 = gpio.PWM(Constants.IN4, fq)

    m1.start(dc); m2.start(dc)
    time.sleep(tf)
    m1.stop(); m2.stop()

    gpio.cleanup()

# Description: rotates all motors in a rightwards direction
# Parameters: tf = timeFrame, fq = Frequency (Hz), dc = Duty Cycle
# function rotateRight(tf: Int, fq: Int, dc: Int) -> Void
def rotateRight(tp, fq, dc):
    m1 = gpio.PWM(Constants.IN1, fq)
    gpio.output(Constants.IN2, False)
    m2 = gpio.PWM(Constants.IN3, fq)
    gpio.output(Constants.IN4, False)

    m1.start(dc); m2.start(dc)
    time.sleep(tf)
    m1.stop(); m2.stop()

    gpio.cleanup()
