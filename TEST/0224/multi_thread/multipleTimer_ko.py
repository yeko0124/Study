#!/usr/bin/env python
# encoding=utf-8

# author        : yeeun ko
# create date   : 2024.02.24
# modified date : 2024.02.24
# description   :

import uuid   # id값 >> 절대 겹치지 않는 id 생성 가능 ( uuid1, uuid3, uuid4, uuid5 가 있고 , uuid4가 무작위 생성임)
import pathlib
import functools
from PySide2 import QtCore, QtGui, QtWidgets

from ui import timer_template_ui
from system import library as sys_lib


# 초를 가져오는 method / 명령 실행하는 method >> test를 해보는 것임

class Signals(QtCore.QObject):
    progress = QtCore.Signal(str, int)
    cmd_run = QtCore.Signal(bool, str)


class WorkerThread(QtCore.QThread):
    def __init__(self, w_id):
        super().__init__()
        self.w_id = w_id
        self.is_stop = True
        self.__total_num = 0
        self.signal = Signals()

    def run(self):
        num = 0
        while num <= self.__total_num:
            self.signal.cmd_run.emit(False, self.w_id)
            if self.is_stop:
                break
            try:
                ratio = int((num / self.__total_num) * 100)
            except ZeroDivisionError as err:
                ratio = 0
            self.signal.progress.emit(self.w_id, ratio)
            num += 1
            self.sleep(1)
        self.signal.cmd_run.emit(True, self.w_id)

    def run_start(self, total_num):
        self.__total_num = total_num
        self.is_stop = False
        self.start()

    def stop(self):
        self.is_stop = True


class MultipleTimer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        w = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()

        # 몇개를 w에 탑재할 것인가
        self.__cnt_widgets = 3
        # set_widgets에 있는 WIDGET을 참조하기 위한
        self.__widget_data = dict()
        self.__thread_data = dict()

        self.set_widgets()
        self.set_threads()   # 아이디 별로 thread를 넣는 함수

        # print(self.__thread_data)

        w.setLayout(self.vbox)
        self.setCentralWidget(w)

    def set_widgets(self):
        for i in range(self.__cnt_widgets):
            w_id = uuid.uuid4().hex
            widget = QtWidgets.QWidget()
            w = timer_template_ui.Ui_Form()
            w.setupUi(widget)
            self.vbox.addWidget(widget)

            # lambda / partial 차이점 >> lambda는 함수가 끝나고 나서 숫자가 생성되는 것이고,
            # partial는 실시간으로 함수가 돌 때마다즉각적으로 생성되는 것

            # lambda 때문에 어떤 것을 눌러도 다 똑같은 id가 나와버림 (import functools를 해야함)
            # w.pushButton__start.pressed.connect(lambda: self.slot_btn_start(w_id))

            # lambda대신 쓸 수 있는 형식 (functools) >> 함수와 매개변수를 변수로 받고 있음
            w.pushButton__start.pressed.connect(functools.partial(self.slot_btn_start, w_id))
            w.pushButton__stop.pressed.connect(functools.partial(self.slot_btn_stop, w_id))

            self.__widget_data[w_id] = w

    def set_threads(self):
        for w_id, widget in self.__widget_data.items():
            th = WorkerThread(w_id)
            th.signal.progress.connect(functools.partial(self.update_progress))
            th.signal.cmd_run.connect(functools.partial(self.get_bool))
            self.__thread_data[w_id] = th

    @QtCore.Slot(str, int)
    def update_progress(self, w_id, val):
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        w.progressBar.setValue(val)

    def slot_btn_stop(self, w_id):
        th: WorkerThread = self.__thread_data[w_id]
        th.stop()
        # print(w_id)

    # flag로 bool값을 받아서, thread run 끝날 떄가 cmd run = true / thread running 일 때 cmd run = False
    @QtCore.Slot(bool)
    def get_bool(self, flag, w_id):
        # th: WorkerThread = self.__thread_data[w_id]
        # w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        # self.run_commands(flag, w_id)
        # if th.isRunning():
        if flag:
            w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
            cmd = w.lineEdit__cmd.text()
            sys_lib.System.open_file_using_thread(pathlib.Path(cmd), None, False)

    def slot_btn_start(self, w_id):
        th: WorkerThread = self.__thread_data[w_id]
        # widget당 타이머 정보를 만들어야 함
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        # start
        th.run_start(MultipleTimer.qtime2secs(w.timeEdit__timer.time()))

    def run_commands(self, flag: bool, w_id: str):
        if flag:
            w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
            cmd = w.lineEdit__cmd.text()
            sys_lib.System.open_file_using_thread(pathlib.Path(cmd), None, False)


    def time2sec(self):
        w: timer_template_ui.Ui_Form = self.__widget_data['0']
        return w.timeEdit__timer.time()

    @staticmethod
    def qtime2secs(qtime) -> int:
        h, m, s = qtime.hour(), qtime.minute(), qtime.second()
        total_sec = h * 3600 + m * 60 + s
        return total_sec

    @staticmethod
    def secs2qtime(secs: int) -> QtCore.QTime:
        h, m = divmod(secs, 3600)
        m = m // 60
        s = secs % 60
        return QtCore.QTime(h, m, s)

    # 숫자든 문자든 다 계산이 되는 method
    @staticmethod
    def addition(a, b):
        return a + b


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mt = MultipleTimer()
    mt.show()
    app.exec_()