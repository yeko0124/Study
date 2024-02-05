#!/usr/bin/env python
# encoding=utf-8

# author        : yeeun ko
# create date   : 2024.02.04
# modified date : 2024.02.04
# description   :

import os
import re
import sys
import pathlib

from lib import change_files, find_file

# TODO 조립을 하자


class Main:
    def __init__(self,
                 find_str: str, change_str: str, pattern: str,
                 parent_dir: pathlib.Path, ext_pattern: list):

        self.__cf = change_files.ChangeFiles(find_str, change_str, pattern)
        self.__ff = find_file.FindFiles(parent_dir, ext_pattern)
        self.__parent_dir = parent_dir

    def change_contents(self):
        files = self.__ff.get_files_recursion(self.__parent_dir)
        for i in files:
            assert isinstance(i, find_file.CheckWord)
            is_exist = find_file.CheckWord.is_check_word(
                i.fullpath, '#include "pxr')
            ###################
            if not is_exist:
                continue
            is_suc = self.__cf.change_file(i.fullpath)
            if not is_suc:
                sys.stderr.write(f'{i.fullpath.as_posix()}: ERR!!!')  # stderr: 표준 오류
            # space = ' ' * i.depth
            # print(f'{space}: {i.fullpath} - {i.depth} : {is_exist}')


class Lego(change_files.ChangeFiles, find_file.CheckWord, find_file.FindFiles):
    def __init__(self, parent=None):
        # super(Lego, self).__init__(parent)
        change_files.ChangeFiles.__init__(self, 'PXR2', '#include "PXR2', '#include "pxr(.+)')
        find_file.FindFiles.__init__(self, pathlib.Path('/home/rapa/workspace/data/usd/ar'), ['.cpp', '.h'])

        res = self.get_files_recursion('/home/rapa/workspace/data/usd/')
        for i in res:
            assert isinstance(i, find_file.CheckWord)
            is_exist = find_file.CheckWord.is_check_word(i.fullpath, '#include "pxr')
            if not is_exist:
                continue
            is_suc = self.change_file(i.fullpath)
            print(f'{i.fullpath} - {i.depth} : {is_exist}')  # 있는거 확인함


if __name__ == '__main__':
    main = Main(find_str='PXR2', change_str='#include "PXR2', pattern='#include "pxr(.+)',
                parent_dir=pathlib.Path('/home/rapa/workspace/data/usd/sdr'),
                ext_pattern=['.cpp', '.h'])

    # main.change_contents()

    lego = Lego()


