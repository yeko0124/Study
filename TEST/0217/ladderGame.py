'''
A, B, C
A User -> [B, C] 본인 제외하고 이 중 하나

ex)
A유저는 C의 코드를 A->C
'''

import random
import re

# def except_user(lst:list)

# name_lst_1 -> 고칠사람
# name_lst_2 -> 코드주인


class NAME:
    name = ['이지영', '고예은', '이상복', '김선희', '김준혁', '박정현', '김시안', '박준오', '성수진']

    def __init__(self):
        self.__lst = NAME.name
        self.name_lst1 = []
        self.name_lst2 = []

    def make_name_lst1(self, user: str):
        for i in self.__lst:
            if user == i:
                continue
            else:
                self.name_lst1.append(i)

    def make_name_lst2(self, lst: list):
        i = random.randrange(len(lst))
        user = lst[i]
        del lst[i]
        return user

    def main(self, lst: list):
        while len(lst) > 0:
            # print('1:', lst)
            i = random.randrange(len(lst))
            # user -> random 으로 픽된 사람이 저절로 들어감
            user = lst[i]
            del lst[i]

            # print('2:', self.__lst)
            print('고칠사람:', user, end='')  # 고칠 사람

            self.make_name_lst1(user)
            if len(lst) == 0:
                code = self.make_name_lst2(NAME.name)
                print('    코드주인:', code)
                break

            code = self.make_name_lst2(lst)  # 코드 주인
            print('    코드주인:', code)

            self.main(self.__lst)

# tODO 나왔던사람 X


if __name__ == '__main__':

    a = NAME()
    print(a.name)
    a.main(a.name)
