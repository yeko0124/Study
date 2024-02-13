import os
import pathlib
import typing
# typing -> ll: typing.List[int] = list() 처럼 형식을 지정해줄 수 있는 것
# 즉, def get(num: int) 처럼 num 이 int인 것을 미리 지정해주는 것
# 


from PySide2 import QtGui, QtCore, QtWidgets

# parent_dir = ''
# pattern = ''

class System:
    @staticmethod
    def get_files(parent_dir: pathlib.Path, pattern: typing.List[str]) -> typing.Generator:
        '''
        사용자가 지정한 부모 디렉토리로부터 모든 하위 디렉토리를 검색하여
        특정 확장자를 가진 파일들을 반환하는 제네레이터
        :return: 파일 경로 <generator>
        '''

        for f in parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in pattern:
                yield f
            else:
                if f.suffix in pattern:
                    yield f

    @staticmethod
    def get_files_lst(parent_dir: pathlib.Path, pattern: typing.List[str]) -> typing.List[pathlib.Path]:
        '''
        사용자가 지정한 부모 디렉토리로부터 모든 하위 디렉토리를 검색하여
        특정 확장자를 가진 파일들을 반환하는 메서드
        :return: 파일 경로 <list>
        '''
        lst = list()
        for f in parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in pattern:
                lst.append(f)
            else:
                if f.suffix in pattern:
                    lst.append(f)
        return lst

    @staticmethod
    def get_files_recursion(dpath, pattern: typing.List[str], depth=0) -> typing.Generator:
        '''

        :param dpath: 부모 디렉토리
        :param pattern: 깊이 값
        :param depth:
        :return: file path generator
        '''

        lst = list()
        file_lst = os.listdir(dpath)
        for f in file_lst:
            # fullpath => '/home/rapa/workspace/usd/sdr/api.h'
            # fullpath => '/home/rapa/workspace/usd/sdr/testenv'
            fullpath = os.path.join(dpath, f)
            if os.path.isdir(fullpath):
                lst += System.get_files_recursion(fullpath, pattern, depth+1)
            else:
                if os.path.isfile(fullpath):
                    if '*' in pattern:
                        lst.append(fullpath)
                    else:
                        ext = f'.{fullpath.split(".")[-1]}'
                        if ext in pattern:
                            lst.append(fullpath)
        yield from lst
