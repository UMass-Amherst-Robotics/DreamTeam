# UMass Robotics Code
# Challenge01 Main Project File
#
# MotorControls.py
#
# Created by Samuel DuBois and Andrew Tran
# Created on April 11, 2020

import RPi.GPIO as gpio
import setup

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

# MARK: Main Motors Variable - Call this for all motor actions / movements
motors = setup.setupPins()

# Description: Stops the PWM Motors and performs a gpio cleanup **This is different from stopping***
# function stop() -> Void
def shutdown():
    for motor in motors:
        motor.stop()
    gpio.cleanup()


# Description: stops all motors for a specified time frame (tf)
# function stop(tf: Int) -> Void
def stop():
    motors[0].ChangeDutyCycle(0)
    motors[1].ChangeDutyCycle(0)
    motors[2].ChangeDutyCycle(0)
    motors[3].ChangeDutyCycle(0)

# Description: moves all motors in a forwards direction
# Parameters: dc = Duty Cycle
# function forward(tf: Int, fq: Int, dc: Int) -> Void
def forwards(dc):
    motors[0].ChangeDutyCycle(0)
    motors[1].ChangeDutyCycle(dc)
    motors[2].ChangeDutyCycle(dc)
    motors[3].ChangeDutyCycle(0)

# Description: moves all motors in a reverse direction
# Parameters: dc = Duty Cycle
# function reverse(tf: Int, fq: Int, dc: Int) -> Void
def reverse(dc):
    motors[0].ChangeDutyCycle(dc)
    motors[1].ChangeDutyCycle(0)
    motors[2].ChangeDutyCycle(0)
    motors[3].ChangeDutyCycle(dc)

# Description: rotates all motors in a leftwards direction
# Parameters: dc = Duty Cycle
# function rotateLeft(tf: Int, fq: Int, dc: Int) -> Void
def rotateLeft(dc):
    motors[0].ChangeDutyCycle(0)
    motors[1].ChangeDutyCycle(dc)
    motors[2].ChangeDutyCycle(0)
    motors[3].ChangeDutyCycle(dc)

# Description: rotates all motors in a rightwards direction
# Parameters: dc = Duty Cycle
# function rotateRight(tf: Int, fq: Int, dc: Int) -> Void
def rotateRight(dc):
    motors[0].ChangeDutyCycle(dc)
    motors[1].ChangeDutyCycle(0)
    motors[2].ChangeDutyCycle(dc)
    motors[3].ChangeDutyCycle(0)
