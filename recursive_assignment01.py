
print('\n <Assignment> \n')

json_data = {
    'shot': {
        'EP0070': {
            'EP0070_C0100': {
                'fps': 24,
                'frame': [1001, 1200],
                'author': [
                    {'worker1': '2023-10-10'},
                    {'worker2': '2023-10-15'}
                ],
                'tmp': {
                    'a': 111,
                }
            },
            'EP0070_C0200': {
                'fps': 24,
                'frame': [1001, 1080],
                'author': 'zzzz'
            }
        }
    }
}


def json_author(data: dict):
    for k, v in data.items():
        if k == 'author':
            if isinstance(v, list):
                for i in range(len(v)):
                    lst = list(v[i].items())
                    aa = lst[0]
                    for j in range(len(aa)):
                        print(aa[j], end = ' - ' if j == 0 else '\n')
            else:
                print(v)
            return
        elif isinstance(v, dict):
            json_author(v)

# worker1 - 2023-10-10
# worker2 - 2023-10-15
# zzz

print('1번')
json_author(json_data)

"""
json_author 출력
( '-'는 넣지 못함.. )
worker1 2023-10-10
worker2 2023-10-15
zzzz
"""

print('-'*10)

json_data2 = {
    'shot': {
        'EP0070': {
            'EP0070_C0100': {
                'fps': 24,
                'frame': [1001, 1200],
                'author': 'anon',
                'tmp': {
                    'a': 111,
                }
            },
            'EP0070_C0200': {
                'fps': 24,
                'frame': [1001, 1080],
                'author': 'zzzz'
            }
        }
    }
}

# print(json_data.keys())
# print(json_data.items())


def author(data: dict):
    for a, b in data.items():
        if a == 'author':
            print(b)
            return
        elif isinstance(b, dict):
            author(b)


print('\n2번')
author(json_data2)


def recursive_dd(lst: list):
    for i in lst:
        if i == 'dd':
            print(i)
            return
        if not isinstance(i, list):
            continue
        return recursive_dd(i)



data = [
    'a', 'b', 'c', [
        'h', [
            'k', [
                'm', 'n', ['aaa', [
                    'cc', 'dd'
                ], 'bbb'], 'o', 'p'
            ], 'l'
        ], 'i', 'j'
    ], 'd', 'e', 'f', 'g'
]

# # 01
# print(data[2])
#
# # 02
# print(data[3][2])
#
# # 03
# for i in data:
#     if i == 'c':
#         print(i)
#     else:
#         continue
#
# # 04
# for i in range(len(data)):
#     if i == 3:
#         lst = data[i]
#         print(lst[2])
#         break
#
# # 04-1
# for i in data:
#     if not isinstance(i, list):
#         continue
#     for j in i:
#         if j == 'j':
#             print(j)
#             break
#
# # 05
# for i in data:
#     if not isinstance(i, list):
#         continue
#     for j in i:
#         if not isinstance(j, list):
#             continue
#         for a in j:
#             if a == 'k':
#                 print(a)
#                 break
#
# # 06
# for i in data:
#     if not isinstance(i, list):
#         continue
#     for j in i:
#         if not isinstance(j, list):
#             continue
#         for a in j:
#             if not isinstance(a, list):
#                 continue
#             for b in a:
#                 if b == 'o':
#                     print(b)
#                     break
#
#
# # �ш컻�⑥닔 (諛섎났)
# # �먭린 �먯떊�� �몄텧�쒕떎湲� 蹂대떎��, �먭린 �먯떊�� 蹂듭궗�댁꽌 蹂듭궗�� �⑥닔濡� 媛꾨떎怨� �앷컖�섎㈃ ��
# def recursive(data):
#     if data < 0:
#         return
#     return recursive(data - 1)
#
#
# recursive(10)
#
#
# # 07
# for i in data:
#     if not isinstance(i, list):
#         continue
#     for j in i:
#         if not isinstance(j, list):
#             continue
#         for a in j:
#             if not isinstance(a, list):
#                 continue
#             for b in a:
#                 if not isinstance(b, list):
#                     continue
#                 for c in b:
#                     if not isinstance(c, list):
#                         continue
#                     for d in c:
#                         if d == 'dd':
#                             print(d)
#                             break
#


# �ш컻�⑥닔瑜� �묒꽦�� �뚮뒗 �⑥닔瑜� �섍컝 議곌굔臾몄쓣 癒쇱� �⑥쨾�� ��



# recursive_dd(data)