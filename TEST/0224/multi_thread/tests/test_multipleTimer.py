#!/usr/bin/env python
# encoding=utf-8

# author        : yeeun ko
# create date   : 2024.02.24
# modified date : 2024.02.24
# description   :


"""
test를 통해서 함수 검증도 되면서, 다른 사람이 봤을 떄 어떻게 사용하는지 알 수가 있는 지표가 됌

*** 함수 이름을 정할 때 앞에 'test_'가 없으면 인식하지 못한다. 즉, test_를 꼭 붙여주어야 함
"""

from PySide2 import QtCore, QtGui, QtWidgets

import pytest
import pathlib
import sys

# sys.path.append('/home/rapa/workspace/python/week_10/multi_thread')
import multipleTimer_ko


# 아직 미완성일 때, 아래와 같은 데코레이션을 붙여주면 test를 skip해서 에러가 안나도록 할 수 있음
# @pytest.mark.skip
def test_get_time2sec():
    qtime = multipleTimer.MultipleTimer.secs2qtime(1000)
    sec = multipleTimer.MultipleTimer.qtime2secs(qtime)
    assert sec == 1000


def test_addition():
    assert multipleTimer.MultipleTimer.addition('3', '5') == '35'


def test_open_file_using_thread():
    # import skip (모듈 테스트)
    # >> thrid party module이 필요한 상황인데, 안깔려 있을 경우 imoprt error 가 나게 될 수 있음
    # from system import library as sys_lib
    # assert sys_lib.System.open_file_using_thread(pathlib.Path('/usr/bin/gnome-terminal'), None, False)

    # import hou
    # hou = pytest.importorskip(modname='hou')  # 이런 식으로 skip 가능

    sys.path.insert(0, '/home/rapa/workspace/python/libraries/system')
    sys_lib = pytest.importorskip(modname='library')

    assert sys_lib.System.open_file_using_thread(pathlib.Path('/usr/bin/gnome-terminal'), None, False) == True


if __name__ == '__main__':
    pass
