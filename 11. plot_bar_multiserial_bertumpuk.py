import numpy as zee
import matplotlib.pyplot as zii
series1 = zee.array([3,4,5,3])
series2 = zee.array([1,2,2,5])
series3 = zee.array([2,3,3,4])
index = zee.arange(4)
zii.axis([-0.5,3.5,0,15])
zii.title('Diagram Batang Bertumpuk Multiserial')
zii.bar(index,series1,color='r')
zii.bar(index,series2,color='b', bottom=series1)
zii.bar(index,series3,color='g', bottom=(series2+series1))
zii.xticks(index+0.4,['Sep21','Okt21','Nov21','Des21'])
zii.show()
