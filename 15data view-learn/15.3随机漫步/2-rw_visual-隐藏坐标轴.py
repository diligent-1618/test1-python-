import matplotlib.pyplot as plt

from random_walk import RandomWalk#从rand_walk.py模块导入Randomwalk类

#只要程序处于活动状态，就不断模拟随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    #更换颜色，渐变色
    plt.scatter(rw.x_values,rw.y_values,c='red',edgecolors='none',s=10)

    #隐藏坐标轴,注意此处一定是在输出图片之前
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    #输出图片
    plt.show()

    #进行一个判断，是否继续循环
    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break
