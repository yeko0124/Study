"""
계산기 프로그램
"""
import sys
from PySide2 import QtGui, QtWidgets, QtCore

import importlib
import cal_custom_ui

importlib.reload(cal_custom_ui)


class Calculator(QtWidgets.QWidget, cal_custom_ui.Ui_Form):
    def __init__(self, num=None, parent=None):
        super(Calculator, self).__init__(parent)
        self.num = num

        self.dis1 = 0
        self.dis2 = 0

        self.setupUi(self)

        self.num_lst = []
        self.num_lst2 = []

        self._signal()

    def _signal(self):
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

        self.pushButton_res.clicked.connect(self.res_show)

    # TODO: 하나하나 다 안쓰고도 할 수 있는 방법이 뭘까? 너무 반복되는데..

    def set1(self):
        self.lcdNumber.display(1)
        self.num = 1
        self.num_lst.append(self.num)
        return self.num_lst

    def set2(self):
        self.lcdNumber.display(2)
        self.num = 2
        self.num_lst.append(self.num)
        return self.num_lst

    def set3(self):
        self.lcdNumber.display(3)
        self.num = 3
        self.num_lst.append(self.num)
        return self.num_lst

    def set4(self):
        self.lcdNumber.display(4)
        self.num = 4
        self.num_lst.append(self.num)
        return self.num_lst

    def set5(self):
        self.lcdNumber.display(5)
        self.num = 5
        self.num_lst.append(self.num)
        return self.num_lst

    def set6(self):
        self.lcdNumber.display(6)
        self.num = 6
        self.num_lst.append(self.num)
        return self.num_lst

    def set7(self):
        self.lcdNumber.display(7)
        self.num = 7
        self.num_lst.append(self.num)
        return self.num_lst

    def set8(self):
        self.lcdNumber.display(8)
        self.num = 8
        self.num_lst.append(self.num)
        return self.num_lst

    def set9(self):
        self.lcdNumber.display(9)
        self.num = 9
        self.num_lst.append(self.num)
        return self.num_lst

    def set0(self):
        self.lcdNumber.display(0)
        self.num = 0
        self.num_lst.append(self.num)
        return self.num_lst

    @staticmethod
    def make_num(lst):
        # reversed를 하면 뒤에서부터 오니까,
        # 1의 자리는 0으로 시작해서 10씩 제곱해주고 제곱한 값을 더하면 될 듯.
        res = 0
        j = 0
        for i in reversed(lst):
            i = i * 10**j
            res += i
            j = j+1
        return res

    # eval을 써야하나
    def res_show(self):
        self.dis1 = self.make_num(self.num_lst2)
        self.dis2 = self.make_num(self.num_lst)
        r = self.dis1 + self.dis2
        print(f'{self.dis2}\n-----\n={r}')
        self.lcdNumber.display(r)
        self.num_lst = []

    def add(self):
        self.dis1 = self.make_num(self.num_lst)  # res가 저장이 됌(int)
        # add를 누르고 나서 뒤의 숫자를 입력하기 때문에,
        # lambda로 임시 함수를 지정해야 하나??? 변수를 늦게 받으니까..?
        self.lcdNumber.display(self.dis1)
        # other 를 쓰고 싶은데,,,,!!!!!!!!
        print(f'{self.dis1}\n+ ')
        self.num_lst2 = self.num_lst
        self.num_lst = []
        # todo: other.make_num()을 할 수 있는 방법이 뭘까 -> RES 에서 써야하나?

    # eval을 쓰면 될까 ????????
    def sub(self):
        self.dis1 = self.make_num(self.num_lst)  # res가 저장이 됌(int)
        self.lcdNumber.display(self.make_num(self.num_lst))
        print(f'{self.make_num(self.num_lst)} - ')
        self.num_lst2 = self.num_lst
        self.num_lst = []

    def mul(self):
        self.dis1 = self.make_num(self.num_lst)  # res가 저장이 됌(int)
        self.lcdNumber.display(self.make_num(self.num_lst))
        print(f'{self.make_num(self.num_lst)} * ')
        self.num_lst2 = self.num_lst
        self.num_lst = []

    def div(self):
        self.dis1 = self.make_num(self.num_lst)  # res가 저장이 됌(int)
        self.lcdNumber.display(self.make_num(self.num_lst))
        print(f'{self.make_num(self.num_lst)} % ')
        self.num_lst2 = self.num_lst
        self.num_lst = []

    # def __add__(self, other):
    #     # for i in self.num_lst:
    #     print(Calculator(self.make_num() + other.make_num()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cal = Calculator()
    cal.show()
    sys.exit(app.exec_())
