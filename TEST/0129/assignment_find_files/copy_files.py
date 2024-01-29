# file copy test
import re
import shutil
import pathlib

# shutil.chown() 권한을 바꿔주는 모듈
# shutil.copytree()  디렉토리 복사해주는 모듈

# dirpath = pathlib.Path('/home/rapa/copy_files/seqeunce_data')

dirpath = pathlib.Path('/Users/yeko/Desktop/netflix_TD/python/sequence_data')

# shutil.copy2('/home/rapa/aaa.py', '/home/rapa/qqq.py')

res = dirpath.glob('*.exr')

comp = re.compile(r'\.(?P<frange>[0-9]{4})\.', re.DOTALL)
file_frame_lst = []

for i in res:
    srch = comp.search(i.name)
    # print(i.name)  # file 이름만 나옴
    file_frame_lst.append(int(srch.group('frange')))


lst = range(1001, 1151)

frame_info = set(lst) ^ set(file_frame_lst)

print(list(frame_info))

# 단일 테스트를 해야한다.

# s = 'render.1047.exr'

# zz = re.search(r'\.(?P<frange>[0-9]{4})\.', s, re.DOTALL)
# match는 처음에 한번 안나오면 바로 끝 / search는 계속 찾아줌
# (?P<ddd>) 으로 re 모듈에서 그룹네임을 만들 수 있음
# print(zz.groups()[0])

# print(zz.group('frange'))

"""
VFX회사에서는 sequence가 많음
렌더팜을 돌리지만, 가끔 렌더에서 사이즈가 0인걸로 나올 때가 있음 . 에러인거지..
그런 것만 찾아내거나, 빼서 추출하도록 해달라는 요청들이 있음
"""

