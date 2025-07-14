from flask import Flask,render_template,jsonify,url_for
import random

app = Flask(__name__)

dog_images = [
   "다운로드.jpg",
   "라쿤.jpg",
]

@app.route("/random-dog")
def random_dog():
    random_img = random.choice(dog_images)
    # immage_url = url_for('static',filename=f'img/{random_img}') # 상대경로가 만들어짐
    immage_url = url_for('static',filename=f'img/{random_img}', _external=True) # 절대경로 만들기
    return jsonify({"url": immage_url})

if __name__ == "__main__":
    app.run(debug=True)