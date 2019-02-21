import pygal
from die import Die

#创建俩D6骰子
die_1 = Die()
die_2 = Die()

#可以自己传参数设定骰子的面数
die_10 = Die(10)#创建一个10面的骰子

#掷骰子多次，并将结果存储到一个列表里
results = []

for roll_num in range(100):
    result = die_1.roll()+die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#可视化分析结果
hist = pygal.Bar()

hist.title = "Result of rolling two D6 dice 1000 times"
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist._x_title = "Result"
hist._y_title = "Frequency of result"

hist.add('D6+D6',frequencies)
hist.render_to_file('掷俩骰子直方图.svg')
