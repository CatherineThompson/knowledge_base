import config
import network
import stepper 
import uasyncio as asyncio
from queue import Queue
from server import Server
import time

def decode_cmd(cmd):
    c = cmd.split(',')
    left = int(c[0])
    right = int(c[1])
    length = int(c[2])
    return  left, right, length

async def processCmdQueue(q, leftStepper, rightStepper):
    while True:
        raw_cmd = await q.get()
        left, right, length = decode_cmd(raw_cmd)
        left_dir = 1
        if left > 0:
            left_dir = 0
        right_dir = 1
        if right > 0:
            right_dir = 0
        leftStepper.move(left_dir, left)
        rightStepper.move(right_dir, right)

        time.sleep(length)

        leftStepper.stop()
        rightStepper.stop()

async def main():
    # connect to wifi access point
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
    print(sta.ifconfig())

    leftStepper = stepper.Stepper(config.LEFT_STEP_PIN, config.LEFT_DIR_PIN, config.STEP_DELAY_MS, )
    rightStepper = stepper.Stepper(config.RIGHT_STEP_PIN, config.RIGHT_DIR_PIN, config.STEP_DELAY_MS)

    q = Queue()

    asyncio.create_task(processCmdQueue(q, leftStepper, rightStepper))

    server = Server(q)
    await server.run()

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()  # Clear retained state
