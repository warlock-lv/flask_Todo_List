# !/usr/bin/env python
# coding:    utf-8
# ----------------------------------------------
# Author:    warlock
# Email:     457880341@qq.com
# Time:      2017-10-22 20:58
# Software:  PyCharm Pro Edition 4.5
# Description:   
# ----------------------------------------------

from app import app
from flask import render_template, request
from app.models import Todo, TodoForm
from datetime import datetime


@app.route('/')
def index():
    form = TodoForm()
    #todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)


@app.route('/add', methods=['POST', 'GET'])
def add():
    # form = request.form
    # content = form['content']
    # print(content)
    # todo = Todo(content=content)
    # todo.save()
    # todos = Todo.objects.all()

    form = TodoForm(request.form)
    if form.validate():
        content = form.content.data
        todo = Todo(content=content, time=datetime.now()  )
        todo.save()
        form.content.data = ''
    # todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)


@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    # todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)


@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    # todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    # todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    pass
