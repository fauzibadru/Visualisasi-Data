import matplotlib.pyplot as zii

labels = ['Lain-Lain','Samsung','Apple','Huawei','Oppo','Vivo']
values = [42,21,14,9,8,7]
colors = ['blue','pink','green','red','orange','yellow']
explode = [0,1,0,0,0,0]

zii.title('Diagram Pie Market Share Samsung')
zii.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)
zii.axis('equal')
zii.show()
