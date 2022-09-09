import config
import network
import stepper 
import uasyncio as asyncio
from queue import Queue
from server import Server
import time

def decode_cmd(cmd):
    l, r, d = cmd.split(',')
    left_freq = abs(int(l))
    right_freq = abs(int(r))
    dur_ms = int(d)
    left_dir = 1
    if int(l) > 0:
        left_dir = 0
    right_dir = 1
    if int(r) > 0:
        right_dir = 0
    return left_freq, left_dir, right_freq, right_dir, dur_ms

async def processCmdQueue(q, leftStepper, rightStepper):
    while True:
        raw_cmd = await q.get()
        left_freq, left_dir, right_freq, right_dir, dur_ms = decode_cmd(raw_cmd)

        leftStepper.move(left_dir, left_freq)
        rightStepper.move(right_dir, right_freq)

        time.sleep_ms(dur_ms)

        leftStepper.stop()
        rightStepper.stop()

        time.sleep_ms(500)

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
