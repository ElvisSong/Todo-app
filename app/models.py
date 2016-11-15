from app import db
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class Todo(db.Model):
    __tablename__= 'todo'
    id = db.Column(db.Integer,primary_key=True,)
    content = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    status = db.Column(db.Integer, default=False)

class TodoForm(Form):
    content = StringField("input your todo", validators=[DataRequired()])