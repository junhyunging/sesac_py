from flask import Flask,render_template,redirect,request,url_for,session
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET")

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
NAVER_REDIRECT_URL = os.getenv("NAVER_REDIRECT_URL")

@app.route('/') 
def index():
    user = session.get('user')
    return render_template("index.html",user=user)

@app.route('/login/naver')
def login_naver():
    auth_url = (
        f"https://nid.naver.com/oauth2.0/authorize?"
        f"response_type=code&client_id={NAVER_CLIENT_ID}"
        f"&redirect_url={NAVER_REDIRECT_URL}&state=xyz"
    )
    return redirect(auth_url)

@app.route('/naver/callback') #네이버 인증 끝난 이후에 돌아올곳
def naver_callback():
    code = request.args.get('code') #서버가 인증 성공한 댓가로 준 값
    state = request.args.get('state') # 내 사이트에서 갓다온건지 확인용, 내가 보낸 글자
    
    token_url = (
        f"https://nid.naver.com/oauth2.0/token?"
        f"grant_type=authorization_code&client_id={NAVER_CLIENT_ID}"
        f"&client_secret={NAVER_CLIENT_SECRET}&code={code}&state={state}"
    )
    
    token_response = requests.get(token_url).json()
    print(token_response)
    access_token = token_response.get('access_token')
    #이제 사용자가 제대로 인증하고 온것 확인했으니, 나도 서버에게 해당 사용자의 정보를 달라고 하자.
    headers = {"Authorization":f"Bearer {access_token}"}
    profile = requests.get('https://openapi.naver.com/v1/nid/me', headers=headers).json()
    
    # TODO: 우리의 db에 이 사용자가 있는지 확인하고, 있으면 그 정보 가져와서 세션에 저장
    # 해당 사용자가 없으묜? 새롭게 DB에 삽입.
    # 이걸 더 확장하고 싶으면?? 사용자가 없으면, 그때 회원가입 페이지로 보내서 더 저장한다.
    
    
    session['user'] = profile['response']
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(debug=True)