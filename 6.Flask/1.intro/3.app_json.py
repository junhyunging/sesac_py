from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'name' : 'Alice','age':25,'mobile':'010-1234-5678'},
    {'name' : 'Bob','age':30,'mobile':'010-4564-5678'},
    {'name' : 'Charlie','age':35,'mobile':'010-3333-5678'}
]

@app.route('/')
def index():
    return jsonify(users)

#소문자도 대문자도 다~~ 매칭하려면

@app.route('/user/<name>')
def get_user_by_name(name):
    #이름이 일치하는지
    # for/if 구문을 통해서, 입력받은 name이 실제로 위에 users에서 존재하는지 찾아서 user에 할당하기
    user = "Not Found"
    for i in len(users):
        if name.lower() == users['name'].lower(): 
            user = users[i]
            break
    # 만약 name에 숫자가 왔을때는, 나이로 검색을 하려면
    for u in users:
        if name == u['age']:
            user = u
            break
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404
    
@app.route('/user/<age>')
def get_user_by_age(age):
    user = None
    for u in users:
        if int(age) == u['age']: #함수의 인자값을 숫자로 바꾸거나, 또는 DB에 인자값을 문자열로 바꾸거나
            user = u
            break
    
        
if __name__ == "__name__":
    app.run(debug=True, port=5000)
    
    