import mysql.connector as mysql_con

'''
SELECT

# ip_addr을 기준으로 오름차순으로 정렬
SELECT * FROM user_info ORDER BY ip_addr DESC; # or ASC
SELECT * FROM user_info;

UPDATE <table> SET <field>=<value> WHERE id=1;

DELETE FROM <table> WHERE id=1;

rename table <old table name> to <new table name>
'''

'''
* 트리거 예시 *

# update_trg_hda_note_history 트리거가 없으면 만들고
CREATE TRIGGER IF NOT EXISTS update_trg_hda_note_history
# note_info 테이블이 UPDATE 되었다면
# note_info 테이블에서 10개의 데이터가 갱신되었다면 각 row마다 BEGIN~END 쿼리를 실행 (FOR EACH ROW 문으로 인하여)
    AFTER
        UPDATE
    ON note_info
    FOR EACH ROW
# BEGIN ~ END : 트리거가 실행할 쿼리문
BEGIN
    INSERT INTO hda_note_history
        (hda_key_id, note, registration_datetime, hda_version)
    VALUES (
        new.hda_key_id,
        (SELECT note FROM note_info WHERE note_info.hda_key_id = new.hda_key_id),
        (SELECT DATETIME('now', 'localtime')),
        (SELECT version FROM hda_info WHERE hda_info.hda_key_id = new.hda_key_id)
    );
END;
'''

con = mysql_con.connect(
    host='127.0.0.1', user='root', passwd='', database='dummy_db')

cur = con.cursor()

insert_q = """ 
INSERT INTO user_info (name, addr, ip_addr, birth) 
VALUES (%s, %s, %s, %s)
"""

delete_q = """
DELETE FROM user_info WHERE name=%s AND addr=%s;
"""

update_q = """
UPDATE user_info SET birth=%s WHERE id={0};
""".format(4300)

select_q = """
SELECT * FROM user_info ORDER BY name DESC;
"""

'''
INSERT INTO <table> (<fields...>) VALUES (<values...>);
'''

'''
git add .
git commit -m "message"
'''

# try:
#     # cur.execute(insert_q, ('aaaa', 'bbbb', 'cccc', '1999/10/10'))
#     # cur.execute(delete_q, ('aaaa', 'bbbb'))
#     # cur.execute(update_q, ('2002/05/15',))
#     con.commit()
#     print('success query!')
# except Exception as err:
#     con.rollback()
#     print('failed query!', err)

cur.execute(select_q)
data = cur.fetchall()

for l in data:
    print(l)