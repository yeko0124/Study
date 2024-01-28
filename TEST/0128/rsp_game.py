import random
import time

"""
가위 바위 보 게임
가위: 1  / 바위: 2 / 보: 3

FOR문 10번 중 3번 모두 이기면 승리 ,,,, 3번 
무작위로 호출 ->> RANDOM
"""

# 딕셔너리를 사용하여, 값을 가지고 오도록 함.
rsp = {1: '가위', 2: '바위', 3: '보'}
cnt = 0  # 이길 때마다 +1
cnt_d = 0  # 비길 때마다 +1
# a = 10

a = int(input('환영합니다. 몇 판 하시겠습니까?\n>>'))
time.sleep(0.3)

print(f'가위바위보 총 {a}판을 진행합니다.')
time.sleep(0.3)

for i in range(a):
    print(f'-----{i+1}ROUND-----')
    user = int(input('가위! 바위! 보!-----[ 가위:1 / 바위:2 / 보:3 ]\n>>'))
    if not 0 < user < 4:
        # print(KeyError)
        print('잘못 내셔서 졌습니다.')
        continue
    com = random.randrange(1, 4)

    print(f'{rsp[user]}를(을) 냈습니다.')
    time.sleep(1)

    print(f'com은 {rsp[com]}를(을) 냈습니다.')
    time.sleep(0.5)

    if cnt != 3:
        if user == com:
            print('비겼습니다.')
            cnt_d += 1
        elif (user == 1 and com == 2) or (user == 2 and com == 3) or (user == 3 and com == 1):
            print('졌습니다.')
        elif (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2):
            print('이겼습니다.')
            cnt += 1
        if cnt == 3:
            print(f'{a}번 중 3번을 먼저 이겨서 게임을 종료합니다.')
            break

print('-'*20)

print(f'{a}번 중 총 {cnt}번 이겼고, {cnt_d}번 비겼고, {a-cnt_d-cnt}번 졌습니다.')
time.sleep(0.5)

if cnt > (a-cnt_d-cnt):
    print('최종 승자는 당신입니다. YOU WIN !!!!')
elif cnt == (a-cnt_d-cnt):
    print('최종 결과는 비겼습니다. DRAW~~~')
else:
    print('최종 승자는 com입니다. YOU LOSE ㅠㅠㅠㅠ')
