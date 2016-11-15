from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
basedir = path.abspath(path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + path.join(basedir, 'todo.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY']="JIKEXUEYUAN"
db = SQLAlchemy(app)

from app import views, models