from flask import Flask, render_template
import database as db

app = Flask(__name__)

#사용자 정보 가져오기
@app.route("/")
def get_user():
    users = db.get_users()
    return render_template('user.html',users=users)
    

if __name__ == "__main__":
    app.run(debug=True)

