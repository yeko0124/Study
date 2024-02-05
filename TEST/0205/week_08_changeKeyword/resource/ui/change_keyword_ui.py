# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_keyword.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow__change_keyword(object):
    def setupUi(self, MainWindow__change_keyword):
        if not MainWindow__change_keyword.objectName():
            MainWindow__change_keyword.setObjectName(u"MainWindow__change_keyword")
        MainWindow__change_keyword.resize(412, 220)
        self.centralwidget = QWidget(MainWindow__change_keyword)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 364, 151))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit__pdr = QLineEdit(self.widget)
        self.lineEdit__pdr.setObjectName(u"lineEdit__pdr")

        self.horizontalLayout.addWidget(self.lineEdit__pdr)

        self.toolButton__pdr = QToolButton(self.widget)
        self.toolButton__pdr.setObjectName(u"toolButton__pdr")

        self.horizontalLayout.addWidget(self.toolButton__pdr)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label__ext = QLabel(self.widget)
        self.label__ext.setObjectName(u"label__ext")

        self.horizontalLayout_4.addWidget(self.label__ext)

        self.lineEdit__ext = QLineEdit(self.widget)
        self.lineEdit__ext.setObjectName(u"lineEdit__ext")

        self.horizontalLayout_4.addWidget(self.lineEdit__ext)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label__chs = QLabel(self.widget)
        self.label__chs.setObjectName(u"label__chs")

        self.horizontalLayout_2.addWidget(self.label__chs)

        self.lineEdit__chs = QLineEdit(self.widget)
        self.lineEdit__chs.setObjectName(u"lineEdit__chs")

        self.horizontalLayout_2.addWidget(self.lineEdit__chs)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label__chp = QLabel(self.widget)
        self.label__chp.setObjectName(u"label__chp")

        self.horizontalLayout_3.addWidget(self.label__chp)

        self.lineEdit__chp = QLineEdit(self.widget)
        self.lineEdit__chp.setObjectName(u"lineEdit__chp")

        self.horizontalLayout_3.addWidget(self.lineEdit__chp)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.progressBar_progress = QProgressBar(self.widget)
        self.progressBar_progress.setObjectName(u"progressBar_progress")
        self.progressBar_progress.setValue(24)

        self.verticalLayout.addWidget(self.progressBar_progress)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton__start = QPushButton(self.widget)
        self.pushButton__start.setObjectName(u"pushButton__start")

        self.horizontalLayout_6.addWidget(self.pushButton__start)

        self.pushButton__stop = QPushButton(self.widget)
        self.pushButton__stop.setObjectName(u"pushButton__stop")

        self.horizontalLayout_6.addWidget(self.pushButton__stop)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        MainWindow__change_keyword.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow__change_keyword)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 412, 20))
        MainWindow__change_keyword.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow__change_keyword)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow__change_keyword.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow__change_keyword)

        QMetaObject.connectSlotsByName(MainWindow__change_keyword)
    # setupUi

    def retranslateUi(self, MainWindow__change_keyword):
        MainWindow__change_keyword.setWindowTitle(QCoreApplication.translate("MainWindow__change_keyword", u"MainWindow", None))
        self.lineEdit__pdr.setPlaceholderText(QCoreApplication.translate("MainWindow__change_keyword", u"/home/rapa", None))
        self.toolButton__pdr.setText(QCoreApplication.translate("MainWindow__change_keyword", u"...", None))
        self.label__ext.setText(QCoreApplication.translate("MainWindow__change_keyword", u"\ud30c\uc77c\ud655\uc7a5\uc790", None))
        self.lineEdit__ext.setPlaceholderText(QCoreApplication.translate("MainWindow__change_keyword", u".h .cpp", None))
        self.label__chs.setText(QCoreApplication.translate("MainWindow__change_keyword", u"\ubcc0\uacbd\ud560 \ubb38\uc790\uc5f4", None))
        self.lineEdit__chs.setPlaceholderText(QCoreApplication.translate("MainWindow__change_keyword", u"#include \"PXR2", None))
        self.label__chp.setText(QCoreApplication.translate("MainWindow__change_keyword", u"\ucc3e\uc744 \ud328\ud134", None))
        self.lineEdit__chp.setPlaceholderText(QCoreApplication.translate("MainWindow__change_keyword", u"#include \"pxr", None))
        self.pushButton__start.setText(QCoreApplication.translate("MainWindow__change_keyword", u"Start", None))
        self.pushButton__stop.setText(QCoreApplication.translate("MainWindow__change_keyword", u"Stop", None))
    # retranslateUi

