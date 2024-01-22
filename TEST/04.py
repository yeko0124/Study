
def edan(num):
    i = 1
    while i < 10:
        a = i * num
        print(f'{num} x {i} = {a}')
        i += 1


# edan(2)


def gugudan(n):
    num = n
    i = 1
    print(f'--------{num}단 시작!!---------')
    while i < 10:
        a = i * num
        print(f'{num} x {i} = {a}')
        i += 1
        if i == 10:
            if num < 9:
                gugudan(n+1)


# 무조건 9단까지 나오는 함수임. 몇단부터 볼건지 숫자적기
# gugudan(2)

dan = 2

while dan < 10:
    if dan == 3 or dan == 5:
        var = 0
        while var < 9:
            var += 1
            res = dan * var
            print(f'{dan} x {var} = {res}')
        dan += 1
    else:
        dan += 1
#
# print('\ncontinue\n')
# # continue / break
# while dan < 10:
#     var = 0
#     # print(dan)
#     if dan != 3 and dan != 5:
#         while var < 9:
#             var += 1
#             res = dan * var
#             print(f'{dan} x {var} = {res}')
#         dan += 1
#     else:
#         continue
#     if dan == 6:
#         break
#     dan += 1


# TODO 쌤 코드
# while dan < 10:
#     dan += 1
#     if dan != 3 and dan != 5:
#         continue
#     variable = 0
#     while variable <9:
#         variable +=1
#         result = dan * variable
#         print(f'{dan} x {var} = {res}')
#
#
# while dan < 10:
#     variable = 0
#     while variable < 9:
#         if dan !=3 and dan != 5:
#             break
#         variable += 1
#         reuslt = dan * variable
#         print(f'{dan} x {var} = {res}')
#     dan += 1