#!/usr/bin/env python
import random

# generate a random number from 1 to 10
n = random.randint(1,10)

# keep running until number is guessed
while True:
    print ('Guess of a number from 1 to 10')
    guess = raw_input()
    guess = int(guess)
    if guess < n:
        print "guess is too low"
    elif guess > n:
        print "Guess is too high"
    else:
        print "you guessed it"
        break
