import re

data = """
park 800905-1049118
kim 700905-1059199
"""

pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******", data))

print(re.sub(r'(.+)-[0-9]{7}', '\g<1>-*******', data))

# vim 에서도 정규표현식을 사용할 수 있음
# /[.!]append 라고 쳐서 .append 아니면 !append 를 찾아줄 수 있다.

###################

a = 'aaaabbbccccc'
b = re.search(r'a{4}b{3}c{5}', a)
print(b)

# but a,b,c가 가변적이면 찾을 수가 없음.
# 그래서 +를 대신 써주면 몇개든 다 찾을 수가 있음

c = re.search(r'a+b{3}c{5}', a)
print(c)

# + 는 1개 이상, *는 0개 이상.
aa = 'bbbccccc'
d = re.search(r'a*b{3}c{5}', aa)
print(d)


pnumber = '010-1234-5678'
pnum = '+82 10-1234-5678'

# re.sub(<pattern>, 바꿀 문자열, 찾을 문자열)
zz = re.sub(r'\+\d{2} ', '0', pnum)
print(zz)

# teacher
res = re.sub(r'\+\d{1,2} \d{1,2}-(.+)', '010-\g<1>', pnum)
# 뒷자리는 다시 써야되니까 (.+)으로 그룹으로 만들고, \g<1> 그룹을 다시 작성함
print(res)
