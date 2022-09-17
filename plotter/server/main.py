import config
import network
from stepper import Stepper
import uasyncio as asyncio
from queue import Queue
from server import Server

def decode_cmd(cmd):
    s, l, r = cmd.split(',')
    steps = int(s)
    l_prd = int(l)
    r_prd = int(r)
    l_dir = 1
    if l_prd > 0:
        l_dir = 0
    r_dir = 1
    if r_prd > 0:
        r_dir = 0
    return steps, l_dir, abs(l_prd), r_dir, abs(r_prd)

async def processCmdQueue(q, stepper):
    while True:
        raw_cmd = await q.get()
        steps, l_dir, l_prd, r_dir, r_prd = decode_cmd(raw_cmd)
        stepper.move(steps, l_dir, l_prd, r_dir, r_prd)


async def main():
    # connect to wifi access point
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
    print(sta.ifconfig())

    stepper = Stepper()

    q = Queue()

    asyncio.create_task(processCmdQueue(q, stepper))

    server = Server(q)
    await server.run()

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()  # Clear retained state
