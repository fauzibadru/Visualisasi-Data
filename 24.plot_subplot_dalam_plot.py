import numpy as zee
import matplotlib.pyplot as zii
fig = zii.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
inner_ax = fig.add_axes([0.6,0.6,0.25,0.25])
x1 = zee.arange(10)
y1 = zee.array([1,2,7,1,5,2,4,2,3,1])
x2 = zee.arange(10)
y2 = zee.array([0.5,1,3.5,0.5,2.5,1,2,1,1.5,0.5])
ax.plot(x1,y1)
inner_ax.plot(x2,y2)
zii.show()
