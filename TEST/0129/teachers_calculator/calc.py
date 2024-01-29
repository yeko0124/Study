

import importlib
import sys

from PySide2 import QtWidgets, QtGui, QtCore
import calc_ui

importlib.reload(calc_ui)   # 새로 ui파일을 convert할 때 reload가 되도록 하는 것


class Calculator(QtWidgets.QWidget, calc_ui.Ui_Form__calc):   # 코딩할 때 더 편하게 하려고 다중상속을 받는 것임
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Calculator')

    # add버튼을 클릭했을 때 slot_calc method를 호출하면서 '+'기호를 전달해줌
        self.pushButton__add.clicked.connect(
            lambda: self.slot_calc('+'))

        self.pushButton__sub.clicked.connect(
            lambda: self.slot_calc('-'))

        self.pushButton__div.clicked.connect(
            lambda: self.slot_calc('/'))

        self.pushButton__mul.clicked.connect(
            lambda: self.slot_calc('*'))
        # 매개변수가 없는 이름없는 함수(익명 함수)
        # lambda가 없으면 함수라서 갑자기 호출이 되어버린다.
        # lambda로 감싸줘서 함수가 호출되지 않도록 한다.

    def slot_calc(self, var: str):  # var는 사칙연산을 전달해주기 위한 인자
        a = self.get_num('a')
        b = self.get_num()   # 이미 get_num에서 'b'를 default값으로 줘서 인자를 안 줘도 됌
        res = eval('{0} {1} {2}'.format(a, var, b))
        # eval -> evaluate의 약자. 문자열을 계산해주는 함수. string으로 받아야 함
        self.textEdit__res.setText(f'결과 값은? {res}')

    def get_num(self, var_str: str = 'b') -> str:
        if var_str == 'a':
            return self.lineEdit__a.text().strip()
        return self.lineEdit__b.text().strip()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
