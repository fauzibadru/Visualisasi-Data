import numpy as zee
import matplotlib.pyplot as zii
x0 = zee.arange(8)
y1 = zee.array([4,3,2,1,2,4,6,6])
y2 = zee.array([5,4,2,1,3,4,5,6])
zii.ylim(-7,7)
zii.bar(x0,y1,0.9,facecolor='r')
zii.bar(x0,-y2,0.9,facecolor='g')
zii.xticks(())
zii.grid(True)
for x, y in zip(x0,y1):
    zii.text(x + 0.4, y+0.05, '%d' % y, ha='center', va='bottom')
for x, y in zip(x0, y2):
    zii.text(x + 0.4, -y  - 0.05, '%d' % y, ha='center', va='top')
zii.show()
