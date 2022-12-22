import numpy as zee
import matplotlib.pyplot as zii
index = zee.arange(5)
values = [5,7,3,4,6]
std = [0.8,1,0.4,0.9,1.3]
zii.title('Diagram Batang')
zii.barh(index,values,xerr=std,error_kw={'ecolor':'0.1','capsize':6},alpha=0.7,label='First')
zii.yticks(index+0.4,['A','B','C','D','E'])
zii.legend(loc=5)
zii.show()
