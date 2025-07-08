from flask import Flask, render_template ,request

app = Flask(__name__)

users = [
    {'name' : 'Alice','age':25,'mobile':'010-1234-5678'},
    {'name' : 'Bob','age':30,'mobile':'010-4564-5678'},
    {'name' : 'Charlie','age':35,'mobile':'010-3333-5678'}
]

#미션1. 사용자 목록을 테이블로 그린다
#<table border="1"> <tr> <td>
# 미션2. 입력폼을 하나 만들고, 사용자 이름으로 원하는 사용자만 골라낸다

#? <-- url에서 

@app.route("/")
def home():
    # 아까 배운 파라미터 처리하는 코드
    name = request.args.get('name')
    filtered_users = users
    # for u in users:
    #     if u['name'].lower() == name:
    #         filtered_users = [u]
    #         break
    
    if name:
        filtered_users = [u for u in users if u['name'].lower() == name.lower()]
    
    return render_template("index4.html", users=filtered_users) #우리의 Html 파일안에 이 names 라는 key에 users라는 값을 담아 보낼거다.


if __name__ == '__main__':
    app.run(debug=True)