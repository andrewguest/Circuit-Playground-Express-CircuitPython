from digitalio import DigitalInOut, Direction, Pull
import board
import time


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
        led.value = True
    else:
        led.value = False

    time.sleep(0.01)
