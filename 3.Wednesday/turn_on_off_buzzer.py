#!/usr/bin/env python
# this script turns the Passive Buzzer on and then off

import RPi.GPIO as GPIO
import time

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Auto Flash LED;  pin 32 = GPIO 12
buzz_pin = 32 

# set Auto Flash LED pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

Buzz.start(50)
time.sleep(1)
Buzz.stop()

# reset GPIO resources used by script
GPIO.cleanup()
