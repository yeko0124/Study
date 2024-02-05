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
from resource.ui import change_keyword_ui

from PySide2 import QtWidgets, QtGui, QtCore

importlib.reload(change_keyword_ui)

logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] : %(message)s',
    level=logging.DEBUG,
    datefmt='%m/%d/%Y %I:%M:%S %p',
)


class Info:
    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

    @property
    def arguments(self):
        return self.__args

    @arguments.setter
    def arguments(self, args: tuple):
        self.__args = args

    @property
    def keyword(self):
        return self.__kwargs

    @keyword.setter
    def keyword(self, kwargs: dict):
        self.__kwargs = kwargs


class CustomSignal(QtCore.QObject):
    signal_info = QtCore.Signal(Info)  # Info 라는 클래스를 여기서 받음
    # 인포에 대한 키 값을 하나에 대한 모듈로 만들어서 계속 공유도 가능


class WorkThread(QtCore.QThread):
    def __init__(self, files, fstr, inst_cf):
        super().__init__()
        self.__custom_sig = CustomSignal()

        self.flst = list(files)
        self.__fstr = fstr
        self.__cf = inst_cf

        self.is_stop = False

    def set_files(self, f):
        self.flst = list(f)

    # run 은 매개변수를 줄수가 없음. 다른 곳에서 초기화(생성자에서)를 시키던지, 다른 메서드를 설정해서 주기적으로 쓰던지 해야함
    def run(self):
        # files = self.__ff.get_files_recursion(self.__parent_dir)
        for i, f in enumerate(self.flst):  # files가 지금 generator라서 한번 쓰면 다음부터 못씀 . 이미 다 빠져서
            assert isinstance(i, findFiles.CheckWord)
            assert isinstance(i, int)
            ratio = int((i /(len(self.flst) - 1)) * 100)
            is_exist = findFiles.CheckWord.is_check_word(
                f.fullpath, self.__fstr)
            ###################
            if not is_exist:
                # self.__custom_sig.signal_info.emit()
                continue

            is_suc = self.__cf.change_file(f.fullpath)  # fullpath -> 바뀌는 경로

            data = {
                'is_suc': is_suc,
                'ratio': ratio,
                'filepath': f.fullpath.as_posix()
            }
            # if not is_suc:
                # sys.stderr.write(f'{f.fullpath.as_posix()}: ERR!!!')  # stderr: 표준 오류

            self.__custom_sig.signal_info.emit(data)
            # space = ' ' * i.depth
            # print(f'{space}: {i.fullpath} - {i.depth} : {is_exist}')


class ChangeFilesUI(QtWidgets.QMainWindow, change_keyword_ui.Ui_MainWindow__change_keyword):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.__work_thread = WorkThread('', '', '')
        self.__ext_flst = list()

        self.__cf = changeFiles.ChangeFiles('', '')
        self.__ff = findFiles.FindFiles(pathlib.Path(), [])

        # self.__work_thread.start()

        self.toolButton__pdir.clicked.connect(self.slot_pdir)
        self.lineEdit__file_ext.returnPressed.connect(self.slot_ext_flst)
        self.pushButton__start.clicked.connect(self.slot_progressbar)
        self.pushButton__stop.clicked.connect(self.slot_stop_progress)
        # self.__work_thread.update_sig.connect(self.slot_set_progress)
        # self.__work_thread.finished_sig.connect(self.slot_finished_work)

        ########## test code ###########
        self.__test__set_parms()


    def slot_stop_progress(self):
        if self.__work_thread.isRunning():
            self.__work_thread.is_stop = True

    @QtCore.Slot(bool)
    def slot_finished_work(self, flag):
        if self.__work_thread.isFinished():
        # if flag:
            # self.__work_thread.stop()
            self.textEdit__log.append('finided work')
            logging.debug('debug logging')
        else:
            pass
            # print('progressing')

    @QtCore.Slot(int)
    def slot_set_progress(self, val):
        self.progressBar.setValue(val)

    def slot_progressbar(self):
        if not self.__work_thread.isRunning():
            # change_str = '#include "PXR2',
            change_str = self.lineEdit__change_str.text()
            # pattern = f'{find_str}(.+)',
            pattern = self.lineEdit__find_pattern.text()
            parent_dir = pathlib.Path(self.lineEdit__pdir.text()),
            ext_pattern = self.slot_ext_flst()

            self.__cf.pattern = pattern
            self.__cf.change_str = change_str
            self.__ff.parent_dir = parent_dir
            self.__ff.pattern = ext_pattern

            files = self.__ff.get_files_recursion(parent_dir)

            self.__work_thread.set_files(files)
            # self.__work_thread.fstr =

        #     dd = (list(files))
        #     print(dd)
        #     print(dd[0].fullpath)
        # #
        #     self.progressBar.setValue(0)
        #     self.__work_thread.start()
        #     # for i in range(0, 101):
        #     #     time.sleep(0.5)
        #     #     self.progressBar.setValue(i)
        # else:
        #     self.textEdit__log.append('이미 실행중...')
        #     logging.debug('run... logging')

    def slot_pdir(self):
        dpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, caption='asdd', dir='/data', )
        if not len(dpath):
            return
        dpath = pathlib.Path(dpath)
        self.lineEdit__pdir.setText(dpath.as_posix())

    def slot_ext_flst(self):
        text = self.lineEdit__file_ext.text()
        if not len(text):
            self.__ext_flst = list()
            return
        self.__ext_flst = list(map(lambda x: x.strip(), text.split()))
        return self.__ext_flst

    def __test__set_parms(self):
        self.lineEdit__pdir.setText('/home/rapa/workspace/data/usd/usdUI')
        self.lineEdit__file_ext.setText('.cpp .h')
        self.lineEdit__change_str.setText('#include "PXR2')
        self.lineEdit__find_pattern.setText('#include "pxr(.+)')

# class Main:
#     def __init__(
#             self,
#             change_str: str, pattern: str,
#             parent_dir: pathlib.Path, ext_pattern: list):
#
#         self.__parent_dir = parent_dir
#
#     def change_contents(self, fstr: str):
#         files = self.__ff.get_files_recursion(self.__parent_dir)
#         for i in files:
#             assert isinstance(i, findFiles.CheckWord)
#             is_exist = findFiles.CheckWord.is_check_word(
#                 i.fullpath, fstr)
#             if not is_exist:
#                 continue
#             is_suc = self.__cf.change_file(i.fullpath)
#             if not is_suc:
#                 sys.stderr.write(f'{i.fullpath.as_posix()}: 에러 발생!')


if __name__ == '__main__':
    # main.change_contents(find_str)
    app = QtWidgets.QApplication(sys.argv)
    ui = ChangeFilesUI()
    ui.show()
    sys.exit(app.exec_())


