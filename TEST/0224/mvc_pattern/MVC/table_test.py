import sys
import datetime

from PySide2 import QtWidgets, QtGui, QtCore

import mysql.connector as mysql_con

import random

from faker import Faker
from MVC.view import table_view
import time
import functools


def secs2qtime(secs: int) -> tuple:
    h, m = divmod(secs, 3600)
    m = m // 60
    s = secs % 60
    return h, m, s


class CheckRuntime:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        functools.wraps(self.__func)
        res = self.__func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time

        h, m, s = secs2qtime(int(elapsed_time))

        # print(f'<{self.__func.__name__}> elapsed time: [시간: {h}], [분: {m}], [초: {s}]')
        print(f'<{self.__func.__name__}>: {elapsed_time}')
        return res


def CheckRuntime2(func):
    def wrapper(self, data):
        start_time = time.time()
        res = func(self, data)
        end_time = time.time()
        elapsed_time = end_time - start_time

        h, m, s = secs2qtime(int(elapsed_time))

        # print(f'<{func.__name__}> elapsed time: [시간: {h}], [분: {m}], [초: {s}]')
        print(f'<{func.__name__}>: {elapsed_time}')
        return res
    return wrapper


@CheckRuntime
def get_temp_data():
    fake = Faker()

    fetch_all = list()

    for i in range(int(1000000 * 0.05)):
        yyyy = random.choice(list(range(1980, 2000)))
        mm = str(random.choice(list(range(1, 12)))).zfill(2)
        dd = str(random.choice(list(range(1, 28)))).zfill(2)
        date_str = f'{yyyy}-{mm}-{dd}'
        date_str = datetime.date.fromisoformat(date_str)

        fetch_all.append(
            (i, fake.name(), fake.address(), fake.ipv4_private(), date_str)
        )

    return fetch_all + fetch_all


con = mysql_con.connect(
    host='127.0.0.1', user='root', passwd='', database='dummy_db'
)
cur = con.cursor()


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.__data = data
        self.__header = ['id', 'name', 'addr', 'ip_addr', 'birth']

    def data(self, index, role=...):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            data = self.__data[index.row()][index.column()]

            if isinstance(data, datetime.datetime):
                return f'{data.year}-{data.month}-{data.day}'
            elif not isinstance(data, str):
                return str(data)
            return data

        elif role == QtCore.Qt.DecorationRole:
            ipath = '/data/apple.jpg'
            image = QtGui.QImage(ipath)
            return QtGui.QPixmap.fromImage(image).scaled(
                QtCore.QSize(24, 24), QtCore.Qt.KeepAspectRatio)

    def rowCount(self, parent=...):
        return len(self.__data)

    def columnCount(self, parent = ...):
        return len(self.__data[0])

    def headerData(self, section, orientation, role=...):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.__header[section]
            elif orientation == QtCore.Qt.Vertical:
                return str(int(section) + 1)


class ControllerMVC(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = QtWidgets.QTableView()
        self.model = TableModel(self.get_data())

        self.set_data_from_db()

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.view)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vlayout)

        self.setCentralWidget(central_widget)

    def set_data_from_db(self):
        self.view.setModel(self.model)
        # st = time.time()
        # self.view = QtWidgets.QTableView()
        # self.model = TableModel(self.get_data())
        # self.view.setModel(self.model)
        # et = time.time()
        # print('model: ', et - st)

    def get_data(self):
        query = """
        SELECT * FROM user_info;
        """

        # cur.execute(query)
        # data = cur.fetchall()

        data = get_temp_data()

        return data


class ControllerWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.__table_widget = QtWidgets.QTableWidget()
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.__table_widget)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vlayout)

        self.setCentralWidget(central_widget)

        self.set_data(self.get_data())

        # self.get_decribe()

    def get_decribe(self):
        query = """
        DESCRIBE user_info;
        """

        cur.execute(query)
        data = cur.fetchone()

        print(data)

    @CheckRuntime2
    def set_data(self, data):
        '''
        [
            (0, "name", "address", "ip_address", datetime.date('1992', '5', '12'),
            (1, "name", "address", "ip_address", datetime.date('1992', '5', '12'),
            (2, "name", "address", "ip_address", datetime.date('1992', '5', '12'),
            ...
        ]
        '''
        self.__table_widget.setRowCount(len(data))
        self.__table_widget.setColumnCount(len(data[0]))

        for row, i in enumerate(data):
            for col in range(5):
                ipath = '/home/rapa/workspace/python/training/alarm.png'
                image = QtGui.QImage(ipath)
                pixmap = QtGui.QIcon(QtGui.QPixmap.fromImage(image).scaled(
                    QtCore.QSize(24, 24), QtCore.Qt.KeepAspectRatio))

                if col == 4:
                    date: datetime.date = i[col]
                    date = f'{date.year}-{date.month}-{date.day}'
                    item = QtWidgets.QTableWidgetItem(pixmap, date)
                elif col == 0:
                    item = QtWidgets.QTableWidgetItem(pixmap, str(i[col]))
                else:
                    item = QtWidgets.QTableWidgetItem(pixmap, i[col])
                self.__table_widget.setItem(row, col, item)

    def get_data(self):
        query = """
        SELECT * FROM user_info;
        """

        # cur.execute(query)
        # data = cur.fetchall()

        data = get_temp_data()

        return data


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ctrl = ControllerMVC()
    ctrl.show()
    sys.exit(app.exec_())