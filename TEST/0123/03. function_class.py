
# class 내의 __add__ override에 대해서

class Number:
    def __init__(self, number: int):
        self.num = number
        self.d = {'a': 55, 'n':44}

    def __add__(self, other):  # override  / other : 다음에 들어오는 객체  / self: 예약하는 느낌
        self.num += other.num
        return self  # 반환을 해줘야 받는 입장ㅇ에서도 속성으로 사용할 수가 있음. return self가 중요!!!

    def __sub__(self, other):
        self.num -= other.num
        return self

    def __mul__(self, other):
        self.num *= other.num
        return self

    def __divmod__(self, other):
        self.num /= other.num
        return self

    def __repr__(self):
        # repr: print할 때 이상한 문자가 들어가면 에러가 나는데,
        # repr은 그냥 그 문자 그대로 나오게 하는 것
        pass

    def __delitem__(self, key):
        print(f'remove item: {key}')
        # 키값을 이용해서, sequence data가 있다고 가정했을 때 사용할 수 있는 method
        # 만약 dict가 있으면, del이용해서 key를 부르면 지울 수가 있음(?) -> #TODO 더 찾아보기
        del self.d[key]


res = Number(5) + Number(7) + Number(12)
res = res - Number(4)

print(res.d)  # 출력: {'a': 55, 'n': 44}
del res.d['a']  # del 키워드 이용해서 key값을 넣어주면 바로 지워짐
print(res.d)  # 출력: {'n': 44}


print(res.num)

#
# class Calculate:
#     def __init__(self):
#         pass
#
#     def add(self, a: Number, b: Number) -> Number:
#         return Number(a.num + b.num)
#
#     def subtract(self, a: Number, b: Number) -> Number:
#         return Number(a.num - b.num)
#
#     def multiply(self, a: Number, b: Number) -> Number:
#         return Number(a.num * b.num)
#
#     def divide(self, a: Number, b: Number) -> Number:
#         return Number(a.num / b.num)
#
#
# cal = Calculate()
# n1 = Number(10)
# n2 = Number(5)
#
# result = cal.divide(n1, n2)
# print(result.num)


