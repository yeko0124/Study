# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form__calc(object):
    def setupUi(self, Form__calc):
        if not Form__calc.objectName():
            Form__calc.setObjectName(u"Form__calc")
        Form__calc.resize(358, 175)
        self.verticalLayout = QVBoxLayout(Form__calc)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit__a = QLineEdit(Form__calc)
        self.lineEdit__a.setObjectName(u"lineEdit__a")

        self.horizontalLayout.addWidget(self.lineEdit__a)

        self.lineEdit__b = QLineEdit(Form__calc)
        self.lineEdit__b.setObjectName(u"lineEdit__b")

        self.horizontalLayout.addWidget(self.lineEdit__b)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton__add = QPushButton(Form__calc)
        self.pushButton__add.setObjectName(u"pushButton__add")

        self.horizontalLayout_2.addWidget(self.pushButton__add)

        self.pushButton__sub = QPushButton(Form__calc)
        self.pushButton__sub.setObjectName(u"pushButton__sub")

        self.horizontalLayout_2.addWidget(self.pushButton__sub)

        self.pushButton__mul = QPushButton(Form__calc)
        self.pushButton__mul.setObjectName(u"pushButton__mul")

        self.horizontalLayout_2.addWidget(self.pushButton__mul)

        self.pushButton__div = QPushButton(Form__calc)
        self.pushButton__div.setObjectName(u"pushButton__div")

        self.horizontalLayout_2.addWidget(self.pushButton__div)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textEdit__res = QTextEdit(Form__calc)
        self.textEdit__res.setObjectName(u"textEdit__res")

        self.verticalLayout.addWidget(self.textEdit__res)


        self.retranslateUi(Form__calc)

        QMetaObject.connectSlotsByName(Form__calc)
    # setupUi

    def retranslateUi(self, Form__calc):
        Form__calc.setWindowTitle(QCoreApplication.translate("Form__calc", u"Form", None))
        self.pushButton__add.setText(QCoreApplication.translate("Form__calc", u"ADD", None))
        self.pushButton__sub.setText(QCoreApplication.translate("Form__calc", u"SUB", None))
        self.pushButton__mul.setText(QCoreApplication.translate("Form__calc", u"MUL", None))
        self.pushButton__div.setText(QCoreApplication.translate("Form__calc", u"DIV", None))
    # retranslateUi

