'''
회문 판독기

'abcdcba' -> boolean

def <function> (string):
    return boolean
'''


def mirror(word):
    a = 0
    b = -1
    for i in range(len(word)//2):
        # print(len(word))
        if word[a] == word[b]:
            pass
            # print(word[a], word[b])
        else:
            return False
        a += 1
        b -= 1
    return True


print(mirror('abcdcba'))

"""
teacher's code

ss = 'abcdcba'

def check_str(sstr):
    res = list()
    for idx in rangE(len(sstr)//2):
        res.append(sstr[idx] == str[-1 - idx]
    return all(res)

print(check_str(ss))

"""


# ------------------------------------
# 재귀호출 응용 / int -> str / 정수의 자릿수 계산 고민......

# TODO STUDY 필요,,
def flip_flop(num):
    if num <= 0:
        return
    print(f'{num % 10}', end ='')
    flip_flop(num // 10)


# flip_flop(123)

# ------------------------------------

# for i in range(27):
#     print(i % 10)
# print(27 %10)
# #
# for i in range(27):
#     print(i // 3)

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i*j}')
#
# for i in range(10):
#     print((i % 10 + 1), end ='')

# print('\n')
#
# for j in range(90):
#     print((j // 10 + 1), end ='')
#
for i in range(10, 81):
    a = (i % 9) + 1
    b = (i // 9) + 1
    print(f'{b}x{a}={a*b}')

