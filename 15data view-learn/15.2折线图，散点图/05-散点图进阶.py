import matplotlib.pyplot as plt

plt.scatter(2,4, s=200)#输入坐标s表示点的大小

#设置图表标题并给坐标轴加上标签
plt.title("square picture",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("square of value",fontsize = 14)

#设置刻度标记的大小
#plt.tick_params(axis='both',which ='major',labsize=14)

plt.show()#输出图形