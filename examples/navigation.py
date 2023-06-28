#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021-2022 iRobot Corporation. All rights reserved.
#

# Very basic example for avoiding front obstacles.

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

robot = Create3(Bluetooth("iRobot-06C2ACFB22E5481198A7D9"))
speed = 10
th = 150


async def forward(robot):
    await robot.set_lights_rgb(0, 255, 0)
    await robot.set_wheel_speeds(speed, speed)


async def backoff(robot):
    await robot.set_lights_rgb(255, 80, 0)
    await robot.move(-20)
    await robot.turn_left(45)


@event(robot.when_bumped, [True, True])
async def bumped(robot):
    await robot.move(-10)
    await robot.turn_right(45)
    await forward(robot) 
    replay(robot)


@event(robot.when_bumped, [True, False])
async def bumped(robot):
    await robot.move(-10)
    await robot.turn_right(45)
    await forward(robot) 
    replay(robot)


@event(robot.when_bumped, [False, True])
async def bumped(robot):
    await robot.move(-10)
    await robot.turn_right(45)
    await forward(robot) 
    replay(robot)
    
def front_obstacle(sensors):
    return sensors[3] > th


def left_obstacle(sensors):
    return sensors[2] > th


def right_obstacle(sensors):
    return sensors[4] > th


@event(robot.when_play)
async def play(robot):
    await forward(robot)
    while enabled():
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await backoff(robot)
            await forward(robot)
        if left_obstacle(sensors):
            await backoff(robot)
            await forward(robot)
        if right_obstacle(sensors):
            await backoff(robot)
            await forward(robot)

async def replay(robot):
    while enabled():            
        sensors = (await robot.get_ir_proximity()).sensors
        if front_obstacle(sensors):
            await backoff(robot)
            await forward(robot)
        if left_obstacle(sensors):
            await backoff(robot)
            await forward(robot)
        if right_obstacle(sensors):
            await backoff(robot)
            await forward(robot)

def enabled():
    f = open("../run", "r")
    run = f.read()
    if "true" in run:
        return True
    else:
        exit()


robot.play()
