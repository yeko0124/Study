
import sys
import time
import shutil
import pathlib
import threading

from PySide2 import QtWidgets, QtCore

import cpy_ui

__import__('importlib').reload(cpy_ui)


# for emittin class
class MultipleData:
    def __init__(self, data: dict, is_copied: bool):
        self.data = data
        self.is_copied = is_copied


# QtCore.QObject클래스는 Qt의 가장 최상위 베이스 클래스
class Signals(QtCore.QObject):  # 상속을 받아야만 connect method를 쓸수가 있음
    # for updating progress bar UI
    sig_update = QtCore.Signal(int)
    # copy information
    # src_file: /home/rapa/aa.txt
    # dst_file: /home/rapa/workspace/bb.txt
    # is_exists: boolean
    sig_info = QtCore.Signal(MultipleData)

    # QtCore.Signal([])
    # -> list도 emit으로 전달이 되기는 함.

##########################################################

# QThread를 상속을 받아야 threading이 가능함. 안쓰면 UI가 멈춰버림(벽돌현상)
# 메인 스레드와 분리시켜서 벽돌현상이 되지 않고 진행이 될 수 있도록 하기 위함임
# -> UI를 자유롭게 사용하고 싶으면 thread를 사용해야 함
# 쓰면 run method를 꼭 사용해서, 작업할 것을 넣어주어야 함

# 공유 객체를 사용하면 문제 발생되는 코드다. 여러 객체를 한번에 할당하려고 하다보면 문제가 생기게 된다.


class WorkThread(QtCore.QThread):
    def __init__(self, srcdir: pathlib.Path, dstdir: pathlib.Path):
        super().__init__()
        self.signals = Signals()  # 따로 만들었던 클래스 함수를 객체로 받는 중
        self.__srcdir = srcdir  # 파일이 있는 곳
        self.__dstdir = dstdir  # copy를 할 곳
        self.is_stop = False

    def set_stop_attr(self, flag):
        self.is_stop = flag

# 왼쪽에 동그라미는 override가 되었다는 것을 의미함
    def run(self):
        # 파일 복사가 이루어 짐

        # source 디렉토리의 모든 파일들
        filelst = list(self.__srcdir.glob('*'))

        # 프로그레스(progress)를 위한 변수 -> (0~1-normalize- 숫자를 만들기 위함)
        totalcnt = len(filelst)  # 다 되면 100%가 되어야 되기 떄문에, 파일들의 개수를 미리 파악하는 것임.

        for i, f in enumerate(filelst):  # i: index  f: filepath
            # 0~1 까지의 숫자를 곱하기 100으로 해서 최종적으로 0~100이 될 수 있음
            ratio = int((i / (totalcnt-1)) * 100)  # 즉, 위에서 normalize시킨 후에 100을 곱하면 되는 것임
            dst_fpath = self.__dstdir / f.name  # f가 filepath이기 떄문에 f.name을 하면 파일명만 나옴

            info = {'src_path': f.as_posix(),
                    'dst_path': dst_fpath.as_posix()}

            multi = MultipleData(info, False)

            # 목적지 디렉토리(복사받을 경로)에 파일이 있으면 emit을 발생시킨 후, 건너뜀
            if dst_fpath.exists():
                self.signals.sig_info.emit(multi)  # multi라는 임의로 만든, 복합 데이터를 넣는 것임
                continue
            else:
                # is_copied : 복사가 정말 이루어졌는지에 대한 확인
                multi.is_copied = True
                try:
                    shutil.copy2(f.as_posix(), dst_fpath.as_posix())
                except Exception:
                    multi.is_copied = False
                self.signals.sig_info.emit(multi)

            # for progress /  프로세스를 위한 발생 시그널
            self.signals.sig_update.emit(ratio)  # int형으로 emit. ui업데이트를 위한 것임

            time.sleep(0.2)

            # 복사 진행 중 멈춤을 위한 코드
            if self.is_stop:
                break


class CopyUI(QtWidgets.QWidget, cpy_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.textEdit.setReadOnly(True)

        srcdir = pathlib.Path('/data/_test_src')
        dstdir = pathlib.Path('/home/rapa/workspace/ddd')

        self.work_thread = WorkThread(srcdir, dstdir)

        # 부모 프로세스가 종료되면 자식 스레드 함께 종료  / 유텍스 ?
        # 특별한 상황이 아닌 이상 항상 setDaemon을 True로 켜놓는 것이 좋음
        # 여기서 부모 프로세스는 gui띄우고 있는 부분
        self.work_thread.setDaemon = True

        # print(dir(self.work_thread))

        self.pushButton__start.clicked.connect(self.slot_start)
        self.pushButton__stop.clicked.connect(self.slot_stop)
        self.work_thread.signals.sig_update.connect(self.slot_update_progress)
        self.work_thread.signals.sig_info.connect(self.slot_info)

        # self.progressBar.setValue(20)

    def slot_start(self):
        # threading 작업이 진행중이지 않으면
        # run method부분을 실행하라고 하는 거임
        if not self.work_thread.isRunning():
            self.work_thread.start()

###################################################################
    # TODO : 재개는 다시 나중에
        # # threading 작업이 작업중이면,
        # else:
        #     # 그런데 멈춰있으면 (paused status)
        #     if self.work_thread.is_stop:
        #         # 다시 start 버튼이 눌리면 재개하라는 시그널
        #         self.textEdit.append('멈춤')  # self.work_thread.start()를 해버리면 0부터 초기화되서 다시 시작
####################################################################

    @QtCore.Slot(MultipleData)
    def slot_info(self, info: MultipleData):
        if not info.is_copied:
            self.textEdit.append(f'복사되지 않은 파일: {info.data.get("src_path")}')
            self.textEdit.append('-' * 30)
        else:
            self.textEdit.append(
                f'{info.data.get("src_path")} -> {info.data.get("dst_path")}')

    @QtCore.Slot(int)
    def slot_update_progress(self, val):
        self.progressBar.setValue(val)


    def slot_stop(self):
        if self.work_thread.isRunning():
            self.work_thread.set_stop_attr(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cpy = CopyUI()
    cpy.show()
    sys.exit(app.exec_())
