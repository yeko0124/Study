# 01
def sum_list(lst: list):
    a = 0
    for i in lst:
        a = a + i
    return print(a)

sum = [1, 6, 3]
sum_list(sum)


# 02
def second_largest(lst: list):
    t_lst = lst
    t_lst.sort()
    t_lst.reverse()
    print(t_lst[1])

second_largest(sum)


# 03
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calculate_area(self) -> int:
        res = self.__width * self.__height
        return res


rec = Rectangle(4, 5)
print(rec.calculate_area())


# 04
# TODO still solving it.... not over yet
def return_vowel(word: str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    lst = list(word)
    # comp = list(zip(lst, vowel))


return_vowel('apple')
