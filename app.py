from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

users = {}

@app.route('/')
def index():
        return render_template('index.html')

@socketio.on("connect")
def handle_connect():
        username = f"User_{random.randint(1000,9999)}"
        gender = random.choice(["girl","boy"])
        # https://avatar.iran.liara.run/public/boy?username=User_123
        avatar_url = f"https://avatar.iran.liara.run/public/{gender}?username={username}"

        users[request.sid] = {"username":username,"avatar":avatar_url}

if __name__ == "__main__":
        socketio.run(app)