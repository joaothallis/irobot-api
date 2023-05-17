from flask import Flask
from flask_restx import Resource, Api
from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, Create3
from irobot_edu_sdk.music import Note

app = Flask(__name__)
api = Api(app)


@api.route("/play")
class Play(Resource):
    def get(self):
        robot = Create3(Bluetooth())
        duration = 0.50

        @event(robot.when_play)
        async def play(robot):
            await robot.play_note(Note.A4, duration)

        robot.play()


if __name__ == "__main__":
    app.run(debug=True)
