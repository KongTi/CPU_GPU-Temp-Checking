# Required Permission
import clr # the pythonnet module.
clr.AddReference(r'OpenHardwareMonitorLib') 

from OpenHardwareMonitor.Hardware import Computer

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about GPU
c.Open()

from itertools import count
index = count()

x_val = []
y_val = []

def checking(i):
    temps = []
    for a in range(0, len(c.Hardware[0].Sensors)):
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            hardward_number = str(c.Hardware[0].Sensors[a].Identifier).split('/')[-1]
            temperature = c.Hardware[0].Sensors[a].get_Value()
            temps.append(temperature)

            #print(f'CPU {hardward_number}: {temperature}도')
            c.Hardware[0].Update()
    
    average = sum(temps)/len(temps)

    x_val.append(next(index))
    y_val.append(average)

    plt.cla()
    plt.ylim(30,80)
    plt.plot(x_val,y_val,marker='o',markersize=2)
    
    #print(f'CPU {len(temps)}개의 평균온도: {sum(temps)/len(temps)}도')
    if (average > 40):
        print("강종이다")

ani = FuncAnimation(plt.gcf(),checking,interval=1000)

plt.show()