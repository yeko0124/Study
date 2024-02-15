"""
새로 다시 쳐보면서 익히기
+ list widget에 f.name emit으로 추가(signal and thread)
(table은 안함. 형식을 모르겠음)
"""

import sys
import pathlib
import shutil
import time
import importlib
import logging

from PySide2 import QtGui, QtCore, QtWidgets

import resource.ui.customFileCopy_ui as cus_file_cpy

from qt import library as qt_lib
from system import library as sys_lib

importlib.reload(cus_file_cpy)
importlib.reload(qt_lib)
importlib.reload(sys_lib)


class MessageSig:
    message = ''
    is_err = False


class Signals(QtCore.QObject):
    progress_update = QtCore.Signal(int)
    message = QtCore.Signal(MessageSig)
    # list widget 추가!
    list = QtCore.Signal(str)


class UiThread(QtCore.QThread):
    def __init__(self, flst: list, target_dir: str):
        super().__init__()
        self.signals = Signals()

        self.__is_start = False
        self.__is_stop = True
        self.__is_pause = False

        self.all_files = flst
        self.__target_dir = target_dir

        self.__condition = QtCore.QWaitCondition()
        self.__mutex = QtCore.QMutex()

    def set_targetdir(self, val):
        self.__target_dir = val

    def resume(self):
        if self.__is_pause:
            self.__condition.wakeAll()

    @property
    def is_start(self):
        return self.__is_start

    @is_start.setter
    def is_start(self, flag: bool):
        self.__is_start = flag

    @property
    def is_stop(self):
        return self.__is_stop

    @is_stop.setter
    def is_stop(self, flag: bool):
        self.__is_stop = flag

    @property
    def is_pause(self):
        return self.__is_pause

    @is_pause.setter
    def is_pause(self, flag: bool):
        self.__is_pause = flag

    def run(self):
        for i, f in enumerate(self.all_files):
            ratio = int((i / (len(self.all_files) - 1)) * 100)
            dst_file = pathlib.Path(self.__target_dir) / pathlib.Path(f).name
            msg_sig = MessageSig()
            dst_file_name = ''

            if not dst_file.exists():
                shutil.copy(f, dst_file.as_posix())
                dst_file_name += pathlib.Path(f).name
            else:
                msg_sig.message = f'{dst_file.as_posix()} 해당파일 존재함'
                msg_sig.is_err = True

            msg_sig.message = f'[{ratio}% {f} -> {dst_file.as_posix()}'
            msg_sig.is_err = False

            if self.__is_pause:
                self.__condition.wait(self.__mutex)

            if self.__is_stop:
                break

            self.signals.progress_update.emit(ratio)
            self.signals.message.emit(msg_sig)
            # list widget 추가!
            self.signals.list.emit(dst_file_name)


class CustomFileCopy(QtWidgets.QMainWindow, cus_file_cpy.Ui_MainWindow__filecopy):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        self.init_set()

        self.__handler = qt_lib.LogHandler(out_stream=self.textBrowser__debug)
        self.__ui_thread = UiThread([], '')

        self.toolButton__srcdir.clicked.connect(self.slot_source_dir)
        self.toolButton__targetdir.clicked.connect(self.slot_source_dir)

        self.pushButton__start.clicked.connect(self.slot_start)
        self.pushButton__stop.clicked.connect(self.slot_stop)
        self.pushButton__pause.clicked.connect(self.slot_pause)

        self.__ui_thread.signals.progress_update.connect(self.slot_update_progress)
        self.__ui_thread.signals.message.connect(self.slot_print_message)
        # list widget 추가!
        self.__ui_thread.signals.list.connect(self.slot_print_list)

    # list widget 추가!
    @QtCore.Slot(str)
    def slot_print_list(self, val):
        self.listWidget.addItem(val)

    @QtCore.Slot(MessageSig)
    def slot_print_message(self, msg: MessageSig):
        if msg.is_err:
            self.__handler.log_msg(logging.error, msg.message)
        else:
            self.__handler.log_msg(logging.info, msg.message)

    @QtCore.Slot(int)
    def slot_update_progress(self, val):
        self.progressBar.setValue(val)


    def slot_pause(self):
        self.pushButton__pause.setEnabled(False)
        self.pushButton__start.setEnabled(True)
        self.pushButton__stop.setEnabled(True)

        self.__ui_thread.is_pause = True
        self.__ui_thread.is_stop = False

    def slot_stop(self):
        self.pushButton__stop.setEnabled(False)
        self.pushButton__start.setEnabled(True)
        self.pushButton__pause.setEnabled(False)

        self.__ui_thread.is_start = False
        self.__ui_thread.is_stop = True

    def slot_start(self):
        self.pushButton__start.setEnabled(False)
        self.pushButton__pause.setEnabled(True)
        self.pushButton__stop.setEnabled(True)

        if not self.__ui_thread.isRunning():
            self.__ui_thread.is_start = True
            self.__ui_thread.is_stop = False
            self.__ui_thread.is_pause = False

            if not self.is_exists_target_dir():
                self.__handler.log_msg(logging.error, '타겟 디렉토리 설정 플리즈')
                return

            all_files = self.get_all_files()
            self.__ui_thread.all_files = all_files
            self.__ui_thread.set_targetdir(self.lineEdit__targetdir.text())

            if not len(all_files):
                self.__handler.log_msg(logging.error, '파일이 없음')
                return

            self.__ui_thread.start()
            self.__ui_thread.daemon = True

        else:
            if self.__ui_thread.is_pause:
                self.__ui_thread.resume()
                self.__ui_thread.is_pause = False

    def get_all_files(self):
        dpath = self.lineEdit__srcdir.text()
        return list(sys_lib.System.get_files_recursion(dpath, ['*']))

    def is_exists_target_dir(self):
        return (QtCore.QDir(self.lineEdit__targetdir.text()).exists()
                and len(self.lineEdit__targetdir.text()))

    def slot_source_dir(self):
        btn: QtWidgets.QToolButton = self.sender()
        sel_dir: pathlib.Path = qt_lib.QtLibs.dir_dialog('/Users/yeko/Desktop/netflix_TD/self_study/')

        if sel_dir is not None:
            if btn.text() == 'source directory':
                self.lineEdit__srcdir.setText(sel_dir.as_posix())
            else:
                self.lineEdit__targetdir.setText(sel_dir.as_posix())

    def init_set(self):
        self.toolButton__srcdir.setText('source directory')
        self.toolButton__targetdir.setText('target directory')
        self.pushButton__pause.setEnabled(False)
        self.pushButton__stop.setEnabled(False)


if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cf = CustomFileCopy()
    cf.show()
    sys.exit(app.exec_())