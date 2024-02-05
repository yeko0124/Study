import re

email_lst = [
'a34ds2aa@naver.com', ' edsa@gmail.com', '+#dsee@naver.com', 'xxse@gamil.com',
'eee22_slz@gmail.com', 'eeww@kakao.co.kr',
'a_z__bd43@naver.com'
]


# def  함수 (email_lst) -> list:

def check_email(email):
    # 메일 패턴 : <name>@<sitename>\.<[A-Za-z]>
    e = re.compile(r"([a-zA-Z\d]+@[a-z]+\.[a-z]+\.*[a-z]*)")
    for i in email:
        i = re.sub('gamil', 'gmail', i)
        # true이면 로그인 됌 출력 / false면 이메일 형식이 아님 출력
        res = e.search(i)
        # print(res)
        if res == None:
            print('이메일 형식이 틀렸습니다.')
            break
        print(f'{res.group()}로 로그인 합니다.')


check_email(email_lst)


######################################################################
# teachers code

def find_invalid_email_addr(email):
    comp = re.compile(r'^\W+')  # \w word  \W word가 아닌 것 => 특수 기호같은 것
    lst = list()
    for i in email:
        res = comp.search(i)
        if res is None:
            continue
        lst.append(res)
        # print(res.group())
        yield res


print(list(find_invalid_email_addr(email_lst)))


def check_email_addr(email) -> list:
    # ^[\w\d_]+@[\w\.]+[\w]?
    comp = re.compile(r'^[\w\d_]+@[\w\.]+[\w]?')  # \w word  \W word가 아닌 것 => 특수 기호같은 것
    for i in email:
        res = comp.search(i)
        if res is None:
            yield i


print(list(check_email_addr(email_lst)))

