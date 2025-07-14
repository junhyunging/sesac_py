from flask import Flask,render_template, request, redirect, url_for

app = Flask(__name__)

# 미션1. 사용자 목록 완성
# 미션2. 로그인할때 사용자 ID/PW 맞는지 체크
# 미션3. 맞으면 로그인성공인거니 성공페이지로 이동 (안녕하세요 OOO님)
# 실패시, 로그인 실패라고 출력
# 사용자 목록

users = [
    # 여기 사용 이름, 아이디, 암호를 3명이상의 사용자를 여기에 넣고
    {"name":"아무개", "id":"dkanro", "pw":"1234"},
    {"name":"신준형", "id":"shin", "pw":"1234"},
    {"name":"무지개", "id":"mu", "pw":"1234"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        #POST 에 대한 처리
        id = request.form["id"]
        pw = request.form["pw"]
        
        for user in users:
            if user["id"] == id and user["pw"] == pw:
                user=user
        return redirect(url_for("user",user=user["name"]))
        # return render_template('user.html',user=user)
    else:
        #POST가 아닐때에 대한 처리 => GET일때의 처리
        return render_template('login.html')

@app.route('/user/<user>')
@app.route('/user')
def user(user=None): #초기값 할당
    return render_template('user.html',user=user)
    
@app.route('/product')
def product():
    return render_template('product.html')

if __name__ == '__main__':
    app.run(debug=True)