from flask import Flask, render_template ,request

app = Flask(__name__)

users = [
    {'name' : 'Alice','age':25,'phone':'010-1234-5678'},
    {'name' : 'Bob','age':30,'phone':'010-4564-5678'},
    {'name' : 'Charlie','age':35,'phone':'010-3333-5678'}
]

#미션1. 사용자 목록을 테이블로 그린다
#<table border="1"> <tr> <td>
# 미션2. 입력폼을 하나 만들고, 사용자 이름으로 원하는 사용자만 골라낸다

#? <-- url에서 

@app.route("/")
def home():
    # 아까 배운 파라미터 처리하는 코드
    name = request.args.get('name')
    age = request.args.get('age',type=int)
    phone = request.args.get('phone')
    filtered_users = users 
    
        
    if name:
        filtered_users = [u for u in filtered_users if name.lower() == u['name'].lower()]
        
    if age:
        filtered_users = [u for u in filtered_users if int(age) == u['age']]   
    
    if phone:
        #in을 사용해서 일부 매칭하기
        filtered_users = [u for u in filtered_users if phone in u['phone']]  
        
           
    return render_template("index5.html", users=filtered_users)

if __name__ == '__main__':
    app.run(debug=True)