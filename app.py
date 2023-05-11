from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
path = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(100))
  complete = db.Column(db.Boolean)

@app.route('/')
def list():
  todo_list = Todo.query.all()
  return render_template('list.html', todo_list = todo_list)

@app.route('/edit')
def home():
  todo_list = Todo.query.all()
  return render_template('base.html', todo_list = todo_list)

@app.route('/add', methods=['POST'])
def add():
  title = request.form.get('title')
  new_todo = Todo(title = title, complete = False)
  db.session.add(new_todo)
  db.session.commit()
  return redirect(url_for('home'))

@app.route('/update/<int:todo_id>')
def update(todo_id):
  todo = Todo.query.filter_by(id = todo_id).first()
  todo.complete = not todo.complete
  db.session.commit()
  return redirect(url_for('home'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
  todo = Todo.query.filter_by(id = todo_id).first()
  db.session.delete(todo)
  db.session.commit()
  return redirect(url_for('home'))

@app.route('/hi')
def hi():
  return 'Hi everyone'

@app.route('/dummy')
def dummy():
  return render_template('dummy.html')

with app.app_context():
  db.create_all()
  # create a default 'Project' to do
  default_todo = Todo(title = 'Project', complete = False)
  db.session.add(default_todo)
  db.session.commit()

if __name__ == '__main__':
  app.run(debug = True)
