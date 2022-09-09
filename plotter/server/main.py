import config
# import network
import stepper 
# import uasyncio as asyncio
# from queue import Queue
# from server import Server
import time
from machine import PWM, Pin

async def processCmdQueue(q, leftStepper, rightStepper):
    while True:
        motor = await q.get()
        dir = await q.get()
        m = leftStepper if motor == 'L' else rightStepper
        d = m.UP if dir == 'U' else m.DOWN
        m.step(d)

def stepper_demo():
    leftStepper = stepper.Stepper(config.LEFT_STEP_PIN, config.LEFT_DIR_PIN, config.LEFT_ENABLE_PIN, config.MAX_FREQ, config.STEP_SIZE)
    rightStepper = stepper.Stepper(config.RIGHT_STEP_PIN, config.RIGHT_DIR_PIN, config.RIGHT_ENABLE_PIN, config.MAX_FREQ, config.STEP_SIZE)

    leftStepper.move()
    rightStepper.move()

    time.sleep(5)

    leftStepper.stop()
    rightStepper.stop()

    time.sleep(5)

    leftStepper.move()
    rightStepper.move()

    time.sleep(5)

    leftStepper.stop()
    rightStepper.stop()

    
stepper_demo()

def pwm_demo():
    pwm1 = PWM(Pin(config.LEFT_STEP_PIN))
    pwm2 = PWM(Pin(config.RIGHT_STEP_PIN))
    # 50%
    pwm1.duty_u16(32768)
    pwm2.duty_u16(32768)

    pwm1.freq(int(config.MAX_FREQ / config.STEP_SIZE))
    pwm2.freq(int(config.MAX_FREQ / config.STEP_SIZE))

    time.sleep(5)

    pwm1.deinit()
    pwm2.deinit()

    time.sleep(5)

    pwm1.duty_u16(32768)
    pwm2.duty_u16(32768)

    pwm1.freq(int(config.MAX_FREQ / config.STEP_SIZE))
    pwm2.freq(int(config.MAX_FREQ / config.STEP_SIZE))
    
    time.sleep(5)

    pwm1.deinit()
    pwm2.deinit()

# pwm_demo()

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
