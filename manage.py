# !/usr/bin/env python
# coding:    utf-8
# ----------------------------------------------
# Author:    warlock
# Email:     457880341@qq.com
# Time:      2017-10-22 20:56
# Software:  PyCharm Pro Edition 4.5
# Description:   此文件用来管理应用的外部脚本
# ----------------------------------------------


from app import app

from app.models import Todo
from flask_script import Manager

manager = Manager(app)


@manager.command
def save():
    todo = Todo(content='study flask 3')
    todo.save()





if __name__ == '__main__':
    manager.run()
