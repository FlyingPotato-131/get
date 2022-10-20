import re
import numpy as np
import matplotlib.pyplot as plot

with open("settings.txt", "r") as settings:
    settings = re.findall("\d+\.\d+", settings.read())
    tmpset = [float(settings[i]) for i in range(len(settings))]
    #print(tmpset)

with open("data.txt", "r") as data:
    data = re.findall("\d+\.\d+", data.read())
    tmpdat = np.array([float(data[i]) for i in range(len(data))])
#    print(tmp)

tmax = tmpdat.argmax() * tmpset[0] / len(tmpdat)

fig, ax = plot.subplots()

plot.yticks(np.arange(0, 3.5, step=0.5))
plot.ylabel("Напряжение, В")

plot.xticks(np.arange(0, len(tmpdat), step=len(tmpdat)/tmpset[0]*50), np.arange(0, tmpset[0], step=50))
plot.xlabel("Время, С")
#fig.figlegend()
plot.title("Зависимость напряжения от времени в RC-цепи")

plot.minorticks_on()
plot.grid(True, "both", "both")
plot.text(0.6 * len(tmpdat), 2.5, "Время заряда {time:.2f} с".format(time = tmax))
plot.text(0.6 * len(tmpdat), 2.3, "Время разряда {time:.2f} с".format(time = tmpset[0] - tmax))

ax.plot(tmpdat, "ro-",linewidth=1, markersize=2, label="V(t)")
ax.legend()
plot.savefig("graph.svg")
plot.show()