import RPi.GPIO as gpio
from time import sleep
from random import randint

dac = [26, 19, 13, 6, 5, 11, 9, 10]
#num = [0,0,0,0,0,0,1,0] #2
num = [1,1,1,1,1,1,1,1] #255
#num = [0,1,1,1,1,1,1,1] #127
#num = [0,1,0,0,0,0,0,0] #64
#num = [0,0,1,0,0,0,0,0] #32
#num = [0,0,0,0,0,1,0,1] #5
#num = [0,0,0,0,0,0,0,0] #0
#256 = 2^8 т.е. его невозможно записать в 8 битах

gpio.setmode(gpio.BCM)
for i in dac: gpio.setup(i, gpio.OUT)

for i in range(8): num[i] = randint(0, 1)

for i in range(8): gpio.output(dac[i], num[i])
sleep(15)
for i in range(8): gpio.output(dac[i], 0)
gpio.cleanup()