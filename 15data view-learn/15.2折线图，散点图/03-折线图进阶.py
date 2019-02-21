#coding=utf-8
import matplotlib.pyplot as plt
#设置x y轴的坐标数值
input_values = [1,2,3,4,5]#输入x轴坐标值
squares = [1,4,9,16,25]#输入y轴坐标值
plt.plot(input_values, squares, linewidth=5)

#设置图表标题并给坐标轴加上标签
plt.xlabel("x name",fontsize=14)
plt.title("title name",fontsize=24)
plt.ylabel("y name",fontsize=14)

#设置刻度标记大小
#plt.tick_params(axis='both',lablesize=14)

plt.show()
