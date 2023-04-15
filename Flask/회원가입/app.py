import os
from flask import Flask, render_template, request, redirect, current_app
from models import db
from models import User

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/register', methods=['GET', 'POST'])        #GET(정보보기), POST(정보수정) 메서드 허용
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        userid = request.form.get('userid')
        email = request.form.get('email')
        password = request.form.get('password')
        password_2 = request.form.get('password')

        if not(userid and email and password and password_2):
            return "입력되지 않은 정보가 있습니다"
        elif password != password_2:
            return "비밀번호가 일치하지 않습니다"
        else:
            usertable = User()      #user_table 클래스
            usertable.userid = userid
            usertable.email = email
            usertable.password = password

            db.session.add(usertable)
            db.session.commit()
            return "회원가입 성공"
        return redirect('/')



if __name__ == '__main__':
    # 데이터베이스 ----
    basedir = os.path.abspath(os.path.dirname(__file__))    # 현재 파일이 있는 디렉토리 절대 경로
    dbfile = os.path.join(basedir, 'db.sqlite')             # 데이터베이스 파일 생성

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile    # 내가 사용할 DB URI
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True      # 비즈니스 로직이 끝날 때 Commit 실행(DB 반영)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # 수정사항에 대한 TRACK

    with app.app_context(): # Models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣는다
        db.init_app(app)    # app설정값 초기화
        db.create_all()     # DB 생성

    app.run(host="127.0.0.1", port=5000, debug=True)


