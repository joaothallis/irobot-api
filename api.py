from flask import Flask, render_template, request
from flask_restx import Resource, Api
import subprocess
import time

app = Flask(__name__, template_folder="./src/templates/")
app.config["STATIC_FOLDER"] = "./src/static"
app.static_folder = "./src/static"
api = Api(
    app,
    version="0.1",
    title="Robot Controller",
    description="API for controlling iRobot Create 3",
)


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("action0") == "beep":
            return play()
        elif request.form.get('action1') == 'move':
            return navigation()
        elif request.form.get("action2") == "left":
            return turn_left()
        elif request.form.get("action3") == "right":
            return turn_right()
        elif request.form.get("action4") == "down":
            return move_down()
        elif request.form.get('stop') == '':
            return stop()
    elif request.method == "GET":
        return render_template("index.html")


def play():
    print("Executing play")
    subprocess.Popen(["pdm", "run", "touch_music.py"], cwd=r"examples")
    print("Successfully executed play")
    return render_template("index.html")


def turn_left():
    stop()
    time.sleep(1)
    print("Executing turn left")
    subprocess.Popen(["pdm", "run", "turn_left.py"], cwd=r"examples")
    return render_template("index.html")


def turn_right():
    stop()
    time.sleep(1)
    print("Executing turn right")
    subprocess.Popen(["pdm", "run", "turn_right.py"], cwd=r"examples")
    return render_template("index.html")


def move_down():
    stop()
    time.sleep(1)
    print("Executing move down")
    subprocess.Popen(["pdm", "run", "move_down.py"], cwd=r"examples")
    return render_template("index.html")


def enable_run():
    f = open("run", "a")
    f.truncate(0)
    f.write("true")
    f.close()


def navigation():
    enable_run()
    print("Executing navigation")
    subprocess.Popen(["pdm", "run", "navigation.py"], cwd=r"examples")
    return render_template("index.html")


def stop():
    f = open("run", "a")
    f.truncate(0)
    f.write("false")
    f.close()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
