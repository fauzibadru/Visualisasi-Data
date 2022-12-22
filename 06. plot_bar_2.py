import numpy as zee
import matplotlib.pyplot as zii
index = zee.arange(5)
values = [5,7,3,4,6]
zii.bar(index,values)
zii.xticks(index+0.4,['A','B','C','D','E'])
zii.show()
