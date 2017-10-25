# !/usr/bin/env python
# coding:    utf-8
# ----------------------------------------------
# Author:    warlock
# Email:     457880341@qq.com
# Time:      2017-10-22 20:58
# Software:  PyCharm Pro Edition 4.5
# Description:   
# ----------------------------------------------

from app import db
import datetime
from flask_mongoengine.wtf import model_form


class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)

TodoForm = model_form(Todo)

if __name__ == '__main__':
    pass
    print(datetime.datetime.now())
