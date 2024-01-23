
import re
import pprint
import itertools as it

# as 붙이면 as 뒤에 오는 걸로 모듈을 지정해서 부를 수 있음. 별명같이

# groupby -> key를 기준으로 그룹을 지어줌
# groupby(iterable, key = None)

l = [(1, 2), (3, 4), (1, 2), (4, 5)]

for key, val in it.groupby(l):
    print(key, list(val))

print('-'*20)

# 그룹이 되기 이전에 sort가 먼저 되어 있어야 함.
for key, val in it.groupby(sorted(l)):
    print(key, list(val))
'''출력
(1, 2) [(1, 2), (1, 2)]
(3, 4) [(3, 4)]
(4, 5) [(4, 5)]
'''

# iter를 이용해서 함수를 다시 변경해보자!


print('-'*20)


def word_find():
    fin = {}
    with open('/data/zzz.txt', 'r') as f:
        lines = f.read().replace('\n', '')
        lines = lines.lower()
        liness = re.sub(r'[0-9?!@#$%^&*()_+=.,–\'"]+', '', lines, re.DOTALL)
        voca = liness.split()
        # for k, v in it.groupby(sorted(liness.split())):
        # 라고 하면 위에 voca라는 것도 필요가 없어짐
        for k, v in it.groupby(sorted(voca)):
            print(k, len(list(v)))
    return fin


pprint.pprint(word_find())
