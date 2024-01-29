"""
재귀 함수 1~100까지 더한 값을 반환하는 함수
"""


def spit_100(num, res):
    if num < 101:
        res += num
        # print(res)
        num += 1
        spit_100(num, res)
    else:
        print('result:', res)


result = 0
spit_100(1, result)
