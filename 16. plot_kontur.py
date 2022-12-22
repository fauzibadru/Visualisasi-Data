import numpy as zee
import matplotlib.pyplot as zii
dx = 0.01; dy = 0.01
x = zee.arange(-2.5,2.5,dx)
y = zee.arange(-2.5,2.5,dy)
X,Y = zee.meshgrid(x,y)
def f(x,y):
    return (1-y**5 + x**5)*zee.exp(-x**2 - y**2)
C = zii.contour(X,Y,f(X,Y),8,colors='black')
zii.clabel(C, inline=1, fontsize=10)
zii.show()
