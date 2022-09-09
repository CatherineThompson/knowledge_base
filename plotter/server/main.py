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
    dur = int(c[2])
    return left, right, dur 

async def processCmdQueue(q, leftStepper, rightStepper):
    while True:
        raw_cmd = await q.get()
        left_freq, right_freq, dur_ms = decode_cmd(raw_cmd)
        left_dir = 1
        if left_freq > 0:
            left_dir = 0
        right_dir = 1
        if right_freq > 0:
            right_dir = 0
        leftStepper.move(left_dir, abs(left_freq))
        rightStepper.move(right_dir, abs(right_freq))

        time.sleep_ms(dur_ms)

        leftStepper.stop()
        rightStepper.stop()

async def main():
    # connect to wifi access point
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
    print(sta.ifconfig())

    leftStepper = stepper.Stepper(config.LEFT_STEP_PIN, config.LEFT_DIR_PIN, config.LEFT_ENABLE_PIN)
    rightStepper = stepper.Stepper(config.RIGHT_STEP_PIN, config.RIGHT_DIR_PIN, config.RIGHT_ENABLE_PIN)

    q = Queue()

    asyncio.create_task(processCmdQueue(q, leftStepper, rightStepper))

    server = Server(q)
    await server.run()

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()  # Clear retained state
