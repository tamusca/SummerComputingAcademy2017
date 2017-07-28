#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import random

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Passive Buzzer;  pin 32 = GPIO 12
buzz_pin = 32

# set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

# generate a random number from 1 to 10
n = random.randint(1,10)

def buzz():
    Buzz.start(50)
    time.sleep(1)
    Buzz.stop()

# keep running until number is guessed
while True:
    print ('Guess of a number from 1 to 10')
    guess = raw_input()
    guess = int(guess)
    if guess < n:
        print "guess is too low"
        buzz()
    elif guess > n:
        print "Guess is too high"
        buzz()
    else:
        print "you guessed it"
        break

# reset GPIO resources used by script
GPIO.cleanup()
