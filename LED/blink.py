import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

while(1):
    gpio.output(17, 1)
    sleep(1)
    gpio.output(17,0)
    sleep(1)