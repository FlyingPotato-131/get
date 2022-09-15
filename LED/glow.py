import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup(17, gpio.OUT)
while(1):
    gpio.output(17,1)