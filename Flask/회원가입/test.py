# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'hello world!'
#
#
# if __name__ == '__main__':
#     app.debug = True
#     app.run()

import os

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')