import numpy as zee
import matplotlib.pyplot as zii
series1 = zee.array([3,4,5,3])
series2 = zee.array([1,2,2,5])
series3 = zee.array([2,3,3,4])
index = zee.arange(4)
zii.axis([0,15,-0,3.5])
zii.title('Diagram Batang Bertumpuk Multiserial')
zii.barh(index,series1,color='r')
zii.barh(index,series2,color='b', left=series1)
zii.barh(index,series3,color='g', left=(series2+series1))
zii.yticks(index+0.4,['Sep21','Okt21','Nov21','Des21'])
zii.show()
