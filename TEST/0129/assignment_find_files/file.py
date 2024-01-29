import re
import sys

from PySide2 import QtGui, QtCore, QtWidgets

import importlib

import file_ui
importlib.reload(file_ui)


class LostFiles(QtWidgets.QWidget, file_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LostFiles, self).__init__(parent)

        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    lof = LostFiles()
    lof.show()
    sys.exit(app.exec_())
