"""
/data/tmp.txt파일에서
and라는 단어가 몇개 나오는지
반복문과 open함수 이용하여 출력 함수
"""

# 함수, 반복문, 제어문, fileIO

try:
    with open('/data/tmp.txt', 'r') as f:
        and_lst = []
        of_lst = []
        for line in f:
            a = f.read()
            b = a.split(' ')
            # print(b)
        for i in range(len(b)):
            if b[i] == 'and':
                and_lst.append(b[i])
            elif b[i] == 'of':
                of_lst.append(b[i])
        # print(and_lst)
        print(f'앤드는 {len(and_lst)}개')
        print(f'오브는 {len(of_lst)}개')
except FileNotFoundError as err:
    print(err)


# # 정현방식 : find 사용 -> 해보기
# try:
#     with open('/data/tmp.txt', 'r') as f1:
#         # d : 문장들을 리스트로 만들고, 그 리스트들을 다 저장한 다른 리스트
#         d = []
#         final = []
#         for i in f1:
#             # c : 문장을 str -> list로 변환
#             c = list()
#             c.append(f1.readline())
#             # print(type(c))
#             d.append(c)
#         # 근데 어차피 list로 받아도 결국 string으로 변환해야되는거 아닌가.?
#         for k in d:
#             strr = k[0]
#             kk = strr.split(' ')
#             # print(kk[0][0])
#             for lst in range(len(d)):
#                 if isinstance(lst, list):
#                     # 리스트면 len길이가 끝날 때까지 돌면서,
#                     # and를 찾아라 다 찾으면 for 문 나와서 다음 리스트로 다시 for문 돌리기
#                     for dd in range(len(kk)):  # 각자의 문장 길이만큼만 포문을 돌리는 것
#                         if kk[dd] == 'and':
#                             print(kk[dd])
#
#         print('final:', final)
# except FileNotFoundError as er:
#     print(er)


def word_count(word_lst: list) -> dict:
    dic = dict()
    with open('/data/tmp.txt', 'r') as fp:
        lines = fp.readlines()
        for word in word_lst:
            print(word)
            dic.setdefault(word, 0)
            cnt = 0
            for line in lines:
                cnt += line.count(word)
            dic[word] = cnt
    return dic

# word_count(['and', 'of'])
# print(word_count(['and', 'of']))
