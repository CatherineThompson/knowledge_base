import config
# import network
import stepper 
# import uasyncio as asyncio
# from queue import Queue
# from server import Server
import time
from machine import PWM, Pin

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
