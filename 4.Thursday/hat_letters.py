#!/usr/bin/env python
from sense_hat import SenseHat
import time
sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

sense.show_letter("H", red)
time.sleep(1)
sense.show_letter("i", blue)
time.sleep(1)
sense.show_letter("!", white)
time.sleep(1)
sense.clear()
