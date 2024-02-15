"""
버블 정렬 -> python

l1 = [3, 4, 6, 9, 1, 23, 0]
l1.sort()  -> [0, 1, 3, 4, 6, 9, 23]
가 되도록 함수를 만들기

class사용해서 만들기

2중 for loop 을 해야 될듯 이라는 힌트를 주심
"""


class Bubble:
    def __init__(self, lst):
        self.lst = lst

    def swap(self, j):
        # tmp = self.lst[j]
        # self.lst[j] = self.lst[j+1]
        # self.lst[j+1] = tmp
        self.lst[j] ^= self.lst[j + 1]
        self.lst[j + 1] ^= self.lst[j]
        self.lst[j] ^= self.lst[j + 1]
        # exclusive or ? bit 연산자 0010 ^ 0011 = 0001 (두개를 비교하면서 다르면 1 같으면 0)

    def run_sort(self) -> list:
        length = len(self.lst)
        for i in range(length - 1):
            # if self.lst[i] > self.lst[i + 1]:
            #     tmp = self.lst[i]
            #     self.lst[i] = self.lst[i + 1]
            #     self.lst[i + 1] = tmp
            # 2중 포문을 하는 이유는, 무작정 1, 2 를 바꾸면 2가 1의 자리에 갓을 때 1이 사라지므로,
            # 미리 2를 다른 곳에 넣어두고 1을 2의 자리에 넣은 후 2를 1의 자리에 넣는 것임
            for j in range(length - i - 1):
                if self.lst[j] > self.lst[j + 1]:  # 오름차순으로 할건지, 내림차순으로 할 건지 이 부분에서 결정을 하는 것임
                    self.swap(j)
                    # tmp = self.lst[j]
                    # self.lst[j] = self.lst[j + 1]
                    # self.lst[j + 1] = tmp
        return self.lst

# callback 함수를 이용할 경우,
    def run_sort_call(self, callback_func) -> list:
        length = len(self.lst)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if callback_func is not None:
                    if callback_func(self.lst[j], self.lst[j+1]):
                        self.swap(j)
                else:
                    if self.lst[j] > self.lst[j + 1]:  # 오름차순으로 할건지, 내림차순으로 할 건지 이 부분에서 결정을 하는 것임
                        self.swap(j)
        return self.lst


# callback함수를 받게되면, 원하는 로직에 맞게 바뀔 수 있다. 없으면 default로 진행이 되는 것임
def callback(a, b):
    return a < b


l1 = [12, 5, 1, 10, 3]

bsort = Bubble(l1)
res = bsort.run_sort_call(callback)
print(res)
