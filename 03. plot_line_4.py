import numpy as zee
import matplotlib.pyplot as zii
x = zee.arange(-2*zee.pi,2*zee.pi,0.01)
y1 = zee.sin(x)/x
y2 = zee.sin(2*x)/x
y3 =zee.sin(3*x)/x
zii.plot(x,y1,color='b')
zii.plot(x,y2,color='r')
zii.plot(x,y3,color='g')
zii.xticks([-1,0,+1,+2,+3],
[r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])
zii.yticks([-2*zee.pi, -zee.pi, 0, zee.pi, 2*zee.pi],
[r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
ax = zii.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
zii.show()
