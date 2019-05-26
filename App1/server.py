from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'ThisIsMySecretKey'
socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatt.db'
db = SQLAlchemy(app)

class History(db.Model):
    id = db.Column('id',db.Integer,primary_key=True)
    message = db.Column('message',db.String(100),unique=False,nullable=False)
    author = db.Column('author',db.String(10),unique=False,nullable=False)
@app.route('/')
def chat():
    # messages = ['m1','m2','m3']
    messages = History.query.all()
    return render_template('chat.html',messages=messages)

@app.route('/login')
def login():
  return render_template('login.html')

@socketio.on('message', namespace='/chat')
def chat_message(message):
  print("message = ", message)
  msg = History(message=message['data']['message'],author=message['data']['author'])
  db.session.add(msg)
  db.session.commit()
  emit('message', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/chat')
def test_connect():
  emit('my response', {'data': 'Connected', 'count': 0})

if __name__ == '__main__':
  socketio.run(app)
