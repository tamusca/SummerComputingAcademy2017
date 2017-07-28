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

def buzz(seconds,frequency):
    Buzz.start(50)
    Buzz.ChangeFrequency(frequency)
    time.sleep(seconds)
    Buzz.stop()

# keep running until number is guessed
while True:
    print ('Guess of a number from 1 to 10')
    guess = raw_input()
    guess = int(guess)
    if guess < n:
        print "guess is too low"
        buzz(1,55)
    elif guess > n:
        print "Guess is too high"
        buzz(1,1000)
    else:
        print "you guessed it"
        buzz(0.2,880)
        buzz(0.2,1760)
        break

# reset GPIO resources used by script
GPIO.cleanup()
