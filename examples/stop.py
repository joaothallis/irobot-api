from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

backend = Bluetooth("iRobot-06C2ACFB22E5481198A7D9")
robot = Root(backend)


robot.disconnect()
