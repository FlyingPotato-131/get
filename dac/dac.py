import RPi.GPIO as gpio

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def decbin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

try:
    while(1):
        inp = input('Введите натуральное число от [0, 255] ')
        if(inp == "q"):
            print("(не) благодарю за неправильное использование")
            break
        else:
            try:
                inp = int(inp)
                print(3.3*inp/256)
                gpio.output(dac, decbin(inp))
            except ValueError:
                print("Вам напомнить определение натуральных чисел? ", inp, " ведь самое что ни на есть натуральное число!")
            except RuntimeError:
                print("Кто то явно не знает, что такое отрезок")
except KeyboardInterrupt:
    print("")
    print("(не) благодарю за неправильное использование")
finally:
    gpio.output(dac, 0)
    gpio.cleanup