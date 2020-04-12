'''
Change color of every pixels to a random value when the A button is pressed
or held down.
'''

from digitalio import DigitalInOut, Direction, Pull
import board
import time
import random
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)


# Sets the led variable to the D13 LED on the board
led = DigitalInOut(board.D13)
# Sets the D13 LED as an OUTPUT
led.direction = Direction.OUTPUT

# Setup the a_button variable to the BUTTON_A on the board
a_button = DigitalInOut(board.BUTTON_A)
# Setup the a_button as an INPUT device
a_button.direction = Direction.INPUT
a_button.pull = Pull.DOWN


while True:
    if a_button.value == True:  # button is pushed
        for light in range(len(pixels)):
            random_red = random.randint(0, 256)
            random_green = random.randint(0, 256)
            random_blue = random.randint(0, 256)
            pixels[light] = (random_red, random_green, random_blue)
            time.sleep(0.05)
    else:
        led.value = False

    time.sleep(0.01)
