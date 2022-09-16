import config
# import network
from stepper import Stepper
# import uasyncio as asyncio
# from queue import Queue
# from server import Server
import time
from machine import Pin
# import demos

def main():
    stepper = Stepper(config.LEFT_STEP_PIN, config.LEFT_DIR_PIN, config.LEFT_ENABLE_PIN, config.STEP_SIZE)
    stepper.move(1000)

main()

# demos.accel_demo()

# max freq = 3400
# total_steps = 100
# acc_dec_steps = ?
# start_freq = 500
# acc = 200 / 10 ms = 20 / ms


# starting_speed = 500
# acc_rate = 20 / ms
# speed_inc = 100
# time_interval = 10 ms
# target_speed = 4000
# steps_to_stop = ?
# 500/s * 0.01 = 5 steps
# 600/s * 0.01 = 6 steps
# 700/s * 0.01 = 7 steps
# 4000/s * 0.01 = 40 steps
# 5 + 7 + 9 + ... 40 = 5 + 2(n - 1)






# def decode_cmd(cmd):
#     l, r, d = cmd.split(',')
#     left_freq = abs(int(l))
#     right_freq = abs(int(r))
#     dur_ms = int(d)
#     left_dir = 1
#     if int(l) > 0:
#         left_dir = 0
#     right_dir = 1
#     if int(r) > 0:
#         right_dir = 0
#     return left_freq, left_dir, right_freq, right_dir, dur_ms

# async def processCmdQueue(q, leftStepper, rightStepper):
#     while True:
#         raw_cmd = await q.get()
#         left_freq, left_dir, right_freq, right_dir, dur_ms = decode_cmd(raw_cmd)

#         leftStepper.move(left_dir, left_freq)
#         rightStepper.move(right_dir, right_freq)

#         time.sleep_ms(dur_ms)

#         leftStepper.stop()
#         rightStepper.stop()

#         time.sleep_ms(500)

# async def main():
#     # connect to wifi access point
#     sta = network.WLAN(network.STA_IF)
#     sta.active(True)
#     sta.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
#     print(sta.ifconfig())

#     leftStepper = stepper.Stepper(config.LEFT_STEP_PIN, config.LEFT_DIR_PIN, config.LEFT_ENABLE_PIN)
#     rightStepper = stepper.Stepper(config.RIGHT_STEP_PIN, config.RIGHT_DIR_PIN, config.RIGHT_ENABLE_PIN)

#     q = Queue()

#     asyncio.create_task(processCmdQueue(q, leftStepper, rightStepper))

#     server = Server(q)
#     await server.run()

# try:
#     asyncio.run(main())
# finally:
#     asyncio.new_event_loop()  # Clear retained state
