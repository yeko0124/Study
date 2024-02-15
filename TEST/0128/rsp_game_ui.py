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
        Form.resize(400, 359)
        palette = QPalette()
        brush = QBrush(QColor(17, 17, 17, 217))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(21, 21, 21, 217))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush3 = QBrush(QColor(23, 23, 23, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(30, 30, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush4)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(36, 36, 36, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(21, 21, 21, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        brush8 = QBrush(QColor(255, 255, 255, 63))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        brush9 = QBrush(QColor(31, 31, 31, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        Form.setPalette(palette)
        self.label__title = QLabel(Form)
        self.label__title.setObjectName(u"label__title")
        self.label__title.setGeometry(QRect(110, 20, 169, 18))
        font = QFont()
        font.setPointSize(15)
        self.label__title.setFont(font)
        self.label__title.setLayoutDirection(Qt.RightToLeft)
        self.label__title.setAlignment(Qt.AlignCenter)
        self.label__user_res = QLabel(Form)
        self.label__user_res.setObjectName(u"label__user_res")
        self.label__user_res.setGeometry(QRect(50, 80, 131, 121))
        self.label__com_res = QLabel(Form)
        self.label__com_res.setObjectName(u"label__com_res")
        self.label__com_res.setGeometry(QRect(240, 100, 101, 101))
        self.label__com_res.setLineWidth(3)
        self.pushButton__stop = QPushButton(Form)
        self.pushButton__stop.setObjectName(u"pushButton__stop")
        self.pushButton__stop.setGeometry(QRect(160, 320, 77, 32))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 50, 301, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label__user_name = QLabel(self.layoutWidget)
        self.label__user_name.setObjectName(u"label__user_name")

        self.horizontalLayout.addWidget(self.label__user_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label__com_name = QLabel(self.layoutWidget)
        self.label__com_name.setObjectName(u"label__com_name")
        self.label__com_name.setAlignment(Qt.AlignRight | Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label__com_name)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 220, 401, 81))
        self.layoutWidget_2 = QWidget(self.groupBox)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 0, 381, 81))
        self.gridLayout = QGridLayout(self.layoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.toolButton__rock = QToolButton(self.layoutWidget_2)
        self.toolButton__rock.setObjectName(u"toolButton__rock")
        self.toolButton__rock.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.toolButton__rock, 0, 1, 1, 1)

        self.toolButton__scissors = QToolButton(self.layoutWidget_2)
        self.toolButton__scissors.setObjectName(u"toolButton__scissors")
        self.toolButton__scissors.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.toolButton__scissors, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 4, 1, 1)

        self.toolButton__paper = QToolButton(self.layoutWidget_2)
        self.toolButton__paper.setObjectName(u"toolButton__paper")
        self.toolButton__paper.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.toolButton__paper, 0, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 6, 1, 1)

        self.label__res_img = QLabel(Form)
        self.label__res_img.setObjectName(u"label__res_img")
        self.label__res_img.setGeometry(QRect(140, 80, 121, 131))
        self.layoutWidget.raise_()
        self.label__title.raise_()
        self.label__user_res.raise_()
        self.label__com_res.raise_()
        self.pushButton__stop.raise_()
        self.groupBox.raise_()
        self.label__res_img.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label__title.setText(QCoreApplication.translate("Form", u"ROCK SCISSORS PAPER", None))
        self.label__user_res.setText("")
        self.label__com_res.setText("")
        self.pushButton__stop.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.label__user_name.setText(QCoreApplication.translate("Form", u"User", None))
        self.label__com_name.setText(QCoreApplication.translate("Form", u"Com", None))
        self.groupBox.setTitle("")
        self.toolButton__rock.setText("")
        self.toolButton__scissors.setText("")
        self.toolButton__paper.setText("")
        self.label__res_img.setText("")
    # retranslateUi

