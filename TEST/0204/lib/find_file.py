import os.path
import pathlib
import re


# 부모 디렉토리
# 특정 확장자만 찾을 수 있는 옵션

# os.listdir() # 파일 이름만
# os.path.exists() # 존재 하는가

class CheckWord:  # wrapping class / pxr이 있는지 검사할 클래스
    def __init__(self, fpath: str, depth: int):
        self.__fpath = fpath
        self.__depth = depth

    @property
    def fullpath(self) -> pathlib.Path:
        return pathlib.Path(self.__fpath)

    @property
    def depth(self) -> int:
        return self.__depth

    @staticmethod
    def is_check_word(fpath: pathlib.Path, find_str: str) -> bool:
        comp = re.compile(r'{0}'.format(find_str))
        with fpath.open('r') as fp:
            return comp.search(fp.read()) is not None
    # def is_check_word(self, find_str: str) -> bool:  # simple check if is or not
    #     comp = re.compile(r'{0}'.format(find_str))
    #     # print(self.fullpath)
    #     with open(i.fullpath, 'r') as fp:
    #         find = fp.read()
    #         # print(find)
    #     return comp.search(find) is not None


class FindFiles:
    def __init__(self,
                 parent_dir: pathlib.Path,
                 pattern: list):
        self.__parent_dir = parent_dir
        self.__pattern = pattern

    @property
    def parent_dir(self) -> pathlib.Path:
        return self.__parent_dir

    @property
    def pattern(self) -> list:
        return self.__pattern

# yield를 사용한 것
    def get_files(self):
        for f in self.parent_dir.glob('**/*'):
            if not f.is_file():  # is_file = 파일인지 아닌지 확인해주는 pathlib에 있는 모
                continue
            if '*' in self.pattern:
                yield f
            else:
                # suffix: 확장자만 출력해주는 모듈
                if f.suffix in self.pattern:
                    yield f

# list를 활용한 것
    def get_files_lst(self):
        lst = list()
        for f in self.parent_dir.glob('**/*'):
            if not f.is_file():  # is_file = 파일인지 아닌지 확인해주는 pathlib에 있는 모
                continue
            if '*' in self.pattern:
                lst.append(f)
            else:
                # suffix: 확장자만 출력해주는 모듈
                if f.suffix in self.pattern:
                    lst.append(f)
        return lst

# 재귀함수를 사용한 것
    def get_files_recursion(self, dpath, depth = 0):
        lst = list()
        file_lst = os.listdir(dpath)
        for f in file_lst:
            # fullpath = '/home/rapa/workspace/usd/dir/api.h'
            fullpath = os.path.join(dpath, f)  # 윈도우든 리눅스든 맥이든 path에 연결해주는 \라던지 \\ 다 상관없이 join시켜주는 모듈
            if os.path.isdir(fullpath):  # directory면?
                lst += self.get_files_recursion(fullpath, depth+1) # 재귀로 다시 돌리는 것
            else:
                if os.path.isfile(fullpath):  # linux는 신기하게도(?) 모든 것을 다 파일로 인식한다
                    if '*' in self.pattern:
                        lst.append(CheckWord(fullpath, depth))
                    else:
                        ext = f'.{fullpath.split(".")[-1]}'
                        if ext in self.pattern:
                            lst.append(CheckWord(fullpath, depth))

        # return lst
        yield from lst


if __name__ == '__main__':
    ff = FindFiles(
        pathlib.Path('/home/rapa/workspace/data/usd/'),
        ['.cpp', '.h'])
    # print(list(ff.get_files()))
    # print(ff.get_files_lst())
    res = ff.get_files_recursion('/home/rapa/workspace/data/usd/sdr')
    # print(list(res))

    for i in res:
        assert isinstance(i, CheckWord)
        is_exist = i.is_check_word('#include "PXR2')
        print(f'{i.fullpath} - {i.depth} : {is_exist}')

