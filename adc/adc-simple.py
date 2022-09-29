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
    for i in range(256):
            gpio.output(dac, decbin(i))
            sleep(0.0007)
            if(gpio.input(4) == 0):
                return(i)
                break

try:
    gpio.output(17, 1)
    while(1):
        vlt = adc()
        print(decbin(vlt), vlt*3.3/256)
        
except ValueError:
    print("Что то странное...")
except KeyboardInterrupt:
    print("")
    print("долго же он их измеряет...")
finally:
    gpio.output(dac, 0)
    gpio.output(17,0)
    gpio.cleanup