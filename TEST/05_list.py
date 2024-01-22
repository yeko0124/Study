# ll = list()
# for i in range(10):
#     ll.append(i)
#
# print(ll)
#
# ll2 = [i for i in range(10) if i > 5]
#
# print(ll2)


# 0~n 숫자까지 합 출력
# 변수 2개 / 반복문 사용 / 100까지 순서대로 증가
def add_all(num: int):
    a = 0
    for i in range(num+1):
        # print(i)
        a = a + i
    print(a)


add_all(100)


def three_five(num):
    for i in range(num+1):
        if i % 5 == 0:
            if i % 3 == 0:
                print(f'{i}, ', end ='')


three_five(100)

print('\n', '-'*10)


def recur(v1, v2):
    print(v1)
    v1 = v1 + 1
    if v1 < v2 + 1:
        return recur(v1, v2)

# v1: 시작 숫자
# v2: 마무리 숫자


print('-'*100)


def recur2(N, E):
    if N > E:
        return
    print(N)
    recur2(N + 1, E)


recur2(1, 20)


# recur(1, 20)
