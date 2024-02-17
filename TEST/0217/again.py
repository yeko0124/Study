import random

all_name = ['이지영', '고예은', '이상복', '김선희', '김준혁', '박정현', '김시안', '박준오', '성수진']
is_code_name = ['이지영', '고예은', '이상복', '박정현', '박준오', '성수진']


def code():
    for i in all_name:
        if i == random.choice(is_code_name):
            random.choice(is_code_name)
            print(f'{i}   --->   코드주인: {random.choice(is_code_name)}')
        else:
            print(f'{i}   --->   코드주인: {random.choice(is_code_name)}')


code()

# all_lst = ['선희', '상복', '예은', '지영', '준오', '시안', '정현', '수진', '준혁']
#
# for name in all_lst:
#     name_lst = ['정현', '준오', '예은', '지영', '상복', '수진']
#     if name in name_lst:
#         name_lst.remove(name)
#     couple = random.choice(name_lst)
#     print(f'{name}님의 짝꿍은 --> {couple}')
