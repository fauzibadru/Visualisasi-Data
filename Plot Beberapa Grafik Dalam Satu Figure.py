import matplotlib.pyplot as zii
import math
import numpy as zee

t = zee.arange(0,5,0.1)
y1 = zee.sin(math.pi*t)
y2 = zee.sin(math.pi*t+math.pi/2)
y3 = zee.sin(math.pi*t-math.pi/2)

zii.subplot(3,1,1)
zii.title('Fungsi y1')
zii.plot(t,y1,'b--')

zii.subplot(3,1,2)
zii.title('Fungsi y2')
zii.plot(t,y2,'g')

zii.subplot(3,1,3)
zii.title('Fungsi y3')
zii.plot(t,y3,'r-.')


zii.show()
