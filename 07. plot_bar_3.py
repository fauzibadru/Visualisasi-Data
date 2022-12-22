import numpy as zee
import matplotlib.pyplot as zii
index = zee.arange(5)
values = [5,7,3,4,6]
std = [0.8,1,0.4,0.9,1.3]
zii.title('Diagram Batang')
zii.bar(index,values,yerr=std,error_kw={'ecolor':'0.1','capsize':6},alpha=0.7,label='First')
zii.xticks(index+0.4,['A','B','C','D','E'])
zii.legend(loc=2)
zii.show()
