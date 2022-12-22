from mpl_toolkits.mplot3d import Axes3D
import numpy as zee
import matplotlib.pyplot as zii
xs = zee.random.randint(30,40,100)
ys = zee.random.randint(20,30,100)
zs = zee.random.randint(10,20,100)
xs2 = zee.random.randint(50,60,100)
ys2 = zee.random.randint(30,40,100)
zs2 = zee.random.randint(50,70,100)
xs3 = zee.random.randint(10,30,100)
ys3 = zee.random.randint(40,50,100)
zs3 = zee.random.randint(40,50,100)
fig = zii.figure()
ax = Axes3D(fig)
ax.scatter(xs,ys,zs)
ax.scatter(xs2,ys2,zs2,c='r',marker='^')
ax.scatter(xs3,ys3,zs3,c='g',marker='*')
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')
zii.show()