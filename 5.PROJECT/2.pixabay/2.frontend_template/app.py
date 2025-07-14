from flask import Flask,render_template,jsonify,url_for,request
import random

app = Flask(__name__)

images = [
   {"filename":"다운로드.jpg","keywords":["racon","animal","cute"]},
   {"filename":"라쿤.jpg","keywords":["racon","pet","cute"]},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q","").lower()
    result = []
    
    for item in images:
        # found = False
        # for keyword in item["keywords"]:
        #     if query in keyword:
        #         found = True
        #         # break #이미지 하나만 찾고 말거다 break
        # if found:
        #     image_url = url_for('static',filename=f'img/{item["filename"]}')
        #     result.append(image_url)
        
        # 한줄로
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static',filename=f'img/{item["filename"]}')
            result.append(image_url)
            
    
    # return jsonify({"url": result})
    return render_template("results.html", query=query, results=result)

if __name__ == "__main__":
    app.run(debug=True)