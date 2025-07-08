from flask import Flask

app = Flask(__name__)

@app.route('/') # 사용자가 /에 접속하면, 이 아래 함수를 호출해줘
def home():
    return "<h1>Hello, Flask!</h1>"

@app.route('/user/<username>') 
def greet_user(username):
    return f"<h1>Hello, {username}!</h1>"

@app.route('/user/<int:age>') #내가 따로 정의하지 않으면 문자열임 . 그래서 바꾸고 싶으면 타입을 정해야함
def greet_age(age):  # 위에 flask 데코레이터에서 정한 변수명 <변수명> 으로 함수 인자로 전달
    return f"<h1>Hello, {age}!</h1>" #서버 사이드 랜더링.. (서버에서 필요한 HTML을 랜더링)

@app.route('/user/<float:weight>') 
def greet_weight(weight):
    if weight > 60:
        message = "뚱뚱한"
    elif weight < 40:
        message = "날씬한"
    else:
        message = ""
    return f"<h1>Hello, {weight}는 {message}!</h1>" 

@app.route('/user/<name>/<int:age>/<float:weight>')
def greet_user_with_detail(name,age,weight):
    return f"<h1>안녕하세요</h1> <h2>사용자정보</h2> <ul><li>이름:{name}</li> <li>나이:{age}</li> <li>몸무게{weight}</li></ul>"
@app.route('/product')
def product():
    return "<h1>Hello, Product!</h1>"


if __name__ == '__main__':
    print("여기가 메인 함수")
    app.run(debug=True) #절대로 이대로 커밋하면 안됨 !! 꼭 끈 다음에 커밋해야함.
    


    
    