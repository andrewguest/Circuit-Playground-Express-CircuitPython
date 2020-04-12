import board
import neopixel
import time
import random

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

while True:
    for light in range(len(pixels)):
        random_red = random.randint(0, 256)
        random_green = random.randint(0, 256)
        random_blue = random.randint(0, 256)
        pixels[light] = (random_red, random_green, random_blue)
        time.sleep(0.05)
