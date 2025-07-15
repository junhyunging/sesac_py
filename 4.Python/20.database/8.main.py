import db_crud_sqlite as db

def main():
    db.create_table()
    
    db.insert_user('Alice',30)
    db.insert_user('Bob',35)
    db.insert_user('Charlie',40)
    
    #데이터 조회
    print("데이터 목록" )
    users = db.get_users()
    for user in users:
        print(user)
        
    #데이터 업데이트
    db.update_user_age('Alice',24)
    
    #데이터 삭제
    db.delete_uesr_by_name('Bob')
    print('사용자 조회')
    
    print("데이터 목록" )
    users = get_users()
    for user in users:
        print(user)
        
    #데이터 삭제
    db.delete_uesr_by_age(30)
    print("데이터 목록" )
    users = db.get_users()
    for user in users:
        print(user)

    
    
if __name__ == '__main__':
    main()
    
