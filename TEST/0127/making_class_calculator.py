"""
add, subtract, multiply, divide, exponent(pow(), a**b)
"""


class Calculator:
    def __init__(self, number: int):
        self.num = number

    def __add__(self, other):
        return Calculator(self.num + other.num)

    # def __add__(self, other):
    #     num = self.num + other.num
    #     return num

    def __sub__(self, other):
        return Calculator(self.num - other.num)

    def __mul__(self, other):
        return Calculator(self.num * other.num)

    def __truediv__(self, other):
        return Calculator(self.num / other.num)

    # def __pow__(self, other):
    #     num = self.num ** other.num
    #     return num
    #
    def __pow__(self, power, modulo=None):
        return Calculator(pow(self.num, power.num))

    def __str__(self):
        return f'Number: {self.num}'

    def __gt__(self, other):
        return self.num > other.num

    def is_great_than(self, cls2):
        return self.num > cls2.num


c = Calculator

print((c(3)**c(2)))

c1 = c(1)
c2 = c(2)
res = c1 + c2
print(res.__str__())

print(c2)

print(c1<c2)