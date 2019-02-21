import matplotlib.pyplot as plt

x_value = [1,2,3,4,5]#输入点的x值
y_value = [1,4,9,16,25]#输入点的y值

plt.scatter(x_value,y_value, s=200)#输入坐标

#设置图表标题并给坐标轴加上标签
plt.title("square picture",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("square of value",fontsize = 14)

#设置刻度标记的大小
#plt.tick_params(axis='both',which ='major',labsize=14)

plt.show()#输出图形
