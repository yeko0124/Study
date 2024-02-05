#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.04
# modified date : 2024.02.04
# description   :

import sys
import time
# import threading
import pathlib
import importlib
import logging

from lib import changeFiles, findFiles

from lib import changeFiles, findFiles
from resource.ui import change_keyword_ui

from PySide2 import QtWidgets, QtGui, QtCore
# QtCore.QThread 도 있음 import threading 해도 되고.
# 하는 이유는, progressbar를 진행하면, 아예 안움직임

importlib.reload(change_keyword_ui)

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
# logger.setLevel(logging.DEBUG)
logger.warning('Protocol problem: %s', 'connection reset', extra=d)
logger.debug('adfadf')


class CustomSignal(QtCore.QObject):  # QObject -> 뭐햇을 때 데이터 넘겨라 시그널을 커스텀할 수 있음
    # progressbar가 인트여서 int 로 받음
    update_signal = QtCore.Signal(int)
    finished_signal = QtCore.Signal(bool)


class WorkThread(QtCore.QThread):
    def __init__(self):
        super().__init__()
        self.__custom_sig = CustomSignal()
        self.update_sig = self.__custom_sig.update_signal
        self.finished_sig = self.__custom_sig.update_signal
        self.is_stop = False

    def run(self):
        idx = 0
        for i in range(0, 101):
            # self.__update_sig.emit(i) # emit -> 정보값을 발산한다 뭐 이런 대충 그런뜻
            # self.emit(self.__update_sig, i)
            self.update_sig.emit(i)
            time.sleep(0.1)
            # print(i)
            idx += 1
            if self.is_stop:
                break
            else:

        if idx >= 100:
            # self.__is_stop = True
            # if self.__is_stop:
            self.finished_sig.emit(True)


class ChangeFilesUI(QtWidgets.QMainWindow, change_keyword_ui.Ui_MainWindow__change_keyword):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setupUi(self)

        self.__work_thread = WorkThread()
        self.__ext_flst = list()  # extension 보관하는 곳

        # self.__work_thread.start()

        self.toolButton__pdr.clicked.connect(self.slot_pdir)
        self.lineEdit__ext.returnPressed.connect(self.slot_ext_flst)

        self.pushButton__start.clicked.connect(self.slot_progressbar)
        self.pushButton__stop.clicked.connect(self.slot_stop_progress)

        self.__work_thread.update_sig.connect(self.slot_set_progress)
        self.__work_thread.finished_sig.connect(self.slot_finished_work)

    def slot_stop_progress(self):
        if self.__work_thread.isRunning():
            self.__work_thread.is_stop = True

    @QtCore.Slot(bool)
    def slot_finished_work(self, flag):
        if self.__work_thread.isFinished():
            # self.__work_thread.
            print('finished work')
        else:
            pass
            # print('progressing')

    @QtCore.Slot(int)
    def slot_set_progress(self, val):
        self.progressBar_progress.setValue(val)

    # def slot_pp(self, val):
    #     print(val)

    def slot_progressbar(self):
        if not self.__work_thread.isRunning():
            self.progressBar_progress.setValue(0)
            self.__work_thread.start()
            # for i in range(0, 101):
            #     time.sleep(0.5)
            #     self.progressBar_progress.setValue(i)
        else:
            print('실행중')
            # logging.debug()

    def slot_pdir(self):
        dpath = QtWidgets.QFileDialog.getExistingDirectory(
            self,
        )
        if not len(dpath):
            return
        dpath = pathlib.Path(dpath)
        self.lineEdit__pdr.setText(dpath.as_posix())

    @QtCore.Slot(str)
    def slot_ext_flst(self):
        text = self.lineEdit__ext.text()
        if not len(text):
            self.__ext_flst = list()
            return
        self.__ext_flst = list(map(lambda x: x.strip(), text.split()))
        print(self.__ext_flst)


class Main:
    def __init__(
            self,
            change_str: str, pattern: str,
            parent_dir: pathlib.Path, ext_pattern: list):
        self.__cf = changeFiles.ChangeFiles(change_str, pattern)
        self.__ff = findFiles.FindFiles(parent_dir, ext_pattern)
        self.__parent_dir = parent_dir

    def change_contents(self, fstr: str):
        files = self.__ff.get_files_recursion(self.__parent_dir)
        for i in files:
            assert isinstance(i, findFiles.CheckWord)
            is_exist = findFiles.CheckWord.is_check_word(
                i.fullpath, fstr)
            if not is_exist:
                continue
            is_suc = self.__cf.change_file(i.fullpath)
            if not is_suc:
                sys.stderr.write(f'{i.fullpath.as_posix()}: 에러 발생!')


if __name__ == '__main__':
    find_str = '#include "pxr'
    main = Main(
        change_str='#include "PXR2',
        pattern=f'{find_str}(.+)',
        parent_dir=pathlib.Path('/home/rapa/workspace/usd/usdUI'),
        ext_pattern=['.cpp', '.h']
    )

    # main.change_contents(find_str)

    app = QtWidgets.QApplication(sys.argv)
    ui = ChangeFilesUI()
    ui.show()
    sys.exit(app.exec_())
