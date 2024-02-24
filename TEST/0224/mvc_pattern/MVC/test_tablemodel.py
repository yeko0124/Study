import sys
import datetime

from PySide2 import QtWidgets, QtGui, QtCore

from faker import Faker


class TableModel(QtCore.QAbstractTableModel):
    # QAbstractListModel를 상속받아서 꼭 data를 해줘야 한다
    # 여기는 data만 넘기면 알아서 돌게끔 만들어 준다. for / while 안써도 됌
    def __init__(self, data):
        super().__init__()
        self.__data = data

        self.__header = ['aaa', 'bbb', 'ccc', 'ddd']

    # data를 꼭 override를 해줘야 함 **** data가 중요함.
    def data(self, index, role=...):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            data = self.__data[index.row()][index.column()]
            if isinstance(data, datetime.datetime):
                return f'{data.year}-{data.month}-{data.day}'
            elif not isinstance(data, str):
                return str(data)
            return data

        # ItemDataRole이 중요함. 이게 역할임. view에 보이는 것을 표시하는 역할
            # return self.__data[index.row()][index.column()]
        elif role == QtCore.Qt.DecorationRole:
            ipath = '/data/apple.jpg'
            image = QtGui.QImage(ipath)
            return QtGui.QPixmap.fromImage(image).scaled(
                QtCore.QSize(24, 24), QtCore.Qt.KeepAspectRatio)

    def columnCount(self, parent=...):
        return len(self.__data[0])

    # rowCount만큼 data의 index가 설정되면서 계속 돌아간다
    def rowCount(self, parent=...):
        return len(self.__data)

    def headerData(self, section, orientation, role=...):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.__header[section]
            elif orientation == QtCore.Qt.Vertical:
                return str(section+1)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = QtWidgets.QTableView()
        # self.model = ListModel(list(range(15)))
        self.model = TableModel(
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12]]
        )
        self.view.setModel(self.model)
        self.setCentralWidget(self.view)


# def testfunc(a, b=...):
#     print(a, b)
#     if b == ... :
#         print('no data')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    # testfunc('dd')