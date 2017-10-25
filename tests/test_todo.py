# !/usr/bin/env python
# coding:    utf-8
# ----------------------------------------------
# Author:    warlock
# Email:     457880341@qq.com
# Time:      2017-10-23 23:21
# Software:  PyCharm Pro Edition 4.5
# Description:   
# ----------------------------------------------

'''
    在Terminal 中切换到py3_env环境下
    并在 命令行中输入：
        python -m unittest discover   即执行测试用例。
        coverage run -m unittest discover
        coverage report    查看测试用例覆盖率
'''

import unittest
from app import app
from app.models import Todo


class TestCaseTodo(unittest.TestCase):

    def setUp(self):
        print('setup')
        self.app = app.test_client()

    def tearDown(self):
        todo = Todo.objects(content='testadd').first()
        if todo:
            todo.delete()

    def test_index(self):
        index = self.app.get('/')
        # print(type(index))          # <class 'flask.wrappers.Response'>
        # print(type(index.data))     # <class 'bytes'>
        assert 'Todo' in index.data.decode()    #decode() 的目的是将bytes 转为 str

    def test_add(self):
        self.app.post('/add', data=dict(content='testadd'))
        todo = Todo.objects.get_or_404(content='testadd')
        assert todo is not None










