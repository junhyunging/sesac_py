# <!-- restapi로 미리보기,파일명,키워드,삭제하기 -->
from flask import Flask,jsonify,url_for,request,send_from_directory, redirect
import os

app = Flask(__name__)

images = [
   {"filename":"다운로드.jpg","keywords":["racon","animal","cute"]},
   {"filename":"라쿤.jpg","keywords":["racon","pet","cute"]},
]

@app.route('/')
def index():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)
    return send_from_directory(app.static_folder,"index.html")

@app.route("/api/upload", methods=["POST"])
def upload():
    file = request.files.get('image')
    keywords = request.form.get('keywords')
    print(keywords)
    
    if file:
        filename = file.filename
        filepath = os.path.join('static', 'img', filename)
        file.save(filepath)
        images.append({'filename': filename, "keywords": keywords.lower().split(',')})
    return send_from_directory(app.static_folder, "admin.html")
    
@app.route("/api/delete/<filename>", methods=["DELETE"])
def delete_image(filename):
    print('삭제할파일: ', filename)
    global images  
    images = [
        img 
        for img in images 
        if img["filename"] != filename
    ]
    filepath = os.path.join('static', 'img', filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    
    return redirect(url_for('admin'))

@app.route("/admin")
def admin():
    return send_from_directory(app.static_folder, "admin.html")

@app.route("/api/update/<filename>", methods=["PUT"])
def update_keywords(filename):
    new_keywords = request.form.get('keywords')
    for i in images:
        if i["filename"] == filename:
            i["keywords"] = [word.strip() for word in new_keywords.lower().split(',') if len(word.strip())]
            break
            
    return redirect(url_for('admin'))


    

if __name__ == "__main__":
    app.run(debug=True)