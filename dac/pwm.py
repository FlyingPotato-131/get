import RPi.GPIO as gpio

port = 2
gpio.setmode(gpio.BCM)
gpio.setup(port, gpio.OUT)
pwmout = gpio.PWM(port, 10000)
pwmout.start(0)

try:
    while(1):
        try:
            inp = float(input('Введите число [0, 100] '))
            print(3.3/100*inp)
            pwmout.start(inp)
        except ValueError:
            print("Это в какой вселенной ", inp, " это число [0, 100]?")
except KeyboardInterrupt:
    print("")
    print("(не) благодарю за неправильное использование")
finally:
    pwmout.start(0)
    gpio.output(port, 0)
    gpio.cleanup()