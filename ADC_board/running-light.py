import RPi.GPIO as gpio
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

gpio.setmode(gpio.BCM)
for i in leds: gpio.setup(i, gpio.OUT)
for i in leds: gpio.output(i, 0)

for i in range(3):
    for i in leds:
        gpio.output(i, 1)
        time.sleep(0.2)
        gpio.output(i, 0)

for i in leds: gpio.output(i, 0)
gpio.cleanup()