"""
계산기 프로그램
"""


class Calculator:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Calculator(self.num + other.num)

    def __sub__(self, other):
        return Calculator(self.num - other.num)

    def __mul__(self, other):
        return Calculator(self.num * other.num)

    def __divmod__(self, other):
        return Calculator(self.num / other.num)

    def __str__(self):
        return f'{self.num}'


cal = Calculator
c1 = cal(3)
c2 = cal(5)
res = c1+c2

print(res)
