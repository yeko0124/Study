# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rsp_game.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import rsg_game_png_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 349)
        self.label__title = QLabel(Form)
        self.label__title.setObjectName(u"label__title")
        self.label__title.setGeometry(QRect(70, 20, 261, 41))
        font = QFont()
        font.setPointSize(15)
        self.label__title.setFont(font)
        self.label__title.setLayoutDirection(Qt.RightToLeft)
        self.label__title.setAlignment(Qt.AlignCenter)
        self.label__user_res = QLabel(Form)
        self.label__user_res.setObjectName(u"label__user_res")
        self.label__user_res.setGeometry(QRect(70, 90, 101, 101))
        self.label__com_res = QLabel(Form)
        self.label__com_res.setObjectName(u"label__com_res")
        self.label__com_res.setGeometry(QRect(220, 90, 101, 101))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 220, 381, 121))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton__rock = QToolButton(self.layoutWidget)
        self.toolButton__rock.setObjectName(u"toolButton__rock")
        self.toolButton__rock.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.toolButton__rock, 0, 0, 1, 1)

        self.toolButton__scissors = QToolButton(self.layoutWidget)
        self.toolButton__scissors.setObjectName(u"toolButton__scissors")
        self.toolButton__scissors.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.toolButton__scissors, 0, 1, 1, 1)

        self.toolButton__paper = QToolButton(self.layoutWidget)
        self.toolButton__paper.setObjectName(u"toolButton__paper")
        self.toolButton__paper.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.toolButton__paper, 0, 2, 1, 1)

        self.label__user_name = QLabel(Form)
        self.label__user_name.setObjectName(u"label__user_name")
        self.label__user_name.setGeometry(QRect(10, 190, 57, 15))
        self.label__com_name = QLabel(Form)
        self.label__com_name.setObjectName(u"label__com_name")
        self.label__com_name.setGeometry(QRect(330, 190, 57, 15))
        self.label__com_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label__title.setText(QCoreApplication.translate("Form", u"ROCK SCISSORS PAPER", None))
        self.label__user_res.setText("")
        self.label__com_res.setText("")
        self.toolButton__rock.setText("")
        self.toolButton__scissors.setText("")
        self.toolButton__paper.setText("")
        self.label__user_name.setText(QCoreApplication.translate("Form", u"User", None))
        self.label__com_name.setText(QCoreApplication.translate("Form", u"Com", None))
    # retranslateUi

