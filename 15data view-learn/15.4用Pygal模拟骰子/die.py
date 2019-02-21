from random import randint
class Die():
    '''表示一个骰子的类'''

    def __init__(self, num_sides=6):
        '''默认骰子的6个面'''
        self.num_sides = num_sides

    def roll(self):#相当于自动返回掷骰子的值
        '''返回一个位于1和骰子面之间的随机数值'''
        return randint(1,self.num_sides)