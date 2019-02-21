from die import Die

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

print(frequencies)
