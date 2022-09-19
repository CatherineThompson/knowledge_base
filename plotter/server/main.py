import config
import network
from stepper import Stepper
import uasyncio as asyncio
from queue import Queue
from server import Server
import time

RATIO_THRESHOLD = 30


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    print(wlan.ifconfig())


def decode_cmd(cmd):
    l, r = cmd.split(',')
    left_steps = abs(int(l))
    right_steps = abs(int(r))
    left_dir = 1
    if int(l) > 0:
        left_dir = 0
    right_dir = 1
    if int(r) > 0:
        right_dir = 0
    return left_steps, left_dir, right_steps, right_dir


def get_ratios(left_steps, right_steps):
    original_left_steps = left_steps
    original_right_steps = right_steps
    left_ratio = 1
    right_ratio = 1
    diff = abs(left_steps - right_steps)
    i = 0
    while diff > RATIO_THRESHOLD * (i**1.05):
        if left_steps < right_steps:
            left_ratio += 1
            left_steps = left_ratio * original_left_steps
        else:
            right_ratio += 1
            right_steps = right_ratio * original_right_steps
        diff = abs(left_steps - right_steps)
        i += 1
    return left_ratio, right_ratio


async def processCmdQueue(q, leftStepper, rightStepper):
    while True:
        raw_cmd = await q.get()
        cmds = raw_cmd.split("|")
        for cmd in cmds:
            if cmd == "":
               continue
            left_steps, left_dir, right_steps, right_dir = decode_cmd(cmd)

            leftStepper.dir(left_dir)
            rightStepper.dir(right_dir)

            left_ratio, right_ratio = get_ratios(left_steps, right_steps)
            print(f"Ratios: L({left_ratio}), R({right_ratio})")

            l = asyncio.create_task(leftStepper.move(left_steps, left_ratio))
            r = asyncio.create_task(rightStepper.move(right_steps, right_ratio))

            await l
            await r
            asyncio.sleep(1)


async def main():
    connect() # to wifi

    leftStepper = Stepper(config.LEFT_STEP_PIN, config.LEFT_DIR_PIN, config.LEFT_ENABLE_PIN, config.STEP_SIZE)
    rightStepper = Stepper(config.RIGHT_STEP_PIN, config.RIGHT_DIR_PIN, config.RIGHT_ENABLE_PIN, config.STEP_SIZE)

    q = Queue()

    asyncio.create_task(processCmdQueue(q, leftStepper, rightStepper))

    server = Server(q)
    await server.run()

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()  # Clear retained state
