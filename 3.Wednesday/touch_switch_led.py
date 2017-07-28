#!/usr/bin/env python
# This script uses Touch Switch and Auto Flash LED sensors
# Touch Switch is used to toggle on/off Auto Flash LED

import RPi.GPIO as GPIO

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Auto Flash LED;  pin 11 = GPIO 17
led_pin = 11

# assign pin number for Touch Switch;  pin 31 = GPIO 6
touch_pin = 31


# set Auto Flash LED pin's mode as output
GPIO.setup(led_pin,GPIO.OUT)

# set Touch Switch pin's mode as input
GPIO.setup(touch_pin,GPIO.IN)


while True:
    if GPIO.input(touch_pin) == 0:
        # turn on LED
        GPIO.output(led_pin,1)
    if GPIO.input(touch_pin) == 1:
        # turn off LED
        GPIO.output(led_pin,0)
