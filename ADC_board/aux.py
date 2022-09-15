import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

for i in leds: gpio.setup(i, gpio.OUT)
for i in aux: gpio.setup(i, gpio.IN)

while(1):
    for i in range(8):
        gpio.output(leds[i], gpio.input(aux[i]))

#while(1): print(gpio.input(14))