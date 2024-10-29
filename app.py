from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

#
users = {}

@app.route('/')
def index():
        return render_template('index.html')

#
@socketio.on("connect")
def handle_connect():
        username = f"User_{random.randint(1000,9999)}"
        gender = random.choice(["girl","boy"])
        # https://avatar.iran.liara.run/public/boy?username=User_123
        avatar_url = f"https://avatar.iran.liara.run/public/{gender}?username={username}"

        users[request.sid] = {"username":username,"avatar":avatar_url}

        emit("user_joined", {"username":username,"avatar":avatar_url},broadcast=True)

        emit("set_username", {"username":username})

@socketio.on("disconnect")
def handle_disconnect():
        user = users.pop(request.sid, None)
        if user:
                emit("user_left", {"username":user["username"]},broadcast=True)




if __name__ == "__main__":
        socketio.run(app)