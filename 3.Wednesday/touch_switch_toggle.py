#!/usr/bin/env python
# this script uses the Touch Switch to toggle on/off sensors

import RPi.GPIO as GPIO
import time

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Touch Switch;  pin 31 = GPIO 6
touch_pin = 31

# set Touch Switch pin's mode as input
GPIO.setup(touch_pin,GPIO.IN)


while True:
    if GPIO.input(touch_pin) == 0:
        # add code here to toggle off a sensor
    if GPIO.input(touch_pin) == 1:
        # add code here to toggle on a sensor
