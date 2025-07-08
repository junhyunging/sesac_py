from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # name = request.args.get('name') # GET 파라미터(아규먼트) 를 받는
    name = request.form.get('name') #   POST로 form(폼)이 전달된거 안에서 name이 키인것을 주시오
    age = request.form.get('age') #   POST로 form이 전달된거 안에서 키가 age로 준거 주시오
    print(name)
    print(request.form)
    return f'안녕하세요 {age}세 {name}님'
    

if __name__ == '__main__':
    app.run(debug=True)
  