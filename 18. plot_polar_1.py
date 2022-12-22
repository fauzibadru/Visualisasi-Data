import numpy as zee
import matplotlib.pyplot as zii
N = 8
theta = zee.arange(0.,2*zee.pi, 2*zee.pi / N)
radius = zee.array([4,7,5,3,1,5,6,7])
zii.axes([0.025, 0.025, 0.95, 0.95], polar=True)
colors = zee.array(['#4bb2c5', '#c5b47f', '#EAA228', '#579575', '#839557', '#4b5de4'])
bars = zii.bar(theta, radius, width=(2*zee.pi/N), bottom=0.0, color=colors)
zii.show()
