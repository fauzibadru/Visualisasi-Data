import matplotlib.pyplot as zii
with open('file.txt', 'r') as f:
    X, Y = zip(*[[float(s) for s in line.split()] for line in f])
zii.plot(X, Y)
zii.title ('Data "file.text"')
zii.xlabel('x')
zii.ylabel('y')
zii.show()
