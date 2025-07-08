from flask import Flask,request

app = Flask(__name__)

@app.route("/search") # /search?q=apple&page =2
def home():
    #사용자가 입력한 다양한 쿼리 파라미터를 처리하는것
    query = request.args.get('q')
    page = request.args.get('page',default=1,type=int) #query구문이 없어도 기본값 1 보내기
    
    print(query,page)
    
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)
    
    