from flask import Flask,send_file, jsonify
# from flask_cors import CORS
#여기다가 cors라이브러리를 추가해서 해결, 프런트엔드를 내가 서빙

app = Flask(__name__)
# CORS(app)

@app.route("/")
def index():
    return send_file("2.fetch.html")

@app.route("/data")
def data():
    return jsonify({'result':'안녕하세요, 반갑습니다.'})

if __name__ == "__main__":
    app.run(debug=True)