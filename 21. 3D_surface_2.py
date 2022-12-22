from mpl_toolkits.mplot3d import Axes3D
import numpy as zee
import matplotlib.pyplot as zii
fig = zii.figure()
ax = Axes3D(fig)
X = zee.arange(-2,2,0.1)
Y = zee.arange(-2,2,0.1)
X,Y = zee.meshgrid(X,Y)
def f(x,y):
    return (1 - y**5 + x**5)*zee.exp(-x**2-y**2)
ax.plot_surface(X,Y,f(X,Y), rstride=1, cstride=1, cmap=zii.cm.hot)
ax.view_init(elev=30,azim=125)
zii.show()
