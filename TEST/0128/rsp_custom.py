import random
import sys
import pathlib
import time

from PySide2 import QtGui, QtCore, QtWidgets

import importlib
import rsp_game_ui


importlib.reload(rsp_game_ui)

"""
**레이블에 이미지 넣는 방법**

버튼을 누른다.
누른 이미지가 위에 label에 옮겨진다.(user)
label.setPixmap(pixmap)
label.setScaledContents(True)
"""


class Custom(QtWidgets.QWidget, rsp_game_ui.Ui_Form):
    rock = '/Users/yeko/Desktop/netflix_TD/self_study/Study/TEST/0128/img/rock.png'
    scissors = '/Users/yeko/Desktop/netflix_TD/self_study/Study/TEST/0128/img/scissors.png'
    paper = '/Users/yeko/Desktop/netflix_TD/self_study/Study/TEST/0128/img/paper.png'

    win = '/Users/yeko/Desktop/netflix_TD/self_study/Study/TEST/0128/img/win.png'
    draw = '/Users/yeko/Desktop/netflix_TD/self_study/Study/TEST/0128/img/draw.png'
    lose = '/Users/yeko/Desktop/netflix_TD/self_study/Study/TEST/0128/img/lose.png'

    rsp_lst = [rock, scissors, paper]  # 리스트를 사용하여 랜덤픽

    def __init__(self, parent=None):
        super(Custom, self).__init__(parent)
        self.setupUi(self)

        self.label__user_res.setScaledContents(True)
        self.label__com_res.setScaledContents(True)
        self.label__res_img.setScaledContents(True)

        self.toolButton__rock.setIcon(QtGui.QIcon(Custom.rock))
        self.toolButton__scissors.setIcon(QtGui.QIcon(Custom.scissors))
        self.toolButton__paper.setIcon(QtGui.QIcon(Custom.paper))
        self._signal_func()

        self.cnt = 0  # 이길 때마다 +1
        self.cnt_d = 0  # 비길 때마다 +1
        self.cnt_l = 0  # 질 때마다 +1


    def _signal_func(self):
        self.toolButton__rock.clicked.connect(self.set_rock)
        self.toolButton__scissors.clicked.connect(self.set_scissors)
        self.toolButton__paper.clicked.connect(self.set_paper)
        self.pushButton__stop.clicked.connect(self.cnt_add)


    def set_rock(self):
        self.label__res_img.setPixmap(QtGui.QPixmap())
        a = random.choice(Custom.rsp_lst)
        self.label__user_res.setPixmap(QtGui.QPixmap(Custom.rock))
        self.label__com_res.setPixmap(QtGui.QPixmap(a))

        if a == Custom.rock:
            self.cnt_d += 1
            print('draw')
        elif a == Custom.scissors:
            self.cnt += 1
            print('win')
        else:
            self.cnt_l += 1
            print('lose')

    def set_scissors(self):
        self.label__res_img.setPixmap(QtGui.QPixmap())
        b = random.choice(Custom.rsp_lst)
        self.label__user_res.setPixmap(QtGui.QPixmap(self.scissors))
        self.label__com_res.setPixmap(QtGui.QPixmap(b))

        if b == Custom.scissors:
            self.cnt_d += 1
            print('draw')
        elif b == Custom.paper:
            self.cnt += 1
            print('win')
        else:
            self.cnt_l += 1
            print('lose')

    def set_paper(self):
        self.label__res_img.setPixmap(QtGui.QPixmap())
        c = random.choice(Custom.rsp_lst)
        self.label__user_res.setPixmap(QtGui.QPixmap(self.paper))
        self.label__com_res.setPixmap(QtGui.QPixmap(c))

        if c == Custom.paper:
            self.cnt_d += 1
            print('draw')
        elif c == Custom.rock:
            self.cnt += 1
            print('win')
        else:
            self.cnt_l += 1
            print('lose')

    def cnt_add(self):
        a = self.cnt + self.cnt_d + self.cnt_l
        print(f'총 {a}번 진행하였고,\n'
              f'{self.cnt}번 이겼고, {self.cnt_d}번 비겼고, {self.cnt_l}번 졌습니다.')

        self.label__user_res.setPixmap(QtGui.QPixmap())
        self.label__com_res.setPixmap(QtGui.QPixmap())

        if self.cnt > (a - self.cnt_d - self.cnt):
            self.label__res_img.setPixmap(QtGui.QPixmap(Custom.win))
        elif self.cnt ==(a - self.cnt_d - self.cnt):
            self.label__res_img.setPixmap(QtGui.QPixmap(Custom.draw))
        elif self.cnt < (a - self.cnt_d - self.cnt):
            self.label__res_img.setPixmap(QtGui.QPixmap(Custom.lose))

        self.cnt, self.cnt_d, self.cnt_l = 0, 0, 0


        # res.show()

        # a = self.cnt_l + self.cnt + self.cnt_l
        # if self.cnt > a:
        #     res.signal(res.w)
        # elif self.cnt == a:
        #     res.signal(res.d)
        # else:
        #     res.signal(res.l)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cus = Custom()
    cus.show()
    sys.exit(app.exec_())
