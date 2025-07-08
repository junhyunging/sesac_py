from flask import Flask, render_template ,request

app = Flask(__name__)

# 더미 유저 100명 생성
users = [
    { 'id': i, 'name': f'User{i}', 'age': 20+i % 10, 'phone': f'010-0000-{str(i).zfill(4)}'} for i in range (1, 101)
]

#페이징 처리 get파라미터로 10개씩 보여주고 next previous 버튼을 만들어서 페이지 넘길수 있도록

# http://localhost:5000/?pages=1
@app.route('/')
def index():
    page = request.args.get('pages', type=int)
    
    if page:
        person_page = 10
        start = (page -1) * 10
        end = start + person_page
        paged_users = users[start:end]

        return render_template('users.html', users=paged_users, page=page)
    else:
        return render_template('users.html', users=users)


if __name__ == "__main__":
    app.run(debug=True)