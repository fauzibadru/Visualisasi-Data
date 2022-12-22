import matplotlib.pyplot as zii
zii.axis([0,5,0,20]) #batas sumbu x dan sumbu y
zii.plot([1,2,3,4],[1,4,9,16],'ro-') #nilai data yang di plot
zii.text(1.1,12,'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
zii.title('Plot Data persamaan Kuadrat',fontsize=20,fontname='Times New Roman')
zii.xlabel('x',fontsize=16,fontname='Times New Roman',color='blue')
zii.ylabel('y',fontsize=16,fontname='Times New Roman',color='blue')
zii.grid(True)
zii.legend(['First series'])
zii.savefig('grafik.png')
zii.show()
