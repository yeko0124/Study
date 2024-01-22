# 10bit -> 4 byte -> 1 byte -> 8bit
# 16진수는 0x
# 8진수는 0o

# 0, 1,2,....9 다음이 10이 아니고 A, B, C, D. E, F.... 가다가 10, 11 로 가는 거?
# (10진수, 2진수 16진수 8진수 wht)

a = "life is too short, you need python"


# print(a.count('y'))  # 몇개
# print(a.find('y'))  # 몇번째
# b = a.split()
# print(b)  # 공백 기준으로 자르기
# print(' '.join(b))  # 공백 기준으로 join
#
# print('--a--'.strip('-'))  # '-' 사라짐
#


def strip(word: str, w: str):
    # word: 단어 / w: 없애고 싶은 문자
    b = ()
    for i in range(len(word)):
        # print(word.find(w))
        b = word[i]
        # print(b)
        if b == w:
            continue
        else:
            print(b, end='')
    pass


strip('aaaaaohaaaaa', 'a')

lst = [1, 2, 3, 4, 5]
lst.insert(0, 5450)  # index 0번에다가 5450을 넣겠다.
print(lst)
print(lst.index(4))  # 4라는 숫자가 lst에 몇번째 인덱스에 잇는지 찾는 것
a = lst.pop()
print(lst)
print(a)

l1 = [1, 2]
l2 = [4, 5]
l1.extend(l2)
print(l1)

d = {'a': 55}
# dict 값 가져오는 방법
print(d['a'])
print(d.get('a'))

d['b'] = 500  # dict에 새로운 값 추가하기
print(d)

d.setdefault('TTT', -10)  # dict에 초기값
print(d)
d.setdefault('TTT', 0)  # 0이라고 햇는데도 아래 print값은 -10이다. 즉, 키는 만들고 싶은데 값은 안바꾸고 싶을 때 하는 방법임
print(d)

# TODO : 102page
# 교집합:
# 차집합:

a1 = [1, 2, 3]
a2 = [2, 3, 4]
s1 = set(l1)
s2 = set(l2)

print(s1 & s2)  # 교집합
print(s1 | s2)  # 합집합

print('here:', s1 ^ s2)  # 차집합

"""
1 ^ 0 = 1
1 ^ 1 = 0
0 ^ 0 = 0
0 ^ 1 = 1
"""


def union(lst1, lst2):
    result: list = lst1 + lst2
    result.sort()

    idx = 0
    box = list()
    while idx < len(result):
        ele = result[idx]
        if ele not in box:
            box.append(ele)
        idx += 1
    return box
    # 인덱스를 사용해서 값을 빼오는 방법
    # 인덱스랑 같이 하려면 ENUMERATE를 사용해야 함

    box2 = list()
    for i, e in enumerate(result):
        if e not in box2:
            box2.append(e)
    return box2


# 차집합 함수 구현 (한쪽엔 있는데 한쪽엔 없는거)


#
# print(a[-7:])
#
# print('{0} hello! {1} - {2}!!'.format('oh!', 'happy', 'day'))
#
# print(f'result:{1+2}')
