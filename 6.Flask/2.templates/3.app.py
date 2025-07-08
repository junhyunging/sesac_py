from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'name' : 'Alice','age':25,'mobile':'010-1234-5678'},
    {'name' : 'Bob','age':30,'mobile':'010-4564-5678'},
    {'name' : 'Charlie','age':35,'mobile':'010-3333-5678'}
]


@app.route("/")
def home():
    return render_template("index3.html", users=users) #우리의 Html 파일안에 이 names 라는 key에 users라는 값을 담아 보낼거다.

if __name__ == '__name__':
    app.run(debug=True)