import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(2, gpio.IN)

while(1):2
    gpio.output(17, gpio.input(2))