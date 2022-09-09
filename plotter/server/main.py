import config
# import network
import stepper 
# import uasyncio as asyncio
# from queue import Queue
# from server import Server
import utime

async def processCmdQueue(q, leftStepper, rightStepper):
    while True:
        motor = await q.get()
        dir = await q.get()
        m = leftStepper if motor == 'L' else rightStepper
        d = m.UP if dir == 'U' else m.DOWN
        m.step(d)

def pio_demo():
    leftStepper = stepper.Stepper(config.LEFT_STEP_PIN, config.LEFT_DIR_PIN, config.LEFT_ENABLE_PIN, 0)
    rightStepper = stepper.Stepper(config.RIGHT_STEP_PIN, config.RIGHT_DIR_PIN, config.RIGHT_ENABLE_PIN, 5)

    leftStepper.move(100000, 0)
    rightStepper.move(100000, 0)

    utime.sleep(10)

    leftStepper.move(50000, 0)
    rightStepper.move(50000, 0)

    utime.sleep(10)

    leftStepper.stop()
    rightStepper.stop()

    utime.sleep(2)

    leftStepper.move(50000, 1)
    rightStepper.move(50000, 1)

    utime.sleep(10)

    leftStepper.stop()
    rightStepper.stop()

    
pio_demo()

# async def main():
    # connect to wifi access point
    # sta = network.WLAN(network.STA_IF)
    # sta.active(True)
    # sta.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
    # print(sta.ifconfig())

    # leftStepper = stepper.Stepper(config.LEFT_STEP_PIN, config.LEFT_DIR_PIN, config.STEP_DELAY_MS, True)
    # rightStepper = stepper.Stepper(config.RIGHT_STEP_PIN, config.RIGHT_DIR_PIN, config.STEP_DELAY_MS)

    # q = Queue()

    # asyncio.create_task(processCmdQueue(q, leftStepper, rightStepper))

    # server = Server(q)
    # await server.run()

# try:
#     asyncio.run(main())
# finally:
#     asyncio.new_event_loop()  # Clear retained state
