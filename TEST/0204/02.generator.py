
def mygen():
    yield 'a'
    yield 'b'
    yield 'c'


m = mygen()

print(next(m))


# mygen2 / mygen3의 비교 -> 2는 제너레이터를 사용한거고 3은 안한거
def mygen2():
    for i in range(1, 1000):
        result = i * i
        yield result


# lst가 왔다갔다하다보니 메모리가 많이 쓰여서 성능 저하가 생김
def mygen3():
    lst = list()
    for i in range(1, 1000):
        lst.append(i * i)
    return lst


lst1 = [i * i for i in range(10)]
gen = (i * i for i in range(10))

print(lst1)
print(gen)
print(list(gen))
# list라고 불러야 리스트가 나온다.
# 이렇게 필요할 때 꺼내쓰는 것이 메모리를 아낄 수 있음.
