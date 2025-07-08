from flask import Flask, render_template, request

app = Flask(__name__)

# 더미 유저 100명 생성
users = [
    { 'id': i, 'name': f'User{i}', 'age': 20+i % 10, 'phone': f'010-0000-{str(i).zfill(4)}'} for i in range (1, 101)
]

@app.route('/')
def all_users():
     return render_template('users2.html', users=users, page=None)
    
@app.route('/pages/<int:page>')
def index(page):
    person_page = 10
    start = (page - 1) * 10
    end = start + person_page
    paged_users = users[start:end]

    return render_template('users.html', users=paged_users, page=page)


if __name__ == "__main__":
    app.run(debug=True)