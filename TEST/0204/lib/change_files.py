import pathlib
import random
import re


# 변경할 문자열, 찾을 문자열(find_file 모듈에서 찾은 문자로 하면 됨)
# main purpose : 해당 클래스에서 파일 변경


class ChangeFiles:
    def __init__(self, find_str: str, change_str: str, pattern: str):
        # 찾을 패턴
        self.__pattern = pattern
        # 검색 대상 문자열 (원본)
        self.__find_str = find_str
        # 바꿀 문자열
        self.__change_str = change_str


    def change_file(self, fpath: pathlib.Path, is_override=False) -> bool:
        try:
            with open(fpath.as_posix(), 'r') as fp:
                read = fp.read()
                self.__find_str = read

                # #include "PXR2\g<1>
                changed_contents = re.sub(
                    r'{0}'.format(self.__pattern),
                    f'{self.__change_str}\g<1>',
                    self.__find_str)

            # save
            if is_override:
                with open(fpath.as_posix(), 'w') as fp:
                    fp.write(changed_contents)
                    return True
            # save as
            else:
                # 위에 디폴트가 is_override = False이기 때문에
                # else가 실행되어 save as가 되고 있는 중임
                with open(fpath.with_name('{0}.{1}'.format(fpath.name, random.randrange(1000))), 'w') as fp2:
                    fp2.write(changed_contents)
                    return True
        except (FileNotFoundError, IOError) as err:
            # File not found error : 파일이 존재하지 않을 떄 발생
            # IoError :
            return False


if __name__ == '__main__':
    # testfile = '/home/rapa/workspace/data/usd/sdr/api.h'
    c = ChangeFiles('PXR2', '#include "PXR2', '#include "pxr(.+)')
    # c.change_file(pathlib.Path())

