
import re
import pathlib

# pxr -> PXR2
# /home/rapa/workspace/data/usd

"""
old
include "pxr/pxr.h"

new
include "PXR2/pxr.h"
"""

# 원본을 살릴거면 다른 이름으로 저장 / 그냥 덮을거면 덮기


# class ChangePxr:
#     def __init__(self, path):
#         self.path = path
#
#         self.read_file()
#
#     def read_path(self):
#         pass
#
#     def read_file(self):
#         # 상위 path에서 디렉토리를 더 들어갈 수도 있고 안들어갈 수도 있어
#         # comp = re.compile(r'[\w+]?/?[\.\w+]')
#         with open(f'{self.path}/', 'r') as fp:
#             print(fp)


fpath = '/home/rapa/workspace/data/usd'

# c = ChangePxr(fpath)

f_path = []


def change_name(path):
    # lst = []
    path = pathlib.Path(path)
    # TODO: 재귀함수로 하는 방법은 뭘까? 재귀는 집에서 해보자
    files = path.glob('**/*')
    comp = re.compile(r'\.(cpp|h)')
    for f_path in list(files):
        # print(f_path)
        res = comp.search(f_path.name)
        if res is None:
            continue
        yield f_path


# .cpp /.h 파일 경로만 f_path로 yield해서 list로 변환
res_file = list(change_name(fpath))
print(res_file)

for i in res_file:
    with open(i, 'r') as f1:
        a = f1.read()
    # print(i[20])
    with open(i, 'w') as f2:
        tmp = f2.write(re.sub('pxr|PXR', 'PXR2', a))



