#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time

r = (255, 0, 0)
b = (0, 0, 255)
w = (255, 255, 255)

pixels = [
    b, b, b, b, r, r, r, r,
    b, b, b, b, w, w, w, w,
    b, b, b, b, r, r, r, r,
    b, b, b, b, w, w, w, w,
    r, r, r, r, r, r, r, r,
    w, w, w, w, w, w, w, w,
    r, r, r, r, r, r, r, r,
    w, w, w, w, w, w, w, w,
]

sense.set_pixels(pixels)
time.sleep(5)
sense.clear()
