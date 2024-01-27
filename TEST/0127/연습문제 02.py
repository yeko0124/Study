"""
어떤 수열 N에서 시작해 N이 짝수면 2로 나누고, 홀수면 3을 곱한 다음 1을 더한다.
이렇게해서 새로 만들어진 숫자를 N으로 놓고 N =1 이 될때까지 같은 작업을 계속 반복.
N =22면 다음과 같은 수열이 만들어짐.
22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

조건
N을 함수인자로 전달하면 해당 n의 수열을 리스트로 반환
해당 리스트를 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 이런 형태로 출력
"""


def list_maker(num):
    lst = list()
    lst.append(num)
    if num != 1:
        if num % 2 == 0:
            num = num // 2
            lst.append(num)
            list_maker(num)
        elif num % 2 == 1:
            num = (num * 3) + 1
            lst.append(num)
            list_maker(num)
        return lst


nn = 22

print(list_maker(nn))


def get_num(n):
    lst = list()
    lst.append(n)
    while True:
        if n % 2 == 0:
        # if n & 0x01:  bit연산으로도 가능함
            n = n//2
        else:
            n = n * 3 + 1
        if n <= 1:
            lst.append(n)
            break
        lst.append(n)
    return lst


print(get_num(nn))

