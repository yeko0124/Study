import re
import pyseq
import shutil
import pathlib
# TODO directory클릭해서 연결해서 나오게하는 것,
#  directory를 검색해서 시퀀스 뭉탱이 string이 나오도록(shtil)

import sys
import importlib

from PySide2 import QtGui, QtCore, QtWidgets

sys.path.append('/home/rapa/git_workspace/Study/sequence_manager/0130_/resource/rc')

from resource.ui import sequence_manager_ui

importlib.reload(sequence_manager_ui)


class SequenceManager(QtWidgets.QMainWindow, sequence_manager_ui.Ui_MainWindow__seq_mng):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__path = None
        self.setupUi(self)

        self.filename_lst = list()
        self.file_frame_lst = list()
        self.zip_f = list()

        self.signal_func()

    def signal_func(self):
        # self.listWidget__seq_info.addItems(['a', 'b', 'c'])

        # seq info 누르면 아래에 LABEL 바뀌기 -> done
        self.listWidget__seq_info.currentItemChanged.connect(self.select_seq_info)
        # self.listWidget__seq_info.currentItemChanged.connect()
        self.listWidget__missing.customContextMenuRequested.connect(self.custom_context)
        self.listWidget__missing.currentItemChanged.connect(self.changed_missing_item)
        self.toolButton__dirpath.clicked.connect(self.open_dir)

# 우측클릭해서 나오는 정보 : 파일이 몇개있는지 (그러면 missing의 여부를 알 수 있을 것임)
    def select_seq_info(self):
        self.label__seq_info.setText(str(self.zip_f))
        self.missing_frame_length()
        self.error_frame()
        self.listWidget__missing.addItems(self.filename_lst)
        self.listWidget__error.addItems(self.file_frame_lst)

    def custom_context_seq_info(self, pos: QtCore.QPoint):
        index = self.listWidget__seq_info.indexAt(pos)
        if not index.isValid():
            return
        context = QtWidgets.QMenu(self)
        test_menu = QtWidgets.QMenu('Info', self)

        action_test_menu_seq_info = QtWidgets.QAction('files_quantity', self)
        test_menu.addAction(action_test_menu_seq_info)

    def missing_frame_length(self):
        num = str(self.zip_f)
        num = re.sub(r'[^0-9-]+', '', num)
        num = (eval(num)*-1) + 1
        print(num)
        print(range(1, num))
    # 예를 들어서 파일이 없다는 건, 1~100까지의 파일 중에 몇개가 없다는 거니까
    # 있는 파일들을 리스트로 저장해서 길이를 구해도 100이 안될거임.
    # 그러니까, 처음부터 끝까지의 frame 이름만큼 sub해서 숫자를 range로 하고
    # 그 길이의 넘버링을 파일들을 하나씩 비교해서 숫자가 끊어지면 missing된걸로 알려주면 되려나?

    def find_missing_file(self):
        pass

    def error_frame(self):
        pass

    # def changed_label(self, idx: QtWidgets.QListWidgetItem):
    #     self.label__seq_info.setText(str(self.zip_f))

    def open_dir(self):
        files = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            'Open Directory',
            '/data/',
        )
        fpath = pathlib.Path(files)
        self.__path = fpath
        self.lineEdit__dirpath.setText(files)
        self.make_files_list(self.__path)
        return fpath

    def make_files_list(self, fpath: pathlib.Path) -> list:
        comp = re.compile(r'\.(?P<frange>[0-9]{4})\.', re.DOTALL)

        res_exr = fpath.glob('*.exr')
        res_her = fpath.glob('HER*')
        res_mrr = fpath.glob('MRR*')

        for i in res_exr:
            srch = comp.search(i.name)
            # i = i.as_posix()
            self.file_frame_lst.append(int(srch.group('frange')))
            self.filename_lst.append(i.name)
        self.zip_f = pyseq.Sequence(self.filename_lst)
        self.listWidget__seq_info.addItem(str(self.zip_f))
        return self.zip_f

    def compress(self, ):
        pass

    def get_files_path(self):
        pass

    def changed_missing_item(self, idx: QtWidgets.QListWidgetItem):
        print(idx.text())

    def custom_context(self, pos: QtCore.QPoint):
        menu = QtWidgets.QMenu('ddd', self)
        menu.addAction('dadfadf')

        menu.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    seq_mgr = SequenceManager()
    seq_mgr.show()
    sys.exit(app.exec_())
