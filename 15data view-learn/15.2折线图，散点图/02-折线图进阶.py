import matplotlib.pyplot as plt

#相当于仅仅描绘出几个二维坐标点

squares = [1,4,9,16,25]
plt.plot(squares, linewidth=5)#相当于传输进入折线数据，并规定折线粗细

#设置图表标题，并给坐标轴加上标签fontsize是文字的大小

plt.title("Square Number",fontsize=24)#标注标题的名称
plt.xlabel("Value",fontsize=14)#标注x轴的名称或者单位
plt.ylabel("Square of Value",fontsize=14)#标注y轴的名称或单位

#设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.show()