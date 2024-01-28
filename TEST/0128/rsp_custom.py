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
label = QLabel(self)
pixmap = QPixmap('이미지 경로')
label.setPixmap(pixmap)
label.setScaledContents(True)
self.setCentralWidget(label)
self.resize(pixmap.width(), pixmap.height()) 
"""


class Custom(QtWidgets.QWidget, rsp_game_ui.Ui_Form):
    rock = '/home/rapa/workspace/python/week_07/0128/img/rock.png'
    scissors = '/home/rapa/workspace/python/week_07/0128/img/scissors.png'
    paper = '/home/rapa/workspace/python/week_07/0128/img/paper.png'

    rsp_lst = [rock, scissors, paper]

    def __init__(self, parent=None):
        super(Custom, self).__init__(parent)
        self.setupUi(self)

        self.label__user_res.setScaledContents(True)
        self.label__com_res.setScaledContents(True)

        self._signal_func()

        self.toolButton__rock.setIcon(QtGui.QIcon(Custom.rock))
        self.toolButton__scissors.setIcon(QtGui.QIcon(Custom.scissors))
        self.toolButton__paper.setIcon(QtGui.QIcon(Custom.paper))

        # self.compare()

    def _signal_func(self):
        self.toolButton__rock.clicked.connect(self.set_rock)
        self.toolButton__scissors.clicked.connect(self.set_scissors)
        self.toolButton__paper.clicked.connect(self.set_paper)

    def set_rock(self):
        self.label__user_res.setPixmap(QtGui.QPixmap(Custom.rock))
        self.label__com_res.setPixmap(QtGui.QPixmap(random.choice(Custom.rsp_lst)))

    def set_scissors(self):
        self.label__user_res.setPixmap(QtGui.QPixmap(self.scissors))
        self.label__com_res.setPixmap(QtGui.QPixmap(random.choice(Custom.rsp_lst)))

    def set_paper(self):
        self.label__user_res.setPixmap(QtGui.QPixmap(self.paper))
        a = random.choice(Custom.rsp_lst)
        self.label__com_res.setPixmap(QtGui.QPixmap(a))

    def compare(self):
        pass
    # 모러그ㅔ[ㅆ다아


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cus = Custom()
    cus.show()
    sys.exit(app.exec_())
