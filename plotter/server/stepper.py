from machine import Pin, PWM
import time
import math
import config

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
  def __init__(self):
    self.step1 = Pin(config.LEFT_STEP_PIN, Pin.OUT)
    self.step2 = Pin(config.RIGHT_STEP_PIN, Pin.OUT)
    self.dir1 = Pin(config.LEFT_DIR_PIN, Pin.OUT)
    self.dir2 = Pin(config.RIGHT_DIR_PIN, Pin.OUT)
    # self.en = Pin(enable_pin, Pin.OUT)
    # self.en.high()
    max_freq = config.STEP_SIZE * 800 # 20000
    min_freq = config.STEP_SIZE * 100
    self.max_delay = Stepper.speed_to_delay(max_freq)
    self.min_delay = Stepper.speed_to_delay(min_freq)
    # change in ramp up/ramp down delay per step
    self.delay_acc = 0.25
    self.steps_to_stop = int((self.min_delay - self.max_delay) / self.delay_acc)

    print(self.max_delay, self.min_delay)
    print(self.steps_to_stop)
    print()

  def speed_to_delay(freq):
    return int(500000 / freq)

  def move(self, steps, l_dir, l_prd, r_dir, r_prd):
    self.dir1.value(l_dir)
    self.dir2.value(r_dir)
    steps_to_stop = min(self.steps_to_stop, int(steps/2))
    for i in range(steps):
      steps_left = steps - i - 1
      if steps_to_stop >= steps_left:
        delay = math.floor(min(self.max_delay + (steps_to_stop - steps_left) * self.delay_acc, self.min_delay))
      else:
        delay = math.floor(max(self.min_delay - i * self.delay_acc, self.max_delay))

      should_step_left = i%l_prd == 0
      should_step_right = i%r_prd == 0 

      if should_step_left:
        self.step1.high()
      if should_step_right:
        self.step2.high()

      time.sleep_us(delay)

      if should_step_left:
        self.step1.low()
      if should_step_right:
        self.step2.low()

      time.sleep_us(delay)
