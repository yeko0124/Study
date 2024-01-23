
# /data/tmp.txt 모든 단어의 개수를 구하는 함수
# 모든 단어는 소문자로 만들어서 개수를 구해야 함 -> a.lower() / count
# dictionary 사용하기


# 딱 알파벳만 거를 수 있는 방법이 뭘까.. only alphabet.. -> re모듈을 사용해보기

# 어딜가나 따라다닐 친구 re모듈

# res = word_find()
# print(res)
import re

def word_find():
    fin = {}
    with open('/data/zzz.txt', 'r') as f:
        lines = f.read()
        lines = lines.lower()
        liness = re.sub(r'[?!@#$%^&*()_+=.,–\'"]+', '', lines, re.DOTALL)
        voca = liness.split()
        for word in voca:
            # print(word)
            fin.setdefault(word, 0)
            cnt = 0
            for fin_word in voca:
                cnt += fin_word.count(word)
            fin[word] = cnt
    return fin


import pprint
# pprint.pprint(word_find())
res = word_find()
print(res.get('solar'))

# import pprint -> 함수를 정렬해주는 느낌?
#


# teacher's code----------------------------------------------------------------------

# def word_count(fpath: str) -> dict:
#     d = dict()
#     with open(fpath, 'r') as fp:
#         lines: list = fp.readlines()
#         total_lst = list()
#         for line in lines:
#             line: str = re.sub(r'[?!@#$%^&*()_+=.,–\'"]+', '', line, re.DOTALL)
#             line: str = line.lower()
#             word_lst: list = line.split()
#             total_lst += word_lst
#
#         unique_lst = list()
#         for ele in total_lst:
#             if ele not in unique_lst:
#                 unique_lst.append(ele)
#
#         for ele in unique_lst:
#             d[ele] = total_lst.count(ele)
#
#     return d


# pprint.pprint(word_count('/data/zzz.txt'))
