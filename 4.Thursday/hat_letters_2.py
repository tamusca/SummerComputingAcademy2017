#!/usr/bin/env python
from sense_hat import SenseHat
import time
sense = SenseHat()

sense.show_letter("H", (255, 0, 0))
time.sleep(1)
sense.show_letter("i", (255, 255, 0))
time.sleep(1)
sense.show_letter("!", (255, 0, 0))
time.sleep(1)
sense.clear()
