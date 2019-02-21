from die import Die
import pygal

#创建一个D6
die = Die()

#掷几次骰子，并讲结果存储在一个列表
results =[]

for roll_num in range(100):
    result = die.roll()
    results.append(result)

#分析结果-分析每个点出现的次数
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化处理--绘制直方图
hist = pygal.Bar()

#设置图表标题及坐标信息
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

#染色，以及输出图片
hist.add('D6', frequencies)
hist.render_to_file('直方图.svg')
