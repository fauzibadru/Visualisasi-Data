import numpy as zee
import matplotlib.pyplot as zii
index = zee.arange(5)
values1 = [5,7,3,4,6]
values2 = [6,5,4,5,5]
values3 = [4,6,5,4,6]
bw = 0.3
zii.axis([0,5,0,8])
zii.title('Diagram Batang Multiserial',fontsize=20)
zii.barh(index,values1,bw,color='b')
zii.barh(index+bw,values2,bw,color='g')
zii.barh(index+2*bw,values3,bw,color='r')
zii.yticks(index+1.5*bw,['A','B','C','D','E'])
zii.show()
