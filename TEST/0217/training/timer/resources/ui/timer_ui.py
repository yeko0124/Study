# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from resources.rc import icons_rc
from resources.rc import images_rc

class Ui_Form__timer(object):
    def setupUi(self, Form__timer):
        if not Form__timer.objectName():
            Form__timer.setObjectName(u"Form__timer")
        Form__timer.resize(589, 410)
        icon = QIcon()
        icon.addFile(u":/icons/icons/timer-play.png", QSize(), QIcon.Normal, QIcon.Off)
        Form__timer.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Form__timer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form__timer)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lcdNumber__remaining = QLCDNumber(Form__timer)
        self.lcdNumber__remaining.setObjectName(u"lcdNumber__remaining")
        self.lcdNumber__remaining.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout.addWidget(self.lcdNumber__remaining)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar__remaining = QProgressBar(Form__timer)
        self.progressBar__remaining.setObjectName(u"progressBar__remaining")
        self.progressBar__remaining.setValue(0)

        self.verticalLayout.addWidget(self.progressBar__remaining)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form__timer)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/clock-check-outline.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.timeEdit__timer = QTimeEdit(Form__timer)
        self.timeEdit__timer.setObjectName(u"timeEdit__timer")
        self.timeEdit__timer.setCurrentSection(QDateTimeEdit.HourSection)

        self.horizontalLayout_3.addWidget(self.timeEdit__timer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listWidget__command = QListWidget(Form__timer)
        self.listWidget__command.setObjectName(u"listWidget__command")

        self.horizontalLayout_4.addWidget(self.listWidget__command)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton__add_item = QPushButton(Form__timer)
        self.pushButton__add_item.setObjectName(u"pushButton__add_item")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton__add_item.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton__add_item)

        self.pushButton__del_item = QPushButton(Form__timer)
        self.pushButton__del_item.setObjectName(u"pushButton__del_item")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton__del_item.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton__del_item)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton__start = QPushButton(Form__timer)
        self.pushButton__start.setObjectName(u"pushButton__start")
        self.pushButton__start.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton__start)

        self.pushButton__stop = QPushButton(Form__timer)
        self.pushButton__stop.setObjectName(u"pushButton__stop")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton__stop.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.pushButton__stop)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form__timer)

        QMetaObject.connectSlotsByName(Form__timer)
    # setupUi

    def retranslateUi(self, Form__timer):
        Form__timer.setWindowTitle(QCoreApplication.translate("Form__timer", u"Timer", None))
        self.label.setText(QCoreApplication.translate("Form__timer", u"\ub0a8\uc740 \uc2dc\uac04", None))
        self.label_2.setText("")
        self.timeEdit__timer.setDisplayFormat(QCoreApplication.translate("Form__timer", u"hh:mm:ss", None))
        self.pushButton__add_item.setText(QCoreApplication.translate("Form__timer", u"\ucd94\uac00", None))
        self.pushButton__del_item.setText(QCoreApplication.translate("Form__timer", u"\uc81c\uac70", None))
        self.pushButton__start.setText(QCoreApplication.translate("Form__timer", u"\uc2dc\uc791", None))
        self.pushButton__stop.setText(QCoreApplication.translate("Form__timer", u"\uc815\uc9c0", None))
    # retranslateUi

