# 파일 복사
# 소스 디렉토리
# 타겟 디렉토리
# 복사, 복사 중 정지, 복사 중 일시정지(condition wait)
# 복사 완료된 파일 목록 리스트에 저장(mutex lock)
# SQLite3 DB(복사 완료 리스트를 Database 저장)
# 초기 실행 시, pause stop은 비활성화 상태
    # start 클릭
        # start 비활성화
        # pause 활성화
        # stop 활성화
    # stop 클릭
        # start 활성화
        # pause 비활성화
        # stop 비활성화
    # pause 클릭
        # start 활성화
        # pause 비활성화
        # stop 활성화

import shutil
import sys
import importlib
import pathlib
import typing
import logging
import time


from PySide2 import QtGui, QtCore, QtWidgets

import resource.ui.customFileCopy_ui as cus_file_cpy

# site.addsitedir('/home/rapa/workspace/python/libs')  -> python path로 했기 때문에 site는 필요가 없어짐

from qt import library as qt_lib
from system import library as sys_lib

importlib.reload(cus_file_cpy)
importlib.reload(qt_lib)
importlib.reload(sys_lib)

# 비트 마스트 : 상태 표시 변수들이 많아질 수록 관리하기 힘들어짐
# 메모리도 많이 차지하고,,,, 변수 하나당 int 하나당 4~8byte,,
# 호출 호출 하다보면 메모리가 엄청 커짐 -> 그래서 비트 마스크 같은 경우
# bit mask
# 0000 0000, 0000 0000, 0000 0000, 0000 0000
#  1byte       2byte      3byte      4byte
# 2의 32승까지 저장이 가능 비트만 껐다가 켰다가.
# ex ) 0000 0001 이면 pause고, 0000 0000 이면 pause가 아닌 상태 이런식으로 정해줄 수가 있음
# >> shift bit 연산자를 사용할 줄 알아야 함 / AND(&), OR(|) 연산자도

# 0 0 0 0 -> 0 <start> <stop> <pause>

# 0 1 0 0 -> start
# 0 0 1 0 -> stop
# 0 0 0 1 -> pause
# 0 0 0 0 -> 초기상태


# error message 도 줄 수 있고, info message도 줄 수 있어서 만드는 그런 느낌이랄까
class MessageSig:
    message = ''
    is_err = False


class Signals(QtCore.QObject):
    progress_update = QtCore.Signal(int)
    message = QtCore.Signal(MessageSig)


# progressing 일 때 버튼을 누를 수 있도록 하기 위해서
class UIThread(QtCore.QThread):
    def __init__(self, flst: typing.List[str], targetdir: str):
        super().__init__()
        self.signals = Signals()
        self.all_files = flst
        self.__targetdir = targetdir
        self.__is_stop = True
        self.__is_pause = False

        # 무한루프를 없애고 wait을 걸기 위해서 만든 변수?
        self.__condition = QtCore.QWaitCondition()
        self.__mutex = QtCore.QMutex()

    def set_targetdir(self, val):
        self.__targetdir = val

    @property
    def is_stop(self):
        return self.__is_stop

    @is_stop.setter
    def is_stop(self, flag: bool):
        self.__is_stop = flag

    def resume(self):
        if self.__is_pause:
            self.__condition.wakeAll()

    @property
    def is_pause(self):
        return self.__is_pause

    @is_pause.setter
    def is_pause(self, flag: bool):
        self.__is_pause = flag

    def run(self):
        # /home/rapa/aa -> /home/rapa/target/aa
        for i, f in enumerate(self.all_files):

            ratio = (i / (len(self.all_files) - 1)) * 100
            dst_file = pathlib.Path(self.__targetdir) / pathlib.Path(f).name
            msg_sig = MessageSig()

            if not dst_file.exists():
                shutil.copy(f, dst_file.as_posix())
            else:
                msg_sig.message = f'{dst_file.as_posix()} 해당파일이 없습니다'
                msg_sig.is_err = True

            # try:
            #     shutil.copy2(f, dst_file.as_posix())
            # except shutil.SameFileError:
            #     msg_sig.message = f'{dst_file.as_posix()} 해당 파일이 존재합니다.'
            #     msg_sig.is_err = True
            #     # self.__handler.log_msg(logging.error, f'{dst_file.as_posix()} 해당 파일이 존재합니다.')
            #     continue

            msg_sig.message = f'[{ratio}%]{f} -> {dst_file.as_posix()}'
            msg_sig.is_err = False

            # self.__handler.log_msg(logging.info, f'[{ratio}%]{f} -> {dst_file.as_posix()}')
            # print(ratio)

            # stop
            if self.__is_stop:
                break

            if self.__is_pause:
                self.__condition.wait(self.__mutex)

            self.signals.progress_update.emit(ratio)
            self.signals.message.emit(msg_sig)


