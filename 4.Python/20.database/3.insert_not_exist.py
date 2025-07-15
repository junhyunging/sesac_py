import sqlite3

#DB 연결
conn = sqlite3.connect('example.db')

#커서 객체 생성
cur = conn.cursor()

#--------------------------------

#데이터를 조회한다.
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]
print(count)

if count == 0: #아무도 없다면

    #데이터 삽입
    cur.execute('''
        INSERT INTO users (name,age) VALUES('Alice',30)
                ''')

    cur.execute('''
        INSERT INTO users (name,age) VALUES('Bob',25)
                ''')

    cur.execute('''
        INSERT INTO users (name,age) VALUES(?,?)
                ''',{'Charlie',40})
else:
    print("이미 데이터가 삽입 되어있음")
    #-------------------------



#커밋하여 변경사항 저장
conn.commit()

#DB 연결을 통로
conn.close()