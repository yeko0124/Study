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
        self.signals = Signals()
        self.w_id = uuid.uuid4().hex

    def run(self):
        self.signals.started.emit(True)
        num = 0
        total_num = int()
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
        self.thread_cnt = int()

        btn_start.pressed.connect(self.start_thread)

        self.job_dict = dict()

    def start_thread(self):
        thread = WorkerThread()
        thread.signals.started.connect(self.slot_started)
        thread.signals.finished.connect(self.slot_finished)
        thread.signals.progress.connect(self.update_progress)
        self.__threads.append(thread)
        self.threadpool.start(thread)
        self.thread_cnt = self.threadpool.activeThreadCount()
        print(self.__threads)
        print('current thread cnt :', )

    def update_progress(self, key, val):
        self.job_dict[key] = val
        num = 0
        for i, j in self.job_dict.items():
            num += j
        ratio = num/self.thread_cnt
        print('activated :',self.thread_cnt,'\nratio :',ratio)
        self.progress.setValue(ratio)

    def slot_started(self):
        print('start thread')

    def slot_finished(self):
        print('finished thread')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()