class CustomFileCopy(QtWidgets.QMainWindow, cus_file_cpy.Ui_MainWindow__filecopy):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)  # 계속 위에 뜨게 할 수 있는 것  always stay on top

        # 초기 상태
        self.init_set()

        # variables
        self.__handler = qt_lib.LogHandler(out_stream=self.textBrowser__debug)
        self.__ui_thread = UIThread([], '')

        self.toolButton__srcdir.clicked.connect(self.slot_source_dir)
        self.toolButton__targetdir.clicked.connect(self.slot_source_dir)
        self.pushButton__start.clicked.connect(self.slot_start)
        self.pushButton__stop.clicked.connect(self.slot_stop)
        self.pushButton__pause.clicked.connect(self.slot_pause)

        self.__ui_thread.signals.progress_update.connect(self.slot_update_progress)
        self.__ui_thread.signals.message.connect(self.slot_print_message)

    @QtCore.Slot(MessageSig)
    def slot_print_message(self, msg: MessageSig):
        if msg.is_err:
            self.__handler.log_msg(logging.error, msg.message)
        else:
            self.__handler.log_msg(logging.info, msg.message)

    @QtCore.Slot(int)
    def slot_update_progress(self, val):
       self.progressBar.setValue(val)

    # 초기 세팅을 담당하는 함수 method
    def init_set(self):
        self.toolButton__srcdir.setText('source directory')
        self.toolButton__targetdir.setText('target directory')
        self.pushButton__pause.setEnabled(False)
        self.pushButton__stop.setEnabled(False)
        self.pushButton__start.setEnabled(True)
        # TODO 추후에 모든 디렉토리 경로를 설정을 해야만 start가 활성화되도록 해보기
    #     self.is_exist_dirs()
    #     if self.is_exist_source_dir() and not self.is_exist_target_dir():
    #         print(self.is_exist_target_dir(), self.is_exist_source_dir())
    #         self.pushButton__start.setEnabled(True)
    #     else:
    #         self.pushButton__start.setEnabled(False)
    #
    # def is_exist_dirs(self):
    #     if self.is_exist_source_dir() and not self.is_exist_target_dir():
    #         print(self.is_exist_target_dir(), self.is_exist_source_dir())
    #         self.pushButton__start.setEnabled(True)
    #     else:
    #         self.pushButton__start.setEnabled(False)

    def get_all_files(self) -> typing.List[str]:
        dpath = self.lineEdit__srcdir.text()
        return list(sys_lib.System.get_files_recursion(dpath, ['*']))

    def is_exist_target_dir(self):
        return QtCore.QDir(self.lineEdit__targetdir.text()).exists() and len(self.lineEdit__srcdir.text())

    def is_exist_source_dir(self):
        return QtCore.QDir(self.lineEdit__srcdir.text()).exists() and len(self.lineEdit__targetdir.text())

    def slot_start(self):
        self.pushButton__start.setEnabled(False)
        self.pushButton__pause.setEnabled(True)
        self.pushButton__stop.setEnabled(True)

        self.__ui_thread.is_pause = False

        # 이미 무한루프에 빠져서 대기상태이므로 not으로 해줌
        # 스레드가 실행중이지 않으면
        if not self.__ui_thread.isRunning():
            self.__ui_thread.is_start = True
            self.__ui_thread.is_stop = False
            self.__ui_thread.is_pause = False

            if not self.is_exist_target_dir():
                self.__handler.log_msg(logging.error, '타겟 디렉토리 설정을 해야합니다.')
                return

            all_files = self.get_all_files()
            self.__ui_thread.all_files = all_files
            self.__ui_thread.set_targetdir(self.lineEdit__targetdir.text())

            if not len(all_files):
                self.__handler.log_msg(logging.error, '파일이 없습니다.')
                return

            self.__ui_thread.start()
            self.__ui_thread.daemon = True
        else:
            print('실행중')
            self.__ui_thread.thread()


    def slot_stop(self):
        self.pushButton__start.setEnabled(True)
        self.pushButton__pause.setEnabled(False)
        self.pushButton__stop.setEnabled(False)

        # False -> True -> False
        # self.__is_stop ^= True  -> check box할 때 도움이 되는 것! 여기서는 노노
        self.__ui_thread.is_stop = True
        self.__ui_thread.is_start = False

        # if self.__ui_thread.is_pause:
        #     print('강제종료')
        #     self.__ui_thread.terminate()  # terminate -> thread 강제 종료

    def slot_pause(self):
        self.pushButton__start.setEnabled(True)
        self.pushButton__pause.setEnabled(False)
        self.pushButton__stop.setEnabled(True)

        self.__ui_thread.is_pause = True
        self.__ui_thread.is_stop = False

    def slot_source_dir(self):
        btn: QtWidgets.QToolButton = self.sender()
        sel_dir: pathlib.Path = qt_lib.QtLibs.dir_dialog('/home/rapa/workspace/data/usd')
        print(btn.text(), btn)

        # sel_dir = library.QtLibs.dir_dialog('/home/rapa')
        if sel_dir is not None:
            if btn.text() == 'source directory':
                self.lineEdit__srcdir.setText(sel_dir.as_posix())
            else:
                self.lineEdit__targetdir.setText(sel_dir.as_posix())  # pathlib.Path니까 as_posix로 해도 되고 str로 해도 될듯


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cfc = CustomFileCopy()
    cfc.show()
    sys.exit(app.exec_())
