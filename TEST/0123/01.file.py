"""
파일 읽고 쓰기 (p.175)
"""

f = open('new.txt', 'w')
f.close()

print(f)

with open('new_2.txt', 'w') as fp:
    print(fp)

# wt: write text
# wb: write binary -> for computer

try:
    with open('/home/rapa/workspace/python/TEST/0123/new3.txt', 'r') as f1:
        f1.write('oh my god')
        # f1.__iter__()  --> iter가 있으면 for문이 자동으로 되는 것임
        # for i in f: ->
        print(f1)
except FileNotFoundError as err:
    print(err)


# print(f.readline())  -> 한줄만 읽는 것 (한줄 한줄을 list에 element로 가져와서 반환)
# print(f.read())  -> 한번에 다 가져오는 것 (스트링 값으로 싸악 통째로 가져오는 것)
