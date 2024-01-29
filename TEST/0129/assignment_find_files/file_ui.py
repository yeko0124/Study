# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(424, 394)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 50, 381, 281))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 341, 241))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.comboBox__lost_imgs = QComboBox(self.layoutWidget)
        self.comboBox__lost_imgs.setObjectName(u"comboBox__lost_imgs")

        self.horizontalLayout.addWidget(self.comboBox__lost_imgs)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget__lost_files_lst = QListWidget(self.layoutWidget)
        self.listWidget__lost_files_lst.setObjectName(u"listWidget__lost_files_lst")

        self.verticalLayout_2.addWidget(self.listWidget__lost_files_lst)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 101, 21))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.layoutWidget_2 = QWidget(self.page_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 30, 342, 241))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.comboBox__zero_imgs = QComboBox(self.layoutWidget_2)
        self.comboBox__zero_imgs.setObjectName(u"comboBox__zero_imgs")

        self.horizontalLayout_4.addWidget(self.comboBox__zero_imgs)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listWidget__zero_files_lst = QListWidget(self.layoutWidget_2)
        self.listWidget__zero_files_lst.setObjectName(u"listWidget__zero_files_lst")

        self.verticalLayout_4.addWidget(self.listWidget__zero_files_lst)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 131, 21))
        self.stackedWidget.addWidget(self.page_2)
        self.toolButton__select_dir = QToolButton(self.centralwidget)
        self.toolButton__select_dir.setObjectName(u"toolButton__select_dir")
        self.toolButton__select_dir.setGeometry(QRect(158, 20, 26, 22))
        self.lineEdit__select_dir = QLineEdit(self.centralwidget)
        self.lineEdit__select_dir.setObjectName(u"lineEdit__select_dir")
        self.lineEdit__select_dir.setGeometry(QRect(40, 20, 108, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 424, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"image", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\ub77c\uc9c4 \ud30c\uc77c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uaecd\ub370\uae30 \ud30c\uc77c (\uc6a9\ub7c9x)", None))
        self.toolButton__select_dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

