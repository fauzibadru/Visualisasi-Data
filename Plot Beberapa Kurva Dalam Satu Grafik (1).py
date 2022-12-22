import numpy as zee
import matplotlib.pyplot as zii
import math
t = zee.arange(0,5,1)
y1 = zee.sin(math.pi*t)
y2 = zee.sin(math.pi*t+math.pi/2)
y3 = zee.sin(math.pi*t-math.pi/2)
zii.plot(t,y1,'b--',t,y2,'g',t,y3,'r-.')
zii.show()
