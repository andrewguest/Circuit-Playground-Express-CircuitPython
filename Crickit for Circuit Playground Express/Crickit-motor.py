import time
import board
import neopixel
from adafruit_crickit import crickit

print("Adabot Tightrope")
RED =   (16, 0, 0)
GREEN = (0, 16, 0)
BLACK = (0, 0, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.2)
pixels.fill(BLACK)

motor = crickit.dc_motor_1

run_time = 6
speed = 0.65

while True:
    # set NeoPixels green in direction of movement
    for i in range(5):
        pixels[i] = GREEN
    for i in range(5):
        pixels[i+5] = BLACK
 
    motor.throttle = speed  # full speed forward
    time.sleep(run_time)  # motor will run for this amount of time
 
    # set NeoPixels red when stopped
    pixels.fill(RED)
    motor.throttle = 0  # stop the motor
    
        # set NeoPixels green in direction of movement
    for i in range(5):
        pixels[i] = BLACK
    for i in range(5):
        pixels[i+5] = GREEN
 
    motor.throttle = -1 * speed  # full speed backward
    time.sleep(run_time)  # motor will run for this amount of time
 
    pixels.fill(RED)
    motor.throttle = 0  # stopped