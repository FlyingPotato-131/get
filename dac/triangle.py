import RPi.GPIO as gpio
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def decbin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

try:
    per = float(input('Введите период в мс '))/512000
    while(1):
        for i in range(256):
            gpio.output(dac, decbin(i))
            sleep(per)
        for i in range(256):
            gpio.output(dac, decbin(255 - i))
            sleep(per)
except ValueError:
    print("С каких пор это можно представить как период?")
except KeyboardInterrupt:
    print("")
    print("Вот это я понимаю треугольники")
finally:
    gpio.output(dac, 0)
    gpio.cleanup