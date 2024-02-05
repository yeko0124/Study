import itertools

# q1) 문자열 바꾸기

# q2) 딕셔너리 값 추출

# q3) 리스트의 더하기와 extend 함수

# q4) 리스트 총합

# q5) 피보나치 함수
def fib(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fib(N-2) + fib(N-1)

# q6) 숫자의 총합

# q7) 한 줄 구구단

# q8) 파일을 읽어 역순으로 저장

# q9) 평균값 구하기

# q10) 계산기 만들기

# q11) 모듈 사용하는 방법

# q12) 오류와 예외 처리

# q13) DashInsert 함수
'''
홀수가 연속되면 두 수 사이 '-'
짝수가 연속되면 '*'
input: 4546793
output: 454*67-9-3
'''
def dash_insert():
    ss = '4546793'
    idx = 0
    res = list()
    length = len(ss) - 1
    while True:
        res.append(ss[idx])
        next_idx = idx+1
        curt_str = int(ss[idx])
        next_str = int(ss[next_idx])
        if curt_str & 0x01 and next_str & 0x01:
            res.append('-')
        elif not (curt_str & 0x01) and not (next_str & 0x01):
            res.append('*')
        idx += 1
        if idx >= length:
            if idx == length:
                res.append(next_str)
            break

    print(''.join(map(lambda x: str(x), res)))

dash_insert()

# q14) 문자열 압축
def compress_str():
    ss = 'aaabbbccca'
    lst = list(sorted(map(lambda x: x, ss)))
    # print(lst)
    res = ''
    for k, v in itertools.groupby(lst):
        res = f'{res}{k}{len(list(v))}'
    print(res)

compress_str()

# q15) Duplicate Numbers 함수

# q16) 모스 부호 해독
'''
문자열 형식으로 입력받은 모스 부호 .(dot)과 -(dash)를 해독하여 영어 문장으로 출력
'''
def read_moss():
    table = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D'
    }

    ss = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'

    def run():
        res = list()
        for i in ss.split(' '):
            for j in i.split(' '):
                try:
                    res.append(table[j.strip()])
                except KeyError:
                    pass
            res.append(' ')
        return res

    print(run())

# read_moss()
# q17) 정규식 - 기초 메타 문자

# q18) 정규식 - 문자열 검색

# q19) 정규식 - 그루핑

# q20) 정규식 - 전방 탐색