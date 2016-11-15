from app import app, db
from flask import render_template, request
from models import Todo, TodoForm
from datetime import datetime

@app.route('/')
def index():
    form = TodoForm()
    todos = Todo.query.order_by(Todo.time.desc())
    return render_template('index.html',todos = todos, form=form)

@app.route('/add', methods=["POST",])
def add():
    form = TodoForm(request.form)
    if form.validate_on_submit():
        content = form.content.data
        todo = Todo(content=content, time=datetime.now())
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.order_by(Todo.time.desc())
    return render_template("index.html", todos=todos, form=form)

@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = TodoForm()
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.status=True
    db.session.add(todo)
    db.session.commit()
    todos = Todo.query.order_by(Todo.time.desc())
    return render_template("index.html", todos=todos, form=form)

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = TodoForm()
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.status=False
    db.session.add(todo)
    db.session.commit()
    todos = Todo.query.order_by(Todo.time.desc())
    return render_template("index.html", todos=todos, form=form)

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoForm()
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    todos = Todo.query.order_by(Todo.time.desc())
    return render_template("index.html", todos=todos, form=form)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")
