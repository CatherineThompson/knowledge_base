import uasyncio as asyncio
from machine import Pin, PWM
import time
import math


class StepperPWM:

    def __init__(self, step_pin, dir_pin, enable_pin):
        self.pwm = PWM(Pin(step_pin))
        self.dir_pin = Pin(dir_pin, Pin.OUT)
        # self.enable_pin = Pin(enable_pin)

    def move(self, dir, freq):
        self.dir_pin(dir)
        # self.enable_pin.low()
        self.pwm.duty_u16(32768)
        self.pwm.freq(freq)

    def stop(self):
        self.pwm.deinit()
        # self.enable_pin.high()


class Stepper:
    delay_ratio = 100000
    max_steps_per_second = 400
    min_steps_per_second = 50
    acceleration = 10

    # TODO: control both motors with the same loop??
    def __init__(self, step_pin, dir_pin, enable_pin, step_size):
        self.step = Pin(step_pin, Pin.OUT)
        self.dir = Pin(dir_pin, Pin.OUT)
        # self.en = Pin(enable_pin, Pin.OUT)
        # self.en.high()
        max_freq = step_size * Stepper.max_steps_per_second
        min_freq = step_size * Stepper.min_steps_per_second
        self.max_delay = Stepper.speed_to_delay(max_freq)
        self.min_delay = Stepper.speed_to_delay(min_freq)

        # print(self.max_delay, self.min_delay)

    def dir(self, direction):
        if direction == 0:
            self.dir.low()
        elif direction == 1:
            self.dir.high()
        else:
            raise Exception("Only 1 or 0 accepted")
    def speed_to_delay(freq):
        return Stepper.delay_ratio / freq

    async def move(self, steps, ratio):
        # print(f"moving {steps} steps")
        # self.en.low()

        steps_to_stop = int((self.min_delay - self.max_delay) / self.acceleration)
        step = 0
        i = 0
        while step < steps:
            if i % ratio == 0:
                steps_left = steps - step
                if steps_to_stop >= steps_left:
                    delay = math.floor(min(self.max_delay + (steps_to_stop - steps_left) * self.acceleration, self.min_delay))
                else:
                    delay = math.floor(max(self.min_delay - step * self.acceleration, self.max_delay))

                self.step.high()
                time.sleep_us(delay)
                self.step.low()
                time.sleep_us(math.floor(delay/19))
                step += 1
            i += 1
            await asyncio.sleep(0)


        # self.en.high()
