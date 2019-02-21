import matplotlib.pyplot as plt

from random_walk import RandomWalk#从rand_walk.py模块导入Randomwalk类

#只要程序处于活动状态，就不断模拟随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)#增大点的个数
    rw.fill_walk()

    #更换颜色，渐变色
    #point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values,linewidth=10)

    #调整图片分辨率以及大小
    plt.figure(figsize=(10,6))

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    #输出图片
    plt.show()

    #进行一个判断，是否继续循环
    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break
