import numpy as zee
import matplotlib.pyplot as zii
x = zee.arange(-2*zee.pi,2*zee.pi,0.01)
y = zee.sin(3*x)/x
zii.plot(x,y)
zii.show()
