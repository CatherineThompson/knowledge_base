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
  # TODO: control both motors with the same loop??
  def __init__(self, step_pin, dir_pin, enable_pin, step_size):
    self.step = Pin(step_pin, Pin.OUT)
    self.dir = Pin(dir_pin, Pin.OUT)
    # self.en = Pin(enable_pin, Pin.OUT)
    # self.en.high()
    max_freq = step_size * 600
    min_freq = step_size * 200 
    self.max_delay = Stepper.speed_to_delay(max_freq)
    self.min_delay = Stepper.speed_to_delay(min_freq)
    # change in ramp up/ramp down delay
    self.delay_acc = 20

    print(self.max_delay, self.min_delay)

  def speed_to_delay(freq):
    return 500000 / freq

  async def move(self, steps):
    # self.en.low()

    steps_to_stop = int((self.min_delay - self.max_delay) / self.delay_acc)
    for i in range(steps):
      steps_left = steps - i
      if steps_to_stop >= steps_left:
        delay = math.floor(min(self.max_delay + (steps_to_stop - steps_left) * self.delay_acc, self.min_delay))
      else:
        delay = math.floor(max(self.min_delay - i * self.delay_acc, self.max_delay))

      self.step.high()
      time.sleep_us(delay)
      self.step.low()
      time.sleep_us(delay)

    # self.en.high()
