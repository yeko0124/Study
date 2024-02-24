
# CRUD -> 조작은 일단 이렇게 네개만 알면 가능은 함
# C -> Create (insert)
# R -> Read (select)
# U -> Update (update)
# D -> Delete (delete)

import mysql.connector as mysql_con

insert_query = '''
insert into user_info (name, addr, ip_addr, birth) 
values (%s, %s, %s, %s)
'''

'''
INSERT INTO <table> (<fields...>) VALUES (<values...>);
'''


select_query = '''
select ip_addr from user_info where ip_addr like '192.%'
'''

update_query = '''
update user_info set name = 'zzz' where id=4301;
'''

delete_query = '''
delete from user_info where id=4301;
'''

delete_q = '''
DELETE FROM user_info WHERE name=%s AND addr=%s;
'''

update_q ='''
UPDATE user_info SET birth=%s WHERE id={0};
'''.format(4300)

# UPDATE <table> SET <field>=<value> WHERE id=1;

# select_q = '''
# SELECT * FROM user_info;
# '''

#오름차순으로 정렬해서 다시 가져오는 방식 -> 아래는 지금 name을 기준으로 오름차순(DESC) 하는 중
select_q= '''
SELECT * FROM user_info ORDER BY name DESC;
'''

con = mysql_con.connect(
    host='127.0.0.1', user='root', passwd='', database='dummy_db')

cur = con.cursor()


# 안전하게 데이터를 쿼리하는 방법
# try:
#     # cur.execute(insert_query, ('aaa', 'bbb','ccc', '1999/10/20'))   # 준비상태
#     # cur.execute(delete_q, ('aaa', 'bbb'))
#     # cur.execute(update_q, ('2002/05/14',))
#     cur.execute(select_q)
#     con.commit()  # commit이 있어야 비로소 데이터 베이스에 데이터가 들어감
#    # select 는 commit이 필요가 없음
#     print('success query!')
# except Exception as err:
#     con.rollback()  # 실패하면 준비상태 처음으로 돌아가라 라는 것. 에러날 때를 대비
#     print('failed query!', err)

cur.execute(select_q)
data = cur.fetchall()    # return 값은 fetchall 해야 나옴

for i in data:
    print(i)
# print(data)

'''
git add .    # 준비상태 
git commit -m 'message'   #진짜 추적 시
'''


if __name__ == '__main__':
    pass
