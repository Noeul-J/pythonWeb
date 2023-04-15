from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 사용자의 username과 password를 input으로 받는다
# form action을 통해 login_check로 redirect 한다.


@app.route('/')
def login():
    return render_template('login.html')

# 사용자의 입력이 admin/admin123이 맞는지 확인한다.
# 맞으면 '환영합니다' 아니면 '관리자가 아닙니다'
# 라고 출력한다.


@app.route('/login_check')
def login_check():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == 'admin' and password == 'admin123':
        message = '환영합니다'
    else :
        message = '관리자가 아닙니다'

    return render_template('login_check.html', message=message)


# app.py 파일이 'python app.py'로 시작되었을 때 서버를 시작하겠다 라는 의미
if __name__ == '__main__':
    app.run(debug=True)
    # 서버가 실행이 되어있는동안 수정이 되면 자동으로 재시작을 하겠다 라는 의미

