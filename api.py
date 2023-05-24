from flask import Flask
from flask_restx import Resource, Api
import subprocess
import signal
import time

app = Flask(__name__)
api = Api(app)


@api.route("/play")
class Play(Resource):

    def get(self):
        process = subprocess.Popen(["pdm", "run", "touch_music.py"])
        time.sleep(15)
        print("Sending CTRL-C signal")
        process.send_signal(signal.SIGINT)
        print("Waiting for CTRL-C")
        process.wait()
        return "Success"


if __name__ == "__main__":
    app.run(debug=True)
