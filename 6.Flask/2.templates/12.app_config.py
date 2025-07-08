from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
# ALLOWED_FILE_EXT = ['png','jpg','jpeg','gif'] #set - 유니크한 리스트 (위와 리스트와 기능은 동일함)
ALLOWED_FILE_EXT = {'png','jpg','jpeg','gif'} #set - 유니크한 리스트 (위와 리스트와 기능은 동일함)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) #시작할때 폴더가 없으면 만들어주기 있으면 오케이~

def allowed_file(filename):
    #파일명에 . 이 있는지 확인한다.
    if '.' not in filename:
        return False
    
    #확장자 파트를 오른쪽부터 읽어서 찾아낸다.
    ext = filename.rsplit('.',1)[1].lower()
    
    # 확장자가 우리의 허용목록에 있는지 확인한다.
    if ext in ALLOWED_FILE_EXT:
        return True
    else:
        return False
    
def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_FILE_EXT

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template("uploaddelet.html", files=files)

@app.route('/delete',methods=['POST'])
def delete_file():
    filename = request.form.get("filename")
    filepath = os.path.join('./',app.config['UPLOAD_FOLDER'],filename)
    os.remove(filepath)
    return redirect(url_for('index'))

@app.route('/upload',methods=['POST'])
def upload_file():
    # print(request.form) #이전에 받아온건 파일명만을 받아왔음.
    print(request.files) #실제로 파일 내용까지 FileStorage라는 객체 형태로 파일 내용을 가죠옴
    
    file = request.files['file']
    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'
    
    #비즈니스 로직 - 내가 정한 프로세싱 룰들을 여기에 하나둘씩 구현
    
    #2.용량을 보고 크기가 1MB큰거
    
        
    # 1. 사진 파일만 업로드 가능하게 한다.
    #확장자를 본다 - jpg, jpeg,png,gif 등등..
    if allowed_file(file.filename):
        #파일 저장하기 - 현재폴더의 uploads 안에 받은 파일명으로 저장하기
        filepath = os.path.join('./',app.config['UPLOAD_FOLDER'],file.filename)
        file.save(filepath)
        # return "파일 업로드 성공"
        return redirect(url_for('index'))
    else:
        return "허용되지 않는 파일입니다."

#오류메세지를 커스텀으로 등록한다.    
@app.errorhandler(413)
def too_large(e):
    size_mb = app.config['MAX_CONTENT_LENGTH'] / (1024 * 1024)
    return f"업로드한 파일이 너무 큽니다. 최대{size_mb}MB까지만 허용합니다."

if __name__ == '__main__':
    app.run(debug=True)
    
# 미션1. 파일 목록을 보여준다 (메인 라우트에서 uploads폴더안의 파일명을 보여준다)
# 미션1-2. 각각의 파일명 옆에 '삭제'버튼을 추가한다.
# 미션2. 실제로 해당 파일을 삭제한다.
  