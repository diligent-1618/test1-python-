import matplotlib.pyplot as plt

#输入点参数
x_values = list(range(1,1000))
y_values = [x**2 for x in x_values]

#生成散点图,默认蓝点黑轮廓，edgecolors=none是删除轮廓的,c=red控制颜色
plt.scatter(x_values, y_values,c = 'red',edgecolors='none',s=40)

#设置标题和数轴
plt.title("square title",fontsize=24)
plt.xlabel("x value",fontsize=14)
plt.ylabel("y value",fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

plt.show()