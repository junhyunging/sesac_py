import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    # dict로 변환
    conn.row_factory = sqlite3.Row
    return conn

# 1-1 유저정보 다 가져오기
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    
    return users