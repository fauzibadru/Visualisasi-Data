import matplotlib.pyplot as zii
X, Y = [], []
for line in open('file.txt', 'r'):
    nilai = [float(s) for s in line.split()]
    X.append(nilai[0]) #nilai sumbu x
    Y.append(nilai[1]) #nilai sumbu y
zii.plot(X, Y)
zii.title('Data "file.text"')
zii.xlabel('x')
zii.ylabel('y')
zii.show()
