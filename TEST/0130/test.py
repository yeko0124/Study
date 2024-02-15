import re

# 정규 표현식을 컴파일
pattern = re.compile(r'[^a-z]+')

# 여러 문자열에서 패턴 매칭을 수행
result1 = pattern.match('123abc')
result2 = pattern.match('456def')

# 결과 확인
if result1:
    print('Match found in 1st string:', result1.group())
else:
    print('No match in 1st string')

if result2:
    print('Match found in 2nd string:', result2.group())
else:
    print('No match in 2nd string')
