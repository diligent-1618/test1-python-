import matplotlib.pyplot as plt

from random_walk import RandomWalk#从rand_walk.py模块导入Randomwalk类

#只要程序处于活动状态，就不断模拟随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    #更换颜色，渐变色
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    plt.show()

    #多次循环
    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break