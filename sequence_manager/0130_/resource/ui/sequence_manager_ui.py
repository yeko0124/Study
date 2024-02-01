# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sequence_manager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import icons_rc

class Ui_MainWindow__seq_mng(object):
    def setupUi(self, MainWindow__seq_mng):
        if not MainWindow__seq_mng.objectName():
            MainWindow__seq_mng.setObjectName(u"MainWindow__seq_mng")
        MainWindow__seq_mng.resize(598, 461)
        self.actionexit = QAction(MainWindow__seq_mng)
        self.actionexit.setObjectName(u"actionexit")
        self.actionabout = QAction(MainWindow__seq_mng)
        self.actionabout.setObjectName(u"actionabout")
        self.centralwidget = QWidget(MainWindow__seq_mng)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit__dirpath = QLineEdit(self.centralwidget)
        self.lineEdit__dirpath.setObjectName(u"lineEdit__dirpath")

        self.horizontalLayout.addWidget(self.lineEdit__dirpath)

        self.toolButton__dirpath = QToolButton(self.centralwidget)
        self.toolButton__dirpath.setObjectName(u"toolButton__dirpath")

        self.horizontalLayout.addWidget(self.toolButton__dirpath)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit__work_filepath = QLineEdit(self.centralwidget)
        self.lineEdit__work_filepath.setObjectName(u"lineEdit__work_filepath")
        self.lineEdit__work_filepath.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit__work_filepath)

        self.toolButton__work_filepath = QToolButton(self.centralwidget)
        self.toolButton__work_filepath.setObjectName(u"toolButton__work_filepath")

        self.horizontalLayout_2.addWidget(self.toolButton__work_filepath)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget__seq_info = QListWidget(self.centralwidget)
        self.listWidget__seq_info.setObjectName(u"listWidget__seq_info")

        self.verticalLayout.addWidget(self.listWidget__seq_info)

        self.label__seq_info = QLabel(self.centralwidget)
        self.label__seq_info.setObjectName(u"label__seq_info")

        self.verticalLayout.addWidget(self.label__seq_info)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.tabWidget__error_frame = QTabWidget(self.centralwidget)
        self.tabWidget__error_frame.setObjectName(u"tabWidget__error_frame")
        self.miss_frame_tab = QWidget()
        self.miss_frame_tab.setObjectName(u"miss_frame_tab")
        self.verticalLayout_2 = QVBoxLayout(self.miss_frame_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget__missing = QListWidget(self.miss_frame_tab)
        self.listWidget__missing.setObjectName(u"listWidget__missing")

        self.verticalLayout_2.addWidget(self.listWidget__missing)

        icon = QIcon()
        icon.addFile(u":/icons/icons/missing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget__error_frame.addTab(self.miss_frame_tab, icon, "")
        self.err_frame_tab = QWidget()
        self.err_frame_tab.setObjectName(u"err_frame_tab")
        self.verticalLayout_3 = QVBoxLayout(self.err_frame_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listWidget__error = QListWidget(self.err_frame_tab)
        self.listWidget__error.setObjectName(u"listWidget__error")

        self.verticalLayout_3.addWidget(self.listWidget__error)

        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/error.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget__error_frame.addTab(self.err_frame_tab, icon1, "")

        self.horizontalLayout_4.addWidget(self.tabWidget__error_frame)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        MainWindow__seq_mng.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow__seq_mng)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 598, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow__seq_mng.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow__seq_mng)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow__seq_mng.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionexit)
        self.menuHelp.addAction(self.actionabout)

        self.retranslateUi(MainWindow__seq_mng)

        self.tabWidget__error_frame.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow__seq_mng)
    # setupUi

    def retranslateUi(self, MainWindow__seq_mng):
        MainWindow__seq_mng.setWindowTitle(QCoreApplication.translate("MainWindow__seq_mng", u"MainWindow", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow__seq_mng", u"exit", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow__seq_mng", u"about", None))
        self.toolButton__dirpath.setText(QCoreApplication.translate("MainWindow__seq_mng", u"Open Dir", None))
        self.toolButton__work_filepath.setText(QCoreApplication.translate("MainWindow__seq_mng", u"Open File", None))
        self.label__seq_info.setText(QCoreApplication.translate("MainWindow__seq_mng", u"...", None))
        self.tabWidget__error_frame.setTabText(self.tabWidget__error_frame.indexOf(self.miss_frame_tab), QCoreApplication.translate("MainWindow__seq_mng", u"Missing Frame", None))
        self.tabWidget__error_frame.setTabText(self.tabWidget__error_frame.indexOf(self.err_frame_tab), QCoreApplication.translate("MainWindow__seq_mng", u"Error Frame", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow__seq_mng", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow__seq_mng", u"Help", None))
    # retranslateUi

