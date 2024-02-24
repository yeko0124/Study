#!/usr/bin/env python
# encoding=utf-8

# author        : yeeun ko
# create date   : 2024.02.24
# modified date : 2024.02.24
# description   :

import time
import uuid
from PySide2 import QtCore, QtGui, QtWidgets


class Signals(QtCore.QObject):
    progress = QtCore.Signal(str, int)
    started = QtCore.Signal(bool)
    finished = QtCore.Signal(bool)


class WorkerThread(QtCore.QRunnable):
    def __init__(self):
        super().__init__()
        self.w_id = uuid.uuid4().hex
        # self.is_more = False   # thread개수가 한개 이상이니?
        self.signals = Signals()

    def run(self):
        self.signals.started.emit(True)
        num = 0
        while num <= 100:
            self.signals.progress.emit(self.w_id, num)
            num += 1
            time.sleep(0.2)
        self.signals.finished.emit(True)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        w = QtWidgets.QWidget()

        # variables
        self.__threads = list()
        self.th_dict = dict()
        self.__cnt = 0

        self.progress = QtWidgets.QProgressBar()
        btn_start = QtWidgets.QPushButton('start')
        btn_stop = QtWidgets.QPushButton('stop')

        hbox_btns = QtWidgets.QHBoxLayout()
        hbox_btns.addWidget(btn_start)
        hbox_btns.addWidget(btn_stop)

        vbox_prog = QtWidgets.QVBoxLayout()
        vbox_prog.addWidget(self.progress)
        vbox_prog.addLayout(hbox_btns)

        w.setLayout(vbox_prog)
        self.setCentralWidget(w)

        self.threadpool = QtCore.QThreadPool()
        print('maximum threads: ', self.threadpool.maxThreadCount())

        btn_start.pressed.connect(self.start_thread)

    def start_thread(self):

        thread = WorkerThread()
        thread.signals.started.connect(self.slot_started)
        thread.signals.finished.connect(self.slot_finished)
        thread.signals.progress.connect(self.update_progress)

        """
        # 개수가 줄어들면 signal을 줘야하나.. 
        # 아니면, id를 signal로 보내서 id에 맞는 thread가 끝이 나면 
        # 다음 thread(list에서 다음 거를 호출하는거지) 를 시작시키는거쥐
        """

        self.__threads.append(thread)
        self.threadpool.start(thread)
        self.__cnt = self.threadpool.activeThreadCount()

    def update_progress(self, w_id, val):
        self.th_dict[w_id] = val
        num = 0
        print(self.th_dict.items())
        for i, j in self.th_dict.items():
            num += j
        print(self.th_dict)

        ratio = num / self.__cnt
        self.progress.setValue(ratio)

        # id를 획득했다!~!
        print(ratio)
        # self.progress.setValue(val)

    def slot_started(self):
        print('start thread')

    def slot_finished(self):
        print('finished thread')
        # if len(self.__threads) > 0:
        # else:
        #
        # # self.id += 1  // id랑 count len는 결국 같은 값
        #     print('생성:', self.__threads)

        # len(self.__threads) = thread 개수
        # thread val / thread 개수
        # for idx, th in enumerate(self.__threads):
        #     print(idx, th)

        ########################NONONONONONONO
        # for i in range(len(self.__threads)):
        #     th = self.__threads[len(self.__threads)-1]
        #     if self.threadpool.activeThreadCount() == 0:
        #         # flag = False
        #         print('activated', self.threadpool.activeThreadCount()+1)
        #         # thread.signals.th.connect(self.slot_multh)
        #         # thread.signals.th.connect(lambda: self.slot_multh(flag))
        #         self.threadpool.start(th)
        #     elif self.threadpool.activeThreadCount() > 0:
        #         print('wait')
                ##############################################
                # 어차피 새로운 thread가 만들어질 때마다 for 문은 돌게되어있고,
                # 두번째 thread부터는 계속 wait만 나올거다(len가 0 이상이니까)
                # 그렇다면, while 문으로 해야하는건가?

        # True? 뭐가 True인데? 삽질하는거같아도 일단 생각..
        # len가 남아있는 동안은 True
        ################################## 얘도 아님 ###########################333
        # while len(self.__threads):
        #     th = self.__threads[len(self.__threads) - 1]
        #     if self.threadpool.activeThreadCount() == 0:
        #         print('activated', self.threadpool.activeThreadCount() + 1)
        #         self.threadpool.start(th)
        #     elif self.threadpool.activeThreadCount() > 0:
        #         print('wait')
####################################################

    # def slot_multh(self, flag):
    #     if flag:
    #         print('wait thread')
    #     else:
    #         print('gogo')

        # 음 ,,, emit을 기다렷다가 해야하나
        # thread.signals.progress.connect(self.update_progress)
        # print(self.__threads)

    # def set_thread(self):
    #     for i in range(self.__cnt):
    #         w_id = uuid.uuid4().hex
    #         self.__thread[w_id] = 0
    #     print(self.__threads)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()