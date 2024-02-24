import sys
import datetime

from PySide2 import QtWidgets, QtGui, QtCore

import mysql.connector as mysql_con

import random

from faker import Faker   # 가짜 데이터 만드는 모듈

import time
import functools


# 시간 받아서 시간 분 초로 계산해주는 것
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

        # h, m, s = secs2qtime(int(elapsed_time))

        print(f'<{self.__func.__name__} >: {elapsed_time}')
        # print(f'<{self.__func.__name__}> elapsed time: [시간: {h}], [분: {m}], [초: {s}]')
        return res


def CheckRuntime2(func):
    def wrapper(self, data):
        start_time = time.time()
        res = func(self, data)
        end_time = time.time()
        elapsed_time = end_time - start_time

        h, m, s = secs2qtime(int(elapsed_time))

        print(f'<{func.__name__}> elapsed time: [시간: {h}], [분: {m}], [초: {s}]')
        return res
    return wrapper


@CheckRuntime2
def zzzz(a, b):
    return a + b


# 이거는 그냥 test용
@CheckRuntime
def get_temp_data():
    fake = Faker()

    fetch_all = list()

    for i in range(100):
        yyyy = random.choice(list(range(1980, 2000)))
        mm = str(random.choice(list(range(1, 12)))).zfill(2)
        dd = str(random.choice(list(range(1, 28)))).zfill(2)
        date_str = f'{yyyy}-{mm}-{dd}'
        date_str = datetime.date.fromisoformat(date_str)

        fetch_all.append(
            (i, fake.name(), fake.address(), fake.ipv4_private(), date_str)
        )

    return fetch_all


# connect 객체는 db를 열고, 닫고, commit(승인), rollback(되돌리기)을 할 수 있는 객체
con = mysql_con.connect(host='127.0.0.1', user='root', passwd='', database='dummy_db')

# cursor 객체는 query(쿼리)를 실행하는 객체
cur = con.cursor()


# MVC 중에 M(Model)에 해당 -> data model class
class TableModel(QtCore.QAbstractTableModel):
    # QAbstractListModel를 상속받아서 꼭 data를 해줘야 한다
    # 여기는 data만 넘기면 알아서 돌게끔 만들어 준다. for / while 안써도 됌
    def __init__(self, data):
        super().__init__()
        self.__data = data
        # COLUMN HEADER NAME
        self.__header = ['id', 'name', 'addr', 'ip_addr', 'birth']

    # data를 꼭 override를 해줘야 함 **** data가 중요함.
    def data(self, index, role=...):
        # 나 대신 해주네... 굳이 호출을 안해도 됨
        # 뷰에 보이게하는 역할하는 부분
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            # 2차원 배열 ([[...],[...]])이므로 ROW, COLUMN을 이용하여 개별적으로 데이터를 뽑아야 함
            # DATA = [[1, 2, 3], [4, 5, 6]]
            # DATA[0][1] --> 2가 나옴
            data = self.__data[index.row()][index.column()]

            # DATABASE에서 TYPE이 DATE라면 파이썬으로 가져왔을 때 DATETIME 객체로 래핑되어 있다.
            # 따라서 문자열로 바꿔줘야 한다
            if isinstance(data, datetime.datetime):
                return f'{data.year}-{data.month}-{data.day}'
            # DATA가 STRING이 아닐 경우를 위하여 STRING으로 변경해주는 부분
            elif not isinstance(data, str):
                return str(data)
            return data

        # ItemDataRole이 중요함. 이게 역할임. view에 보이는 것을 표시하는 역할
            # return self.__data[index.row()][index.column()]
        # DECORATION ROLE이 하는 역할은, ICON을 나 대신 등록해준다.
        elif  role == QtCore.Qt.DecorationRole:
            ipath = '/data/apple.jpg'
            image = QtGui.QImage(ipath)
            return QtGui.QPixmap.fromImage(image).scaled(
                QtCore.QSize(24, 24), QtCore.Qt.KeepAspectRatio)

    # MODEL로 넘어온 데이터의 COLUMN 개수
    def columnCount(self, parent=...):
        return len(self.__data[0])

    # MODEL 로 넘어온 데이터의 ROW 개수
    # rowCount만큼 data의 index가 설정되면서 계속 돌아간다
    def rowCount(self, parent=...):
        return len(self.__data)

    # 테이블 뷰의 헤더 부분을 나 대신 등록해주는 ...
    def headerData(self, section, orientation, role=...):
        if role == QtCore.Qt.DisplayRole:
            # 뷰의 가로 부분 헤더
            if orientation == QtCore.Qt.Horizontal:
                return self.__header[section]
            # 뷰의 세로 부분 헤더
            elif orientation == QtCore.Qt.Vertical:
                return str((int(section) + 1))
        # elif role == QtCore.Qt.DecorationRole:
        #     pass

# Database Viewer Application
# Framework : Pyside2, MySQL, ... (썼던 것 싹 다 적고)
# API (사용자 정의)
#   get_data(name: str, brith: datetime)-> list:
#       이름과 생년월일을 매개변수 전달하여 database에서 특정 데이터 반환
#   ...
#
# Class Controller ADT
# get_join_data(table_name: list) -> tuple:
#   table_name 시퀀스 데이터를 기반으로 database table inner join 사용
#   원하는 모든 필드 데이터들을 가져와 반한


class ControllerMVC(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # MVC 중 V(view)에 해당
        self.view = QtWidgets.QTableView()
        # 가져온 데이터를 모델에 전달. 그래서 데이터를 모델링한 형식에 맞춰 알아서 처리 해준다.
        self.model = TableModel(self.get_data())
        # 나 대신 처리해준 데이터들을 나 대신하여 view에 등록
        self.view.setModel(self.model)

        # view의 레이아웃
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.view)

        # QMainWindow는 QWidget, QDialog와 달리 centralWidget이라는 것이 존재하여 이곳에 위젯이 들어가야 한다
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)

        # self.set_data_from_db()

    def set_data_from_db(self):
        st = time.time()
        self.view.setModel(self.model)
        et = time.time()
        print(et - st)

    # DB에서 데이터 가져오기
    def get_data(self):
        query = """
        SELECT * FROM user_info;
        """
        cur.execute(query)
        data = cur.fetchall()
        # data = get_temp_data()   ->  fake data
        return data


class Controller(QtWidgets.QMainWindow):
    # 여기서는 set data만 알면 됌
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

    # 본인이 직접 등록을 해야하는 구조
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
                ipath = '/data/apple.jpg'
                image = QtGui.QImage(ipath)
                pixmap = QtGui.QIcon(QtGui.QPixmap.fromImage(image).scaled(
                    QtCore.QSize(24, 24), QtCore.Qt.KeepAspectRatio))

                if col == 4:
                    date: datetime.date = i[col]
                    date = f'{date.year}-{date.month}-{date.day}'
                    item = QtWidgets.QTableWidgetItem(date)
                    QtWidgets.QTableWidgetItem(pixmap, date)
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

    # 위젯 실행 시간 : 1분 4초 (64초)