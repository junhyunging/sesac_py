from flask import Flask,jsonify,url_for,request,send_from_directory
# form flask_cors improt CORS
#pip install flask-cors

app = Flask(__name__)

# CORS(app) #나의 서버에 누구든지 와서 정보를 요청할수 있음.

images = [
   {"filename":"다운로드.jpg","keywords":["racon","animal","cute"]},
   {"filename":"라쿤.jpg","keywords":["racon","pet","cute"]},
]

@app.route("/")
def index():
    return send_from_directory(app.static_folder,"index.html")

@app.route("/api/search")
def search():
    query = request.args.get("q","").lower()
    result = []
    
    for item in images:
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static',filename=f'img/{item["filename"]}')
            result.append(image_url)
            
    
    return jsonify({"url": result})

if __name__ == "__main__":
    app.run(debug=True)