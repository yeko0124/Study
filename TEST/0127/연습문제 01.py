
# 구구단 2-9단까지 거꾸로 출력 (9단, 2단)
"""
9*9 = 81
2*1 = 2
"""


def geogguro():
    for i in range(0,81):
        a = (i % 9) + 1
        b = (i // 9) + 1
        # 프린트 전에 거꾸로 해버리고 프린트하고 싶은데,,음

        print(f'{b}X{a}={a*b}')


# geogguro()


dan = [2, 3, 4, 5, 6, 7, 8, 9]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 추출할 때부터 -1 로 추출하는 방법 /
# or 제일 높은 숫자들끼리 먼저 곱해버리는,, 낮으면 pass로?


print(dan[0:-1])


def geogguro2(d, n):
    print('------------')
    for i in d:
        if i == d[-1]:
            b = -1
            for j in n:
                print(f'{i} X {num[b]} = {i*num[b]}')
                b -= 1
            else:
                geogguro2(d[:-1], n)


print(geogguro2(dan, num))
