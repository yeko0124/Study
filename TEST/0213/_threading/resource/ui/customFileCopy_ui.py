# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customFileCopy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow__filecopy(object):
    def setupUi(self, MainWindow__filecopy):
        if not MainWindow__filecopy.objectName():
            MainWindow__filecopy.setObjectName(u"MainWindow__filecopy")
        MainWindow__filecopy.resize(494, 367)
        self.centralwidget = QWidget(MainWindow__filecopy)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_6 = QHBoxLayout(self.page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(self.page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit__srcdir = QLineEdit(self.page)
        self.lineEdit__srcdir.setObjectName(u"lineEdit__srcdir")

        self.horizontalLayout.addWidget(self.lineEdit__srcdir)

        self.toolButton__srcdir = QToolButton(self.page)
        self.toolButton__srcdir.setObjectName(u"toolButton__srcdir")

        self.horizontalLayout.addWidget(self.toolButton__srcdir)

        self.lineEdit__targetdir = QLineEdit(self.page)
        self.lineEdit__targetdir.setObjectName(u"lineEdit__targetdir")

        self.horizontalLayout.addWidget(self.lineEdit__targetdir)

        self.toolButton__targetdir = QToolButton(self.page)
        self.toolButton__targetdir.setObjectName(u"toolButton__targetdir")

        self.horizontalLayout.addWidget(self.toolButton__targetdir)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton__start = QPushButton(self.page)
        self.pushButton__start.setObjectName(u"pushButton__start")

        self.horizontalLayout_2.addWidget(self.pushButton__start)

        self.pushButton__pause = QPushButton(self.page)
        self.pushButton__pause.setObjectName(u"pushButton__pause")

        self.horizontalLayout_2.addWidget(self.pushButton__pause)

        self.pushButton__stop = QPushButton(self.page)
        self.pushButton__stop.setObjectName(u"pushButton__stop")

        self.horizontalLayout_2.addWidget(self.pushButton__stop)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textBrowser__debug = QTextBrowser(self.page)
        self.textBrowser__debug.setObjectName(u"textBrowser__debug")

        self.verticalLayout.addWidget(self.textBrowser__debug)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.tabWidget__filecopy = QTabWidget(self.page)
        self.tabWidget__filecopy.setObjectName(u"tabWidget__filecopy")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.tabWidget__filecopy.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.tabWidget__filecopy.addTab(self.tab_2, "")

        self.horizontalLayout_4.addWidget(self.tabWidget__filecopy)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_7 = QHBoxLayout(self.page_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(16)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.tableView = QTableView(self.page_2)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_5.addWidget(self.stackedWidget)

        MainWindow__filecopy.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow__filecopy)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 494, 20))
        MainWindow__filecopy.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow__filecopy)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow__filecopy.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow__filecopy)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget__filecopy.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow__filecopy)
    # setupUi

    def retranslateUi(self, MainWindow__filecopy):
        MainWindow__filecopy.setWindowTitle(QCoreApplication.translate("MainWindow__filecopy", u"Custom File Copy", None))
        self.toolButton__srcdir.setText(QCoreApplication.translate("MainWindow__filecopy", u"...", None))
        self.toolButton__targetdir.setText(QCoreApplication.translate("MainWindow__filecopy", u"...", None))
        self.pushButton__start.setText(QCoreApplication.translate("MainWindow__filecopy", u"Start", None))
        self.pushButton__pause.setText(QCoreApplication.translate("MainWindow__filecopy", u"Pause", None))
        self.pushButton__stop.setText(QCoreApplication.translate("MainWindow__filecopy", u"Stop", None))
        self.tabWidget__filecopy.setTabText(self.tabWidget__filecopy.indexOf(self.tab), QCoreApplication.translate("MainWindow__filecopy", u"List", None))
        self.tabWidget__filecopy.setTabText(self.tabWidget__filecopy.indexOf(self.tab_2), QCoreApplication.translate("MainWindow__filecopy", u"Table", None))
        self.label.setText(QCoreApplication.translate("MainWindow__filecopy", u"Database Info", None))
    # retranslateUi

