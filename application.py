import os


from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

username = None
error = None


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("login.html", error=error)
    else:
        username = request.form.get("username")
        if len(username) == 0:
            return render_template("login.html",
                                   error="Please, add a username.")
        # need saving to local storage
        return render_template("chat.html", username=username)
