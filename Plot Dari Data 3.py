import matplotlib.pyplot as zii
import numpy as zee

data = zee.loadtxt('file.txt')

zii.plot(data[:,0], data[:,1])
zii.title ('Data "file.text"')
zii.xlabel('x')
zii.ylabel('y')
zii.show()

