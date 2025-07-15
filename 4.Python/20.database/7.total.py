import sqlite3

MY_DATABASE = 'example.db'

#DB에 접속하는 함수를 작성하시오.

def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    return conn

#테이블 생성 함수를 작성하시오
def create_table():
    conn= connect_db()
    cur = conn.cursor()
    
    cur.execute('''
              CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL, 
                age INTEGER NOT NULL
                )
    ''')
    
    conn.commit()
    conn.close()
    

#데이터 삽입
def insert_user(name,age):

    conn=connect_db()
    cur = conn.cursor()
    
    cur.execute(
         "INSERT INTO users (name,age) VALUES(?,?)",(name,age)
    )
    
    conn.commit()
    conn.close()

#데이터 조회
def get_users():
    conn=connect_db()
    cur = conn.cursor()
    
    cur.execute(
        "SELECT * FROM users"
    )
    
    rows = cur.fetchall()
    
    conn.commit()
    conn.close()
    
    return rows


#데이터 업데이트함수
def update_user_age(name, new_age):
    conn=connect_db()
    cur = conn.cursor()
    
    cur.execute(
        "UPDATE users SET age=? WHERE name='?'",(new_age,name)
    )
    
    conn.commit()
    conn.close()

#삭제 함수
def delete_uesr_by_name(name):
    conn=connect_db()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM users WHERE name=?",(name,))
    
    conn.commit()
    conn.close()
    
def delete_uesr_by_age(age):
    conn=connect_db()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM users WHERE age=?",(age,))
    
    
    conn.commit()
    conn.close()


#메인 함수
def main():
    create_table()
    
    insert_user('Alice',30)
    insert_user('Bob',35)
    insert_user('Charlie',40)
    
    #데이터 조회
    print("데이터 목록" )
    users = get_users()
    for user in users:
        print(user)
        
    #데이터 업데이트
    update_user_age('Alice',24)
    
    #데이터 삭제
    delete_uesr_by_name('Bob')
    print('사용자 조회')
    
    print("데이터 목록" )
    users = get_users()
    for user in users:
        print(user)
        
    #데이터 삭제
    delete_uesr_by_age(30)
    print("데이터 목록" )
    users = get_users()
    for user in users:
        print(user)

    
    
if __name__ == '__main__':
    main()
    
