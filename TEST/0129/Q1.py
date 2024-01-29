"""
2~9단 중 홀수단 결과값만 누적하여 반환하는 함수
"""


# def odd_gugudan():
#     for d in range(2, 10):
#         for n in range(1, 10):

def odd_gugudan():
    for i in range(10, 81):
        dan = (i // 9) + 1
        num = (i % 9) + 1
        if dan % 2 == 1:
            print(f'{dan} x {num} = {dan*num}')
            if num == 9:
                print('----------\n')
        else:
            pass


odd_gugudan()
