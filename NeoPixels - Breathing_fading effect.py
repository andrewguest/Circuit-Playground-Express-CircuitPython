'''
This code fades from the min_brightness up to the max_brightness, by increments of 5, then back down to the
min_brightness again, by increments of 5.

This is set to "breathe" with only the green color.

'''

import time
 
import board
import neopixel
 
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()
 

def fade_up(i, max_brightness, delay):
    while i != max_brightness:
        pixels.fill((0, i, 0))
        pixels.show()
        time.sleep(delay)
        print(i)
        i += 5


def fade_down(i, min_brightness, delay):
    while i != min_brightness:
        pixels.fill((0, i, 0))
        pixels.show()
        time.sleep(delay)
        print(i)
        i -= 5


def breathe():
    # CHANGE ME to speed up or slow down beathing.
    delay = 0.04
    
    # CHANGE ME to change how dim the fading goes.
    min_brightness = 15
    
    # CHANGE ME to change how bright the fading goes.
    max_brightness = 175
    
    # CHANGE ME to change where the fading starts.
    starting_brightness = min_brightness
    
    while True:
        fade_up(min_brightness, max_brightness, delay)
        fade_down(max_brightness, min_brightness, delay)
        
 
while True:
    breathe()
