#!/usr/bin/env python
# encoding=utf-8

import sys
import datetime

# author        : yeeun ko
# create date   : 2024.02.20
# modified date : 2024.02.20
# description   : practice mvc pattern

from PySide2 import QtWidgets, QtGui, QtCore

# 원래는 클래스에 mapping해서 해야함
import mysql.connector as mysql_con

import random
from faker import Faker


def get_temp_data():
    fake = Faker()

    fetch_all = list()

    for i in range(int(1000000)):
        yyyy = random.choice(list(range(1980, 2000)))
        mm = str(random.choice(list(range(1, 12)))).zfill(2)
        dd = str(random.choice(list(range(1, 28)))).zfill(2)
        date_str = f'{yyyy}-{mm}-{dd}'
        date_str = datetime.date.fromisoformat(date_str)

        fetch_all.append((i, fake.name(), fake.address(), fake.ipv4_private(), date_str))
    return fetch_all


con = mysql_con.connect(
    host='127.0.0.1', user='root', passwd='', database='dummy_db'
)
cur = con.cursor()


class Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.__table_widgt = QtWidgets.QTableWidget()
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.__table_widgt)

        # main window는 일반 위젯이랑 좀 다름 -> 여기서는 그래서 setLayout이 안된다
        # -> central widget이라는게 존재하기 떄문에 안됨
        # central widget을 만들어서 그 곳에 너ㅎ어줘야 함
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)

        # item = QtWidgets.QTableWidgetItem('aaa')
        # item2 = QtWidgets.QTableWidgetItem('bbb')

        # self.__table_widgt.setItem(0, 0, item)
        # self.__table_widgt.setItem(1, 0, item2)

        self.set_data(self.get_data())
        # self.get_describe()

    def get_describe(self):
        query = '''
        DESCRIBE user_info;
        '''

        # cur.execute(query)
        # data = cur.fetchall()
        data = get_temp_data()
        # return data
        print(data)

    def set_data(self, data):
        # fetchall
        '''
        [
            (0, 'name', 'address', 'ip_address', datetime.date('1992', '5', '12'),
            (1, 'name', 'address', 'ip_address', datetime.date('1992', '5', '12'),
            (2, 'name', 'address', 'ip_address', datetime.date('1992', '5', '12'),
            ...
        ]
        '''

        # print(len(data[0]))
        self.__table_widgt.setRowCount(len(data))
        self.__table_widgt.setColumnCount(len(data[0]))

        for row, i in enumerate(data):
            for col in range(len(data[0])):
                print(i)
                if col == 4:
                    date: datetime.date = i[col]
                    date = f'{date.year}-{date.month}-{date.day}'
                    item = QtWidgets.QTableWidgetItem(date)
                elif col == 0:
                    item = QtWidgets.QTableWidgetItem(str(i[col]))
                else:
                    item = QtWidgets.QTableWidgetItem(i[col])
                self.__table_widgt.setItem(row, col, item)

    def get_data(self):
        query = '''
        SELECT * FROM user_info;
        '''
        cur.execute(query)
        data = cur. fetchall()

        return data


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ctrl = Controller()
    ctrl.show()
    sys.exit(app.exec_())
