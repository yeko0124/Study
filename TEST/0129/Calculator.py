"""
(사칙연산 한번만 누를 수 있는, 일회용)
신기한 계산기 프로그램.....입니다..^_^
"""

import sys
from PySide2 import QtGui, QtWidgets, QtCore

import importlib
import cal_custom_ui

importlib.reload(cal_custom_ui)


class Calculator(QtWidgets.QWidget, cal_custom_ui.Ui_Form):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('사칙연산 한번만 누를 수 있는 계신기')

        self.num = 0  # 버튼을 누를 때, 그에 맞는 숫자를 받기 위한 용도

        # 리스트들은 1의 자리수부터 10의 0제곱으로 시작해서,
        # 1, 10, 100 씩 곱해주며 더해주기 위해 사용하였음
        self.num_lst = []  # 사칙연산 누르기 전의 숫자들을 받을 리스트
        self.num_lst2 = []  # 사칙연산 누른 후의 숫자들을 받기 위해 lst를 lst2로 옮겨놓기 위함

        self.dis1 = 0  # lst를 값으로 변환한 후에 저장하기 위한 용도
        self.dis2 = 0   # lst2를 값으로 변환한 후에 저장하기 위한 용도
        # dis1, dis2를 str으로 변환하여 eval로 계산할 수 있게 됌.

        self.str_to_eval = ' '  # eval을 하기 위한 비어있는 변수

        self._signal()

    def _signal(self):
        # TODO: 하나하나 다 안쓰고도 할 수 있는 방법이 뭘까? 너무 반복되는데..
        # 그래도 일단은, 각 버튼마다 시그널을 주기 위해 하나씩 다 만듦
        self.pushButton_1.clicked.connect(self.set1)
        self.pushButton_2.clicked.connect(self.set2)
        self.pushButton_3.clicked.connect(self.set3)
        self.pushButton_4.clicked.connect(self.set4)
        self.pushButton_5.clicked.connect(self.set5)
        self.pushButton_6.clicked.connect(self.set6)
        self.pushButton_7.clicked.connect(self.set7)
        self.pushButton_8.clicked.connect(self.set8)
        self.pushButton_9.clicked.connect(self.set9)
        self.pushButton_0.clicked.connect(self.set0)

        self.pushButton__add.clicked.connect(self.add)
        self.pushButton__div.clicked.connect(self.div)
        self.pushButton__mul.clicked.connect(self.mul)
        self.pushButton__sub.clicked.connect(self.sub)

        self.pushButton_res.clicked.connect(self.calculate)

    def set1(self):
        self.lcdNumber.display(1)
        self.num = 1
        print(1, end = '')
        self.num_lst.append(self.num)
        # return self.num_lst

    def set2(self):
        self.lcdNumber.display(2)
        self.num = 2
        print(2, end = '')
        self.num_lst.append(self.num)
        # return self.num_lst

    def set3(self):
        self.lcdNumber.display(3)
        self.num = 3
        print(3, end = '')
        self.num_lst.append(self.num)
        # return self.num_lst

    def set4(self):
        self.lcdNumber.display(4)
        self.num = 4
        print(4, end ='')
        self.num_lst.append(self.num)
        # return self.num_lst

    def set5(self):
        self.lcdNumber.display(5)
        self.num = 5
        print(5, end ='')
        self.num_lst.append(self.num)
        # return self.num_lst

    def set6(self):
        self.lcdNumber.display(6)
        self.num = 6
        print(6, end ='')
        self.num_lst.append(self.num)
        # return self.num_lst

    def set7(self):
        self.lcdNumber.display(7)
        self.num = 7
        print(7, end = '')
        self.num_lst.append(self.num)
        # return self.num_lst

    def set8(self):
        self.lcdNumber.display(8)
        self.num = 8
        print(8, end ='')
        self.num_lst.append(self.num)
        # return self.num_lst

    def set9(self):
        self.lcdNumber.display(9)
        self.num = 9
        print(9, end ='')
        self.num_lst.append(self.num)
        # return self.num_lst

    def set0(self):
        self.lcdNumber.display(0)
        self.num = 0
        print(0, end ='')
        self.num_lst.append(self.num)
        # return self.num_lst

    def make_num(self, lst):
        # reversed를 하면 뒤에서부터 오니까,
        # 1의 자리는 0으로 시작해서 10씩 제곱해주고 제곱한 값을 더하면 될 듯.
        res = 0
        j = 0
        for i in reversed(lst):
            i = i * 10**j
            res += i
            self.lcdNumber.display(res)
            j = j+1
        return res

    def calculate(self, var: str):
        self.dis1 = self.make_num(self.num_lst2)
        self.dis2 = self.make_num(self.num_lst)
        self.str_to_eval += str(self.dis2)
        print('\n----------')
        e = eval(self.str_to_eval)
        print(f'={e}\n')
        self.lcdNumber.display(e)
        self.num_lst = []
        self.dis1, self.dis2, self.str_to_eval = 0, 0, ''
        # print(e)

    def save_num(self):
        self.dis1 = self.make_num(self.num_lst)  # res가 저장이 됌(int)
        self.lcdNumber.display(self.dis1)
        self.num_lst2 = self.num_lst
        self.num_lst = []

    def add(self):
        self.save_num()
        self.str_to_eval = str(f'{self.dis1}+')
        print('\n+')

    def sub(self):
        self.save_num()
        self.str_to_eval = str(f'{self.dis1}-')
        print('\n-')

    def mul(self):
        self.save_num()
        self.str_to_eval = str(f'{self.dis1}*')
        print('\nx')

    def div(self):
        self.save_num()
        self.str_to_eval = str(f'{self.dis1}/')
        print('\n%')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cal = Calculator()
    cal.show()
    sys.exit(app.exec_())
