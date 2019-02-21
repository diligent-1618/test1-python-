import matplotlib.pyplot as plt

x_value = list(range(1,101))
y_value = [x**3 for x in x_value]

#设定散点图图形的颜色，点大小
plt.scatter(x_value, y_value,c = y_value,cmap=plt.cm.Blues,edgecolors='none',s=40)

#设定散点图的标题，x轴y轴的名称
plt.title('square',fontsize=24)
plt.xlabel('x name',fontsize=14)
plt.ylabel('y name',fontsize=14)

#设定坐标轴取值范围
plt.axis([0,110,0,1000000])

#输出图形
plt.show()