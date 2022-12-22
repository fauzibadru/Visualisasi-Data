from mpl_toolkits.mplot3d import Axes3D
import numpy as zee
import matplotlib.pyplot as zii
x = zee.arange(8)
y = zee.random.randint(0,10,8)
y2 = y + zee.random.randint(0,3,8)
y3 = y2 + zee.random.randint(0,3,8)
y4 = y3 + zee.random.randint(0,3,8)
y5 = y4 + zee.random.randint(0,3,8)
clr = ['#4bb2c5', '#c5b47f', '#EAA228', '#579575', '#839557', '#958c12', '#4b5de4']
fig = zii.figure()
ax = Axes3D(fig)
ax.bar(x,y,0,zdir='y',color=clr)
ax.bar(x,y2,10,zdir='y',color=clr)
ax.bar(x,y3,20,zdir='y',color=clr)
ax.bar(x,y4,30,zdir='y',color=clr)
ax.bar(x,y5,40,zdir='y',color=clr)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
zii.show()
