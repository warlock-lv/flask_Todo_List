# !/usr/bin/env python
# coding:    utf-8
# ----------------------------------------------
# Author:    warlock
# Email:     457880341@qq.com
# Time:      2017-10-22 20:57
# Software:  PyCharm Pro Edition 4.5
# Description:   
# ----------------------------------------------


from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

from app import views, models



if __name__ == '__main__':
    pass
