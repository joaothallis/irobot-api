from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note
import time

backend = Bluetooth('iRobot-06C2ACFB22E5481198A7D9')
robot = Root(backend)

@event(robot.when_play)
async def walk(robot):
    while True:
        print('walk')
        await robot.move(100)
        exit()


@event(robot.when_bumped, [True, True])
async def talk(robot):
    while True:
        print('talk')
        await robot.say("It's a beautiful day in the neighborhood")


print("Start executing")
robot.play()

