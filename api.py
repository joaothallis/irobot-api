from flask import Flask, render_template, request
from flask_restx import Resource, Api
import subprocess
import signal
import time

app = Flask(__name__)
app.config['STATIC_FOLDER'] = '/static'
app.static_folder = 'static'
api = Api(app,
          version='0.1',
          title='Robot Controller',
          description='API for controlling iRobot Create 3')


@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action0') == 'beep':
            return play()
        elif request.form.get('action1') == 'up':
            return move()
    elif request.method == 'GET':
        return render_template('index.html')


def play():
    print('Executing play')
    subprocess.Popen(["pdm", "run", "touch_music.py"], cwd=r'examples')
    print('Successfully executed play')
    return render_template('index.html')


def move():
    print('Executing move')
    subprocess.Popen(["pdm", "run", "move.py"], cwd=r'examples')
    return render_template('index.html')


@api.route("/play")
class Play(Resource):

    def get(self):
        process = subprocess.Popen(["pdm", "run", "touch_music.py"],
                                   cwd=r'examples')
        time.sleep(15)
        print("Sending CTRL-C signal")
        process.send_signal(signal.SIGINT)
        print("Waiting for CTRL-C")
        process.wait()
        return "Success"


if __name__ == "__main__":
    app.run(debug=True)
