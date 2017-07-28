#!/usr/bin/env python
# This script uses Touch Switch, Auto Flash LED, and Passive Buzzer sensors
# Touch Switch is used to toggle on/off Auto Flash LED and Passive Buzzer

import RPi.GPIO as GPIO

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Auto Flash LED;  pin 11 = GPIO 17
led_pin = 11

# assign pin number for Passive Buzzer;  pin 32 = GPIO 12
buzz_pin = 32

# assign pin number for Touch Switch;  pin 31 = GPIO 6
touch_pin = 31


# set Auto Flash LED pin's mode as output
GPIO.setup(led_pin,GPIO.OUT)

# set Touch Switch pin's mode as input
GPIO.setup(touch_pin,GPIO.IN)

# set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)


# create Buzz function and set initial sound frequency to 1000
Buzz = GPIO.PWM(buzz_pin,1000)

while True:
    if GPIO.input(touch_pin) == 0:
        GPIO.output(led_pin, 1)
        Buzz.start(50)
    if GPIO.input(touch_pin) == 1:
        GPIO.output(led_pin, 0)
        Buzz.stop()
