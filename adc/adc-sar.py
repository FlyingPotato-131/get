import RPi.GPIO as gpio
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(4, gpio.IN)
gpio.setup(17, gpio.OUT)

def decbin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def adc():
    gpio.output(17, 1)
    vlt = 0
    for i in range(8):
        gpio.output(dac, decbin(vlt + 2**(7-i)))
        sleep(0.001)
        if(gpio.input(4) == 1):
            vlt += 2**(7-i)
    return vlt

try:
    while(1):
        vlt = adc()
        res = ", Напряжение {outvlt:.2f} В"
        print(decbin(vlt), res.format(outvlt=vlt*3.3/256))
except KeyboardInterrupt:
    print("")
    print("этот гораздо быстрее")

finally:
    gpio.output(dac, 0)
    gpio.output(17,0)
    gpio.cleanup