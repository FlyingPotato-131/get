import RPi.GPIO as gpio
from time import sleep
import time
import matplotlib.pyplot as plot

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(4, gpio.IN)
gpio.setup(17, gpio.OUT)
gpio.setup(leds, gpio.OUT)

def adc(): #считывание напряжения в виде числа от 0 до 255
    vlt = 0
    for i in range(8):
        gpio.output(dac, decbin(vlt + 2**(7-i)))
        sleep(0.001)
        if(gpio.input(4) == 1):
            vlt += 2**(7-i)
    return vlt

def decbin(n): #преобразование числа в двоичную систему
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def ledbin(num): #выставить число на светодиодах
    bin = decbin(num)
    gpio.output(leds, bin)

try:
    msr = []
    t0 = time.time()
    gpio.output(17, 1) #начать зарядку конденсатора
    raw = 0
    open("data.txt", "w") #очистить файл если он существует
    data = open("data.txt", "a")
    data.write("Зарядка \n")
    while(raw < 248):
        raw = adc() #считать данные
        gpio.output(leds, decbin(raw))
        msr.append(raw*3.3/256) #записать данные в список
        res = "Зарядка, текущее напряжение {vlt:.2f} В"
        print(res.format(vlt = msr[-1])) #вывести результат в терминал и в файл
        data.write(str(msr[-1]))
        data.write("\n")
        sleep(0.1)
    gpio.output(17, 0) #отключить напряжение от конденсатора
    data.write("Разрядка \n")
    while(raw > 5):
        raw = adc() #считать данные
        gpio.output(leds, decbin(raw))
        msr.append(raw*3.3/256) #записать данные в список
        res = "Разрядка, текущее напряжение {vlt:.2f} В"
        print(res.format(vlt = msr[-1])) #вывести результат в терминал и в файл
        data.write(str(msr[-1]))
        data.write("\n")
        sleep(0.1)
    t = time.time()
    print("Время эксперимента ", t - t0, " с") #вывести настройки в терминал и в файл
    print("Период измерения ", (t - t0)/len(msr), " с")
    print("Частота дискретизации ", len(msr)/(t-t0), " Гц")
    print("Шаг Квантования 0.013 В")
    open("settings.txt", "w")
    settings = open("settings.txt", "a")
    res = "Время эксперимента {time:.2f} с"
    settings.write(res.format(time = t - t0))
    settings.write("\n")
    res = "Период измерения {time:.2f} с"
    settings.write(res.format(time = (t - t0)/len(msr)))
    settings.write("\n")
    res = "Частота дискретизации {time:.2f} "
    settings.write(res.format(time = (len(msr)/(t - t0))))
    settings.write("\n")
    settings.write("Шаг Квантования 0.013 В")
    plot.plot(msr) #построить график по списку
    plot.show()

finally:
    data.close()
    gpio.output(dac, 0)
    gpio.output(leds, 0)
    gpio.output(17,0)
    gpio.cleanup
